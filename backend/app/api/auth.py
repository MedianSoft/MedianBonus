from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Security, status
from fastapi_jwt import JwtAuthorizationCredentials

from app.container.base import BaseContainer
from app.schema.auth import AuthLoginRequest, TokenResponse
from app.security.password import (
    access_security,
    ensure_refresh_not_revoked,
    get_refresh_security,
    refresh_security,
    revoked_refresh_jti,
)
from app.service.auth import AuthService
from app.util.exception_handler import RoleForbiddenError

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse,
)
@inject
async def create(
    data: AuthLoginRequest,
    service: AuthService = Depends(Provide[BaseContainer.auth.service]),  # type: ignore
) -> TokenResponse:
    return await service.get_jwt_token(data)


@router.post(
    "/refresh_token",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse,
)
def refresh(credentials: JwtAuthorizationCredentials = Security(get_refresh_security)) -> TokenResponse:
    ensure_refresh_not_revoked(credentials)

    access_token = access_security.create_access_token(subject=credentials.subject)
    refresh_token = refresh_security.create_refresh_token(subject=credentials.subject)
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.delete(
    "/logout",
    status_code=status.HTTP_200_OK,
)
def logout(credentials: JwtAuthorizationCredentials = Security(get_refresh_security)) -> None:
    ensure_refresh_not_revoked(credentials)
    if credentials.jti is not None:
        revoked_refresh_jti.add(credentials.jti)
    else:
        raise RoleForbiddenError

from fastapi import APIRouter, Depends, status, Security
from fastapi_jwt import JwtAuthorizationCredentials

from app.factoriy.service import get_auth_service
from app.schema.auth import AuthLoginRequest, TokenResponse
from app.security.password import refresh_security, ensure_refresh_not_revoked, revoked_refresh_jti, access_security
from app.service.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse,
)
async def create(
    data: AuthLoginRequest,
    service: AuthService = Depends(get_auth_service),
) -> TokenResponse:
    return await service.get_jwt_token(data)


@router.post(
    "/refresh_token",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse,
)
def refresh(credentials: JwtAuthorizationCredentials = Security(refresh_security)):
    ensure_refresh_not_revoked(credentials)

    access_token = access_security.create_access_token(subject=credentials.subject)
    refresh_token = refresh_security.create_refresh_token(subject=credentials.subject)
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.post(
    "/logout",
    status_code=status.HTTP_200_OK,
)
def logout(credentials: JwtAuthorizationCredentials = Security(refresh_security)):
    ensure_refresh_not_revoked(credentials)
    revoked_refresh_jti.add(credentials.jti)
    return {"ok": True}
import uuid

from fastapi import APIRouter, Depends, status
from fastapi_jwt import JwtAuthorizationCredentials

from app.factoriy.service import get_business_service
from app.schema.business import (
    BusinessCreateRequest,
    BusinessDeleteRequest,
    BusinessGetByEmailRequest,
    BusinessListResponse,
    BusinessResponse,
    BusinessUpdateRequest,
)
from app.service.business import BusinessService
from app.util.role_checker import require_roles

router = APIRouter(prefix="/business", tags=["business"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=BusinessResponse,
)
async def create(
    data: BusinessCreateRequest,
    service: BusinessService = Depends(get_business_service),
) -> BusinessResponse:
    return await service.create(data)


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=BusinessResponse,
)
async def update(
    data: BusinessUpdateRequest,
    service: BusinessService = Depends(get_business_service),
) -> BusinessResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    data: BusinessDeleteRequest,
    service: BusinessService = Depends(get_business_service),
) -> None:
    await service.delete(data)
    return


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=BusinessResponse,
)
async def get(
    id: uuid.UUID,  # noqa
    service: BusinessService = Depends(get_business_service),
) -> BusinessResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=BusinessListResponse,
)
async def get_all(
    service: BusinessService = Depends(get_business_service), _cred: JwtAuthorizationCredentials = Depends(require_roles("business"))
) -> BusinessListResponse:
    return await service.get_all()


@router.post(
    "/get_by_email",
    status_code=status.HTTP_200_OK,
    response_model=BusinessResponse,
)
async def get_by_email(
    data: BusinessGetByEmailRequest,
    service: BusinessService = Depends(get_business_service),
) -> BusinessResponse | None:
    return await service.get_by_email(data)

from fastapi import APIRouter, Depends, status

from backend.factories.service import get_business_service
from backend.schemas.business import (
    BusinessCreateRequest,
    BusinessDeleteRequest,
    BusinessGetByEmailRequest,
    BusinessGetByIDRequest,
    BusinessListResponse,
    BusinessResponse,
)
from backend.services.business import BusinessService

router = APIRouter(prefix="/business", tags=["business"])


# All APIs consist of POST methods due to the future need for RBAC and JWT verification.
# TODO: RBAC, JWT


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


@router.post(
    "/delete",
    status_code=status.HTTP_200_OK,
    response_model=BusinessResponse,
)
async def delete(
    data: BusinessDeleteRequest,
    service: BusinessService = Depends(get_business_service),
) -> BusinessResponse | None:
    return await service.delete(data)


@router.post(
    "/get",
    status_code=status.HTTP_200_OK,
    response_model=BusinessResponse,
)
async def get(
    data: BusinessGetByEmailRequest,
    service: BusinessService = Depends(get_business_service),
) -> BusinessResponse | None:
    return await service.get(data)


@router.post(
    "/get_by_id",
    status_code=status.HTTP_200_OK,
    response_model=BusinessResponse,
)
async def get_by_id(
    data: BusinessGetByIDRequest,
    service: BusinessService = Depends(get_business_service),
) -> BusinessResponse | None:
    return await service.get_by_id(data)


@router.post(
    "/get_all",
    status_code=status.HTTP_200_OK,
    response_model=BusinessListResponse,
)
async def get_all(
    service: BusinessService = Depends(get_business_service),
) -> BusinessListResponse:
    return await service.get_all()

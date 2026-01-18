from fastapi import APIRouter, Depends, status

from backend.factories.store import get_store_service
from backend.schemas.store import (
    StoreCreateRequest,
    StoreDeleteRequest,
    StoreGetByNameRequest,
    StoreListRequest,
    StoreListResponse,
    StoreResponse,
)
from backend.services.store import StoreService

router = APIRouter(prefix="/store", tags=["store"])


# All APIs consist of POST methods due to the future need for RBAC and JWT verification.
# TODO: RBAC, JWT


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=StoreResponse,
)
async def create(
    data: StoreCreateRequest,
    service: StoreService = Depends(get_store_service),
) -> StoreResponse:
    return await service.create(data)


@router.post(
    "/delete",
    status_code=status.HTTP_200_OK,
    response_model=StoreResponse,
)
async def delete(
    data: StoreDeleteRequest,
    service: StoreService = Depends(get_store_service),
) -> StoreResponse | None:
    return await service.delete(data)


@router.post(
    "/get_by_name",
    status_code=status.HTTP_200_OK,
    response_model=StoreResponse,
)
async def get_by_name(
    data: StoreGetByNameRequest,
    service: StoreService = Depends(get_store_service),
) -> StoreResponse | None:
    return await service.get_by_name(data)


@router.post(
    "/get_all",
    status_code=status.HTTP_200_OK,
    response_model=StoreListResponse,
)
async def get_all(
    data: StoreListRequest,
    service: StoreService = Depends(get_store_service),
) -> StoreListResponse:
    return await service.get_all(data)

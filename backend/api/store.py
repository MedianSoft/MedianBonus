import uuid

from fastapi import APIRouter, Depends, status

from backend.factories.service import get_store_service
from backend.schemas.store import (
    StoreAllByBusinessRequest,
    StoreCreateRequest,
    StoreDeleteRequest,
    StoreGetByNameInBusinessRequest,
    StoreListResponse,
    StoreResponse,
    StoreUpdateRequest,
)
from backend.services.store import StoreService

router = APIRouter(prefix="/store", tags=["store"])


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


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=StoreResponse,
)
async def update(
    data: StoreUpdateRequest,
    service: StoreService = Depends(get_store_service),
) -> StoreResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    data: StoreDeleteRequest,
    service: StoreService = Depends(get_store_service),
) -> None:
    await service.delete(data)
    return


@router.post(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=StoreResponse,
)
async def get(
    id: uuid.UUID,  # noqa
    service: StoreService = Depends(get_store_service),
) -> StoreResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=StoreListResponse,
)
async def get_all(
    service: StoreService = Depends(get_store_service),
) -> StoreListResponse:
    return await service.get_all()


@router.post(
    "/get_by_name_in_business",
    status_code=status.HTTP_200_OK,
    response_model=StoreResponse,
)
async def get_by_name_in_business(
    data: StoreGetByNameInBusinessRequest,
    service: StoreService = Depends(get_store_service),
) -> StoreResponse | None:
    return await service.get_by_name_in_business(data)


@router.post(
    "/get_all_by_business",
    status_code=status.HTTP_200_OK,
    response_model=StoreListResponse,
)
async def get_all_by_business(
    data: StoreAllByBusinessRequest,
    service: StoreService = Depends(get_store_service),
) -> StoreListResponse:
    return await service.get_all_by_business(data)

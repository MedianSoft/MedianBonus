import uuid

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.container.base import BaseContainer
from app.schema.store import (
    StoreAllByBusinessRequest,
    StoreCreateRequest,
    StoreDeleteRequest,
    StoreGetByNameInBusinessRequest,
    StoreListResponse,
    StoreResponse,
    StoreUpdateRequest,
)
from app.service.store import StoreService

router = APIRouter(prefix="/store", tags=["store"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=StoreResponse,
)
@inject
async def create(
    data: StoreCreateRequest,
    service: StoreService = Depends(Provide[BaseContainer.store.service]),  # type: ignore
) -> StoreResponse:
    return await service.create(data)


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=StoreResponse,
)
@inject
async def update(
    data: StoreUpdateRequest,
    service: StoreService = Depends(Provide[BaseContainer.store.service]),  # type: ignore
) -> StoreResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    data: StoreDeleteRequest,
    service: StoreService = Depends(Provide[BaseContainer.store.service]),  # type: ignore
) -> None:
    await service.delete(data)
    return


@router.post(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=StoreResponse,
)
@inject
async def get(
    id: uuid.UUID,  # noqa
    service: StoreService = Depends(Provide[BaseContainer.store.service]),  # type: ignore
) -> StoreResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=StoreListResponse,
)
@inject
async def get_all(
    service: StoreService = Depends(Provide[BaseContainer.store.service]),  # type: ignore
) -> StoreListResponse:
    return await service.get_all()


@router.post(
    "/get_by_name_in_business",
    status_code=status.HTTP_200_OK,
    response_model=StoreResponse,
)
@inject
async def get_by_name_in_business(
    data: StoreGetByNameInBusinessRequest,
    service: StoreService = Depends(Provide[BaseContainer.store.service]),  # type: ignore
) -> StoreResponse | None:
    return await service.get_by_name_in_business(data)


@router.post(
    "/get_all_by_business",
    status_code=status.HTTP_200_OK,
    response_model=StoreListResponse,
)
@inject
async def get_all_by_business(
    data: StoreAllByBusinessRequest,
    service: StoreService = Depends(Provide[BaseContainer.store.service]),  # type: ignore
) -> StoreListResponse:
    return await service.get_all_by_business(data)

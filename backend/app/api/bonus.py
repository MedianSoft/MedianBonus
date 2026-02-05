import uuid

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.container.base import BaseContainer
from app.schema.bonus import (
    BonusCreateRequest,
    BonusDeleteRequest,
    BonusGetAllByStore,
    BonusListResponse,
    BonusResponse,
    BonusUpdateRequest,
)
from app.service.bonus import BonusService

router = APIRouter(prefix="/bonus", tags=["bonus"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=BonusResponse,
)
@inject
async def create(
    data: BonusCreateRequest,
    service: BonusService = Depends(Provide[BaseContainer.bonus.service]),  # type: ignore
) -> BonusResponse:
    return await service.create(data)


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=BonusResponse,
)
@inject
async def update(
    data: BonusUpdateRequest,
    service: BonusService = Depends(Provide[BaseContainer.bonus.service]),  # type: ignore
) -> BonusResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    data: BonusDeleteRequest,
    service: BonusService = Depends(Provide[BaseContainer.bonus.service]),  # type: ignore
) -> None:
    await service.delete(data)
    return


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=BonusResponse,
)
@inject
async def get(
    id: uuid.UUID,  # noqa
    service: BonusService = Depends(Provide[BaseContainer.bonus.service]),  # type: ignore
) -> BonusResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=BonusListResponse,
)
@inject
async def get_all(
    service: BonusService = Depends(Provide[BaseContainer.bonus.service]),  # type: ignore
) -> BonusListResponse:
    return await service.get_all()


@router.post(
    "/get_all_by_store",
    status_code=status.HTTP_200_OK,
    response_model=BonusListResponse,
)
@inject
async def get_all_by_store(
    data: BonusGetAllByStore,
    service: BonusService = Depends(Provide[BaseContainer.bonus.service]),  # type: ignore
) -> BonusListResponse:
    return await service.get_all_by_store(data)

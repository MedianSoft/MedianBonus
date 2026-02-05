import uuid

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.container.base import BaseContainer
from app.schema.business import (
    BusinessCreateRequest,
    BusinessDeleteRequest,
    BusinessGetByEmailRequest,
    BusinessListResponse,
    BusinessResponse,
    BusinessUpdateRequest,
)
from app.service.business import BusinessService

router = APIRouter(prefix="/business", tags=["business"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=BusinessResponse,
)
@inject
async def create(
    data: BusinessCreateRequest,
    service: BusinessService = Depends(Provide[BaseContainer.business.service]),  # type: ignore
) -> BusinessResponse:
    return await service.create(data)


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=BusinessResponse,
)
@inject
async def update(
    data: BusinessUpdateRequest,
    service: BusinessService = Depends(Provide[BaseContainer.business.service]),  # type: ignore
) -> BusinessResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    data: BusinessDeleteRequest,
    service: BusinessService = Depends(Provide[BaseContainer.business.service]),  # type: ignore
) -> None:
    await service.delete(data)
    return


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=BusinessResponse,
)
@inject
async def get(
    id: uuid.UUID,  # noqa
    service: BusinessService = Depends(Provide[BaseContainer.business.service]),  # type: ignore
) -> BusinessResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=BusinessListResponse,
)
@inject
async def get_all(
    service: BusinessService = Depends(Provide[BaseContainer.business.service]),  # type: ignore
) -> BusinessListResponse:
    return await service.get_all()


@router.post(
    "/get_by_email",
    status_code=status.HTTP_200_OK,
    response_model=BusinessResponse,
)
@inject
async def get_by_email(
    data: BusinessGetByEmailRequest,
    service: BusinessService = Depends(Provide[BaseContainer.business.service]),  # type: ignore
) -> BusinessResponse | None:
    return await service.get_by_email(data)

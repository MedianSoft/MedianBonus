import uuid

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.container.base import BaseContainer
from app.schema.product import (
    ProductAllByStoreRequest,
    ProductCreateRequest,
    ProductDeleteRequest,
    ProductGetByNameInStoreRequest,
    ProductListResponse,
    ProductResponse,
    ProductUpdateRequest,
)
from app.service.product import ProductService

router = APIRouter(prefix="/product", tags=["product"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductResponse,
)
@inject
async def create(
    data: ProductCreateRequest,
    service: ProductService = Depends(Provide[BaseContainer.product.service]),  # type: ignore
) -> ProductResponse:
    return await service.create(data)


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ProductResponse,
)
@inject
async def update(
    data: ProductUpdateRequest,
    service: ProductService = Depends(Provide[BaseContainer.product.service]),  # type: ignore
) -> ProductResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    data: ProductDeleteRequest,
    service: ProductService = Depends(Provide[BaseContainer.product.service]),  # type: ignore
) -> None:
    await service.delete(data)
    return


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponse,
)
@inject
async def get(
    id: uuid.UUID,  # noqa
    service: ProductService = Depends(Provide[BaseContainer.product.service]),  # type: ignore
) -> ProductResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=ProductListResponse,
)
@inject
async def get_all(
    service: ProductService = Depends(Provide[BaseContainer.product.service]),  # type: ignore
) -> ProductListResponse:
    return await service.get_all()


@router.post(
    "/get_by_name_in_store",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponse,
)
@inject
async def get_by_name_in_store(
    data: ProductGetByNameInStoreRequest,
    service: ProductService = Depends(Provide[BaseContainer.product.service]),  # type: ignore
) -> ProductResponse | None:
    return await service.get_by_name_in_store(data)


@router.post(
    "/get_all_by_store",
    status_code=status.HTTP_200_OK,
    response_model=ProductListResponse,
)
@inject
async def get_all_by_store(
    data: ProductAllByStoreRequest,
    service: ProductService = Depends(Provide[BaseContainer.product.service]),  # type: ignore
) -> ProductListResponse:
    return await service.get_all_by_store(data)

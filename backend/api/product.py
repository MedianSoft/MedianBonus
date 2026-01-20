import uuid

from fastapi import APIRouter, Depends, status

from backend.factories.service import get_product_service
from backend.schemas.product import (
    ProductAllByStoreRequest,
    ProductCreateRequest,
    ProductDeleteRequest,
    ProductGetByNameInStoreRequest,
    ProductListResponse,
    ProductResponse,
    ProductUpdateRequest,
)
from backend.services.product import ProductService

router = APIRouter(prefix="/product", tags=["product"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductResponse,
)
async def create(
    data: ProductCreateRequest,
    service: ProductService = Depends(get_product_service),
) -> ProductResponse:
    return await service.create(data)


@router.patch(
    "/update",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ProductResponse,
)
async def update(
    data: ProductUpdateRequest,
    service: ProductService = Depends(get_product_service),
) -> ProductResponse | None:
    return await service.update(data)


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    data: ProductDeleteRequest,
    service: ProductService = Depends(get_product_service),
) -> None:
    await service.delete(data)
    return


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponse,
)
async def get(
    id: uuid.UUID,  # noqa
    service: ProductService = Depends(get_product_service),
) -> ProductResponse | None:
    return await service.get(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=ProductListResponse,
)
async def get_all(
    service: ProductService = Depends(get_product_service),
) -> ProductListResponse:
    return await service.get_all()


@router.post(
    "/get_by_name_in_store",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponse,
)
async def get_by_name_in_store(
    data: ProductGetByNameInStoreRequest,
    service: ProductService = Depends(get_product_service),
) -> ProductResponse | None:
    return await service.get_by_name_in_store(data)


@router.post(
    "/get_all_by_store",
    status_code=status.HTTP_200_OK,
    response_model=ProductListResponse,
)
async def get_all_by_store(
    data: ProductAllByStoreRequest,
    service: ProductService = Depends(get_product_service),
) -> ProductListResponse:
    return await service.get_all_by_store(data)

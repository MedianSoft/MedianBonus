from fastapi import APIRouter, Depends, status

from backend.factories.product import get_product_service
from backend.schemas.product import (
    ProductCreateRequest,
    ProductDeleteRequest,
    ProductGetByNameRequest,
    ProductListRequest,
    ProductListResponse,
    ProductResponse,
)
from backend.services.product import ProductService

router = APIRouter(prefix="/product", tags=["product"])


# All APIs consist of POST methods due to the future need for RBAC and JWT verification.
# TODO: RBAC, JWT


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


@router.post(
    "/delete",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponse,
)
async def delete(
    data: ProductDeleteRequest,
    service: ProductService = Depends(get_product_service),
) -> ProductResponse | None:
    return await service.delete(data)


@router.post(
    "/get_by_name",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponse,
)
async def get_by_name(
    data: ProductGetByNameRequest,
    service: ProductService = Depends(get_product_service),
) -> ProductResponse | None:
    return await service.get_by_name(data)


@router.post(
    "/get_all",
    status_code=status.HTTP_200_OK,
    response_model=ProductListResponse,
)
async def get_all(
    data: ProductListRequest,
    service: ProductService = Depends(get_product_service),
) -> ProductListResponse:
    return await service.get_all(data)

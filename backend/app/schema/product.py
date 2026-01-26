import uuid

from app.domain.product import ProductStatus
from app.domain.product.enum import Category
from app.schema.base import BaseRequest, BaseResponse


class ProductCreateRequest(BaseRequest):
    name: str
    store_id: uuid.UUID
    category: Category
    price: float


class ProductUpdateRequest(BaseRequest):
    id: uuid.UUID
    name: str | None
    category: Category | None
    price: float | None


class ProductDeleteRequest(BaseRequest):
    id: uuid.UUID


class ProductGetByNameInStoreRequest(BaseRequest):
    name: str
    store_id: uuid.UUID


class ProductAllByStoreRequest(BaseRequest):
    store_id: uuid.UUID


class ProductResponse(BaseResponse):
    id: uuid.UUID
    store_id: uuid.UUID
    name: str
    status: ProductStatus
    category: Category
    price: float


class ProductListResponse(BaseResponse):
    productes: list[ProductResponse]

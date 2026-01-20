import uuid

from pydantic import BaseModel

from backend.domain.product import ProductStatus
from backend.domain.product.enum import Category
from backend.schemas.base import BaseRequest


class ProductCreateRequest(BaseRequest):
    name: str
    store_id: uuid.UUID
    category: Category
    price: float


class ProductDeleteRequest(BaseRequest):
    id: uuid.UUID


class ProductUpdateRequest(BaseRequest):
    name: str
    new_name: str
    store_id: uuid.UUID
    category: Category
    status: ProductStatus
    price: float


class ProductGetByNameRequest(BaseRequest):
    name: str
    store_id: uuid.UUID


class ProductGetByIDRequest(BaseRequest):
    id: uuid.UUID


class ProductListRequest(BaseRequest):
    store_id: uuid.UUID


class ProductResponse(BaseModel):
    id: uuid.UUID
    store_id: uuid.UUID
    name: str
    status: ProductStatus
    category: Category
    price: float


class ProductListResponse(BaseModel):
    productes: list[ProductResponse]

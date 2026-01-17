import uuid

from pydantic import BaseModel

from backend.domain.product import ProductStatus
from backend.domain.product.enum import Category


class ProductCreateRequest(BaseModel):
    name: str
    store_id: uuid.UUID
    category: Category
    price: float


class ProductDeleteRequest(BaseModel):
    name: str
    store_id: uuid.UUID


class ProductUpdateRequest(BaseModel):
    name: str
    new_name: str
    store_id: uuid.UUID
    category: Category
    status: ProductStatus
    price: float


class ProductGetByNameRequest(BaseModel):
    name: str
    store_id: uuid.UUID


class ProductListRequest(BaseModel):
    store_id: uuid.UUID


class ProductResponse(BaseModel):
    id: uuid.UUID
    store_id: uuid.UUID
    name: str
    status: ProductStatus
    category: Category
    price: float

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    productes: list[ProductResponse]

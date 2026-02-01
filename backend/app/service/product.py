from typing import TYPE_CHECKING

from app.domain.base import Status
from app.domain.product import Product
from app.schema.product import (
    ProductListResponse,
    ProductResponse,
)
from app.util.exception_handler import AlreadyExistsError, NotFoundError

if TYPE_CHECKING:
    import uuid

    from app.domain.product import ProductRepository
    from app.schema.product import (
        ProductAllByStoreRequest,
        ProductCreateRequest,
        ProductDeleteRequest,
        ProductGetByNameInStoreRequest,
        ProductUpdateRequest,
    )


class ProductService:
    def __init__(self, repository: "ProductRepository"):
        self.repository = repository

    async def create(self, data: "ProductCreateRequest") -> ProductResponse:
        existing = await self.repository.get_by_name_in_store(name=data.name, store_id=data.store_id)
        if existing:
            raise AlreadyExistsError("Product")

        product = Product(
            name=data.name,
            store_id=data.store_id,
            category=data.category,
            price=data.price,
        )
        result = await self.repository.create(product)

        return ProductResponse.model_validate(result)

    async def update(self, data: "ProductUpdateRequest") -> ProductResponse:
        existing = await self.repository.get(Product, data.id)
        if not existing:
            raise NotFoundError("Product")

        if data.name:
            existing.name = data.name
        if data.category:
            existing.category = data.category
        if data.price:
            existing.price = data.price

        result = await self.repository.update(existing)

        return ProductResponse.model_validate(result)

    async def delete(self, data: "ProductDeleteRequest") -> None:
        existing = await self.repository.get(Product, data.id)
        if not existing:
            raise NotFoundError("Product")

        existing.status = Status.SUSPENDED
        _ = await self.repository.update(existing)

    async def get(self, id: "uuid.UUID") -> ProductResponse:  # noqa
        result = await self.repository.get(Product, id)
        if not result:
            raise NotFoundError("Product")

        return ProductResponse.model_validate(result)

    async def get_all(self) -> ProductListResponse:
        result = await self.repository.get_all(Product)
        if not result:
            raise NotFoundError("Product")

        return ProductListResponse(productes=[ProductResponse.model_validate(product) for product in result])

    async def get_by_name_in_store(self, data: "ProductGetByNameInStoreRequest") -> ProductResponse:
        result = await self.repository.get_by_name_in_store(name=data.name, store_id=data.store_id)
        if not result:
            raise NotFoundError("Product")

        return ProductResponse.model_validate(result)

    async def get_all_by_store(self, data: "ProductAllByStoreRequest") -> ProductListResponse:
        result = await self.repository.get_all_by_store(store_id=data.store_id)
        if not result:
            raise NotFoundError("Product")

        return ProductListResponse(productes=[ProductResponse.model_validate(product) for product in result])

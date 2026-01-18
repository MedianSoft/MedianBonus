from backend.domain.product import Product, ProductRepository, ProductStatus
from backend.factories.product import get_product_repository
from backend.schemas.product import (
    ProductCreateRequest,
    ProductDeleteRequest,
    ProductGetByNameRequest,
    ProductListRequest,
    ProductListResponse,
    ProductResponse,
    ProductUpdateRequest,
)
from backend.utils.exception_handler import AlreadyExistsError, NotFoundError


class ProductService:
    def __init__(self, repository: ProductRepository = get_product_repository()):
        self.repository = repository

    async def create(self, data: ProductCreateRequest) -> ProductResponse:
        existing = await self.repository.get_by_name(name=data.name, store_id=data.store_id)
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

    async def delete(self, data: ProductDeleteRequest) -> ProductResponse | None:
        existing = await self.repository.get_by_name(name=data.name, store_id=data.store_id)
        if not existing:
            raise NotFoundError("Product")

        existing.status = ProductStatus.REMOVED
        result = await self.repository.update(existing)

        return ProductResponse.model_validate(result)

    async def update(self, data: ProductUpdateRequest) -> ProductResponse | None:
        existing = await self.repository.get_by_name(name=data.name, store_id=data.store_id)
        if not existing:
            raise NotFoundError("Product")

        existing.status = data.status
        existing.name = data.name
        existing.category = data.category
        existing.price = data.price

        result = await self.repository.update(existing)

        return ProductResponse.model_validate(result)

    async def get_by_name(self, data: ProductGetByNameRequest) -> ProductResponse | None:
        result = await self.repository.get_by_name(name=data.name, store_id=data.store_id)
        if not result:
            raise NotFoundError("Product")

        return ProductResponse.model_validate(result)

    async def get_all(self, data: ProductListRequest) -> ProductListResponse:
        result = await self.repository.get_all(store_id=data.store_id)
        if not result:
            raise NotFoundError("Product")

        return ProductListResponse(productes=[ProductResponse.model_validate(product) for product in result])

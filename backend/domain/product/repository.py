import uuid

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.domain.product import Product, ProductStatus


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, product: Product) -> Product:
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def update(self, product: Product) -> Product:
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def get_by_name(self, name: str, store_id: uuid.UUID) -> Product | None:
        result = await self.session.execute(
            select(Product).where(
                and_(
                    Product.store_id == store_id,
                    Product.name == name,
                    Product.status != ProductStatus.REMOVED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_all(self, store_id: uuid.UUID) -> list[Product | None]:
        result = await self.session.execute(
            select(Product).where(
                and_(
                    Product.store_id == store_id,
                    Product.status != ProductStatus.REMOVED,
                )
            )
        )
        return list(result.scalars().all())

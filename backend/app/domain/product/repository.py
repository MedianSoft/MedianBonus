from typing import TYPE_CHECKING

from sqlalchemy import and_, select

from app.domain.base import Status
from app.domain.base.repository import BaseRepository
from app.domain.product import Product

if TYPE_CHECKING:
    import uuid


class ProductRepository(BaseRepository[Product]):
    async def get_by_name_in_store(
        self,
        name: str,
        store_id: "uuid.UUID",
    ) -> Product | None:
        result = await self.session.execute(
            select(Product).where(
                and_(
                    Product.store_id == store_id,
                    Product.name == name,
                    Product.status != Status.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_all_by_store(self, store_id: "uuid.UUID") -> list[Product]:
        result = await self.session.execute(
            select(Product).where(
                and_(
                    Product.store_id == store_id,
                    Product.status != Status.SUSPENDED,
                )
            )
        )
        return list(result.scalars().all())

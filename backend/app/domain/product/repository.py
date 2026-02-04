# mypy: disable-error-code=union-attr
from typing import TYPE_CHECKING

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import ensure_session
from app.domain.base import Status
from app.domain.base.repository import BaseRepository
from app.domain.product import Product

if TYPE_CHECKING:
    import uuid


class ProductRepository(BaseRepository[Product]):
    @staticmethod
    @ensure_session
    async def get_by_name_in_store(
        *, name: str, store_id: "uuid.UUID", session: AsyncSession | None = None
    ) -> Product | None:
        result = await session.execute(
            select(Product).where(
                and_(
                    Product.store_id == store_id,
                    Product.name == name,
                    Product.status != Status.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    @ensure_session
    async def get_all_by_store(*, store_id: "uuid.UUID", session: AsyncSession | None = None) -> list[Product]:
        result = await session.execute(
            select(Product).where(
                and_(
                    Product.store_id == store_id,
                    Product.status != Status.SUSPENDED,
                )
            )
        )
        return list(result.scalars().all())

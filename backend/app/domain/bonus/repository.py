# mypy: disable-error-code=union-attr
from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.operators import and_

from app.database.session import ensure_session
from app.domain.base.repository import BaseRepository
from app.domain.bonus import Bonus
from app.domain.store import Store

if TYPE_CHECKING:
    import uuid


class BonusRepository(BaseRepository[Bonus]):
    @staticmethod
    @ensure_session
    async def get_by_product(*, product_id: "uuid.UUID", session: AsyncSession | None = None) -> Bonus | None:
        result = await session.execute(select(Bonus).where(Bonus.product_id == product_id))
        return result.scalar_one_or_none()

    @staticmethod
    @ensure_session
    async def get_all_by_store(*, store_id: "uuid.UUID", session: AsyncSession | None = None) -> list[Bonus]:
        result = await session.execute(
            select(Bonus).where(
                and_(
                    Store.id == store_id,
                    Bonus.is_active,
                )
            )
        )
        return list(result.scalars().all())

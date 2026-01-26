from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.sql.operators import and_

from app.domain.base.repository import BaseRepository
from app.domain.bonus import Bonus
from app.domain.store import Store

if TYPE_CHECKING:
    import uuid


class BonusRepository(BaseRepository[Bonus]):
    async def get_by_product(self, product_id: "uuid.UUID") -> Bonus | None:
        result = await self.session.execute(select(Bonus).where(Bonus.product_id == product_id))
        return result.scalar_one_or_none()

    async def get_all_by_store(self, store_id: "uuid.UUID") -> list[Bonus]:
        result = await self.session.execute(
            select(Bonus).where(
                and_(
                    Store.id == store_id,
                    Bonus.is_active,
                )
            )
        )
        return list(result.scalars().all())

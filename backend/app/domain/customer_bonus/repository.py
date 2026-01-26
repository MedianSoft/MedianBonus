from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.operators import and_

from app.domain.bonus import Bonus

from .entity import CustomerBonus

if TYPE_CHECKING:
    import uuid


class CustomerBonusRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, entity: CustomerBonus) -> CustomerBonus:
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(self, entity: CustomerBonus) -> CustomerBonus:
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def get_by_customer_and_bonus(self, customer_id: "uuid.UUID", bonus_id: "uuid.UUID") -> CustomerBonus | None:
        result = await self.session.execute(
            select(CustomerBonus).where(
                and_(
                    CustomerBonus.customer_id == customer_id,
                    CustomerBonus.bonus_id == bonus_id,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_all_by_customer_in_store(
        self,
        customer_id: "uuid.UUID",
        store_id: "uuid.UUID",
    ) -> list[CustomerBonus]:
        result = await self.session.execute(
            select(CustomerBonus)
            .join(Bonus, Bonus.id == CustomerBonus.bonus_id)
            .where(
                and_(
                    CustomerBonus.customer_id == customer_id,
                    Bonus.store_id == store_id,
                )
            )
        )
        return list(result.scalars().all())

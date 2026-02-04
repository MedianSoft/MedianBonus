# mypy: disable-error-code=union-attr
from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.operators import and_

from app.database.session import ensure_session
from app.domain.bonus import Bonus

from .entity import CustomerBonus

if TYPE_CHECKING:
    import uuid


class CustomerBonusRepository:
    @staticmethod
    @ensure_session
    async def get_by_customer_and_bonus(
        *,
        customer_id: "uuid.UUID",
        bonus_id: "uuid.UUID",
        session: AsyncSession | None = None,
    ) -> CustomerBonus | None:
        result = await session.execute(
            select(CustomerBonus).where(
                and_(
                    CustomerBonus.customer_id == customer_id,
                    CustomerBonus.bonus_id == bonus_id,
                )
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    @ensure_session
    async def get_all_by_customer_in_store(
        *,
        customer_id: "uuid.UUID",
        store_id: "uuid.UUID",
        session: AsyncSession | None = None,
    ) -> list[CustomerBonus]:
        result = await session.execute(
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

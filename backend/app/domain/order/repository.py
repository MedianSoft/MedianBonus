# mypy: disable-error-code=union-attr
from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import ensure_session
from app.domain.base.repository import BaseRepository
from app.domain.order.entity import Order, OrderProduct

if TYPE_CHECKING:
    import uuid


class OrderRepository(BaseRepository[Order]):
    @staticmethod
    @ensure_session
    async def get_all_by_customer(*, customer_id: "uuid.UUID", session: AsyncSession | None = None) -> list[Order]:
        result = await session.execute(select(Order).where(Order.customer_id == customer_id))
        return list(result.scalars().all())

    @staticmethod
    @ensure_session
    async def get_all_by_store(*, store_id: "uuid.UUID", session: AsyncSession | None = None) -> list[Order]:
        result = await session.execute(select(Order).where(Order.store_id == store_id))
        return list(result.scalars().all())


class OrderProductRepository(BaseRepository[OrderProduct]):
    @staticmethod
    @ensure_session
    async def get_all_by_order_id(*, order_id: "uuid.UUID", session: AsyncSession | None = None) -> list[OrderProduct]:
        result = await session.execute(select(OrderProduct).where(OrderProduct.order_id == order_id))
        return list(result.scalars().all())

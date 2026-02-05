from typing import TYPE_CHECKING

from sqlalchemy import select

from app.domain.base.repository import BaseRepository
from app.domain.order.entity import Order, OrderProduct

if TYPE_CHECKING:
    import uuid


class OrderRepository(BaseRepository[Order]):
    async def get_all_by_customer(self, customer_id: "uuid.UUID") -> list[Order]:
        result = await self.session.execute(select(Order).where(Order.customer_id == customer_id))
        return list(result.scalars().all())

    async def get_all_by_store(self, store_id: "uuid.UUID") -> list[Order]:
        result = await self.session.execute(select(Order).where(Order.store_id == store_id))
        return list(result.scalars().all())


class OrderProductRepository(BaseRepository[OrderProduct]):
    async def get_all_by_order_id(self, order_id: "uuid.UUID") -> list[OrderProduct]:
        result = await self.session.execute(select(OrderProduct).where(OrderProduct.order_id == order_id))
        return list(result.scalars().all())

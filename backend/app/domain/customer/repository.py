from sqlalchemy import select

from app.domain.base.repository import BaseRepository
from app.domain.customer.entity import Customer


class CustomerRepository(BaseRepository[Customer]):
    async def get_by_phone(self, phone: str) -> Customer | None:
        result = await self.session.execute(select(Customer).where(Customer.phone == phone))
        return result.scalar_one_or_none()

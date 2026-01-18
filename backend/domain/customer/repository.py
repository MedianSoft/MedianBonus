from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.domain.customer.entity import Customer


class CustomerRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, customer: Customer) -> Customer:
        self.session.add(customer)
        await self.session.commit()
        await self.session.refresh(customer)
        return customer

    async def update(self, customer: Customer) -> Customer:
        await self.session.commit()
        await self.session.refresh(customer)
        return customer

    async def get_by_phone(self, phone: str) -> Customer | None:
        result = await self.session.execute(select(Customer).where(Customer.phone == phone))
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Customer | None]:
        result = await self.session.execute(select(Customer))
        return list(result.scalars().all())

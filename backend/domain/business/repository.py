from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.domain.business import Business


class BusinessRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, business: Business) -> Business:
        self.session.add(business)
        await self.session.commit()
        await self.session.refresh(business)
        return business

    async def get_by_email(self, email: str) -> Business | None:
        result = await self.session.execute(
            select(Business).where(Business.email == email)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Business | None]:
        result = await self.session.execute(select(Business))
        return list(result.scalars().all())

    async def update(self, business: Business) -> Business:
        await self.session.commit()
        await self.session.refresh(business)
        return business

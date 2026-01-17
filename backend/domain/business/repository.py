import uuid

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.domain.business import Business, BusinessStatus


class BusinessRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, business: Business) -> Business:
        self.session.add(business)
        await self.session.commit()
        await self.session.refresh(business)
        return business

    async def update(self, business: Business) -> Business:
        await self.session.commit()
        await self.session.refresh(business)
        return business

    async def get_by_email(self, email: str) -> Business | None:
        result = await self.session.execute(
            select(Business).where(
                and_(
                    Business.email == email,
                    Business.status != BusinessStatus.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_by_id(self, id: uuid.UUID) -> Business | None:
        result = await self.session.execute(
            select(Business).where(
                and_(
                    Business.id == id,
                    Business.status != BusinessStatus.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Business | None]:
        result = await self.session.execute(
            select(Business).where(Business.status != BusinessStatus.SUSPENDED)
        )
        return list(result.scalars().all())

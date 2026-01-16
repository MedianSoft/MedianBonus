from fastapi import Depends
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.domain.business import Business


class BusinessRepository:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.session = session

    async def get_by_email(self, email: EmailStr) -> Business | None:
        result = await self.session.execute(
            select(Business).where(Business.email == email)
        )
        return result.scalar_one_or_none()

    async def add(self, business: Business) -> Business:
        self.session.add(business)
        await self.session.commit()
        await self.session.refresh(business)
        return business

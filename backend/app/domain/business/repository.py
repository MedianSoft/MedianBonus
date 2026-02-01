from typing import TYPE_CHECKING

from sqlalchemy import and_, select

from app.domain.base import Status
from app.domain.base.repository import BaseRepository
from app.domain.business import Business

if TYPE_CHECKING:
    pass


class BusinessRepository(BaseRepository[Business]):
    async def get_by_email(self, email: str) -> Business | None:
        result = await self.session.execute(
            select(Business).where(
                and_(
                    Business.email == email,
                    Business.status != Status.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

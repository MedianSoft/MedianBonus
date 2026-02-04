# mypy: disable-error-code=union-attr
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import ensure_session
from app.domain.base import Status
from app.domain.base.repository import BaseRepository
from app.domain.business import Business


class BusinessRepository(BaseRepository[Business]):
    @staticmethod
    @ensure_session
    async def get_by_email(*, email: str, session: AsyncSession | None = None) -> Business | None:
        result = await session.execute(
            select(Business).where(
                and_(
                    Business.email == email,
                    Business.status != Status.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

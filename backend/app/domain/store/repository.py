# mypy: disable-error-code=union-attr
from typing import TYPE_CHECKING

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import ensure_session
from app.domain.base import Status
from app.domain.base.repository import BaseRepository
from app.domain.store import Store

if TYPE_CHECKING:
    import uuid


class StoreRepository(BaseRepository[Store]):
    @staticmethod
    @ensure_session
    async def get_by_name_in_business(
        *, name: str, business_id: "uuid.UUID", session: AsyncSession | None = None
    ) -> Store | None:
        result = await session.execute(
            select(Store).where(
                and_(
                    Store.business_id == business_id,
                    Store.name == name,
                    Store.status != Status.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    @ensure_session
    async def get_all_by_business(*, business_id: "uuid.UUID", session: AsyncSession | None = None) -> list[Store]:
        result = await session.execute(select(Store).where(Store.business_id == business_id))
        return list(result.scalars().all())

from typing import TYPE_CHECKING

from sqlalchemy import and_, select

from app.domain.base import Status
from app.domain.base.repository import BaseRepository
from app.domain.store import Store

if TYPE_CHECKING:
    import uuid


class StoreRepository(BaseRepository[Store]):
    async def get_by_name_in_business(
        self,
        name: str,
        business_id: "uuid.UUID",
    ) -> Store | None:
        result = await self.session.execute(
            select(Store).where(
                and_(
                    Store.business_id == business_id,
                    Store.name == name,
                    Store.status != Status.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_all_by_business(self, business_id: "uuid.UUID") -> list[Store]:
        result = await self.session.execute(select(Store).where(Store.business_id == business_id))
        return list(result.scalars().all())

from typing import TYPE_CHECKING

from sqlalchemy import select

from backend.domain.base.repository import BaseRepository
from backend.domain.bonus import Bonus

if TYPE_CHECKING:
    import uuid


class BonusRepository(BaseRepository):
    async def get(self, id: "uuid.UUID") -> Bonus | None:
        result = await self.session.execute(select(Bonus).where(Bonus.id == id))
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Bonus | None]:
        result = await self.session.execute(select(Bonus).where(Bonus.is_active))
        return list(result.scalars().all())

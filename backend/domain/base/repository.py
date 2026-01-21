from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.domain.base.entity import Entity

if TYPE_CHECKING:
    import uuid


class BaseRepository[ModelT: Entity]:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, model: type[ModelT], entity_id: "uuid.UUID") -> ModelT | None:
        result = await self.session.execute(select(model).where(model.id == entity_id))
        return result.scalar_one_or_none()

    async def get_all(self, model: type[ModelT]) -> list[ModelT]:
        result = await self.session.execute(select(model))
        return list(result.scalars().all())

    async def create(self, entity: ModelT) -> ModelT:
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(self, entity: ModelT) -> ModelT:
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

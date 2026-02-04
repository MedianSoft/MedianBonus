# mypy: disable-error-code=union-attr
from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.operators import and_

from app.database.session import ensure_session

from .entity import Base
from .enum import Status

if TYPE_CHECKING:
    import uuid


class BaseRepository[ModelT: Base]:
    @staticmethod
    @ensure_session
    async def get(*, model: type[ModelT], id: "uuid.UUID", session: AsyncSession | None = None) -> ModelT | None:
        result = await session.execute(
            select(model).where(
                and_(
                    model.id == id,
                    model.status != Status.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    @ensure_session
    async def get_all(*, model: type[ModelT], session: AsyncSession | None = None) -> list[ModelT]:
        result = await session.execute(select(model).where(model.status != Status.SUSPENDED))
        return list(result.scalars().all())

# mypy: disable-error-code=union-attr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import ensure_session
from app.domain.base.repository import BaseRepository
from app.domain.customer.entity import Customer


class CustomerRepository(BaseRepository[Customer]):
    @staticmethod
    @ensure_session
    async def get_by_phone(*, phone: str, session: AsyncSession | None = None) -> Customer | None:
        result = await session.execute(select(Customer).where(Customer.phone == phone))
        return result.scalar_one_or_none()

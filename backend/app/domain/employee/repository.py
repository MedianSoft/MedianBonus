# mypy: disable-error-code=union-attr
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import ensure_session
from app.domain.base import Status
from app.domain.base.repository import BaseRepository
from app.domain.employee import Employee


class EmployeeRepository(BaseRepository[Employee]):
    @staticmethod
    @ensure_session
    async def get_by_email(*, email: str, session: AsyncSession | None = None) -> Employee | None:
        result = await session.execute(
            select(Employee).where(
                and_(
                    Employee.email == email,
                    Employee.status != Status.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

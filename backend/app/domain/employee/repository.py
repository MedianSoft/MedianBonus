from typing import TYPE_CHECKING

from sqlalchemy import and_, select

from app.domain.base import Status
from app.domain.base.repository import BaseRepository
from app.domain.employee import Employee

if TYPE_CHECKING:
    pass


class EmployeeRepository(BaseRepository[Employee]):
    async def get_by_email(self, email: str) -> Employee | None:
        result = await self.session.execute(
            select(Employee).where(
                and_(
                    Employee.email == email,
                    Employee.status != Status.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

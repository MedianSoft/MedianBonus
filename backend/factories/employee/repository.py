from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.session import get_db
from backend.domain.employee import EmployeeRepository


def get_employee_repository(
    session: AsyncSession = Depends(get_db),
) -> EmployeeRepository:
    return EmployeeRepository(session=session)

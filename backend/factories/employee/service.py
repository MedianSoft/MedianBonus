from fastapi import Depends

from backend.domain.employee import EmployeeRepository
from backend.services.employee import EmployeeService

from .repository import get_employee_repository


def get_employee_service(
    repository: EmployeeRepository = Depends(get_employee_repository),
) -> EmployeeService:
    return EmployeeService(repository)

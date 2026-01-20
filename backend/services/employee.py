from backend.domain.employee import Employee, EmployeeRepository, EmployeeStatus
from backend.factories.repository import get_employee_repository
from backend.schemas.employee import (
    EmployeeCreateRequest,
    EmployeeDeleteRequest,
    EmployeeGetByEmailRequest,
    EmployeeGetByIDRequest,
    EmployeeListResponse,
    EmployeeResponse,
)
from backend.security import hash_password
from backend.utils.exception_handler import AlreadyExistsError, NotFoundError


class EmployeeService:
    def __init__(self, repository: EmployeeRepository = get_employee_repository()):
        self.repository = repository

    async def create(self, data: EmployeeCreateRequest) -> EmployeeResponse:
        existing = await self.repository.get(str(data.email))
        if existing:
            raise AlreadyExistsError("Email")

        employee = Employee(
            name=data.name,
            email=str(data.email),
            password_hash=hash_password(data.password),
            business_id=data.business_id,
        )
        result = await self.repository.create(employee)

        return EmployeeResponse.model_validate(result)

    async def delete(self, data: EmployeeDeleteRequest) -> EmployeeResponse | None:
        existing = await self.repository.get_by_id(data.id)
        if not existing:
            raise NotFoundError("Employee")

        existing.status = EmployeeStatus.SUSPENDED
        result = await self.repository.update(existing)

        return EmployeeResponse.model_validate(result)

    async def get(self, data: EmployeeGetByEmailRequest) -> EmployeeResponse | None:
        result = await self.repository.get(str(data.email))
        if not result:
            raise NotFoundError("Employee")

        return EmployeeResponse.model_validate(result)

    async def get_by_id(self, data: EmployeeGetByIDRequest) -> EmployeeResponse | None:
        result = await self.repository.get_by_id(data.id)
        if not result:
            raise NotFoundError("Employee")

        return EmployeeResponse.model_validate(result)

    async def get_all(self) -> EmployeeListResponse:
        result = await self.repository.get_all()
        if not result:
            raise NotFoundError("Employeees")

        return EmployeeListResponse(employeees=[EmployeeResponse.model_validate(employee) for employee in result])

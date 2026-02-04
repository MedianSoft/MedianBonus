from typing import TYPE_CHECKING

from app.database.session import async_session_manager
from app.domain.base import Status
from app.domain.employee import Employee
from app.schema.employee import (
    EmployeeListResponse,
    EmployeeResponse,
)
from app.security import hash_password
from app.util.exception_handler import AlreadyExistsError, NotFoundError

if TYPE_CHECKING:
    import uuid

    from app.domain.employee import EmployeeRepository
    from app.schema.employee import (
        EmployeeCreateRequest,
        EmployeeDeleteRequest,
        EmployeeGetByEmailRequest,
        EmployeeUpdateRequest,
    )


class EmployeeService:
    def __init__(self, repository: "EmployeeRepository"):
        self.repository = repository

    async def create(self, data: "EmployeeCreateRequest") -> EmployeeResponse:
        async with async_session_manager() as session:
            existing = await self.repository.get_by_email(email=str(data.email), session=session)
            if existing:
                raise AlreadyExistsError("Email")

            employee = Employee(
                name=data.name,
                email=str(data.email),
                password_hash=hash_password(data.password),
                business_id=data.business_id,
            )
            session.add(employee)
            await session.flush()
            result = await self.repository.get_by_email(email=str(data.email), session=session)

            return EmployeeResponse.model_validate(result)

    async def update(self, data: "EmployeeUpdateRequest") -> EmployeeResponse:
        async with async_session_manager() as session:
            existing = await self.repository.get(Employee, data.id, session)
            if not existing:
                raise NotFoundError("Employee")

            if data.name:
                existing.name = data.name
            if data.email:
                existing.email = str(data.email)
            if data.password:
                existing.password_hash = hash_password(data.password)

            return EmployeeResponse.model_validate(existing)

    async def delete(self, data: "EmployeeDeleteRequest") -> None:
        async with async_session_manager() as session:
            existing = await self.repository.get(Employee, data.id, session)
            if not existing:
                raise NotFoundError("Employee")

            existing.status = Status.SUSPENDED

    async def get(self, id: "uuid.UUID") -> EmployeeResponse:  # noqa
        result = await self.repository.get(Employee, id)
        if not result:
            raise NotFoundError("Employee")

        return EmployeeResponse.model_validate(result)

    async def get_all(self) -> EmployeeListResponse:
        result = await self.repository.get_all(Employee)
        if not result:
            raise NotFoundError("Employeees")

        return EmployeeListResponse(employeees=[EmployeeResponse.model_validate(employee) for employee in result])

    async def get_by_email(self, data: "EmployeeGetByEmailRequest") -> EmployeeResponse:
        result = await self.repository.get_by_email(str(data.email))
        if not result:
            raise NotFoundError("Employee")

        return EmployeeResponse.model_validate(result)

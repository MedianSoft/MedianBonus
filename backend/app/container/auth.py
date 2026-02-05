from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.business import BusinessRepository
from app.domain.employee import EmployeeRepository
from app.service.auth import AuthService


class AuthContainer(containers.DeclarativeContainer):
    session: providers.Dependency[AsyncSession] = providers.Dependency()

    business_repository = providers.Factory(
        BusinessRepository,
        session=session,
    )

    employee_repository = providers.Factory(
        EmployeeRepository,
        session=session,
    )

    service = providers.Factory(
        AuthService,
        business_repository=business_repository,
        employee_repository=employee_repository,
    )

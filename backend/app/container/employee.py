from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.employee import EmployeeRepository
from app.service.employee import EmployeeService


class EmployeeContainer(containers.DeclarativeContainer):
    session: providers.Dependency[AsyncSession] = providers.Dependency()

    repository = providers.Factory(
        EmployeeRepository,
        session=session,
    )

    service = providers.Factory(
        EmployeeService,
        repository=repository,
    )

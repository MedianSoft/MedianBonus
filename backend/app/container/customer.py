from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.customer import CustomerRepository
from app.service.customer import CustomerService


class CustomerContainer(containers.DeclarativeContainer):
    session: providers.Dependency[AsyncSession] = providers.Dependency()

    repository = providers.Factory(
        CustomerRepository,
        session=session,
    )

    service = providers.Factory(
        CustomerService,
        repository=repository,
    )

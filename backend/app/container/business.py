from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.business import BusinessRepository
from app.service.business import BusinessService


class BusinessContainer(containers.DeclarativeContainer):
    session: providers.Dependency[AsyncSession] = providers.Dependency()

    repository = providers.Factory(
        BusinessRepository,
        session=session,
    )

    service = providers.Factory(
        BusinessService,
        repository=repository,
    )

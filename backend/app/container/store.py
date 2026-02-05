from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.store import StoreRepository
from app.service.store import StoreService


class StoreContainer(containers.DeclarativeContainer):
    session: providers.Dependency[AsyncSession] = providers.Dependency()

    repository = providers.Factory(
        StoreRepository,
        session=session,
    )

    service = providers.Factory(
        StoreService,
        repository=repository,
    )

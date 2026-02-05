from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.bonus import BonusRepository
from app.service.bonus import BonusService


class BonusContainer(containers.DeclarativeContainer):
    session: providers.Dependency[AsyncSession] = providers.Dependency()

    repository = providers.Factory(
        BonusRepository,
        session=session,
    )

    service = providers.Factory(
        BonusService,
        repository=repository,
    )

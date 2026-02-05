from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.product import ProductRepository
from app.service.product import ProductService


class ProductContainer(containers.DeclarativeContainer):
    session: providers.Dependency[AsyncSession] = providers.Dependency()

    repository = providers.Factory(
        ProductRepository,
        session=session,
    )

    service = providers.Factory(
        ProductService,
        repository=repository,
    )

from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.bonus import BonusRepository
from app.domain.customer import CustomerRepository
from app.domain.customer_bonus import CustomerBonusRepository
from app.domain.order import OrderProductRepository, OrderRepository
from app.domain.product import ProductRepository
from app.service.order import OrderService


class OrderContainer(containers.DeclarativeContainer):
    session: providers.Dependency[AsyncSession] = providers.Dependency()

    order_repository = providers.Factory(OrderRepository, session=session)
    order_product_repository = providers.Factory(OrderProductRepository, session=session)
    bonus_repository = providers.Factory(BonusRepository, session=session)
    product_repository = providers.Factory(ProductRepository, session=session)
    customer_bonus_repository = providers.Factory(CustomerBonusRepository, session=session)
    customer_repository = providers.Factory(CustomerRepository, session=session)

    service = providers.Factory(
        OrderService,
        order_repository=order_repository,
        order_product_repository=order_product_repository,
        bonus_repository=bonus_repository,
        product_repository=product_repository,
        customer_bonus_repository=customer_bonus_repository,
        customer_repository=customer_repository,
    )

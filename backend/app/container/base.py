from dependency_injector import containers, providers

from app.container.auth import AuthContainer
from app.container.bonus import BonusContainer
from app.container.business import BusinessContainer
from app.container.customer import CustomerContainer
from app.container.employee import EmployeeContainer
from app.container.order import OrderContainer
from app.container.product import ProductContainer
from app.container.store import StoreContainer
from app.database.session import session_scope


class BaseContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.auth",
            "app.api.bonus",
            "app.api.business",
            "app.api.customer",
            "app.api.employee",
            "app.api.order",
            "app.api.product",
            "app.api.store",
        ]
    )

    session = providers.Resource(session_scope)

    auth = providers.Container(AuthContainer, session=session)
    bonus = providers.Container(BonusContainer, session=session)
    business = providers.Container(BusinessContainer, session=session)
    customer = providers.Container(CustomerContainer, session=session)
    employee = providers.Container(EmployeeContainer, session=session)
    order = providers.Container(OrderContainer, session=session)
    product = providers.Container(ProductContainer, session=session)
    store = providers.Container(StoreContainer, session=session)

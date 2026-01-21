from functools import lru_cache
from typing import TYPE_CHECKING

from fastapi import Depends

from backend.domain.customer_bonus import CustomerBonusRepository
from backend.domain.order import OrderProductRepository
from backend.factoriy.repository import (
    get_bonus_repository,
    get_business_repository,
    get_customer_bonus_repository,
    get_customer_repository,
    get_employee_repository,
    get_order_product_repository,
    get_order_repository,
    get_product_repository,
    get_store_repository,
)
from backend.service.bonus import BonusService
from backend.service.business import BusinessService
from backend.service.customer import CustomerService
from backend.service.employee import EmployeeService
from backend.service.order import OrderService
from backend.service.product import ProductService
from backend.service.store import StoreService

if TYPE_CHECKING:
    from backend.domain.bonus import BonusRepository
    from backend.domain.business import BusinessRepository
    from backend.domain.customer import CustomerRepository
    from backend.domain.employee import EmployeeRepository
    from backend.domain.order import OrderRepository
    from backend.domain.product import ProductRepository
    from backend.domain.store import StoreRepository


@lru_cache
def get_business_service(
    repository: "BusinessRepository" = Depends(get_business_repository),
) -> BusinessService:
    return BusinessService(repository)


@lru_cache
def get_customer_service(
    repository: "CustomerRepository" = Depends(get_customer_repository),
) -> CustomerService:
    return CustomerService(repository)


@lru_cache
def get_employee_service(
    repository: "EmployeeRepository" = Depends(get_employee_repository),
) -> EmployeeService:
    return EmployeeService(repository)


@lru_cache
def get_product_service(
    repository: "ProductRepository" = Depends(get_product_repository),
) -> ProductService:
    return ProductService(repository)


@lru_cache
def get_store_service(
    repository: "StoreRepository" = Depends(get_store_repository),
) -> StoreService:
    return StoreService(repository)


@lru_cache
def get_bonus_service(
    repository: "BonusRepository" = Depends(get_bonus_repository),
) -> BonusService:
    return BonusService(repository)


@lru_cache
def get_order_service(
    order_repository: "OrderRepository" = Depends(get_order_repository),
    order_product_repository: "OrderProductRepository" = Depends(get_order_product_repository),
    product_repository: "ProductRepository" = Depends(get_product_repository),
    bonus_repository: "BonusRepository" = Depends(get_bonus_repository),
    customer_repository: "CustomerRepository" = Depends(get_customer_repository),
    customer_bonus_repository: "CustomerBonusRepository" = Depends(get_customer_bonus_repository),
) -> OrderService:
    return OrderService(
        order_repository=order_repository,
        order_product_repository=order_product_repository,
        product_repository=product_repository,
        bonus_repository=bonus_repository,
        customer_bonus_repository=customer_bonus_repository,
        customer_repository=customer_repository,
    )

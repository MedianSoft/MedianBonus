from functools import lru_cache
from typing import TYPE_CHECKING

from fastapi import Depends

from app.domain.customer_bonus import CustomerBonusRepository
from app.domain.order import OrderProductRepository
from app.factoriy.repository import (
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
from app.service.auth import AuthService
from app.service.bonus import BonusService
from app.service.business import BusinessService
from app.service.customer import CustomerService
from app.service.employee import EmployeeService
from app.service.order import OrderService
from app.service.product import ProductService
from app.service.store import StoreService

if TYPE_CHECKING:
    from app.domain.bonus import BonusRepository
    from app.domain.business import BusinessRepository
    from app.domain.customer import CustomerRepository
    from app.domain.employee import EmployeeRepository
    from app.domain.order import OrderRepository
    from app.domain.product import ProductRepository
    from app.domain.store import StoreRepository


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


@lru_cache
def get_auth_service(
    business_repository: "BusinessRepository" = Depends(get_business_repository),
    employee_repository: "EmployeeRepository" = Depends(get_employee_repository)
) -> AuthService:
    return AuthService(
        business_repository=business_repository,
        employee_repository=employee_repository
    )

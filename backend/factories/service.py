from functools import lru_cache
from typing import TYPE_CHECKING

from fastapi import Depends

from backend.factories.repository import (
    get_bonus_repository,
    get_business_repository,
    get_customer_repository,
    get_employee_repository,
    get_product_repository,
    get_store_repository,
)
from backend.services.bonus import BonusService
from backend.services.business import BusinessService
from backend.services.customer import CustomerService
from backend.services.employee import EmployeeService
from backend.services.product import ProductService
from backend.services.store import StoreService

if TYPE_CHECKING:
    from backend.domain.bonus import BonusRepository
    from backend.domain.business import BusinessRepository
    from backend.domain.customer import CustomerRepository
    from backend.domain.employee import EmployeeRepository
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

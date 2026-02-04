from functools import lru_cache

from app.domain.bonus import BonusRepository
from app.domain.business import BusinessRepository
from app.domain.customer import CustomerRepository
from app.domain.customer_bonus import CustomerBonusRepository
from app.domain.employee import EmployeeRepository
from app.domain.order import OrderProductRepository, OrderRepository
from app.domain.product import ProductRepository
from app.domain.store import StoreRepository


@lru_cache
def get_business_repository() -> BusinessRepository:
    return BusinessRepository()


@lru_cache
def get_customer_repository() -> CustomerRepository:
    return CustomerRepository()


@lru_cache
def get_employee_repository() -> EmployeeRepository:
    return EmployeeRepository()


@lru_cache
def get_product_repository() -> ProductRepository:
    return ProductRepository()


@lru_cache
def get_store_repository() -> StoreRepository:
    return StoreRepository()


@lru_cache
def get_bonus_repository() -> BonusRepository:
    return BonusRepository()


@lru_cache
def get_customer_bonus_repository() -> CustomerBonusRepository:
    return CustomerBonusRepository()


@lru_cache
def get_order_repository() -> OrderRepository:
    return OrderRepository()


@lru_cache
def get_order_product_repository() -> OrderProductRepository:
    return OrderProductRepository()

from functools import lru_cache
from typing import TYPE_CHECKING

from fastapi import Depends

from app.database.session import get_db
from app.domain.bonus import BonusRepository
from app.domain.business import BusinessRepository
from app.domain.customer import CustomerRepository
from app.domain.customer_bonus import CustomerBonusRepository
from app.domain.employee import EmployeeRepository
from app.domain.order import OrderProductRepository, OrderRepository
from app.domain.product import ProductRepository
from app.domain.store import StoreRepository

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@lru_cache
def get_business_repository(
    session: "AsyncSession" = Depends(get_db),
) -> BusinessRepository:
    return BusinessRepository(session=session)


@lru_cache
def get_customer_repository(
    session: "AsyncSession" = Depends(get_db),
) -> CustomerRepository:
    return CustomerRepository(session=session)


@lru_cache
def get_employee_repository(
    session: "AsyncSession" = Depends(get_db),
) -> EmployeeRepository:
    return EmployeeRepository(session=session)


@lru_cache
def get_product_repository(
    session: "AsyncSession" = Depends(get_db),
) -> ProductRepository:
    return ProductRepository(session=session)


@lru_cache
def get_store_repository(
    session: "AsyncSession" = Depends(get_db),
) -> StoreRepository:
    return StoreRepository(session=session)


@lru_cache
def get_bonus_repository(
    session: "AsyncSession" = Depends(get_db),
) -> BonusRepository:
    return BonusRepository(session=session)


@lru_cache
def get_customer_bonus_repository(
    session: "AsyncSession" = Depends(get_db),
) -> CustomerBonusRepository:
    return CustomerBonusRepository(session=session)


@lru_cache
def get_order_repository(
    session: "AsyncSession" = Depends(get_db),
) -> OrderRepository:
    return OrderRepository(session=session)


@lru_cache
def get_order_product_repository(
    session: "AsyncSession" = Depends(get_db),
) -> OrderProductRepository:
    return OrderProductRepository(session=session)

from functools import lru_cache
from typing import TYPE_CHECKING

from fastapi import Depends

from backend.database.session import get_db
from backend.domain.bonus import BonusRepository
from backend.domain.business import BusinessRepository
from backend.domain.customer import CustomerRepository
from backend.domain.employee import EmployeeRepository
from backend.domain.product import ProductRepository
from backend.domain.store import StoreRepository

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

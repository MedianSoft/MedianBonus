from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.session import get_db
from backend.domain.customer.repository import CustomerRepository


def get_customer_repository(
    session: AsyncSession = Depends(get_db),
) -> CustomerRepository:
    return CustomerRepository(session=session)

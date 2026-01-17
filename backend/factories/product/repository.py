from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.session import get_db
from backend.domain.product.repository import ProductRepository


def get_product_repository(
    session: AsyncSession = Depends(get_db),
) -> ProductRepository:
    return ProductRepository(session=session)

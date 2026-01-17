from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.session import get_db
from backend.domain.store.repository import StoreRepository


def get_store_repository(
    session: AsyncSession = Depends(get_db),
) -> StoreRepository:
    return StoreRepository(session=session)

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.session import get_db
from backend.domain.business import BusinessRepository


def get_business_repository(
    session: AsyncSession = Depends(get_db),
) -> BusinessRepository:
    return BusinessRepository(session=session)

import uuid

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.domain.store import StoreStatus, Store


class StoreRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, store: Store) -> Store:
        self.session.add(store)
        await self.session.commit()
        await self.session.refresh(store)
        return store

    async def update(self, store: Store) -> Store:
        await self.session.commit()
        await self.session.refresh(store)
        return store

    async def get_by_name(self, name: str, business_id: uuid.UUID) -> Store | None:
        result = await self.session.execute(
            select(Store).where(
                and_(
                    Store.business_id == business_id,
                    Store.name == name,
                    Store.status != StoreStatus.SUSPENDED,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_all(self, business_id: uuid.UUID) -> list[Store | None]:
        result = await self.session.execute(
            select(Store).where(
                and_(
                    Store.business_id == business_id,
                    Store.status != StoreStatus.SUSPENDED,
                )
            )
        )
        return list(result.scalars().all())

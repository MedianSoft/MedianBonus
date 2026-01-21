# ruff: noqa: F401
# noinspection PyUnresolvedReferences
from backend.domain.base import Entity

# noinspection PyUnresolvedReferences
from backend.domain.bonus import Bonus, BonusType

# noinspection PyUnresolvedReferences
from backend.domain.business import Business, BusinessStatus

# noinspection PyUnresolvedReferences
from backend.domain.customer import Customer, CustomerBonus

# noinspection PyUnresolvedReferences
from backend.domain.product import Product, ProductStatus

# noinspection PyUnresolvedReferences
from backend.domain.store import Store, StoreStatus

from .session import engine


async def init_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Entity.metadata.create_all)


# for early dev purposes only
async def drop_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Entity.metadata.drop_all)

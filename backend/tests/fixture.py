import os
from collections.abc import AsyncGenerator

import pytest
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from backend.domain.base import Base

load_dotenv()
TEST_DB_DSN = os.getenv("TEST_DB_DSN", "sqlite:///:memory:")
engine = create_async_engine(TEST_DB_DSN, echo=False)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@pytest.fixture(scope="session")
async def init_db() -> AsyncGenerator[None]:
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    yield
    await engine.dispose()

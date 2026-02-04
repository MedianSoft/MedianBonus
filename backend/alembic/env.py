# ruff: noqa: F401
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool

from app.domain.base import Base

# noinspection PyUnresolvedReferences
from app.domain.bonus import Bonus, BonusType

# noinspection PyUnresolvedReferences
from app.domain.business import Business

# noinspection PyUnresolvedReferences
from app.domain.customer import Customer

# noinspection PyUnresolvedReferences
from app.domain.customer_bonus import CustomerBonus

# noinspection PyUnresolvedReferences
from app.domain.employee import Employee

# noinspection PyUnresolvedReferences
from app.domain.order import Order, OrderProduct

# noinspection PyUnresolvedReferences
from app.domain.product import Product

# noinspection PyUnresolvedReferences
from app.domain.store import Store
from app.setting.database import database_settings

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

config.set_main_option("sqlalchemy.url", database_settings.dsn)


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    from sqlalchemy.ext.asyncio import create_async_engine

    url = config.get_main_option("sqlalchemy.url")
    if url.startswith("sqlite://"):
        url = url.replace("sqlite://", "sqlite+aiosqlite://", 1)
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+asyncpg://", 1)

    connectable = create_async_engine(
        url,
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio

    asyncio.run(run_migrations_online())

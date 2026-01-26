import os
from logging.config import fileConfig

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import pool

from app.domain.base import Base
# noinspection PyUnresolvedReferences
from app.domain.bonus import Bonus, BonusType
# noinspection PyUnresolvedReferences
from app.domain.business import Business, BusinessStatus
# noinspection PyUnresolvedReferences
from app.domain.customer import Customer, CustomerStatus
# noinspection PyUnresolvedReferences
from app.domain.customer_bonus import CustomerBonus
# noinspection PyUnresolvedReferences
from app.domain.employee import Employee, EmployeeStatus
# noinspection PyUnresolvedReferences
from app.domain.order import Order, OrderProduct, OrderStatus
# noinspection PyUnresolvedReferences
from app.domain.product import Product, ProductStatus
# noinspection PyUnresolvedReferences
from app.domain.store import Store, StoreStatus


config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"))

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = "localhost"
DB_PORT = os.getenv("DB_PORT_EXTERNAL")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(f">>> {DATABASE_URL}")
config.set_main_option("sqlalchemy.url", DATABASE_URL)


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

    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url").replace("postgresql://", "postgresql+asyncpg://"),
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

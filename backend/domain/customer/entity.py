import uuid

from sqlalchemy import ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import TimestampMixin


class Customer(TimestampMixin):
    __tablename__ = "customers"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    name: Mapped[str] = mapped_column(String(63))

    phone: Mapped[str] = mapped_column(unique=True, index=True)


class CustomerGift(TimestampMixin):
    __tablename__ = "customer_product"

    customer_id: Mapped[UUID] = mapped_column(ForeignKey("customers.id"))

    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"))

    count: Mapped[int] = mapped_column(default=0)


class CustomerPoints(TimestampMixin):
    __tablename__ = "customer_points"

    customer_id: Mapped[UUID] = mapped_column(
        ForeignKey("customers.id"),
        primary_key=True,
    )

    store_id: Mapped[UUID] = mapped_column(
        ForeignKey("stores.id"),
        primary_key=True,
    )

    points: Mapped[int] = mapped_column(default=0)

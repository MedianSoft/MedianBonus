import uuid

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import TimestampMixin


class Customer(TimestampMixin):
    __tablename__ = "customers"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(String(63))

    phone: Mapped[str] = mapped_column(unique=True, index=True)


class CustomerGift(TimestampMixin):
    __tablename__ = "customer_gift"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("customers.id"),
        UUID(as_uuid=True),
        primary_key=True,
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("products.id"),
        UUID(as_uuid=True),
        primary_key=True,
    )

    count: Mapped[int] = mapped_column(default=0)


class CustomerPoints(TimestampMixin):
    __tablename__ = "customer_points"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("customers.id"),
        UUID(as_uuid=True),
        primary_key=True,
    )

    store_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("stores.id"),
        UUID(as_uuid=True),
        primary_key=True,
    )

    points: Mapped[int] = mapped_column(default=0)

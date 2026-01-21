import uuid

from sqlalchemy import UUID, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.domain.base import Base, Entity

from .enum import CustomerStatus


class Customer(Entity):
    __tablename__ = "customers"

    name: Mapped[str] = mapped_column(String(63))

    phone: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)

    status: Mapped[CustomerStatus] = mapped_column(
        Enum(CustomerStatus, name="customer_status"),
        nullable=False,
        default=CustomerStatus.ACTIVATED,
    )


class CustomerBonus(Base):
    __tablename__ = "customer_bonus"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("customers.id"),
        primary_key=True,
    )

    bonus_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("bonus.id"),
        primary_key=True,
    )

    value: Mapped[int] = mapped_column(default=0)

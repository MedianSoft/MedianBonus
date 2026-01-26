from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base

from .enum import CustomerStatus


class Customer(Base):
    __tablename__ = "customers"

    name: Mapped[str] = mapped_column(String(63))

    phone: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)

    status: Mapped[CustomerStatus] = mapped_column(
        Enum(CustomerStatus, name="customer_status"),
        nullable=False,
        default=CustomerStatus.ACTIVATED,
    )

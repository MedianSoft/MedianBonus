from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base


class Customer(Base):
    __tablename__ = "customers"

    name: Mapped[str] = mapped_column(String(63))

    phone: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base

from .enum import BusinessStatus


class Business(Base):
    __tablename__ = "businesses"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[BusinessStatus] = mapped_column(
        Enum(BusinessStatus, name="business_status"),
        nullable=False,
        default=BusinessStatus.ACTIVATED,
    )

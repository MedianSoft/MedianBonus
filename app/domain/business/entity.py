from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import TimestampMixin
from .enum import Status


class Business(TimestampMixin):
    __tablename__ = "businesses"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[Status] = mapped_column(
        nullable=False,
        default=Status.ACTIVATED,
    )

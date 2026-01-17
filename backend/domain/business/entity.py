import uuid

from sqlalchemy import Enum, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import TimestampMixin
from .enum import Status


class Business(TimestampMixin):
    __tablename__ = "businesses"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[Status] = mapped_column(
        Enum(Status, name="status"),
        nullable=False,
        default=Status.ACTIVATED,
    )

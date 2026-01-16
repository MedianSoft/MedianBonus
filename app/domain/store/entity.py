import uuid

from sqlalchemy import Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import TimestampMixin

from .enum import Status


class Store(TimestampMixin):
    __tablename__ = "stores"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[Status] = mapped_column(
        Enum(Status, name="status"),
        nullable=False,
        default=Status.CREATED,
    )

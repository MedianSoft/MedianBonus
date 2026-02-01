import uuid
from datetime import datetime

from sqlalchemy import Enum, UUID, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .enum import Status

class AbstractBase(DeclarativeBase):
    __abstract__ = True


class Base(AbstractBase):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    status: Mapped[Status] = mapped_column(
        Enum(Status, name="status"),
        nullable=False,
        default=Status.ACTIVATED,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

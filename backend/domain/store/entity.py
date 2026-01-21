import uuid

from sqlalchemy import UUID, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.domain.base import Entity

from .enum import StoreStatus


class Store(Entity):
    __tablename__ = "stores"

    business_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("businesses.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[StoreStatus] = mapped_column(
        Enum(StoreStatus, name="store_status"),
        nullable=False,
        default=StoreStatus.ACTIVATED,
    )

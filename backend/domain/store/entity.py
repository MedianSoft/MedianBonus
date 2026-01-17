import uuid

from sqlalchemy import Enum, ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import TimestampMixin
from .enum import StoreStatus


class Store(TimestampMixin):
    __tablename__ = "stores"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    business_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("businesses.id"))

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[StoreStatus] = mapped_column(
        Enum(StoreStatus, name="store_status"),
        nullable=False,
        default=StoreStatus.ACTIVATED,
    )

import uuid

from sqlalchemy import UUID, Enum, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import TimestampMixin

from .enum import BonusType


class Bonus(TimestampMixin):
    __tablename__ = "bonus_programs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    type: Mapped[BonusType] = mapped_column(
        Enum(BonusType, name="bonus_type"),
        nullable=False,
    )

    store_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("stores.id", ondelete="CASCADE"),
        nullable=False,
    )

    product_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=True,
    )

    parameter: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        nullable=False,
        default=True,
    )

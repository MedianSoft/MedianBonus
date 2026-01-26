import uuid

from sqlalchemy import UUID, Enum, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base

from .enum import BonusType


class Bonus(Base):
    __tablename__ = "bonuses"

    type: Mapped[BonusType] = mapped_column(
        Enum(BonusType, name="bonus_type"),
        nullable=False,
    )

    store_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("stores.id", ondelete="CASCADE"),
        nullable=False,
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False,
    )

    value: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        nullable=False,
        default=True,
    )

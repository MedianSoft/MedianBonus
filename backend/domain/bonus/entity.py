import uuid

from sqlalchemy import UUID, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import TimestampMixin

from .enum import BonusProgramType


class BonusProgram(TimestampMixin):
    __tablename__ = "bonus_programs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    store_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("stores.id", ondelete="CASCADE"),
        nullable=False,
    )

    type: Mapped[BonusProgramType] = mapped_column(
        Enum(BonusProgramType, name="bonus_program_type"),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(default=True)


class DiscountRule(TimestampMixin):
    __tablename__ = "discount_rules"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    program_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("bonus_programs.id", ondelete="CASCADE"),
        nullable=False,
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=True,
    )

    percent: Mapped[int] = mapped_column(nullable=False)


class GiftRule(TimestampMixin):
    __tablename__ = "gift_rules"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    program_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("bonus_programs.id", ondelete="CASCADE"),
        nullable=False,
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False,
    )

    count: Mapped[int] = mapped_column(nullable=False)


class PointsRule(TimestampMixin):
    __tablename__ = "points_rules"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    program_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("bonus_programs.id", ondelete="CASCADE"),
        nullable=False,
    )

    points: Mapped[int] = mapped_column(nullable=False)

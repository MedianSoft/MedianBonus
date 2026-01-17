import uuid

from sqlalchemy import Enum, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import TimestampMixin
from .enum import BonusProgramType


class BonusProgram(TimestampMixin):
    __tablename__ = "bonus_programs"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    store_id: Mapped[UUID] = mapped_column(
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

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    program_id: Mapped[UUID] = mapped_column(
        ForeignKey("bonus_programs.id", ondelete="CASCADE")
    )

    product_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("products.id"),
        nullable=True,
    )

    # 1:100 % discount
    percent: Mapped[int] = mapped_column(nullable=False)


class GiftRule(TimestampMixin):
    __tablename__ = "gift_rules"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    program_id: Mapped[UUID] = mapped_column(
        ForeignKey("bonus_programs.id", ondelete="CASCADE")
    )

    product_id: Mapped[UUID] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
    )

    # How many you should buy to get the free one
    count: Mapped[int] = mapped_column(nullable=False)


class PointsRule(TimestampMixin):
    __tablename__ = "points_rules"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    program_id: Mapped[UUID] = mapped_column(
        ForeignKey("bonus_programs.id", ondelete="CASCADE")
    )

    # Amount of points per customer
    points: Mapped[int] = mapped_column(nullable=False)

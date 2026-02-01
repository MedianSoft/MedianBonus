import uuid

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base


class Order(Base):
    __tablename__ = "orders"

    store_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("stores.id"),
        nullable=False,
    )

    customer_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("customers.id"),
        nullable=True,
    )

    price: Mapped[float] = mapped_column(nullable=False, default=0)

    price_with_discount: Mapped[float] = mapped_column(nullable=False, default=0)

    points_spend: Mapped[int] = mapped_column(nullable=False, default=0)

    points_earned: Mapped[int] = mapped_column(nullable=False, default=0)


class OrderProduct(Base):
    __tablename__ = "order_products"

    order_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False,
    )

    price: Mapped[float] = mapped_column(nullable=False, default=0)

    quantity: Mapped[int] = mapped_column(nullable=False, default=1)

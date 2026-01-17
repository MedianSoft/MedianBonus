import uuid

from sqlalchemy import ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import TimestampMixin
from backend.domain.product.enum import Category, Status


class Product(TimestampMixin):
    __tablename__ = "products"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    store_id: Mapped[UUID] = mapped_column(
        ForeignKey("stores.id", ondelete="CASCADE"),
        nullable=False,
    )

    category: Mapped[Category] = mapped_column(nullable=False, default=Category.OTHER)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    price: Mapped[float] = mapped_column(nullable=False)

    status: Mapped[Status] = mapped_column(default=Status.AVAILABLE)

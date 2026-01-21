import uuid

from sqlalchemy import UUID, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.domain.base import Entity

from .enum import Category, ProductStatus


class Product(Entity):
    __tablename__ = "products"

    store_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("stores.id", ondelete="CASCADE"),
        nullable=False,
    )

    category: Mapped[Category] = mapped_column(nullable=False, default=Category.OTHER)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    price: Mapped[float] = mapped_column(nullable=False)

    status: Mapped[ProductStatus] = mapped_column(
        Enum(ProductStatus, name="product_status"),
        nullable=False,
        default=ProductStatus.AVAILABLE,
    )

import uuid

from sqlalchemy import ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base
from .enum import Category


class Product(Base):
    __tablename__ = "products"

    store_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("stores.id", ondelete="CASCADE"),
        nullable=False,
    )

    category: Mapped[Category] = mapped_column(nullable=False, default=Category.OTHER)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    price: Mapped[float] = mapped_column(nullable=False)

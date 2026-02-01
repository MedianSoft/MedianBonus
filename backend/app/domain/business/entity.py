from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base import Base


class Business(Base):
    __tablename__ = "businesses"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

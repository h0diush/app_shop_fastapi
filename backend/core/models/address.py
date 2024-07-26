from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models.mixins import IntIdMixin
from .base import Base


class Address(Base, IntIdMixin):
    __tablename__ = "addresses"

    city: Mapped[str] = mapped_column(String(18))
    street: Mapped[str] = mapped_column(String(28))
    home: Mapped[int]
    room: Mapped[int | None] = mapped_column(nullable=True)
    entrance: Mapped[int | None] = mapped_column(nullable=True)

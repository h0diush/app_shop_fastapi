from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins import IntIdMixin
from .base import Base

if TYPE_CHECKING:
    from .category import Category


class Product(Base, IntIdMixin):
    name: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(75))
    price: Mapped[float]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="products")

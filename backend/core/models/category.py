from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins import IntIdMixin
from .base import Base

if TYPE_CHECKING:
    from .product import Product


class Category(Base, IntIdMixin):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(20))
    products: Mapped[list["Product"]] = relationship(back_populates="category")

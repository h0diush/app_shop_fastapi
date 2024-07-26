from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins import IntIdMixin
from .base import Base

if TYPE_CHECKING:
    from .address import Address


class Profile(Base, IntIdMixin):
    first_name: Mapped[str] = mapped_column(String(24))
    last_name: Mapped[str] = mapped_column(String(24))
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
    )
    phone: Mapped[int]
    addresses: Mapped[list["Address"]] = relationship(
        secondary="address_profile_association",
        back_populates="profile",
    )

from typing import TYPE_CHECKING


from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins import IntIdMixin
from .base import Base

if TYPE_CHECKING:
    from .profile import Profile


class Address(Base, IntIdMixin):
    __tablename__ = "addresses"

    city: Mapped[str] = mapped_column(String(18))
    street: Mapped[str] = mapped_column(String(28))
    home: Mapped[int]
    room: Mapped[int | None] = mapped_column(nullable=True)
    entrance: Mapped[int | None] = mapped_column(nullable=True)
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("profiles.id", ondelete="cascade"),
    )
    profile: Mapped["Profile"] = relationship(
        back_populates="addresses",
    )

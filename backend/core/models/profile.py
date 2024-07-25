from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from core.models.mixins import IntIdMixin
from .base import Base


class Profile(Base, IntIdMixin):
    first_name: Mapped[str] = mapped_column(String(24))
    last_name: Mapped[str] = mapped_column(String(24))
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
    )
    phone: Mapped[int]

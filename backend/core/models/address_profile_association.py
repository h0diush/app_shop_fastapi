from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models.mixins import IntIdMixin
from .base import Base


class AddressProfileAssociation(Base, IntIdMixin):
    __tablename__ = "address_profile_association"

    profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"))
    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"))

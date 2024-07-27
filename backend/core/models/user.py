from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy.orm import Mapped, relationship

from core.models import Base
from core.models.mixins import IntIdMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .profile import Profile


class User(Base, IntIdMixin, SQLAlchemyBaseUserTable[int]):
    profile: Mapped["Profile"] = relationship(back_populates="user")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)

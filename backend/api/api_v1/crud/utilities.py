from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.models import User, Profile


async def get_addresses_through_profile_user(
    session: AsyncSession,
    user_id: int,
) -> User:
    stmt = (
        select(User)
        .where(
            User.id == user_id,
        )
        .options(
            selectinload(
                User.profile,
            ).selectinload(Profile.addresses),
        )
    )
    user = await session.scalar(stmt)
    return user

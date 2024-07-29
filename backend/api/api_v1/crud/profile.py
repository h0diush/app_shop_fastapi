from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from api.exception.message import PROFILE_EXISTS
from core.models import Profile


async def create_profile(
    session: AsyncSession,
    profile_create: dict,
) -> Profile:
    profile = Profile(**profile_create)
    session.add(profile)
    try:
        await session.commit()
    except IntegrityError:
        raise PROFILE_EXISTS
    return profile


async def get_profile_current_user(
    session: AsyncSession,
    user_id: int,
) -> Profile:
    stmt = select(Profile).where(Profile.user_id == user_id)
    profile = await session.scalar(stmt)
    return profile


async def delete_profile(session: AsyncSession, user_id: int) -> None:
    stmt = delete(Profile).where(Profile.user_id == user_id)
    await session.execute(stmt)
    await session.commit()
    return None

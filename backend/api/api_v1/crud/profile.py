from fastapi import HTTPException
from sqlalchemy import select, Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

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
        raise HTTPException(status_code=400, detail="adadaw")
    return profile


async def get_profile_current_user(
    session: AsyncSession,
    user_id: int,
) -> Profile:
    stmt = select(Profile).where(Profile.user_id == user_id)
    profile = await session.scalar(stmt)
    return profile

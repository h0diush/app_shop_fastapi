from asyncpg import UniqueViolationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Profile
from core.schemas.profile import ProfileCreate
from fastapi import HTTPException


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

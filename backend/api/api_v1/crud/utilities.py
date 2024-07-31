from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api.exception.message import NO_ADDRESS
from core.models import User, Profile, Address


async def get_user_select_in_load_profile(
    session: AsyncSession,
    user_id: int,
) -> User:
    stmt = (
        select(User)
        .where(User.id == user_id)
        .options(
            selectinload(User.profile).selectinload(
                Profile.addresses,
            ),
        )
    )
    user = await session.scalar(stmt)
    return user


async def address_delete_and_update_utility(
    session: AsyncSession,
    address_id: int,
    user_id: int,
):
    user = await get_user_select_in_load_profile(session, user_id)
    stmt = select(Address).where(Address.id == address_id)
    address = await session.scalar(stmt)
    if not address or address.profile_id != user.profile.id:
        raise NO_ADDRESS
    return address

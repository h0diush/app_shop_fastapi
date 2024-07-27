from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.models import Address, User, Profile
from core.schemas.address import AddressModel


async def add_address(
    session: AsyncSession,
    address_in: AddressModel,
    user_id: int,
) -> Address:
    address = Address(**address_in.model_dump())
    session.add(address)
    user = await session.scalar(
        select(User)
        .where(User.id == user_id)
        .options(
            selectinload(
                User.profile,
            ).selectinload(Profile.addresses),
        ),
    )
    user.profile.addresses.append(address)
    await session.commit()
    return address

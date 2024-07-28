from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api.exception.message import NO_ADDRESS
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


async def delete_address(
    session: AsyncSession,
    address_id: int,
    user_id: int,
) -> None:
    user = await session.scalar(
        select(User)
        .where(User.id == user_id)
        .options(
            selectinload(
                User.profile,
            ).selectinload(Profile.addresses),
        ),
    )
    stmt = select(Address).where(Address.id == address_id)
    address = await session.scalar(stmt)
    if not address or not address in user.profile.addresses:
        raise NO_ADDRESS
    await session.delete(address)
    await session.commit()

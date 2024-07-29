from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud.utilities import get_addresses_through_profile_user
from api.exception.message import NO_ADDRESS
from core.models import Address
from core.schemas.address import AddressModel


async def add_address(
    session: AsyncSession,
    address_in: AddressModel,
    user_id: int,
) -> Address:
    address = Address(**address_in.model_dump())
    session.add(address)
    user = await get_addresses_through_profile_user(session, user_id)
    user.profile.addresses.append(address)
    await session.commit()
    return address


async def delete_address(
    session: AsyncSession,
    address_id: int,
    user_id: int,
) -> None:
    user = await get_addresses_through_profile_user(session, user_id)
    stmt = select(Address).where(Address.id == address_id)
    address = await session.scalar(stmt)
    if not address or not address in user.profile.addresses:
        raise NO_ADDRESS
    await session.delete(address)
    await session.commit()


async def get_addresses_for_current_user(
    session: AsyncSession,
    user_id: int,
):
    user = await get_addresses_through_profile_user(session, user_id)
    return user.profile.addresses

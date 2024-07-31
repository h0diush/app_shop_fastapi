from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud.utilities import (
    address_delete_and_update_utility,
    get_user_select_in_load_profile,
)
from api.exception.message import NO_PROFILE
from core.models import Address
from core.schemas.address import AddressModel, AddressMeModel


async def add_address(
    session: AsyncSession, address_in: AddressModel, user_id: int
) -> Address | None:
    user = await get_user_select_in_load_profile(session, user_id)
    if not user.profile:
        return None
    address_dict = address_in.dict()
    address_dict["profile_id"] = user.profile.id
    address = Address(**address_dict)
    session.add(address)
    await session.commit()
    return address


async def delete_address(
    session: AsyncSession,
    address_id: int,
    user_id: int,
) -> None:
    address = await address_delete_and_update_utility(
        session,
        address_id,
        user_id,
    )
    await session.delete(address)
    await session.commit()


async def get_addresses_for_current_user(
    session: AsyncSession,
    user_id: int,
) -> list[AddressMeModel] | None:
    user = await get_user_select_in_load_profile(session, user_id)
    if user.profile:
        return user.profile.addresses
    raise NO_PROFILE

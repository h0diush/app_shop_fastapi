from fastapi import APIRouter, Depends, status

from api.api_v1.crud import address as crud_address
from api.api_v1.fastapi_users import current_user
from api.dependencies.session import session_depends
from core.config import settings
from core.models import User
from core.schemas.address import AddressModel, AddressMeModel

router = APIRouter(
    prefix=settings.api.v1.address,
    tags=["Address"],
)


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=AddressModel,
)
async def create_address_for_user_profile(
    session: session_depends,
    address_in: AddressModel,
    user: User = Depends(current_user),
):
    return await crud_address.add_address(
        session=session,
        address_in=address_in,
        user_id=user.id,
    )


@router.delete(
    "/delete",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_addresses(
    session: session_depends,
    address_id: int,
    user: User = Depends(current_user),
):
    return await crud_address.delete_address(
        session=session,
        user_id=user.id,
        address_id=address_id,
    )


@router.get("/me", response_model=list[AddressMeModel])
async def get_addresses_current_user(
    session: session_depends,
    user: User = Depends(current_user),
):
    return await crud_address.get_addresses_for_current_user(
        session,
        user.id,
    )

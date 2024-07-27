from fastapi import APIRouter, Depends, status

from api.api_v1.fastapi_users import current_user
from api.dependencies.session import session_depends
from api.exception.message import NO_PROFILE
from core.config import settings
from core.models import User
from core.schemas.address import AddressModel
from core.schemas.profile import ProfileSchemas
from .crud import profile as crud_profile
from .crud import address as crud_address

router = APIRouter(
    prefix=settings.api.v1.profile,
    tags=["Profiles"],
)


@router.post(
    "/create",
    response_model=ProfileSchemas,
    status_code=status.HTTP_201_CREATED,
)
async def create_profile(
    session: session_depends,
    profile_in: ProfileSchemas,
    user: User = Depends(current_user),
):
    profile_data = profile_in.dict()
    profile_data["user_id"] = user.id
    profile = await crud_profile.create_profile(session, profile_data)
    return profile


@router.get("/me", response_model=ProfileSchemas)
async def get_main_profile(
    session: session_depends,
    user: User = Depends(current_user),
):
    if profile := await crud_profile.get_profile_current_user(
        session,
        user.id,
    ):
        return profile
    raise NO_PROFILE


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(
    session: session_depends,
    user: User = Depends(current_user),
) -> None:
    await crud_profile.delete_profile(session, user.id)


@router.post(
    "/address_create",
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

from fastapi import APIRouter, Depends

from api.api_v1.fastapi_users import current_user
from api.dependencies.session import session_depends
from core.config import settings
from core.models import User
from core.schemas.profile import ProfileCreate
from .crud import profile as crud_profile

router = APIRouter(
    prefix=settings.api.v1.profile,
    tags=["Profiles"],
)


@router.post("/create", response_model=ProfileCreate)
async def create_profile(
    session: session_depends,
    profile_in: ProfileCreate,
    user: User = Depends(current_user),
):
    profile_data = profile_in.dict()
    profile_data["user_id"] = user.id
    profile = await crud_profile.create_profile(session, profile_data)
    return profile

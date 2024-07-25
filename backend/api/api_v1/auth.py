from fastapi import APIRouter

from api.dependencies.authentication.backend import authentication_backend
from core.config import settings
from core.schemas.user import UserRead, UserCreate
from .fastapi_users import fastapi_users

router = APIRouter(prefix=settings.api.v1.auth, tags=["Auth"])

# /login
# / logout
router.include_router(
    fastapi_users.get_auth_router(
        authentication_backend,
    )
)


# /register
router.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    )
)

# /forgot-password
# /reset-password
router.include_router(fastapi_users.get_reset_password_router())


# /request-verify-token
# /verify
router.include_router(fastapi_users.get_verify_router(UserRead))

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.config import settings
from .address import router as address_router
from .auth import router as auth_router
from .category import router as category_router
from .product import router as product_router
from .profile import router as profile_router
from .user import router as user_router

http_bearer = HTTPBearer(auto_error=False)
router = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)
router.include_router(address_router)
router.include_router(auth_router)
router.include_router(category_router)
router.include_router(product_router)
router.include_router(profile_router)
router.include_router(user_router)

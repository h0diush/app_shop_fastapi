from fastapi import APIRouter, Depends

from api.api_v1.crud import category as crud_category
from api.api_v1.fastapi_users import superuser
from api.dependencies.session import session_depends
from core.config import settings
from core.models import User
from core.schemas.category import CategoryCreate, CategoryList

router = APIRouter(
    prefix=settings.api.v1.categories,
    tags=["Categories"],
)


@router.get("/", response_model=list[CategoryList])
async def get_list_categories(session: session_depends):
    return await crud_category.get_list_categories(session)


@router.post("/create", response_model=CategoryCreate)
async def create_category(
    session: session_depends,
    product_in: CategoryCreate,
    user: User = Depends(superuser),
):
    return await crud_category.create_category(session, product_in)

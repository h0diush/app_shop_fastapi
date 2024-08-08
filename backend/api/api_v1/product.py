from fastapi import APIRouter, Depends

from api.api_v1.crud import product as crud_product
from api.api_v1.fastapi_users import superuser
from api.dependencies.session import session_depends
from core.config import settings
from core.models import User
from core.schemas.product import ProductList, ProductCreate

router = APIRouter(
    prefix=settings.api.v1.products,
    tags=["Products"],
)


@router.get("/", response_model=list[ProductList])
async def get_list_products(session: session_depends):
    return await crud_product.get_list_products(session)


@router.post("/create", response_model=ProductCreate)
async def create_product(
    session: session_depends,
    product_in: ProductCreate,
    user: User = Depends(superuser),
):
    return await crud_product.create_product(session, product_in)

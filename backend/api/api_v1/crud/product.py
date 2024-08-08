from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import Product, Category
from core.schemas.product import ProductCreate


async def get_list_products(session: AsyncSession):
    stmt = select(Product)
    products = await session.scalars(stmt)
    return products


async def get_product_by_id(session: AsyncSession, product_id: int):
    stmt = select(Product).where(Product.id == product_id)
    product = await session.scalar(stmt)
    return product


async def create_product(session: AsyncSession, product_in: ProductCreate):
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product_id: int):
    stmt = delete(Product).where(Product.id == product_id)
    await session.execute(stmt)
    await session.commit()
    return None


async def get_products_by_category_id(session: AsyncSession, category_id):
    stmt = (
        select(Category)
        .where(Category.id == category_id)
        .options(joinedload(Category.products))
    )
    category = await session.scalar(stmt)
    if category:
        return category.products
    return None

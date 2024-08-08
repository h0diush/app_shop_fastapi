from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Category
from core.schemas.category import CategoryCreate


async def get_list_categories(session: AsyncSession):
    stmt = select(Category)
    category = await session.scalars(stmt)
    return category


async def get_category_by_id(session: AsyncSession, category_id: int):
    stmt = select(Category).where(Category.id == category_id)
    category = await session.scalar(stmt)
    return category


async def create_category(session: AsyncSession, product_in: CategoryCreate):
    category = Category(**product_in.model_dump())
    session.add(category)
    await session.commit()
    return category


async def delete_product(session: AsyncSession, category_id: int):
    stmt = delete(Category).where(Category.id == category_id)
    await session.execute(stmt)
    await session.commit()
    return None

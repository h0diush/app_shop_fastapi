from pydantic import BaseModel


class CategoryList(BaseModel):
    id: int
    name: str


class CategoryCreate(BaseModel):
    name: str


class CategoryUpdate(BaseModel):
    name: str | None = None
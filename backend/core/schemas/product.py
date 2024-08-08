from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    name: str
    price: float


class ProductList(ProductBase):
    pass


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int


class ProductRead(ProductBase):
    description: str
    # category_id: int

from pydantic import BaseModel


class ProfileSchemas(BaseModel):
    first_name: str
    last_name: str
    phone: int


class ProfileUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone: int | None = None

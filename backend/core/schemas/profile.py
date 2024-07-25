from pydantic import BaseModel


class ProfileCreate(BaseModel):
    first_name: str
    last_name: str
    phone: int

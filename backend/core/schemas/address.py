from pydantic import BaseModel


class AddressModel(BaseModel):
    city: str
    street: str
    home: int
    room: int | None
    entrance: int | None


class AddressMeModel(AddressModel):
    id: int

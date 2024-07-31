from pydantic import BaseModel


class AddressModel(BaseModel):
    city: str
    street: str
    home: int
    room: int | None
    entrance: int | None


class AddressMeModel(AddressModel):
    id: int


class AddressUpdate(BaseModel):
    city: str | None = None
    street: str | None = None
    home: int | None = None
    room: int | None = None
    entrance: int | None = None

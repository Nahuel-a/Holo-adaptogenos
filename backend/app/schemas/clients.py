from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    phone: str
    country: str
    city: str
    address: str
    number: int
    apartment: str | None = None
    postal_code: str

class ClientCreate(ClientBase):
    pass

class ClientSchema(ClientBase):
    id: int

    class Config:
        from_attributes = True

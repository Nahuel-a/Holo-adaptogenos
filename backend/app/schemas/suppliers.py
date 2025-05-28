from pydantic import BaseModel, EmailStr

class SupplierBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    alias: str
    website: str

class SupplierCreate(SupplierBase):
    pass

class SupplierSchema(SupplierBase):
    id: int

    class Config:
        from_attributes = True
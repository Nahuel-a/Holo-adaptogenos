from pydantic import BaseModel
from datetime import date
from .commons import PaymentMethod

class PurchasesBase(BaseModel):
    purchase_date: date
    supplier_id: int
    payment_method: PaymentMethod
    total_price: float


class PurchasesCreate(PurchasesBase):
    pass


class PurchasesSchema(PurchasesBase):
    id: int

    class Config:
        from_attributes = True
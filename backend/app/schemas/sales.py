from pydantic import BaseModel
from .commons import PaymentMethod, SaleStatus
from datetime import date

class SaleBase(BaseModel):
    client_id: int
    sale_date: date
    payment_method: PaymentMethod
    total_price: float
    status: SaleStatus


class SaleCreate(SaleBase):
    pass

class SaleSchema(SaleBase):
    id: int 

    class Config:
        from_attributes = True
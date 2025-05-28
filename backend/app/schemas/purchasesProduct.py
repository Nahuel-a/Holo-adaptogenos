from pydantic import BaseModel

class PurchasesProductBase(BaseModel):
    purchase_id: int
    product_id: int
    quantity: float
    unit_price: float
    sub_total: float


class PurchasesProductCreate(PurchasesProductBase):
    pass


class PurchasesProductSchema(PurchasesProductBase):
    id: int

    class Config:
        from_attributes = True
from pydantic import BaseModel

class SalesProductBase(BaseModel):
    sales_id: int
    product_id: int
    quantity: float
    unit_price: float
    sub_total: float


class SalesProductCreate(SalesProductBase):
    pass


class SalesProductSchema(SalesProductBase):
    id: int

    class Config:
        from_attributes = True
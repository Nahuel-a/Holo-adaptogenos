from pydantic import BaseModel

class ProductComplementBase(BaseModel):
    product_id: int
    sub_product_id: int
    quantity_used: float

class ProductComplementCreate(ProductComplementBase):
    pass

class ProductComplementSchema(ProductComplementBase):
    id: int

    class Config:
        from_attributes = True
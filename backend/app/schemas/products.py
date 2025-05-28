from pydantic import BaseModel, Field
from .commons import ProductUnit

class ProductBase(BaseModel):
    name: str = Field(..., example="Product Name")
    unit_price: float = Field(...,gt=0, example=25000)
    stock: int = Field(..., gt=0, example=100)   
    min_stock: int = Field(..., gt=0, example=10)
    unit: ProductUnit = Field(..., example=ProductUnit.LITERS)

class ProductCreate(ProductBase):
    pass

class ProductSchema(ProductBase):
    id: int = Field(..., example=1)

    class Config:
        from_attributes = True
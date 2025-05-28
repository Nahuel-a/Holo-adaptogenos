from pydantic import BaseModel, Field
from datetime import date

class ProductionBase(BaseModel):
    final_product_id: int = Field(..., title="ID of the final product",)
    quantity_produced: float = Field(...,gt=0, title="Quantity produced")
    production_date: date = Field(..., title="Date of production ")
    

class ProductionCreate(ProductionBase):
    pass


class ProductionSchema(ProductionBase):
    id: int = Field(..., title="ID of the production record")
    
    class Config:
        from_attributes = True


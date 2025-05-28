from pydantic import BaseModel
from .commons import ProductionStageType, ProductionStageStatus
from datetime import date

class ProductionStageBase(BaseModel):
    stage_type: ProductionStageType
    start_date: date
    end_date: date
    status: ProductionStageStatus
    production_id: int

class ProductionStageCreate(ProductionStageBase):
    pass

class ProductionStageSchema(ProductionStageBase):
    id: int

    class Config:
        from_attributes = True


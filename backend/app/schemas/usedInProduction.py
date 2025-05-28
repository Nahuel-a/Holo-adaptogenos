from pydantic import BaseModel

class UsedInProductionBase(BaseModel):
    product_id: int
    production_stage_id: int
    quantity_used: float


class UsedInProductionCreate(UsedInProductionBase):
    pass


class UsedInProductionSchema(UsedInProductionBase):
    id: int

    class Config:
        from_attributes = True
        
from .baseServices import BaseService
from models.production import Production
from schemas.production import ProductionCreate, ProductionSchema

production_service = BaseService[Production, ProductionCreate, ProductionSchema](Production)

from .baseServices import BaseService
from models.purchases import Purchases
from schemas.purchases import PurchasesCreate, PurchasesSchema

purchace_service = BaseService[Purchases, PurchasesCreate, PurchasesSchema](Purchases)
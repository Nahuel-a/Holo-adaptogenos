from .baseServices import BaseService
from models.sales import Sale
from schemas.sales import SaleCreate, SaleSchema

sale_service = BaseService[Sale, SaleCreate, SaleSchema](Sale)
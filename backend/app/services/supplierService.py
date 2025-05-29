from .baseServices import BaseService
from models.suppliers import Suppliers
from schemas.suppliers import SupplierCreate, SupplierSchema

supplier_service = BaseService[Suppliers, SupplierCreate, SupplierSchema](Suppliers)
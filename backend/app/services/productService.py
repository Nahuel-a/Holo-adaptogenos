from .baseServices import BaseService
from models.products import Product
from schemas.products import ProductCreate, ProductSchema

product_service = BaseService[Product, ProductCreate, ProductSchema](Product)
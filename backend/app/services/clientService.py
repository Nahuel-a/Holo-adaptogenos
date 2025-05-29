from .baseServices import BaseService
from models.clients import Client
from schemas.clients import ClientCreate, ClientSchema

client_service = BaseService[Client, ClientCreate, ClientSchema](Client)

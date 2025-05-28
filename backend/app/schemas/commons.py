from enum import Enum

class PaymentMethod(str, Enum):
    CASH = "Cash"
    TRANSFER = "Transfer"
    DEBIT_CARD = "Debit Card"

class SaleStatus(str, Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELED = "Canceled"

class ProductionStageType(str, Enum):
    MACERATION = "Maceration"
    EVAPORATION = "Evaporation"

class ProductionStageStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class ProductUnit(str, Enum):
    LITERS = "liters"
    GRAMS = "grams"
    UNITS = "units"
    METERS = "meters"



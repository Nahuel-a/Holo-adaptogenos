from typing import TYPE_CHECKING, Optional, List
from core.database import Base
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.products import Product  # noqa: F401
    from app.models.productionStage import ProductionStage  # noqa: F401
else:
    Product = 'Product'
    ProductionStage = 'ProductionStage'

class Production(Base):
    __tablename__ = "table_production"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    final_product_id: Mapped[Optional[int]] = mapped_column(ForeignKey('table_product.id'))
    quantity_produced: Mapped[float] = mapped_column(nullable=False)
    production_date: Mapped[DateTime] = mapped_column(nullable=False)
    
    #Ver si se agrega las fechas de inicio y fin de producción

    # Relationships
    stages: Mapped[List[ProductionStage]] = relationship(
        back_populates="production",
        cascade="all, delete-orphan",
    )

    final_product: Mapped[Product] = relationship(
        back_populates="productions",
    )
    

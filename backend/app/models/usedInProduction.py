from typing import TYPE_CHECKING, Optional
from core.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.products import Product  # noqa: F401
    from app.models.productionStage import ProductionStage  # noqa: F401
else:
    Product = 'Product' # noqa: F401
    ProductionStage = 'ProductionStage'

class UsedProduct(Base):
    __tablename__ = "table_used_product"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('table_product.id'))
    production_stage_id: Mapped[Optional[int]] = mapped_column(ForeignKey('table_production_stage.id'))
    quantity_used: Mapped[float] = mapped_column(nullable=False)
    
    # Relationships
    product: Mapped[Product] = relationship(back_populates="used_products")
    production_stage: Mapped[ProductionStage] = relationship(back_populates="used_in_production")
    

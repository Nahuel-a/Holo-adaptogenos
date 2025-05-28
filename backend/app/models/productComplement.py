from typing import TYPE_CHECKING, Optional
from core.database import Base
from sqlalchemy import ForeignKey, Integer as Int
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.products import Product   # noqa: F401
else:
    Product = 'Product' # noqa: F401


class ProductComplement(Base):
    __tablename__ = "product_complement"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,unique=True)
    product_id: Mapped[Optional[int]] = mapped_column(ForeignKey('table_product.id'))
    sub_product_id: Mapped[Optional[int]] = mapped_column(ForeignKey('table_product.id'))
    quantity_used: Mapped[float] = mapped_column(nullable=False)

    # Relationships
    product: Mapped[Product] = relationship(
        back_populates="components", 
        foreign_keys=[product_id]
    )
    sub_product: Mapped[Product] = relationship(
        back_populates="used_in", 
        foreign_keys=[sub_product_id]
    )

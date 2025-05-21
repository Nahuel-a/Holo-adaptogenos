from typing import TYPE_CHECKING, List
from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.sales import Sale  # noqa: F401
    from app.models.products import Product  # noqa: F401
else:
    Sales = 'Sales' # noqa: F401
    Product = 'Product' # noqa: F401
    
class SalesProducts(Base):
    __tablename__ = "table_sales_products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,unique=True)
    sales_id: Mapped[int] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[float] = mapped_column(nullable=False)
    unit_price: Mapped[float] = mapped_column(nullable=False)
    sub_total: Mapped[float] = mapped_column(nullable=False)

    # Relationships
    sales: Mapped[Sale] = relationship(back_populates="sales_products")
    products: Mapped[List[Product]] = relationship(back_populates="sales_products")
from typing import TYPE_CHECKING, List
from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.purchases import Purchases  # noqa: F401
    from app.models.products import Product  # noqa: F401
else:
    Purchases = 'Purchases' # noqa: F401
    Product = 'Product' # noqa: F401
    
class PurchasesProducts(Base):
    __tablename__ = "table_purchases_products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,unique=True)
    purchase_id: Mapped[int] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[float] = mapped_column(nullable=False)
    unit_price: Mapped[float] = mapped_column(nullable=False)
    sub_total: Mapped[float] = mapped_column(nullable=False)

    # Relationships
    purchases: Mapped[Purchases] = relationship(back_populates="purchase_product")
    products: Mapped[List[Product]] = relationship(back_populates="purchases_products")
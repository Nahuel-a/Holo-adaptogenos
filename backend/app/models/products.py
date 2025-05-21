from typing import TYPE_CHECKING, List, Optional
from core.database import Base
from sqlalchemy import String, Integer as Int, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.productComplement import ProductComplement  # noqa: F401
    from app.models.purchasesProduct import PurchasesProducts  # noqa: F401
    from app.models.production import Production  # noqa: F401
    from app.models.usedInProduction import UsedProduct  # noqa: F401
else:
    ProductComplement = 'ProductComplement' # noqa: F401
    PurchasesProducts = 'PurchasesProducts' # noqa: F401
    Production = 'Production' # noqa: F401
    UsedProduct = 'UsedProduct' # noqa: F401

class Product(Base):
    __tablename__ = "table_product"

    id: Mapped[int] = mapped_column(Int, primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    unit_price: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(Int, default=0, nullable=False)
    min_stock: Mapped[int] = mapped_column(Int, default=0, nullable=False)
    unit: Mapped[Enum] = mapped_column(
        Enum('liters', 'grams', 'units', 'meters'), default='grams'
    )

    # Relationships
    # Sub-products that compose this product
    components: Mapped[Optional[List[ProductComplement]]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan",
        foreign_keys="[product_complement.product_id]",
    )
    # Products in which this product is used as component
    used_in: Mapped[Optional[List[ProductComplement]]] = relationship(
        back_populates="sub_product",
        cascade="all, delete-orphan",
        foreign_keys="[product_complement.sub_product_id]",
    )
    # Purchases that include this product
    purchases_products: Mapped[List[PurchasesProducts]] = relationship(
        back_populates="products",
        cascade="all, delete-orphan",
        foreign_keys="[PurchasesProducts.product_id]",
    )
    # Production stages that use this product
    used_products: Mapped[List[UsedProduct]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan",
        foreign_keys="[UsedProduct.product_id]",
    )
    # Production records for this product
    productions: Mapped[List[Production]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan",
        foreign_keys="[Production.final_product_id]",
    )

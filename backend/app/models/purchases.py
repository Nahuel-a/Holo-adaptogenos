from typing import List, TYPE_CHECKING
from core.database import Base
from sqlalchemy import DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.suppliers import Suppliers  # noqa: F401
    from app.models.purchasesProduct import PurchasesProducts  # noqa: F401
else:
    Suppliers = "Suppliers"
    PurchasesProducts = "PurchasesProducts"  # noqa: F401

class Purchases(Base):
    __tablename__ = "table_purchases"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    purchase_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("table_suppliers.id"), nullable=False)
    payment_method: Mapped[Enum] = mapped_column(
        Enum('Chash', 'Transfer', 'Debit_card')
    )
    total_price: Mapped[float] = mapped_column(nullable=False)


    # Relationships
    supplier: Mapped[Suppliers] = relationship(back_populates="purchases")
    purchases_products: Mapped[List[PurchasesProducts]] = relationship(
        back_populates="purchases",
        cascade="all, delete-orphan",
        foreign_keys="PurchasesProducts.purchase_id",
    )
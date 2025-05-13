from core.database import Base
from sqlalchemy import DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship


class PurchasesProducts(Base):
    __tablename__ = "purchases_products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    #purchase_id: Mapped[int] = mapped_column(nullable=False)
    #product_id: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[float] = mapped_column(nullable=False)
    unit_price: Mapped[float] = mapped_column(nullable=False)

    # Relationships
    # purchases = relationship("Purchases", back_populates="purchases_products")
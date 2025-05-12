from core.database import Base
from sqlalchemy import DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Purchases(Base):
    __tablename__ = "purchases"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    purchase_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    supplier_id: Mapped[int] = mapped_column(nullable=False)
    payment_method: Mapped[Enum] = mapped_column(
        Enum('Chash', 'Transfer', 'Debit_card')
    )
    total_amount: Mapped[float] = mapped_column(nullable=False)


    # Relationships
    # supplier = relationship("Supplier", back_populates="purchases")
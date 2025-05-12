from core.database import Base
from sqlalchemy import DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

class Sale(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    client_id: Mapped[int] = mapped_column(index=True)
    sale_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    payment_method: Mapped[Enum] = mapped_column(
        Enum('Chash', 'Transfer', 'Debit_card')
    )
    total_amount: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[Enum] = mapped_column(
        Enum('Pending', 'Completed', 'Canceled'), default='Pending'
    )


    # Relationships
    #client: Mapped["Client"] = relationship(back_populates="sales")
    

    
    
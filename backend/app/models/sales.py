from typing import TYPE_CHECKING, Optional
from core.database import Base
from sqlalchemy import DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

if TYPE_CHECKING:
    from app.models.clients import Client  # noqa: F401
else:
    Client = "Client"  # noqa: F401



class Sale(Base):
    __tablename__ = "table_sale"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    sale_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    payment_method: Mapped[Enum] = mapped_column(
        Enum('Chash', 'Transfer', 'Debit_card')
    )
    total_price: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[Enum] = mapped_column(
        Enum('Pending', 'Completed', 'Canceled'), default='Pending'
    )

    # Relationships
    client: Mapped[Optional[Client]] = relationship(back_populates="sales")

    

    
    
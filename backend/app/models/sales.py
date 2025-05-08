from core.database import Base
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

class Sale(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    client_id: Mapped[int] = mapped_column(index=True)
    sale_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


    # Relationships
    #client: Mapped["Client"] = relationship(back_populates="sales")
    

    
    
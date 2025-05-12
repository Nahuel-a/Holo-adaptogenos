from core.database import Base
from sqlalchemy import String, Integer as Int
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ProductComplement(Base):
    __tablename__ = "product_complement"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(Int(255), nullable=False)#Foreign key to Product table
    sub_product_id: Mapped[int] = mapped_column(Int(255), nullable=False)#Foreign key to Product table
    quantity_used: Mapped[float] = mapped_column(nullable=False)

    # Relationships
    

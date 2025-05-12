from core.database import Base
from sqlalchemy import String, Integer as Int, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Int, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(Int, default=0, nullable=False)
    min_stock: Mapped[int] = mapped_column(Int, default=0, nullable=False)
    unit: Mapped[Enum] = mapped_column(
        Enum('liters', 'grams', 'units', 'meters'), default='grams'
    )


    # Relationships
    # categories_id
    # unit_id








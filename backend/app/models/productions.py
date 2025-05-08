from core.database import Base
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Productions(Base):
    __tablename__ = "productions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    final_product_id: Mapped[int] = mapped_column(nullable=False)
    production_date: Mapped[DateTime] = mapped_column(nullable=False)
    
    #Ver si se agrega las fechas de inicio y fin de producción

    # Relationships
    
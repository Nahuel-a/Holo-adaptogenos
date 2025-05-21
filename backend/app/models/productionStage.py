from typing import TYPE_CHECKING, List
from core.database import Base
from sqlalchemy import DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.usedInProduction import UsedProduct  # noqa: F401
    from app.models.production import Production  # noqa: F401
else:
    UsedProduct = 'UsedProduct'
    Production = 'Production'  # noqa: F401

class ProductionStage(Base):
    __tablename__ = "table_production_stage"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    stage_type: Mapped[Enum] = mapped_column(
        Enum('Maceration', 'Evaporation')
    )
    start_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    status: Mapped[Enum] = mapped_column(
        Enum('Pending', 'In_Progress', 'Completed')
    )
    production_id: Mapped[int] = mapped_column(ForeignKey("table_production.id"), nullable=False)
        
    # Relationships
    used_in_production: Mapped[List[UsedProduct]] = relationship(
        back_populates="production_stage",
        cascade="all, delete-orphan",
        foreign_keys="[UsedProduct.table_production_stage_id]",
    )

    production: Mapped[Production] = relationship(
        back_populates="stages",
    )

    
    
from core.database import Base
from sqlalchemy import DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ProductionStage(Base):
    __tablename__ = "production_stage"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    stage_type: Mapped[Enum] = mapped_column(
        Enum('Maceration', 'Evaporation')
    )
    start_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    status: Mapped[Enum] = mapped_column(
        Enum('Pending', 'In_Progress', 'Completed')
    )
    quatity_used: Mapped[float] = mapped_column(nullable=False)
    #production_id: Mapped[int] = mapped_column(nullable=False)

    # Relationships
    # production = relationship("Production", back_populates="production_stage")
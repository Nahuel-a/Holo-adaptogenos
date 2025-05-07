from core.database import Base 
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Unit(Base):
    __tablename__ = "units"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    symbol: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    
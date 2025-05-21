from core.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column,relationship

class Suppliers(Base):
    __tablename__ = "table_suppliers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    alias: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    website: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)


    #def __repr__(self) -> str:
    
    purchases: Mapped[List[Purchase]] = relationship(
        back_populates="supplier",
        cascade="all, delete-orphan",
    )

    
    
    
    
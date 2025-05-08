from core.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    # Relationships
    #products: Mapped["Product"] = relationship(back_populates="category")
from typing import TYPE_CHECKING, Optional, List
from core.database import Base
from sqlalchemy import String, Integer as Int
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.sales import Sale  # noqa: F401
else:
    Sale = "Sale"  # noqa: F401


class Client(Base):
    __tablename__ = "table_client"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    country: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    number: Mapped[int] = mapped_column(Int(255), nullable=False)
    apartment: Mapped[str] = mapped_column(String(255), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(255), nullable=False)

    # Relationships
    sales: Mapped[Optional[List[Sale]]] = relationship(back_populates="client")
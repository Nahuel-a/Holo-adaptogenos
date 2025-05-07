from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from core.config import get_settings

settings = get_settings()

async_engine = create_async_engine(
    settings.DATABASE_URL, echo=settings.DEBUG
)

AsyncSessionLocal = sessionmaker(
    bind=async_engine, 
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass


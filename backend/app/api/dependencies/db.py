from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import AsyncSessionLocal

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get a database session.
    Yields:
        AsyncSession: An asynchronous database session.
    """
    async with AsyncSessionLocal() as session:
        yield session

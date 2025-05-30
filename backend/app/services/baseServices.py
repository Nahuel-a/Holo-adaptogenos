from typing import Generic, TypeVar, Type, Optional
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase

TModel = TypeVar('TModel', bound=DeclarativeBase)
TCreate = TypeVar('TCreate', bound=BaseModel)
TUpdate = TypeVar('TUpdate', bound=BaseModel)

class BaseService(Generic[TModel, TCreate, TUpdate]):
    def __init__(self, model:Type[TModel]):
        self.model = model

    async def get (self, db: AsyncSession, model_id:int)-> Optional[TModel]:
        try:
            statement = select(self.model).where(self.model.id == model_id)
            result = await db.execute(statement)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error fetching {self.model.__name__} with id {model_id}") from e

    async def get_all(self, db: AsyncSession)-> list[TModel]:
        try:
            statement = select(self.model)
            result = await db.execute(statement)
            return result.scalars().all()
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error fetching all {self.model.__name__}") from e
        
    async def create(self, db: AsyncSession, data: TCreate) -> TModel:
        try:
            instance =self.model(**data.model_dump())
            db.add(instance)
            await db.commit()
            await db.refresh(instance)
            return instance
        except SQLAlchemyError as e:
            await db.rollback()
            raise RuntimeError(f'Error creating {self.model.__name__}') from e

    async def update(self, db: AsyncSession, model_id: int, data: TUpdate) -> Optional[TModel]:
        try:
            statement = select(self.model).where(self.model.id == model_id)
            result = await db.execute(statement)
            instance = result.scalar_one_or_none()
            if not instance:
                return None
            for key, value in data.model_dump().items():
                setattr(instance, key, value)
            await db.commit()
            await db.refresh(instance)
            return instance
        except SQLAlchemyError as e:
            await db.rollback()
            raise RuntimeError(f'Error updating {self.model.__name__} with id {model_id}') from e
    
    async def delete(self, db: AsyncSession, model_id: int) -> bool:
        try:
            statement = select(self.model).where(self.model.id == model_id)
            result = await db.execute(statement)
            instance = result.scalar_one_or_none()
            if not instance:
                return False
            await db.delete(instance)
            await db.commit()
            return True
        except SQLAlchemyError as e:
            await db.rollback()
            raise RuntimeError(f'Error deleting {self.model.__name__} with id {model_id}') from e
        

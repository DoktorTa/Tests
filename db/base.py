import os
from collections.abc import AsyncGenerator
from typing import Any

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(os.getenv('DATABASE_URL'), echo=False)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    """ Получить сессию """
    async with async_session() as session, session.begin():
        yield session


async def create_models() -> None:
    """ Создает таблицы в бд, если они не созданы """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

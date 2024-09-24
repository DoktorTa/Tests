import os
from collections.abc import AsyncGenerator
from typing import Any

from asyncpg.transaction import ISOLATION_LEVELS
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

async_engine = create_async_engine(
    os.getenv('DATABASE_URL'),
    echo=False,
    isolation_level='serializable'
)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def create_models() -> None:
    """ Создает таблицы в бд, если они не созданы """
    print('Start models create')
    async with async_engine.begin() as conn:
        print('models create p 1', Base.metadata.info)
        await conn.run_sync(Base.metadata.create_all)

""" Defines functions to create and manage asynchronous database sessions. """
from typing import AsyncGenerator

from sqlalchemy import QueuePool
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from conf.config import settings


def create_engine() -> AsyncEngine:
    """
    Creates an asynchronous database engine.

    Returns:
    - AsyncEngine: Asynchronous engine for database connections.
    """
    return create_async_engine(
        settings.DB_URL,
        poolclass=QueuePool,
        connect_args={
            'statement_cache_size': 0,
        },
    )


def create_session(engine: AsyncEngine | None = None) -> async_sessionmaker[AsyncSession]:
    """
    Creates an asynchronous session for database operations.

    Args:
    - engine (AsyncEngine, optional): Asynchronous engine to bind the session to.
      If not provided, a new engine will be created.

    Returns:
    - async_sessionmaker[AsyncSession]: Asynchronous session maker for creating sessions.
    """
    return async_sessionmaker(
        bind=engine or create_engine(),
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False,
    )


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Asynchronous generator function to get a database session.

    Yields:
    - AsyncSession: Asynchronous session for database operations.
    """
    async with async_session() as session:
        yield session


engine = create_engine()
async_session = create_session(engine)

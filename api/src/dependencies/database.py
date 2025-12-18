from typing import Annotated
from urllib.parse import quote

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from src.dependencies.config import Config, get_config
from src.dependencies.logger import Logger, get_logger

config: Config = get_config()
logger: Logger = get_logger()


_engine: AsyncEngine | None = None


async def create_engine() -> AsyncEngine:
    url = config.database.url
    if not url:
        url = (
            f"{config.database.kind}+{config.database.adapter}://"
            f"{config.database.username}:{quote(config.database.password)}@"
            f"{config.database.host}:{config.database.port}/"
            f"{config.database.name}"
        )

    logger.info(f"creating database engine: {url}")

    return create_async_engine(url=url, echo=True, future=True)


async def init():
    import asyncio

    from alembic import command
    from alembic.config import Config as AlembicConfig

    await asyncio.to_thread(
        command.upgrade, config=AlembicConfig("db/alembic.ini"), revision="head"
    )

    # Create and store a single AsyncEngine instance for the lifetime of the app
    global _engine
    if _engine is None:
        logger.info("creating global async database engine")
        _engine = await create_engine()


async def get_engine() -> AsyncEngine:
    """
    Return the global AsyncEngine instance.
    Falls back to lazy initialization if init() was not awaited for some reason.
    """
    global _engine
    if _engine is None:
        logger.warning(
            "database engine not initialized in init(), creating lazily"
        )
        _engine = await create_engine()
    return _engine


async def aget_session(
    engine: Annotated[AsyncEngine, Depends(get_engine)],
) -> AsyncSession:
    logger.info("creating database session")

    session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )

    async with session() as session:
        yield session
        await session.close()

    logger.info("closing database session")


Database = Annotated[AsyncSession, Depends(aget_session)]

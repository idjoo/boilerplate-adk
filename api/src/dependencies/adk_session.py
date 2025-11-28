from typing import Annotated
from urllib.parse import quote

from fastapi import Depends
from google.adk.sessions import BaseSessionService, DatabaseSessionService

from .config import Config


async def aget_adk_session(config: Config) -> BaseSessionService:
    db_url = config.database.url
    if not db_url:
        db_url = (
            f"{config.database.kind}+{config.database.adapter}://"
            f"{config.database.username}:{quote(config.database.password)}@"
            f"{config.database.host}:{config.database.port}/"
            f"{config.database.name}"
        )
    return DatabaseSessionService(db_url=db_url)


AdkSession = Annotated[BaseSessionService, Depends(aget_adk_session)]

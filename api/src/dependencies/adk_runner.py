from typing import Annotated
from urllib.parse import urljoin

from fastapi import Depends
from google.adk.agents.remote_a2a_agent import (
    AGENT_CARD_WELL_KNOWN_PATH,
    RemoteA2aAgent,
)
from google.adk.runners import Runner

from .adk_session import AdkSession
from .config import Config


async def aget_adk_runner(
    config: Config, session_service: AdkSession
) -> Runner:
    return Runner(
        app_name=config.service,
        agent=RemoteA2aAgent(
            name="root_agent",
            agent_card=(urljoin(config.ai.url, AGENT_CARD_WELL_KNOWN_PATH)),
        ),
        session_service=session_service,
    )


AdkRunner = Annotated[Runner, Depends(aget_adk_runner)]

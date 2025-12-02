from typing import Annotated

import vertexai
from fastapi import Depends
from vertexai import agent_engines
from vertexai.agent_engines import AdkApp

from .config import Config, get_config


async def init():
    config: Config = get_config()
    vertexai.init(
        project=config.agent.project,
        location=config.agent.location,
    )


async def aget_agent(config: Config) -> AdkApp:
    return agent_engines.get(config.agent.resource)


Agent = Annotated[AdkApp, Depends(aget_agent)]

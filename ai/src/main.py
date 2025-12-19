import asyncio
import os

import httpx
import uvicorn
from a2a.types import AgentCard
from google.adk.a2a.utils.agent_card_builder import AgentCardBuilder
from google.adk.a2a.utils.agent_to_a2a import to_a2a

from src.config import Environment, get_config

from .agent import root_agent

config = get_config()


async def get_rpc_url() -> str:
    def metadata_google_internal(path: str):
        return httpx.get(
            f"http://metadata.google.internal/computeMetadata/v1/{path}",
            headers={"Metadata-Flavor": "Google"},
        ).text

    if os.environ.get("K_SERVICE"):
        service = os.environ.get("K_SERVICE")
        project_number = metadata_google_internal("project/numeric-project-id")
        region = metadata_google_internal("instance/region")
        return f"https://{service}-{project_number}.{region.split('/')[-1]}.run.app"
    else:
        return f"http://{config.host}:{config.port}"


async def get_agent_card() -> AgentCard:
    agent_card_builder = AgentCardBuilder(
        agent=root_agent,
        rpc_url=await get_rpc_url(),
    )
    return await agent_card_builder.build()


app = to_a2a(root_agent, agent_card=asyncio.run(get_agent_card()))


# ===============
# WSGI
# ===============
def server():
    uvicorn.run(
        app="src:app",
        host=config.host,
        port=config.port,
        log_level=config.logging.level.lower(),
        reload=True if config.environment == Environment.LOCAL else False,
    )

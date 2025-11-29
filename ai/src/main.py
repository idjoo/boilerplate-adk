import uvicorn
from google.adk.a2a.utils.agent_to_a2a import to_a2a

from src.config import get_config

from .agent import root_agent

config = get_config()
app = to_a2a(root_agent, host=config.host, port=config.port)


# ===============
# WSGI
# ===============
def server():
    uvicorn.run(
        app="src:app",
        host=config.host,
        port=config.port,
        log_level=config.logging.level.lower(),
        reload=True if config.environment == Environment.DEV else False,
    )
import uvicorn
from google.adk.a2a.utils.agent_to_a2a import to_a2a

from .agent import root_agent

app = to_a2a(root_agent, host="0.0.0.0", port=8081)


# ===============
# WSGI
# ===============
def server():
    uvicorn.run(app="src:app", host="0.0.0.0", port=8081)

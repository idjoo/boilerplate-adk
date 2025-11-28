import uvicorn
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
)

app = to_a2a(root_agent, host="0.0.0.0", port=8081)


# ===============
# WSGI
# ===============
def server():
    uvicorn.run(app="src:app", host="0.0.0.0", port=8081)

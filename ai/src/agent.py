from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search

root_agent = Agent(
    name="General",
    model=Gemini(
        model="gemini-3-pro-preview",
        use_interactions_api=True,
    ),
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
    tools=[google_search],
)

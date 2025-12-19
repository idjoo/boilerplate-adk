from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    name="General",
    model="gemini-3-pro-preview",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
)

from google.adk import Agent
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
    tools=[PreloadMemoryTool()],
)

from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools import google_search, preload_memory


async def auto_save_session(callback_context: CallbackContext):
    await callback_context._invocation_context.memory_service.add_session_to_memory(
        callback_context._invocation_context.session
    )


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
    tools=[preload_memory, google_search],
    after_agent_callback=[auto_save_session],
)

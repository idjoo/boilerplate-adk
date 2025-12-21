# Agent Development Guide

The project contains the AI Agent implementation using Google ADK.

## Development Workflow

1.  **Dependency Management**:
    - Add a package: `uv add <package>`

2.  **Running Locally**:
    - `uv run adk web` starts a local web interface to interact with your agent.
    - `uv run app` starts the A2A compatible server.

## Creating Agents and Tools

### Agents

Agents are defined in `src/agent.py` or `src/agents/`. An agent typically uses a specific model and has access to a set of tools.

```python
# Example Agent Definition
from google.adk.core import Agent

agent = Agent(
    name="my-agent",
    model="gemini-1.5-flash",
    tools=[my_tool]
)
```

### Tools

Tools are functions that the Agent can call. Define them in `src/tools/`.

```python
# Example Tool
from google.adk.core import tool

@tool
def my_tool(param: str) -> str:
    """Description of what the tool does."""
    return f"Processed {param}"
```

## Testing

Write unit tests for your tools in `tests/` (if created) or ensure your tools are pure functions where possible.

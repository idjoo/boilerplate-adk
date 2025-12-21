# Architecture & Design

This project contains an **AI Agent** built with the Google Agent Development Kit (ADK).

## Folder Structure

```
boilerplate-adk/
├── src/
│   ├── agent.py    # Root Agent definition
│   ├── agents/     # Sub-agents
│   ├── tools/      # Agent Tools
│   └── main.py     # Entrypoint
├── ci/             # CI/CD configurations
└── docs/           # Documentation
```

## Components

### AI Agent

The AI component is built using **Google ADK (Agent Development Kit)** and **A2A (Agent 2 Agent)** SDK.

- **Agent**: Defined in `src/agent.py`. It orchestrates the logic.
- **Tools**: located in `src/tools/`. Functions exposed to the LLM.
- **A2A Wrapper**: `src/main.py` wraps the agent in a FastAPI service compatible with the A2A protocol.


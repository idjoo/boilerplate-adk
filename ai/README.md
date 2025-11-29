# Agent Boilerplate

## Environment Variables

```bash
export GOOGLE_GENAI_USE_VERTEXAI=1
export GOOGLE_CLOUD_PROJECT=lv-playground-genai
export GOOGLE_CLOUD_LOCATION=global
```

## Running the Agent

```bash
uv run app
```

## Project Structure

```
 .
 ├── README.md
 ├── src/
 │   ├── __init__.py
 │   ├── agents/
 │   │   ├── __init__.py
 │   │   └── example_agent.py
 │   ├── tools/
 │   │   ├── __init__.py
 │   │   └── example_tool.py
 │   ├── agent.py
 │   └── main.py
 └── pyproject.toml
```

- `README.md`: This file.
- `src/`: The source code directory.
- `src/agent.py`: This should contain the root agent.
- `src/agents/`: The agents directory if you have multiple agents.
- `src/tools/`: The tools directory if you have multiple tools.
- `src/main.py`: This file contains functions to run the agent.
- `pyproject.toml`: The project configuration file.
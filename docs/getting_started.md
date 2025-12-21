# Getting Started

## Prerequisites

Ensure you have the following installed:

- **Python 3.13+** (Required)
- **Docker** & **Docker Compose** (for containerization and local DB)
- **uv** (Required for dependency management)
- **gcloud CLI** (For Google Cloud interactions)

## Installation

1.  **Clone the repository:**

    ```sh
    git clone <your-repo-url>
    cd boilerplate-adk
    ```

## Setup

**Install Dependencies:**

```sh
uv sync
```

**Environment Variables:**

Set the required environment variables:

```sh
export GOOGLE_GENAI_USE_VERTEXAI=1
export GOOGLE_CLOUD_PROJECT=<your-project-id>
export GOOGLE_CLOUD_LOCATION=<your-location>
```

**Run the Agent:**

To run as an A2A (Agent-to-Agent) service:

```sh
uv run app
```

To run using the ADK CLI:

```sh
uv run adk web
```


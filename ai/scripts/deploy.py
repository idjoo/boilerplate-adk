import argparse
import tomllib
from pathlib import Path

import vertexai
from pydantic import BaseModel
from vertexai import agent_engines

from src.agent import root_agent


class Config(BaseModel):
    name: str
    description: str = ""
    dependencies: list[str]


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project",
        default="lv-playground-genai",
    )
    parser.add_argument(
        "--region",
        default="asia-southeast2",
    )
    parser.add_argument(
        "--bucket",
        default="gs://lv-playground-genai_cloudbuild",
        help="GCS staging bucket",
    )
    return parser.parse_args()


def get_config() -> Config:
    pyproject_path = Path.cwd() / "pyproject.toml"
    data = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
    return Config(**(data.get("project", {})))


def get_agent(config: Config, kwargs: dict):
    agents = agent_engines.list(filter=f'display_name="{config.name}"')
    for agent in agents:
        return agent
    agent_engines.create(**kwargs)


def main() -> None:
    args = get_args()
    config = get_config()

    vertexai.init(
        project=args.project,
        location=args.region,
        staging_bucket=args.bucket
        if "gs://" in args.bucket
        else f"gs://{args.bucket}",
    )

    cpu = 1
    memory = 1
    kwargs = {
        "agent_engine": root_agent,
        "display_name": config.name,
        "description": config.description or config.name,
        "requirements": config.dependencies,
        "extra_packages": ["./src/"],
        "env_vars": {
            "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY": "true",
            "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT": "true",
        },
        "min_instances": 0,
        "max_instances": 10,
        "resource_limits": {"cpu": f"{cpu}", "memory": f"{memory}Gi"},
        "container_concurrency": 2 * cpu + 1,
    }

    agent = get_agent(config, kwargs)
    if agent:
        agent_engines.update(
            resource_name=agent.resource_name,
            **kwargs,
        )


if __name__ == "__main__":
    main()

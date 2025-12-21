# Observability

This boilerplate includes built-in observability using **Google Cloud Logging** and **OpenTelemetry**.

## Logging

Structured JSON logging is configured to work out-of-the-box with Cloud Logging.

- **Agent**: Ensure you use the provided logging mechanisms or standard Python logging, which will be captured by the container runtime.

## Tracing

**OpenTelemetry** is integrated to provide distributed tracing.

- **Google Cloud Trace**: Traces are exported to Google Cloud Trace when running in the cloud.

## Configuration

You can configure observability settings in `config.yaml` or via environment variables:

- `LOG_LEVEL`: Set the logging level (INFO, DEBUG, etc.).
- `OTEL_ENABLE`: Enable/Disable tracing.

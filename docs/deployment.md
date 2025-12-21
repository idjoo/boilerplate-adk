# Deployment

The AI service is containerized and designed to be deployed to **Google Cloud Run**.

## CI/CD Pipeline

The project includes Cloud Build configurations in the `ci/` directory.

- `ci/cloud-build.yaml`: Builds the container image.
- `ci/cloud-run.yaml`: Deploys the container to Cloud Run.

## Deploying Manually

### Agent Deployment

```sh
gcloud builds submit --config ci/cloud-build.yaml .
```

## Docker

You can build the image locally using the Dockerfile provided in `ci/Dockerfile`.

```sh
docker build -f ci/Dockerfile -t my-agent .
```

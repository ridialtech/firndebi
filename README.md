# Sample CI/CD Pipeline

This repository contains an example GitHub Actions workflow for a project with a Django backend and a Next.js frontend using a PostgreSQL database.

The workflow located in `.github/workflows/ci-cd.yml` performs the following steps:

1. Checks out the code.
2. Sets up Python and Node.js environments.
3. Starts a PostgreSQL service for tests.
4. Installs backend and frontend dependencies.
5. Runs backend and frontend tests. The provided `backend` and `frontend` directories only contain placeholder files so these tests are trivial.

The backend includes sample unit tests for simple auth and diploma logic.
It also contains an integration test that checks the end-to-end flow of
authenticating a user and validating one of their diplomas.

6. Builds Docker images for the backend and frontend if tests succeed.
7. Pushes these images to Docker Hub. The workflow expects `DOCKER_USERNAME` and
   `DOCKER_TOKEN` secrets for authentication.
8. Deploys the application (replace the deployment step with your actual deployment commands).

The `backend/requirements.txt`, `frontend/package.json`, and their `Dockerfile`s are minimal examples so the CI workflow can run even before real code is added.

## Local tasks

A `Makefile` is provided to run common development tasks:

- `make test_backend` – run backend unit and integration tests
- `make test_frontend` – run frontend tests
- `make all_tests` – run both backend and frontend tests
- `make build_backend` / `make build_frontend` – build Docker images
- `make push_backend` / `make push_frontend` – push Docker images (requires a valid `DOCKER_USERNAME`)



---
openspp:
  doc_status: unverified
---

# Installation Guide

## Installing using Docker (recommended)

### Quick start

The recommended Docker deployment workflow uses the `openspp-docker` repository.

You need to have Docker and Docker Compose installed. For the helper commands, you also need Python and the Python
packages used by the `openspp-docker` tooling (for example `invoke`).

```bash
git clone https://github.com/OpenSPP/openspp-docker.git
cd openspp-docker

# Create the development environment
invoke develop

# Pull / build images (depending on your local setup)
invoke img-pull
invoke img-build

# Download aggregated repositories (addons)
invoke git-aggregate

# Create a fresh database and start the stack
invoke resetdb
invoke start
```

Then open `http://localhost:17069/` in your browser.

```{note}
The exact commands and ports can vary depending on the `openspp-docker` configuration you are using. Use the
`openspp-docker` README as the reference for your deployment.
```

## Local development / E2E environment (advanced)

```{note}
The `openspp-modules-v2` repository contains a Docker Compose setup under `e2e/` for end-to-end testing and local
validation. It is intended for testing workflows, not as the primary deployment path.
```

## Installing for production

### Using Docker

For production deployments, use the `openspp-docker` repository and follow its production deployment guidance. It
packages the Docker configuration, addons aggregation, and operational conventions used by OpenSPP deployments.

# Installation Guide

## Installing using Docker (recommended)

### Quick start

You need:

- Docker
- Docker Compose
- Git

```bash
git clone https://github.com/OpenSPP/openspp-modules-v2.git
cd openspp-modules-v2
git checkout 19.0

# Start a local OpenSPP + PostgreSQL environment
docker compose -f e2e/docker-compose.yml up -d --build
```

Then open `http://localhost:8069/` in your browser.

Default credentials (from the provided compose file):

- Database: `e2e_test`
- Username: `admin`
- Password: `admin`

```{note}
The compose file in `e2e/docker-compose.yml` is designed for a complete local environment and uses the Dockerfile in the
repository to build an Odoo 19 image with OpenSPP modules.
```

## Installing for production

### Using Docker

OpenSPP can be deployed as a Docker container connected to PostgreSQL (with persistent volumes for the Odoo data
directory).

At minimum, the container entrypoint expects these environment variables:

- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`
- `ODOO_ADMIN_PASSWD`

For deployments behind a reverse proxy, set `PROXY_MODE=True`.

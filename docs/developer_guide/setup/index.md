---
openspp:
  doc_status: draft
  products: [core]
---

# Development setup

**For: developers**

This guide walks you through setting up a local OpenSPP development environment. OpenSPP V2 runs on **Odoo 19** (OCA/OCB) inside Docker — the container ships with **Python 3.13**. The only Python you install on your host is for the `spp` CLI (3.12+).

## Prerequisites

Before you begin, make sure you have:

| Tool                                                       | Version | Purpose                                |
| ---------------------------------------------------------- | ------- | -------------------------------------- |
| [Docker](https://docs.docker.com/get-docker/)              | 20.10+  | Container runtime                      |
| [Docker Compose](https://docs.docker.com/compose/install/) | V2+     | Multi-container orchestration          |
| [Git](https://git-scm.com/)                                | 2.30+   | Source control                         |
| Python                                                     | 3.12+   | Running the `spp` CLI (host-side only) |

## Clone the repository

```bash
git clone git@github.com:OpenSPP/OpenSPP2.git
cd OpenSPP2
```

## The `spp` CLI

OpenSPP includes a developer CLI that wraps common Docker Compose operations. Activate it by sourcing the `activate` script:

```bash
. ./activate
```

This adds `spp` to your PATH and enables tab completion (bash/zsh). You can verify your setup with:

```bash
spp doctor
```

### Command reference

| Command       | Alias | Purpose                          |
| ------------- | ----- | -------------------------------- |
| `spp start`   | `s`   | Start the development server     |
| `spp stop`    | —     | Stop all services                |
| `spp restart` | `r`   | Restart the Odoo container       |
| `spp test`    | `t`   | Run module tests                 |
| `spp update`  | `u`   | Update changed modules           |
| `spp logs`    | `l`   | View container logs              |
| `spp shell`   | `sh`  | Open Odoo interactive shell      |
| `spp sql`     | —     | Open PostgreSQL shell or run SQL |
| `spp url`     | —     | Show or open the dev server URL  |
| `spp lint`    | —     | Run linters on files             |
| `spp build`   | `b`   | Build Docker images              |
| `spp status`  | `st`  | Show service status              |
| `spp doctor`  | —     | Check prerequisites              |

### Configuration

You can create a `~/.spp.toml` file to set your defaults:

```toml
default_demo = "mis"
default_profile = "dev"
default_db = "openspp"
```

## Start the development server

```bash
spp start --demo mis
```

This command:

1. Builds the Docker image if needed (checks dependency freshness on each run)
2. Starts PostgreSQL 18 with PostGIS
3. Starts the Odoo server with the MIS demo modules installed
4. Starts the job worker for background tasks

The `--demo` flag specifies which demo data to load:

| Profile | Module              | Description                        |
| ------- | ------------------- | ---------------------------------- |
| `mis`   | `spp_mis_demo_v2`   | Full social protection MIS         |
| `drims` | `spp_drims_sl_demo` | Disaster relief (Sri Lanka config) |
| `grm`   | `spp_grm_demo`      | Grievance redress mechanism        |

You can also pass a module name directly: `spp start --demo spp_base_common`.

### Access the application

By default, the `dev` profile uses a dynamic port to avoid conflicts. Find the assigned port with:

```bash
spp url
```

Or open it directly in your browser:

```bash
spp url --open
```

If you need a fixed port (for example, when connecting external tools), use the `ui` profile:

```bash
spp start --demo mis --profile ui
```

This binds Odoo to `http://localhost:8069`.

**Default credentials:** `admin` / `admin`

### Docker Compose profiles

Under the hood, `spp start` runs Docker Compose with profiles:

| Profile | Purpose                                        |
| ------- | ---------------------------------------------- |
| `dev`   | Development server with dynamic port (default) |
| `ui`    | Fixed port 8069 for UI development             |
| `e2e`   | End-to-end testing environment with Playwright |

You can also use Docker Compose directly:

```bash
docker compose --profile dev up -d
docker compose --profile dev ps    # Shows assigned port
```

### Services

The development environment runs these services:

| Service                   | Image                           | Purpose                        |
| ------------------------- | ------------------------------- | ------------------------------ |
| `db`                      | `postgis/postgis:18-3.6-alpine` | PostgreSQL 18 with PostGIS     |
| `openspp` / `openspp-dev` | Built from `docker/Dockerfile`  | Odoo web server                |
| `jobworker`               | Same image                      | Background job queue processor |

## Common development tasks

### View logs

```bash
spp logs                        # All services
spp logs openspp -f --tail=100  # Follow Odoo logs
```

### Auto-reload

The `dev` profile enables auto-reload by default (`--dev=reload,qweb,xml`). This means most Python code changes are picked up automatically without restarting the container. You will see a "Watching for file changes" message in the logs.

To disable auto-reload:

```bash
spp start --demo mis --no-watch
```

### Restart Odoo

Some changes require a manual restart (e.g., adding new files, changing `__init__.py` imports, modifying `__manifest__.py` dependencies):

```bash
spp restart
```

### Update modules

When you change module files (models, views, data), update the affected modules:

```bash
spp update
```

This auto-detects which modules have changed by comparing checksums.

### Open a shell

```bash
spp shell        # Odoo interactive shell
spp sql          # PostgreSQL shell (psql)
spp sql "SELECT id, name FROM spp_program LIMIT 5;"
```

### Install a new module

If you're developing a new module and want to install it, you can either:

- **Via the CLI** — restart with the module specified:

  ```bash
  spp stop
  ODOO_INIT_MODULES=spp_my_module spp start
  ```

- **Via the Odoo UI** — go to **Apps**, click **Update Apps List**, search for your module, and click **Install**.

### Reset the database

```bash
spp resetdb --demo mis
```

This drops the current database and recreates it with the specified demo data. You will be prompted to confirm.

Alternatively, you can wipe everything and start fresh in one step:

```bash
spp start --demo mis --wipe
```

### Stop the environment

```bash
spp stop
```

To also remove volumes (full cleanup):

```bash
docker compose --profile dev down -v
```

## Running tests

Run tests for a specific module in an isolated database:

```bash
spp test spp_registry
```

This creates a temporary test database, runs the tests, and reports results. Your development database is not affected.

Run with specific test tags:

```bash
spp test spp_programs --tags=post_install
```

Test output is displayed in your terminal. Detailed logs are also saved inside the container at `/tmp/openspp-test-logs/`.

## Code quality tools

### Pre-commit hooks

OpenSPP uses pre-commit hooks to enforce code standards. Install them with:

```bash
pip install pre-commit
pre-commit install
```

The hooks run automatically on `git commit` and include:

- **Ruff** — Python linting and formatting (line length: 120, target: Python 3.12+)
- **Prettier** — Formatting for CSS, HTML, JSON, YAML, XML
- **ESLint** — JavaScript validation
- **Pylint-Odoo** — Odoo-specific checks (valid versions: 19.0)
- **Gitleaks** — Secret detection
- **Bandit** — Python security scanning
- **Semgrep** — Static analysis with OpenSPP custom rules
- **OpenSPP custom linting** — Naming conventions, PII-in-logs detection, API security, Odoo 19 compatibility

### Run linters manually

```bash
spp lint                          # Lint changed files (default)
spp lint spp_programs/models/programs.py   # Lint specific files
```

You can also run pre-commit directly for more control:

```bash
pre-commit run --all-files        # All hooks on all files
pre-commit run ruff --all-files   # Specific hook on all files
```

### Key code style settings

| Setting              | Value                                                                     |
| -------------------- | ------------------------------------------------------------------------- |
| Line length          | 120                                                                       |
| Python target        | 3.12+                                                                     |
| Indent (Python, XML) | 4 spaces                                                                  |
| Indent (JSON, YAML)  | 2 spaces                                                                  |
| Line endings         | LF                                                                        |
| Import order         | future, stdlib, third-party, odoo, odoo-addons, first-party, local-folder |

## Environment variables

These environment variables configure the Odoo container:

### Required

| Variable            | Default   | Description         |
| ------------------- | --------- | ------------------- |
| `DB_HOST`           | —         | PostgreSQL hostname |
| `DB_PORT`           | `5432`    | PostgreSQL port     |
| `DB_USER`           | —         | Database user       |
| `DB_PASSWORD`       | —         | Database password   |
| `DB_NAME`           | `openspp` | Database name       |
| `ODOO_ADMIN_PASSWD` | —         | Admin user password |

### Optional

| Variable              | Default                | Description                                            |
| --------------------- | ---------------------- | ------------------------------------------------------ |
| `DATABASE_URL`        | —                      | Full connection URL (overrides individual `DB_*` vars) |
| `ODOO_INIT_MODULES`   | —                      | Comma-separated modules to install on startup          |
| `ODOO_UPDATE_MODULES` | —                      | Comma-separated modules to update on startup           |
| `ODOO_WORKERS`        | `0` (dev) / `2` (prod) | Number of worker processes                             |
| `LOG_LEVEL`           | `info`                 | Log level: `debug`, `info`, `warn`, `error`            |
| `PROXY_MODE`          | `False` (dev)          | Enable when behind a reverse proxy                     |

```{note}
When using the `spp` CLI, these variables are managed automatically. You only need to set them when running Docker Compose directly or deploying to production.
```

## Project structure

```
OpenSPP2/
├── spp_base_common/         # Core foundation module
├── spp_registry/            # Registrant management
├── spp_programs/            # Program management
├── spp_*                    # Other OpenSPP modules (~110 total)
├── docker/
│   ├── Dockerfile           # Multi-stage build (builder → runtime → dev → production)
│   ├── entrypoint.sh        # Container startup and DB initialization
│   ├── odoo.conf.template   # Odoo configuration template
│   ├── requirements.txt     # Additional Python dependencies
│   └── requirements-dev.txt # Dev-only tools (debugpy, pudb, watchdog)
├── scripts/
│   └── test_single_module.sh  # Test runner script
├── docker-compose.yml       # Development Docker Compose
├── spp                      # Developer CLI
├── activate                 # CLI activation script
├── requirements.txt         # Core Python dependencies (from manifests)
├── pyproject.toml           # Project configuration
├── .pre-commit-config.yaml  # Pre-commit hook configuration
├── .ruff.toml               # Ruff linter configuration
├── .pylintrc                # Pylint configuration (optional checks)
├── .pylintrc-mandatory      # Pylint configuration (blocking checks)
└── .editorconfig            # Editor settings
```

## IDE configuration

### VS Code

Recommended extensions for OpenSPP development:

- **Python** (ms-python.python)
- **Pylance** (ms-python.vscode-pylance)
- **Ruff** (charliermarsh.ruff)
- **XML** (redhat.vscode-xml)

### Remote debugging

The dev Docker image includes `debugpy` for remote debugging. Configure your IDE to attach to the debugger on the standard port.

## Are you stuck?

- **Docker image won't build?** Run `spp doctor` to check prerequisites.
- **Module not found?** Make sure it's in the addons path. OpenSPP modules are mounted at `/mnt/extra-addons/openspp` inside the container.
- **Database errors after code changes?** Try `spp update` to apply pending migrations, or `spp resetdb --demo mis` for a clean slate.
- **Port conflict?** The `dev` profile uses a dynamic port. Use `spp url` to find the assigned port, or switch to `--profile ui` for a fixed port.
- **Pre-commit hooks failing?** Run `pre-commit run --all-files` to identify issues, or `pre-commit run ruff --all-files` to auto-fix Python formatting.

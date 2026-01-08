---
openspp:
  doc_status: draft
---

# Docker Installation

This guide is for **sys admins** and **evaluators** setting up OpenSPP using Docker. You'll have a running instance in under 5 minutes.

## Prerequisites

### Install Docker

**Ubuntu/Debian:**
```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Logout and login for group changes to take effect
```

**macOS:** Download and install [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/).

**Windows:** Install [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/) with WSL2 backend.

### Install Git

```shell
# Ubuntu/Debian
sudo apt-get install git

# macOS (via Homebrew)
brew install git
```

### Verify Installation

```shell
docker --version          # Expected: 24.0+
docker compose version    # Expected: v2.20+
git --version             # Expected: 2.30+
```

## Quick Start

```shell
# Clone the repository
git clone https://github.com/OpenSPP/openspp-modules-v2.git
cd openspp-modules-v2

# Start OpenSPP
docker compose --profile ui up -d

# Wait for initialization (~60-90 seconds on first run)
docker compose logs -f odoo
# Look for: "registry: X modules loaded in Y.ZZs"
# Press Ctrl+C to exit logs

# Find the port
docker compose port odoo 8069
# Output: 0.0.0.0:XXXXX -> open http://localhost:XXXXX
```

**Default credentials:** `admin` / `admin`

## What Just Happened?

The Docker setup started two containers:

| Container | Purpose |
|-----------|---------|
| `db` | PostgreSQL 18 with PostGIS 3.6 (spatial extensions) |
| `odoo` | Odoo 19 with OpenSPP modules |

On first startup, OpenSPP:
1. Creates the database
2. Installs the base OpenSPP module (`spp_base`)
3. Sets up the admin user

## Configuration

Set environment variables before starting:

```shell
# Example: Use a demo module with sample data
ODOO_INIT_MODULES=spp_mis_demo_v2 docker compose --profile ui up -d
```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ODOO_DB_NAME` | `openspp` | Database name |
| `ODOO_INIT_MODULES` | `spp_base` | Modules to install on startup |
| `ODOO_UPDATE_MODULES` | (empty) | Modules to update on restart |
| `ODOO_ADMIN_PASSWD` | `admin` | Master password for database management |

### Available Demo Modules

| Module | Description |
|--------|-------------|
| `spp_base` | Minimal installation (default) |
| `spp_mis_demo_v2` | Sample registry with programs and beneficiaries |
| `spp_drims_sl_demo` | DRIMS disaster response demo |

## Common Operations

| Task | Command |
|------|---------|
| Start | `docker compose --profile ui up -d` |
| Stop | `docker compose --profile ui down` |
| View logs | `docker compose logs -f odoo` |
| Restart Odoo | `docker compose --profile ui restart odoo` |
| Find port | `docker compose port odoo 8069` |
| Shell into container | `docker compose exec odoo bash` |

### Rebuilding After Updates

```shell
# Pull latest code
git pull

# Rebuild and restart
docker compose --profile ui up -d --build
```

### Update Installed Modules

To update modules after code changes:

```shell
ODOO_UPDATE_MODULES=spp_registry,spp_programs docker compose --profile ui up -d
```

## Database Management

### Backup

```shell
# Create a backup
docker compose exec db pg_dump -U odoo openspp | gzip > backup_$(date +%Y%m%d).sql.gz
```

### Restore

```shell
# Stop Odoo first
docker compose --profile ui stop odoo

# Drop and recreate database
docker compose exec db dropdb -U odoo openspp
docker compose exec db createdb -U odoo openspp

# Restore backup
gunzip -c backup_20250108.sql.gz | docker compose exec -T db psql -U odoo openspp

# Start Odoo
docker compose --profile ui start odoo
```

### Reset Database

To start fresh with a clean database:

```shell
# Stop everything and remove volumes
docker compose down -v

# Start fresh
docker compose --profile ui up -d
```

## Are You Stuck?

**Container won't start**
```shell
# Check container logs
docker compose logs odoo
docker compose logs db

# Common issue: port conflict
docker compose port odoo 8069
# If empty, check if port 8069 is in use: sudo lsof -i :8069
```

**Can't login with admin/admin**
The admin password is set during first database initialization. If you've changed it or can't remember:
```shell
# Reset by recreating the database
docker compose down -v
docker compose --profile ui up -d
```

**Database connection refused**
```shell
# Check if database is healthy
docker compose ps
# db should show "healthy" status

# If not, check db logs
docker compose logs db
```

**Modules not loading**
```shell
# Check ODOO_INIT_MODULES is set correctly
docker compose exec odoo printenv | grep ODOO

# Force reinstall
docker compose down -v
ODOO_INIT_MODULES=spp_mis_demo_v2 docker compose --profile ui up -d
```

**Out of disk space**
```shell
# Clean up unused Docker resources
docker system prune -a
```

## Next Steps

- {doc}`../first_program/index` - Create your first social protection program
- {doc}`/user_guide/index` - Learn the OpenSPP interface
- {doc}`/config_guide/index` - Configure eligibility rules and expressions

## Production Considerations

This Docker setup is designed for **evaluation and development**. For production deployments, consider:

- Use a managed PostgreSQL service (AWS RDS, Azure Database, GCP Cloud SQL)
- Set strong passwords for database and admin accounts
- Configure SSL/TLS with a reverse proxy (Nginx, Traefik)
- Set up regular automated backups
- Configure monitoring and alerting
- Review the {doc}`/ops_guide/index` for operational guidance

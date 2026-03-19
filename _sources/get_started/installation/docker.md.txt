---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Docker installation

This guide is for **sys admins** and **evaluators** setting up OpenSPP using Docker. You'll have a running instance in under 5 minutes.

## Prerequisites

### Install Docker

**Ubuntu/Debian:**
```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

:::{note}
You must log out and log back in for the group changes to take effect.
:::

**macOS:** Download and install [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/).

**Windows:** Install [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/) with WSL2 backend.

### Install Git

```shell
# Ubuntu/Debian
sudo apt-get install git

# macOS (via Homebrew)
brew install git
```

### Verify installation

```shell
docker --version          # Expected: 24.0+
docker compose version    # Expected: v2.20+
git --version             # Expected: 2.30+
```

## Quick start

```shell
# Clone the repository
git clone https://github.com/OpenSPP/OpenSPP2.git
cd OpenSPP2

# Start OpenSPP
docker compose --profile ui up -d

# Wait for initialization (~60-90 seconds on first run)
docker compose --profile ui logs -f openspp
# Look for: "Registry loaded in X.XXXs"
# Press Ctrl+C to exit logs

# Open http://localhost:8069 in your browser
```

:::{tip}
If port 8069 is already in use, Docker may assign a different port.
Find the assigned port by running:

```shell
docker compose --profile ui port openspp 8069
```
:::

:::{tip}
Add `--build` to the `up` command to force a rebuild when code or dependencies have changed:
`docker compose --profile ui up -d --build`
:::

:::{note}
**Default credentials:** `admin` / `admin`
:::

## What just happened?

The Docker setup started two containers:

| Container | Purpose |
|-----------|---------|
| `db` | PostgreSQL 18 with PostGIS 3.6 (spatial extensions) |
| `openspp` | Odoo 19 with OpenSPP modules |

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

### Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ODOO_DB_NAME` | `openspp` | Database name |
| `ODOO_INIT_MODULES` | `spp_base` | Modules to install on startup |
| `ODOO_UPDATE_MODULES` | (empty) | Modules to update on restart |
| `ODOO_ADMIN_PASSWD` | `admin` | Master password for database management |

### Available demo modules

| Module | Description |
|--------|-------------|
| `spp_base` | Minimal installation (default) |
| `spp_mis_demo_v2` | Sample registry with programs and beneficiaries |
| `spp_drims_sl_demo` | DRIMS disaster response demo |

## Common operations

| Task | Command |
|------|---------|
| Start | `docker compose --profile ui up -d` |
| Stop | `docker compose --profile ui down` |
| View logs | `docker compose --profile ui logs -f openspp` |
| Restart OpenSPP | `docker compose --profile ui restart openspp` |
| Shell into container | `docker compose --profile ui exec openspp bash` |

### Rebuilding after updates

```shell
# Pull latest code
git pull

# Rebuild and restart
docker compose --profile ui up -d --build
```

### Update installed modules

To update modules after code changes:

```shell
ODOO_UPDATE_MODULES=spp_registry,spp_programs docker compose --profile ui up -d
```

## Database management

### Backup

```shell
# Create a backup
docker compose exec db pg_dump -U odoo openspp | gzip > backup_$(date +%Y%m%d).sql.gz
```

### Restore

```shell
# Stop OpenSPP first
docker compose --profile ui stop openspp

# Drop and recreate database
docker compose exec db dropdb -U odoo openspp
docker compose exec db createdb -U odoo openspp

# Restore backup
gunzip -c backup_20250108.sql.gz | docker compose exec -T db psql -U odoo openspp

# Start OpenSPP
docker compose --profile ui start openspp
```

### Reset database

To start fresh with a clean database:

```shell
# Stop everything and remove volumes
docker compose down -v

# Start fresh
docker compose --profile ui up -d
```

## Are you stuck?

**Container won't start**

```shell
# Check container logs
docker compose --profile ui logs openspp
docker compose logs db
```

:::{tip}
A common cause is a port conflict on 8069. Check if another process is using it:
`sudo lsof -i :8069`
:::

**Can't login with admin/admin**
The admin password is set during first database initialization. If you've changed it or can't remember:
```shell
# Reset by recreating the database
docker compose down -v
docker compose --profile ui up -d
```

**Database connection refused**

```shell
docker compose ps
```

:::{tip}
The `db` container should show `healthy` status. If it does not, check the database logs:
`docker compose logs db`
:::

**Modules not loading**
```shell
# Check ODOO_INIT_MODULES is set correctly
docker compose --profile ui exec openspp printenv | grep ODOO

# Force reinstall
docker compose down -v
ODOO_INIT_MODULES=spp_mis_demo_v2 docker compose --profile ui up -d
```

**Out of disk space**
```shell
# Clean up unused Docker resources
docker system prune -a
```

## Next steps

- {doc}`../modules/index` - Install modules
- {doc}`../first_program/index` - Create your first social protection program
- {doc}`/user_guide/index` - Learn the OpenSPP interface
- {doc}`/config_guide/index` - Configure eligibility rules and expressions

## Production considerations

:::{warning}
This Docker setup is designed for **evaluation and development only**. For production deployments, consider:

- Use a managed PostgreSQL service (AWS RDS, Azure Database, GCP Cloud SQL)
- Set strong passwords for database and admin accounts
- Configure SSL/TLS with a reverse proxy (Nginx, Traefik)
- Set up regular automated backups
- Configure monitoring and alerting
- Review the {doc}`/ops_guide/index` for operational guidance
:::

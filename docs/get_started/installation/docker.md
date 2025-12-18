---
openspp:
  doc_status: draft
---

# Docker Installation

This guide is for **sys admins** installing OpenSPP using Docker containers. This is the recommended installation method for all deployment types.

Docker deployment uses the [openspp-docker](https://github.com/OpenSPP/openspp-docker) repository, which packages OpenSPP with Docker Compose, configuration management, and operational tooling based on the [Doodba](https://github.com/Tecnativa/doodba) framework.

## Prerequisites

Before starting, verify:

```shell
# Check Docker
docker --version
# Expected: Docker version 24.0+

# Check Docker Compose
docker compose version
# Expected: Docker Compose version v2.20+

# Check Python
python3 --version
# Expected: Python 3.8+

# Check Git
git --version
# Expected: git version 2.30+
```

If any command fails, see {doc}`index` for installation instructions.

## Installation Steps

### 1. Clone the Repository

```shell
# Clone openspp-docker
git clone https://github.com/OpenSPP/openspp-docker.git
cd openspp-docker
```

### 2. Install Python Dependencies

```shell
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install invoke and git-aggregator
pip install invoke git-aggregator
```

### 3. Initialize Development Environment

```shell
# Create .env and docker-compose.override.yml
invoke develop
```

This creates:
- `.env` - Environment variables
- `docker-compose.override.yml` - Local overrides
- Symlink `docker-compose.yml` → `devel.yaml`

### 4. Configure Environment

Edit `.env` to customize your installation:

| Variable | Default | Description |
|----------|---------|-------------|
| `ODOO_MAJOR` | 17 | Odoo version (don't change) |
| `ODOO_MINOR` | 17.0 | Minor version |
| `POSTGRES_VERSION` | 15 | PostgreSQL version |
| `POSTGRES_PASSWORD` | odoopassword | DB password (**change in production**) |
| `PGDATABASE` | prod | Database name |
| `PGUSER` | odoo | Database user |

**Example production `.env`:**

```shell
ODOO_MAJOR=17
ODOO_MINOR=17.0
POSTGRES_VERSION=15
POSTGRES_PASSWORD=<generate-strong-password>
PGDATABASE=openspp_prod
PGUSER=odoo_user
```

### 5. Pull Docker Images

```shell
# Pull pre-built images (faster)
invoke img-pull
```

**Or build locally** (for custom modifications):

```shell
invoke img-build
```

Building locally takes 15-30 minutes depending on your connection and CPU.

### 6. Download OpenSPP Code

```shell
# Aggregate all repositories
invoke git-aggregate
```

This downloads OpenSPP modules from GitHub. Takes 5-10 minutes.

**If you encounter SSH key errors:**

```shell
# Use HTTPS instead of SSH
invoke git-aggregate-host
```

### 7. Create Database

```shell
# Initialize fresh database with demo data
invoke resetdb
```

This will:
1. Stop containers
2. Remove existing database
3. Create new database
4. Start containers
5. Install OpenSPP modules
6. Load demo data

Takes 10-20 minutes.

**For production without demo data:**

```shell
# Create empty database
invoke resetdb --no-demo
```

### 8. Start OpenSPP

```shell
# Start all services
invoke start
```

**Verify startup:**

```shell
# Check all containers running
docker compose ps
# Expected: odoo, db, smtpfake all "Up"

# Watch logs
invoke logs
```

### 9. Access OpenSPP

Open your browser to:
- **URL:** http://localhost:17069
- **Email:** admin@example.com
- **Password:** admin

```{warning}
**Change the admin password immediately** in production:
Settings → Users & Companies → Users → Administrator
```

## Configuration

### Ports

| Service | Default Port | Change In |
|---------|--------------|-----------|
| Odoo HTTP | 17069 | `.env` → `ODOO_MAJOR` |
| PostgreSQL | 5432 | `docker-compose.override.yml` |
| SMTP (fake) | 8025 | `docker-compose.override.yml` |

### Persistent Data

Data persists in Docker volumes:

```shell
# List volumes
docker volume ls | grep openspp-docker

# Backup volumes
docker run --rm -v openspp-docker_filestore:/data \
  -v $(pwd)/backup:/backup ubuntu \
  tar czf /backup/filestore.tar.gz -C /data .
```

### Resource Limits

Edit `docker-compose.override.yml` to set resource limits:

```yaml
version: "2.4"
services:
  odoo:
    cpus: 2
    mem_limit: 4g

  db:
    cpus: 2
    mem_limit: 4g
    shm_size: 2g
```

## Common Operations

### Start/Stop Services

```shell
# Start
invoke start

# Stop
invoke stop

# Restart Odoo only
invoke restart
```

### Update OpenSPP

```shell
# Update code
invoke git-aggregate

# Update modules
invoke update --modules=all

# Or specific modules
invoke update --modules=spp_registry,spp_programs
```

### Install Modules

```shell
# Install specific modules
invoke install --modules=spp_dci,spp_api_v2

# Install all pending
invoke install --modules=all
```

### View Logs

```shell
# All services
invoke logs

# Odoo only
docker compose logs -f odoo

# Database
docker compose logs -f db

# Last 100 lines
docker compose logs --tail=100 odoo
```

### Database Operations

```shell
# Create snapshot
invoke snapshot

# List snapshots
ls -lh backups/

# Restore snapshot
invoke restore-snapshot --snapshot=backup_20250118.dump

# Direct database access
invoke psql
```

### Shell Access

```shell
# Odoo shell (Python REPL with Odoo environment)
docker compose run --rm odoo shell

# Container bash
docker compose exec odoo bash

# Database shell
docker compose exec db psql -U odoo -d prod
```

## Production Deployment

### Security Hardening

1. **Change default passwords:**

```shell
# Generate strong password
openssl rand -base64 32

# Update .env
POSTGRES_PASSWORD=<generated-password>
```

2. **Disable demo data:**

```shell
invoke resetdb --no-demo
```

3. **Configure SSL/TLS:**

Create `docker-compose.override.yml`:

```yaml
version: "2.4"
services:
  odoo:
    environment:
      # Force HTTPS
      PROXY_MODE: "true"
    labels:
      # Traefik labels for automatic SSL
      traefik.enable: "true"
      traefik.http.routers.odoo.rule: "Host(`openspp.yourdomain.com`)"
      traefik.http.routers.odoo.tls.certresolver: "letsencrypt"
```

4. **Restrict database access:**

```yaml
services:
  db:
    # Remove port exposure
    # ports:
    #   - "5432:5432"
```

### Reverse Proxy (Nginx)

```nginx
# /etc/nginx/sites-available/openspp
server {
    listen 80;
    server_name openspp.yourdomain.com;

    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name openspp.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/openspp.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/openspp.yourdomain.com/privkey.pem;

    # Modern SSL configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    # Proxy settings
    location / {
        proxy_pass http://localhost:17069;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Websocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        # Timeouts
        proxy_connect_timeout 600s;
        proxy_send_timeout 600s;
        proxy_read_timeout 600s;
    }

    # File upload size
    client_max_body_size 100M;
}
```

Enable and restart:

```shell
sudo ln -s /etc/nginx/sites-available/openspp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### Backups

Create backup script `/usr/local/bin/backup-openspp.sh`:

```shell
#!/bin/bash
set -e

BACKUP_DIR="/backup/openspp"
DATE=$(date +%Y%m%d_%H%M%S)
COMPOSE_DIR="/opt/openspp-docker"

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Backup database
cd "$COMPOSE_DIR"
docker compose exec -T db pg_dump -U odoo -d prod -Fc \
  > "$BACKUP_DIR/database_$DATE.dump"

# Backup filestore
docker run --rm \
  -v openspp-docker_filestore:/data \
  -v "$BACKUP_DIR":/backup \
  ubuntu tar czf "/backup/filestore_$DATE.tar.gz" -C /data .

# Keep only last 7 days
find "$BACKUP_DIR" -name "*.dump" -mtime +7 -delete
find "$BACKUP_DIR" -name "*.tar.gz" -mtime +7 -delete

echo "Backup completed: $DATE"
```

Schedule with cron:

```shell
# Make executable
sudo chmod +x /usr/local/bin/backup-openspp.sh

# Add to crontab
sudo crontab -e

# Daily at 2 AM
0 2 * * * /usr/local/bin/backup-openspp.sh >> /var/log/openspp-backup.log 2>&1
```

### Monitoring

```shell
# Resource usage
docker stats

# Container health
docker compose ps

# Disk usage
docker system df
du -sh /var/lib/docker/volumes/openspp-docker_*
```

## Updating OpenSPP

### Update to Latest Release

```shell
# 1. Backup first
invoke snapshot

# 2. Pull latest code
cd openspp-docker
git pull origin main

# 3. Update repositories
invoke git-aggregate

# 4. Pull new images
invoke img-pull

# 5. Restart with updates
invoke stop
invoke start

# 6. Update modules
invoke update --modules=all
```

### Update Specific Modules

```shell
# Update code
invoke git-aggregate

# Update only changed modules
invoke update --modules=spp_registry,spp_programs
```

## Are You Stuck?

### Container fails to start

**Check logs:**
```shell
docker compose logs odoo
docker compose logs db
```

**Common issues:**
- Port already in use: Change `ODOO_MAJOR` in `.env`
- Permission denied: Check file ownership in `./odoo/custom`
- Out of memory: Increase Docker memory limit

### Database connection errors

```shell
# Check database is running
docker compose ps db

# Check database logs
docker compose logs db

# Test connection
docker compose exec odoo psql -h db -U odoo -d prod
```

### Git aggregate fails with SSH errors

```shell
# Use HTTPS instead
invoke git-aggregate-host

# Or configure SSH keys
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
# Add to GitHub: Settings → SSH Keys
```

### Module installation fails

```shell
# Check Odoo logs
docker compose logs -f odoo

# Install with debug
docker compose run --rm odoo \
  --log-level=debug \
  -d prod \
  -i spp_module_name
```

### Out of disk space

```shell
# Clean old images
docker image prune -a

# Clean build cache
docker builder prune -a

# Remove unused volumes (careful!)
docker volume prune
```

### Slow performance

**Increase resources:**

Edit `docker-compose.override.yml`:

```yaml
services:
  odoo:
    mem_limit: 8g
  db:
    mem_limit: 8g
    shm_size: 4g
```

**Check database performance:**

```shell
# Database size
docker compose exec db psql -U odoo -d prod -c \
  "SELECT pg_size_pretty(pg_database_size('prod'));"

# Index health
docker compose exec db psql -U odoo -d prod -c \
  "SELECT schemaname, tablename, indexname FROM pg_indexes WHERE schemaname = 'public';"
```

### Cannot access after deployment

**Check firewall:**
```shell
sudo ufw status
sudo ufw allow 17069/tcp
```

**Check container is listening:**
```shell
docker compose ps
docker compose logs odoo | grep "HTTP service"
```

**Check reverse proxy:**
```shell
sudo nginx -t
sudo systemctl status nginx
```

## Advanced Topics

### Custom Modules Development

Mount local module directory:

```yaml
# docker-compose.override.yml
services:
  odoo:
    volumes:
      - ./custom-modules:/opt/odoo/custom/src/custom-modules:z
```

### Multi-Database Setup

```shell
# Enable database manager
# Edit docker-compose.override.yml
services:
  odoo:
    environment:
      LIST_DB: "true"
```

Access database manager at: http://localhost:17069/web/database/manager

### External PostgreSQL

To use external PostgreSQL instead of container:

```yaml
# docker-compose.override.yml
services:
  odoo:
    environment:
      PGHOST: external-db.example.com
      PGPORT: 5432
      PGDATABASE: openspp_prod
      PGUSER: odoo_user
      PGPASSWORD: <password>
```

Remove `db` service dependency.

## Next Steps

- {doc}`/get_started/first_program/index` - Create your first program
- {doc}`/ops_guide/security/access_control` - Configure security
- {doc}`/ops_guide/backup_recovery` - Set up backups
- {doc}`/ops_guide/monitoring` - Configure monitoring

## Support

- **Documentation:** https://docs.openspp.org
- **Docker Repo:** https://github.com/OpenSPP/openspp-docker
- **Issues:** https://github.com/OpenSPP/openspp-docker/issues
- **Community:** https://github.com/OpenSPP/openspp-docker/discussions

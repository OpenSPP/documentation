---
openspp:
  doc_status: draft
---

# Installation from Source

This guide is for **sys admins** and **developers** installing OpenSPP manually from source code. This method gives you full control over the installation but requires more technical expertise.

**Use this method if:**
- You're developing OpenSPP modules
- You need to modify core code
- You have specific Python environment requirements
- You want to understand OpenSPP internals

**Otherwise, use {doc}`docker` for faster setup.**

## Prerequisites

### System Requirements

| Component | Requirement |
|-----------|-------------|
| OS | Ubuntu 22.04, Debian 12, or macOS 12+ |
| Python | 3.10 or 3.11 |
| PostgreSQL | 15.x with PostGIS |
| RAM | 4+ GB |
| Disk | 20+ GB |

### Install System Dependencies

**Ubuntu/Debian:**

```shell
# Update package list
sudo apt-get update

# Install Python and build tools
sudo apt-get install -y \
    python3.11 \
    python3.11-dev \
    python3.11-venv \
    python3-pip \
    build-essential \
    libpq-dev \
    libsasl2-dev \
    libldap2-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    libopenjp2-7-dev \
    libtiff5-dev \
    zlib1g-dev \
    fonts-liberation \
    git \
    curl \
    wget \
    node-less \
    npm

# Install wkhtmltopdf (for PDF reports)
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo apt-get install -y ./wkhtmltox_0.12.6.1-2.jammy_amd64.deb
rm wkhtmltox_0.12.6.1-2.jammy_amd64.deb
```

**macOS:**

```shell
# Install Homebrew if needed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python@3.11 postgresql@15 node libxml2 libxslt libjpeg libpng freetype

# Install wkhtmltopdf
brew install --cask wkhtmltopdf
```

### Install PostgreSQL

**Ubuntu/Debian:**

```shell
# Install PostgreSQL 15
sudo apt-get install -y postgresql-15 postgresql-15-postgis-3

# Start PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create Odoo user and database
sudo -u postgres createuser -s $USER
createdb openspp_dev
```

**macOS:**

```shell
# Start PostgreSQL
brew services start postgresql@15

# Create database
createdb openspp_dev
```

### Verify PostgreSQL

```shell
# Test connection
psql -d openspp_dev -c "SELECT version();"

# Enable PostGIS extension
psql -d openspp_dev -c "CREATE EXTENSION IF NOT EXISTS postgis;"
```

## Installation Steps

### 1. Create Installation Directory

```shell
# Create directory structure
sudo mkdir -p /opt/openspp
sudo chown $USER:$USER /opt/openspp
cd /opt/openspp
```

### 2. Clone Odoo

OpenSPP is built on Odoo 17. Clone Odoo first:

```shell
# Clone Odoo 17
git clone https://github.com/odoo/odoo.git --depth 1 --branch 17.0 --single-branch
```

### 3. Clone OpenSPP Modules

```shell
# Create custom addons directory
mkdir -p custom/addons
cd custom/addons

# Clone OpenSPP modules
git clone https://github.com/OpenSPP/openspp-modules-v2.git
```

### 4. Create Python Virtual Environment

```shell
# Return to root directory
cd /opt/openspp

# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate     # On Windows
```

Your prompt should now show `(venv)`.

### 5. Install Python Dependencies

```shell
# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install Odoo dependencies
pip install -r odoo/requirements.txt

# Install OpenSPP dependencies
pip install -r custom/addons/openspp-modules-v2/requirements.txt
```

This takes 5-15 minutes.

### 6. Create Configuration File

Create `/opt/openspp/odoo.conf`:

```ini
[options]
# Server configuration
addons_path = /opt/openspp/odoo/addons,/opt/openspp/custom/addons/openspp-modules-v2
data_dir = /opt/openspp/data
admin_passwd = admin
http_port = 8069

# Database configuration
db_host = localhost
db_port = 5432
db_user = your_username
db_password = False
dbfilter = openspp_.*

# Performance
workers = 2
max_cron_threads = 1
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200

# Logging
logfile = /opt/openspp/logs/odoo.log
log_level = info

# Security (for development)
list_db = True
```

**Adjust these settings:**

| Setting | Description |
|---------|-------------|
| `db_user` | Your PostgreSQL username (usually `$USER`) |
| `workers` | Number of worker processes (2 per CPU core) |
| `http_port` | Web interface port (default 8069) |

### 7. Create Required Directories

```shell
# Create data and logs directories
mkdir -p /opt/openspp/data
mkdir -p /opt/openspp/logs

# Set permissions
chmod 755 /opt/openspp/data
chmod 755 /opt/openspp/logs
```

### 8. Initialize Database

```shell
# Activate virtual environment if not already
source /opt/openspp/venv/bin/activate

# Initialize database with OpenSPP modules
cd /opt/openspp
python odoo/odoo-bin \
  -c odoo.conf \
  -d openspp_dev \
  -i base,spp_base,spp_registry,spp_programs \
  --stop-after-init \
  --without-demo=all
```

This installs core OpenSPP modules. Takes 10-20 minutes.

**With demo data** (for evaluation):

```shell
python odoo/odoo-bin \
  -c odoo.conf \
  -d openspp_dev \
  -i base,spp_base,spp_registry,spp_programs,spp_demo \
  --stop-after-init
```

### 9. Start OpenSPP

```shell
# Start server
python odoo/odoo-bin -c odoo.conf
```

**Access OpenSPP:**
- URL: http://localhost:8069
- Database: openspp_dev
- Email: admin@example.com
- Password: admin

Press `Ctrl+C` to stop.

## Running as a Service

### Create Systemd Service (Ubuntu/Debian)

Create `/etc/systemd/system/openspp.service`:

```ini
[Unit]
Description=OpenSPP (Odoo 17)
After=network.target postgresql.service
Requires=postgresql.service

[Service]
Type=simple
User=openspp
Group=openspp
Environment="PATH=/opt/openspp/venv/bin"
ExecStart=/opt/openspp/venv/bin/python /opt/openspp/odoo/odoo-bin -c /opt/openspp/odoo.conf
StandardOutput=journal
StandardError=journal
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Create service user:**

```shell
# Create openspp user
sudo useradd -r -s /bin/false -d /opt/openspp openspp

# Transfer ownership
sudo chown -R openspp:openspp /opt/openspp
```

**Enable and start service:**

```shell
# Reload systemd
sudo systemctl daemon-reload

# Enable service
sudo systemctl enable openspp

# Start service
sudo systemctl start openspp

# Check status
sudo systemctl status openspp

# View logs
sudo journalctl -u openspp -f
```

### Create Launch Agent (macOS)

Create `~/Library/LaunchAgents/org.openspp.odoo.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>org.openspp.odoo</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/openspp/venv/bin/python</string>
        <string>/opt/openspp/odoo/odoo-bin</string>
        <string>-c</string>
        <string>/opt/openspp/odoo.conf</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/opt/openspp</string>
    <key>StandardOutPath</key>
    <string>/opt/openspp/logs/stdout.log</string>
    <key>StandardErrorPath</key>
    <string>/opt/openspp/logs/stderr.log</string>
    <key>KeepAlive</key>
    <true/>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

**Load and start:**

```shell
# Load agent
launchctl load ~/Library/LaunchAgents/org.openspp.odoo.plist

# Check status
launchctl list | grep openspp
```

## Configuration

### Production Settings

Edit `/opt/openspp/odoo.conf` for production:

```ini
[options]
# Disable database manager
list_db = False

# Set admin password
admin_passwd = <generate-strong-password>

# Increase workers
workers = 8

# Database filter (security)
dbfilter = ^openspp_prod$

# Disable demo data
without_demo = all

# Proxy mode (behind Nginx/Apache)
proxy_mode = True

# Log to file
logfile = /opt/openspp/logs/odoo.log
log_level = warn
```

### Performance Tuning

```ini
# Multi-processing
workers = <2 * num_cpus + 1>
max_cron_threads = 2

# Memory limits (bytes)
limit_memory_hard = 2684354560    # 2.5 GB
limit_memory_soft = 2147483648    # 2 GB

# Request limits
limit_request = 8192               # Max HTTP request size
limit_time_cpu = 600               # Max CPU time per request (seconds)
limit_time_real = 1200             # Max real time per request (seconds)

# Database connection pool
db_maxconn = 64
db_maxconn_gevent = False
```

### SSL/TLS Configuration

OpenSPP should run behind a reverse proxy (Nginx/Apache) for SSL.

**Nginx configuration** (`/etc/nginx/sites-available/openspp`):

```nginx
upstream openspp {
    server 127.0.0.1:8069;
}

upstream openspp-im {
    server 127.0.0.1:8072;
}

server {
    listen 80;
    server_name openspp.example.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name openspp.example.com;

    ssl_certificate /etc/letsencrypt/live/openspp.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/openspp.example.com/privkey.pem;

    access_log /var/log/nginx/openspp-access.log;
    error_log /var/log/nginx/openspp-error.log;

    proxy_read_timeout 720s;
    proxy_connect_timeout 720s;
    proxy_send_timeout 720s;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;

    location / {
        proxy_redirect off;
        proxy_pass http://openspp;
    }

    location /longpolling {
        proxy_pass http://openspp-im;
    }

    location ~* /web/static/ {
        proxy_cache_valid 200 90m;
        proxy_buffering on;
        expires 864000;
        proxy_pass http://openspp;
    }

    gzip on;
    gzip_types text/css text/scss text/plain text/xml application/xml application/json application/javascript;
    client_max_body_size 100M;
}
```

**Enable and restart:**

```shell
sudo ln -s /etc/nginx/sites-available/openspp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## Module Management

### Install Additional Modules

```shell
# Using command line
source /opt/openspp/venv/bin/activate
python /opt/openspp/odoo/odoo-bin \
  -c /opt/openspp/odoo.conf \
  -d openspp_dev \
  -i spp_dci,spp_api_v2 \
  --stop-after-init

# Restart service
sudo systemctl restart openspp
```

### Update Modules

```shell
# Update specific modules
python /opt/openspp/odoo/odoo-bin \
  -c /opt/openspp/odoo.conf \
  -d openspp_dev \
  -u spp_registry,spp_programs \
  --stop-after-init

# Update all modules
python /opt/openspp/odoo/odoo-bin \
  -c /opt/openspp/odoo.conf \
  -d openspp_dev \
  -u all \
  --stop-after-init
```

### List Installed Modules

```shell
# Connect to database
psql openspp_dev

# Query installed modules
SELECT name, state, latest_version
FROM ir_module_module
WHERE state = 'installed'
ORDER BY name;

# Exit
\q
```

## Backup and Recovery

### Database Backup

```shell
# Full backup
pg_dump -Fc openspp_dev > /backup/openspp_$(date +%Y%m%d).dump

# Plain SQL backup
pg_dump openspp_dev > /backup/openspp_$(date +%Y%m%d).sql
```

### Filestore Backup

```shell
# Backup filestore
tar czf /backup/filestore_$(date +%Y%m%d).tar.gz /opt/openspp/data/filestore/openspp_dev
```

### Restore

```shell
# Stop OpenSPP
sudo systemctl stop openspp

# Drop and recreate database
dropdb openspp_dev
createdb openspp_dev

# Restore database
pg_restore -d openspp_dev /backup/openspp_20250118.dump

# Restore filestore
tar xzf /backup/filestore_20250118.tar.gz -C /opt/openspp/data/

# Start OpenSPP
sudo systemctl start openspp
```

### Automated Backups

Create `/usr/local/bin/backup-openspp.sh`:

```shell
#!/bin/bash
set -e

BACKUP_DIR="/backup/openspp"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="openspp_dev"

mkdir -p "$BACKUP_DIR"

# Backup database
pg_dump -Fc "$DB_NAME" > "$BACKUP_DIR/db_$DATE.dump"

# Backup filestore
tar czf "$BACKUP_DIR/filestore_$DATE.tar.gz" \
  /opt/openspp/data/filestore/"$DB_NAME"

# Keep only last 7 days
find "$BACKUP_DIR" -name "*.dump" -mtime +7 -delete
find "$BACKUP_DIR" -name "*.tar.gz" -mtime +7 -delete

echo "Backup completed: $DATE"
```

**Schedule with cron:**

```shell
sudo chmod +x /usr/local/bin/backup-openspp.sh
sudo crontab -e

# Daily at 2 AM
0 2 * * * /usr/local/bin/backup-openspp.sh >> /var/log/openspp-backup.log 2>&1
```

## Development Setup

For development, use these additional settings:

```ini
[options]
# Development mode
dev_mode = reload,qweb,werkzeug,xml

# Enable developer features
log_level = debug
log_db = True
log_db_level = warning

# Auto-reload on code changes
dev_mode = reload

# Test mode
test_enable = True
```

**Run with auto-reload:**

```shell
source /opt/openspp/venv/bin/activate
python odoo/odoo-bin -c odoo.conf --dev=all
```

## Are You Stuck?

### Python dependencies fail to install

**Error: "pg_config executable not found"**
```shell
# Ubuntu/Debian
sudo apt-get install libpq-dev

# macOS
brew install postgresql@15
```

**Error: "xml2-config not found"**
```shell
# Ubuntu/Debian
sudo apt-get install libxml2-dev libxslt1-dev

# macOS
brew install libxml2 libxslt
```

### PostgreSQL connection fails

**Check PostgreSQL is running:**
```shell
# Ubuntu/Debian
sudo systemctl status postgresql

# macOS
brew services list
```

**Check connection:**
```shell
psql -d openspp_dev -c "SELECT 1;"
```

**Reset password:**
```shell
sudo -u postgres psql
ALTER USER your_username WITH PASSWORD 'newpassword';
\q
```

### Module installation fails

**Check addons path:**
```shell
# Verify modules exist
ls -la /opt/openspp/custom/addons/openspp-modules-v2/

# Check odoo.conf addons_path
grep addons_path /opt/openspp/odoo.conf
```

**Install with debug:**
```shell
python odoo/odoo-bin \
  -c odoo.conf \
  -d openspp_dev \
  -i spp_module_name \
  --log-level=debug \
  --stop-after-init
```

### Permission denied errors

```shell
# Fix ownership
sudo chown -R openspp:openspp /opt/openspp

# Fix permissions
chmod -R 755 /opt/openspp
chmod -R 644 /opt/openspp/odoo.conf
```

### Out of memory

**Increase memory limits in odoo.conf:**
```ini
limit_memory_hard = 4294967296    # 4 GB
limit_memory_soft = 3221225472    # 3 GB
```

**Check system memory:**
```shell
free -h
```

### Service won't start

**Check logs:**
```shell
# Systemd
sudo journalctl -u openspp -n 50

# Log file
tail -f /opt/openspp/logs/odoo.log
```

**Test manually:**
```shell
sudo systemctl stop openspp
source /opt/openspp/venv/bin/activate
python /opt/openspp/odoo/odoo-bin -c /opt/openspp/odoo.conf
```

## Updating OpenSPP

### Update OpenSPP Modules

```shell
# Stop service
sudo systemctl stop openspp

# Update code
cd /opt/openspp/custom/addons/openspp-modules-v2
git pull origin main

# Update Python dependencies
source /opt/openspp/venv/bin/activate
pip install --upgrade -r requirements.txt

# Update modules
python /opt/openspp/odoo/odoo-bin \
  -c /opt/openspp/odoo.conf \
  -d openspp_dev \
  -u all \
  --stop-after-init

# Start service
sudo systemctl start openspp
```

### Update Odoo

**Caution:** Odoo updates can break compatibility. Always test in staging first.

```shell
# Backup first!
pg_dump -Fc openspp_dev > /backup/before_upgrade.dump

# Update Odoo
cd /opt/openspp/odoo
git fetch origin
git checkout 17.0
git pull origin 17.0

# Update Python dependencies
source /opt/openspp/venv/bin/activate
pip install --upgrade -r requirements.txt

# Update database
python odoo-bin -c /opt/openspp/odoo.conf -d openspp_dev -u all --stop-after-init
```

## Next Steps

- {doc}`/get_started/first_program/index` - Create your first program
- {doc}`/developer_guide/extending/index` - Develop custom modules
- {doc}`/ops_guide/security/access_control` - Configure security
- {doc}`/ops_guide/backup_recovery` - Set up backups

## Support

- **Documentation:** https://docs.openspp.org
- **GitHub:** https://github.com/OpenSPP/openspp-modules-v2
- **Issues:** https://github.com/OpenSPP/openspp-modules-v2/issues
- **Community:** https://github.com/OpenSPP/openspp-docker/discussions

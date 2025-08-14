---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Installing OpenSPP on Ubuntu/Debian

This guide walks you through installing OpenSPP on Ubuntu 24.04 or Debian 12 (Bookworm) using the official APT repository hosted on Nexus.

## Prerequisites

Before installing OpenSPP, ensure you have:

- Ubuntu 24.04 LTS (Noble Numbat) or Debian 12 (Bookworm)
- Minimum 4GB RAM (8GB recommended for production)
- Minimum 10GB disk space
- Root or sudo access
- Internet connection for downloading packages
- Access to https://builds.acn.fr (OpenSPP APT repository)

## Step 1: Update System

First, ensure your system is up to date:

```bash
sudo apt-get update
sudo apt-get upgrade -y
```

## Step 2: Install PostgreSQL

OpenSPP requires PostgreSQL as its database backend.

# Install PostgreSQL
```bash
sudo apt-get install -y postgresql postgresql-client
```

# Verify PostgreSQL is running
```bash
sudo systemctl status postgresql
```

## Step 3: Configure OpenSPP Repository

Add the OpenSPP APT repository to your system:

```bash
# Add the OpenSPP public key
wget -qO - https://builds.acn.fr/repository/apt-keys/openspp/public.key | sudo apt-key add -

# Add the OpenSPP repository
echo "deb https://builds.acn.fr/repository/apt-openspp-daily bookworm main" | \
  sudo tee /etc/apt/sources.list.d/openspp.list

# Update package list
sudo apt-get update
```

## Step 4: Install OpenSPP

Install OpenSPP directly from the repository:

```bash
# Install OpenSPP package
sudo apt-get install -y openspp-17-daily
```

### Alternative: Manual Download

If you prefer to download the package manually or the repository is not accessible:

```bash
# Create a temporary directory
mkdir -p ~/openspp-install
cd ~/openspp-install

# Download directly from Nexus repository
wget https://builds.acn.fr/repository/apt-openspp/pool/main/o/openspp/openspp_17.0.1+odoo17.0-1_amd64.deb

# Install the package
sudo dpkg -i openspp_17.0.1+odoo17.0-1_amd64.deb

# Fix any dependency issues if they occur
sudo apt-get install -f
```

The installation will:
- Create an `openspp` system user
- Install files to `/opt/openspp/`
- Create data directory at `/var/lib/openspp/`
- Create log directory at `/var/log/openspp/`
- Install systemd service
- Install command-line tools in `/usr/bin/`

## Step 5: Configure PostgreSQL

Create a PostgreSQL user for OpenSPP:

```bash
# Create the openspp PostgreSQL user
sudo -u postgres createuser -s openspp

# Optional: If you want to use password authentication instead of peer authentication
# sudo -u postgres psql -c "ALTER USER openspp WITH PASSWORD 'your_secure_password';"
```

## Step 6: Configure OpenSPP

### Basic Configuration

The main configuration file is located at `/etc/openspp/odoo.conf`. 

1. **Set the admin password** (IMPORTANT for security):

```bash
# Generate a strong password
openssl rand -base64 32

# Edit the configuration
sudo nano /etc/openspp/odoo.conf
```

Find and update these lines:
```ini
; Security
admin_passwd = YOUR_STRONG_PASSWORD_HERE
```

2. **Database Management Settings**:

```ini
; Database Management
list_db = True          ; IMPORTANT: Set to True to enable database creation via web UI
                        ; Set to False for production (more secure)
```

3. **Queue Job Configuration** (REQUIRED for OpenSPP):

OpenSPP uses the queue_job module for asynchronous operations. The package includes default configuration, but you may need to adjust it:

```ini
; Server-wide modules (queue_job is required)
server_wide_modules = base,web,queue_job

; Performance - workers MUST be > 0 for queue_job to function
workers = 4              ; Set to number of CPU cores - 1 (minimum 2 for queue_job)

[queue_job]
channels = root:2        ; Number of worker channels
; Database connection for job runner (should match main database settings)
jobrunner_db_host =      ; Empty for Unix socket
jobrunner_db_port = 5432
jobrunner_db_user = openspp
jobrunner_db_password = False
```

**Important**: Queue jobs will NOT run if `workers = 0`. Always set workers to at least 2 for production.

4. **Other optional configurations** you may want to adjust:

```ini
; Memory limits
limit_memory_hard = 4294967296  ; 4GB in bytes
limit_memory_soft = 3221225472  ; 3GB in bytes

; Network
xmlrpc_port = 8069      ; Change if you need a different port
longpolling_port = 8072 ; For real-time features

; Logging
log_level = info        ; Options: debug, info, warning, error, critical
```

### Database Configuration

By default, the package is configured to use Unix socket authentication (peer). This means the `openspp` system user can connect to PostgreSQL without a password.

If you need to use password authentication:

```bash
sudo nano /etc/openspp/odoo.conf
```

Update:
```ini
db_host = localhost
db_password = your_postgresql_password
```

## Step 7: Start OpenSPP Service

```bash
# Enable the service to start on boot
sudo systemctl enable openspp

# Start the service
sudo systemctl start openspp

# Check service status
sudo systemctl status openspp
```

You should see output indicating the service is active and running.

## Step 8: Create Your First Database

### Option A: Via Web Interface (Recommended)

**Prerequisites**: Ensure `list_db = True` is set in `/etc/openspp/odoo.conf` (see Step 6).

1. Open a web browser and navigate to:
   ```
   http://your-server-ip:8069
   ```

2. You'll see the database creation page. Fill in:
   - **Master Password**: The admin password you set in odoo.conf
   - **Database Name**: Choose a name (e.g., `openspp_prod`)
   - **Email**: Your admin email address
   - **Password**: Password for the admin user in this database
   - **Language**: Select your preferred language
   - **Country**: Select your country
   - **Demo Data**: Uncheck for production (check only for testing)

3. Click "Create Database" and wait (this may take 2-3 minutes)

### Option B: Via Command Line

```bash
# Create a database
sudo -u openspp openspp-server \
    --database=openspp_prod \
    --init=base \
    --stop-after-init

# Restart the service
sudo systemctl restart openspp
```

## Step 9: Access OpenSPP

Once the database is created:

1. Access the login page at: `http://your-server-ip:8069`
2. Login with:
   - **Email**: The email you provided during database creation
   - **Password**: The password you set for the admin user

## Step 10: Install OpenSPP Modules

After logging in, you'll need to activate the OpenSPP modules:

1. Navigate to **Apps** menu
2. Remove the "Apps" filter to see all available modules
3. **First, install the queue_job module** (required for OpenSPP):
   - Search for `queue_job`
   - Click Install
   - This enables asynchronous job processing
4. **IMPORTANT: Restart OpenSPP after installing queue_job**:
   ```bash
   sudo systemctl restart openspp
   ```
   This is required for the job runner to start listening for async jobs.
5. Then install these core OpenSPP modules:
   - `spp_base` - OpenSPP Base
   - `g2p_registry_base` - G2P Registry Base
   - `g2p_programs` - G2P Programs
   - Other modules as needed for your use case

**Note**: The `queue_job` module is automatically loaded as a server-wide module but must be installed in the database AND the service restarted for OpenSPP async operations to function properly.

## Security Recommendations

### 1. Database Security Configuration

After initial setup and database creation, it's strongly recommended to:

```bash
# Edit the configuration
sudo nano /etc/openspp/odoo.conf

# Set list_db to False for production
list_db = False

# Restart the service
sudo systemctl restart openspp
```

**Why disable list_db in production:**
- Prevents unauthorized users from seeing database names
- Disables database creation/deletion via web interface
- Reduces attack surface by hiding database management interface
- Forces direct database URL access (e.g., `http://server:8069/web?db=openspp_prod`)

**When to keep list_db = True:**
- Development environments
- Testing environments
- Initial setup phase
- When multiple databases need frequent management

### 2. Firewall Configuration

```bash
# Install UFW firewall
sudo apt-get install -y ufw

# Allow SSH (adjust port if needed)
sudo ufw allow 22/tcp

# Allow OpenSPP web interface
sudo ufw allow 8069/tcp

# Allow OpenSPP longpolling (if using real-time features)
sudo ufw allow 8072/tcp

# Enable firewall
sudo ufw enable
```

### 3. SSL/TLS with Nginx (Recommended for Production)

```bash
# Install Nginx
sudo apt-get install -y nginx certbot python3-certbot-nginx

# Create Nginx configuration
sudo nano /etc/nginx/sites-available/openspp
```

Add this configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;

    # SSL certificates (will be added by certbot)
    # ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    # ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    # Proxy settings
    proxy_read_timeout 720s;
    proxy_connect_timeout 720s;
    proxy_send_timeout 720s;

    # Add headers
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;

    # Redirect requests to OpenSPP
    location / {
        proxy_redirect off;
        proxy_pass http://127.0.0.1:8069;
    }

    # Longpolling
    location /longpolling {
        proxy_pass http://127.0.0.1:8072;
    }

    # Static files
    location ~* /web/static/ {
        proxy_cache_valid 200 90m;
        proxy_buffering on;
        expires 864000;
        proxy_pass http://127.0.0.1:8069;
    }
}
```

Enable the site and get SSL certificate:
```bash
# Enable the site
sudo ln -s /etc/nginx/sites-available/openspp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

# Get SSL certificate
sudo certbot --nginx -d your-domain.com
```

### 4. Regular Backups

Create a backup script:

```bash
sudo nano /usr/local/bin/openspp-backup.sh
```

```bash
#!/bin/bash
BACKUP_DIR="/var/backups/openspp"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="openspp_prod"

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup database
sudo -u postgres pg_dump $DB_NAME | gzip > $BACKUP_DIR/db_${DB_NAME}_${DATE}.sql.gz

# Backup filestore
tar -czf $BACKUP_DIR/filestore_${DATE}.tar.gz /var/lib/openspp/

# Keep only last 30 days of backups
find $BACKUP_DIR -type f -mtime +30 -delete

echo "Backup completed: $DATE"
```

Make it executable and schedule:
```bash
sudo chmod +x /usr/local/bin/openspp-backup.sh

# Add to crontab (daily at 2 AM)
echo "0 2 * * * /usr/local/bin/openspp-backup.sh" | sudo crontab -
```

## Monitoring and Maintenance

### View Logs

```bash
# Real-time service logs
sudo journalctl -u openspp -f

# Application logs
sudo tail -f /var/log/openspp/openspp.log

# PostgreSQL logs
sudo tail -f /var/log/postgresql/postgresql-*.log
```

### Service Management

```bash
# Restart service
sudo systemctl restart openspp

# Stop service
sudo systemctl stop openspp

# Start service
sudo systemctl start openspp

# Reload configuration without restart
sudo systemctl reload openspp
```

### Update OpenSPP

When a new version is available:

```bash
# Update package list
sudo apt-get update

# Check for OpenSPP updates
apt list --upgradable | grep openspp

# Stop service before upgrade
sudo systemctl stop openspp

# Backup current installation
sudo tar -czf /var/backups/openspp-backup-$(date +%Y%m%d).tar.gz /opt/openspp /etc/openspp

# Upgrade OpenSPP
sudo apt-get upgrade openspp

# Start service
sudo systemctl start openspp

# Update modules via web interface
```

### Alternative: Manual Update

If updating manually:

```bash
# Download new package from Nexus
wget https://builds.acn.fr/repository/apt-openspp/pool/main/o/openspp/openspp_X.X.X_amd64.deb

# Stop service
sudo systemctl stop openspp

# Backup current installation
sudo tar -czf /var/backups/openspp-backup-$(date +%Y%m%d).tar.gz /opt/openspp /etc/openspp

# Install new version
sudo dpkg -i openspp_X.X.X_amd64.deb

# Start service
sudo systemctl start openspp
```

## Troubleshooting

### Service Won't Start

Check logs for errors:
```bash
sudo journalctl -u openspp -n 50 --no-pager
```

Common issues:
- **PostgreSQL connection failed**: Check db_host and authentication settings
- **Port already in use**: Another service using port 8069
- **Permission denied**: Check file ownership in `/var/lib/openspp/`

### Cannot Access Web Interface

1. Check if service is running:
   ```bash
   sudo systemctl status openspp
   sudo ss -tlnp | grep 8069
   ```

2. Check firewall:
   ```bash
   sudo ufw status
   ```

3. Test locally:
   ```bash
   curl -I http://localhost:8069
   ```

### Database Connection Issues

1. Verify PostgreSQL is running:
   ```bash
   sudo systemctl status postgresql
   ```

2. Test connection:
   ```bash
   sudo -u openspp psql -d postgres -c "SELECT 1;"
   ```

3. Check PostgreSQL authentication:
   ```bash
   sudo cat /etc/postgresql/16/main/pg_hba.conf | grep -E '^(local|host)'
   ```

### Queue Jobs Not Running

If background jobs are not being processed:

1. Check workers configuration:
   ```bash
   grep workers /etc/openspp/odoo.conf
   # Should be > 0 (at least 2 for production)
   ```

2. Verify queue_job module is loaded:
   ```bash
   grep server_wide_modules /etc/openspp/odoo.conf
   # Should include: base,web,queue_job
   ```

3. Check queue_job database settings:
   ```bash
   grep -A 5 "\[queue_job\]" /etc/openspp/odoo.conf
   ```

4. Restart the service:
   ```bash
   sudo systemctl restart openspp
   ```

5. Monitor jobs in Odoo:
   - Navigate to Settings > Technical > Queue Job > Jobs
   - Check for failed or pending jobs

### Reset Admin Password

If you forget the admin password for the database:

```bash
# Connect to the database
sudo -u openspp openspp-shell --database=openspp_prod

# In the Python shell
>>> self.env['res.users'].browse(2).write({'password': 'new_password'})
>>> self.env.cr.commit()
>>> exit()
```

## Performance Tuning

For production environments with high load:

1. **Increase workers** (1 worker per CPU core, minimum 2 for queue_job):
   ```ini
   workers = 8  # For 8-core server
   server_wide_modules = base,web,queue_job  # Required
   ```
   
   **Note**: Never set `workers = 0` in production as this disables queue_job async processing.

2. **Adjust memory limits** based on available RAM:
   ```ini
   limit_memory_hard = 8589934592  # 8GB
   limit_memory_soft = 6442450944  # 6GB
   ```

3. **PostgreSQL tuning**:
   ```bash
   sudo nano /etc/postgresql/16/main/postgresql.conf
   ```
   
   Adjust:
   ```ini
   shared_buffers = 2GB
   effective_cache_size = 6GB
   maintenance_work_mem = 512MB
   checkpoint_completion_target = 0.9
   wal_buffers = 16MB
   default_statistics_target = 100
   random_page_cost = 1.1
   ```

4. **Enable caching** with Redis (optional):
   ```bash
   sudo apt-get install -y redis-server
   # Configure in odoo.conf if your OpenSPP version supports it
   ```

## Getting Help

- **Documentation**: https://docs.openspp.org
- **Community Forum**: https://community.openspp.org
- **Issue Tracker**: https://github.com/openspp/openspp-modules/issues
- **Email Support**: support@openspp.org
- **APT Repository**: https://builds.acn.fr/repository/apt-openspp/

## Next steps

After installation, see:

- {doc}`../user_guide/index` for using OpenSPP features
- {doc}`../developer_guide/index` for customization and development
- {doc}`poc_and_pilot` for setting up pilot programs

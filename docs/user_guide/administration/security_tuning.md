---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Security and Performance Tuning

This guide provides essential recommendations for securing your OpenSPP instance and tuning its performance for production environments. It covers database security, firewall setup, SSL/TLS configuration with Nginx, and implementing regular backups. Additionally, it offers tips on performance tuning, including adjusting worker processes, memory limits, and PostgreSQL settings to handle high-load scenarios.

## Security Recommendations

### 1. Database Security Configuration

After initial setup and database creation, it's strongly recommended to:

```bash
sudo nano /etc/openspp/odoo.conf
```

Set list_db to False for production
```ini
list_db = False
```

Restart the service
```bash
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
sudo apt-get install -y ufw
sudo ufw allow 22/tcp
sudo ufw allow 8069/tcp
sudo ufw allow 8072/tcp
sudo ufw enable
```

### 3. SSL/TLS with Nginx (Recommended for Production)

```bash
sudo apt-get install -y nginx certbot python3-certbot-nginx
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
sudo ln -s /etc/nginx/sites-available/openspp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
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
echo "0 2 * * * /usr/local/bin/openspp-backup.sh" | sudo crontab -
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
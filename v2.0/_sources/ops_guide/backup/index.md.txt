---
openspp:
  doc_status: draft
  products: [core]
---

# Backup & Recovery

**For:** System administrators managing backups and disaster recovery

This guide covers backup configuration for OpenSPP deployments using the production Docker Compose stack.

## Automated Backups

The production compose file includes an automated backup service using the official `postgis/postgis` image. This ensures full compatibility with PostGIS spatial data. Backups run daily and are stored in a Docker volume.

```{note}
The included `backup.sh` script is a reference implementation. Adapt it to your organization's backup policies, retention requirements, and infrastructure (e.g., off-site storage, encryption at rest, monitoring integration).
```

### Configuration

Set backup options in `.env.production`:

```bash
# Backup schedule (cron format, default: daily at 2am)
BACKUP_SCHEDULE=0 2 * * *

# Retention policy
BACKUP_KEEP_DAYS=7
BACKUP_KEEP_WEEKS=4
BACKUP_KEEP_MONTHS=6

# PostgreSQL connection (uses same credentials as Odoo)
DB_HOST=db
DB_PORT=5432
DB_NAME=openspp
DB_USER=odoo
DB_PASSWORD=your-secure-password

# Optional admin role for destructive restore operations (Option A, strict)
# This role should have CREATEDB (or SUPERUSER if required for PostGIS)
DB_ADMIN_USER=admin
```

### Retention Policy

The default retention policy keeps:

| Type | Retention | When Saved |
|------|-----------|------------|
| Daily | 7 days | Every backup |
| Weekly | 4 weeks | Sundays |
| Monthly | 6 months | 1st of month |

Backups are stored in `/backups/daily/`, `/backups/weekly/`, and `/backups/monthly/` directories.

### Backup Format

Backups use PostgreSQL custom format (`pg_dump -Fc`) with compression level 6. This format:
- Fully supports PostGIS geometry types and spatial indexes
- Enables selective restore (individual tables)
- Supports parallel restore for faster recovery
- Compresses automatically

## Manual Backup

To create a manual backup outside the scheduled time:

```bash
# Trigger immediate backup
docker compose exec backup /backup.sh

# Or use pg_dump directly
docker compose exec db pg_dump -U odoo -Fc openspp > backup_$(date +%Y%m%d_%H%M%S).dump
```

## Backup Verification

Regularly verify backups are working:

```bash
# Check backup service logs
docker compose logs backup --tail=50

# List available backups
docker compose exec backup ls -la /backups/

# Check backup file sizes (should not be empty)
docker compose exec backup du -h /backups/*
```

### Test Restore

Periodically test restoration to a separate database:

```bash
# Create a test database
# Option A (strict): use admin role with CREATEDB / SUPERUSER
docker compose exec db createdb -U ${DB_ADMIN_USER:-admin} openspp_test
# Option B (flexible): use Odoo role (CREATEDB)
# docker compose exec db createdb -U odoo openspp_test

# Ensure PostGIS extension exists (strict mode)
docker compose exec db psql -U ${DB_ADMIN_USER:-admin} openspp_test -c "CREATE EXTENSION IF NOT EXISTS postgis;"

# Restore latest backup (using pg_restore for custom format)
# Option A (strict): restore as Odoo role without changing ownership
docker compose exec backup pg_restore -h db -U odoo --no-owner -d openspp_test \
  /backups/daily/openspp_latest.dump

# Verify data
docker compose exec db psql -U odoo openspp_test -c "SELECT COUNT(*) FROM res_partner;"

# Verify PostGIS extension
docker compose exec db psql -U odoo openspp_test -c "SELECT PostGIS_Version();"

# Clean up test database
docker compose exec db dropdb -U ${DB_ADMIN_USER:-admin} openspp_test
# Option B (flexible): use Odoo role (CREATEDB)
# docker compose exec db dropdb -U odoo openspp_test
```

## Recovery Procedures

### Full Database Restore

To restore to the primary database (destructive), follow the workflow for your chosen database policy:

**Option A (strict hardening, recommended):**
- Use an admin role to drop/create the database and (if needed) create the PostGIS extension.
- Restore data as the Odoo role or as admin with `--no-owner`.

**Option B (operational flexibility):**
- Use the Odoo role for create/drop/restore (requires `CREATEDB`).

```bash
# Stop Odoo to prevent writes
docker compose stop odoo queue-worker

# Drop and recreate database
# Option A (strict): use admin role with CREATEDB / SUPERUSER
docker compose exec db dropdb -U ${DB_ADMIN_USER:-admin} openspp
docker compose exec db createdb -U ${DB_ADMIN_USER:-admin} openspp
# Option B (flexible): use Odoo role (CREATEDB)
# docker compose exec db dropdb -U odoo openspp
# docker compose exec db createdb -U odoo openspp

# Ensure PostGIS extension exists (strict mode)
docker compose exec db psql -U ${DB_ADMIN_USER:-admin} openspp -c "CREATE EXTENSION IF NOT EXISTS postgis;"

# Restore from backup (using pg_restore for custom format)
# Option A (strict): restore as Odoo role without changing ownership
docker compose exec backup pg_restore -h db -U odoo --no-owner -d openspp \
  /backups/daily/openspp_latest.dump

# Option B (flexible): restore as Odoo role (CREATEDB)
# docker compose exec backup pg_restore -h db -U odoo -d openspp \
#   /backups/daily/openspp_latest.dump

# Restart services
docker compose start odoo queue-worker
```

### Point-in-Time Recovery

For more granular recovery, you need PostgreSQL WAL archiving enabled. This is not configured by default in the Docker stack but can be added for critical deployments.

### Filestore Recovery

The Odoo filestore (attachments, documents) is stored in the `odoo_data` volume. Back this up separately:

```bash
# Backup filestore
docker run --rm -v openspp_odoo_data:/data -v $(pwd):/backup alpine \
  tar czf /backup/filestore_$(date +%Y%m%d).tar.gz -C /data .

# Restore filestore
docker run --rm -v openspp_odoo_data:/data -v $(pwd):/backup alpine \
  tar xzf /backup/filestore_20240115.tar.gz -C /data
```

## Off-Site Backup

For production deployments, copy backups to off-site storage:

### Using rclone (S3, GCS, Azure, etc.)

```bash
# Install rclone on host
curl https://rclone.org/install.sh | sudo bash

# Configure remote (interactive)
rclone config

# Sync backups to remote storage
rclone sync /var/lib/docker/volumes/openspp_backup_data/_data remote:openspp-backups/
```

### Using rsync (remote server)

```bash
# Sync to remote backup server
rsync -avz /var/lib/docker/volumes/openspp_backup_data/_data/ \
  backup@remote-server:/backups/openspp/
```

Add to crontab for automatic off-site sync:

```bash
# Run after daily backup (3am)
0 3 * * * rsync -avz /var/lib/docker/volumes/openspp_backup_data/_data/ backup@remote:/backups/openspp/
```

## Disaster Recovery Planning

### Recovery Time Objective (RTO)

| Scenario | Estimated RTO |
|----------|--------------|
| Database corruption | 30 minutes |
| Full server failure | 2-4 hours |
| Data center outage | 4-8 hours (with off-site backups) |

### Recovery Point Objective (RPO)

With daily backups, maximum data loss is 24 hours. To reduce RPO:

| Backup Frequency | RPO | Compose Change |
|------------------|-----|----------------|
| Daily (default) | 24 hours | `BACKUP_SCHEDULE=0 2 * * *` |
| Every 6 hours | 6 hours | `BACKUP_SCHEDULE=0 */6 * * *` |
| Hourly | 1 hour | `BACKUP_SCHEDULE=0 * * * *` |

### Checklist

Before going to production:

- [ ] Verify automated backups are running
- [ ] Test restore procedure on a separate database
- [ ] Configure off-site backup sync
- [ ] Document recovery procedures for your team
- [ ] Schedule quarterly restore tests
- [ ] Set up backup monitoring/alerting

## Troubleshooting

### Backup Not Running

```bash
# Check backup container status
docker compose ps backup

# Check logs for errors
docker compose logs backup

# Verify cron is running inside container
docker compose exec backup crontab -l
```

### Backup Files Empty or Missing

```bash
# Check disk space
docker compose exec backup df -h /backups

# Check PostgreSQL connectivity
docker compose exec backup pg_isready -h db -U odoo
```

### Restore Fails

```bash
# Check for active connections blocking restore
docker compose exec db psql -U odoo -c "SELECT * FROM pg_stat_activity WHERE datname = 'openspp';"

# Force disconnect all users
docker compose exec db psql -U odoo -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'openspp' AND pid <> pg_backend_pid();"
```

## Related Documentation

- Production deployment: {doc}`../deployment/production-hardening`
- Security configuration: {doc}`../security/index`


# Database Management

This section explains how to manage your OpenSPP database, including how to reset the database, and how to back up your data before making major changes. Proper database management helps ensure data integrity and system reliability.

## Reset Database

If you need to reset your OpenSPP database (e.g., for testing or to start fresh):

### Option A: Via Web Interface (if list_db = True)

1. Navigate to `http://your-server-ip:8069/web/database/manager`
3. Click the "Delete" from the right side of the Database you wanted to Delete.
4. Enter the Master Password then Click the "Delete".
5. Create a new database with the same name or different name

### Option B: Via Command Line

```bash
# Stop OpenSPP service
sudo systemctl stop openspp

# Drop the existing database
sudo -u postgres dropdb openspp_prod

# Create a new empty database
sudo -u postgres createdb openspp_prod

# Start OpenSPP service
sudo systemctl start openspp

# Initialize the database with base modules
sudo -u openspp openspp-server \
    --database=openspp_prod \
    --init=base \
    --stop-after-init

# Restart service
sudo systemctl restart openspp
```

**Warning**: Resetting the database will permanently delete all data, including:
- All registrant records
- Program configurations
- Entitlements and payments
- Uploaded documents
- User accounts and settings
- Custom configurations

## Backup Before Reset

Always create a backup before resetting:

```bash
# Create backup directory
sudo mkdir -p /var/backups/openspp

# Backup database
sudo -u postgres pg_dump openspp_prod | gzip > /var/backups/openspp/db_backup_$(date +%Y%m%d_%H%M%S).sql.gz

# Backup filestore
sudo tar -czf /var/backups/openspp/filestore_backup_$(date +%Y%m%d_%H%M%S).tar.gz /var/lib/openspp/filestore/openspp_prod
```
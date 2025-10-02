
# Database management

This section explains how to manage your OpenSPP database, including how to reset the database, and how to back up your data before making major changes. Proper database management helps ensure data integrity and system reliability.

## Reset database

If you need to reset your OpenSPP database (e.g., for testing or to start fresh):

### Option A: Via web interface (if list_db = True)

1. Navigate to `http://your-server-ip:8069/web/database/manager`
3. Click the "Delete" from the right side of the Database you wanted to Delete.
4. Enter the Master Password then Click the "Delete".
5. Create a new database with the same name or different name

### Option B: Via command line

In your terminal, run the following commands:

```bash
sudo systemctl stop openspp
sudo -u postgres dropdb openspp_prod
sudo -u postgres createdb openspp_prod
sudo systemctl start openspp
sudo -u openspp openspp-server \
    --database=openspp_prod \
    --init=base \
    --stop-after-init
sudo systemctl restart openspp
```
This drops the openspp_prod database, creates a new one, initializes it, and starts the OpenSPP service.

**Warning**: Resetting the database will permanently delete all data, including:
- All registrant records
- Program configurations
- Entitlements and payments
- Uploaded documents
- User accounts and settings
- Custom configurations

## Backup before reset

The following commands create a backup of both the database and the filestore:

```bash
sudo mkdir -p /var/backups/openspp
sudo -u postgres pg_dump openspp_prod | gzip > /var/backups/openspp/db_backup_$(date +%Y%m%d_%H%M%S).sql.gz
sudo tar -czf /var/backups/openspp/filestore_backup_$(date +%Y%m%d_%H%M%S).tar.gz /var/lib/openspp/filestore/openspp_prod
```
---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Troubleshooting

This guide provides solutions to common problems encountered while running OpenSPP. It covers issues such as the service failing to start, inability to access the web interface, database connection problems, and background jobs not running. It also includes a procedure for resetting the admin password if it's forgotten.

## Service Won't Start

Check logs for errors:
```bash
sudo journalctl -u openspp -n 50 --no-pager
```

Common issues:
- **PostgreSQL connection failed**: Check db_host and authentication settings
- **Port already in use**: Another service using port 8069
- **Permission denied**: Check file ownership in `/var/lib/openspp/`

## Cannot Access Web Interface

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

## Database Connection Issues

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

## Queue Jobs Not Running

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

## Reset Admin Password

If you forget the admin password for the database:

```bash
# Connect to the database
sudo -u openspp openspp-shell --database=openspp_prod

# In the Python shell
>>> self.env['res.users'].browse(2).write({'password': 'new_password'})
>>> self.env.cr.commit()
>>> exit()
```
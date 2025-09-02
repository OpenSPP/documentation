---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Uninstalling OpenSPP

This guide provides detailed instructions for uninstalling OpenSPP from your system. It covers both complete removal, which includes deleting the application, configuration files, and database, as well as a partial uninstallation that keeps your data intact for future use.

## Complete Uninstallation

To completely remove OpenSPP from your system:

### Step 1: Stop and Disable Services

```bash
# Stop OpenSPP service
sudo systemctl stop openspp

# Disable service from starting on boot
sudo systemctl disable openspp

# Remove systemd service file
sudo rm -f /etc/systemd/system/openspp.service
sudo rm -f /lib/systemd/system/openspp.service

# Reload systemd
sudo systemctl daemon-reload
```

### Step 2: Remove OpenSPP Package

```bash
# Remove OpenSPP package
sudo apt-get remove --purge openspp-17-daily

# Remove configuration files
sudo rm -rf /etc/openspp

# Remove data directories
sudo rm -rf /var/lib/openspp
sudo rm -rf /var/log/openspp

# Remove binary files
sudo rm -f /usr/bin/openspp-server
sudo rm -f /usr/bin/openspp-shell
```

### Step 3: Remove PostgreSQL Database (Optional)

**Warning**: This will permanently delete all OpenSPP data.

```bash
# Drop the OpenSPP database
sudo -u postgres dropdb openspp_prod

# Remove the OpenSPP PostgreSQL user
sudo -u postgres dropuser openspp
```

### Step 4: Remove Repository Configuration

```bash
# Remove APT repository configuration
sudo rm -f /etc/apt/sources.list.d/openspp.list

# Remove GPG key (if added)
sudo apt-key del "OpenSPP Repository"

# Update package list
sudo apt-get update
```

### Step 5: Clean Up Dependencies (Optional)

If you want to remove PostgreSQL as well:

```bash
# Remove PostgreSQL
sudo apt-get remove --purge postgresql postgresql-client postgresql-common

# Remove PostgreSQL data
sudo rm -rf /var/lib/postgresql

# Remove PostgreSQL configuration
sudo rm -rf /etc/postgresql
```

## Partial Uninstallation

If you want to keep the database but remove the application:

```bash
# Stop service
sudo systemctl stop openspp
sudo systemctl disable openspp

# Remove package but keep configuration
sudo apt-get remove openspp-17-daily

# Keep database and filestore for potential reinstallation
# /var/lib/openspp/ and PostgreSQL database remain intact
```

## Reinstall After Uninstallation

To reinstall OpenSPP after uninstallation:

```bash
# Follow the installation steps from the beginning
# If you kept the database, you can reuse it by:
# 1. Reinstall OpenSPP
# 2. Update configuration to point to existing database
# 3. Start service
```
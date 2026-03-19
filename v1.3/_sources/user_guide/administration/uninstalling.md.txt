
# Uninstalling OpenSPP

This guide provides instructions for uninstalling OpenSPP from a Debian or Ubuntu system. It covers two main scenarios:
- **Complete uninstallation**: Removes the application, configuration, data, and database.
- **Partial uninstallation**: Removes the application but keeps your data and configuration for future use.

## Before you begin: back up your data

**Warning**: A complete uninstallation is irreversible and will permanently delete your data. Before proceeding, it is strongly recommended to create a full backup of your database and filestore.

For detailed backup instructions, refer to the {doc}`database_management` guide.

## Complete uninstallation

Follow these steps to completely remove OpenSPP and all its components from your system.

### Step 1: Stop and disable the OpenSPP service

**Stop and disable (remove) OpenSPP service**
```bash
sudo systemctl stop openspp
sudo systemctl disable openspp
```

### Step 2: Remove OpenSPP package

**Remove OpenSPP package and configuration files**
```bash
sudo apt-get remove --purge openspp-17-daily
sudo rm -rf /etc/openspp
sudo rm -rf /var/lib/openspp
sudo rm -rf /var/log/openspp
sudo rm -f /usr/bin/openspp-server
sudo rm -f /usr/bin/openspp-shell
```

### Step 3: Remove PostgreSQL database (Optional)

**Warning**: This will permanently delete all OpenSPP data.


**Drop the OpenSPP database and remove the user**
```bash
sudo -u postgres dropdb name_of_your_db
sudo -u postgres dropuser openspp
```

### Step 4: Remove repository configuration

**Remove APT repository configuration and GPG Key**
```bash
sudo rm -f /etc/apt/sources.list.d/openspp.list
sudo apt-key del "OpenSPP Repository"
sudo apt-get update
```

### Step 5: Clean up dependencies (Optional)

If you want to remove PostgreSQL as well:

**Remove PostgreSQL and its data and configuration**
```bash
sudo apt-get remove --purge postgresql postgresql-client postgresql-common
sudo rm -rf /var/lib/postgresql
sudo rm -rf /etc/postgresql
```

## Partial uninstallation

If you want to keep the database but remove the application:


**Stop, disable (remove) service, and remove package** 
```bash
sudo systemctl stop openspp
sudo systemctl disable openspp
sudo apt-get remove openspp-17-daily
```

- Keep database and filestore for potential reinstallation 
- var/lib/openspp/ and PostgreSQL database remain intact

## Reinstall after uninstallation

To reinstall OpenSPP after uninstallation, follow the {doc}`../../getting_started/installation_deb`.
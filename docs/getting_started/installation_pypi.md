---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Installing OpenSPP using PyPI

This guide explains how to install OpenSPP modules from the Python Package Index (PyPI) for development and production environments.

## Prerequisites

Before installing OpenSPP via PyPI, ensure you have:

- Python 3.8 or higher
- pip (Python package installer)
- A working Odoo 15.0 installation
- PostgreSQL database

## Setting up Odoo 15.0

OpenSPP is built on top of Odoo 15.0. You need to have Odoo 15.0 installed first.

### Install Odoo 15.0 from PyPI

```bash
pip install odoo==15.0
```

### Install system dependencies

Depending on your operating system, you may need to install additional system packages:

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev \
    libssl-dev libpq-dev postgresql postgresql-contrib
```

**CentOS/RHEL:**
```bash
sudo yum install python3-devel libxml2-devel libxslt-devel openldap-devel \
    postgresql-devel postgresql-server postgresql-contrib
```

## Installing OpenSPP modules

### Available OpenSPP packages

OpenSPP modules are available as separate packages on PyPI:

- `openspp-registry` - Core registry functionality
- `openspp-programs` - Program management modules
- `openspp-base` - Base OpenSPP functionality

### Install core OpenSPP modules

```bash
pip install openspp-registry openspp-programs openspp-base
```

### Install additional modules

For specific use cases, you can install additional modules:

```bash
# For farmer registry functionality
pip install openspp-farmer-registry

# For payment integrations
pip install openspp-payments

# For API functionality
pip install openspp-api
```

## Configuration

### 1. Create configuration file

Create an Odoo configuration file (`odoo.conf`):

```ini
[options]
addons_path = /path/to/openspp/addons,/path/to/odoo/addons
admin_passwd = your_admin_password
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo_password
xmlrpc_port = 8069
logfile = /var/log/odoo/odoo.log
```

### 2. Initialize database

Create a new database for your OpenSPP instance:

```bash
odoo -c odoo.conf -d openspp_db -i base --stop-after-init
```

### 3. Install OpenSPP modules

Install the required OpenSPP modules:

```bash
odoo -c odoo.conf -d openspp_db -i spp_base,g2p_registry_base --stop-after-init
```

## Running OpenSPP

Start your OpenSPP instance:

```bash
odoo -c odoo.conf
```

Your OpenSPP instance will be available at `http://localhost:8069`

## Production deployment

For production deployments:

1. Use a reverse proxy (nginx, Apache)
2. Configure SSL certificates
3. Set up proper database backups
4. Configure log rotation
5. Use a process manager (systemd, supervisor)

### Example systemd service

Create `/etc/systemd/system/openspp.service`:

```ini
[Unit]
Description=OpenSPP Server
After=network.target postgresql.service

[Service]
Type=simple
User=odoo
Group=odoo
ExecStart=/usr/local/bin/odoo -c /etc/odoo/odoo.conf
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## Troubleshooting

### Common issues

1. **Module not found**: Ensure the module path is correctly set in `addons_path`
2. **Database connection errors**: Verify PostgreSQL is running and credentials are correct
3. **Permission errors**: Check file permissions for Odoo user

### Getting help

- Check the {doc}`../developer_guide/troubleshooting` guide
- Visit the [OpenSPP Community](https://openspp.org/community/)
- Report issues on [GitHub](https://github.com/OpenSPP/openspp)

## Next steps

After installation, see:

- {doc}`../user_guide/index` for using OpenSPP features
- {doc}`../developer_guide/index` for customization and development
- {doc}`poc_and_pilot` for setting up pilot programs

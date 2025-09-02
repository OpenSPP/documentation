---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Installation Guide

This guide walks you through installing OpenSPP on Ubuntu 24.04 or Debian 12 (Bookworm) using the official APT repository hosted on Nexus.

## Prerequisites

Before installing OpenSPP, ensure you have:

- Ubuntu 24.04 LTS (Noble Numbat) or Debian 12 (Bookworm)
- 64-bit Intel or AMD CPU (amd64)
- Minimum 4GB RAM (8GB recommended for production)
- Minimum 10GB disk space
- Root or sudo access
- Internet connection for downloading packages
- Access to https://builds.acn.fr (OpenSPP APT repository)

## Step 1: Update System

First, ensure your system is up to date and install `wget` and `gnupg2`:

```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y wget gnupg2
```

## Step 2: Install PostgreSQL

OpenSPP requires PostgreSQL as its database backend. Install and verify by running the commands:

```bash
sudo apt-get install -y postgresql postgresql-client
sudo systemctl status postgresql
```

## Step 3: Configure OpenSPP Repository

Add the OpenSPP APT repository to your system:

```bash
wget -qO - https://builds.acn.fr/repository/apt-keys/openspp/public.key | sudo apt-key add -
echo "deb https://builds.acn.fr/repository/apt-openspp-daily bookworm main" | \
  sudo tee /etc/apt/sources.list.d/openspp.list
sudo apt-get update
```

## Step 4: Install OpenSPP

Install OpenSPP directly from the repository:

### Install OpenSPP package
```bash
sudo apt-get install -y openspp-17-daily
```

### Alternative: Manual Download

If you prefer to download the package manually or the repository is not accessible:

```bash
mkdir -p ~/openspp-install && cd ~/openspp-install
wget https://builds.acn.fr/repository/apt-openspp/pool/main/o/openspp/openspp_17.0.1+odoo17.0-1_amd64.deb
sudo dpkg -i openspp_17.0.1+odoo17.0-1_amd64.deb
```

#### Fix any dependency issues if they occur
```bash
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

### Create the openspp PostgreSQL user
```bash
sudo -u postgres createuser -s openspp
```
### Set password (Optional)
If you want to use password authentication instead of peer authentication
```bash
sudo -u postgres psql -c "ALTER USER openspp WITH PASSWORD 'your_secure_password';"
```

## Step 6: Configure OpenSPP

### Basic Configuration

The main configuration file is located at `/etc/openspp/odoo.conf`. 

1. **Set the admin password** (IMPORTANT for security):

### Generate a strong password
```bash
openssl rand -base64 32
```
Copy the generated password

### Edit the configuration
```bash
sudo nano /etc/openspp/odoo.conf
```

Find and update these lines (paste the generated password):
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

### Enable the service to start on boot
```bash
sudo systemctl enable openspp
```
### Start the service
```bash
sudo systemctl start openspp
```
### Check service status
Type `q`to exit this state
```bash
sudo systemctl status openspp
```
### Restart the service
Needed for config changes to be applied
```bash
sudo systemctl restart openspp
```

You should see output indicating the service is active and running.

## Step 8: Create Your First Database

### Option A: Via Web Interface (Recommended)

**Prerequisites**: Ensure `list_db = True` is set in `/etc/openspp/odoo.conf` (see Step 6).

1. Open a web browser and navigate to:
   ```
   http://your-server-ip:8069
   # e.g http://localhost:8069
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

Create the database, then restart the service:
```bash
sudo -u openspp openspp-server \
    --database=openspp_prod \
    --init=base \
    --stop-after-init
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
2. Search and install `spp_mis_demo` (OpenSPP Demo) or `spp_farmer_registry_demo` (OpenSPP Farmer Registry Demo)
3. Restart OpenSPP after installing the demo modules:
   ```bash
   sudo systemctl restart openspp
   ```

**Note**: The `queue_job` module, which is essential for asynchronous background tasks, is automatically installed as a dependency of the main OpenSPP modules. It is also pre-configured as a `server_wide_module`, ensuring that background workers can process jobs correctly after a service restart.


## Getting Help

- **Documentation**: https://docs.openspp.org
- **Community Forum**: https://community.openspp.org
- **Issue Tracker**: https://github.com/openspp/openspp-modules/issues
- **Email Support**: support@openspp.org
- **APT Repository**: https://builds.acn.fr/repository/apt-openspp/


## Next Steps

Now that OpenSPP is installed, here are some recommended next steps:

- **Learn to Use OpenSPP**: Start with the {doc}`../user_guide/index` to understand core features.
- **Administer the System**: Refer to the {doc}`../user_guide/administration/index` for guides on security, maintenance, and troubleshooting.
- **Customize and Develop**: Explore the {doc}`../developer_guide/index` to learn how to extend the platform. 
- **Set Up a Pilot Program**: Follow the {doc}`../overview/poc_and_pilot` guide to launch a Proof of Concept (PoC).

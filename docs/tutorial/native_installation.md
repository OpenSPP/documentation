# OpenSPP Installation Guide for Non-Docker Environments

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Prerequisites](#prerequisites)
3. [Development Environment Installation](#development-environment-installation)
4. [Production Environment Setup](#production-environment-setup)
5. [Database Configuration](#database-configuration)
6. [Module Installation](#module-installation)
7. [Troubleshooting](#troubleshooting)

## System Requirements <a name="system-requirements"></a>

### Minimum Requirements
- **Operating System**: Ubuntu 20.04/22.04 LTS (recommended), Debian 11+, or CentOS 7+
- **CPU**: 2 cores (4 recommended for production)
- **RAM**: 4GB (8GB recommended for production)
- **Storage**: 20GB free space (SSD recommended)
- **Python**: 3.7 - 3.10
- **PostgreSQL**: 12 - 15
- **Node.js**: 14.x or 16.x (for frontend assets)

### Recommended for Production
- 4+ CPU cores
- 16GB RAM
- 100GB+ SSD storage
- Dedicated PostgreSQL server
- Firewall configured to allow ports 80, 443, and 5432 (if PostgreSQL is local)

## Prerequisites <a name="prerequisites"></a>

### For Ubuntu/Debian:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git python3-pip python3-dev python3-venv python3-wheel \
    libxml2-dev libxslt1-dev libzip-dev libsasl2-dev libldap2-dev \
    libssl-dev libpq-dev postgresql postgresql-client postgresql-contrib \
    build-essential wget nodejs npm libfreetype6-dev libjpeg-dev \
    zlib1g-dev libopenjp2-7-dev liblcms2-dev
```
### For CentOS/RHEL:
```bash
sudo yum update -y
sudo yum install -y git python3-pip python3-devel gcc postgresql postgresql-server \
    postgresql-contrib postgresql-devel libxml2-devel libxslt-devel \
    libzip-devel openldap-devel openssl-devel nodejs npm freetype-devel \
    libjpeg-turbo-devel zlib-devel libopenjp2-devel liblcms2-devel
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

## Development Environment Installation <a name="development-environment-installation"></a>

### 1. Create a Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 2. Upgrade pip and Install Required Python Packages
```bash
pip install --upgrade pip wheel setuptools
```

### 3. Clone the OpenSPP Source Code
```bash 
git clone https://github.com/OpenSPP/openspp.git
cd openspp
git clone https://github.com/OpenSPP/openspp-modules.git addons
```

### 4. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 5. Install Node.js Dependencies (Frontend Assets)
```bash 
cd addons/web
npm install
npm run build
cd ../..
```
## Production Environment Setup <a name="production-environment-setup"></a>

### 1. Create a System User (optional but recommended)
```bash
sudo useradd -m -d /opt/openspp -U -r -s /bin/bash openspp
sudo su - openspp
```

### 2. Set Up Directories
Place your OpenSPP source code in /opt/openspp or your preferred location.

Ensure correct permissions for the system user.

### 3. Set Up a Python Virtual Environment
```bash 
python3 -m venv venv
source venv/bin/activate
```

### 4. Configure Gunicorn (for production)
```bash 
pip install gunicorn
```

### 5. Set Up a Reverse Proxy (Nginx/Apache)
Configure Nginx to proxy requests to Gunicorn and serve static files.

## Database Configuration <a name="database-configuration"></a>

### 1. Initialize PostgreSQL
```bash
sudo -u postgres createuser -s openspp_user
sudo -u postgres createdb openspp_db -O openspp_user
sudo -u postgres psql
# Set password for the user
ALTER USER openspp_user WITH PASSWORD 'yourpassword';
\q
```

### 2. Update OpenSPP Configuration
```bash
[options]
db_host = localhost
db_port = 5432
db_user = openspp_user
db_password = yourpassword
db_name = openspp_db
addons_path = ./addons
```

## Module Installation <a name="module-installation"></a>

### 1. Ensure All Modules Are Present
Place all required OpenSPP modules in the addons directory.

### 2. Update Addons Path

In your configuration file, ensure addons_path includes all relevant module directories.

### 3. Initialize Database with Modules

Run Odoo/OpenSPP with the -i flag to install core modules:
```bash
python odoo-bin -c openspp.conf -i base,openspp_core,openspp_module1,openspp_module2
```
![alt text](<Screenshot 2025-06-19 093519.png>)
## Troubleshooting <a name="troubleshooting"></a>
<li> Database Connection Errors: Double-check your PostgreSQL credentials and ensure the service is running.

<li> Missing Dependencies: Re-run pip install -r requirements.txt and check for system library errors.

<li> Frontend Build Issues: Ensure Node.js and npm versions are compatible; delete node_modules and reinstall if needed.

<li> Permission Issues: Ensure the OpenSPP user has read/write access to all relevant directories.

<li> Logs: Check logs in the OpenSPP directory or via systemd if running as a service.


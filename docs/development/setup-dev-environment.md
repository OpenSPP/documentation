
# OpenSPP Development Environment Setup (Bash Script)

This guide explains how to use an automated Bash script to set up a complete OpenSPP development environment on **Ubuntu/Debian** or **macOS** systems.

---

## ��� What This Script Does

The script automates:

- OS detection (Ubuntu/Debian/macOS)
- Installation of system dependencies
- Setup of Python virtual environment
- Installation of PostgreSQL and creation of databases
- Cloning of OpenSPP and Odoo repositories
- Installation of Python and Node.js dependencies
- Configuration of Odoo
- Initialization of test data
- Pre-commit hook setup
- Creation of helper scripts for development

---

## Prerequisites

Before running the setup script, ensure you have:

- A supported operating system:
  - Ubuntu 20.04 or later
  - Debian 10 or later
  - macOS 10.15 or later
  - Windows 10/11 with WSL2 (see [Windows Setup](#windows-setup))
- Administrative (sudo) access
- At least 4GB of RAM
- At least 10GB of free disk space
- A stable internet connection

---

## ��� Quick Start

### Linux/macOS

1. Download the setup script:

   ```bash
   wget https://raw.githubusercontent.com/OpenSPP/openspp-modules/main/scripts/setup-dev-env.sh
   ```

2. Make it executable:

   ```bash
   chmod +x setup-dev-env.sh
   ```

3. Run the script:

   ```bash
   ./setup-dev-env.sh
   ```

### Windows Setup

#### Using WSL2 (Recommended)

1. Install WSL2 with Ubuntu:

   ```powershell
   wsl --install -d Ubuntu-22.04
   ```

---

## Script Options

The setup script supports the following options:

- `--branch BRANCH`: Specify the OpenSPP branch to checkout (default: main)
- `--python VERSION`: Specify Python version to use (default: 3.10)
- `--odoo-version VERSION`: Specify Odoo version to clone (default: 15.0)
- `--help`: Display help message

Examples:

```bash
# Use a specific branch
./setup-dev-env.sh --branch develop

# Use Python 3.11 and Odoo 16.0
./setup-dev-env.sh --python 3.11 --odoo-version 16.0

# Dry run to see what would be installed
./setup-dev-env.sh --dry-run
```

---

## What Gets Installed

### System Dependencies

- Python 3.10+ and development headers
- PostgreSQL 14
- Node.js 18
- Git
- Libraries for image processing, XML, cryptography

### Python Packages

- Odoo 15.0 requirements
- OpenSPP requirements
- Dev tools (black, flake8, pre-commit, pytest)

### Directory Structure

```bash
~/openspp-dev/
├── venv/                 # Python virtual environment
├── odoo/                 # Odoo source code
├── openspp-modules/      # OpenSPP modules repository
├── openspp-docs/         # OpenSPP documentation
├── odoo.conf             # Odoo configuration
├── start_openspp.sh      # Start server
└── update_openspp.sh     # Update environment
```

---

## Post-Installation Steps

### Activate Virtual Environment

```bash
source ~/openspp-dev/venv/bin/activate
```

### Start Development Server

```bash
~/openspp-dev/start_openspp.sh
```

### Access OpenSPP

- Open [http://localhost:8069](http://localhost:8069)
- Login with admin credentials

### Install Modules

1. Log in as admin
2. Navigate to Apps
3. Remove "Apps" filter
4. Search for "spp" and install modules

---

## Updating Your Environment

To get the latest updates:

```bash
~/openspp-dev/update_openspp.sh
```

This updates:

- Repositories
- Python dependencies
- Database modules

---

## Troubleshooting

### PostgreSQL Connection Error

```bash
# Linux
sudo systemctl status postgresql
sudo systemctl restart postgresql

# macOS
brew services list
brew services restart postgresql@14
```

### Python Version Issues

```bash
python3.10 -m venv ~/openspp-dev/venv
```

### Permissions

```bash
sudo chown -R $USER:$USER ~/openspp-dev
chmod -R u+rwX ~/openspp-dev
```

### Module Import Errors

```bash
source ~/openspp-dev/venv/bin/activate
pip install -r odoo/requirements.txt
pip install -r openspp-modules/requirements.txt
```

### Port Conflict

```bash
lsof -i :8069
kill <pid>
```

---

## Verification Steps

```bash
python --version
psql --version
psql -l | grep openspp
source ~/openspp-dev/venv/bin/activate
python -c "import odoo; print(odoo.__version__)"
```

---

## Development Workflow

### Create Feature Branch

```bash
cd ~/openspp-dev/openspp-modules
git checkout -b feature/your-feature
```

### Run Tests

```bash
python -m pytest
python -m pytest tests/test_module.py
python -m pytest --cov=your_module tests/
```

### Commit and Push

```bash
git add .
git commit -m "feat: your change"
git push origin feature/your-feature
```

---

## IDE Configuration

### VS Code

```json
{
  "python.defaultInterpreterPath": "~/openspp-dev/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}
```

### PyCharm

1. Set interpreter: `~/openspp-dev/venv/bin/python`
2. Mark `openspp-modules` and `odoo/addons` as Source Root

---

## Database Management

```bash
createdb -O $USER openspp_dev
pg_dump openspp_dev > backup.sql
psql openspp_dev < backup.sql
```

---

## Performance Tips

### Development

```ini
dev_mode = reload,qweb,xml
workers = 0
limit_time_cpu = 600
limit_time_real = 1200
```

### Staging/Production

```ini
workers = 4
dev_mode = False
```

---

## Additional Resources

- [OpenSPP Documentation](https://docs.openspp.org)
- [OpenSPP GitHub](https://github.com/OpenSPP/openspp-modules)
- [Odoo Dev Docs](https://www.odoo.com/documentation/15.0/developer.html)

---

## Getting Help

- GitHub Issues: [OpenSPP Issues](https://github.com/OpenSPP/openspp-modules/issues)
- Community: [OpenSPP Forum](https://community.openspp.org)
- Discord: [OpenSPP Discord](https://discord.gg/openspp)

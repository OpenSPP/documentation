---
openspp:
  doc_status: draft
---

# Installation

This guide is for **sys admins** deploying and maintaining OpenSPP in development, staging, or production environments.

OpenSPP is a containerized application built on Odoo 17 and PostgreSQL. This guide covers installation methods from quick Docker setups for evaluation to production-ready cloud deployments.

## Installation Methods

| Method | Best For | Complexity | Time |
|--------|----------|------------|------|
| {doc}`docker` | Development, evaluation, production | Low | 15-30 min |
| {doc}`from_source` | Custom development, deep customization | High | 1-2 hours |
| {doc}`cloud` | Production deployments on AWS/Azure/GCP | Medium | 30-60 min |

**Recommendation:** Start with Docker. It's the officially supported deployment method and used by production OpenSPP installations worldwide.

## System Requirements

### Minimum (Evaluation/Development)

| Component | Requirement |
|-----------|-------------|
| CPU | 2 cores |
| RAM | 4 GB |
| Disk | 20 GB SSD |
| OS | Ubuntu 20.04+, Debian 11+, RHEL 8+, macOS 12+ |

### Recommended (Production)

| Component | Requirement |
|-----------|-------------|
| CPU | 4+ cores |
| RAM | 8+ GB (16 GB for large registries) |
| Disk | 100+ GB SSD (scale with data volume) |
| OS | Ubuntu 22.04 LTS, Debian 12 |
| Network | 1 Gbps, static IP |

### Database Server (Production)

| Component | Requirement |
|-----------|-------------|
| CPU | 4+ cores |
| RAM | 16+ GB |
| Disk | 200+ GB SSD with RAID 10 |
| PostgreSQL | Version 15 |
| Extensions | PostGIS 3.3+ |

## Prerequisites

All installation methods require:

### Docker Installation (Recommended)

```shell
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

Logout and login for group changes to take effect.

### Docker Compose

```shell
# Install Docker Compose V2
sudo apt-get update
sudo apt-get install docker-compose-plugin

# Verify
docker compose version
```

Expected output: `Docker Compose version v2.x.x`

### Python 3.8+

```shell
# Ubuntu/Debian
sudo apt-get install python3 python3-pip python3-venv

# Verify
python3 --version
```

### Git

```shell
# Ubuntu/Debian
sudo apt-get install git

# Verify
git --version
```

### Required Ports

Ensure these ports are available:

| Port | Service | Can Change? |
|------|---------|-------------|
| 17069 | Odoo HTTP | Yes, via config |
| 5432 | PostgreSQL (external access) | Optional |
| 8069 | Longpolling | Yes, via config |

## Network Requirements

### Outbound Access Required

OpenSPP needs outbound access to:

- `github.com` - Code repositories
- `pypi.org` - Python packages
- `hub.docker.com` / `ghcr.io` - Docker images
- `deb.debian.org` / `archive.ubuntu.com` - System packages

### Firewall Rules (Production)

```shell
# Allow HTTP/HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Allow Odoo (if not behind reverse proxy)
sudo ufw allow 17069/tcp

# Enable firewall
sudo ufw enable
```

## Security Considerations

**Before installing in production:**

- [ ] Use SSL/TLS certificates (Let's Encrypt or commercial)
- [ ] Configure a reverse proxy (Nginx/Traefik)
- [ ] Set strong database passwords
- [ ] Enable database backups
- [ ] Restrict database network access
- [ ] Configure log aggregation
- [ ] Set up monitoring and alerts
- [ ] Review {doc}`/ops_guide/security/access_control`

## Quick Decision Guide

**Choose Docker if:**
- You want the fastest setup
- You're evaluating OpenSPP
- You need a production deployment
- You want official support

**Choose From Source if:**
- You're developing OpenSPP modules
- You need to modify core code
- You have specific Python environment needs
- You're contributing to OpenSPP

**Choose Cloud if:**
- You need high availability
- You want managed infrastructure
- You're deploying multiple environments
- You need auto-scaling

## Next Steps

```{toctree}
:maxdepth: 1

docker
from_source
cloud
```

## Are You Stuck?

**Docker daemon not running**
```shell
# Ubuntu/Debian
sudo systemctl start docker
sudo systemctl enable docker
```

**Permission denied accessing Docker**
```shell
# Add user to docker group
sudo usermod -aG docker $USER
# Logout and login
```

**Port 17069 already in use**
Edit `.env` in `openspp-docker` and change `ODOO_MAJOR=17` to use a different port, or stop the conflicting service:
```shell
# Find what's using the port
sudo lsof -i :17069
```

**PostgreSQL connection refused**
Check if PostgreSQL container is running:
```shell
docker compose ps
docker compose logs db
```

## Support

- Documentation: https://docs.openspp.org
- Community Forum: https://github.com/OpenSPP/openspp-docker/discussions
- Issue Tracker: https://github.com/OpenSPP/openspp-docker/issues
- Security Issues: security@openspp.org

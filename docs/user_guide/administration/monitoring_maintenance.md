
# Monitoring and Maintenance

This section provides basic instructions for monitoring your OpenSPP system, viewing logs, managing services, and performing updates. Regular monitoring and maintenance help keep your system running smoothly and securely.

## View Logs

```bash
# Real-time service logs
sudo journalctl -u openspp -f

# Application logs
sudo tail -f /var/log/openspp/openspp.log

# PostgreSQL logs
sudo tail -f /var/log/postgresql/postgresql-*.log
```

## Service Management

```bash
# Restart service
sudo systemctl restart openspp

# Stop service
sudo systemctl stop openspp

# Start service
sudo systemctl start openspp

# Reload configuration without restart
sudo systemctl reload openspp
```

## Update OpenSPP

When a new version is available:

```bash
# Update package list
sudo apt-get update

# Check for OpenSPP updates
apt list --upgradable | grep openspp

# Stop service before upgrade
sudo systemctl stop openspp

# Backup current installation
sudo tar -czf /var/backups/openspp-backup-$(date +%Y%m%d).tar.gz /opt/openspp /etc/openspp

# Upgrade OpenSPP
sudo apt-get upgrade openspp

# Start service
sudo systemctl start openspp

# Update modules via web interface
```

## Alternative: Manual Update

If updating manually:

```bash
# Download new package from Nexus
wget https://builds.acn.fr/repository/apt-openspp/pool/main/o/openspp/openspp_X.X.X_amd64.deb

# Stop service
sudo systemctl stop openspp

# Backup current installation
sudo tar -czf /var/backups/openspp-backup-$(date +%Y%m%d).tar.gz /opt/openspp /etc/openspp

# Install new version
sudo dpkg -i openspp_X.X.X_amd64.deb

# Start service
sudo systemctl start openspp
```
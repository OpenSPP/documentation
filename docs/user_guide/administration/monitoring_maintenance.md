
# Monitoring and Maintenance

This section provides basic instructions for monitoring your OpenSPP system, viewing logs, managing services, and performing updates. Regular monitoring and maintenance help keep your system running smoothly and securely.

## View Logs

### Real-time service logs

```bash
sudo journalctl -u openspp -f
```

### Application logs
```bash
sudo tail -f /var/log/openspp/openspp.log
```

### PostgreSQL logs
```bash
sudo tail -f /var/log/postgresql/postgresql-*.log
```

## Service Management

### Restart service
```bash
sudo systemctl restart openspp
```

### Stop service
```bash
sudo systemctl stop openspp
```

### Start service
```bash
sudo systemctl start openspp
```

### Reload configuration without restart
```bash
sudo systemctl reload openspp
```

## Update OpenSPP

When a new version is available, run the following commands to get the latest version of OpenSPP and upgrade it:

```bash
sudo apt-get update
apt list --upgradable | grep openspp
sudo systemctl stop openspp
sudo tar -czf /var/backups/openspp-backup-$(date +%Y%m%d).tar.gz /opt/openspp /etc/openspp
sudo apt-get upgrade openspp
sudo systemctl start openspp
```

## Alternative: Manual Update

If updating manually, run the following commands to get the latest debian package and upgrade OpenSPP:

```bash
wget https://builds.acn.fr/repository/apt-openspp/pool/main/o/openspp/openspp_X.X.X_amd64.deb
sudo systemctl stop openspp
sudo tar -czf /var/backups/openspp-backup-$(date +%Y%m%d).tar.gz /opt/openspp /etc/openspp
sudo dpkg -i openspp_X.X.X_amd64.deb
sudo systemctl start openspp
```

**Note**: Replace X.X.X with the target version number in the wget and dpkg commands.
---
openspp:
  doc_status: draft
---

# Attachment Antivirus Scan

**Module:** `spp_attachment_av_scan`

## Overview

OpenSPP Attachment Antivirus Scan module for OpenSPP.

## Purpose

This module is designed to:

- **Scan attachments for malware:** Automatically queue antivirus scans for all binary attachments on creation and update using ClamAV.
- **Quarantine infected files:** Remove infected file data and store an encrypted backup for forensic analysis, preventing malware from being downloaded.
- **Manage quarantined files:** Provide AV administrators with tools to restore false positives, download for analysis, or permanently delete quarantined files.
- **Notify security administrators:** Send internal notifications to the AV Admin group when malware is detected.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `base` | Odoo core framework |
| `mail` | Communication and activity tracking |
| `job_worker` | Background job worker |
| `spp_encryption` | Implements advanced cryptographic services for OpenSPP, e... |
| `spp_security` | Central security definitions for OpenSPP modules |

### External Dependencies

| Package | Purpose |
| --- | --- |
| `pyclamd` | Python interface to ClamAV daemon for malware scanning |

## Key Features

### Scanner Backend Configuration

The `spp.av.scanner.backend` model configures ClamAV connections. Two backend types are supported:

| Backend Type | Description |
| --- | --- |
| ClamAV Unix Socket | Connect via local Unix socket (default: `/var/run/clamav/clamd.sock`) |
| ClamAV Network | Connect via TCP to a remote ClamAV daemon (host + port) |

Each backend has configurable file size limits (default 100 MB) and scan timeouts (default 60 seconds). A **Test Connection** button verifies connectivity and displays the ClamAV version.

### Automatic Scanning

Every binary attachment is automatically queued for scanning via `job_worker` background jobs when created or updated. The scan lifecycle adds these fields to `ir.attachment`:

| Field | Description |
| --- | --- |
| Scan Status | pending, scanning, clean, infected, error, or skipped |
| Scan Date | When the scan completed |
| Threat Name | Name of detected malware (if infected) |
| Is Quarantined | Whether the file has been quarantined |

Files exceeding the configured maximum size are skipped. Attachments can also be manually rescanned via the **Rescan** action.

### Quarantine Workflow

When malware is detected, the module:

1. Marks the attachment as quarantined
2. Computes a SHA256 hash of the original file
3. Encrypts the file data using the configured encryption provider
4. Stores the encrypted backup in the `quarantine_data` field
5. Removes the original file data (`datas` set to False)
6. Notifies AV administrators via internal message

Access to quarantined attachment data is blocked at the `read()` level -- any attempt to read `datas` on a quarantined record returns False.

### AV Admin Actions

Users in the `group_av_admin` security group can perform these actions on quarantined files:

| Action | Description |
| --- | --- |
| Restore | Decrypt and restore the original file (for false positives), with size and hash verification |
| Download for Analysis | Decrypt and create a temporary download attachment for forensic analysis |
| Permanently Delete | Remove both the encrypted backup and the attachment record |

### Automated Cleanup

Two cron jobs maintain the quarantine system:

| Cron Job | Description |
| --- | --- |
| Purge Old Quarantined Files | Remove encrypted backups older than the retention period (default 90 days) |
| Cleanup Forensic Downloads | Delete temporary forensic download attachments after retention period (default 24 hours) |

## Integration

- **job_worker:** Malware scans run as background jobs via `with_delay()`, ensuring attachment creation is not blocked by scan latency.
- **spp_encryption:** Quarantined file data is encrypted using a JWCrypto encryption provider before storage, and decrypted on restore or forensic download.
- **mail:** Security notifications for infected files are sent as internal messages to partners of AV admin users.

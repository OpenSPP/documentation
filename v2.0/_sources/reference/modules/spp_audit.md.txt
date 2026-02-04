---
openspp:
  doc_status: draft
---

# Audit

**Module:** `spp_audit`

## Overview

The Audit module (`spp_audit`) provides comprehensive tracking of all data modifications and user actions across the OpenSPP platform. It records old and new values for configured data fields, maintaining an immutable history of changes crucial for internal audits, compliance, and detecting unauthorized alterations.

## Purpose

This module is designed to:

- **Track data changes:** Record create, update, and delete operations on configured models
- **Maintain audit trail:** Store before/after values for changed fields
- **Support compliance:** Provide evidence for regulatory audits and investigations
- **Enable forensics:** Detect unauthorized or accidental data modifications
- **Prevent tampering:** Log configuration changes to tamper-resistant backends

## Module Dependencies

| Dependency           | Description                         |
| -------------------- | ----------------------------------- |
| `base`               | Odoo core framework                 |
| `mail`               | Mail thread for audit notifications |
| `spp_registry`       | Registry models to audit            |
| `spp_security`       | Security groups and access control  |
| `spp_programs`       | Program models to audit             |
| `spp_service_points` | Service point models to audit       |

### External Python Dependencies

| Package    | Description                             |
| ---------- | --------------------------------------- |
| `requests` | HTTP backend for external audit logging |

## Key Features

### Audit Rules

Configure which models and fields to track:

| Setting          | Description                                   |
| ---------------- | --------------------------------------------- |
| Name             | Unique rule identifier                        |
| Model            | Target model to audit                         |
| Fields to Log    | Specific fields to track (blank = all fields) |
| Log Creation     | Track new record creation                     |
| Log Update       | Track field modifications                     |
| Log Deletion     | Track record deletion                         |
| View Logs Action | Add "View Logs" to record action menu         |

### Lifecycle Action Logging

Track explicit state changes:

| Action         | Description                        |
| -------------- | ---------------------------------- |
| Activation     | Record enabled/activated           |
| Deactivation   | Record disabled/deactivated        |
| State Changes  | Draft, approve, reject transitions |
| File Downloads | Attachment downloads               |
| File Previews  | Attachment views                   |
| Data Exports   | Export operations                  |

### Multiple Backends

Audit logs can be sent to multiple destinations:

| Backend  | Description                                     |
| -------- | ----------------------------------------------- |
| Database | Standard `spp.audit.log` records with UI access |
| File     | JSON log files for archival                     |
| Syslog   | System logging for SIEM integration             |
| HTTP     | Webhook to external audit systems               |

### Tamper Resistance

Configuration changes are always logged to non-database backends:

- Rule creation, modification, deletion logged to file/syslog/HTTP
- Cannot be disabled via database settings
- Provides evidence if audit rules are modified

### Audit Log Records

Each log entry contains:

| Field     | Description                                  |
| --------- | -------------------------------------------- |
| Timestamp | When the action occurred                     |
| User      | Who performed the action                     |
| Model     | What model was affected                      |
| Record ID | Which record was changed                     |
| Method    | Operation type (create, write, unlink, etc.) |
| Data      | Old and new values as structured data        |

### Parent Rule Linking

For related records, link audit logs to parent records:

- Changes to `spp.program.membership` can link to `spp.program`
- Changes to `spp.entitlement` can link to `res.partner`
- Enables viewing all related changes from parent record

## Integration

### Automatic Auditing

Once configured, auditing is automatic:

```python
# This write operation is automatically logged
partner.write({"name": "New Name"})
```

### Explicit Lifecycle Logging

For custom actions, log explicitly:

```python
self.env["spp.audit.rule"].log_lifecycle_action(
    model_name="spp.program",
    record_id=program.id,
    action="approve",
    old_values={"state": "draft"},
    new_values={"state": "approved"}
)
```

### Viewing Audit Logs

From any audited record:

1. Open the record form view
2. Click **Action** menu
3. Select **View Logs**

Or navigate to **Settings > Technical > Audit > Audit Logs**.

### Mail Thread Integration

Optionally post audit summaries to record chatter:

| Setting            | Recommendation                          |
| ------------------ | --------------------------------------- |
| Enabled            | Low-volume, human-reviewed records only |
| Disabled (default) | High-volume or automated processes      |

---
openspp:
  doc_status: draft
  products: [core]
---

# Audit backends

This guide is for **implementers** and **system administrators** configuring where audit logs are stored. The default database storage works for most organizations. Advanced options (file, syslog, HTTP) require assistance from your IT team.

## Mental model

Backends determine where audit data goes:

| Backend | Where logs go | Best for |
|---------|-------------|----------|
| **Database** | Inside the system's own database | Default — works for most organizations |
| **File** | Files on the server | Long-term archival, high volume |
| **Syslog** | Centralized logging server | Integration with enterprise security monitoring |
| **HTTP** | External web service | Cloud-based audit systems |

Think of it like choosing where to save files: **database** is your local hard drive (fast, searchable), **file** is an external backup drive, **syslog** is your corporate logging server, and **HTTP** is a cloud storage service.

## Backend configuration

### Database backend (recommended)

The default backend. Logs are stored in the system's database and viewable through the **Audit Logs** menu.

| Advantage | Limitation |
|-----------|-----------|
| Searchable through the interface | Grows database size over time |
| No additional setup needed | May need periodic cleanup for very large systems |
| Included in standard backups | |

No configuration needed — it works out of the box.

### File backend

Writes audit entries to files on the server. Ask your IT team to set this up.

| Advantage | Limitation |
|-----------|-----------|
| Minimal database impact | Not searchable through the interface |
| Good for long-term archival | Requires IT to manage file storage |

### Syslog backend

Sends audit entries to a centralized logging server. This is typically used in organizations with enterprise security monitoring tools. Ask your IT team to set this up.

| Advantage | Limitation |
|-----------|-----------|
| Integrates with security monitoring tools | Requires IT infrastructure |
| Centralized log management | Not viewable in OpenSPP |

### HTTP backend

Sends audit entries to an external cloud service. Ask your IT team to set this up.

| Advantage | Limitation |
|-----------|-----------|
| Cloud-based logging | Requires external service subscription |
| Logs stored outside the system | Depends on network connectivity |

## Multi-backend setup

You can enable multiple backends simultaneously. For example:

| Backend | Purpose |
|---------|---------|
| Database | Day-to-day UI access and searching |
| File | Long-term archival backup |
| Syslog | SIEM integration for security monitoring |

Each audit event is sent to all active backends.

## Tamper resistance

Audit logs are designed to be immutable:

- Log records cannot be modified after creation
- Each entry has a unique identifier that prevents tampering
- Deletion is restricted to administrators and is itself logged

```{warning}
For maximum tamper resistance, use an external backend (file, syslog, or HTTP) in addition to the database. This ensures audit data exists outside the system being audited. Ask your IT team to set this up.
```

## Are You Stuck?

**Which backend should I use?**

Start with **Database** (the default) — it works for most organizations. Add **File** or **Syslog** if your compliance framework requires logs to be stored outside the system. Your IT team can help determine which is right.

**Can I disable a backend without losing existing logs?**

Yes. Disabling a backend only stops new logs from being sent to it. Existing logs in that backend are preserved.

**HTTP backend failing?**

Ask your IT team to check the connection settings and network access to the external service.

**Database growing too large from audit logs?**

Ask your IT team about archiving old logs and cleaning up entries older than your retention period. Always check your compliance requirements before removing any logs.

## Next steps

- {doc}`overview` - Audit rule configuration

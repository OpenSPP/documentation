---
myst:
  html_meta:
    "description": "Audit logging in OpenSPP"
    "property=og:title": "Audit Logs"
    "keywords": "OpenSPP, audit, audit logs, compliance, Odoo 19"
---

# Audit Logs

OpenSPP includes an audit logging framework implemented by the `spp_audit` module. It records changes made to
configured models and fields, including **old and new values**, to support accountability, compliance, and operational
investigations.

## What `spp_audit` logs

Audit behavior is configured using **Audit Rules**:

- **Standard actions (automatic):**
  - create
  - write
  - unlink (delete)
- **Optional actions (explicit logging):**
  - activation / deactivation
  - generic state changes (for example approve/reject)
  - file access events (download / preview / export)

```{note}
The optional actions are logged only when the application code explicitly calls the lifecycle logging helper (the rule
flags are “allow lists” for those event types).
```

## Access and menus

Audit configuration and logs are available to users with the **Audit Log: Manager** privilege (provided by `spp_audit`).

Menus:

- **Audit Log → Audit → Rule** (configure what is logged)
- **Audit Log → Audit → Log** (view audit log entries)

### Screenshot placeholders

- `technical_reference/audit_logs/audit_menu.png`: Audit Log menu + submenus
- `technical_reference/audit_logs/audit_rule_form.png`: Audit Rule form with action toggles and field selection
- `technical_reference/audit_logs/audit_log_form.png`: Audit Log entry showing “Changes”

## Configuring audit rules

An audit rule defines:

- **Model**: which Odoo model is audited (for example registry, programs, service points)
- **Fields to log**: which fields are tracked (recommended: keep this minimal and meaningful)
- **Which actions to log**: create/write/unlink and optional lifecycle/file events

Some deployments also use rule hierarchy:

- **Parent Rule** + **Connecting Field** let a rule link changes on a child model back to a parent record (for example a
  program configuration component posting audit info on the program record).

## Viewing and interpreting logs

Each audit log entry captures:

- timestamp
- user
- model + record identifier
- method/action
- a “Changes” table showing old vs new values for each changed field

Open a log entry from **Audit Log → Audit → Log** to see the change details.

```{note}
Audit rendering respects field-level security when displaying the “Changes” table. If a field is restricted to a group,
users without that group will not see that field’s values in the log display.
```

## Default rules (what you may see out of the box)

The `spp_audit` module ships with a set of default rules to cover common OpenSPP flows (for example registry records,
programs/cycles, and service points). Implementations should review these defaults and adjust them to local requirements.

## Operational considerations

- **Performance and storage:** auditing increases database write volume and storage usage. Log only the fields you need.
- **Immutability:** audit logs are intended to be tamper-resistant. Deleting audit logs is blocked by default.
- **Retention:** if your deployment requires retention limits, implement them as a deliberate policy (database retention,
  archiving, or a dedicated retention mechanism), aligned with local regulations.

---
openspp:
  doc_status: draft
  products: [core]
---

# Audit configuration

This guide is for **implementers** configuring audit trails to track data changes, user actions, and file access for compliance and accountability.

## What you'll find here

- **{doc}`overview`** - Audit concepts, rules, action types, and field-level tracking
- **{doc}`backends`** - Storage backend configuration for audit logs

```{toctree}
:hidden:
:maxdepth: 1

overview
backends
```

## Quick start

1. Navigate to **Audit Rules** in the configuration menu
2. Create or review **Audit Rules** for each model you want to track
3. Enable the desired action types (Create, Update, Delete, Lifecycle, File Access)
4. Optionally configure **field-level tracking** for sensitive fields
5. Choose one or more **Audit Backends** for log storage

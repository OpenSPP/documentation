---
openspp:
  doc_status: draft
  products: [core]
---

# Audit configuration

This guide is for **implementers** configuring audit trails to track data changes, user actions, and file access for compliance and accountability.

## Prerequisites

```{important}
The `spp_audit` module must be installed. See {doc}`/get_started/modules/index` for module installation instructions.
```

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

1. From the main menu, click **Audit Log**
2. Click the **Audit** tab to display options
3. Create or review **Audit Rules** for each model you want to track
4. Enable the desired action types (Create, Update, Delete, Lifecycle, File Access)
5. Optionally configure **field-level tracking** for sensitive fields
6. Choose one or more **Audit Backends** for log storage

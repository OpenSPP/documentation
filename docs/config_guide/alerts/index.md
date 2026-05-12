---
openspp:
  doc_status: draft
  products: [core]
---

# Alerts

This guide is for **implementers** configuring threshold and deadline monitoring rules that automatically flag records needing attention.

## Prerequisites

```{important}
The `spp_alerts` module must be installed. See {doc}`/get_started/modules/index` for module installation instructions.
```

```{note}
Developer mode must be enabled. Log in as admin, go to **Settings > General Settings**, and activate developer mode first.
```

## What you'll find here

- **{doc}`overview`** - Alert concepts, rule types (threshold and date-based), priority levels, and evaluation

```{toctree}
:hidden:
:maxdepth: 1

overview
```

## Quick start

1. Go to **Settings > Technical**, scroll down to **Alerts**, then click **Alert Rules**
2. Click **New** to define a new alert rule
3. Select the **Model to Monitor** (e.g., Programs, Entitlements)
4. Choose the **Rule Type** (Threshold or Date/Deadline)
5. Configure the condition (field, operator, value) and set the **Priority**

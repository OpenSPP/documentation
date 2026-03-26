---
openspp:
  doc_status: draft
  products: [core]
---

# Approval workflows

This guide is for **implementers** configuring multi-tier approval processes for program operations, change requests, and other workflows.

## What you'll find here

- **{doc}`overview`** - Approval concepts, definition types, SLA, and notification settings
- **{doc}`tiers`** - Multi-tier sequencing, escalation, and conditional approval rules
- **{doc}`batch_approvals`** - Batch processing, freeze periods, and async configuration

```{toctree}
:hidden:
:maxdepth: 1

overview
tiers
batch_approvals
```

## Quick start

1. Navigate to **Configuration > Approval Definitions**
2. Click **Create** to define a new approval workflow
3. Select the **Model** the approval applies to (e.g., Change Requests, Cases)
4. Choose the **Approval Type** (Security Group, Specific Users, Manager of Submitter, or Dynamic Field)
5. Optionally add **Tiers** for multi-step approval chains

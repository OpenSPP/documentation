---
openspp:
  doc_status: draft
  products: [core]
---

# Change Request Types

**For: Implementers**

Change request types define the workflows for modifying registrant data. They control what changes can be requested, who can approve them, and how approved changes are applied to registrant records.

## What You'll Learn

This guide shows you how to configure change request types, create custom detail models, set up field mappings, and define security rules for your change management workflows.

```{toctree}
:maxdepth: 1

configure
```

## Quick Links

| Topic | When to Use |
|-------|-------------|
| {doc}`configure` | Create and configure change request types with detail models and field mappings |

## Prerequisites

Before configuring change request types, you should:

- Have **Studio** access in OpenSPP
- Understand your organization's change approval workflows
- Know what registrant fields users need to modify
- Have familiarity with Odoo models (for custom detail models)

## What's New in V2

OpenSPP V2 introduces a configuration-driven change request system:

- **Detail Models** - Real Odoo fields instead of JSON blobs for type safety
- **Field Mapping** - Declarative configuration for applying approved changes
- **Apply Strategies** - Flexible patterns for different change types
- **Studio Integration** - Visual configuration without Python code
- **Conflict Detection** - Automatic detection of overlapping pending changes
- **Audit Trail** - Complete history of all change requests and approvals

---

*This documentation covers OpenSPP V2 change request configuration for implementers.*

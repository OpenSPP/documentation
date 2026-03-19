---
openspp:
  doc_status: draft
  products: [core]
---

# Access control overview

This guide is for **implementers** understanding how OpenSPP manages access permissions through a three-tier architecture.

## Three-tier architecture

OpenSPP uses a layered approach to access control:

```
Roles → Privileges → Groups → Permissions
```

| Layer | What it does | Example |
|-------|--------------|---------|
| **Roles** | Assigned to users, bundles multiple groups | "Global Registrar" role |
| **Privileges** | Organizes groups in Settings UI (Odoo 19) | "Registry" privilege section |
| **Groups** | Grants specific permissions via ACLs and record rules | `spp_registry.group_registry_officer` |

### Roles

Roles are the primary way to manage user access. Each role:

- Has a **name** and optional description
- Contains one or more **implied groups** that grant permissions
- Can be **global** (system-wide access) or **local** (area-restricted)
- Is assigned to users via **role lines** (optionally time-bounded)

When you assign a role to a user, all groups implied by that role are automatically applied.

### Groups

Groups define actual permissions through:

- **Access Control Lists (ACLs)** - Create, read, update, delete permissions per model
- **Record rules** - Domain-based restrictions on which records a user can access

### Privileges

Privileges (Odoo 19 feature) organize how groups appear in the Settings UI. They control the visual presentation of access rights but don't affect the underlying permission logic.

## Global vs local roles

OpenSPP distinguishes between two types of roles:

| Role type | Description | Area assignment |
|-----------|-------------|-----------------|
| **Global** | Access to all records system-wide | Cannot have areas assigned |
| **Local** | Access restricted to assigned areas | Must have at least one area |

### How local roles work

1. A role is defined as `local` in its configuration
2. When assigning to a user, you select one or more **Center Areas**
3. Record rules filter data based on the user's assigned areas
4. The user only sees records associated with their areas

### Constraints

The system enforces these rules:

| Situation | Result |
|-----------|--------|
| Local role without areas | Error: "Local roles must have at least one area assigned" |
| Global role with areas | Error: "Global roles cannot have areas assigned" |

## How roles are applied

When a user logs in:

1. System checks all role lines assigned to the user
2. For each role line, verifies if it's enabled (based on date range)
3. Collects all implied groups from enabled roles
4. Applies the union of all permissions from those groups

### Enabled status

The **Enabled** field on role lines is computed automatically from the date range:

| Dates | Enabled? |
|-------|----------|
| No From/To dates | Yes |
| Today is after From date | Yes |
| Today is before From date | No |
| Today is after To date | No |

You cannot manually toggle the Enabled field - it's calculated from the From/To dates.

## Role management banner

If the Roles module is installed, OpenSPP displays a banner on user forms indicating that "access rights are managed by roles."

```{note}
When roles are active, changes made directly in the user's "Access Rights" tab are not persistent. The system overwrites them based on role assignments.
```

## See also

- {doc}`assigning_roles` - Step-by-step role assignment
- {doc}`predefined_roles` - List of default roles
- {doc}`/tutorial/user_guides/administrating_role_based_access` - Illustrated tutorial

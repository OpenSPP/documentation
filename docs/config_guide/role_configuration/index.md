---
openspp:
  doc_status: draft
  products: [core]
---

# Role configuration

This guide is for **implementers** configuring role-based access in OpenSPP: assigning roles to users, understanding global vs local roles, and managing access permissions.

## What you'll find here

- **{doc}`overview`** - Three-tier access control architecture (roles, privileges, groups)
- **{doc}`assigning_roles`** - Assign roles to users with optional time bounds and area scoping
- **{doc}`predefined_roles`** - Reference list of 9 default roles included with OpenSPP
- **{doc}`creating_roles`** - Create custom roles for your program needs
- **{doc}`troubleshooting`** - Common issues and solutions

```{toctree}
:hidden:
:maxdepth: 1

overview
assigning_roles
predefined_roles
creating_roles
troubleshooting
```

## Quick start

To configure role-based access:

1. Navigate to **Settings → Users & Companies → Users**
2. Create or select a user
3. Go to the **Roles** tab
4. Add role lines with optional date bounds
5. For local roles, assign **Center Areas** to restrict data access

For a fully illustrated walkthrough with step-by-step screenshots, see {doc}`/tutorial/user_guides/administrating_role_based_access`.

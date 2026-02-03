---
openspp:
  doc_status: unverified
  products: [core]
---

# Access management

OpenSPP uses Odoo 19’s access control framework (users, groups, record rules) and adds an opinionated, role-based way to assign permissions.

## How access control works in OpenSPP

In day-to-day operations, you typically manage access through **roles**, not by directly ticking groups on the user’s “Access Rights” tab:

- **Roles** are assigned to users (optionally time-bounded). A role implies one or more groups.
- **Groups** grant permissions through access control lists (ACLs) and record rules.
- **Privileges** (Odoo 19) organize which groups appear in the Settings UI and how they are presented to administrators.

```{note}
If your deployment includes the Roles feature, OpenSPP shows a banner on the user form indicating that “access rights are managed by roles”. In that setup, changes made directly in the user’s “Access Rights” tab are not persistent.
```

## Common admin workflows

For a fully illustrated walkthrough (including screenshots), see {doc}`user_guides/administrating_role_based_access`. For implementer-focused role configuration, see {doc}`/config_guide/role_configuration/index`.

### Create a user

1. Go to **Settings → Users & Companies → Users** and click **Create**.
2. Fill in name and email/login, then **Save**.

```{note}
Screenshot needed: User creation form (Odoo 19 + OpenSPP).
```

### Assign roles (recommended)

1. Open the user record.
2. Go to the **Roles** tab.
3. Add one or more role lines:
   - **Role**: the access role to grant
   - **From / To** (optional): time-bound access
   - **Enabled**: computed status based on date range

```{note}
Screenshot needed: Roles tab on the user form showing one enabled role line.
```

### Restrict access to an area (local roles)

If the Areas module is installed, roles can be assigned as **local** and scoped to one or more **Center Areas**.

- For a **local** role line, select a **Center Area** on the role line.
- OpenSPP computes the user’s “Center Areas” based on local role assignments.
- Record rules in domain modules can use the user’s center areas to restrict which records are visible.

```{note}
Screenshot needed: Role line with a selected Center Area, and the computed Center Areas field on the user.
```

### Remove or suspend access

- To temporarily remove access, **Archive** the user (or disable specific role lines).
- To end time-bound access, set the role line’s **To** date.
- To permanently remove permissions, remove role lines and save.

## Troubleshooting

### Menus don’t show up after changing roles

Odoo caches menu visibility at login. If you change roles/groups for a user who is already logged in, ask them to **log out and log back in** to refresh the menus.

## Advanced: creating custom roles

You can create new roles that combine multiple groups:

1. Go to **Settings → Users & Companies → Roles**.
2. Create a role and add the implied groups it should grant.
3. Assign the role to users on the user form.

```{note}
For long-term maintainability, prefer implementing new privileges/groups/roles in an OpenSPP module (XML/CSV) rather than changing core security definitions from the UI.
```

## For implementers and developers

See {doc}`../technical_reference/access_rights` for:

- the OpenSPP access rights architecture (roles, privileges, groups)
- record rule patterns and anti-patterns
- the access-control compliance checker (security “linter”) used in CI and locally

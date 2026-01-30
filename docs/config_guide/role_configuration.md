---
openspp:
  doc_status: draft
  products: [core]
---

# Role configuration

This page is for **implementers** configuring role-based access in OpenSPP: assigning roles to users, using privileges and groups, and optionally scoping roles by area.

For a fully illustrated walkthrough (including step-by-step screenshots), see {doc}`/tutorial/user_guides/administrating_role_based_access`.

## How access control works in OpenSPP

In day-to-day operations, you typically manage access through **roles**, not by directly ticking groups on the user's "Access Rights" tab:

- **Roles** are assigned to users (optionally time-bounded). A role implies one or more groups.
- **Groups** grant permissions through access control lists (ACLs) and record rules.
- **Privileges** (Odoo 19) organize which groups appear in the Settings UI and how they are presented to administrators.

```{note}
If your deployment includes the Roles feature, OpenSPP shows a banner on the user form indicating that "access rights are managed by roles". In that setup, changes made directly in the user's "Access Rights" tab are not persistent.
```

## Configuration workflows

### Create a user

1. Go to **Settings → Users & Companies → Users** and click **Create**.
2. Fill in name and email/login, then **Save**.

![User creation form](/_images/en-us/config-guide/role-configuration/01-user-creation-form.png)

### Assign roles (recommended)

1. Open the user record.
2. Go to the **Roles** tab.
3. Add one or more role lines:
   - **Role**: the access role to grant
   - **From / To** (optional): time-bound access
   - **Enabled**: turn the role on/off

![Roles tab on the user form with one enabled role line](/_images/en-us/config-guide/role-configuration/02-roles-tab-with-role-line.png)

### Restrict access to an area (local roles)

If the Areas module is installed, roles can be assigned as **local** and scoped to one or more **Center Areas**.

- For a **local** role line, select a **Center Area** on the role line.
- OpenSPP computes the user's "Center Areas" based on local role assignments.
- Record rules in domain modules can use the user's center areas to restrict which records are visible.

![Role line with a selected Center Area and the computed Center Areas field on the user](/_images/en-us/config-guide/role-configuration/03-local-role-center-area.png)

### Remove or suspend access

- To temporarily remove access, **Archive** the user (or disable specific role lines).
- To end time-bound access, set the role line's **To** date.
- To permanently remove permissions, remove role lines and save.

## Troubleshooting

### Menus don't show up after changing roles

Odoo caches menu visibility at login. If you change roles/groups for a user who is already logged in, ask them to **log out and log back in** to refresh the menus.

## Advanced: creating custom roles

You can create new roles that combine multiple groups:

1. Go to **Settings → Users & Companies → Roles**.
2. Create a role and add the implied groups it should grant.
3. Assign the role to users on the user form.

![Settings → Users & Companies → Roles for custom role configuration](/_images/en-us/config-guide/role-configuration/04-custom-roles-settings.png)

```{note}
For long-term maintainability, prefer implementing new privileges/groups/roles in an OpenSPP module (XML/CSV) rather than changing core security definitions from the UI.
```

## For implementers and developers

See {doc}`/tutorial/access_management` for a concise overview of access management. For architecture details (roles, privileges, groups, record rules, and the access-control compliance checker), refer to your project's technical reference or OpenSPP module documentation.

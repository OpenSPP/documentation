---
openspp:
  doc_status: draft
  products: [core]
---

# Creating custom roles

This guide is for **implementers** creating custom roles when the predefined roles don't meet program requirements.

## When to create custom roles

Create custom roles when:

- Predefined roles don't match your organizational structure
- You need to combine permissions from multiple existing roles
- You want finer-grained access control for specific functions
- Your program has unique access patterns

## Navigate to roles

Go to **Settings → Users & Companies → Roles**.

## Creating a role

### Step 1: Create new role

Click **New** to create a role.

### Step 2: Configure basic information

| Field | Value | Notes |
|-------|-------|-------|
| Name | Case Manager | Descriptive name |
| Role Type | Global or Local | See below for guidance |

**Role Type guidelines:**

| Choose | When |
|--------|------|
| **Global** | Users need access across all geographic areas |
| **Local** | Users should only see data from specific areas |

### Step 3: Add implied groups

In the **Groups** tab, add the groups this role should grant:

1. Click **Add a line**
2. Search for and select a group
3. Repeat for all needed groups

**Common groups to include:**

| Group | Purpose |
|-------|---------|
| `base.group_user` | Required - basic internal user access |
| `spp_registry.group_registry_viewer` | Read registry data |
| `spp_registry.group_registry_officer` | Edit registry data |
| `spp_programs.group_program_viewer` | View program data |
| `spp_programs.group_program_officer` | Edit program data |

### Step 4: Add description (optional)

In the **Internal Notes** tab, document:

- The purpose of this role
- Which job functions should receive it
- Any special considerations

### Step 5: Save the role

Click **Save**. The role is now available for assignment.

## Example: Creating a case manager role

**Scenario:** Case managers need to view registrants and manage their cases, but shouldn't modify registry data.

| Field | Value |
|-------|-------|
| Name | Case Manager |
| Role Type | Local |
| Implied Groups | `base.group_user`, `spp_registry.group_registry_viewer`, `spp_case_management.group_case_manager` |

## Viewing role permissions

After creating a role, verify its effective permissions:

1. Open the role record
2. Click the **Access Rights** stat button to see ACL permissions
3. Click the **Record Rules** stat button to see domain restrictions
4. Review that the combined permissions match your requirements

## Updating users after role changes

When you modify a role's implied groups, existing users with that role need to be updated.

### Automatic update

Click the **Update User Roles** button on the role form to immediately apply changes to all users with this role.

### Scheduled update

A scheduled job periodically synchronizes role changes. For immediate effect, use the manual update button.

## Best practices

### Naming conventions

Use clear, descriptive names:

| Good | Bad |
|------|-----|
| Regional Enrollment Officer | Role1 |
| Area Finance Coordinator | Custom Role |
| Field Data Collector | New Role |

### Start minimal

Begin with the minimum required groups and add more as needed. It's easier to grant additional permissions than to revoke excessive ones.

### Document roles

Always add notes explaining:
- Why the role exists
- What job functions use it
- Any dependencies or considerations

### Use local when possible

Prefer local roles for field staff to enforce area-based data isolation. This:
- Reduces risk of unauthorized data access
- Improves performance (fewer records to load)
- Supports data governance requirements

### Consider module-based roles

If using specific OpenSPP modules, create roles aligned with module functionality:

| Module | Example role |
|--------|--------------|
| `spp_programs` | Program Enrollment Officer |
| `spp_change_request_v2` | Change Request Reviewer |
| `spp_grievance` | Grievance Handler |

## Long-term maintenance

```{note}
For production deployments, implement roles in an OpenSPP module (XML/CSV) rather than creating them through the UI. This ensures:
- Roles are version-controlled
- Changes are tracked in code
- Deployments are reproducible
- Roles can be tested before deployment
```

## Are you stuck?

**Can't find the groups I need?**

Groups are defined by OpenSPP modules. If a group doesn't exist, the related module may not be installed.

**Role changes not affecting users?**

Click the **Update User Roles** button on the role form to manually sync changes.

**User still has old permissions after role change?**

The user must log out and back in for menu visibility to update. Permission changes apply immediately, but the UI caches menus at login.

## See also

- {doc}`overview` - Understanding the role architecture
- {doc}`predefined_roles` - Default roles for reference
- {doc}`assigning_roles` - How to assign created roles

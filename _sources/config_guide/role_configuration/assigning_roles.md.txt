---
openspp:
  doc_status: draft
  products: [core]
---

# Assigning roles to users

This guide is for **implementers** assigning roles to users in OpenSPP.

## Navigate to users

Go to **Settings → Users & Companies → Users**.

## Creating a user

### Step 1: Create new user

Click **New** to create a new user record.

### Step 2: Configure basic information

| Field | Value | Notes |
|-------|-------|-------|
| Name | Maria Santos | User's display name |
| Email | maria@agency.gov | Used for login and notifications |

### Step 3: Save the user

Click **Save** before assigning roles.

## Assigning roles

### Step 1: Open the Roles tab

On the user form, click the **Roles** tab.

### Step 2: Add a role line

Click **Add a line** to create a new role assignment.

| Field | Description |
|-------|-------------|
| Role | Select the role to assign |
| Center Areas | For local roles only - select one or more areas |
| From | Optional start date |
| To | Optional end date |
| Enabled | Computed - shows if role is currently active |

### Step 3: Configure time bounds (optional)

| Field | Effect |
|-------|--------|
| **From** (blank) | Role active immediately |
| **From** (future date) | Role activates on that date |
| **To** (blank) | Role never expires |
| **To** (date) | Role deactivates after that date |

```{note}
The **Enabled** field is computed automatically from the date range. You cannot manually toggle it.
```

### Step 4: Assign center areas (local roles only)

For **local** roles, the Center Areas field is required:

1. The Center Areas field appears only for local role types
2. Select one or more areas from the dropdown
3. The user will only see records associated with these areas

For **global** roles, the Center Areas field is hidden and cannot be set.

### Step 5: Save

Click **Save** to apply the role assignment. The user's permissions update automatically.

## Assigning multiple roles

Users can have multiple roles simultaneously:

1. Add multiple role lines on the Roles tab
2. Permissions are cumulative (union of all role permissions)
3. If any role grants a permission, the user has that permission

**Example:**

| Role | Permissions |
|------|-------------|
| Global Registrar | Registry read/write |
| Global Finance | Finance read |
| **Combined** | Registry read/write + Finance read |

## Removing or suspending access

### Remove a role

1. Open the user record
2. Go to the Roles tab
3. Delete the role line
4. Save

### Suspend access temporarily

**Option 1: Set end date**
1. Edit the role line
2. Set the **To** date to yesterday
3. Role becomes disabled

**Option 2: Archive the user**
1. Open the user record
2. Click **Action → Archive**
3. All access suspended

### End time-bound access

If a role has a **To** date, it automatically deactivates when that date passes. No action needed.

## Verifying role assignments

After assigning roles, verify the user has correct access:

1. Ask the user to **log out and log back in** (menus are cached at login)
2. Check that expected menus are visible
3. Verify they can access appropriate records

## Are you stuck?

**User doesn't see expected menus?**

Menus are cached at login. The user must log out and log back in after role changes.

**Can't assign areas to a role?**

Check if the role type is **local**. Global roles cannot have areas assigned.

**Getting "must have at least one area" error?**

Local roles require at least one Center Area. Either assign areas or use the global version of the role.

**User has more permissions than expected?**

Permissions are cumulative across all assigned roles. Check all role lines, not just one.

## See also

- {doc}`overview` - Understanding the three-tier architecture
- {doc}`predefined_roles` - List of available roles
- {doc}`troubleshooting` - Common issues

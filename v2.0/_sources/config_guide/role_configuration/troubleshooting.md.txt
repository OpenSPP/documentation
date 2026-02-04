---
openspp:
  doc_status: draft
  products: [core]
---

# Troubleshooting

This guide helps **implementers** resolve common role configuration issues.

## Menu and UI issues

### Menus don't show up after changing roles

**Cause:** Odoo caches menu visibility at login time.

**Solution:** Ask the user to log out and log back in. Menu changes only take effect after a fresh login.

### User sees empty list views

**Cause:** User has permission to access the menu but record rules filter out all records.

**Check:**
1. Verify the user's role includes the correct groups
2. For local roles, verify Center Areas are assigned
3. Check that records exist in the user's assigned areas

### Access denied errors

**Cause:** User's role doesn't include required groups.

**Solution:**
1. Identify which model the user is trying to access (check error message)
2. Find which group grants access to that model
3. Add that group to the user's role

## Role assignment issues

### Can't assign areas to a role

**Cause:** The role is configured as **global**.

**Solution:** Global roles cannot have areas. Either:
- Use a local version of the role
- Create a new local role with the same groups

### Error: "Local roles must have at least one area assigned"

**Cause:** Trying to assign a local role without selecting areas.

**Solution:** Select at least one Center Area when assigning a local role.

### Error: "Global roles cannot have areas assigned"

**Cause:** Trying to assign areas to a global role.

**Solution:** Remove the area selection. Global roles apply system-wide.

### Role line shows as disabled

**Cause:** The role's date range makes it inactive.

**Check:**
- Is **From** date in the future? Role isn't active yet.
- Is **To** date in the past? Role has expired.

**Solution:** Adjust the From/To dates or remove them for permanent access.

## Permission issues

### User has more permissions than expected

**Cause:** Permissions are cumulative across all assigned roles.

**Check:** Review all role lines on the user's Roles tab. The user gets the union of all permissions.

**Solution:** Remove roles that grant unwanted permissions.

### User missing permissions

**Cause:** Role doesn't include all required groups.

**Check:**
1. Open the role definition
2. Review the Groups tab
3. Click Access Rights button to see effective permissions

**Solution:** Add missing groups to the role.

### Changes to Access Rights tab don't persist

**Cause:** When roles are active, the system overwrites Access Rights based on role assignments.

**Solution:** Don't modify the Access Rights tab directly. Instead:
1. Create or modify a role
2. Assign the role to the user
3. Changes persist through role assignments

## Local role issues

### Local user sees all records instead of filtered

**Cause:** Record rules may not be configured for the relevant models.

**Check:**
1. Verify the role is type **local**
2. Verify Center Areas are assigned
3. Check that record rules exist for the models in question

**Solution:** Record rules must be defined in the module to filter by user's center areas. Contact your developer if rules are missing.

### User can't see records in their assigned area

**Cause:** Records may not be associated with the user's area.

**Check:**
1. Open a record the user should see
2. Verify it has an area assignment that matches the user's Center Areas

**Solution:** Either:
- Assign the record to the user's area
- Add the record's area to the user's Center Areas

## Role synchronization issues

### Role changes not applying to existing users

**Cause:** Role-to-user synchronization may be delayed.

**Solution:**
1. Open the role definition
2. Click the **Update User Roles** button
3. This forces immediate synchronization

### Scheduled job not running

**Cause:** The cron job for role updates may be disabled.

**Check:** Go to **Settings → Technical → Scheduled Actions** and search for role update jobs.

**Solution:** Enable and run the scheduled action.

## Diagnostic checklist

When troubleshooting access issues, check in order:

1. **User exists and is active**
   - User not archived?
   - User can log in?

2. **Role is assigned**
   - Role line exists on Roles tab?
   - Role line is enabled (dates valid)?

3. **Role is configured correctly**
   - Role has correct type (global/local)?
   - Role includes required groups?

4. **Areas are assigned (for local roles)**
   - Center Areas selected on role line?
   - Records exist in those areas?

5. **User has logged in fresh**
   - Logged out and back in after changes?

## Getting help

If issues persist after checking this guide:

1. Document the exact error message
2. Note which user, role, and action caused the issue
3. Check the server logs for detailed error information
4. Contact your system administrator or OpenSPP support

## See also

- {doc}`overview` - Understanding how access control works
- {doc}`assigning_roles` - Correct role assignment procedures
- {doc}`/tutorial/user_guides/administrating_role_based_access` - Illustrated tutorial

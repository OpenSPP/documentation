---
openspp:
  doc_status: draft
---

# CR Types - Advanced

**Module:** `spp_cr_types_advanced`

## Overview

This module is for **implementers** who need to understand available change request types, and **developers** who need to extend or customize complex registry operations.

CR Types - Advanced provides pre-built change request types that require custom Python logic for complex registry operations. These types handle membership changes, registrant lifecycle events, group operations, and data quality tasks that cannot be implemented through Studio configuration alone.

{note}
These types have `is_studio_editable=False` by design. If you need to modify their behavior, see the [Extending Advanced Types](#extending-advanced-types) section.

## Module Dependencies

| Dependency | Purpose |
|------------|---------|
| `spp_change_request_v2` | Base change request infrastructure |

## Available Change Request Types

### Membership Operations

| Type | Code | Target | Description |
|------|------|--------|-------------|
| Add Group Member | `add_member` | Group | Add a new member to an existing group/household |
| Remove Group Member | `remove_member` | Group | Remove a member from a group |
| Change Head of Household | `change_hoh` | Group | Reassign head of household role |
| Transfer Member | `transfer_member` | Group | Move member from one group to another |

### Registrant Lifecycle

| Type | Code | Target | Description |
|------|------|--------|-------------|
| Exit Registrant | `exit_registrant` | Both | Deactivate or exit a registrant from the system |

### Group Operations

| Type | Code | Target | Description |
|------|------|--------|-------------|
| Create New Group | `create_group` | Group | Create a new group/household |
| Split Household | `split_household` | Group | Split a household into two separate groups |

### Data Quality

| Type | Code | Target | Description |
|------|------|--------|-------------|
| Merge Registrants | `merge_registrants` | Both | Merge duplicate registrant records |

## Type Properties

All advanced types share these characteristics:

| Property | Value | Description |
|----------|-------|-------------|
| `is_studio_editable` | False | Cannot be modified via Studio |
| `is_studio_cloneable` | False | Cannot be duplicated via Studio |
| `is_system_type` | True | System-managed type |
| `apply_strategy` | custom | Uses custom Python apply model |

## How Each Type Works

Each type follows a three-component pattern:

1. **Detail Model** - Captures request-specific data (e.g., `spp.cr.detail.add_member`)
2. **Detail Form View** - UI for entering request details
3. **Apply Model** - Custom Python logic to execute the change (e.g., `spp.cr.apply.add_member`)

### Add Group Member

Use when adding a new individual to an existing household or group.

**Details captured:**

- New member information (name, birth date, gender)
- Role in the group (Head, Spouse, Child, Other)
- Relationship to head of household

**On approval:**

- Creates new individual in registry
- Creates membership linking individual to group
- Sets appropriate role

### Remove Group Member

Use when a member needs to be removed from a group (death, departure, etc.).

**Details captured:**

- Member to remove
- End date
- Reason for removal

**On approval:**

- Ends membership record
- Optionally deactivates individual

### Change Head of Household

Use when the head of household needs to change (death, divorce, new designation).

**Details captured:**

- Current head
- New head (must be existing member)
- Effective date
- Reason for change

**On approval:**

- Updates membership roles
- Transfers head role to new member

### Transfer Member

Use when a member is moving from one household to another.

**Details captured:**

- Member to transfer
- Source group
- Destination group
- New role in destination
- Transfer date

**On approval:**

- Ends membership in source group
- Creates membership in destination group

### Exit Registrant

Use when a registrant (individual or group) needs to be deactivated.

**Details captured:**

- Registrant to exit
- Exit date
- Exit reason
- Cascading options (for groups)

**On approval:**

- Deactivates registrant
- Ends all active memberships
- Updates related records

### Create New Group

Use when creating a new household or group.

**Details captured:**

- Group name/identifier
- Group type
- Initial head of household (optional)
- Location/area

**On approval:**

- Creates new group registrant
- Optionally creates head of household membership

### Split Household

Use when a household needs to be divided (divorce, adult children moving out).

**Details captured:**

- Original household
- Members for new household
- New household head
- Split date

**On approval:**

- Creates new group
- Transfers selected members
- Maintains original group with remaining members

### Merge Registrants

Use when duplicate records need to be consolidated.

**Details captured:**

- Primary record (to keep)
- Secondary record(s) (to merge)
- Field conflict resolution

**On approval:**

- Merges data from secondary to primary
- Transfers memberships and relationships
- Archives secondary records

## Extending Advanced Types

To modify the behavior of an advanced type, create a custom module that inherits from the apply model:

```python
# my_custom_module/models/custom_add_member.py

from odoo import models


class CustomAddMember(models.Model):
    _inherit = "spp.cr.apply.add_member"

    def _apply(self, change_request):
        """Override to add custom logic."""
        # Call original implementation
        result = super()._apply(change_request)

        # Add custom post-processing
        # e.g., send notification, update external system

        return result
```

## Technical Details

| Property | Value |
|----------|-------|
| Technical Name | `spp_cr_types_advanced` |
| Category | OpenSPP |
| Version | 19.0.1.0.0 |
| License | LGPL-3 |
| Development Status | Beta |

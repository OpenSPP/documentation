---
openspp:
  doc_status: draft
  products: [core]
---

# Apply strategies

The apply strategy determines what happens when an approved change request is applied. This reference covers the two strategy types (field mapping and custom), the base class contract, and patterns from the built-in strategies.

If you have not built a CR type before, start with the {doc}`tutorial`.

## Field mapping vs. custom

Choose the strategy type based on what the apply action needs to do:

| Use field mapping when... | Use a custom strategy when... |
|---------------------------|-------------------------------|
| Copying field values from the detail to the registrant | Creating or deleting records |
| Renaming fields (e.g., `postal_code` → `zip`) | Updating multiple models in one operation |
| Applying expression-based transforms | Changing relationships (memberships, roles) |
| Clearing registrant fields | Changing record status (active/inactive) |
| | Merging or splitting records |
| | Any logic beyond field-to-field copying |

**Field mapping** is configured entirely in XML — no Python required. See {doc}`/config_guide/change_request_types/field_mappings` for the configuration guide.

**Custom strategies** require a Python class. The rest of this page covers how to build them.

## Base class contract

All custom strategies inherit from `spp.cr.strategy.base`, which defines three methods:

```python
class SPPCRStrategyBase(models.AbstractModel):
    _name = "spp.cr.strategy.base"

    def apply(self, change_request):
        """Apply the change request. Required.

        Args:
            change_request: The spp.change.request record

        Returns:
            True on success

        Raises:
            UserError: If apply fails
        """
        raise NotImplementedError("Subclasses must implement apply()")

    def preview(self, change_request):
        """Preview what changes will be applied. Optional.

        Returns:
            dict describing planned changes
        """
        return {}

    def validate(self, change_request):
        """Custom validation before apply. Optional.

        Raises:
            ValidationError: If validation fails
        """
        pass
```

Only `apply()` is required. The framework calls these methods in order: `validate()` → `apply()`, with `preview()` called separately when a reviewer requests a preview.

## Anatomy of a custom strategy

Every custom strategy follows the same structure. Here is the `add_member` strategy, which creates a new individual and adds them to a group:

```python
import logging
from odoo import Command, _, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class SPPCRApplyAddMember(models.AbstractModel):
    _name = "spp.cr.apply.add_member"
    _inherit = "spp.cr.strategy.base"
    _description = "CR Apply: Add Group Member"

    def apply(self, change_request):
        # 1. Get the registrant and detail record
        group = change_request.registrant_id
        detail = change_request.get_detail()

        # 2. Validate preconditions
        if not group.is_group:
            raise UserError(_("Registrant must be a group."))
        if not detail:
            raise UserError(_("No detail record found."))
        if not detail.member_name:
            raise UserError(_("Member name is required."))

        # 3. Execute changes
        individual_vals = {
            "name": detail.member_name,
            "given_name": detail.given_name,
            "family_name": detail.family_name,
            "birthdate": detail.birthdate,
            "is_registrant": True,
            "is_group": False,
        }
        if detail.gender_id:
            individual_vals["gender_id"] = detail.gender_id.id

        individual = self.env["res.partner"].create(individual_vals)

        membership_vals = {
            "group": group.id,
            "individual": individual.id,
            "start_date": fields.Datetime.now(),
        }
        if detail.relationship_id:
            membership_vals["membership_type_ids"] = [
                Command.link(detail.relationship_id.id)
            ]
        self.env["spp.group.membership"].create(membership_vals)

        # 4. Store results on the detail record
        detail.write({"created_individual_id": individual.id})

        # 5. Log the operation
        _logger.info(
            "Added member partner_id=%s to group partner_id=%s via CR %s",
            individual.id, group.id, change_request.name,
        )

        return True
```

### The five-step pattern

1. **Get registrant and detail** — `change_request.registrant_id` and `change_request.get_detail()`
2. **Validate preconditions** — check everything before making changes; raise `UserError` on failure
3. **Execute changes** — create, update, or delete records as needed
4. **Store results** — write back to the detail record (e.g., `created_individual_id`) so the UI can display what was created
5. **Log** — use `_logger.info()` for audit trail in the server log

```{warning}
Strategies run with `sudo()`. The CR framework calls `strategy.apply()` with full system privileges. This is by design: the approval workflow is the security gate, not the strategy. Do not add permission checks inside your strategy — they would be redundant and could prevent legitimate applies.
```

## Preview pattern

The `preview()` method returns a dict that the CR UI displays to reviewers. Include an `_action` key to identify the type of change, and human-readable values for the rest:

```python
def preview(self, change_request):
    detail = change_request.get_detail()
    if not detail:
        return {}

    return {
        "_action": "add_member",
        "member_name": detail.member_name,
        "group": change_request.registrant_id.name,
        "relationship": (
            detail.relationship_id.display
            if detail.relationship_id else None
        ),
    }
```

For the field mapping strategy, `preview()` automatically computes a diff of old vs. new values for each mapped field.

## Registering a strategy

In your module's XML data, the CR type record connects the strategy to the detail model:

```xml
<record id="cr_type_add_member" model="spp.change.request.type">
    <field name="name">Add Group Member</field>
    <field name="code">add_member</field>
    <field name="detail_model">spp.cr.detail.add_member</field>
    <field name="apply_strategy">custom</field>
    <field name="apply_model">spp.cr.apply.add_member</field>
    <!-- ... other fields ... -->
</record>
```

The two key fields:
- **`apply_strategy`** — set to `custom` to use a Python strategy class (or `field_mapping` for configuration-only)
- **`apply_model`** — the `_name` of your `AbstractModel` strategy class

## Built-in strategies by pattern

The built-in strategies fall into four categories:

### Field copy (no custom code)

| Strategy | CR type | What it does |
|----------|---------|--------------|
| `spp.cr.strategy.field_mapping` | edit_individual, edit_group | Copies mapped fields from detail to registrant, with optional expression transforms |

### Record creation

| Strategy | CR type | What it does |
|----------|---------|--------------|
| `spp.cr.apply.add_member` | add_member | Creates individual + group membership |
| `spp.cr.apply.create_group` | create_group | Creates a new group registrant |
| `spp.cr.apply.update_id` | update_id | Creates or updates DMS document records |

### Relationship changes

| Strategy | CR type | What it does |
|----------|---------|--------------|
| `spp.cr.apply.transfer_member` | transfer_member | Ends source membership, creates target membership |
| `spp.cr.apply.remove_member` | remove_member | Ends a group membership |
| `spp.cr.apply.change_hoh` | change_hoh | Swaps the "head" membership type between two individuals |

### Status and complex operations

| Strategy | CR type | What it does |
|----------|---------|--------------|
| `spp.cr.apply.exit_registrant` | exit_registrant | Deactivates a registrant record |
| `spp.cr.apply.merge_registrants` | merge_registrants | Consolidates two registrant records into one |
| `spp.cr.apply.split_household` | split_household | Splits a group into two groups, moving selected members |

### Manual (no-op)

The `manual` apply strategy does nothing — the administrator must apply changes manually outside the system. Use this for CR types that track requests without automated application.

---
openspp:
  doc_status: draft
  products: [core]
---

# Detail models

This reference covers the base class API, field patterns, and validation techniques for CR detail models. If you have not built a CR type before, start with the {doc}`tutorial`.

## Base class: `spp.cr.detail.base`

Every detail model inherits from `spp.cr.detail.base`. This abstract model provides the link to the parent change request and convenience methods for navigating the CR workflow.

### Fields provided by the base class

| Field | Type | Description |
|-------|------|-------------|
| `change_request_id` | Many2one | Link to the parent `spp.change.request` (cascade delete) |
| `registrant_id` | Many2one | Related field — the CR's registrant (`res.partner`) |
| `approval_state` | Selection | Related field — the CR's approval state (draft, pending, approved, revision, rejected) |
| `stage` | Selection | Related field — the CR's current stage (details, documents, review) |
| `is_applied` | Boolean | Related field — whether the CR has been applied |
| `is_cr_manager` | Boolean | Computed — whether the current user has CR manager permissions |
| `use_dynamic_approval` | Boolean | Related field — whether the CR type uses dynamic (field-based) approval routing |
| `field_to_modify` | Selection | Selection of which detail field the user is modifying (used with dynamic approval). Override `_get_field_to_modify_selection()` to narrow the options. |

Do not shadow these fields in your subclass — they're `related` fields backed by the parent CR, and redefining them breaks the sync.

### Methods provided by the base class

| Method | What it does |
|--------|--------------|
| `action_proceed_to_cr()` | Navigate from the detail form to the parent CR form |
| `action_next_documents()` | Advance the CR stage to "documents" |
| `action_skip_to_review()` | Advance the CR stage to "review" |
| `action_save_and_go_to_list()` | Save the CR and return to the CR list view |
| `action_submit_for_approval()` | Delegate to the parent CR's submission action (usable from detail form buttons) |
| `action_approve()` | Delegate to the parent CR's approve action |
| `action_reject()` | Delegate to the parent CR's reject action |
| `action_request_revision()` | Delegate to the parent CR's request-revision action |
| `prefill_from_registrant()` | Copy current registrant values into detail fields using `_get_prefill_mapping()` |
| `_get_prefill_mapping()` | Override to define which detail fields get pre-filled from the registrant (see [Pre-filling from the registrant](#pre-filling-from-the-registrant)) |
| `_get_field_to_modify_selection()` | Override for dynamic approval — return the list of field names the user can modify |

You do not need to implement these methods — they are inherited. The form view buttons in the {doc}`tutorial` call them directly.

```{note}
`action_proceed_to_cr()`, `action_next_documents()`, and `action_skip_to_review()` raise `UserError("No proposed changes detected")` if the detail record has no modified fields yet (i.e., `change_request_id.has_proposed_changes` is False). Make sure the user has entered something before these actions fire.
```

## Field patterns

### Simple fields

For CR types that edit basic registrant information, use standard Odoo field types. The `edit_individual` detail model is the simplest example:

```python
class SPPCRDetailEditIndividual(models.Model):
    _name = "spp.cr.detail.edit_individual"
    _inherit = ["spp.cr.detail.base", "mail.thread"]

    given_name = fields.Char(string="Given Name", tracking=True)
    family_name = fields.Char(string="Family Name", tracking=True)
    birthdate = fields.Date(string="Date of Birth", tracking=True)
    phone = fields.Char(string="Phone Number", tracking=True)
    email = fields.Char(string="Email", tracking=True)
```

This model uses the `field_mapping` apply strategy — no custom strategy code needed. The field mappings are defined in XML data records that map each detail field to the corresponding registrant field (e.g., `given_name` → `given_name`, `postal_code` → `zip`).

### Vocabulary references

OpenSPP uses `spp.vocabulary.code` for controlled vocabularies (gender, relationship types, document types). Reference them with a Many2one field and a domain that filters by the vocabulary's namespace URI:

```python
gender_id = fields.Many2one(
    "spp.vocabulary.code",
    string="Gender",
    domain="[('vocabulary_id.namespace_uri', '=', 'urn:iso:std:iso:5218')]",
    tracking=True,
)

relationship_id = fields.Many2one(
    "spp.vocabulary.code",
    string="Relationship to Head",
    domain="[('vocabulary_id.namespace_uri', '=',"
    " 'urn:openspp:vocab:group-membership-type'),"
    " ('code', '!=', 'head')]",
    tracking=True,
)
```

In the form view, add `options="{'no_create': True, 'no_open': True}"` to prevent users from creating or editing vocabulary codes inline.

### Computed and dynamic fields

Use computed fields to provide dynamic behavior in the form. The `transfer_member` detail model computes the list of available individuals based on the source group:

```python
available_individual_ids = fields.Many2many(
    "res.partner",
    compute="_compute_available_individuals",
)

@api.depends("change_request_id.registrant_id")
def _compute_available_individuals(self):
    for rec in self:
        group = rec.change_request_id.registrant_id
        if not group:
            rec.available_individual_ids = self.env["res.partner"]
            continue

        memberships = self.env["spp.group.membership"].search([
            ("group", "=", group.id),
            ("status", "=", "active"),
        ])
        rec.available_individual_ids = memberships.mapped("individual")
```

The form view then uses this computed field as a domain filter:

```xml
<field name="available_individual_ids" invisible="1" />
<field
    name="individual_id"
    domain="[('id', 'in', available_individual_ids)]"
/>
```

### Related display fields

Use `related` fields to surface data from linked records without duplicating storage. These are useful for showing names in the form and in the preview:

```python
member_name = fields.Char(related="individual_id.name", readonly=True)
source_group_name = fields.Char(related="source_group_id.name", readonly=True)
```

### Tracked fields

Add `tracking=True` to any field that should appear in the chatter audit trail. This is standard Odoo functionality provided by the `mail.thread` mixin:

```python
given_name = fields.Char(string="Given Name", tracking=True)
```

When a tracked field changes, Odoo automatically logs the old and new values in the record's chatter.

## Validation patterns

### Constraints

Use `@api.constrains` for rules that must always hold. The constraint runs on every `create()` and `write()` that touches the listed fields:

```python
@api.constrains("target_group_id", "source_group_id")
def _check_different_groups(self):
    for rec in self:
        if rec.target_group_id and rec.source_group_id:
            if rec.target_group_id == rec.source_group_id:
                raise ValidationError(
                    "Target group must be different from source group."
                )
```

### Onchange handlers

Use `@api.onchange` for UX-level logic that should run when the user changes a field in the form. Onchange handlers do not run during programmatic writes or in tests — use constraints for rules that must be enforced server-side.

The `add_member` detail model uses an onchange to auto-compute the full name:

```python
@api.onchange("given_name", "family_name")
def _onchange_names(self):
    if self.given_name or self.family_name:
        parts = [
            f"{self.family_name}," if self.family_name and self.given_name
            else self.family_name or "",
            self.given_name,
        ]
        self.member_name = " ".join(filter(None, parts)).upper()
```

### Pre-filling from the registrant

Override `_get_prefill_mapping()` to auto-populate detail fields with the registrant's current values when the CR is created. This lets the user see and edit existing data:

```python
def _get_prefill_mapping(self):
    return {
        "given_name": "given_name",
        "family_name": "family_name",
        "birthdate": "birthdate",
        "gender_id": "gender_id",
        "phone": "phone",
        "email": "email",
        "address_line1": "street",   # detail field name : registrant field name
        "postal_code": "zip",
    }
```

The base class provides a `prefill_from_registrant()` method that reads this mapping and copies the registrant's values into the corresponding detail fields. This method is called during the CR creation workflow — you do not need to call it manually.

## Built-in detail models

The following 11 detail models ship with `spp_change_request_v2`. Study them for patterns that match your use case:

| Model | Purpose | Complexity | What makes it instructive |
|-------|---------|:----------:|---------------------------|
| `spp.cr.detail.edit_individual` | Edit individual fields | Simple | Field mapping only, `_get_prefill_mapping()`, no strategy code |
| `spp.cr.detail.edit_group` | Edit group fields | Simple | Same pattern as edit_individual for groups |
| `spp.cr.detail.add_member` | Add person to group | Medium | Onchange for name computation, custom strategy creates records |
| `spp.cr.detail.remove_member` | Remove person from group | Medium | Member selection with domain filtering |
| `spp.cr.detail.change_hoh` | Change head of household | Medium | Swaps membership types between old and new head |
| `spp.cr.detail.update_id` | Update ID document | Medium | DMS integration for document storage |
| `spp.cr.detail.transfer_member` | Transfer between groups | Medium | Computed fields, membership lifecycle |
| `spp.cr.detail.exit_registrant` | Deactivate registrant | Medium | Reason and classification fields, status change |
| `spp.cr.detail.create_group` | Create a new group | Complex | Multi-step record creation |
| `spp.cr.detail.split_household` | Split household in two | Complex | Multi-member selection, new group creation |
| `spp.cr.detail.merge_registrants` | Merge duplicate records | Complex | Record consolidation, conflict resolution |

## Common mistakes

**Forgetting `mail.thread`** — If you omit `mail.thread` from `_inherit`, the chatter and tracking features will not work, and the form view will fail if it includes `<chatter />`.

**Not handling empty recordsets in computed fields** — Always set the field to an empty recordset in the `else` branch of a compute method. Odoo raises an error if a computed field is not assigned for every record in `self`.

**Using `@api.onchange` for server-side validation** — Onchange handlers only run in the web client UI. Use `@api.constrains` for rules that must be enforced regardless of how the record is modified.

**Forgetting `force_save="1"` on readonly fields** — If a field is `readonly=True` in the Python model but populated by an onchange handler, the form view will not send its value to the server unless you add `force_save="1"` in the XML.

**Many2one domain without `no_create`** — If your Many2one references a vocabulary model, always add `options="{'no_create': True}"` in the form view to prevent users from creating vocabulary codes inline.

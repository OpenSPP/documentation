---
openspp:
  doc_status: draft
  products: [core]
---

# Tutorial: build a transfer member CR type

This tutorial walks you through building a complete change request type from scratch. By the end, you will have a working Odoo module that lets users request transferring a person from one household to another, with approval workflow, validation, and tests.

## Prerequisites

- Python and Odoo model inheritance
- A working OpenSPP development environment
- The `spp_change_request_v2` module installed

## What you will build

The **Transfer Member** CR type allows a user to select a member of one group and request their transfer to a different group. When approved and applied, the system ends the membership in the source group and creates a new membership in the target group.

This requires a custom apply strategy because the built-in field mapping strategy can only copy field values — it cannot create or end membership records.

## Module structure

Create the following directory structure:

```text
spp_cr_transfer_member/
├── __init__.py
├── __manifest__.py
├── details/
│   ├── __init__.py
│   └── transfer_member.py
├── strategies/
│   ├── __init__.py
│   └── transfer_member.py
├── views/
│   └── detail_transfer_member_views.xml
├── data/
│   └── cr_type.xml
├── security/
│   └── ir.model.access.csv
└── tests/
    ├── __init__.py
    └── test_transfer_member.py
```

### `__manifest__.py`

```python
{
    "name": "CR Type: Transfer Member",
    "version": "17.0.1.0.0",
    "category": "OpenSPP",
    "depends": ["spp_change_request_v2"],
    "data": [
        "security/ir.model.access.csv",
        "views/detail_transfer_member_views.xml",
        "data/cr_type.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
```

The only required dependency is `spp_change_request_v2`, which provides the base models, approval mixin, and CR infrastructure.

### `__init__.py` files

Root `__init__.py`:

```python
from . import details
from . import strategies
```

`details/__init__.py`:

```python
from . import transfer_member
```

`strategies/__init__.py`:

```python
from . import transfer_member
```

`tests/__init__.py`:

```python
from . import test_transfer_member
```

## Step 1: define the detail model

The detail model captures the data for the transfer request. It inherits from `spp.cr.detail.base` (which links it to the parent change request) and `mail.thread` (which enables the message log / chatter).

### `details/transfer_member.py`

```python
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SPPCRDetailTransferMember(models.Model):
    _name = "spp.cr.detail.transfer_member"
    _description = "CR Detail: Transfer Member"
    _inherit = ["spp.cr.detail.base", "mail.thread"]

    # Source group comes from the parent change request's registrant
    source_group_id = fields.Many2one(
        "res.partner",
        string="Source Group",
        related="change_request_id.registrant_id",
        store=True,
        readonly=True,
    )

    # Computed list of transferable members (excludes head of household)
    available_individual_ids = fields.Many2many(
        "res.partner",
        string="Available Individuals",
        compute="_compute_available_individuals",
        help="Active members excluding head of household",
    )

    individual_id = fields.Many2one(
        "res.partner",
        string="Member to Transfer",
        tracking=True,
        domain="[('is_group', '=', False), ('is_registrant', '=', True)]",
    )

    # Set automatically when individual_id changes
    membership_id = fields.Many2one(
        "spp.group.membership",
        string="Current Membership",
        readonly=True,
    )

    target_group_id = fields.Many2one(
        "res.partner",
        string="Target Group",
        tracking=True,
        domain="[('is_group', '=', True), ('is_registrant', '=', True),"
        " ('id', '!=', registrant_id)]",
    )

    new_role_id = fields.Many2one(
        "spp.vocabulary.code",
        string="Role in New Group",
        domain="[('vocabulary_id.namespace_uri', '=',"
        " 'urn:openspp:vocab:group-membership-type'),"
        " ('code', '!=', 'head')]",
        tracking=True,
    )

    transfer_reason = fields.Selection(
        [
            ("marriage", "Marriage"),
            ("separation", "Separation/Divorce"),
            ("relocation", "Relocation"),
            ("household_split", "Household Split"),
            ("correction", "Data Correction"),
            ("other", "Other"),
        ],
        string="Transfer Reason",
        tracking=True,
    )

    transfer_date = fields.Date(
        string="Transfer Date",
        default=fields.Date.today,
        tracking=True,
    )

    remarks = fields.Text(string="Remarks", tracking=True)

    # Computed display fields
    member_name = fields.Char(related="individual_id.name", readonly=True)
    source_group_name = fields.Char(related="source_group_id.name", readonly=True)
    target_group_name = fields.Char(related="target_group_id.name", readonly=True)

    @api.depends("change_request_id.registrant_id")
    def _compute_available_individuals(self):
        """Compute transferable members, excluding the head of household."""
        head_kind = self.env["spp.vocabulary.code"].get_code(
            "urn:openspp:vocab:group-membership-type", "head"
        )
        for rec in self:
            group = rec.change_request_id.registrant_id
            if not group:
                rec.available_individual_ids = self.env["res.partner"]
                continue

            memberships = self.env["spp.group.membership"].search([
                ("group", "=", group.id),
                ("status", "=", "active"),
            ])

            if head_kind:
                memberships = memberships.filtered(
                    lambda m: head_kind not in m.membership_type_ids
                )

            rec.available_individual_ids = memberships.mapped("individual")

    @api.onchange("individual_id")
    def _onchange_individual_id(self):
        """Look up the active membership when the user selects a member."""
        self.membership_id = False
        if self.individual_id and self.change_request_id.registrant_id:
            membership = self.env["spp.group.membership"].search([
                ("group", "=", self.change_request_id.registrant_id.id),
                ("individual", "=", self.individual_id.id),
                ("status", "=", "active"),
            ], limit=1)
            if membership:
                self.membership_id = membership

    @api.constrains("target_group_id", "source_group_id")
    def _check_different_groups(self):
        """Prevent transferring to the same group."""
        for rec in self:
            if rec.target_group_id and rec.source_group_id:
                if rec.target_group_id == rec.source_group_id:
                    raise ValidationError(
                        "Target group must be different from source group."
                    )
```

**Key patterns to notice:**

- **`source_group_id`** is a `related` field — it reads directly from the parent CR's registrant, so the user never has to set it manually.
- **`available_individual_ids`** is a computed Many2many that filters out the head of household. The form view uses it as a domain filter on `individual_id`.
- **`membership_id`** is set automatically via `@api.onchange` when the user picks an individual. The `readonly=True` keeps it hidden from direct editing.
- **`@api.constrains`** enforces that source and target groups differ — this validation runs on every write.
- **`tracking=True`** on key fields enables the chatter audit trail.

## Step 2: create the form view

The form view follows the standard CR detail pattern: a header with navigation buttons and a stage statusbar, and a sheet with grouped fields.

### `views/detail_transfer_member_views.xml`

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
    <record id="spp_cr_detail_transfer_member_form" model="ir.ui.view">
        <field name="name">spp.cr.detail.transfer_member.form</field>
        <field name="model">spp.cr.detail.transfer_member</field>
        <field name="arch" type="xml">
            <form
                string="Transfer Member Details"
                readonly="not is_cr_manager or approval_state not in ('draft', 'revision')"
            >
                <header>
                    <field name="is_cr_manager" invisible="1" />
                    <button
                        name="action_next_documents"
                        string="Next: Upload Documents"
                        type="object"
                        class="btn-primary"
                        icon="fa-arrow-right"
                        invisible="approval_state not in ('draft', 'revision')"
                        groups="spp_change_request_v2.group_cr_manager"
                    />
                    <button
                        name="action_skip_to_review"
                        string="Review &amp; Submit"
                        type="object"
                        class="btn-success"
                        icon="fa-check-circle"
                        invisible="approval_state not in ('draft', 'revision')"
                        groups="spp_change_request_v2.group_cr_manager"
                    />
                    <button
                        name="action_save_and_go_to_list"
                        string="Save as Draft"
                        type="object"
                        class="btn-outline-secondary"
                        invisible="approval_state not in ('draft', 'revision')"
                        groups="spp_change_request_v2.group_cr_manager"
                    />
                    <field
                        name="stage"
                        widget="statusbar"
                        statusbar_visible="details,documents,review"
                    />
                </header>
                <sheet>
                    <group>
                        <group string="Source">
                            <field
                                name="source_group_id"
                                options="{'no_create': True, 'no_open': True}"
                            />
                            <field name="available_individual_ids" invisible="1" />
                            <field
                                name="individual_id"
                                options="{'no_create': True}"
                                domain="[('id', 'in', available_individual_ids)]"
                                required="1"
                            />
                            <field name="member_name" />
                            <field name="membership_id" invisible="1" force_save="1" />
                        </group>
                        <group string="Target">
                            <field
                                name="target_group_id"
                                options="{'no_create': True}"
                                required="1"
                            />
                            <field
                                name="new_role_id"
                                options="{'no_create': True, 'no_open': True}"
                            />
                        </group>
                    </group>
                    <group>
                        <group string="Transfer Details">
                            <field name="transfer_reason" />
                            <field name="transfer_date" />
                        </group>
                    </group>
                    <group string="Additional Information">
                        <field
                            name="remarks"
                            placeholder="Enter any additional notes..."
                        />
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
```

**Key patterns to notice:**

- The top-level `<form>` tag has a `readonly` attribute that locks the entire form when the user is not a CR manager or the CR is past the draft/revision stage. This is the standard pattern for all CR detail views.
- **`available_individual_ids`** is declared `invisible="1"` — it exists only to provide the domain filter for `individual_id`.
- **`membership_id`** uses `force_save="1"` because it is `readonly` in Python but needs to persist when set by the onchange handler.
- The header buttons (`action_next_documents`, `action_skip_to_review`, `action_save_and_go_to_list`) are inherited from `spp.cr.detail.base` — you do not need to implement them.

## Step 3: build the apply strategy

The apply strategy contains the business logic that executes when an approved CR is applied. It inherits from `spp.cr.strategy.base` and must implement the `apply()` method.

### `strategies/transfer_member.py`

```python
import logging

from odoo import Command, _, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class SPPCRApplyTransferMember(models.AbstractModel):
    _name = "spp.cr.apply.transfer_member"
    _inherit = "spp.cr.strategy.base"
    _description = "CR Apply: Transfer Member"

    def apply(self, change_request):
        """Transfer a member from the source group to the target group."""
        source_group = change_request.registrant_id
        if not source_group.is_group:
            raise UserError(_("Source registrant must be a group."))

        detail = change_request.get_detail()
        if not detail:
            raise UserError(_("No detail record found."))
        if not detail.membership_id:
            raise UserError(_("No member selected for transfer."))
        if not detail.target_group_id:
            raise UserError(_("No target group selected."))
        if not detail.target_group_id.is_group:
            raise UserError(_("Target must be a group."))

        membership = detail.membership_id
        individual = membership.individual
        target_group = detail.target_group_id

        # Verify the membership is still active
        if membership.status != "active":
            raise UserError(_("Membership is already inactive."))

        # Prevent duplicate membership in target group
        existing = self.env["spp.group.membership"].search([
            ("group", "=", target_group.id),
            ("individual", "=", individual.id),
            ("status", "=", "active"),
        ], limit=1)
        if existing:
            raise UserError(
                _("Individual is already a member of the target group.")
            )

        # End membership in source group
        transfer_datetime = fields.Datetime.to_datetime(detail.transfer_date)
        if membership.start_date and transfer_datetime < membership.start_date:
            transfer_datetime = membership.start_date
        membership.write({"ended_date": transfer_datetime, "active": False})

        # Create membership in target group
        new_membership_vals = {
            "group": target_group.id,
            "individual": individual.id,
            "start_date": transfer_datetime,
        }
        if detail.new_role_id:
            new_membership_vals["membership_type_ids"] = [
                Command.link(detail.new_role_id.id)
            ]

        self.env["spp.group.membership"].create(new_membership_vals)

        _logger.info(
            "Transferred member partner_id=%s from group partner_id=%s "
            "to group partner_id=%s via CR %s",
            individual.id,
            source_group.id,
            target_group.id,
            change_request.name,
        )

        return True

    def preview(self, change_request):
        """Return a summary of what the transfer will do."""
        detail = change_request.get_detail()
        if not detail:
            return {}

        return {
            "_action": "transfer_member",
            "member_name": detail.member_name,
            "source_group": detail.source_group_name,
            "target_group": detail.target_group_name,
            "new_role": (
                detail.new_role_id.display if detail.new_role_id else None
            ),
            "transfer_date": str(detail.transfer_date),
            "reason": detail.transfer_reason,
        }
```

**Key patterns to notice:**

- The strategy is an **`AbstractModel`**, not a regular `Model` — it has no database table. It exists only to provide the `apply()` and `preview()` methods.
- **Validate first, then act.** The method checks every precondition before making any changes. If any check fails, it raises `UserError` with a translatable message.
- **`change_request.get_detail()`** returns the linked detail record. This is a helper from the base CR model.
- The strategy runs with `sudo()` privileges (the CR framework calls it that way), so the approval workflow is the security gate — not the strategy itself.
- **`Command.link()`** adds a Many2many relation without replacing existing values.
- The `preview()` method returns a dict describing the planned changes. The CR UI displays this to reviewers before they approve.

## Step 4: register the CR type

The CR type record tells the system about your new type — its name, which detail model to use, and which strategy to apply.

### `data/cr_type.xml`

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
    <data noupdate="1">
        <record id="cr_type_transfer_member" model="spp.change.request.type">
            <field name="name">Transfer Member</field>
            <field name="code">transfer_member</field>
            <field name="description">Transfer a member from one group to another</field>
            <field name="target_type">group</field>
            <field name="detail_model">spp.cr.detail.transfer_member</field>
            <field
                name="detail_form_view_id"
                ref="spp_cr_detail_transfer_member_form"
            />
            <field name="apply_strategy">custom</field>
            <field name="apply_model">spp.cr.apply.transfer_member</field>
            <field name="icon">fa-exchange-alt</field>
            <field name="sequence">60</field>
        </record>
    </data>
</odoo>
```

**Field reference:**

| Field | Purpose |
|-------|---------|
| `code` | Unique identifier used in API calls and tests |
| `target_type` | `individual`, `group`, or `both` — controls which registrants this CR type appears for |
| `detail_model` | The `_name` of your detail model class |
| `detail_form_view_id` | Reference to the form view XML record |
| `apply_strategy` | `field_mapping` (built-in) or `custom` (your own strategy) |
| `apply_model` | The `_name` of your strategy class (only needed when `apply_strategy` is `custom`) |
| `icon` | Font Awesome icon class for the CR type selector |
| `sequence` | Display order in the CR type list |

The `noupdate="1"` wrapper means this record is created on install but not overwritten on module upgrade, allowing administrators to customize it after installation.

## Step 5: set up security

Every detail model needs access rules for the CR security groups. The pattern is the same for all CR types: users, validators, and HQ validators get read/write/create; managers also get delete.

### `security/ir.model.access.csv`

```text
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_transfer_member_user,spp.cr.detail.transfer_member user,model_spp_cr_detail_transfer_member,spp_change_request_v2.group_cr_user,1,1,1,0
access_transfer_member_validator,spp.cr.detail.transfer_member validator,model_spp_cr_detail_transfer_member,spp_change_request_v2.group_cr_validator,1,1,1,0
access_transfer_member_validator_hq,spp.cr.detail.transfer_member validator hq,model_spp_cr_detail_transfer_member,spp_change_request_v2.group_cr_validator_hq,1,1,1,0
access_transfer_member_manager,spp.cr.detail.transfer_member manager,model_spp_cr_detail_transfer_member,spp_change_request_v2.group_cr_manager,1,1,1,1
```

The base module (`spp_change_request_v2`) already defines record rules that restrict which CRs a user can see based on their role. Your detail model inherits this protection through its link to the parent CR record.

## Step 6: write tests

Tests verify that the detail model validates correctly, the strategy applies as expected, and error cases are handled.

### `tests/test_transfer_member.py`

```python
from odoo import fields
from odoo.exceptions import UserError, ValidationError
from odoo.tests import TransactionCase


class TestTransferMember(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        Partner = cls.env["res.partner"]
        Membership = cls.env["spp.group.membership"]

        # Create source and target groups
        cls.source_group = Partner.create({
            "name": "Source Household",
            "is_registrant": True,
            "is_group": True,
        })
        cls.target_group = Partner.create({
            "name": "Target Household",
            "is_registrant": True,
            "is_group": True,
        })

        # Create a test individual and add to source group
        cls.individual = Partner.create({
            "name": "Test Person",
            "is_registrant": True,
            "is_group": False,
        })
        cls.membership = Membership.create({
            "group": cls.source_group.id,
            "individual": cls.individual.id,
            "start_date": fields.Datetime.now(),
        })

        # Look up or create the CR type
        cls.cr_type = cls.env["spp.change.request.type"].search(
            [("code", "=", "transfer_member")], limit=1
        )
        if not cls.cr_type:
            cls.cr_type = cls.env["spp.change.request.type"].create({
                "name": "Transfer Member",
                "code": "transfer_member",
                "target_type": "group",
                "detail_model": "spp.cr.detail.transfer_member",
                "apply_strategy": "custom",
                "apply_model": "spp.cr.apply.transfer_member",
            })

    def _create_cr(self, **detail_vals):
        """Helper: create a CR and populate its detail record."""
        cr = self.env["spp.change.request"].create({
            "request_type_id": self.cr_type.id,
            "registrant_id": self.source_group.id,
        })
        detail = cr.get_detail()
        detail.write(detail_vals)
        return cr

    def test_successful_transfer(self):
        """Applying an approved transfer ends old membership,
        creates new one."""
        cr = self._create_cr(
            membership_id=self.membership.id,
            target_group_id=self.target_group.id,
            transfer_reason="marriage",
            transfer_date=fields.Date.today(),
        )
        cr.approval_state = "approved"
        cr.action_apply()

        self.assertTrue(cr.is_applied)

        # Old membership is ended
        self.assertTrue(self.membership.ended_date)
        self.assertEqual(self.membership.status, "inactive")

        # New membership exists in target group
        new_membership = self.env["spp.group.membership"].search([
            ("group", "=", self.target_group.id),
            ("individual", "=", self.individual.id),
            ("status", "=", "active"),
        ])
        self.assertTrue(new_membership)

    def test_transfer_with_role(self):
        """Transferred member receives the assigned role."""
        # Create a fresh individual for this test
        individual = self.env["res.partner"].create({
            "name": "Role Test",
            "is_registrant": True,
            "is_group": False,
        })
        membership = self.env["spp.group.membership"].create({
            "group": self.source_group.id,
            "individual": individual.id,
            "start_date": fields.Datetime.now(),
        })

        role = self.env["spp.vocabulary.code"].search([
            ("vocabulary_id.namespace_uri", "=",
             "urn:openspp:vocab:group-membership-type"),
            ("code", "!=", "head"),
        ], limit=1)

        cr = self._create_cr(
            membership_id=membership.id,
            target_group_id=self.target_group.id,
            new_role_id=role.id if role else False,
            transfer_reason="relocation",
            transfer_date=fields.Date.today(),
        )
        cr.approval_state = "approved"
        cr.action_apply()

        new_membership = self.env["spp.group.membership"].search([
            ("group", "=", self.target_group.id),
            ("individual", "=", individual.id),
            ("status", "=", "active"),
        ])
        if role:
            self.assertIn(role, new_membership.membership_type_ids)

    def test_same_group_raises_validation_error(self):
        """Cannot set target group to the same as source group."""
        cr = self.env["spp.change.request"].create({
            "request_type_id": self.cr_type.id,
            "registrant_id": self.source_group.id,
        })
        detail = cr.get_detail()

        with self.assertRaises(ValidationError):
            detail.write({
                "target_group_id": self.source_group.id,
            })

    def test_duplicate_membership_raises_user_error(self):
        """Cannot transfer if individual is already in target group."""
        individual = self.env["res.partner"].create({
            "name": "Duplicate Test",
            "is_registrant": True,
            "is_group": False,
        })
        # Membership in source
        source_membership = self.env["spp.group.membership"].create({
            "group": self.source_group.id,
            "individual": individual.id,
            "start_date": fields.Datetime.now(),
        })
        # Membership already in target
        self.env["spp.group.membership"].create({
            "group": self.target_group.id,
            "individual": individual.id,
            "start_date": fields.Datetime.now(),
        })

        cr = self._create_cr(
            membership_id=source_membership.id,
            target_group_id=self.target_group.id,
            transfer_reason="other",
            transfer_date=fields.Date.today(),
        )
        cr.approval_state = "approved"

        with self.assertRaises(UserError):
            cr.action_apply()

    def test_inactive_membership_raises_user_error(self):
        """Cannot transfer an already-ended membership."""
        individual = self.env["res.partner"].create({
            "name": "Inactive Test",
            "is_registrant": True,
            "is_group": False,
        })
        membership = self.env["spp.group.membership"].create({
            "group": self.source_group.id,
            "individual": individual.id,
            "start_date": fields.Datetime.now(),
            "ended_date": fields.Datetime.now(),
        })

        cr = self._create_cr(
            membership_id=membership.id,
            target_group_id=self.target_group.id,
            transfer_reason="other",
            transfer_date=fields.Date.today(),
        )
        cr.approval_state = "approved"

        with self.assertRaises(UserError):
            cr.action_apply()

    def test_preview_returns_expected_structure(self):
        """Preview returns a dict describing the planned changes."""
        cr = self._create_cr(
            membership_id=self.membership.id,
            target_group_id=self.target_group.id,
            transfer_reason="marriage",
            transfer_date=fields.Date.today(),
        )

        preview = cr.action_preview_changes()

        self.assertEqual(preview["_action"], "transfer_member")
        self.assertIn("source_group", preview)
        self.assertIn("target_group", preview)
```

**Key patterns to notice:**

- **`setUpClass`** creates all shared test data once. Each test method creates its own CR so tests are independent.
- **`_create_cr` helper** reduces boilerplate — create the CR and populate the detail in one call.
- **Happy path tests** verify the end state (membership ended, new membership created), not just that no error was raised.
- **Error case tests** use `assertRaises` and verify the specific exception type (`ValidationError` for constraint violations, `UserError` for strategy failures).
- The CR type is looked up first and only created if not found, so the tests work whether or not the XML data has been loaded.

## Verify it works

Install the module and test it manually:

1. Go to **Change Requests** in the menu
2. Click **New** and select **Transfer Member**
3. Pick a source group (household) as the registrant
4. Select a member to transfer and a target group
5. Submit the CR for approval
6. Approve and apply it
7. Verify the member now appears in the target group's member list

## What's next

You now have a working CR type. To go further:

- {doc}`detail_models` — learn about pre-filling from the registrant, additional validation patterns, and the full base class API
- {doc}`apply_strategies` — understand when to use field mapping vs. custom strategies, and see how other built-in strategies handle record creation and relationship changes
- {doc}`approval_hooks` — hook into the approval lifecycle to add custom behavior on submit, approve, or reject
- {doc}`testing` — patterns for testing approval workflows, conflict detection, and common pitfalls

## See also

- {doc}`/config_guide/change_request_types/index` — configuring CR types through the UI (no code required)
- {doc}`/config_guide/change_request_types/field_mappings` — the field mapping apply strategy (for simple field-copy CR types)
- {doc}`/config_guide/change_request_types/conflict_detection` — configuring conflict and duplicate detection rules

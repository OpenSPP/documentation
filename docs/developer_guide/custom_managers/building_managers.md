---
openspp:
  doc_status: draft
  products: [core]
---

# Building a custom manager

**For: developers**

This page walks you through building a custom program manager. The process is the same for all manager types (eligibility, entitlement, cycle, payment) — you create a new model, inherit from the base class, implement the required methods, and register it.

Read the {doc}`manager_pattern` page first if you haven't already.

## The common pattern

Every custom manager follows these steps:

1. **Create a module** with a dependency on `spp_programs`
2. **Define the implementation model** inheriting from the base class and `spp.manager.source.mixin`
3. **Override required methods** with your custom logic
4. **Register the manager** by extending `_selection_manager_ref_id()` on the wrapper model
5. **Create a form view** so administrators can configure your manager
6. **Add security** (ACLs for the new model)

## Step-by-step: custom eligibility manager

This example creates an eligibility manager that filters registrants by age range.

### Module manifest

```python
# spp_eligibility_age/__manifest__.py
{
    "name": "OpenSPP Age-Based Eligibility",
    "summary": "Eligibility manager that filters registrants by age range.",
    "category": "OpenSPP/Core",
    "version": "19.0.2.0.0",
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/OpenSPP2",
    "license": "LGPL-3",
    "depends": [
        "spp_programs",
        "spp_security",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/eligibility_manager_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
```

### Implementation model

```python
# spp_eligibility_age/models/eligibility_manager_age.py
import logging
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class AgeEligibilityManager(models.Model):
    """Eligibility manager that filters registrants by age range."""

    _name = "spp.program.membership.manager.age"
    _inherit = ["spp.program.membership.manager", "spp.manager.source.mixin"]
    _description = "Age-Based Eligibility Manager"

    # Custom configuration fields
    min_age = fields.Integer(
        string="Minimum Age",
        default=0,
        help="Minimum age in years (inclusive).",
    )
    max_age = fields.Integer(
        string="Maximum Age",
        default=120,
        help="Maximum age in years (inclusive).",
    )

    def _get_eligible_partner_ids(self):
        """Return partner IDs that match the age criteria."""
        today = date.today()
        # Born before this date = at least min_age years old
        max_birthdate = today - relativedelta(years=self.min_age)
        # Born after this date = at most max_age years old
        min_birthdate = today - relativedelta(years=self.max_age + 1)

        domain = [
            ("is_registrant", "=", True),
            ("is_group", "=", False),
            ("birthdate", ">=", min_birthdate),
            ("birthdate", "<=", max_birthdate),
        ]

        # Apply target type filter from program
        if self.program_id.target_type == "group":
            domain = [
                ("is_registrant", "=", True),
                ("is_group", "=", True),
            ]

        return self.env["res.partner"].search(domain).ids

    def enroll_eligible_registrants(self, program_memberships):
        """Validate which program members meet the age criteria."""
        eligible_ids = self._get_eligible_partner_ids()

        return program_memberships.filtered(
            lambda m: m.partner_id.id in eligible_ids
        )

    def verify_cycle_eligibility(self, cycle, membership):
        """Verify cycle members still meet the age criteria."""
        eligible_ids = self._get_eligible_partner_ids()

        return membership.filtered(
            lambda m: m.partner_id.id in eligible_ids
        )

    def import_eligible_registrants(self, state=None):
        """Import registrants matching the age criteria into the program."""
        eligible_ids = self._get_eligible_partner_ids()

        # Filter out already-enrolled registrants
        existing = self.env["spp.program.membership"].search([
            ("program_id", "=", self.program_id.id),
            ("partner_id", "in", eligible_ids),
        ]).mapped("partner_id.id")

        new_ids = [pid for pid in eligible_ids if pid not in existing]

        # Create memberships
        vals_list = [
            {
                "program_id": self.program_id.id,
                "partner_id": pid,
                "state": state or "draft",
            }
            for pid in new_ids
        ]

        if vals_list:
            self.env["spp.program.membership"].create(vals_list)

        return len(vals_list)
```

### Register the manager

Add a file that extends the wrapper model's selection:

```python
# spp_eligibility_age/models/eligibility_manager.py
from odoo import api, models


class EligibilityManager(models.Model):
    _inherit = "spp.eligibility.manager"

    @api.model
    def _selection_manager_ref_id(self):
        selection = super()._selection_manager_ref_id()
        new_manager = (
            "spp.program.membership.manager.age",
            "Age-Based Eligibility",
        )
        if new_manager not in selection:
            selection.append(new_manager)
        return selection
```

Don't forget the `models/__init__.py`:

```python
from . import eligibility_manager
from . import eligibility_manager_age
```

### Create a form view

The form view is displayed when an administrator clicks the gear icon to configure the manager on a program:

```xml
<!-- spp_eligibility_age/views/eligibility_manager_views.xml -->
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <record id="view_eligibility_manager_age_form" model="ir.ui.view">
        <field name="name">spp.program.membership.manager.age.form</field>
        <field name="model">spp.program.membership.manager.age</field>
        <field name="arch" type="xml">
            <form string="Age-Based Eligibility Manager">
                <sheet>
                    <group>
                        <group string="Age Range">
                            <field name="min_age" />
                            <field name="max_age" />
                        </group>
                        <group string="Program">
                            <field name="name" />
                            <field name="program_id" readonly="1" />
                        </group>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
```

### Add security

```text
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_spp_eligibility_age_system,Age Eligibility System,model_spp_program_membership_manager_age,base.group_system,1,1,1,1
access_spp_eligibility_age_admin,Age Eligibility Admin,model_spp_program_membership_manager_age,spp_security.group_spp_admin,1,1,1,1
```

### Result

After installing this module, administrators will see "Age-Based Eligibility" as an option when configuring a program's eligibility manager. The form lets them set min/max age, and the program will only enroll registrants within that age range.

## Registration reference

Each manager type has a wrapper model where you register your implementation:

| Manager type | Wrapper model | Override method |
|-------------|---------------|----------------|
| Eligibility | `spp.eligibility.manager` | `_selection_manager_ref_id()` |
| Entitlement | `spp.program.entitlement.manager` | `_selection_manager_ref_id()` |
| Cycle | `spp.cycle.manager` | `_selection_manager_ref_id()` |
| Payment | `spp.program.payment.manager` | `_selection_manager_ref_id()` |
| Program | `spp.program.manager` | `_selection_manager_ref_id()` |
| Deduplication | `spp.deduplication.manager` | `_selection_manager_ref_id()` |
| Notification | `spp.program.notification.manager` | `_selection_manager_ref_id()` |

The selection tuple format is `("model_name", "Display Label")`.

## Method reference by manager type

### Eligibility manager

Base class: `spp.program.membership.manager`

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `enroll_eligible_registrants` | `program_memberships` (recordset) | Filtered recordset of eligible memberships | Validate which members meet criteria |
| `verify_cycle_eligibility` | `cycle`, `membership` (recordset) | Filtered recordset of eligible cycle memberships | Re-check eligibility for a cycle |
| `import_eligible_registrants` | `state=None` | Integer count of imported registrants | Import matching registrants into the program |

### Entitlement manager

Base class: `spp.base.program.entitlement.manager`

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `prepare_entitlements` | `cycle`, `beneficiaries` (recordset) | Created entitlement recordset | Create entitlement records for beneficiaries |
| `set_pending_validation_entitlements` | `cycle` | None | Move entitlements to pending approval |
| `validate_entitlements` | `cycle` | Action dict or None | Validate and approve entitlements |
| `approve_entitlements` | `entitlements` (recordset) | Tuple `(error_count, error_message)` | Approve entitlements and create payments |
| `cancel_entitlements` | `cycle` | None | Cancel draft/pending entitlements |

Important class attributes:

| Attribute | Default | Purpose |
|-----------|---------|---------|
| `IS_CASH_ENTITLEMENT` | `True` | Set to `False` for in-kind entitlements |
| `MIN_ROW_JOB_QUEUE` | `200` | Threshold for async processing |

### Cycle manager

Base class: `spp.base.cycle.manager`

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `new_cycle` | `name`, `new_start_date`, `sequence` | Created `spp.cycle` record | Create a new cycle with dates |
| `check_eligibility` | `cycle`, `beneficiaries=None` | Action dict | Check beneficiary eligibility for cycle |
| `prepare_entitlements` | `cycle` | Action dict or None | Delegate to entitlement manager |
| `validate_entitlements` | `cycle`, `cycle_memberships` | Error dict or None | Validate cycle entitlements |
| `approve_cycle` | `cycle`, `auto_approve=False`, `entitlement_manager=None` | Action dict or None | Approve cycle and optionally auto-approve entitlements |
| `copy_beneficiaries_from_program` | `cycle`, `state="enrolled"` | Action dict | Copy enrolled members into cycle |
| `add_beneficiaries` | `cycle`, `beneficiaries`, `state="draft"` | Action dict | Add specific beneficiaries to cycle |
| `issue_payments` | `cycle` | None | Delegate to payment manager |
| `mark_distributed` | `cycle` | None | Set cycle state to distributed |
| `mark_ended` | `cycle` | None | Set cycle state to ended |

The default cycle manager (`spp.cycle.manager.default`) also inherits from `spp.cycle.recurrence.mixin`, which provides recurrence scheduling fields (frequency, interval, day of month, etc.).

### Payment manager

Base class: `spp.base.program.payment.manager`

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `prepare_payments` | `cycle`, `entitlements=None` | Action dict | Create payment records from entitlements |
| `send_payments` | `batches` (recordset) | Action dict or None | Process/export payment batches |
| `validate_accounts` | `entitlements` (recordset) | List of errors | Verify beneficiary payment accounts |

Notification, compliance, and deduplication managers are less commonly extended. See their source files in `spp_programs/models/managers/` for method signatures.

## Async processing

For large batches, managers should use async processing via `delayable()`:

```python
def prepare_entitlements(self, cycle, beneficiaries):
    if len(beneficiaries) > self.MIN_ROW_JOB_QUEUE:
        # Process asynchronously
        self.delayable()._prepare_entitlements_async(
            cycle, beneficiaries
        )
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Processing"),
                "message": _("Entitlements are being prepared in the background."),
                "type": "info",
            },
        }
    # Process synchronously for small batches
    return self._prepare_entitlements_sync(cycle, beneficiaries)
```

The threshold constants `MIN_ROW_JOB_QUEUE` (200) and `MAX_ROW_JOB_QUEUE` (2000) are defined on the base classes.

## Inheritance checklist

When creating a custom manager, always inherit from both the base class and the source mixin:

```python
class MyManager(models.Model):
    _name = "spp.program.entitlement.manager.custom"
    _inherit = [
        "spp.base.program.entitlement.manager",  # Base class
        "spp.manager.source.mixin",               # Lifecycle management
    ]
```

The `spp.manager.source.mixin` handles:

- Updating the reference on the parent wrapper model when the implementation is created
- Cleaning up wrapper records when the implementation is deleted
- Providing `get_manager_view_id()` for the form view lookup

## Common mistakes

**Forgetting `spp.manager.source.mixin`** — If you only inherit from the base class and omit the source mixin, the wrapper model will not automatically link to your implementation when it is created. The manager will appear in the selection but fail to open.

**Using `(4, id)` instead of `(6, 0, [id])` for Many2many manager slots** — Most manager slots on programs are constrained to a single manager. Using the append command `(4, id)` can violate this constraint. Use `(6, 0, [id])` to replace the entire set.

**Not registering in the wrapper's selection** — Your manager will not appear in the dropdown unless you override `_selection_manager_ref_id()` on the wrapper model. This is a separate file from the implementation — see the registration pattern above.

**Returning the wrong type from `prepare_entitlements`** — The method must return an `spp.entitlement` recordset (even if empty), not a list or count. Returning the wrong type causes downstream failures in the cycle workflow.

**Skipping `existing_partner_ids` check in `prepare_entitlements`** — If you do not check for existing entitlements before creating new ones, running the preparation step twice will create duplicate entitlements. Always filter out already-processed partners.

## What's next

- {doc}`tutorial` — build a complete CCT program module that uses all three manager types together

## See also

- {doc}`manager_pattern` — the wrapper/implementation architecture in depth
- {doc}`/developer_guide/change_request_types/index` — building custom change request types (similar extension pattern)

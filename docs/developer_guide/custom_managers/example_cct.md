---
openspp:
  doc_status: draft
  products: [core]
---

# Example: CCT program managers

**For: developers**

This tutorial builds a complete set of custom managers for a **conditional cash transfer (CCT)** program — one of the most common social protection program types. The module includes an eligibility manager, an entitlement manager, and a cycle manager that work together.

```{tip}
Want to skip ahead? Download the complete module: {download}`spp_cct_managers.zip </_static/samples/spp_cct_managers.zip>`
```

## What you will build

| Manager | Logic | Configuration fields |
|---------|-------|---------------------|
| **Eligibility** | Households with income ≤ threshold AND at least one child under age limit | `max_income`, `child_max_age` |
| **Entitlement** | Base amount per household + per-child top-up (capped) | `base_amount`, `per_child_amount`, `max_children`, `child_max_age` |
| **Cycle** | Quarterly cycles aligned to Q1-Q4, with auto-copy of beneficiaries | `is_auto_copy_beneficiaries` |

### How they work together

```
1. Admin creates a CCT program and selects these managers
2. Eligibility manager imports households matching income + children criteria
3. Admin enrolls eligible households
4. Admin creates a new cycle → cycle manager creates Q1/Q2/Q3/Q4 cycle
5. Cycle manager auto-copies enrolled beneficiaries into the cycle
6. Entitlement manager calculates: base_amount + (per_child_amount × children)
7. Entitlements are approved and sent for payment
```

## Prerequisites

- A running development environment (see {doc}`../setup/index`)
- Understanding of the {doc}`manager_pattern`
- The `spp_programs` module installed (included in the `mis` demo profile)

## Eligibility manager

The CCT eligibility manager filters households based on income and whether they have children under a certain age.

### `models/eligibility_manager_cct.py`

```python
import logging
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class CCTEligibilityManager(models.Model):
    """Eligibility manager for conditional cash transfer programs.

    Filters households based on two criteria:
    1. Household income is at or below a configurable threshold
    2. Household has at least one child under a configurable age
    """

    _name = "spp.program.membership.manager.cct"
    _inherit = ["spp.program.membership.manager", "spp.manager.source.mixin"]
    _description = "CCT Eligibility Manager"

    max_income = fields.Float(
        string="Maximum Household Income",
        default=10000.0,
        help="Households with income above this amount are not eligible.",
    )

    child_max_age = fields.Integer(
        string="Maximum Child Age",
        default=18,
        help="Children must be under this age for the household to qualify.",
    )

    def _get_child_birthdate_cutoff(self):
        """Return the earliest birthdate for a child to be considered eligible."""
        return date.today() - relativedelta(years=self.child_max_age)

    def _get_eligible_group_ids(self):
        """Return IDs of groups that meet income and child-age criteria."""
        cutoff_date = self._get_child_birthdate_cutoff()

        # Find groups with income at or below the threshold
        groups = self.env["res.partner"].search([
            ("is_registrant", "=", True),
            ("is_group", "=", True),
            ("income", "<=", self.max_income),
        ])

        eligible_ids = []
        for group in groups:
            # Check if any member is a child under the age threshold
            for membership in group.group_membership_ids:
                individual = membership.individual
                if (
                    individual.birthdate
                    and individual.birthdate >= cutoff_date
                ):
                    eligible_ids.append(group.id)
                    break

        return eligible_ids

    def enroll_eligible_registrants(self, program_memberships):
        """Validate which program members meet the CCT criteria."""
        eligible_ids = self._get_eligible_group_ids()
        return program_memberships.filtered(
            lambda m: m.partner_id.id in eligible_ids
        )

    def verify_cycle_eligibility(self, cycle, membership):
        """Re-check CCT eligibility for cycle members."""
        eligible_ids = self._get_eligible_group_ids()
        return membership.filtered(
            lambda m: m.partner_id.id in eligible_ids
        )

    def import_eligible_registrants(self, state=None):
        """Import households matching CCT criteria into the program."""
        eligible_ids = self._get_eligible_group_ids()

        # Exclude already-enrolled households
        existing = self.env["spp.program.membership"].search([
            ("program_id", "=", self.program_id.id),
            ("partner_id", "in", eligible_ids),
        ]).mapped("partner_id.id")

        new_ids = [pid for pid in eligible_ids if pid not in existing]

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

Key points:

- The private method `_get_eligible_group_ids()` contains the core logic, reused by all three interface methods
- It searches for groups (households) where `income <= max_income`
- Then filters to those with at least one member whose `birthdate` makes them younger than `child_max_age`
- The `import_eligible_registrants` method avoids creating duplicate memberships

### Registration

A separate file extends the wrapper model's selection dropdown:

```python
# models/eligibility_manager.py
from odoo import api, models


class EligibilityManagerRegistration(models.Model):
    _inherit = "spp.eligibility.manager"

    @api.model
    def _selection_manager_ref_id(self):
        selection = super()._selection_manager_ref_id()
        new_manager = (
            "spp.program.membership.manager.cct",
            "CCT Eligibility (Income + Children)",
        )
        if new_manager not in selection:
            selection.append(new_manager)
        return selection
```

## Entitlement manager

The CCT entitlement manager calculates transfer amounts based on household composition.

### `models/entitlement_manager_cct.py`

```python
import logging
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class CCTEntitlementManager(models.Model):
    """Entitlement manager for conditional cash transfer programs.

    Calculates entitlements as:
        amount = base_amount + (per_child_amount * eligible_children)

    Where eligible_children is capped at max_children.
    """

    _name = "spp.program.entitlement.manager.cct"
    _inherit = [
        "spp.base.program.entitlement.manager",
        "spp.manager.source.mixin",
    ]
    _description = "CCT Entitlement Manager"

    IS_CASH_ENTITLEMENT = True

    base_amount = fields.Monetary(
        string="Base Amount per Household",
        default=1000.0,
        currency_field="currency_id",
    )

    per_child_amount = fields.Monetary(
        string="Per-Child Top-Up",
        default=500.0,
        currency_field="currency_id",
    )

    max_children = fields.Integer(
        string="Maximum Children for Top-Up",
        default=5,
        help="Set to 0 for no cap.",
    )

    child_max_age = fields.Integer(
        string="Maximum Child Age",
        default=18,
    )

    currency_id = fields.Many2one(
        "res.currency",
        related="program_id.journal_id.currency_id",
        readonly=True,
    )

    def _count_eligible_children(self, group):
        """Count children under the age threshold in a household."""
        cutoff_date = date.today() - relativedelta(years=self.child_max_age)
        count = 0
        for membership in group.group_membership_ids:
            individual = membership.individual
            if individual.birthdate and individual.birthdate >= cutoff_date:
                count += 1
        return count

    def _calculate_amount(self, group):
        """Calculate entitlement amount for a household."""
        eligible_children = self._count_eligible_children(group)
        if self.max_children > 0:
            eligible_children = min(eligible_children, self.max_children)
        return self.base_amount + (self.per_child_amount * eligible_children)

    def prepare_entitlements(self, cycle, beneficiaries):
        """Create entitlement records for each beneficiary household."""
        existing_partner_ids = self.env["spp.entitlement"].search([
            ("cycle_id", "=", cycle.id),
        ]).mapped("partner_id.id")

        entitlement_vals = []
        for membership in beneficiaries:
            partner = membership.partner_id
            if partner.id in existing_partner_ids:
                continue

            amount = self._calculate_amount(partner)
            entitlement_vals.append({
                "cycle_id": cycle.id,
                "partner_id": partner.id,
                "initial_amount": amount,
                "state": "draft",
                "is_cash_entitlement": True,
            })

        entitlements = self.env["spp.entitlement"]
        if entitlement_vals:
            entitlements = self.env["spp.entitlement"].create(entitlement_vals)
        return entitlements

    def set_pending_validation_entitlements(self, cycle):
        """Move draft entitlements to pending validation."""
        entitlements = self.env["spp.entitlement"].search([
            ("cycle_id", "=", cycle.id),
            ("state", "=", "draft"),
        ])
        if entitlements:
            entitlements.write({"state": "pending_validation"})

    def validate_entitlements(self, cycle):
        """Approve pending entitlements."""
        entitlements = self.env["spp.entitlement"].search([
            ("cycle_id", "=", cycle.id),
            ("state", "in", ["draft", "pending_validation"]),
        ])
        if entitlements:
            return self.approve_entitlements(entitlements)

    def approve_entitlements(self, entitlements):
        """Approve entitlements and mark them ready for payment."""
        err_count = 0
        error_messages = []
        for entitlement in entitlements:
            try:
                entitlement.write({"state": "approved"})
            except Exception as e:
                err_count += 1
                error_messages.append(str(e))
        error_message = "\n".join(error_messages) if error_messages else ""
        return (err_count, error_message)

    def cancel_entitlements(self, cycle):
        """Cancel all non-final entitlements in the cycle."""
        entitlements = self.env["spp.entitlement"].search([
            ("cycle_id", "=", cycle.id),
            ("state", "in", ["draft", "pending_validation", "approved"]),
        ])
        if entitlements:
            entitlements.write({"state": "cancelled"})
```

Key points:

- `prepare_entitlements` is the core method — it creates one `spp.entitlement` record per beneficiary household
- The amount formula is `base_amount + (per_child_amount × min(eligible_children, max_children))`
- The other methods (`set_pending_validation_entitlements`, `validate_entitlements`, `approve_entitlements`, `cancel_entitlements`) handle the entitlement state machine
- `IS_CASH_ENTITLEMENT = True` tells the system this is a cash-type entitlement

## Cycle manager

The CCT cycle manager creates quarterly cycles aligned to calendar quarters.

### `models/cycle_manager_cct.py`

```python
import logging
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import _, fields, models

_logger = logging.getLogger(__name__)

QUARTER_START_MONTHS = {
    1: (1, 3),    # Q1: Jan-Mar
    2: (4, 6),    # Q2: Apr-Jun
    3: (7, 9),    # Q3: Jul-Sep
    4: (10, 12),  # Q4: Oct-Dec
}


class CCTCycleManager(models.Model):
    """Cycle manager that creates quarterly cycles aligned to Q1-Q4."""

    _name = "spp.cycle.manager.cct"
    _inherit = ["spp.base.cycle.manager", "spp.manager.source.mixin"]
    _description = "CCT Cycle Manager (Quarterly)"

    is_auto_copy_beneficiaries = fields.Boolean(
        string="Auto-Copy Beneficiaries",
        default=True,
        help="Automatically copy enrolled beneficiaries when creating a cycle.",
    )

    def _get_quarter(self, d):
        """Return the quarter number (1-4) for a date."""
        return (d.month - 1) // 3 + 1

    def _get_quarter_dates(self, year, quarter):
        """Return (start_date, end_date) for a given quarter."""
        start_month, end_month = QUARTER_START_MONTHS[quarter]
        start_date = date(year, start_month, 1)
        end_date = date(year, end_month, 1) + relativedelta(months=1, days=-1)
        return start_date, end_date

    def new_cycle(self, name, new_start_date, sequence):
        """Create a new quarterly cycle aligned to calendar quarters."""
        quarter = self._get_quarter(new_start_date)
        year = new_start_date.year
        start_date, end_date = self._get_quarter_dates(year, quarter)

        cycle = self.env["spp.cycle"].create({
            "name": name or f"Q{quarter} {year}",
            "program_id": self.program_id.id,
            "start_date": start_date,
            "end_date": end_date,
            "sequence": sequence,
        })

        if self.is_auto_copy_beneficiaries:
            self.copy_beneficiaries_from_program(cycle)

        return cycle
```

Key points:

- `new_cycle` overrides the default date calculation — instead of using recurrence rules, it snaps to calendar quarters
- When `is_auto_copy_beneficiaries` is enabled, enrolled beneficiaries are automatically added to the cycle on creation
- The remaining methods (`check_eligibility`, `prepare_entitlements`, `approve_cycle`, etc.) delegate to the program's other managers — see the full source in the download for all implementations

## Module structure

```
spp_cct_managers/
├── __init__.py
├── __manifest__.py
├── pyproject.toml
├── models/
│   ├── __init__.py
│   ├── eligibility_manager_cct.py    # CCT eligibility implementation
│   ├── eligibility_manager.py         # Registration in wrapper selection
│   ├── entitlement_manager_cct.py    # CCT entitlement implementation
│   ├── entitlement_manager.py         # Registration in wrapper selection
│   ├── cycle_manager_cct.py          # CCT cycle implementation
│   └── cycle_manager.py              # Registration in wrapper selection
├── views/
│   ├── eligibility_views.xml          # Eligibility config form
│   ├── entitlement_views.xml          # Entitlement config form
│   └── cycle_views.xml                # Cycle config form
├── security/
│   └── ir.model.access.csv
└── readme/
    └── DESCRIPTION.md
```

Notice the pattern: each manager type has an **implementation file** (the actual logic) and a **registration file** (extends the wrapper's selection). This keeps responsibilities separate and makes the code easier to navigate.

## Install and verify

```bash
spp stop
ODOO_INIT_MODULES=spp_cct_managers spp start --demo mis
```

Once running:

1. Navigate to **Programs** → create a new program
2. In the program wizard, you should see the new manager options:
   - Eligibility: **CCT Eligibility (Income + Children)**
   - Entitlement: **CCT Entitlement (Base + Per-Child)**
   - Cycle: **CCT Quarterly Cycle**
3. Configure each manager with your desired thresholds
4. Import and enroll beneficiaries
5. Create a cycle — it will auto-create a Q1/Q2/Q3/Q4 cycle based on the current date

{download}`Download the complete module </_static/samples/spp_cct_managers.zip>`

---
openspp:
  doc_status: draft
  products: [core]
---

# Tutorial: build CCT program managers

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

```text
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

## Step 1: module scaffold

Create the following directory structure:

```text
spp_cct_managers/
├── __init__.py
├── __manifest__.py
├── pyproject.toml
├── models/
│   ├── __init__.py
│   ├── eligibility_manager_cct.py
│   ├── eligibility_manager.py
│   ├── entitlement_manager_cct.py
│   ├── entitlement_manager.py
│   ├── cycle_manager_cct.py
│   └── cycle_manager.py
├── views/
│   ├── eligibility_views.xml
│   ├── entitlement_views.xml
│   └── cycle_views.xml
├── security/
│   └── ir.model.access.csv
└── tests/
    ├── __init__.py
    └── test_cct_managers.py
```

Notice the pattern: each manager type has an **implementation file** (the actual logic) and a **registration file** (extends the wrapper's selection). This keeps responsibilities separate.

### `__manifest__.py`

```python
{
    "name": "OpenSPP CCT Program Managers",
    "summary": "Custom managers for conditional cash transfer programs: "
    "income-based eligibility, per-child entitlements, and quarterly cycles.",
    "category": "OpenSPP",
    "version": "19.0.1.0.0",
    "author": "OpenSPP",
    "website": "https://openspp.org",
    "license": "LGPL-3",
    "depends": [
        "spp_programs",
        "spp_security",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/eligibility_views.xml",
        "views/entitlement_views.xml",
        "views/cycle_views.xml",
    ],
    "installable": True,
}
```

The module depends on `spp_programs` (for the base manager models) and `spp_security` (for the admin group used in access rules).

### `__init__.py` files

Root `__init__.py`:

```python
from . import models
```

### `pyproject.toml`

```toml
[project]
name = "odoo-addon-spp_cct_managers"
```

`models/__init__.py`:

```python
from . import eligibility_manager_cct
from . import eligibility_manager
from . import entitlement_manager_cct
from . import entitlement_manager
from . import cycle_manager_cct
from . import cycle_manager
```

`tests/__init__.py`:

```python
from . import test_cct_managers
```

## Step 2: eligibility manager

The eligibility manager filters households based on two criteria: income at or below a threshold, and at least one child under a configurable age.

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

**Key patterns to notice:**

- The private method `_get_eligible_group_ids()` contains the core logic, reused by all three interface methods
- It searches for groups (households) where `income <= max_income`
- Then filters to those with at least one member whose `birthdate` makes them younger than `child_max_age`
- The `import_eligible_registrants` method avoids creating duplicate memberships

### `models/eligibility_manager.py`

Each manager needs a registration file that adds it to the wrapper model's selection dropdown:

```python
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

## Step 3: entitlement manager

The entitlement manager calculates transfer amounts based on household composition: a base amount per household plus a per-child top-up, capped at a configurable maximum.

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

**Key patterns to notice:**

- `prepare_entitlements` is the core method — it creates one `spp.entitlement` record per beneficiary household
- The amount formula is `base_amount + (per_child_amount × min(eligible_children, max_children))`
- The other methods (`set_pending_validation_entitlements`, `validate_entitlements`, `approve_entitlements`, `cancel_entitlements`) handle the entitlement state machine
- `IS_CASH_ENTITLEMENT = True` tells the system this is a cash-type entitlement

### `models/entitlement_manager.py`

```python
from odoo import api, models


class EntitlementManagerRegistration(models.Model):
    _inherit = "spp.entitlement.manager"

    @api.model
    def _selection_manager_ref_id(self):
        selection = super()._selection_manager_ref_id()
        new_manager = (
            "spp.program.entitlement.manager.cct",
            "CCT Entitlement (Base + Per-Child)",
        )
        if new_manager not in selection:
            selection.append(new_manager)
        return selection
```

## Step 4: cycle manager

The cycle manager creates quarterly cycles aligned to calendar quarters, optionally auto-copying enrolled beneficiaries into each new cycle.

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

**Key patterns to notice:**

- `new_cycle` overrides the default date calculation — instead of using recurrence rules, it snaps to calendar quarters
- When `is_auto_copy_beneficiaries` is enabled, enrolled beneficiaries are automatically added to the cycle on creation
- The cycle manager base class requires you to implement several workflow methods. For most CCT programs, these delegate to the program's other managers. The complete set is in the downloadable module — the key ones are `check_eligibility`, `prepare_entitlements`, `validate_entitlements`, and `approve_cycle`
- The `approve_cycle()` method is called automatically when a cycle is approved through the approval workflow. If the cycle manager's `auto_approve_entitlements` flag is enabled, it also triggers auto-approval of all pending entitlements. See the {doc}`building_managers` page for the full approval flow

### `models/cycle_manager.py`

```python
from odoo import api, models


class CycleManagerRegistration(models.Model):
    _inherit = "spp.cycle.manager"

    @api.model
    def _selection_manager_ref_id(self):
        selection = super()._selection_manager_ref_id()
        new_manager = (
            "spp.cycle.manager.cct",
            "CCT Quarterly Cycle",
        )
        if new_manager not in selection:
            selection.append(new_manager)
        return selection
```

## Step 5: views

Each manager needs a form view so administrators can configure it. These are simple forms with grouped fields.

### `views/eligibility_views.xml`

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <record id="view_eligibility_manager_cct_form" model="ir.ui.view">
        <field name="name">spp.program.membership.manager.cct.form</field>
        <field name="model">spp.program.membership.manager.cct</field>
        <field name="arch" type="xml">
            <form string="CCT Eligibility Manager">
                <sheet>
                    <group>
                        <group string="Configuration">
                            <field name="name" />
                            <field name="program_id" readonly="1" />
                        </group>
                        <group string="Eligibility Criteria">
                            <field name="max_income" />
                            <field name="child_max_age" />
                        </group>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
```

### `views/entitlement_views.xml`

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <record id="view_entitlement_manager_cct_form" model="ir.ui.view">
        <field name="name">spp.program.entitlement.manager.cct.form</field>
        <field name="model">spp.program.entitlement.manager.cct</field>
        <field name="arch" type="xml">
            <form string="CCT Entitlement Manager">
                <sheet>
                    <group>
                        <group string="Configuration">
                            <field name="name" />
                            <field name="program_id" readonly="1" />
                        </group>
                        <group string="Amounts">
                            <field name="base_amount" />
                            <field name="per_child_amount" />
                            <field name="max_children" />
                            <field name="child_max_age" />
                            <field name="currency_id" invisible="1" />
                        </group>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
```

### `views/cycle_views.xml`

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <record id="view_cycle_manager_cct_form" model="ir.ui.view">
        <field name="name">spp.cycle.manager.cct.form</field>
        <field name="model">spp.cycle.manager.cct</field>
        <field name="arch" type="xml">
            <form string="CCT Cycle Manager">
                <sheet>
                    <group>
                        <group string="Configuration">
                            <field name="name" />
                            <field name="program_id" readonly="1" />
                        </group>
                        <group string="Cycle Behavior">
                            <field name="is_auto_copy_beneficiaries" />
                        </group>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
```

## Step 6: security

Each manager model needs access rules. The CCT managers are configured by program administrators:

### `security/ir.model.access.csv`

```text
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_spp_eligibility_cct_system,CCT Eligibility System,model_spp_program_membership_manager_cct,base.group_system,1,1,1,1
access_spp_eligibility_cct_admin,CCT Eligibility Admin,model_spp_program_membership_manager_cct,spp_security.group_spp_admin,1,1,1,1
access_spp_entitlement_cct_system,CCT Entitlement System,model_spp_program_entitlement_manager_cct,base.group_system,1,1,1,1
access_spp_entitlement_cct_admin,CCT Entitlement Admin,model_spp_program_entitlement_manager_cct,spp_security.group_spp_admin,1,1,1,1
access_spp_cycle_cct_system,CCT Cycle System,model_spp_cycle_manager_cct,base.group_system,1,1,1,1
access_spp_cycle_cct_admin,CCT Cycle Admin,model_spp_cycle_manager_cct,spp_security.group_spp_admin,1,1,1,1
```

## Step 7: tests

Tests verify that the eligibility logic filters correctly and the entitlement calculation produces expected amounts.

### `tests/test_cct_managers.py`

```python
"""Tests for CCT program managers."""

from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import fields
from odoo.tests import TransactionCase


class TestCCTEligibility(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        Partner = cls.env["res.partner"]

        # Create a household with one adult and one child
        cls.household = Partner.create({
            "name": "Test Household",
            "is_registrant": True,
            "is_group": True,
            "income": 5000.0,
        })
        cls.adult = Partner.create({
            "name": "Adult Member",
            "is_registrant": True,
            "is_group": False,
            "birthdate": date.today() - relativedelta(years=30),
        })
        cls.child = Partner.create({
            "name": "Child Member",
            "is_registrant": True,
            "is_group": False,
            "birthdate": date.today() - relativedelta(years=5),
        })
        cls.env["spp.group.membership"].create({
            "group": cls.household.id,
            "individual": cls.adult.id,
            "start_date": fields.Datetime.now(),
        })
        cls.env["spp.group.membership"].create({
            "group": cls.household.id,
            "individual": cls.child.id,
            "start_date": fields.Datetime.now(),
        })

        # Create eligibility manager
        cls.program = cls.env["spp.program"].create({
            "name": "Test CCT Program",
        })
        cls.eligibility = cls.env[
            "spp.program.membership.manager.cct"
        ].create({
            "name": "Test CCT Eligibility",
            "program_id": cls.program.id,
            "max_income": 10000.0,
            "child_max_age": 18,
        })

    def test_eligible_household_found(self):
        """Household with income under threshold and a child is eligible."""
        eligible_ids = self.eligibility._get_eligible_group_ids()
        self.assertIn(self.household.id, eligible_ids)

    def test_high_income_excluded(self):
        """Household with income above threshold is not eligible."""
        self.household.write({"income": 20000.0})
        eligible_ids = self.eligibility._get_eligible_group_ids()
        self.assertNotIn(self.household.id, eligible_ids)

    def test_no_children_excluded(self):
        """Household with only adults is not eligible."""
        # Age the child past the threshold
        self.child.write({
            "birthdate": date.today() - relativedelta(years=25),
        })
        eligible_ids = self.eligibility._get_eligible_group_ids()
        self.assertNotIn(self.household.id, eligible_ids)

    def test_import_no_duplicates(self):
        """Importing twice does not create duplicate memberships."""
        count_1 = self.eligibility.import_eligible_registrants()
        count_2 = self.eligibility.import_eligible_registrants()
        self.assertGreater(count_1, 0)
        self.assertEqual(count_2, 0, "Second import should find no new registrants")


class TestCCTEntitlement(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        Partner = cls.env["res.partner"]

        cls.household = Partner.create({
            "name": "Entitlement Household",
            "is_registrant": True,
            "is_group": True,
        })
        # Create 3 children
        for i in range(3):
            child = Partner.create({
                "name": f"Child {i+1}",
                "is_registrant": True,
                "is_group": False,
                "birthdate": date.today() - relativedelta(years=5 + i),
            })
            cls.env["spp.group.membership"].create({
                "group": cls.household.id,
                "individual": child.id,
                "start_date": fields.Datetime.now(),
            })

        cls.program = cls.env["spp.program"].create({
            "name": "Test CCT Program",
        })
        cls.entitlement_mgr = cls.env[
            "spp.program.entitlement.manager.cct"
        ].create({
            "name": "Test CCT Entitlement",
            "program_id": cls.program.id,
            "base_amount": 1000.0,
            "per_child_amount": 500.0,
            "max_children": 5,
            "child_max_age": 18,
        })

    def test_amount_calculation(self):
        """Amount = base + (per_child * children)."""
        amount = self.entitlement_mgr._calculate_amount(self.household)
        # 1000 + (500 * 3 children) = 2500
        self.assertEqual(amount, 2500.0)

    def test_max_children_cap(self):
        """Per-child top-up is capped at max_children."""
        self.entitlement_mgr.write({"max_children": 2})
        amount = self.entitlement_mgr._calculate_amount(self.household)
        # 1000 + (500 * 2 capped) = 2000
        self.assertEqual(amount, 2000.0)

    def test_no_cap_when_zero(self):
        """max_children=0 means no cap."""
        self.entitlement_mgr.write({"max_children": 0})
        amount = self.entitlement_mgr._calculate_amount(self.household)
        # 1000 + (500 * 3 children) = 2500
        self.assertEqual(amount, 2500.0)
```

**Key patterns to notice:**

- `setUpClass` creates shared test data (households, members, managers)
- Eligibility tests verify both inclusion and exclusion criteria
- Entitlement tests verify the amount formula, the cap, and the no-cap edge case
- Each test is independent — modifying data in one test does not affect others

## Verify it works

### Run the tests

```bash
odoo-bin --test-enable --stop-after-init -i spp_cct_managers -d openspp
```

This installs the module, runs the test suite, and exits. All tests should pass.

### Manual verification

Start the environment (the `spp` CLI is installed as part of the development environment — see {doc}`../setup/index`):

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

## What's next

You now have a working set of custom managers. To go further:

- {doc}`manager_pattern` — understand the wrapper/implementation architecture in depth
- {doc}`building_managers` — reference for the base class methods and registration patterns

## See also

- {doc}`/developer_guide/change_request_types/index` — building custom change request types (similar tutorial pattern)

{download}`Download the complete module </_static/samples/spp_cct_managers.zip>`

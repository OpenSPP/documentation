---
openspp:
  doc_status: unverified
  products: [core]
---

# Adding custom fields and using them in variables/expressions

Custom fields let you capture additional information for your deployment. Once a field exists, you can immediately use it in:

- Studio **variables** (field-based variables)
- Studio **expressions**
- Scoring indicators (direct field paths, mappings, or CEL formulas)

This guide focuses on the recommended pattern: **add a field → expose it in the UI → reference it via variables/expressions**.

## 1) Add the field

OpenSPP registrants (individuals and groups/households) extend `res.partner`. They are commonly differentiated by flags such as:

- `is_registrant`
- `is_group` (group/household vs individual)

You can add fields either:

- via **Studio** (creates fields named `x_...`), or
- via a custom module (recommended for version-controlled deployments)

Example (custom module): add a field to `res.partner`:

```python
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_disability_level = fields.Integer(string="Disability Level")
```

## 2) Expose the field in the UI (optional)

If the field should be visible/editable on registry forms or list views, extend the corresponding views in your custom module.

## 3) Create a variable for the field (recommended)

Create a field-based variable in **Studio → Variables**:

- **Source Type**: Model Field
- **Source Model**: typically `res.partner`
- **Source Field**: your field name (for example `x_disability_level`)
- **CEL Accessor**: a stable identifier you want to use in expressions (for example `disability_level`)
- **Applies To**: individual, group/household, or both

Now you can reference it in expressions as:

```text
disability_level >= 3
```

## 4) Use it in expressions and features

Once the variable exists, you can reuse it in:

- program eligibility / compliance rules (compile-to-domain)
- scoring formulas (including CEL Formula indicators)
- validations and workflow rules (runtime evaluation screens, where applicable)

See {doc}`/config_guide/variables/index` and {doc}`/config_guide/cel/index`.

```{note}
For complex derived values (counts, sums, “children under 5”, event-based queries), prefer Studio aggregate variables and event aggregation variables instead of implementing custom computed fields.
```
import logging

from dateutil.relativedelta import relativedelta
from odoo.tests import tagged
from odoo.tests.common import TransactionCase

_logger = logging.getLogger(__name__)

@tagged("post_install", "-at_install")
class ComputeIndicatorFieldsTest(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(
            context=dict(
                cls.env.context,
                test_queue_job_no_delay=True,
            )
        )

        # Initial Setup of Variables
        cls.registrant_1 = cls.env["res.partner"].create(
            {
                "name": "Heidi Jaddranka",
                "is_group": False,
                "is_registrant": True,
                "gender": "Female",
                "birthdate": datetime.datetime.now(),
                "z_cst_indv_disability_level": 5,
            }
        )
        cls.registrant_2 = cls.env["res.partner"].create

        (
            {
                "name": "Angus Kleitos",
                "is_group": False,
                "is_registrant": True,
                "gender": "Male",
                "birthdate": datetime.datetime.now(),
                "z_cst_indv_disability_level": 10,
            }
        )
        cls.group_1 = cls.env["res.partner"].create(
            {
                "name": "Group 1",
                "is_group": True,
                "is_registrant": True,
            }
        )
        members1 = [
            {"individual": cls.registrant_1.id},
            {"individual": cls.registrant_2.id}
        ]
        group1_members = [[0, 0, val] for val in members1]
        cls.group_1.write({"group_membership_ids": group1_members})

    def test_01_num_children(self):
        self.group_1._compute_ind_grp_num_children()
        self.assertEqual(
            self.group_1.z_ind_grp_num_children,
            2,
        )

    def test_02_num_elderly(self):
        now = datetime.datetime.now()
        birthdate = now - relativedelta(years=66)
        self.registrant_1.write({"birthdate": birthdate})
        self.group_1._compute_ind_grp_num_elderly()
        self.assertEqual(
            self.group_1.z_ind_grp_num_elderly,
            1,
        )

    def test_03_num_adults_female_not_elderly(self):
        now = datetime.datetime.now()
        birthdate = now - relativedelta(years=30)
        self.registrant_1.write({"birthdate": birthdate})
        self.group_1._compute_ind_grp_num_adults_female_not_elderly()
        self.assertEqual(
            self.group_1.z_ind_grp_num_adults_female_not_elderly,
            1,
        )

    def test_04_num_adults_male_not_elderly(self):
        now = datetime.datetime.now()
        birthdate = now - relativedelta(years=30)
        self.registrant_2.write({"birthdate": birthdate})
        self.group_1._compute_ind_grp_num_adults_male_not_elderly()
        self.assertEqual(
            self.group_1.z_ind_grp_num_adults_male_not_elderly,
            1,
        )
```

By writing and running these tests, you can ensure that your custom fields and indicators work correctly within OpenSPP. This approach helps maintain the system's integrity and reliability as you implement customizations.

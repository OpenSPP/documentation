---
openspp:
  doc_status: draft
  products: [core]
---

# Example: custom registry fields

**For: developers**

This tutorial walks you through building a complete OpenSPP module from scratch. You will create a module that adds two custom fields to the individual registry: **education level** and **head of household**.

By the end, you will have a working module that demonstrates all the patterns covered in this section — manifest, models, security, views, and tests.

```{tip}
Want to skip ahead? Download the complete module: {download}`spp_custom_registry_fields.zip </_static/samples/spp_custom_registry_fields.zip>`
```

## What you will build

| Field | Type | Purpose |
|-------|------|---------|
| `education_level_id` | Many2one (vocabulary code) | Highest education level completed |
| `is_head_of_household` | Boolean | Whether the individual is head of their household |

## Prerequisites

- A running development environment (see {doc}`../setup/index`)
- The `spp_registry` module installed (included in all demo profiles)

## Step 1: Create the module scaffold

Create the directory structure:

```bash
mkdir -p spp_custom_registry_fields/{models,views,security,tests,readme}
```

### `__manifest__.py`

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenSPP Custom Registry Fields",
    "summary": "Adds education level and head of household fields to the individual registry.",
    "category": "OpenSPP/Configuration",
    "version": "19.0.2.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/OpenSPP2",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": [],
    "depends": [
        "spp_registry",
        "spp_security",
        "spp_vocabulary",
    ],
    "data": [
        # Security (must be first)
        "security/groups.xml",
        "security/ir.model.access.csv",
        # Views
        "views/individual_views.xml",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
```

Note the dependencies:

- `spp_registry` — provides the individual registry we are extending
- `spp_security` — provides the `group_spp_admin` group we link to
- `spp_vocabulary` — provides `spp.vocabulary.code` for the education level field

### `pyproject.toml`

```toml
[build-system]
requires = ["whool"]
build-backend = "whool.buildapi"
```

### `__init__.py`

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from . import models
```

### `models/__init__.py`

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from . import individual
```

## Step 2: Define the model

We are not creating a new model — we are extending the existing `res.partner` model used by the registry. This adds our fields to the existing database table.

### `models/individual.py`

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartnerCustomFields(models.Model):
    """Add custom fields to the individual registry.

    Extends res.partner to add education level and head of household
    tracking for individual registrants.
    """

    _inherit = "res.partner"

    education_level_id = fields.Many2one(
        "spp.vocabulary.code",
        string="Education Level",
        domain="[('namespace_uri', '=', 'urn:openspp:vocab:education-level')]",
        help="Highest level of education completed.",
    )

    is_head_of_household = fields.Boolean(
        string="Head of Household",
        default=False,
        help="Whether this individual is the head of their household.",
    )
```

Key points:

- We use `_inherit = "res.partner"` without `_name` — this extends the existing model
- `education_level_id` ends with `_id` (Many2one naming rule)
- `is_head_of_household` starts with `is_` (Boolean naming rule)
- The `domain` filter on `education_level_id` restricts the dropdown to codes from the "Education Level" vocabulary
- We use `spp.vocabulary.code` instead of a hardcoded `Selection` field — this allows the education levels to be configured without code changes

## Step 3: Set up security

### `security/groups.xml`

This follows the three-tier pattern. Since our module only adds fields to an existing model (not a new model), we use a simplified version with viewer and manager roles:

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <!-- Custom Registry Fields Security Groups -->

    <!-- Technical Groups (Tier 3) -->
    <record id="group_custom_fields_read" model="res.groups">
        <field name="name">Custom Registry Fields: Read</field>
        <field name="comment">Technical group for read access to custom registry fields.</field>
    </record>

    <record id="group_custom_fields_write" model="res.groups">
        <field name="name">Custom Registry Fields: Write</field>
        <field name="comment">Technical group for write access to custom registry fields.</field>
        <field name="implied_ids" eval="[Command.link(ref('group_custom_fields_read'))]" />
    </record>

    <!-- User-Facing Groups (Tier 2) -->

    <!-- Viewer: read-only access to custom fields -->
    <record id="privilege_custom_fields_viewer" model="res.groups.privilege">
        <field name="name">Viewer</field>
        <field name="category_id" ref="spp_security.category_spp_admin" />
        <field name="sequence">200</field>
    </record>

    <record id="group_custom_fields_viewer" model="res.groups">
        <field name="name">Custom Registry Fields Viewer</field>
        <field name="privilege_id" ref="privilege_custom_fields_viewer" />
        <field name="comment">Can view custom registry fields but cannot modify them.</field>
        <field name="implied_ids" eval="[Command.link(ref('group_custom_fields_read'))]" />
    </record>

    <!-- Manager: can edit custom fields on registrants -->
    <record id="privilege_custom_fields_manager" model="res.groups.privilege">
        <field name="name">Manager</field>
        <field name="category_id" ref="spp_security.category_spp_admin" />
        <field name="sequence">210</field>
    </record>

    <record id="group_custom_fields_manager" model="res.groups">
        <field name="name">Custom Registry Fields Manager</field>
        <field name="privilege_id" ref="privilege_custom_fields_manager" />
        <field name="comment">Can edit custom fields on registrant records.</field>
        <field name="implied_ids" eval="[
            Command.link(ref('group_custom_fields_write')),
            Command.link(ref('group_custom_fields_viewer')),
        ]" />
    </record>

    <!-- Link Manager to SPP Admin -->
    <record id="spp_security.group_spp_admin" model="res.groups">
        <field name="implied_ids" eval="[Command.link(ref('group_custom_fields_manager'))]" />
    </record>
</odoo>
```

### `security/ir.model.access.csv`

Since we are extending `res.partner` (not creating a new model), the ACL grants field-level access through the existing model:

```text
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_res_partner_custom_fields_viewer,Partner Custom Fields Viewer,base.model_res_partner,group_custom_fields_viewer,1,0,0,0
access_res_partner_custom_fields_manager,Partner Custom Fields Manager,base.model_res_partner,group_custom_fields_manager,1,1,0,0
```

`res.partner` is defined by the `base` module, so the `model_id` reference is always `base.model_res_partner` — even when `spp_registry` has extended it with additional fields. Using `spp_registry.model_res_partner` would fail at install time because that external ID does not exist.

## Step 4: Create the view

We extend the existing individual form view using XPath to inject our fields into the Demographics section.

### `views/individual_views.xml`

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <!-- Extend Individual Form View: add custom fields to Demographics section -->
    <record id="view_individual_custom_fields_form" model="ir.ui.view">
        <field name="name">spp.custom.registry.fields.individual.form</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="spp_registry.view_individuals_form" />
        <field name="arch" type="xml">
            <!-- Add education level after the occupation field in Demographics -->
            <xpath expr="//group[@name='demographics_section']/group[field[@name='occupation_id']]" position="after">
                <group>
                    <field
                        name="education_level_id"
                        readonly="disabled"
                        options="{'no_create': True, 'no_create_edit': True}"
                    />
                </group>
                <group>
                    <field name="is_head_of_household" readonly="disabled" />
                </group>
            </xpath>
        </field>
    </record>
</odoo>
```

Key points:

- `inherit_id` references the original form view we are extending
- The XPath targets the occupation field's `<group>` wrapper inside `demographics_section` and adds our fields after it
- `readonly="disabled"` follows the registry pattern — the field respects the form's overall edit mode
- `options="{'no_create': True, 'no_create_edit': True}"` prevents users from creating new vocabulary codes from the dropdown (codes should be managed through the vocabulary system)

## Step 5: Write tests

### `tests/__init__.py`

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from . import common
from . import test_custom_fields
```

### `tests/common.py`

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from odoo import Command
from odoo.tests.common import TransactionCase


class CustomFieldsTestCommon(TransactionCase):
    """Common test setup for spp_custom_registry_fields tests."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Create an "Education Level" vocabulary and codes
        cls.vocab_education = cls.env["spp.vocabulary"].create({
            "name": "Education Level",
        })

        cls.education_primary = cls.env["spp.vocabulary.code"].create({
            "vocabulary_id": cls.vocab_education.id,
            "name": "Primary",
        })

        cls.education_secondary = cls.env["spp.vocabulary.code"].create({
            "vocabulary_id": cls.vocab_education.id,
            "name": "Secondary",
        })

        cls.education_tertiary = cls.env["spp.vocabulary.code"].create({
            "vocabulary_id": cls.vocab_education.id,
            "name": "Tertiary",
        })

        # Create test users with different access levels
        base_user_group = cls.env.ref("base.group_user")

        cls.user_viewer = cls.env["res.users"].create({
            "name": "Registry Viewer",
            "login": "custom_fields_viewer",
            "email": "viewer@test.com",
            "group_ids": [
                Command.link(base_user_group.id),
                Command.link(
                    cls.env.ref(
                        "spp_custom_registry_fields.group_custom_fields_viewer"
                    ).id
                ),
            ],
        })

        cls.user_manager = cls.env["res.users"].create({
            "name": "Registry Manager",
            "login": "custom_fields_manager",
            "email": "manager@test.com",
            "group_ids": [
                Command.link(base_user_group.id),
                Command.link(
                    cls.env.ref(
                        "spp_custom_registry_fields.group_custom_fields_manager"
                    ).id
                ),
            ],
        })

    def _create_test_individual(self, **kwargs):
        """Create a test individual registrant.

        Args:
            **kwargs: Override default field values.

        Returns:
            res.partner: Created individual record.
        """
        default_vals = {
            "name": "Test Individual",
            "is_registrant": True,
            "is_group": False,
        }
        default_vals.update(kwargs)
        return self.env["res.partner"].create(default_vals)
```

### `tests/test_custom_fields.py`

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from odoo.tests import tagged

from .common import CustomFieldsTestCommon


@tagged("post_install", "-at_install")
class TestCustomRegistryFields(CustomFieldsTestCommon):
    """Tests for custom registry fields on individual registrants."""

    def test_create_individual_with_education_level(self):
        """Test creating an individual with an education level."""
        individual = self._create_test_individual(
            education_level_id=self.education_secondary.id,
        )

        self.assertEqual(individual.education_level_id, self.education_secondary)

    def test_create_individual_with_head_of_household(self):
        """Test creating an individual marked as head of household."""
        individual = self._create_test_individual(
            is_head_of_household=True,
        )

        self.assertTrue(individual.is_head_of_household)

    def test_default_head_of_household_is_false(self):
        """Test that head of household defaults to False."""
        individual = self._create_test_individual()

        self.assertFalse(individual.is_head_of_household)

    def test_update_education_level(self):
        """Test updating an individual's education level."""
        individual = self._create_test_individual(
            education_level_id=self.education_primary.id,
        )

        individual.write({
            "education_level_id": self.education_tertiary.id,
        })

        self.assertEqual(individual.education_level_id, self.education_tertiary)
```

## Step 6: Install and verify

Copy the module to your OpenSPP addons directory and install it:

```bash
spp stop
ODOO_INIT_MODULES=spp_custom_registry_fields spp start
```

Once Odoo is running:

1. Navigate to **Registry** in the main menu
2. Open any individual record
3. Scroll to the **Demographics** section
4. You should see the new **Education Level** and **Head of Household** fields

To run the tests:

```bash
spp test spp_custom_registry_fields
```

## Complete file listing

```
spp_custom_registry_fields/
├── __init__.py
├── __manifest__.py
├── pyproject.toml
├── models/
│   ├── __init__.py
│   └── individual.py
├── views/
│   └── individual_views.xml
├── security/
│   ├── groups.xml
│   └── ir.model.access.csv
├── tests/
│   ├── __init__.py
│   ├── common.py
│   └── test_custom_fields.py
└── readme/
    └── DESCRIPTION.md
```

{download}`Download the complete module </_static/samples/spp_custom_registry_fields.zip>`

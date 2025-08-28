---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Indicators

This article guides you through understanding and customizing indicators in OpenSPP, using a practical scenario and a working example. Indicators are computed fields that provide dynamic, calculated values based on registrant data, essential for social protection programs to track demographic information, eligibility criteria, and program outcomes.

**Field Naming Conventions**

OpenSPP uses systematic field naming prefixes to categorize different types of indicators:

- `z_ind_`: Prefix for all indicator fields
- `grp`: Group-level indicators (households, families)
- `indv`: Individual-level indicators
- `cst`: Custom/arbitrary indicators

Examples:
- `z_ind_grp_num_children`: Number of children in a group
- `z_ind_indv_age_years`: Age in years for an individual
- `z_ind_grp_is_single_head_hh`: Boolean indicating single-headed household

**Indicator Types**

1. **Count Indicators**: Count records matching specific criteria
2. **Boolean Indicators**: True/false flags based on conditions
3. **Computed Indicators**: Calculated values from other fields

## Prerequisites

- Solid understanding of Odoo 17 module development, including Python, XML, and XPath.
- OpenSPP modules "g2p_registry_group", "g2p_registry_individual", and "spp_custom_field" must be installed.
- To set up OpenSPP for development, please refer to the {doc}`Development Setup Guide <setup>`.

## Module Structure

A typical custom indicators module follows the standard Odoo module structure. Here’s an example for `spp_custom_indicators`:

```
spp_custom_indicators/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── res_partner.py
└── security/
    └── ir.model.access.csv
```

## Step-by-Step Guide

### Step 1: Create the Module Scaffold

Create a new directory for your module (e.g., `spp_custom_indicators`) and populate it with the basic Odoo module files and structure shown above.

### Step 2: Define Module Manifest

Create a manifest file that includes the proper dependencies:

```python
{
    "name": "OpenSPP Custom Indicators",
    "summary": "Adds custom indicators to registrants (res.partner)",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "author": "Your Organization",
    "website": "https://your-website.com",
    "license": "LGPL-3",
    "depends": [
        "g2p_registry_group",
        "g2p_registry_individual",
        "spp_custom_field",
    ],
    "data": [
        # No need for view XML if using spp_custom_field
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
```

### Step 3: Extend the res.partner Model

Create `models/res_partner.py` to add your indicators and import it in `models/__init__.py`:

```python
from odoo import fields, models
import datetime
from dateutil.relativedelta import relativedelta

class G2PRegistrant(models.Model):
    _inherit = "res.partner"

    # Count indicator example
    z_ind_grp_num_children = fields.Integer(
        string="Number of children",
        compute="_compute_ind_grp_num_children",
        help="Number of children in the group",
        store=True,
        allow_filter=True,
    )

    # Boolean indicator example
    z_ind_grp_is_single_head_hh = fields.Boolean(
        string="Is single-headed household",
        compute="_compute_ind_grp_is_single_head_hh",
        help="Single-headed HH - extracted from demographic data of HH adult members",
        store=True,
        allow_filter=True,
    )

    # Individual indicator example
    z_ind_indv_age_years = fields.Integer(
        string="Age (years)",
        compute="_compute_ind_indv_age_years",
        store=True,
        help="Computed age in years for individuals",
    )

    def _compute_ind_grp_num_children(self):
        """Compute the number of children in the group"""
        now = datetime.datetime.now()
        children = now - relativedelta(years=18)
        domain = [("birthdate", ">=", children)]
        self.compute_count_and_set_indicator("z_ind_grp_num_children", None, domain)

    def _compute_ind_grp_is_single_head_hh(self):
        """Compute if this is a single-headed household"""
        now = datetime.datetime.now()
        domain = [("birthdate", "<", now - relativedelta(years=18))]
        self.compute_count_and_set_indicator("z_ind_grp_is_single_head_hh", None, domain, presence_only=True)

    def _compute_ind_indv_age_years(self):
        """Compute age in years for individuals"""
        today = fields.Date.context_today(self)
        for partner in self:
            if partner.is_group or not partner.birthdate:
                partner.z_ind_indv_age_years = 0
                continue
            age = today.year - partner.birthdate.year - (
                (today.month, today.day) < (partner.birthdate.month, partner.birthdate.day)
            )
            partner.z_ind_indv_age_years = max(age, 0)
```

### Step 4: Add Security Access (Optional)

If you introduce new models, add access rights. For simple field additions, this is not required. Example:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_spp_custom_indicator_admin,spp.custom.indicator.admin,spp_custom_indicators.model_g2pregistrant,g2p_registry_base.group_g2p_admin,1,1,1,1
```

### Step 5: Add More Indicators (Optional)

You can add more complex indicators, such as those based on gender, disability, or custom fields. Use the provided helper method for consistency and performance:

```python
def compute_count_and_set_indicator(self, field_name, membership_kinds, domain, presence_only=False):
    """
    Helper method to compute and set indicator values
    """
    # ...implementation provided by OpenSPP base modules...
```

#### Example: Elderly and Gender-Based Indicators

```python
def _compute_ind_grp_num_elderly(self):
    now = datetime.datetime.now()
    domain = [("birthdate", "<", now - relativedelta(years=65))]
    self.compute_count_and_set_indicator("z_ind_grp_num_elderly", None, domain)

def _compute_ind_grp_num_adults_female_not_elderly(self):
    now = datetime.datetime.now()
    domain = [
        ("birthdate", ">=", now - relativedelta(years=65)),
        ("birthdate", "<", now - relativedelta(years=18)),
        ("gender", "=", "Female"),
    ]
    self.compute_count_and_set_indicator("z_ind_grp_num_adults_female_not_elderly", None, domain)
```

#### Example: Disability Indicators

```python
def _compute_ind_grp_num_disability(self):
    domain = [("z_cst_indv_disability_level", ">", 0)]
    self.compute_count_and_set_indicator("z_ind_grp_num_disability", None, domain)

def _compute_ind_grp_is_hh_with_disabled(self):
    domain = [("z_cst_indv_disability_level", ">", 0)]
    self.compute_count_and_set_indicator("z_ind_grp_is_hh_with_disabled", None, domain, presence_only=True)
```

### Step 6: Add Constraints, and Validations (Optional)

You can add additional constraints for indicator logic:

```python
from odoo import api, ValidationError

    @api.constrains("z_ind_grp_num_children")
    def _check_num_children_positive(self):
        for record in self:
            if record.z_ind_grp_num_children is not None and record.z_ind_grp_num_children < 0:
                raise ValidationError("Number of children cannot be negative.")
```

### Step 7: Install and Test

1. Install or upgrade the module through the Apps menu.
2. Open the Individual and Group registries and verify the new indicators display in form views (handled automatically by `spp_custom_field`).
3. Create or update records and ensure the indicators compute correctly.
4. Test filtering and searching by indicator values.

## Best Practices

- Use `store=True` for indicators that need to be queried.
- Use `allow_filter=True` for indicators that should be filterable in views.
- Provide clear help text explaining the indicator's purpose.

## References

- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Documentation](https://docs.openspp.org/)
- Registry modules: `g2p_registry_group`, `g2p_registry_individual`
- Example implementations: `g2p_connect_demo`
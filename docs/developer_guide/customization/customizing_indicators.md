---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Creating Indicators in OpenSPP

Indicators in OpenSPP are computed fields that provide dynamic, calculated values based on registrant data. They are essential for social protection programs to track demographic information, eligibility criteria, and program outcomes. This guide shows how to create indicators following OpenSPP conventions and patterns.

## Understanding OpenSPP Indicators

### Field Naming Conventions

OpenSPP uses systematic field naming prefixes to categorize different types of indicators:

- `z_ind_`: Prefix for all indicator fields
- `grp`: Group-level indicators (households, families)
- `indv`: Individual-level indicators
- `cst`: Custom/arbitrary indicators

Examples:
- `z_ind_grp_num_children`: Number of children in a group
- `z_ind_indv_age_years`: Age in years for an individual
- `z_ind_grp_is_single_head_hh`: Boolean indicating single-headed household

### Indicator Types

1. **Count Indicators**: Count records matching specific criteria
2. **Boolean Indicators**: True/false flags based on conditions
3. **Computed Indicators**: Calculated values from other fields

## Creating Indicators in a Module

In this scenario, we create a module that adds indicators to both Individual and Group registries. This follows the same pattern as custom fields but focuses on computed indicators.

> **Note:**  
> If you use the `spp_custom_field` module, all fields defined on the model will be automatically exposed in the UI. You do **not** need to manually extend views.

### 1. Create Module Structure

Create a new module following the OpenSPP module structure:

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

### 2. Define Module Manifest

Declare the dependency on `spp_custom_field` (and registry modules):

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
        "spp_custom_field",  # Ensure this is included
    ],
    "data": [
        # No need for view XML if using spp_custom_field
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
```

### 3. Extend the res.partner Model

Create `models/res_partner.py` to add your indicators and import it in `models/__init__.py`.

```python
from odoo import fields, models
import datetime
from dateutil.relativedelta import relativedelta

class G2PRegistrant(models.Model):
    _inherit = "res.partner"

    # Count indicator example
    z_ind_grp_num_children = fields.Integer(
        "Number of children",
        compute="_compute_ind_grp_num_children",
        help="Number of children in the group",
        store=True,
        allow_filter=True,
    )

    # Boolean indicator example
    z_ind_grp_is_single_head_hh = fields.Boolean(
        "Is single-headed household",
        compute="_compute_ind_grp_is_single_head_hh",
        help="Single-headed HH - extracted from demographic data of HH adult members",
        store=True,
        allow_filter=True,
    )

    # Individual indicator example
    z_ind_indv_age_years = fields.Integer(
        "Age (years)",
        compute="_compute_ind_indv_age_years",
        store=True,
        help="Computed age in years for individuals",
    )

    def _compute_ind_grp_num_children(self):
        """
        Compute the number of children in the group
        """
        now = datetime.datetime.now()
        children = now - relativedelta(years=18)  # Children under 18
        domain = [("birthdate", ">=", children)]
        self.compute_count_and_set_indicator("z_ind_grp_num_children", None, domain)

    def _compute_ind_grp_is_single_head_hh(self):
        """
        Compute if this is a single-headed household
        """
        now = datetime.datetime.now()
        domain = [("birthdate", "<", now - relativedelta(years=18))]  # Adults only
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

### 4. Install and Test

1. Install the module through the Apps menu.
2. Open the Individual and Group registries and verify the new indicators display in both list and form views (handled automatically by `spp_custom_field`).
3. Create or update records and ensure the indicators compute correctly.
4. Test filtering and searching by indicator values.

## Using OpenSPP's Helper Methods

### compute_count_and_set_indicator

OpenSPP provides a helper method that simplifies indicator computation:

```python
def compute_count_and_set_indicator(self, field_name, membership_kinds, domain, presence_only=False):
    """
    Helper method to compute and set indicator values
    
    Args:
        field_name: The field name to set
        membership_kinds: List of membership kinds to filter by (e.g., ["Head"])
        domain: Domain to filter group members
        presence_only: If True, sets 1/0 instead of count
    """
```

### Examples Using the Helper Method

```python
def _compute_ind_grp_num_elderly(self):
    """Number of elderly in this household"""
    now = datetime.datetime.now()
    domain = [("birthdate", "<", now - relativedelta(years=65))]
    self.compute_count_and_set_indicator("z_ind_grp_num_elderly", None, domain)

def _compute_ind_grp_num_adults_female_not_elderly(self):
    """Number of adult females in this household"""
    now = datetime.datetime.now()
    domain = [
        ("birthdate", ">=", now - relativedelta(years=65)),
        ("birthdate", "<", now - relativedelta(years=18)),
        ("gender", "=", "Female"),
    ]
    self.compute_count_and_set_indicator("z_ind_grp_num_adults_female_not_elderly", None, domain)

def _compute_ind_grp_is_elderly_head_hh(self):
    """Is this an elderly-headed household"""
    now = datetime.datetime.now()
    domain = [("birthdate", "<", now - relativedelta(years=65))]
    self.compute_count_and_set_indicator("z_ind_grp_is_elderly_head_hh", ["Head"], domain, presence_only=True)
```

## Individual-Level Indicators

For individual-level indicators, use different patterns:

```python
class G2PIndividual(models.Model):
    _inherit = "res.partner"

    z_ind_indv_age_years = fields.Integer(
        "Age (years)",
        compute="_compute_ind_indv_age_years",
        store=True,
        help="Computed age in years for individuals",
    )

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

## Complex Indicator Examples

### Counting Children by Birth Certificate Status

```python
def _compute_ind_grp_num_single_child_less_36m_with_birth_cert(self):
    """Number of single children under 36 months with birth certificate"""
    for rec in self:
        rec.z_ind_grp_num_single_child_less_36m_with_birth_cert = rec._count_child_by_group(1)

def _count_child_by_group(self, group):
    """Helper method to count children by group type (single, twins, triplets)"""
    self.ensure_one()
    now = datetime.datetime.now()
    children = now - relativedelta(years=18)

    domain = [
        ("birthdate", ">=", children),
        ("z_cst_indv_has_birth_certificate", "=", True),
    ]

    children_birthdate = self.group_membership_ids.individual.filtered_domain(domain).mapped("birthdate")
    
    # Count children by birth date to identify twins/triplets
    children_birthdate = sorted(children_birthdate)
    children_birthdate = map(lambda x: x.strftime("%Y-%m-%d"), children_birthdate)
    count_by_date = collections.Counter(children_birthdate)

    count_by_type = {}
    for _date, count in count_by_date.items():
        count_by_type.setdefault(count, 0)
        count_by_type[count] += 1
    
    if group == 3:
        return sum(count_by_type.values()) - count_by_type.get(1, 0) - count_by_type.get(2, 0)
    return count_by_type.get(group, 0)
```

### Disability Indicators

```python
def _compute_ind_grp_num_disability(self):
    """Number of members with disability"""
    domain = [("z_cst_indv_disability_level", ">", 0)]
    self.compute_count_and_set_indicator("z_ind_grp_num_disability", None, domain)

def _compute_ind_grp_is_hh_with_disabled(self):
    """Households with disabled members"""
    domain = [("z_cst_indv_disability_level", ">", 0)]
    self.compute_count_and_set_indicator("z_ind_grp_is_hh_with_disabled", None, domain, presence_only=True)
```

## Best Practices

### 1. Field Configuration

- Always use `store=True` for indicators that need to be queried
- Use `allow_filter=True` for indicators that should be filterable in views
- Provide clear help text explaining the indicator's purpose

### 2. Performance Considerations

- Use OpenSPP's `compute_count_and_set_indicator` helper when possible
- Avoid heavy `@api.depends` chains for complex indicators
- Consider batch recomputation strategies for high-volume indicators

### 3. Naming and Documentation

- Follow OpenSPP naming conventions consistently
- Document complex compute methods with clear docstrings
- Use meaningful field labels and help text

### 4. Testing Indicators

```python
@tagged("post_install", "-at_install")
class TestGroupIndicators(TransactionCase):
    def test_01_num_children(self):
        """Test children count indicator computation"""
        self.group._compute_ind_grp_num_children()
        self.assertEqual(
            self.group.z_ind_grp_num_children,
            1,  # Expected count based on test data
            "The number of children should be 1"
        )

    def test_02_is_single_head_hh(self):
        """Test single-headed household indicator"""
        self.group._compute_ind_grp_is_single_head_hh()
        self.assertEqual(
            self.group.z_ind_grp_is_single_head_hh,
            True,  # Expected result based on test data
            "The group should be a single-headed household"
        )
```

## Common Indicator Patterns

### Age-Based Indicators

```python
# Constants for age limits
CHILDREN_AGE_LIMIT = 18
ELDERLY_AGE_LIMIT = 65

def _compute_ind_grp_num_children(self):
    now = datetime.datetime.now()
    children = now - relativedelta(years=CHILDREN_AGE_LIMIT)
    domain = [("birthdate", ">=", children)]
    self.compute_count_and_set_indicator("z_ind_grp_num_children", None, domain)
```

### Gender-Based Indicators

```python
def _compute_ind_grp_num_adults_male_not_elderly(self):
    now = datetime.datetime.now()
    domain = [
        ("birthdate", ">=", now - relativedelta(years=ELDERLY_AGE_LIMIT)),
        ("birthdate", "<", now - relativedelta(years=CHILDREN_AGE_LIMIT)),
        ("gender", "=", "Male"),
    ]
    self.compute_count_and_set_indicator("z_ind_grp_num_adults_male_not_elderly", None, domain)
```

### Custom Field-Based Indicators

```python
def _compute_ind_grp_num_receive_government_benefits(self):
    domain = [("z_cst_indv_receive_government_benefits", "=", True)]
    self.compute_count_and_set_indicator("z_ind_grp_num_receive_government_benefits", None, domain)
```

## References

For more information on computed fields and indicators in OpenSPP:

- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Development Guidelines](https://docs.openspp.org/)
- Registry modules: `g2p_registry_group`, `g2p_registry_individual`
- Example implementations: `g2p_connect_demo` module

---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Adding New Fields and Indicators

Custom fields allow the system to capture additional information that may be crucial for various social protection programs. Indicator fields are predefined fields within the system used to capture specific, standard metrics or key performance indicators (KPIs) that are essential for monitoring and evaluating the performance of social protection programs. Customizing groups and individuals with new fields and indicators enhances the system's ability to manage and analyze registrant data effectively.

## Prerequisites

- Knowledge of Python, Odoo, XML.
- To set up OpenSPP for development, please refer to the [Developer Guide](https://docs.openspp.org/howto/developer_guides/development_setup.html).

## Objective

After following this guide, developers will be able to customize indicators in OpenSPP.

## Step-by-step

In OpenSPP, both groups and individuals are based on the **res.partner** model. They are differentiated by the is_group field:

- is_group = True for groups.
- is_group = False for individuals.

These entities are linked through the **G2PGroupMembership** model, which connects individuals to their respective groups.

### Naming conventions for custom fields

Custom fields in OpenSPP follow a specific naming convention:

- **z\_** prefix for custom fields (x\_ when created from the UI).
- **ind** for indicator fields.
- **grp** for group-related fields.
- **cst** for custom fields.
- **indv** for individual-related fields.

#### Example naming conventions

1. Indicator field for group

```python
z_ind_grp_num_children
```

**z\_**: prefix.
**ind**: Indicator.
**grp**: Group-related.
**num_children**: Descriptive name indicating the number of children

2. Custom field for individual

```python
z_cst_indv_disability_level
```

**z\_**: prefix.
**cst**: Custom field.
**indv**: Individual-related.
**disability_level**: Descriptive name indicating the disability level.

### Adding custom fields to groups

#### Example 1: Adding an indicator to track the number of children

To add a custom field to a group, follow these steps:

1. Define the field:

```python
class G2PGroup(models.Model):
    _inherit = "res.partner"

    z_ind_grp_num_children = fields.Integer(
        "Number of Children",
        compute="_compute_ind_grp_num_children",
        help="Number of children in the group",
        store=True,
        allow_filter=True,
    )
```

2. Implement the compute method:

```python
def _compute_ind_grp_num_children(self):
    now = datetime.datetime.now()
    children = now - relativedelta(years=CHILDREN_AGE_LIMIT)
    domain = [("birthdate", ">=", children)]
    self.compute_count_and_set_indicator("z_ind_grp_num_children", None, domain)
```

**compute_count_and_set_indicator** is a helper function in the OpenSPP API that simplifies computing indicators. You provide the field name, any specific relationship kinds, and the domain criteria to filter the relevant records.

#### Example 2: Without compute_count_and_set_indicator

To compute an indicator without using compute_count_and_set_indicator, directly implement the compute logic within the method.

1. Define the field:

```python
class G2PGroup(models.Model):
    _inherit = "res.partner"

    z_ind_grp_is_single_head_hh = fields.Boolean(
        "Is Single-Headed Household",
        compute="_compute_ind_grp_is_single_head_hh",
        help="Indicates if the household is single-headed",
        store=True,
        allow_filter=True,
    )
```

2. Implement the compute method:

```python
def _compute_ind_grp_is_single_head_hh(self):
    for record in self:
        adult_count = record.group_membership_ids.filtered(
            lambda member: member.individual.birthdate <= (datetime.datetime.now() - relativedelta(years=18))
        ).mapped('individual')
        record.z_ind_grp_is_single_head_hh = len(adult_count) == 1
```

Do not use **@api.depends** when you want to compute indicators based on individual information, it will be very inefficient. we have another mechanism to recompute when needed.

### Adding custom fields to individuals

#### Example: Adding a custom field for disability level

To add a custom field to an individual it is only necessary to define the field:

```python
class G2PIndividual(models.Model):
    _inherit = "res.partner"
    z_cst_indv_disability_level = fields.Integer("Disability Level")
```

### Integrating custom fields into the UI

To ensure custom fields are accessible in the user interface for filtering and reporting, modify the XML views in OpenSPP. Below is a list of views that can be extended, followed by examples of how to add custom fields to these views.

#### OpenSPP views that can be extended

**Individuals views**

- Tree view
  -- Identifier: g2p_registry_individual.view_individuals_list_tree
- Form view
  -- Identifier: g2p_registry_individual.view_individuals_form

**Groups views**

- Tree view
  -- Identifier: g2p_registry_group.view_groups_list_tree
- Form view
  -- Identifier: g2p_registry_group.view_groups_form

By extending these views, you can ensure that custom fields are visible and manageable within the OpenSPP interface. Here are examples of how to extend these views to add your custom fields.

#### Adding custom fields to individual views

**Tree view**

```xml
<odoo>
    <record id="view_individuals_list_tree_custom" model="ir.ui.view">
        <field name="name">view_individuals_list_tree_custom</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_individual.view_individuals_list_tree" />
        <field name="arch" type="xml">
            <xpath expr="//field[@name='address']" position="attributes">
                <attribute name="invisible">1</attribute>
            </xpath>
            <xpath expr="//field[@name='address']" position="after">
                <field name="z_cst_indv_disability_level" string="Disability Level" />
            </xpath>
        </field>
    </record>
</odoo>
```

**Form view**

```xml
<odoo>
    <record id="view_individuals_form_custom" model="ir.ui.view">
        <field name="name">view_individuals_form_custom</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_individual.view_individuals_form" />
        <field name="arch" type="xml">
            <xpath expr="//page[@name='basic_info']/group/group[1]" position="attributes">
                <attribute name="invisible">1</attribute>
            </xpath>
            <xpath expr="//page[@name='basic_info']/group/group[1]" position="after">
                <group colspan="2">
                    <field name="z_cst_indv_disability_level"/>
                </group>
            </xpath>
        </field>
    </record>
</odoo>
```

#### Adding custom fields to group views

**Tree view**

```xml
<odoo>
    <record id="view_individuals_list_tree_custom" model="ir.ui.view">
        <field name="name">view_individuals_list_tree_custom</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_individual.view_individuals_list_tree" />
        <field name="arch" type="xml">
            <xpath expr="//field[@name='address']" position="attributes">
                <attribute name="invisible">1</attribute>
            </xpath>
            <xpath expr="//field[@name='address']" position="after">
                <field name="z_cst_indv_disability_level" string="Disability Level" />
            </xpath>
        </field>
    </record>
</odoo>
```

**Form view**

```xml
<odoo>
    <record id="view_individuals_form_custom" model="ir.ui.view">
        <field name="name">view_individuals_form_custom</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_individual.view_individuals_form" />
        <field name="arch" type="xml">
            <xpath expr="//page[@name='basic_info']/group/group[1]" position="attributes">
                <attribute name="invisible">1</attribute>
            </xpath>
            <xpath expr="//page[@name='basic_info']/group/group[1]" position="after">
                <group colspan="2">
                    <field name="z_cst_indv_disability_level"/>
                </group>
            </xpath>
        </field>
    </record>
</odoo>
```

By integrating these fields into the appropriate views, you ensure that the custom data is visible and manageable within the OpenSPP interface, enhancing the system's usability and functionality.

### Testing and validation

Testing customizations is essential to ensure they work as expected. Validate your changes by writing tests with sample data and scenarios.

#### Example test case

To validate your custom fields and computed indicators, create a test class.

```python
import datetime
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

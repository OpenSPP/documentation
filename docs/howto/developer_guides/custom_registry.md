# Customize Registry

The following article guides the reader in understanding how the registry module will work in OpenSPP and how it can be customized by providing a sample scenario and a working example.

## Prerequisites

- Knowledge of Python, Odoo, XML, Xpaths.
- To set up OpenSPP for development, please refer to the [Developer Guide](https://docs.openspp.org/howto/developer_guides/development_setup.html)

## If the Registry module is not installed

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search for the following modules that are required to be installed such as G2P Registry: Groups, G2P Registry: Individual and G2P Registry: Membership.

![](custom_registry/1.png)

## Utilizing the Registry Module

For more detailed guidance on utilizing the Registry module in OpenSPP, please refer to the information available at the provided link, which will be published soon.

## Customise Registry

In this hypothetical scenario, we will look at the following customizations

- Storing a new field salary of an individual to be used as a indicator
- Adding an indicator in the group of the registry
- To show the salary of every individual in the group member view.

A working sample module for the described scenario can be accessed at the provided [link](https://github.com/OpenSPP/documentation_code/tree/main/howto/developer_guides/customizations/spp_registry_custom).

The key steps in module development are as follows:

1. To do the above customizations, a new module can be developed.

2. To initiate the development of the custom module for registry customization, begin by creating a manifest file. This file should include fields like name, category, and version. Additionally, it's important to define the dependencies of the new module as outlined below.

```python
  "depends": [
       "g2p_registry_group",
       "g2p_registry_individual",
       "g2p_registry_membership",
   ],
```

3. To add the new field for salary in the registry, develop a Python file named `individual.py` that extends `res.partner` and incorporate this file into `models/init.py`. The definition of the salary and currency fields should be implemented as demonstrated below.

```python
from odoo import fields, models

class OpenSPPIndividualCustom(models.Model):
   _inherit = "res.partner"


   ind_currency_id = fields.Many2one(
       "res.currency",
       "Currency",
       default=lambda self: self.env.user.company_id.currency_id or None,
   )
   ind_salary = fields.Monetary("Salary", currency_field="ind_currency_id", default=0.0)
```

Note that when adding fields that are specific for individual It should have the prefix `ind_`

4. To add the new column in the Members table in the groups, develop a Python file named `group_membership.py` that extends `g2p.group.membership` and incorporate this file into `models/__init__.py`. The definition of the salary and currency fields should be implemented as demonstrated below.

```python
from odoo import fields, models

class OpenSPPMembershipCustom(models.Model):
   _inherit = "g2p.group.membership"

   currency_id = fields.Many2one(
       "res.currency",
       related="individual.ind_currency_id",
   )


   salary = fields.Monetary(
       "Salary",
       currency_field="currency_id",
       related="individual.ind_salary",
   )

```

5. To add the salary as an indicator in the group-level, develop a Python file named `group.py` that extends `res.partner` and incorporate this file into `models/init.py`. The definition of the number of individuals with a salary below 100 USD should be implemented as demonstrated below.

```python
from odoo import api, fields, models

class OpenSPPGroupCustom(models.Model):
   _inherit = "res.partner"


   z_ind_grp_count_below_salary = fields.Integer(
       "Number of members with below 100 salary",
       compute="_compute_count_below_salary",
   )


   @api.depends("group_membership_ids", "group_membership_ids.salary")
   def _compute_count_below_salary(self):
       for rec in self:
           below_salary_count = 0
           for membership in rec.group_membership_ids:
               if membership.salary < 100:
                   below_salary_count += 1


           rec.z_ind_grp_count_below_salary = below_salary_count

```

To understand further, refer to the following documentation given [1](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/04_basicmodel.html),[2](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/14_other_module.html),[3](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/13_inheritance.html)

6. The following steps should be followed to integrate the new fields into the UI. Create new files named `views/individual_views.xml` and `views/group_membership_views.xml` in the module. Add the below code to the manifest file.

```python
   "data": [
       "views/group_membership_views.xml",
       "views/individual_views.xml",
   ],

```

7. The following code can be added to the `individual_views.xml` file to show the currency and salary in the UI.

```xml
   <record id="view_individuals_salary_detail" model="ir.ui.view">
       <field name="name">view_individuals_salary_detail</field>
       <field name="model">res.partner</field>
       <field name="inherit_id" ref="g2p_registry_individual.view_individuals_form" />
       <field name="arch" type="xml">
           <xpath expr="//field[@name='email']" position="after">
               <field name="ind_currency_id" />
               <field name="ind_salary" />
           </xpath>
       </field>
   </record>
```

8. The following code can be added to the `group_membership_views.xml` to show the salary of every member of a group.

```xml
   <record id="view_group_membership_salary_indicator" model="ir.ui.view">
       <field name="name">view_group_membership_salary_indicator</field>
       <field name="model">res.partner</field>
       <field name="inherit_id" ref="g2p_registry_group.view_groups_form" />
       <field name="arch" type="xml">
           <xpath expr="//field[@name='group_membership_ids']/tree/field[@name='ended_date']" position="after">
               <field name="salary" />
           </xpath>
       </field>
   </record>
```

9. Install the module to include the new changes.

10. The following screenshot shows the added field in the newly developed module.

See the following for the Individual view.
![](custom_registry/2.png)

See the following for the Members table in Groups.
![](custom_registry/3.png)

See the following for the Indicators in Groups
![](custom_registry/4.png)

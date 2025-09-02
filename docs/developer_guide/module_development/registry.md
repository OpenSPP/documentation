---
myst:
  html_meta:
    "title": "Registry"
    "description": "Learn how to customize OpenSPP registry system by adding new top-level group types and extending registry functionality"
    "keywords": "OpenSPP, registry customization, group types, registry system, module development, registry extension"
---

# Registry

This article explains how to customize OpenSPP's registry system by introducing a new **top-level group** type.
As a practical example, we'll add a new top-level group type (such as "Village") that can contain regular groups (households), along with custom UI, data, and actions.

**Core Models**

- **`res.partner`**: Main registry model for individuals and groups.
- **`g2p.group.kind`**: Defines types of groups (e.g., Household, Village).
- **`g2p.group.membership`**: Manages group membership relationships.

**Key Features**

- Hierarchical group structure (e.g., Villages > Households > Individuals)
- Custom group kinds and indicators
- Computed statistics for top-level groups
- Custom actions for navigation and reporting

## Prerequisites

- Solid understanding of Odoo 17 module development, including Python, XML, and XPath.
- Required modules: `g2p_registry_base`, `g2p_registry_group`, `g2p_registry_individual`, `g2p_registry_membership`, `spp_registry_group_hierarchy`.
- To set up OpenSPP for development, please refer to the {doc}`Development Setup Guide <../setup>`.

## Module Structure

A typical registry customization module follows the standard Odoo structure.
Here's the structure for our example module, `spp_top_level_groups`:

```
spp_top_level_groups/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── res_partner.py
│   └── group_kind.py
├── views/
│   ├── top_level_group_views.xml
│   ├── group_views.xml
│   └── group_kind_views.xml
├── data/
│   └── group_kind_data.xml
└── security/
    └── ir.model.access.csv
```

## Step-by-Step Guide

### Create the Module Scaffold

Create a new directory for your module (e.g., `spp_top_level_groups`) and populate it with the files and folders shown above.

### Define Module Manifest

Create a manifest file with the necessary dependencies and data files:

```python
{
    "name": "OpenSPP Top Level Groups",
    "summary": "Adds top-level group types like villages and communities to the registry system.",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "author": "Your Organization",
    "website": "https://your-website.com",
    "license": "LGPL-3",
    "depends": [
        "base",
        "g2p_registry_base",
        "g2p_registry_individual",
        "g2p_registry_group",
        "g2p_registry_membership",
        "spp_registry_group_hierarchy",
    ],
    "data": [
        "data/group_kind_data.xml",
        "views/group_kind_views.xml",
        "views/top_level_group_views.xml",
        "views/group_views.xml",
        "security/ir.model.access.csv",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
```

### Add Custom Group Kind Data

Create `data/group_kind_data.xml` to define the new group kind:

```xml
<odoo>
    <data noupdate="1">
        <record id="group_kind_village" model="g2p.group.kind">
            <field name="name">Village</field>
            <field name="description">A village that contains multiple households</field>
            <field name="allow_all_member_type">True</field>
        </record>
    </data>
</odoo>
```

### Extend the Registry Model

Create `models/res_partner.py` to add custom fields, indicators, and actions:

```python
from odoo import fields, models, api

class G2PTopLevelGroup(models.Model):
    _inherit = "res.partner"

    village_code = fields.Char("Village Code", help="Official village code or identifier")
    population = fields.Integer("Population", help="Total population of the village/community")

    total_households = fields.Integer(
        "Total Households", compute="_compute_total_households", store=True,
        help="Total number of households in this village"
    )
    total_individuals = fields.Integer(
        "Total Individuals", compute="_compute_total_individuals", store=True,
        help="Total number of individuals in this village"
    )
    avg_household_size = fields.Float(
        "Average Household Size", compute="_compute_avg_household_size", store=True,
        help="Average number of individuals per household"
    )

    def _compute_total_households(self):
        for rec in self:
            if not rec.is_group or not rec.kind or rec.kind.name != 'Village':
                rec.total_households = 0
                continue
            household_groups = rec.group_membership_ids.mapped('individual').filtered(
                lambda x: x.is_group and x.kind and x.kind.name == 'Household'
            )
            rec.total_households = len(household_groups)

    def _compute_total_individuals(self):
        for rec in self:
            if not rec.is_group or not rec.kind or rec.kind.name != 'Village':
                rec.total_individuals = 0
                continue
            total = 0
            household_groups = rec.group_membership_ids.mapped('individual').filtered(
                lambda x: x.is_group and x.kind and x.kind.name == 'Household'
            )
            for household in household_groups:
                total += len(household.group_membership_ids.mapped('individual').filtered(lambda x: not x.is_group))
            rec.total_individuals = total

    def _compute_avg_household_size(self):
        for rec in self:
            if rec.total_households > 0:
                rec.avg_household_size = rec.total_individuals / rec.total_households
            else:
                rec.avg_household_size = 0.0

    def action_view_households(self):
        self.ensure_one()
        household_groups = self.group_membership_ids.mapped('individual').filtered(
            lambda x: x.is_group and x.kind and x.kind.name == 'Household'
        )
        return {
            'name': f'Households in {self.name}',
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', household_groups.ids)],
            'context': {'default_is_group': True, 'default_kind': self.env.ref('g2p_registry_group.group_kind_household').id},
        }

    def action_view_individuals(self):
        self.ensure_one()
        all_individuals = self.env['res.partner']
        household_groups = self.group_membership_ids.mapped('individual').filtered(
            lambda x: x.is_group and x.kind and x.kind.name == 'Household'
        )
        for household in household_groups:
            individuals = household.group_membership_ids.mapped('individual').filtered(lambda x: not x.is_group)
            all_individuals |= individuals
        return {
            'name': f'Individuals in {self.name}',
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', all_individuals.ids)],
            'context': {'default_is_group': False},
        }
```

### Extend Group Kind Model

Create `models/group_kind.py` to add custom flags:

```python
from odoo import fields, models

class SPPGroupKind(models.Model):
    _inherit = "g2p.group.kind"

    is_top_level_group = fields.Boolean("Is Top Level Group", default=False, help="Indicates if this group kind represents a top-level group")
    can_contain_households = fields.Boolean("Can Contain Households", default=False, help="Indicates if this group kind can contain household groups")
```

### Create View Extensions

#### Top Level Group Views (`views/top_level_group_views.xml`)

Update all field names to remove the prefix:

```xml
<odoo>
    <!-- Village Form View -->
    <record id="view_villages_form" model="ir.ui.view">
        <field name="name">view_villages_form</field>
        <field name="model">res.partner</field>
        <field name="arch" type="xml">
            <form string="Village">
                <sheet>
                    <div class="oe_button_box" name="button_box">
                        <button name="action_view_households" type="object" class="oe_stat_button" icon="fa-home">
                            <field name="total_households" widget="statinfo" string="Households"/>
                        </button>
                        <button name="action_view_individuals" type="object" class="oe_stat_button" icon="fa-users">
                            <field name="total_individuals" widget="statinfo" string="Individuals"/>
                        </button>
                    </div>
                    <div class="oe_title mb24">
                        <h1>
                            <field name="name" placeholder="Village Name"/>
                        </h1>
                    </div>
                    <group>
                        <group>
                            <field name="kind" domain="[('name', '=', 'Village')]"/>
                            <field name="village_code"/>
                            <field name="population"/>
                        </group>
                        <group>
                            <field name="avg_household_size"/>
                            <field name="is_group" invisible="1"/>
                        </group>
                    </group>
                    <notebook>
                        <page string="Members" name="members">
                            <field name="group_membership_ids" context="{'default_group': active_id}">
                                <tree editable="bottom">
                                    <field name="individual" domain="[('is_group', '=', True), ('kind.name', '=', 'Household')]"/>
                                    <field name="kind"/>
                                    <field name="start_date"/>
                                    <field name="ended_date"/>
                                    <field name="status"/>
                                </tree>
                            </field>
                        </page>
                        <page string="Statistics" name="statistics">
                            <group>
                                <group>
                                    <field name="total_households"/>
                                    <field name="total_individuals"/>
                                </group>
                                <group>
                                    <field name="avg_household_size"/>
                                </group>
                            </group>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>

    <!-- Village Tree View -->
    <record id="view_villages_tree" model="ir.ui.view">
        <field name="name">view_villages_tree</field>
        <field name="model">res.partner</field>
        <field name="arch" type="xml">
            <tree string="Villages">
                <field name="name"/>
                <field name="kind"/>
                <field name="village_code"/>
                <field name="population"/>
                <field name="total_households"/>
                <field name="total_individuals"/>
                <field name="avg_household_size"/>
            </tree>
        </field>
    </record>

    <!-- Village Search View -->
    <record id="view_villages_search" model="ir.ui.view">
        <field name="name">view_villages_search</field>
        <field name="model">res.partner</field>
        <field name="arch" type="xml">
            <search string="Villages">
                <field name="name"/>
                <field name="village_code"/>
                <field name="kind"/>
                <filter string="Villages" name="villages" domain="[('kind.name', '=', 'Village')]"/>
                <group expand="0" string="Group By">
                    <filter string="Group Kind" name="group_kind" context="{'group_by': 'kind'}"/>
                </group>
            </search>
        </field>
    </record>

    <!-- Villages Action -->
    <record id="action_villages" model="ir.actions.act_window">
        <field name="name">Villages</field>
        <field name="res_model">res.partner</field>
        <field name="view_mode">tree,form</field>
        <field name="domain">[('is_group', '=', True), ('kind.name', '=', 'Village')]</field>
        <field name="view_ids" eval="[(5, 0, 0),
            (0, 0, {'view_mode': 'tree', 'view_id': ref('view_villages_tree')}),
            (0, 0, {'view_mode': 'form', 'view_id': ref('view_villages_form')})]"/>
        <field name="search_view_id" ref="view_villages_search"/>
        <field name="context">{'default_is_group': True, 'default_kind': ref('group_kind_village')}</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Create your first village!
            </p>
            <p>
                Villages can contain multiple households as members.
            </p>
        </field>
    </record>

    <!-- Menu Item -->
    <menuitem id="menu_villages"
        name="Villages"
        parent="g2p_registry_group.menu_groups"
        action="action_villages"
        sequence="20"/>
</odoo>
```

#### Group Kind Views (`views/group_kind_views.xml`)

```xml
<odoo>
    <record id="view_group_kind_tree_top_level" model="ir.ui.view">
        <field name="name">view_group_kind_tree_top_level</field>
        <field name="model">g2p.group.kind</field>
        <field name="inherit_id" ref="g2p_registry_group.view_group_kind_tree" />
        <field name="arch" type="xml">
            <xpath expr="//field[@name='name']" position="after">
                <field name="is_top_level_group"/>
                <field name="can_contain_households"/>
            </xpath>
        </field>
    </record>
</odoo>
```

#### Group Views (`views/group_views.xml`)

```xml
<odoo>
    <record id="view_groups_form_village_info" model="ir.ui.view">
        <field name="name">view_groups_form_village_info</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_group.view_groups_form" />
        <field name="arch" type="xml">
            <xpath expr="//page[@name='basic_info']/group/group[1]" position="after">
                <group colspan="2">
                    <field name="group_membership_ids" invisible="1"/>
                    <field name="belongs_to_village" 
                           compute="_compute_belongs_to_village" 
                           readonly="1"
                           string="Belongs to Village"/>
                </group>
            </xpath>
        </field>
    </record>
</odoo>
```

### Add Security Access

Create `security/ir.model.access.csv`:

```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_top_level_groups_admin,top.level.groups.admin,base.model_res_partner,g2p_registry_base.group_g2p_admin,1,1,1,1
```

### Install and Test

1. **Install the module** via the Apps menu.
2. **Configure group kinds**: Registry > Configuration > Group Kinds.
   Ensure "Village" is present and allows group/individual members.
3. **Create villages**: Registry > Groups > Villages.
   Add households as members.
4. **Test**: Use action buttons to view households and individuals.
   Check computed indicators.

### Example Use Case

```
Village A (Top Level Group)
├── Household 1 (Regular Group)
│   ├── John Doe (Individual)
│   └── Jane Doe (Individual)
└── Household 2 (Regular Group)
    ├── Bob Smith (Individual)
    └── Alice Smith (Individual)
```

## Best Practices

- Use descriptive names for group kinds.
- Enable hierarchy only for appropriate group kinds.
- Use domains and validation to enforce group relationships.
- Provide clear navigation and action buttons for users.

## References

For more information on extending OpenSPP modules, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- Related guides: {doc}`Customizing Fields <fields>`, {doc}`Customizing Indicators <indicators>`
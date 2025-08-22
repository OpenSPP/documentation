---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Customizing the Registry

This guide demonstrates how to customize OpenSPP's registry system by extending its functionality. We'll create a module that adds a new higher-level group type (like "Villages" or "Communities") that can contain regular groups (households) as members, along with custom UI, data, and actions.

## Prerequisites

- Knowledge of Python, Odoo, XML, Xpaths.
- To set up OpenSPP for development, please refer to the [Developer Guide](https://docs.openspp.org/howto/developer_guides/development_setup.html).

## Understanding Registry Customization

### Default OpenSPP Structure
- **Individuals**: Single persons (`is_group = False`)
- **Groups**: Collections of individuals like households (`is_group = True`)

### Extended Structure with Higher Groups
- **Higher Groups**: Super groups that contain regular groups (e.g., villages, communities)
- **Regular Groups**: Groups that belong to higher groups (e.g., households within villages)
- **Individuals**: Members of the regular groups

## Creating a Higher Group Registry Module

In this example, we'll create a module that adds "Villages" as a higher-level group type that can contain households.

### 1. Create Module Structure

Create a new module following the OpenSPP module structure:

```
spp_higher_groups/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── res_partner.py
│   └── group_kind.py
├── views/
│   ├── higher_group_views.xml
│   ├── group_views.xml
│   └── group_kind_views.xml
├── data/
│   └── group_kind_data.xml
└── security/
    └── ir.model.access.csv
```

### 2. Define Module Manifest

Create a manifest file that includes the proper dependencies and data files:

```python
{
    "name": "OpenSPP Higher Groups",
    "summary": "Adds higher-level group types like villages and communities to the registry system.",
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
        "spp_registry_group_hierarchy",  # For hierarchy support
    ],
    "data": [
        "data/group_kind_data.xml",
        "views/group_kind_views.xml",
        "views/higher_group_views.xml",
        "views/group_views.xml",
        "security/ir.model.access.csv",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
```

### 3. Create Group Kind Data

Create `data/group_kind_data.xml` to define the new group kind:

```xml
<odoo>
    <data noupdate="1">
        <!-- Village Group Kind -->
        <record id="group_kind_village" model="g2p.group.kind">
            <field name="name">Village</field>
            <field name="description">A village that contains multiple households</field>
            <field name="allow_all_member_type">True</field>
        </record>
    </data>
</odoo>
```

### 4. Extend the res.partner Model

Create `models/res_partner.py` to add custom fields and methods:

```python
from odoo import fields, models, api
import datetime
from dateutil.relativedelta import relativedelta

class G2PHigherGroup(models.Model):
    _inherit = "res.partner"

    # Custom fields for higher groups
    z_cst_grp_village_code = fields.Char(
        "Village Code",
        help="Official village code or identifier"
    )
    
    z_cst_grp_population = fields.Integer(
        "Population",
        help="Total population of the village/community"
    )

    # Custom indicators for villages
    z_ind_grp_total_households = fields.Integer(
        "Total Households",
        compute="_compute_total_households",
        store=True,
        help="Total number of households in this village"
    )

    z_ind_grp_total_individuals = fields.Integer(
        "Total Individuals",
        compute="_compute_total_individuals",
        store=True,
        help="Total number of individuals in this village"
    )

    z_ind_grp_avg_household_size = fields.Float(
        "Average Household Size",
        compute="_compute_avg_household_size",
        store=True,
        help="Average number of individuals per household"
    )

    def _compute_total_households(self):
        """Compute total households in this village"""
        for rec in self:
            if not rec.is_group or not rec.kind or rec.kind.name != 'Village':
                rec.z_ind_grp_total_households = 0
                continue
            
            # Count groups that are households
            household_groups = rec.group_membership_ids.mapped('individual').filtered(
                lambda x: x.is_group and x.kind and x.kind.name == 'Household'
            )
            rec.z_ind_grp_total_households = len(household_groups)

    def _compute_total_individuals(self):
        """Compute total individuals in this village"""
        for rec in self:
            if not rec.is_group or not rec.kind or rec.kind.name != 'Village':
                rec.z_ind_grp_total_individuals = 0
                continue
            
            total = 0
            # Count individuals in household groups
            household_groups = rec.group_membership_ids.mapped('individual').filtered(
                lambda x: x.is_group and x.kind and x.kind.name == 'Household'
            )
            for household in household_groups:
                total += len(household.group_membership_ids.mapped('individual').filtered(lambda x: not x.is_group))
            
            rec.z_ind_grp_total_individuals = total

    def _compute_avg_household_size(self):
        """Compute average household size"""
        for rec in self:
            if rec.z_ind_grp_total_households > 0:
                rec.z_ind_grp_avg_household_size = rec.z_ind_grp_total_individuals / rec.z_ind_grp_total_households
            else:
                rec.z_ind_grp_avg_household_size = 0.0

    def action_view_households(self):
        """Action to view households in this village"""
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
        """Action to view all individuals in this village"""
        self.ensure_one()
        all_individuals = self.env['res.partner']
        
        # Get individuals from all household groups
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

### 5. Extend Group Kinds

Create `models/group_kind.py` to add custom functionality:

```python
from odoo import fields, models

class SPPGroupKind(models.Model):
    _inherit = "g2p.group.kind"

    is_higher_group = fields.Boolean(
        "Is Higher Group",
        default=False,
        help="Indicates if this group kind represents a higher-level group"
    )

    can_contain_households = fields.Boolean(
        "Can Contain Households",
        default=False,
        help="Indicates if this group kind can contain household groups"
    )
```

### 6. Create View Extensions

#### Higher Group Views (`views/higher_group_views.xml`)

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
                            <field name="z_ind_grp_total_households" widget="statinfo" string="Households"/>
                        </button>
                        <button name="action_view_individuals" type="object" class="oe_stat_button" icon="fa-users">
                            <field name="z_ind_grp_total_individuals" widget="statinfo" string="Individuals"/>
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
                                <field name="z_cst_grp_village_code"/>
                                <field name="z_cst_grp_population"/>
                            </group>
                            <group>
                                <field name="z_ind_grp_avg_household_size"/>
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
                                    <field name="z_ind_grp_total_households"/>
                                    <field name="z_ind_grp_total_individuals"/>
                                </group>
                                <group>
                                    <field name="z_ind_grp_avg_household_size"/>
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
                <field name="z_cst_grp_village_code"/>
                <field name="z_cst_grp_population"/>
                <field name="z_ind_grp_total_households"/>
                <field name="z_ind_grp_total_individuals"/>
                <field name="z_ind_grp_avg_household_size"/>
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
                <field name="z_cst_grp_village_code"/>
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
    <record id="view_group_kind_tree_villages" model="ir.ui.view">
        <field name="name">view_group_kind_tree_villages</field>
        <field name="model">g2p.group.kind</field>
        <field name="inherit_id" ref="g2p_registry_group.view_group_kind_tree" />
        <field name="arch" type="xml">
            <xpath expr="//field[@name='name']" position="after">
                <field name="is_higher_group"/>
                <field name="can_contain_households"/>
            </xpath>
        </field>
    </record>
</odoo>
```

#### Group Views (`views/group_views.xml`)

```xml
<odoo>
    <!-- Extend regular group form to show village info -->
    <record id="view_groups_form_village_info" model="ir.ui.view">
        <field name="name">view_groups_form_village_info</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_group.view_groups_form" />
        <field name="arch" type="xml">
            <xpath expr="//page[@name='basic_info']/group/group[1]" position="after">
                <group colspan="2">
                    <field name="group_membership_ids" invisible="1"/>
                    <field name="z_cst_grp_belongs_to_village" 
                           compute="_compute_belongs_to_village" 
                           readonly="1"
                           string="Belongs to Village"/>
                </group>
            </xpath>
        </field>
    </record>
</odoo>
```

### 7. Add Security Access

Create `security/ir.model.access.csv`:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_higher_groups_admin,higher.groups.admin,base.model_res_partner,g2p_registry_base.group_g2p_admin,1,1,1,1
```

### 8. Install and Configure

1. **Install the module** through the Apps menu.

2. **Configure Group Kinds**:
   - Go to Registry > Configuration > Group Kinds
   - Verify that "Village" and "Community" group kinds are created
   - Ensure "Allow group and individual members" is enabled for these kinds

3. **Create Villages**:
   - Go to Registry > Groups > Villages
   - Create villages
   - Add household groups as members

4. **Test the Functionality**:
   - Create a village and add households to it
   - Use the action buttons to view households and individuals
   - Verify that indicators are computed correctly

## Example Use Cases

### Village Structure
```
Village A (Village Group)
├── Household 1 (Regular Group)
│   ├── John Doe (Individual)
│   └── Jane Doe (Individual)
└── Household 2 (Regular Group)
    ├── Bob Smith (Individual)
    └── Alice Smith (Individual)
```

## Best Practices

### 1. Group Kind Configuration
- Use descriptive names for group kinds
- Enable hierarchy support only for appropriate group kinds
- Document the intended hierarchy structure

### 2. Data Management
- Use proper domains to filter group kinds in views
- Implement validation to ensure proper group relationships
- Consider performance for large hierarchical structures

### 3. User Experience
- Provide clear navigation between different group levels
- Use action buttons for quick access to related data
- Implement proper form inheritance and view extensions

### 4. Customization Patterns
- Follow OpenSPP naming conventions for custom fields
- Use computed fields for indicators and statistics
- Implement proper security access controls

## Advanced Customization

### Adding Custom Actions

You can add more custom actions for specific use cases:

```python
def action_export_village_data(self):
    """Export village data to external format"""
    self.ensure_one()
    # Implementation for data export
    pass

def action_generate_village_report(self):
    """Generate village report"""
    self.ensure_one()
    # Implementation for report generation
    pass
```

### Adding Custom Validation

```python
@api.constrains('kind', 'group_membership_ids')
def _check_village_constraints(self):
    """Validate village constraints"""
    for rec in self:
        if rec.kind and rec.kind.name == 'Village':
            # Ensure only household groups can be members
            invalid_members = rec.group_membership_ids.mapped('individual').filtered(
                lambda x: not x.is_group or (x.kind and not x.kind.name == 'Household')
            )
            if invalid_members:
                raise ValidationError(_("Villages can only contain household groups as members."))
```

## References

For more information on customizing OpenSPP's registry system:

- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Development Guidelines](https://docs.openspp.org/)
- Registry modules: `g2p_registry_group`, `g2p_registry_individual`, `g2p_registry_membership`
- Hierarchy module: `spp_registry_group_hierarchy`
- Related guides: [Customizing Fields](customizing_fields.md), [Customizing Indicators](customizing_indicators.md)

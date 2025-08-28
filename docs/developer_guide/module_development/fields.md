---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Registry Fields

This article guides you through understanding how the registry modules work in OpenSPP and how to add custom fields to registrants. The `g2p_registry_group` and `g2p_registry_individual` modules surface registrants (groups and individuals) based on the `res.partner` model.

**Core Models**

The registry separates groups and individuals while sharing the same underlying model:
- `res.partner`: Base model used for both groups and individuals. Differentiated by `is_group`.
- `g2p.group.membership` (referenced in OpenSPP): Connects individuals to their groups.

**Key Features**
- A unified `res.partner` record represents either a group (`is_group = True`) or an individual (`is_group = False`).
- Rich registry user interfaces provided by `g2p_registry_group` and `g2p_registry_individual`.
- Existing views that you can extend to expose your custom fields:
  - Individuals
    - Tree: `g2p_registry_individual.view_individuals_list_tree`
    - Form: `g2p_registry_individual.view_individuals_form`
  - Groups
    - Tree: `g2p_registry_group.view_groups_list_tree`
    - Form: `g2p_registry_group.view_groups_form`

## Prerequisites

- Solid understanding of Odoo 17 module development, including Python, XML, and XPath.
- Registry modules (`g2p_registry_group`, `g2p_registry_individual`) installed.
- To set up OpenSPP for development, please refer to the {doc}`Development Setup Guide <setup>`.

## Module Structure

A typical customization module for registry fields follows the standard Odoo module structure. Here’s an example for `spp_custom_registry_field`:

```
spp_custom_registry_field/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── res_partner.py
├── views/
│   ├── individual_views.xml
│   └── group_views.xml
└── security/
    └── ir.model.access.csv
```

## Step-by-Step Guide

### Step 1: Create the Module Scaffold

Create a new directory for your module (e.g., `spp_custom_registry_field`) and populate it with the files and structure above.

### Step 2: Define Module Manifest

Create a manifest file with dependencies and data files:

```python
{
    "name": "OpenSPP Custom Registry Field",
    "summary": "Adds a simple custom field to registrants (res.partner)",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "author": "Your Organization",
    "website": "https://your-website.com",
    "license": "LGPL-3",
    "depends": [
        "g2p_registry_group",
        "g2p_registry_individual",
    ],
    "data": [
        "views/individual_views.xml",
        "views/group_views.xml",
        # "security/ir.model.access.csv",  # Only needed if you add new models
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
```

### Step 3: Extend the res.partner Model

Create `models/res_partner.py` to add your custom field and import it in `models/__init__.py`:

```python
from odoo import fields, models

class G2PRegistrant(models.Model):
    _inherit = "res.partner"

    # Custom field shared by both individuals and groups
    reg_note = fields.Char(
        string="Registrant Note",
        help="Free-form note for this registrant",
    )
```

### Step 4: Create View Extensions

Expose the field on both Individuals and Groups UI by extending the existing views.

```xml
<odoo>
    <!-- Individual: show in form -->
    <record id="view_individuals_form_custom_reg_note" model="ir.ui.view">
        <field name="name">view_individuals_form_custom_reg_note</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_individual.view_individuals_form" />
        <field name="arch" type="xml">
            <xpath expr="//page[@name='basic_info']/group/group[1]" position="after">
                <group colspan="2">
                    <field name="reg_note"/>
                </group>
            </xpath>
        </field>
    </record>

    <!-- Individual: show in tree -->
    <record id="view_individuals_list_tree_custom_reg_note" model="ir.ui.view">
        <field name="name">view_individuals_list_tree_custom_reg_note</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_individual.view_individuals_list_tree" />
        <field name="arch" type="xml">
            <xpath expr="//field[@name='address']" position="after">
                <field name="reg_note" string="Note"/>
            </xpath>
        </field>
    </record>

    <!-- Group: show in form -->
    <record id="view_groups_form_custom_reg_note" model="ir.ui.view">
        <field name="name">view_groups_form_custom_reg_note</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_group.view_groups_form" />
        <field name="arch" type="xml">
            <xpath expr="//page[@name='basic_info']/group/group[1]" position="after">
                <group colspan="2">
                    <field name="reg_note"/>
                </group>
            </xpath>
        </field>
    </record>

    <!-- Group: show in tree -->
    <record id="view_groups_list_tree_custom_reg_note" model="ir.ui.view">
        <field name="name">view_groups_list_tree_custom_reg_note</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_group.view_groups_list_tree" />
        <field name="arch" type="xml">
            <xpath expr="//field[@name='name']" position="after">
                <field name="reg_note" string="Note"/>
            </xpath>
        </field>
    </record>
</odoo>
```

### Step 5: Add Security Access (Optional)

If you introduce new models, add access rights. For a simple field addition to `res.partner`, this is not required. Example:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_custom_partner_note,custom.partner.note,base.model_res_partner,base.group_user,1,1,0,0
```

### Step 6: Install and Test

1. Install the module through the Apps menu.
2. Open the Individual and Group registries and verify the new field displays in both list and form views.
3. Create or update records and ensure the new field can be edited and saved.

## References

For more information on extending Odoo models and views, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Documentation](https://docs.openspp.org/)
- Registry modules referenced: `g2p_registry_group`, `g2p_registry_individual`

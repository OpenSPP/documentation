---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Adding New Fields and Indicators

The following article guides the reader in understanding how the registry modules work in OpenSPP and how to add a simple custom field to registrants by providing a sample scenario and a working-style example. In OpenSPP, registrants (both groups and individuals) are implemented on the `res.partner` model and surfaced through the `g2p_registry_group` and `g2p_registry_individual` modules.

## Prerequisites

- Knowledge of Python, Odoo, XML, Xpaths.
- To set up OpenSPP for development, please refer to the [Developer Guide](https://docs.openspp.org/howto/developer_guides/development_setup.html).

## If the Registry modules are not installed

1. Log into OpenSPP with administrative rights.

2. Access the "Apps" menu from the dashboard to manage OpenSPP modules.

3. Choose "Update Apps List" to refresh the module list.

4. Search and initiate installation of the following modules, this will also install the other required modules:

   - G2P Registry: Group (`g2p_registry_group`)
   - G2P Registry: Individual (`g2p_registry_individual`)

## Understanding the Registry Structure

The registry separates groups and individuals while sharing the same underlying model:

### Core Models
- `res.partner`: Base model used for both groups and individuals. Differentiated by `is_group`.
- `g2p.group.membership` (referenced in OpenSPP): Connects individuals to their groups.

### Key Features
- A unified `res.partner` record represents either a group (`is_group = True`) or an individual (`is_group = False`).
- Rich registry user interfaces provided by `g2p_registry_group` and `g2p_registry_individual`.
- Existing views that you can extend to expose your custom fields:
  - Individuals
    - Tree: `g2p_registry_individual.view_individuals_list_tree`
    - Form: `g2p_registry_individual.view_individuals_form`
  - Groups
    - Tree: `g2p_registry_group.view_groups_list_tree`
    - Form: `g2p_registry_group.view_groups_form`

## Customizing the Registry (Add one field on res.partner)

In this scenario, we add a single custom field to `res.partner` that can be shown on both the Individual and Group registry interfaces. This keeps the example simple and focused.

The key steps in module development are as follows:

### 1. Create Module Structure

Create a new module following the OpenSPP module structure:

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

### 2. Define Module Manifest

Create a manifest file that includes the proper dependencies and data files:

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
        # "security/ir.model.access.csv",  # not needed if you do not add new models
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
```

### 3. Extend the res.partner Model

Create `models/res_partner.py` to add your custom field and import it in `models/__init__.py`.

```python
from odoo import fields, models

class G2PRegistrant(models.Model):
    _inherit = "res.partner"

    # A simple custom field shared by both individuals and groups
    z_cst_reg_note = fields.Char(
        string="Registrant Note",
        help="Free-form note for this registrant",
    )
```

### 4. Create View Extensions

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
                    <field name="z_cst_reg_note"/>
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
                <field name="z_cst_reg_note" string="Note"/>
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
                    <field name="z_cst_reg_note"/>
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
                <field name="z_cst_reg_note" string="Note"/>
            </xpath>
        </field>
    </record>
</odoo>
```

### 5. Add Security Access (Optional)

If you introduce new models, include access rights. For a simple field addition to `res.partner`, this is not required. A minimal example (optional):

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_custom_partner_note,custom.partner.note,base.model_res_partner,base.group_user,1,1,0,0
```

### 6. Install and Test

1. Install the module through the Apps menu.
2. Open the Individual and Group registries and verify the new field displays in both list and form views.
3. Create or update records and ensure the new field can be edited and saved.

## Advanced Customization Examples

## Adding a One2many Field (creates a new model)

To relate multiple records to a registrant, add a One2many on `res.partner` and define its comodel. Because this introduces a new model, include proper access rights and reference the G2P admin group from `g2p_registry_base`.

### 7. Define the New Model and One2many

Create `models/partner_note.py`:

```python
from odoo import fields, models

class PartnerNote(models.Model):
    _name = "spp.partner.note"
    _description = "Partner Note"

    partner_id = fields.Many2one(
        "res.partner",
        string="Registrant",
        required=True,
        ondelete="cascade",
    )
    name = fields.Char(required=True)
    description = fields.Text()
```

Extend `res.partner` in `models/res_partner.py`:

```python
from odoo import fields, models

class G2PRegistrant(models.Model):
    _inherit = "res.partner"

    z_cst_reg_notes = fields.One2many(
        "spp.partner.note",
        "partner_id",
        string="Notes",
    )
```

Update `models/__init__.py`:

```python
from . import res_partner
from . import partner_note
```

### 8. Expose in the UI

```xml
<odoo>
    <!-- Individual form: One2many -->
    <record id="view_individuals_form_custom_reg_notes" model="ir.ui.view">
        <field name="name">view_individuals_form_custom_reg_notes</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_individual.view_individuals_form" />
        <field name="arch" type="xml">
            <xpath expr="//page[@name='basic_info']" position="after">
                <page string="Notes">
                    <field name="z_cst_reg_notes" context="{'default_partner_id': active_id}">
                        <tree editable="bottom">
                            <field name="name"/>
                            <field name="description"/>
                        </tree>
                        <form string="Partner Note">
                            <group>
                                <field name="name"/>
                                <field name="description"/>
                            </group>
                        </form>
                    </field>
                </page>
            </xpath>
        </field>
    </record>

    <!-- Group form: One2many -->
    <record id="view_groups_form_custom_reg_notes" model="ir.ui.view">
        <field name="name">view_groups_form_custom_reg_notes</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_group.view_groups_form" />
        <field name="arch" type="xml">
            <xpath expr="//page[@name='basic_info']" position="after">
                <page string="Notes">
                    <field name="z_cst_reg_notes" context="{'default_partner_id': active_id}">
                        <tree editable="bottom">
                            <field name="name"/>
                            <field name="description"/>
                        </tree>
                        <form string="Partner Note">
                            <group>
                                <field name="name"/>
                                <field name="description"/>
                            </group>
                        </form>
                    </field>
                </page>
            </xpath>
        </field>
    </record>
</odoo>
```

### 9. Manifest and Security

Update the manifest to include security:

```python
"data": [
    "views/individual_views.xml",
    "views/group_views.xml",
    "security/ir.model.access.csv",
],
```

Create `security/ir.model.access.csv` with access for the G2P Admin group (from `g2p_registry_base.g2p_security`, XML ID `g2p_registry_base.group_g2p_admin`):

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_spp_partner_note_admin,spp.partner.note.admin,model_spp_partner_note,g2p_registry_base.group_g2p_admin,1,1,1,1
```

## Best Practices

1. **Follow OpenSPP Naming Conventions**: Use the `z_cst_` prefix for custom fields. Add `indv`/`grp` when a field is specific to one type.
2. **Extend Existing Views**: Always inherit from existing views rather than creating new ones.
3. **Be Selective**: Only surface fields that add value to users; place them logically in the form/tree.
4. **Test Thoroughly**: Verify both Individual and Group flows where the field appears.
5. **Document Changes**: Update your module README with usage instructions.

## References

For more information on extending Odoo models and views, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Development Guidelines](https://docs.openspp.org/)
- Registry modules referenced: `g2p_registry_group`, `g2p_registry_individual`

---
review-status: needs-review
review-date: 2025-08-15
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Programs

In OpenSPP, program eligibility is managed through a powerful and extensible system called **Eligibility Managers**. An Eligibility Manager is a self-contained component that defines a specific set of rules to determine who is eligible for a program. This allows for creating reusable and complex eligibility logic that can be easily attached to any program.

This guide will walk you through creating a custom Eligibility Manager module from scratch. We will use the `spp_eligibility_tags` module as a practical reference to build a new manager that determines eligibility based on a combination of **registrant tags** and **geographical areas**.

By the end of this guide, you will be able to:

- Understand the role and structure of an Eligibility Manager.
- Create a new model for your custom eligibility rules.
- Implement the core logic to find and enroll beneficiaries.
- Create a user interface for configuring your manager.
- Register your new manager so it can be used in any program.
- Extend the Program Creation Wizard to pre-configure your manager.
- Set up the necessary security access for your new model.

## Prerequisites

- Solid understanding of Odoo 17 module development, including Python, XML, and XPath.
- Familiarity with the OpenG2P and OpenSPP core modules, especially `OpenG2P Programs` (`g2p_programs`), `OpenSPP Programs` (`spp_programs`), and `G2P Registry (Base)` (`g2p_registry_base`).
- To set up OpenSPP for development, please refer to the {doc}`Development Setup Guide <setup>`.

## Module Structure

A typical Eligibility Manager module follows the standard Odoo module structure. Here's the complete structure of our reference module, `spp_eligibility_tags`:
```
spp_eligibility_tags/ 
├── init.py 
├── manifest.py 
├── models/ 
│   ├── init.py 
│   └── eligibility_manager.py # The core manager logic & registration 
├── security/
│   └── ir.model.access.csv 
├── views/
│   └── eligibility_manager_view.xml # The manager's UI
└── wizard/
    ├── init.py
    └── create_program_wizard.py # Extends the program creation wizard
```


---

## Step-by-Step Guide

### Step 1: Create the Module Scaffold

Start by creating a new directory for your module (e.g., `spp_custom_eligibility_manager`) and populate it with the basic Odoo module files and the complete directory structure shown above.

### Step 2: Define the Manifest (`__manifest__.py`)

The manifest file declares your module's metadata and dependencies. It's crucial to list all the modules your customization will interact with. Our manager will depend on `g2p_programs` and `spp_programs` for the base manager framework, and `g2p_registry_base` for using tags and areas.

```python
# __manifest__.py
{
    "name": "OpenSPP Tag Based Eligibility Manager",
    "summary": "Define eligibility criteria for programs based on registrant tags and geographical areas.",
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "category": "OpenSPP",
    "version": "17.0.1.3.0",
    "license": "LGPL-3",
    "depends": [
        "base",
        "g2p_registry_base",
        "g2p_programs",
        "spp_programs",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/create_program_wizard.xml",
        "views/eligibility_manager_view.xml",
    ],
    "installable": True,
    "auto_install": False,
}

```

Your dependencies will vary based on the models and features you need to extend.

### Step 3: Create the Eligibility Manager Model

This is the core of your module. You will create a new model that holds the specific configuration for your eligibility rule and contains the logic to identify eligible registrants.

1.  **Create the model file**: In your `models/` directory, create a Python file named
    `eligibility_manager.py`. Remember to import it in `models/__init__.py`.

2.  **Define the model**:
    - The model name (_name) should be descriptive, like `g2p.program_membership.manager.tags`.
    - Inherit from `g2p.program.membership.manager`. This provides the essential framework for an eligibility manager.
    - Define fields to store the configuration, in this case, the tags and area to be used for filtering.

```python
# From: spp_eligibility_tags/models/eligibility_manager.py

from odoo import api, fields, models

class TagBasedEligibilityManager(models.Model):
    _name = "g2p.program_membership.manager.tags"
    _inherit = ["g2p.program.membership.manager", "g2p.manager.source.mixin"]
    _description = "Tag-based Eligibility"

    tags_id = fields.Many2one("g2p.registrant.tags", string="Tags")
    area_id = fields.Many2one(
        "spp.area",
        domain=lambda self: [("kind", "=", self.env.ref("spp_area_base.admin_area_kind").id)],
    )
    # ... other fields and methods

    def _prepare_eligible_domain(self, membership=None):
        """Builds the Odoo domain to find eligible registrants."""
        domain = []
        domain.extend(self._get_initial_domain(membership=membership))
        domain.extend(self._get_beneficiaries_by_tags())
        return domain

    def import_eligible_registrants(self, state="draft"):
        """Finds and enrolls beneficiaries based on the domain."""
        # ... (logic to search partners with the domain and create memberships) ...
```

The `_prepare_eligible_domain` method is the most critical part. It constructs and returns an Odoo domain that will be used to search for all res.partner records that match the rule.

### Step 4: Register the New Manager

To make OpenSPP aware of your new manager, you must add it to the list of available eligibility managers.

1.  **Extend the `g2p.eligibility.manager` model**: In the same file, `models/eligibility_manager.py`, inherit from `g2p.eligibility.manager`.

2.  **Extend the selection method**: Override the `_selection_manager_ref_id` method to add your new manager's model name and a user-friendly label to the selection list.

```python
# From: spp_eligibility_tags/models/eligibility_manager.py

class EligibilityManager(models.Model):
    _inherit = "g2p.eligibility.manager"

    @api.model
    def _selection_manager_ref_id(self):
        """Register the new manager type."""
        selection = super()._selection_manager_ref_id()
        new_manager = ("g2p.program_membership.manager.tags", "Tag-based Eligibility")
        if new_manager not in selection:
            selection.append(new_manager)
        return selection
```

### Step 5: Create the User Interface

Now, create a form view so that program administrators can configure the tags and area for each instance of your new manager.

```xml
<!-- From: spp_eligibility_tags/views/eligibility_manager_view.xml -->
<record id="view_eligibility_manager_tag_form" model="ir.ui.view">
    <field name="name">view_eligibility_manager_tag_form</field>
    <field name="model">g2p.program_membership.manager.tags</field>
    <field name="arch" type="xml">
        <form string="Tag-based Eligibility Manager">
            <sheet>
                <!-- ... (header and title) ... -->
                <group colspan="4" col="4">
                    <field name="tags_id" colspan="4" required="1" />
                    <field name="area_id" colspan="4" />
                    <!-- ... other fields ... -->
                </group>
            </sheet>
        </form>
    </field>
</record>
```

This simple form will be displayed when a user configures the "Tag-based Eligibility" manager for a program.

### Step 6: Extend the Program Creation Wizard

To improve user experience, you can add configuration fields directly to the "Create Program" wizard. This allows users to set up the basic eligibility rules when they first create the program.

1. **Extend the wizard model**: In your `wizard/` directory, create `create_program_wizard.py`.
   - Inherit from `g2p.program.create.wizard`.
   - Add an `eligibility_kind` selection for your new manager type.
   - Add fields that correspond to your manager's configuration (`tags_id` and `area_id`).
   - Override `_get_eligibility_manager` to pass the data from the wizard to the new manager instance.

```python
# In: wizard/create_program_wizard.py
class SPPCreateNewProgramWiz(models.TransientModel):
    _inherit = "g2p.program.create.wizard"

    eligibility_kind = fields.Selection(
        selection_add=[("tags_eligibility", "Tag-based Eligibility")]
    )
    tags_id = fields.Many2one("g2p.registrant.tags", string="Tags")
    area_id = fields.Many2one("spp.area", ...)

    def _get_eligibility_manager(self, program_id):
        res = super()._get_eligibility_manager(program_id)
        if self.eligibility_kind == "tags_eligibility":
            # Logic to create 'g2p.program_membership.manager.tags'
            # and link it to the program via 'g2p.eligibility.manager'
            # ...
        return res
```

2. **Extend the wizard view**: In `wizard/create_program_wizard.xml`, extend the wizard form to show your new fields.

```xml
<!-- In: wizard/create_program_wizard.xml -->
<record id="create_program_wizard_form_view_custom_eligibility_tags" model="ir.ui.view">
    <field name="name">create_program_wizard_form_view_custom_eligibility_tags</field>
    <field name="model">g2p.program.create.wizard</field>
    <field name="inherit_id" ref="spp_programs.create_program_wizard_form_view_spp" />
    <field name="arch" type="xml">
        <xpath expr="//group[@name='default_eligibility']" position="after">
            <group name='tags_eligibility' invisible="eligibility_kind != 'tags_eligibility'">
                <field name="tags_id" colspan="4" />
                <field name="area_id" colspan="4" />
            </group>
        </xpath>
    </field>
</record>
```

### Step 7: Set Up Security

Grant users access to your new model in `security/ir.model.access.csv`. At a minimum, you need to provide access to the relevant user groups, such as program managers and administrators.

```csv
# From: spp_eligibility_tags/security/ir.model.access.csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
g2p_program_membership_manager_tags_admin,Eligibility Manager Tag-based Admin Access,spp_eligibility_tags.model_g2p_program_membership_manager_tags,g2p_registry_base.group_g2p_admin,1,1,1,1
g2p_program_membership_manager_tags_program_manager,Eligibility Manager Tag-based Program Manager Access,spp_eligibility_tags.model_g2p_program_membership_manager_tags,g2p_programs.g2p_program_manager,1,1,1,0
```

### Step 8: Install and Use Your New Manager

1. Install or upgrade the module through the Apps menu.
2. Navigate to Programs and click ***Create Program***.
3. In the wizard, select your new ***"Tag-based Eligibility"*** manager type.
4. The fields for your manager (e.g., Tags and Area) will appear. Configure them directly in the wizard.
5. Click Create. A new program will be created, and an instance of your eligibility manager will be automatically created and configured with the values you provided.
6. You can verify or update the configuration by navigating to the program's Configuration tab, finding your manager in the list, and opening its form.

## References

For more information on extending Odoo models and views, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Development Guidelines](https://docs.openspp.org/)
- [OpenSPP Programs Module Source](https://github.com/OpenSPP/openspp-modules/tree/17.0/spp_programs)

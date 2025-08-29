---
review-status: needs-review
review-date: 2025-08-17
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Program Entitlements

In OpenSPP, program benefits are defined and calculated through a flexible system called **Entitlement Managers**. An Entitlement Manager is a self-contained component that defines the logic for how much a beneficiary is entitled to receive in a given program cycle. This allows for creating reusable and complex benefit calculation rules that can be easily attached to any program.

This guide will walk you through creating a custom Entitlement Manager module from scratch. We will use the `spp_entitlement_cash` module as a practical reference to build a new manager that calculates cash-based entitlements with flexible rules.

By the end of this guide, you will be able to:

- Understand the role and structure of an Entitlement Manager.
- Create a new model for your custom entitlement rules.
- Implement the core logic to calculate and create entitlements.
- Create a user interface for configuring your manager.
- Register your new manager so it can be used in any program.
- Extend the Program Creation Wizard to pre-configure your manager.
- Set up the necessary security access for your new model.

## Prerequisites

- Solid understanding of Odoo 17 module development, including Python, XML, and XPath.
- Familiarity with the OpenG2P and OpenSPP core modules, especially `OpenG2P Programs` (`g2p_programs`), `OpenSPP Programs` (`spp_programs`), and `G2P Registry (Base)` (`g2p_registry_base`).
- To set up OpenSPP for development, please refer to the {doc}`Development Setup Guide <../setup>`.

## Module Structure

A typical Entitlement Manager module follows the standard Odoo module structure. Here's the complete structure of our reference module, `spp_entitlement_cash`:

```
spp_entitlement_cash/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── entitlement_manager.py # The core manager logic & registration
├── security/
│   └── ir.model.access.csv
├── views/
│   └── entitlement_manager_view.xml # The manager's UI
└── wizard/
    ├── __init__.py
    └── create_program_wizard.py # Extends the program creation wizard
```

---

## Step-by-Step Guide

### Step 1: Create the Module Scaffold

Start by creating a new directory for your module (e.g., `spp_custom_entitlement_manager`) and populate it with the basic Odoo module files and the directory structure shown above.

### Step 2: Define the Manifest (`__manifest__.py`)

The manifest file declares your module's metadata and dependencies. It's crucial to list all the modules your customization will interact with. Our cash entitlement manager depends on `g2p_programs` and `spp_programs` for the base manager framework.

```python
# From: spp_entitlement_cash/__manifest__.py
{
    "name": "OpenSPP Cash Entitlement",
    "summary": "Manage cash-based entitlements for beneficiaries within social protection programs, including defining calculation rules, automating disbursement, and tracking payments.",
    "category": "OpenSPP",
    "version": "17.0.1.3.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "license": "LGPL-3",
    "development_status": "Production/Stable",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "base",
        "g2p_registry_base",
        "g2p_programs",
        "spp_programs",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/entitlement_manager_view.xml",
        "wizard/create_program_wizard.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
```

### Step 3: Create the Entitlement Manager Model

This is the core of your module. You will create a new model that holds the specific configuration for your entitlement rules and contains the logic to calculate and generate entitlements.

1.  **Create the model file**: In your `models/` directory, create a Python file named `entitlement_manager.py`. Remember to import it in `models/__init__.py`.

2.  **Define the model**:
    -   The model name (`_name`) should be descriptive, like `g2p.program.entitlement.manager.cash`.
    -   Inherit from `g2p.base.program.entitlement.manager`. This provides the essential framework for an entitlement manager.
    -   Define fields to store the configuration. In this case, we have a one-to-many field to a separate model, `g2p.program.entitlement.manager.cash.item`, which holds the individual calculation rules.

    ```python
    # From: spp_entitlement_cash/models/entitlement_manager.py

    class G2PCashEntitlementManager(models.Model):
        _name = "g2p.program.entitlement.manager.cash"
        _inherit = [
            "g2p.base.program.entitlement.manager",
            "g2p.manager.source.mixin",
        ]
        _description = "Cash Entitlement Manager"

        entitlement_item_ids = fields.One2many(
            "g2p.program.entitlement.manager.cash.item",
            "entitlement_id",
            "Entitlement Items",
        )
        max_amount = fields.Monetary(...)
        # ... other fields

        def prepare_entitlements(self, cycle, beneficiaries):
            """Prepare Cash Entitlements."""
            # ... (logic to iterate through items and beneficiaries) ...
            for beneficiary_id in beneficiaries_with_entitlements_to_create:
                # ... (calculate amount based on rules) ...
                new_entitlements_to_create[beneficiary_id.id] = {
                    "cycle_id": cycle.id,
                    "partner_id": beneficiary_id.id,
                    "initial_amount": amount,
                    # ... other entitlement values
                }
            # ... (create g2p.entitlement records) ...
    ```

    The `prepare_entitlements` method is the most critical part. It is called by the system to generate the `g2p.entitlement` records for a given cycle and set of beneficiaries, based on the rules defined in the manager.

### Step 4: Register the New Manager

To make OpenSPP aware of your new manager, you must add it to the list of available entitlement managers.

1.  **Extend the `g2p.program.entitlement.manager` model**: In the same file, `models/entitlement_manager.py`, inherit from `g2p.program.entitlement.manager`.

2.  **Extend the selection method**: Override the `_selection_manager_ref_id` method to add your new manager's model name and a user-friendly label to the selection list.

    ```python
    # From: spp_entitlement_cash/models/entitlement_manager.py

    class EntitlementManager(models.Model):
        _inherit = "g2p.program.entitlement.manager"

        @api.model
        def _selection_manager_ref_id(self):
            selection = super()._selection_manager_ref_id()
            new_manager = ("g2p.program.entitlement.manager.cash", "Cash")
            if new_manager not in selection:
                selection.append(new_manager)
            return selection
    ```

### Step 5: Create the User Interface

Create a form view so that program administrators can configure the rules for your new manager.

```xml
<!-- From: spp_entitlement_cash/views/entitlement_manager_view.xml -->
<record id="view_entitlement_manager_cash_form" model="ir.ui.view">
    <field name="name">view_entitlement_manager_cash_form</field>
    <field name="model">g2p.program.entitlement.manager.cash</field>
    <field name="arch" type="xml">
        <form string="Cash Entitlement Manager">
            <sheet>
                <!-- ... (header and title) ... -->
                <group>
                    <field name="entitlement_item_ids" nolabel="1" colspan="4">
                        <tree>
                            <field name="amount" />
                            <field name="multiplier_field" />
                            <field name="max_multiplier" />
                        </tree>
                        <!-- ... (form view for items) ... -->
                    </field>
                </group>
            </sheet>
        </form>
    </field>
</record>
```

### Step 6: Extend the Program Creation Wizard

To improve user experience, add configuration fields directly to the "Create Program" wizard.

1.  **Extend the wizard model**: In `wizard/create_program_wizard.py`, inherit from `g2p.program.create.wizard`, add an `entitlement_kind` selection for your new manager, and override `_get_entitlement_manager` to handle its creation.

    ```python
    # In: wizard/create_program_wizard.py
    class G2PCreateNewProgramWiz(models.TransientModel):
        _inherit = "g2p.program.create.wizard"

        entitlement_kind = fields.Selection(selection_add=[("cash", "Cash")])
        entitlement_cash_item_ids = fields.One2many(...)

        def _get_entitlement_manager(self, program_id):
            res = super()._get_entitlement_manager(program_id)
            if self.entitlement_kind == "cash":
                # Logic to create 'g2p.program.entitlement.manager.cash'
                # and link it to the program via 'g2p.program.entitlement.manager'
                # ...
            return res
    ```

2.  **Extend the wizard view**: In `wizard/create_program_wizard.xml`, extend the form to show your new fields when the "Cash" entitlement kind is selected.

### Step 7: Set Up Security

Grant users access to your new models in `security/ir.model.access.csv`.

```
# From: spp_entitlement_cash/security/ir.model.access.csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
g2p_program_entitlement_manager_cash_admin,Program Entitlement Manager Cash Admin Access,spp_entitlement_cash.model_g2p_program_entitlement_manager_cash,g2p_registry_base.group_g2p_admin,1,1,1,1
g2p_program_entitlement_manager_cash_program_manager,Program Entitlement Manager Cash Program Manager Access,spp_entitlement_cash.model_g2p_program_entitlement_manager_cash,g2p_programs.g2p_program_manager,1,1,1,0
```

### Step 8: Install and Test

1.  Install or upgrade the module through the Apps menu.
2.  Navigate to **Programs** and click **Create Program**.
3.  In the wizard, under the **Entitlement** page, select your new **"Cash"** manager type from the **Manager** dropdown.
4.  The fields for your manager will appear, allowing you to define entitlement rules directly in the wizard.
5.  Click **Create**. A new program will be created, and an instance of your entitlement manager will be automatically created and configured.

## References

For more information on extending OpenSPP modules, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Documentation](https://docs.openspp.org/)
- [OpenSPP Programs Module Source](https://github.com/OpenSPP/openspp-modules/tree/17.0/spp_programs)

---
review-status: needs-review
review-date: 2025-08-20
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Program Cycles

In OpenSPP, the creation and scheduling of program cycles are handled by a flexible system called **Cycle Managers**. A Cycle Manager is a self-contained component that defines the logic for how and when new cycles are created for a program. This allows for creating reusable and complex cycle generation rules that can be easily attached to any program.

This guide will walk you through creating a custom Cycle Manager module from scratch. We will build a new manager based on the default one, but with a specific business rule: creating cycles with a fixed six-month duration, regardless of other settings.

By the end of this guide, you will be able to:

- Understand the role and structure of a Cycle Manager.
- Create a new model for your custom cycle generation rules.
- Implement the core logic to override cycle date calculations.
- Create a user interface for configuring your manager.
- Register your new manager so it can be used in any program.
- Extend the Program Creation Wizard to pre-configure your manager.
- Set up the necessary security access for your new model.

## Prerequisites

- Solid understanding of Odoo 17 module development, including Python, XML, and XPath.
- Familiarity with the OpenG2P and OpenSPP core modules, especially `OpenG2P Programs` (`g2p_programs`) and `OpenSPP Programs` (`spp_programs`).
- To set up OpenSPP for development, please refer to the {doc}`Development Setup Guide <setup>`.

## Module Structure

A typical Cycle Manager module follows the standard Odoo module structure. Here's the complete structure of the module we will build, `spp_cycle_manager_fixed_interval`:

```
spp_cycle_manager_fixed_interval/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── cycle_manager.py # The core manager logic & registration
├── security/
│   └── ir.model.access.csv
├── views/
│   └── cycle_manager_view.xml # The manager's UI
└── wizard/
    ├── __init__.py
    └── create_program_wizard.py # Extends the program creation wizard
```

---

## Step-by-Step Guide

### Step 1: Create the Module Scaffold

Start by creating a new directory for your module (e.g., `spp_cycle_manager_fixed_interval`) and populate it with the basic Odoo module files and the directory structure shown above.

### Step 2: Define the Manifest (`__manifest__.py`)

The manifest file declares your module's metadata and dependencies. Our cycle manager depends on `g2p_programs` and `spp_programs` for the base manager framework.

```python
# From: spp_cycle_manager_fixed_interval/__manifest__.py
{
    "name": "OpenSPP Fixed Interval Cycle Manager",
    "summary": "A cycle manager that creates cycles with a fixed six-month duration.",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "license": "LGPL-3",
    "depends": [
        "g2p_programs",
        "spp_programs",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/cycle_manager_view.xml",
        "wizard/create_program_wizard.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
```

### Step 3: Create the Cycle Manager Model

This is the core of your module. You will create a new model that inherits from the default cycle manager and overrides its behavior.

1.  **Create the model file**: In your `models/` directory, create a Python file named `cycle_manager.py`. Remember to import it in `models/__init__.py`.

2.  **Define the model**:
    -   The model name (`_name`) should be descriptive, like `g2p.cycle.manager.fixed.interval`.
    -   Inherit from `g2p.cycle.manager.default`. This provides the essential framework and fields of the default cycle manager.
    -   Override the `_get_end_date` method. This is where we'll inject our custom logic to enforce a six-month duration.

    ```python
    # From: spp_cycle_manager_fixed_interval/models/cycle_manager.py
    from dateutil.relativedelta import relativedelta
    from odoo import api, models

    class FixedIntervalCycleManager(models.Model):
        _name = "g2p.cycle.manager.fixed.interval"
        _inherit = "g2p.cycle.manager.default"
        _description = "Fixed Interval Cycle Manager"

        def _get_end_date(self, start_date):
            """Override to set a fixed 6-month end date, ignoring cycle_duration."""
            return start_date + relativedelta(months=6, days=-1)
    ```

### Step 4: Register the New Manager

To make OpenSPP aware of your new manager, you must add it to the list of available cycle managers.

1.  **Extend the `g2p.cycle.manager` model**: In the same file, `models/cycle_manager.py`, inherit from `g2p.cycle.manager`.

2.  **Extend the selection method**: Override the `_selection_manager_ref_id` method to add your new manager's model name and a user-friendly label to the selection list.

    ```python
    # From: spp_cycle_manager_fixed_interval/models/cycle_manager.py

    class CycleManager(models.Model):
        _inherit = "g2p.cycle.manager"

        @api.model
        def _selection_manager_ref_id(self):
            selection = super()._selection_manager_ref_id()
            new_manager = ("g2p.cycle.manager.fixed.interval", "Fixed 6-Month Interval")
            if new_manager not in selection:
                selection.append(new_manager)
            return selection
    ```

### Step 5: Create the User Interface

Create a form view for your manager. Since we are inheriting from the default manager, we can also inherit its view and modify it to hide the fields that are no longer relevant (like the recurrence rules).

```xml
<!-- From: spp_cycle_manager_fixed_interval/views/cycle_manager_view.xml -->
<record id="view_cycle_manager_fixed_interval_form" model="ir.ui.view">
    <field name="name">view_cycle_manager_fixed_interval_form</field>
    <field name="model">g2p.cycle.manager.fixed.interval</field>
    <field name="inherit_id" ref="g2p_programs.view_cycle_manager_default_form"/>
    <field name="arch" type="xml">
        <xpath expr="//field[@name='cycle_duration']" position="attributes">
            <attribute name="invisible">1</attribute>
        </xpath>
        <xpath expr="//group[field[@name='rrule_type']]" position="attributes">
            <attribute name="invisible">1</attribute>
        </xpath>
        <xpath expr="//group[field[@name='rrule_type']]" position="before">
            <group>
                <p>This manager automatically creates cycles with a fixed six-month duration. The recurrence settings below are ignored.</p>
            </group>
        </xpath>
    </field>
</record>
```

### Step 6: Extend the Program Creation Wizard

To improve user experience, add a selection to the "Create Program" wizard so users can choose your new manager from the start.

1.  **Extend the wizard model**: In `wizard/create_program_wizard.py`, inherit from `g2p.program.create.wizard`, add a `cycle_manager_kind` selection, and override `create_program` to handle the creation of your custom manager.

    ```python
    # In: spp_cycle_manager_fixed_interval/wizard/create_program_wizard.py
    from odoo import _, fields, models

    class CustomCycleManagerWizard(models.TransientModel):
        _inherit = "g2p.program.create.wizard"

        cycle_manager_kind = fields.Selection(
            selection_add=[("fixed_interval", "Fixed 6-Month Interval")],
            string="Cycle Manager Type",
            default='default'
        )

        def create_program(self):
            if self.cycle_manager_kind != 'fixed_interval':
                return super().create_program()

            self._check_required_fields()
            rec = self
            program_vals = rec.get_program_vals()
            program = self.env["g2p.program"].create(program_vals)
            program_id = program.id
            vals = {}
            vals.update(rec._get_eligibility_manager(program_id))

            # Create our custom cycle manager
            cycle_manager_default_val = rec.get_cycle_manager_default_val(program_id)
            fixed_interval_mgr = self.env["g2p.cycle.manager.fixed.interval"].create(cycle_manager_default_val)
            mgr = self.env["g2p.cycle.manager"].create({
                "program_id": program_id,
                "manager_ref_id": f"{fixed_interval_mgr._name},{str(fixed_interval_mgr.id)}",
            })
            vals.update({"cycle_managers": [(4, mgr.id)]})

            vals.update(rec._get_entitlement_manager(program_id))
            vals.update({"is_one_time_distribution": rec.is_one_time_distribution})
            program.update(vals)

            if rec.import_beneficiaries == "yes":
                rec.program_wizard_import_beneficiaries(program)
            if rec.is_one_time_distribution:
                program.create_new_cycle()

            view_id = self.env.ref("g2p_programs.view_program_list_form")
            if rec.view_id:
                view_id = rec.view_id
            program.view_id = view_id.id

            return {
                "name": _("Programs"),
                "view_mode": "form",
                "res_model": "g2p.program",
                "res_id": program_id,
                "view_id": view_id.id,
                "type": "ir.actions.act_window",
                "target": "current",
            }
    ```

2.  **Extend the wizard view**: In `wizard/create_program_wizard.xml`, extend the form to show your new selection field and hide the default recurrence rules when your manager is selected.

    ```xml
    <!-- In: spp_cycle_manager_fixed_interval/wizard/create_program_wizard.xml -->
    <record id="create_program_wizard_form_view_custom_cycle" model="ir.ui.view">
        <field name="name">create_program_wizard_form_view_custom_cycle</field>
        <field name="model">g2p.program.create.wizard</field>
        <field name="inherit_id" ref="g2p_programs.create_program_wizard_form_view"/>
        <field name="arch" type="xml">
            <xpath expr="//page[@name='cycle']/group[1]" position="before">
                <group>
                    <field name="cycle_manager_kind" widget="radio" options="{'horizontal': true}"/>
                </group>
            </xpath>
            <xpath expr="//page[@name='cycle']/group/div/group[2]" position="attributes">
                <attribute name="invisible">cycle_manager_kind == 'fixed_interval'</attribute>
            </xpath>
        </field>
    </record>
    ```

### Step 7: Set Up Security

Grant users access to your new model in `security/ir.model.access.csv`.

```csv
# From: spp_cycle_manager_fixed_interval/security/ir.model.access.csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
g2p_cycle_manager_fixed_interval_admin,Cycle Manager Fixed Interval Admin Access,spp_cycle_manager_fixed_interval.model_g2p_cycle_manager_fixed_interval,g2p_registry_base.group_g2p_admin,1,1,1,1
g2p_cycle_manager_fixed_interval_program_manager,Cycle Manager Fixed Interval Program Manager Access,spp_cycle_manager_fixed_interval.model_g2p_cycle_manager_fixed_interval,g2p_programs.g2p_program_manager,1,1,1,0
```

### Step 8: Install and Test

1.  Install or upgrade the module through the Apps menu.
2.  Navigate to **Programs** and click **Create Program**.
3.  In the wizard, on the **Cycle** page, select your new **"Fixed 6-Month Interval"** manager type.
4.  Notice that the recurrence settings disappear.
5.  Complete the wizard and click **Create**. A new program will be created, and an instance of your cycle manager will be automatically created and configured. When new cycles are created for this program, they will automatically have a six-month duration.

## References

For more information on extending Odoo models and views, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Development Guidelines](https://docs.openspp.org/)
- [OpenSPP Programs Module Source](https://github.com/OpenSPP/openspp-modules/tree/17.0/spp_programs)
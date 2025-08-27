---
review-status: needs-review
review-date: 2025-08-27
reviewer: "Edwin Gonzales"
migration-notes: "Added during 2025 documentation reorganization"
---

# Module Development

OpenSPP is built on the powerful and flexible Odoo framework. One of the core principles of Odoo is its modular architecture. Instead of modifying the core source code of the platform, customizations and new features are added through self-contained packages called **modules**.

This guide will walk you through the fundamental process of creating a custom OpenSPP module. We will build a simple but practical module that adds a "National ID" field to the Individual record in the registry.

By the end of this guide, you will understand:
- Why creating a custom module is the best practice.
- The basic structure of an OpenSPP/Odoo module.
- How to extend existing models to add new data fields.
- How to modify user interface forms to display these new fields.
- The complete process for installing and activating your custom module.

### Why Create a Custom Module?

For developers new to Odoo, it might seem easier to directly edit the existing OpenSPP files. However, this approach, often called forking, leads to significant long-term problems. The recommended approach is to encapsulate all your customizations within a custom module.

**Key Advantages of Using Modules:**

- **Maintainability & Upgradability:** When a new version or security patch for OpenSPP is released, you can update the core platform code without losing your custom features. Your module remains separate and can be easily installed on the new version, often with minimal changes.
- **Cleanliness & Organization:** Your custom code is neatly organized in its own directory, making it easy to find, understand, and manage.
- **Portability:** You can easily share your module with other projects or deploy it on different OpenSPP instances.
- **Collaboration:** It allows multiple teams to work on different custom features without creating conflicts in the core codebase.

In short, creating modules is the professional standard for Odoo and OpenSPP development that ensures your solution is robust and future-proof.

This modular approach is the foundation for all advanced customizations. From here, you can explore:
- Adding more complex field types (Selection, Many2one, etc.).
- Creating entirely new models and menus.
- Adding business logic with Python methods.
- Building more advanced features documented in the {doc}`customization/index` guides.

By mastering this pattern, you can tailor OpenSPP to meet any specific program requirement while ensuring your implementation remains clean, stable, and easy to maintain.

## Best Practices in OpenSPP Development

OpenSPP follows the coding standards of the Odoo Community Association (OCA), which are designed to ensure high-quality, maintainable, and consistent code. While the full guidelines are extensive, here are some of the most important best practices to follow:

-   **Follow Python and Odoo Coding Standards:**
    -   Adhere to **PEP8** guidelines for Python code.
    -   Use tools like `black` for code formatting, `isort` for import sorting, and `flake8` for linting to maintain consistency.
    -   Follow Odoo's import order: standard Python libraries, third-party libraries, then Odoo and OpenSPP modules.

-   **Write Clean and Readable XML:**
    -   Use a consistent naming convention for record IDs. For example: `view_model_name_form`, `action_model_name_window`.
    -   Logically order fields in views to create an intuitive user experience.

-   **Prioritize Security and Extensibility:**
    -   Always define access rights in `security/ir.model.access.csv`. Never grant universal access (`group_id:id,"",...`) without a strong reason.
    -   Avoid using raw SQL queries. Use the Odoo ORM to ensure security rules are respected.
    -   Always use `_inherit` and `xpath` to extend existing functionality. Never modify core OpenSPP or Odoo files directly.

-   **Adhere to Licensing Requirements:**
    -   All custom modules for OpenSPP must be licensed under **LGPL-3**.
    -   Ensure that any third-party Python libraries or other dependencies you add are compatible with the LGPL-3 license.

## Prerequisites

- A working OpenSPP development environment. See the {doc}`setup` guide for instructions.
- Solid understanding of Odoo 17 module development.
- Knowledge of Python, Odoo, XML, and XPaths.

## Module Structure

We will create a module named `spp_custom_registry_fields`. A standard Odoo module has a specific directory structure. Here is what ours will look like:

```
spp_custom_registry_fields/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── registry_models.py
└── views/
    └── registry_views.xml
```

- **`__manifest__.py`**: A metadata file that describes the module, its dependencies, and which files to load.
- **`__init__.py`**: Python files that make directories importable.
- **`models/`**: Contains the Python files that define or extend the data models (the database structure).
- **`views/`**: Contains the XML files that define the user interface (forms, lists, etc.).

---

## Step-by-Step Guide

### Step 1: Create the Module Scaffold

First, navigate to your `custom/src` directory (or wherever you store your custom addons) and create the directory for your new module.

```bash
mkdir spp_custom_registry_fields
```

Inside this new directory, create the files and subdirectories as shown in the structure above. You can use these commands:

```bash
cd spp_custom_registry_fields
touch __init__.py
touch __manifest__.py
mkdir models
touch models/__init__.py
touch models/registry_models.py
mkdir views
touch views/registry_views.xml
```

### Step 2: Define the Manifest (`__manifest__.py`)

The manifest file is the entry point for your module. It tells Odoo what your module is, who made it, and what it depends on.

Open `spp_custom_registry_fields/__manifest__.py` and add the following code:

```python
# __manifest__.py
{
    "name": "OpenSPP Custom Registry Fields",
    "summary": "Adds a custom National ID field to the Individual registry record.",
    "author": "Your Name",
    "website": "https://openspp.org",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "license": "LGPL-3",
    "depends": [
        "g2p_registry_individual",  # We need this to extend the registry models and views
    ],
    "data": [
        # We will load the view file here. Security files would also go here.
        "views/registry_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
```

The `depends` key is crucial. It ensures that the `g2p_registry_individual` module is loaded before our module, so we can successfully extend its models and views. The `data` key lists the XML files that should be parsed and loaded.

### Step 3: Extend the Data Models

Now, let's add our new fields to the database schema. We do this by "inheriting" the existing models and adding our fields.

1.  **Import the models file:**
    Open `spp_custom_registry_fields/__init__.py` and add this line to make the `models` directory visible to Python:

    ```python
    from . import models
    ```

2.  **Import the Python file:**
    Open `spp_custom_registry_fields/models/__init__.py` and add this line to load our new model file:

    ```python
    from . import registry_models
    ```

3.  **Define the fields:**
    Open `spp_custom_registry_fields/models/registry_models.py` and add the following code:

    ```python
    from odoo import fields, models

    class ResPartner(models.Model):
        """
        Inherit the res.partner model to add a national ID field.
        In OpenSPP, res.partner represents an Individual or a group.
        """
        _inherit = "res.partner"

        national_id = fields.Char(string="National ID")
    ```

    - `_inherit = "res.partner"` tells Odoo that this class is extending the existing `res.partner` model.
    - `national_id = fields.Char(...)` defines a new field named `national_id` of type `Char` (a string of text).

### Step 4: Display the New Fields in the User Interface

Our fields now exist in the database, but they are not visible on any forms. We need to extend the existing views to add them. We use `xpath` to pinpoint exactly where in the original form we want to add our new field.

Open `spp_custom_registry_fields/views/registry_views.xml` and add the following code:

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <!-- Inherit the Individual form view to add the National ID field -->
    <record id="view_partner_form_custom" model="ir.ui.view">
        <field name="name">res.partner.form.custom</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="g2p_registry_individual.view_individuals_form"/>
        <field name="arch" type="xml">
            <!-- Add the new field after the 'gender' field -->
            <xpath expr="//field[@name='gender']" position="after">
                <field name="national_id"/>
            </xpath>
        </field>
    </record>
</odoo>
```

- `inherit_id`: This specifies which original view we are extending. We use the full external ID: `module_name.view_id`.
- `xpath`: This is the powerful part. `expr="//field[@name='gender']"` finds the field named `gender` in the form. `position="after"` tells Odoo to insert our code block immediately after that field.

### Step 5: Install Your Module

Your module is now complete and ready to be installed.

1.  **Ensure Addons Path is Correct:** Your custom module's parent directory (e.g., `custom/src`) must be listed in your Odoo server's `addons_path`.

2.  **Restart the Odoo Server:** You must restart the server for Odoo to discover the new module. If you are using `invoke start`, you can stop it with `Ctrl+C` and run it again.

3.  **Activate Developer Mode:**
    - In your browser, log in to your OpenSPP instance.
    - Go to **Settings**.
    - Scroll to the bottom and click **Activate the developer mode**. A bug icon will appear in the header.

4.  **Update the Apps List:**
    - Go to the **Apps** menu.
    - In the top menu, click on **Update Apps List**.
    - A confirmation dialog will appear. Click **Update**.

5.  **Install the Module:**
    - In the **Apps** menu, clear the default "Apps" filter from the search bar.
    - Search for your module's name: `spp_custom_registry_fields`.
    - You will see your module. Click the **Activate** button.

The page will reload, and your module will be installed.

### Step 6: Verify the Changes

Let's confirm that our new fields are visible.

**Check the Individual Form:**
    - Navigate to **Registry -> Individuals**.
    - Click on any existing individual or create a new one.
    - You should now see the **National ID** field right below the **Sex** (gender) field.

## References

For more information on extending OpenSPP models and views, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Development Guidelines](https://docs.openspp.org/)
- [OpenSPP Source](https://github.com/OpenSPP/openspp-modules/tree/17.0/)

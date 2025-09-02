
# Dashboards

In OpenSPP, dashboards provide a powerful way to visualize key metrics and data at a glance. They are built using the Odoo OWL framework, allowing for dynamic, interactive, and real-time reporting. A custom dashboard is a self-contained module that fetches data from the server and presents it using various UI components like charts and summary cards.

This guide will walk you through creating a custom dashboard module from scratch. We will develop the `spp_custom_dashboard` module to build a new dashboard that displays key statistics from the OpenSPP Farmer Registry.

By the end of this guide, you will be able to:

- Understand the structure of a dashboard module.
- Create a server-side method to fetch and prepare data.
- Implement a client-side OWL component for the dashboard.
- Design the dashboard layout using XML templates.
- Use pre-built components like charts and cards.
- Register your dashboard to make it accessible from the Odoo menu.

## Prerequisites

- Solid understanding of Odoo 17 module development, including Python, XML, XPath, and JavaScript (specifically the OWL framework).
- Familiarity with the OpenG2P and OpenSPP core modules, especially `OpenSPP Dashboard (Base)` (`spp_dashboard_base`) and `OpenSPP Farmer Registry (Base)` (`spp_farmer_registry_base`).
- To set up OpenSPP for development, please refer to the {doc}`Development Setup Guide <../setup>`.

## Module Structure

A typical dashboard module follows a standard Odoo module structure. Here's the complete structure of our example module, `spp_custom_dashboard`:

```
spp_custom_dashboard/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── res_partner.py         # Data-fetching logic
├── static/
│   └── src/
│       └── dashboard/
│           ├── dashboard.js   # OWL component for the dashboard
│           └── dashboard.xml  # XML template for the dashboard layout
└── views/
    └── dashboard_views.xml    # Client action and menu item
```
---

## Step-by-Step Guide

### Create the Module Scaffold

Start by creating a new directory for your module (e.g., `spp_custom_dashboard`) and populate it with the basic Odoo module files and the directory structure shown above.

### Define the Manifest (`__manifest__.py`)

The manifest file declares your module's metadata and dependencies. It's crucial to list all the modules your customization will interact with. Our dashboard depends on `spp_dashboard_base` for the core dashboard components and `spp_farmer_registry_base` for the data.

```python
# In: spp_custom_dashboard/__manifest__.py
{
    "name": "OpenSPP Custom Dashboard",
    "summary": "A custom dashboard to display key metrics from the Farmer Registry.",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "license": "LGPL-3",
    "depends": [
        "spp_dashboard_base",
        "spp_farmer_registry_base",
    ],
    "data": [
        "views/dashboard_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "spp_custom_dashboard/static/src/dashboard/**/*",
        ],
    },
    "application": True,
    "installable": True,
}
```

### Prepare the Data on the Server (Python)

The dashboard needs data to display. We'll create a method on an existing model to gather and format this data. For our example, we'll extend the `res.partner` model, which represents farms and farmers in the `spp_farmer_registry_base` module.

1.  **Create the model file**: In your `models/` directory, create a Python file named `res_partner.py`. Remember to import it in `models/__init__.py`.

2.  **Define the data-fetching method**:
    -   Extend the `res.partner` model.
    -   Create a method, for example, `get_farmer_dashboard_data`, that will be called from the client-side component.
    -   This method will search for farms and farmers and aggregate the data into a dictionary.

    ```python
    # In: spp_custom_dashboard/models/res_partner.py
    from odoo import api, models

    class Partner(models.Model):
        _inherit = "res.partner"

        @api.model
        def get_farmer_dashboard_data(self):
            """Fetch and prepare data for the farmer registry dashboard."""
            farm_kind_id = self.env.ref("spp_farmer_registry_base.kind_farm")
            farms = self.search([("kind", "=", farm_kind_id.id)])
            farmers = self.search([("is_registrant", "=", True), ("is_group", "=", False)])

            # Data for a chart: Farms by Type
            farm_types = {
                "crop": 0,
                "livestock": 0,
                "aquaculture": 0,
                "mixed": 0,
            }
            for farm in farms:
                if farm.details_farm_type in farm_types:
                    farm_types[farm.details_farm_type] += 1

            return {
                # Data for CardBoard components
                "total_farms": len(farms),
                "total_farmers": len(farmers),

                # Data for ChartComponent
                "farm_types_data": list(farm_types.values()),
                "farm_types_labels": [label.capitalize() for label in farm_types.keys()],
            }
    ```

### Create the Dashboard Component (JavaScript)

The client-side component is responsible for calling the server to get the data and rendering the dashboard template.

1.  **Create the JavaScript file**: In `static/src/dashboard/`, create `dashboard.js`.

2.  **Implement the OWL component**:
    -   Import `SppDashboard` from the base dashboard module.
    -   Extend the `SppDashboard` class.
    -   Use the `onWillStart` lifecycle hook to call your Python method using the `orm` service.
    -   Store the fetched data in `this.dashboard_data` to make it available in the template.
    -   Register your new component in the `actions` registry with a unique tag.

    ```javascript
    // In: spp_custom_dashboard/static/src/dashboard/dashboard.js
    /** @odoo-module **/

    import { SppDashboard } from "@spp_dashboard_base/dashboard/dashboard";
    import { registry } from "@web/core/registry";

    export class CustomDashboard extends SppDashboard {
        setup() {
            super.setup();
            this.dashboard_title = "Farmer Registry Dashboard";
        }

        async onWillStart() {
            await super.onWillStart();
            this.dashboard_data = await this.orm.call(
                "res.partner",
                "get_farmer_dashboard_data",
                []
            );
        }
    }

    CustomDashboard.template = "spp_custom_dashboard.dashboard_page";

    registry.category("actions").add("spp_custom_dashboard_tag", CustomDashboard);
    ```

### Design the Dashboard Layout (XML)

The XML template defines the structure and appearance of your dashboard. It uses the data prepared by the JavaScript component.

1.  **Create the XML file**: In `static/src/dashboard/`, create `dashboard.xml`.

2.  **Define the template**:
    -   Create a template with a unique name (e.g., `spp_custom_dashboard.dashboard_page`).
    -   Use the `CardBoardComponent` and `ChartComponent` provided by `spp_dashboard_base`.
    -   Pass the data from `dashboard_data` to the components' props.

    ```xml
    <!-- In: spp_custom_dashboard/static/src/dashboard/dashboard.xml -->
    <?xml version="1.0" encoding="UTF-8" ?>
    <templates>
        <t t-name="spp_custom_dashboard.dashboard_page">
            <div class="main" style="height: 100vh; overflow-y: auto;">
                <div class="title" name="title">
                    <center>
                        <h1><t t-esc="dashboard_title" /></h1>
                    </center>
                </div>
                <div class="container dashboard-container" name="dashboard-container">
                    <div class="row card-section">
                        <CardBoardComponent
                            size="'col-md-6'"
                            data="dashboard_data.total_farms"
                            title="'Total Farms'"
                        />
                        <CardBoardComponent
                            size="'col-md-6'"
                            data="dashboard_data.total_farmers"
                            title="'Total Farmers'"
                        />
                    </div>
                    <br />
                    <br />
                    <div class="row chart-section" style="padding-bottom: 10em">
                        <ChartComponent
                            labels="dashboard_data.farm_types_labels"
                            data_label="'Farms by Type'"
                            data="dashboard_data.farm_types_data"
                            backgroundColor="['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']"
                            chart_type="'pie'"
                        />
                    </div>
                </div>
            </div>
        </t>
    </templates>
    ```

### Register the Dashboard

Finally, create a client action and a menu item to make your dashboard accessible in the Odoo interface.

1.  **Create the view file**: In the `views/` directory, create `dashboard_views.xml`.

2.  **Define the action and menu**:
    -   Create an `ir.actions.client` record. The `tag` must match the one you registered in your JavaScript file (`spp_custom_dashboard_tag`).
    -   Create a `menuitem` that calls this client action.

    ```xml
    <!-- In: spp_custom_dashboard/views/dashboard_views.xml -->
    <odoo>
        <record id="custom_dashboard_action" model="ir.actions.client">
            <field name="name">Farmer Dashboard</field>
            <field name="tag">spp_custom_dashboard_tag</field>
        </record>

        <menuitem
            id="custom_dashboard_menu"
            name="Dashboard"
            sequence="1"
            action="custom_dashboard_action"
            parent="g2p_registry_base.g2p_main_menu_root"
        />
    </odoo>
    ```

### Install and View Your Dashboard

1.  Install or upgrade the module through the Apps menu.
2.  Refresh your browser.
3.  Navigate to the main menu, and you should see a new "Dashboard" menu item. Click it to view your custom dashboard.

## References

For more information on extending OpenSPP modules, refer to:
- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer/)
- [OpenSPP Dashboard Base Module Source](https://github.com/OpenSPP/openspp-modules/tree/17.0/spp_dashboard_base)

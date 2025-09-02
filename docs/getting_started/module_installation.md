---
review-status: needs-review
review-date: 2025-08-28
reviewer: Edwin Gonzales
migration-notes: "Added during 2025 documentation reorganization"
myst:
  html_meta:
    "title": "OpenSPP Module Installation Guide"
    "description": "Step-by-step guide for installing and configuring OpenSPP modules including SP-MIS, Social Registry, and Farmer Registry"
    "keywords": "OpenSPP, modules, installation, Odoo, SP-MIS, Social Registry, Farmer Registry"
---

# Module installation

OpenSPP's modular architecture allows organizations to deploy only the features they need. Built on Odoo 17, the platform extends functionality through specialized modules that can be mixed and matched to create tailored social protection solutions. This guide covers installing OpenSPP modules for different use cases.

## Prerequisites

Before installing OpenSPP modules, ensure you have:

- **Odoo 17 instance** running and accessible
- **OpenSPP modules** source code from the [OpenSPP repository](https://github.com/OpenSPP/openspp-modules/tree/17.0/)
- **Addons path** configured to include the `openspp-modules` directory
- **Administrator access** to your Odoo instance
- **Developer mode** knowledge (required for module installation)

:::{tip}
For development setup instructions, see the {doc}`Development Setup Guide <../developer_guide/setup>`.
:::

## General installation process

Installing an Odoo module, including those for OpenSPP, follows a standard procedure:

1.  **Place Modules in Addons Path**: Ensure the `openspp-modules` directory is included in your Odoo configuration's `addons_path`.
2.  **Update Apps List**:
    -   Log in to your Odoo instance with administrator privileges.
    -   Activate the developer mode.
    -   Navigate to the **Apps** menu.
    -   Click on **Update Apps List** and confirm the update.
3.  **Install the Module**:
    -   In the **Apps** menu, clear the default "Apps" filter from the search bar.
    -   Search for the desired module by its technical name or title.
    -   Click the **Activate** button on the module's card to begin the installation.

![](module_installation/01-apps-ui.jpg)

## Installation setups

OpenSPP can be configured in different ways depending on your project's needs. Below are the installation guides for three primary setups.

:::{important}
The **SP-MIS** ({doc}`spp_base </reference/modules/spp_base>`), and **Farmer Registry** ({doc}`spp_farmer_registry_base </reference/modules/spp_farmer_registry_base>`) modules are mutually exclusive. You can only have one of them installed in a single Odoo database. Attempting to install multiple base modules will result in an error.
:::

### 1. SP-MIS installation (spp_base)

The Social Protection Management Information System ({doc}`SP-MIS <../overview/products/sp_mis>`) configuration provides comprehensive functionality for managing social protection programs. This setup is ideal for organizations running cash transfers, social assistance programs, or humanitarian interventions.

**What's Included:**
- Registry management for individuals and groups
- Program cycles and beneficiary enrollment
- Eligibility determination and targeting
- Entitlement calculation and management
- Payment processing integration

**Installation Steps:**

1.  Follow the General Installation Process to update your Apps list
2.  In the Apps menu, search for {doc}`spp_base </reference/modules/spp_base>` or "OpenSPP Base"

![](module_installation/02-spp_base01.jpg)

3.  Click the **Activate** button to install the module. This will also install all its dependencies, providing a complete SP-MIS foundation.

![](module_installation/03-spp_base2.jpg)

Once installed, you will see the "Registry" application in your Odoo dashboard, which is the main entry point for the OpenSPP system.

![](module_installation/04-spp_base3.jpg)

### 2. Social Registry installation (spp_registry_base)

The {doc}`Social Registry <../overview/products/social_registry>` configuration provides a centralized repository for beneficiary data that can be shared across multiple social protection programs. This setup is ideal for governments and organizations coordinating multiple interventions and requiring a single source of truth for beneficiary information.

**What's Included:**
- Unified beneficiary database across programs
- Advanced deduplication and data quality management
- Dynamic registration and needs assessment
- Inter-program data sharing and coordination
- Household composition and relationship tracking
- Socioeconomic data collection and analysis
- Data privacy and access control mechanisms

**Installation Steps:**

1.  Follow the General Installation Process to update your Apps list
2.  In the Apps menu, search for {doc}`spp_registry_base </reference/modules/spp_registry_base>` or "OpenSPP Social Registry"
3.  Click the **Activate** button to install the module and its dependencies

Once installed, the Social Registry becomes the central hub for managing beneficiary data that can be accessed by various social protection programs.

### 3. Farmer Registry installation (spp_farmer_registry_base)

The {doc}`Farmer Registry <../overview/products/farmer_registry>` configuration enables convergence between social protection and agricultural development programs. This setup is designed for organizations supporting smallholder farmers, managing agricultural subsidies, or implementing climate-smart agriculture initiatives.

**What's Included:**
- Farmer and farm household registration
- Land parcel mapping with GIS integration
- Crop and livestock tracking
- Agricultural input distribution management
- Seasonal cycle management
- Integration with agricultural extension services

**Installation Steps:**

1.  Follow the General Installation Process to update your Apps list
2.  In the Apps menu, search for {doc}`spp_farmer_registry_base </reference/modules/spp_farmer_registry_base>` or "OpenSPP Farmer Registry Base"

![](module_installation/05-spp_farmer1.jpg)

3.  Click the **Activate** button to install the module and its dependencies.

![](module_installation/06-spp_farmer2.jpg)

## Installing additional modules

After setting up your base system (either SP-MIS or Farmer Registry), you can extend functionality with additional modules. OpenSPP offers 60+ specialized modules covering various aspects of social protection delivery.

:::{note}
Additional modules automatically detect and respect your base configuration (SP-MIS or Farmer Registry). Some modules are specific to one configuration, while others work with both.
:::

### Common extension modules

**Data Management:**
- **Change Request** ({doc}`spp_change_request </reference/modules/spp_change_request>`) - Workflow for reviewing and approving data modifications
- **Data Import** ({doc}`spp_registrant_import </reference/modules/spp_registrant_import>`) - Bulk data import from Excel/CSV files
- **Manual Eligibility** ({doc}`spp_manual_eligibility </reference/modules/spp_manual_eligibility>`) - Manual beneficiary selection

**Program Features:**
- **Cash Entitlements** ({doc}`spp_entitlement_cash </reference/modules/spp_entitlement_cash>`) - Cash transfer calculations and management
- **In-Kind Distribution** ({doc}`spp_entitlement_in_kind </reference/modules/spp_entitlement_in_kind>`) - Non-cash benefit distribution
- **Eligibility SQL** ({doc}`spp_eligibility_sql </reference/modules/spp_eligibility_sql>`) - SQL-based targeting criteria

**Integration & APIs:**
- **REST API** ({doc}`spp_api </reference/modules/spp_api>`) - RESTful API for external system integration
- **OpenID Connect** ({doc}`spp_oauth </reference/modules/spp_oauth>`) - Single sign-on and authentication
- **DCI API Server** ({doc}`spp_dci_api_server </reference/modules/spp_dci_api_server>`) - Data Collection Interface API

### Example: Installing change request module

Let's walk through installing the {doc}`Change Request </reference/modules/spp_change_request>` module as an example:

**Steps:**

1.  Navigate to the **Apps** menu
2.  Search for `spp_change_request` or "OpenSPP Change Request"

![](module_installation/08-spp_cr1.jpg)

3.  Click the **Activate** button.

![](module_installation/09-spp_cr2.jpg)

### Example: Installing cash entitlement module

The **OpenSPP Entitlement: Cash** ({doc}`spp_entitlement_cash </reference/modules/spp_entitlement_cash>`) module adds functionality to manage cash-based entitlements for registrants.

**Steps:**

1.  Navigate to the **Apps** menu.
2.  Search for `spp_entitlement_cash` or "OpenSPP Entitlement: Cash".

![](module_installation/10-spp_ent_cash1.jpg)

3.  Click the **Activate** button.

![](module_installation/11-spp_ent_cash2.jpg)

## Module dependencies

OpenSPP modules often have dependencies that are automatically installed. Understanding these relationships helps with troubleshooting:

- **Core dependencies** are always installed (e.g., {doc}`spp_base </reference/modules/spp_base>` installs registry modules)
- **Optional dependencies** can be manually selected based on your needs
- **Conflicting modules** will show warnings during installation attempts

:::{tip}
Use the module's information page to view its dependencies before installation. This helps you understand what additional functionality will be added.
:::

## Troubleshooting

**Module not appearing in Apps list:**
- Ensure the `openspp-modules` directory is in your addons path
- Click "Update Apps List" in developer mode
- Check module folder naming matches technical name

**Installation fails:**
- Check Odoo logs for specific error messages
- Verify all dependencies are available
- Ensure no conflicting modules are installed
- Confirm Odoo version compatibility (17.0)

**After installation issues:**
- Clear browser cache and reload
- Restart Odoo service if menu items don't appear
- Check user access rights for new features

## Next steps

After installing your modules:

1. **Configure settings** - Each module may add configuration options under Settings
2. **Set up user permissions** - Review and assign appropriate access rights
3. **Import initial data** - Use data import modules or APIs to populate your system
4. **Test workflows** - Verify the installed features work as expected

For detailed configuration guides for specific modules, see the {doc}`../user_guide/index` and {doc}`../reference/modules/index`.

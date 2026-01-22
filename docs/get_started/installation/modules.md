---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Install a module in Odoo

This tutorial is for **users** and **implementers** working in an existing OpenSPP system who need to activate a module using the Odoo interface.

## What you'll do

Learn how to find and activate a module in OpenSPP.

## Before you start

- The OpenSPP system must already be running
- Have access to an Odoo user with **Apps administration** rights
- Know the **exact name of the module** you want to install
- Allow 3-5 minutes to complete this step

If you are not sure which module you need, or what functionality a module provides, see the
{doc}`Modules Index </reference/modules/index>`.

*Note:* Installing a module from the Odoo interface **does not upload or deploy code**.
It only activates a module that is already present on the system.

## Steps

### 1: Open the Apps menu

Log in to Odoo and open the **Apps** menu from the main navigation bar.

![Screenshot: "Apps"" button](/_images/en-us/get_started/installation/modules/cle8_1.png)

### 2: Remove the Apps filter

If the **Apps** filter is enabled, remove it so all available modules are visible.

![Screenshot: Remove the Apps filter](/_images/en-us/get_started/installation/modules//cle8_2.png)

### 3: Search for the module

Use the search bar to enter the **exact module name**.

If you are unsure of the name, see the
{doc}`Modules Index </reference/modules/index>`.

![Screenshot: Search for the app](/_images/en-us/get_started/installation/modules/cle8_3.png)

### 4: Activate the module

Click **Activate** to start the installation.

During installation, Odoo automatically:

* creates required database tables
* applies access rights
* loads default configuration data

### 5: Wait for installation to complete

Wait until the installation finishes and OpenSPP exits the **Apps** page.

### After installation

After the module is installed:

* the module appears as **Installed** in the Apps menu
* new menus or configuration options may become available

Some modules require **additional configuration** before they can be used.

Always continue with:

* the module’s configuration documentation
* any required setup steps described in the related guide

### Are you stuck?

If the module does not install successfully, check the following:

* you have sufficient access rights
* the module name is spelled correctly
* the module appears in the Apps list
* no error message is shown during installation

If the problem persists:

* contact your system administrator
* provide them with the module name and any error messages

## Next Steps

- {doc}`../first_program/index` - Create your first social protection program
- {doc}`/user_guide/index` - Learn the OpenSPP interface
- {doc}`/config_guide/index` - Configure eligibility rules and expressions


---
openspp:
  doc_status: unverified
---

# PMT using Module Development

This tutorial guides you through installing and implementing the Proxy Means Testing (PMT) module in OpenSPP with the help of custom module development. By following these steps, you will be able to extend the functionality of the OpenSPP with PMT features.

## Prerequisites

- A working OpenSPP installation.
- Administrator access to install and configure new modules.
- Download and deploy the spp_pmt module from the Github repository[Link] into “custom/src/openspp_registry” folder in “odoo” in your OpenSPP installation.

## 1. Installation of the PMT Module

1.1. Start by logging into your OpenSPP instance with administrative privileges.

1.2. Navigate to the "Apps" menu from the dashboard. Here, modules are managed for your OpenSPP environment.

1.3. In the "Apps" menu, select "Update Apps List" to ensure all recently added modules are visible.

1.4. In the search bar, type "Proxy Means Testing" and press enter. Locate the module from the list that appears.

1.5. Click on the "Install" button next to the PMT module. The system will automatically handle the installation, managing any dependencies as declared in the module's manifest file.

## 2. Understanding Module Structure

2.1 **init**.py: This file indicates that its containing directory, `spp_pmt`, is a Odoo module. It imports the `models` package, suggesting the main business logic resides there.

2.2 **manifest**.py: The manifest file defines essential metadata about the module. Key points include:

- The module's name is "Proxy Means Testing".
- It belongs to the "OpenSPP" category.
- Current version is "15.0.0.0.0".
- The module is still in "Beta" development status.
- Dependencies include "base", "spp_registry", and "spp_registry".

  2.3. `models/__init__.py`: This file signifies that the `models` directory is a Python package and imports `pmt.py`, where the PMT model is defined.

  2.4. models/pmt.py: This file defines the PMT feature's business logic. It extends the `res.partner` model (standard in Odoo). It also computes a PMT score based on these fields.

## 3. Using the PMT Features

3.1. Navigate to the “Individual” under "Registry" menu.

3.2. Select a entry. With the PMT module installed, under “Additional Details”, an individual data fields related to PMT calculation can be modified.

3.4. Save the entry. The PMT score should be calculated and shown under the “Indicators” menu in the “Groups” where the individual is part of the group.

3.5. Utilize the PMT score as needed within your OpenSPP operations, noting that it's calculated using the specific logic defined within the PMT module.

By following this tutorial, the Proxy Means Testing module should now be fully integrated into your OpenSPP instance, providing additional functionality to your social protection operations.

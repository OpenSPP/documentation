---
openspp:
  doc_status: draft
myst:
  html_meta:
    "title": "OpenSPP DRIMS Installation Guide"
    "description": "Step-by-step guide for installing and configuring the OpenSPP Disaster Response Inventory Management System (DRIMS)"
    "keywords": "OpenSPP, DRIMS, disaster response, inventory management, installation, Odoo"
---

# DRIMS installation

**OpenSPP DRIMS / spp_drims**

The {doc}`OpenSPP Disaster Response Inventory Management System (DRIMS) <../../products/drims/index>` provides end-to-end management of emergency supplies, from donation intake through dispatch and returns. This setup is designed for government agencies, humanitarian organizations, and logistics teams coordinating disaster response operations.

**What's included:**
- Donation tracking with state-based workflows (announced, received, inspected, stocked)
- Request management with multi-tier approval and FIFO stock allocation
- Dispatch coordination and fulfillment tracking
- Real-time inventory visibility and stock health indicators
- SLA monitoring with configurable priority thresholds
- Automated alerts for low stock, expiring items, and SLA breaches
- Inter-agency coordination and personnel deployment tracking
- GIS-based geographic coverage and area management

**Installation steps:**

1.  Navigate to the **Apps** menu.
2.  In the Apps menu, search for `spp_drims` or "OpenSPP DRIMS"

![Searching for the DRIMS module in the Apps menu](/_images/en-us/get_started/module_installation/drims_installation/01-apps-search.png)

3.  Click the **Activate** button to install the module. This will also install all its dependencies, including inventory management, GIS, approval workflows, and alert engine modules.

Once installed, you will see the **DRIMS** application in your Odoo dashboard as the main entry point for managing disaster response inventory.

![DRIMS module successfully installed](/_images/en-us/get_started/module_installation/drims_installation/02-installed.png)

## Next steps

Now that you have installed OpenSPP DRIMS, you can:

- {doc}`../../products/drims/demo_module` - Load demo data to explore DRIMS functionality
- {doc}`../../products/drims/user_guides` - Start using DRIMS to manage disaster response operations
- {doc}`../../products/drims/config_guides` - Configure warehouses, approval chains, vocabularies, and alerts to match your operational needs

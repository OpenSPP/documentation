---
myst:
  html_meta:
    "title": "OpenSPP Module Installation Guide"
    "description": "Step-by-step guide for installing and configuring OpenSPP modules including SP-MIS, Social Registry, and Farmer Registry"
    "keywords": "OpenSPP, modules, installation, Odoo, SP-MIS, Social Registry, Farmer Registry"
---

# Farmer Registry installation

**OpenSPP Farmer Registry Base / spp_base_farmer_registry (available from 17.0.1.4)**

The {doc}`OpenSPP Farmer Registry <../../products/farmer_registry>` configuration enables convergence between social protection and agricultural development programs. This setup is designed for organizations supporting smallholder farmers, managing agricultural subsidies, or implementing climate-smart agriculture initiatives.

**What's included:**
- Farmer and farm household registration
- Land parcel mapping with GIS integration
- Crop and livestock tracking
- Agricultural input distribution management
- Seasonal cycle management
- Integration with agricultural extension services

**Installation steps:**

1.  Navigate to the **Apps** menu.
2.  In the Apps menu, search for "OpenSPP Farmer Registry Base"

![Searching for SPP Farmer Registry module](/_images/en-us/get_started/modules/05-spp_farmer1.jpg)

3.  Click the **Activate** button to install the module and its dependencies.

![SPP Farmer Registry module installation complete](/_images/en-us/get_started/modules/06-spp_farmer2.jpg)

4. Restart OpenSPP after installing the module:
   ```bash
   sudo systemctl restart openspp
   ```

**Note**: The `queue_job` module, which is essential for asynchronous background tasks, is automatically installed as a dependency of the main OpenSPP modules. It is also pre-configured as a `server_wide_module`, ensuring that background workers can process jobs correctly after a service restart.

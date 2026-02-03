---
myst:
  html_meta:
    "title": "OpenSPP Module Installation Guide"
    "description": "Step-by-step guide for installing and configuring OpenSPP modules including SP-MIS, Social Registry, and Farmer Registry"
    "keywords": "OpenSPP, modules, installation, Odoo, SP-MIS, Social Registry, Farmer Registry"
---

# SP-MIS installation

**OpenSPP SPMIS Base / spp_base_spmis (available from 17.0.1.4)**

The OpenSPP Social Protection Management Information System ({doc}`OpenSPP SP-MIS </products/sp_mis>`) configuration provides comprehensive functionality for managing social protection programs. This setup is ideal for organizations running cash transfers, social assistance programs, or humanitarian interventions.

**What's included:**
- Registry management for individuals and groups
- Program cycles and beneficiary enrollment
- Eligibility determination and targeting
- Entitlement calculation and management
- Payment processing integration

**Installation steps:**

1.  Navigate to the **Apps** menu.
2.  In the Apps menu, search for {doc}`spp_starter_sp_mis </reference/modules/spp_starter_sp_mis>` or "OpenSPP SP-MIS Starter"

![Searching for SPP Base module in Apps](/_images/en-us/get_started/modules/02-spp_base01.jpg)

3.  Click the **Activate** button to install the module. This will also install all its dependencies, providing a complete SP-MIS foundation.

![SPP Base module installation screen](/_images/en-us/get_started/modules/03-spp_base2.jpg)

4. Restart OpenSPP after installing the module:
   ```bash
   sudo systemctl restart openspp
   ```

**Note**: The `queue_job` module, which is essential for asynchronous background tasks, is automatically installed as a dependency of the main OpenSPP modules. It is also pre-configured as a `server_wide_module`, ensuring that background workers can process jobs correctly after a service restart.

Once installed, you will see the "Registry" application in your Odoo dashboard, which is the main entry point for the OpenSPP system.

![SPP Base module successfully installed](/_images/en-us/get_started/modules/04-spp_base3.jpg)

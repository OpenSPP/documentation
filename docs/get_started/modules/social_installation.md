---
myst:
  html_meta:
    "title": "OpenSPP Module Installation Guide"
    "description": "Step-by-step guide for installing and configuring OpenSPP modules including SP-MIS, Social Registry, and Farmer Registry"
    "keywords": "OpenSPP, modules, installation, Odoo, SP-MIS, Social Registry, Farmer Registry"
---

# Social Registry installation

**OpenSPP Social Registry Base / spp_base_social_registry (available from 17.0.1.4)**

The {doc}`OpenSPP Social Registry <../overview/products/social_registry>` configuration provides a centralized repository for beneficiary data that can be shared across multiple social protection programs. This setup is ideal for governments and organizations coordinating multiple interventions and requiring a single source of truth for beneficiary information.

**What's included:**
- Unified beneficiary database across programs
- Advanced deduplication and data quality management
- Dynamic registration and needs assessment
- Inter-program data sharing and coordination
- Household composition and relationship tracking
- Socioeconomic data collection and analysis
- Data privacy and access control mechanisms

**Installation steps:**

1.  Navigate to the **Apps** menu.
2.  In the Apps menu, search for {doc}`spp_base_social_registry </reference/modules/spp_base_social_registry>` or "OpenSPP Social Registry Base"

![Searching for SPP Base module in Apps](/_images/en-us/get_started/modules/12-social_inst_base01.jpg)

3.  Click the **Activate** button to install the module and its dependencies

![SPP Base module installation screen](/_images/en-us/get_started/modules/13-social_inst_base2.jpg)

4. Restart OpenSPP after installing the module:
   ```bash
   sudo systemctl restart openspp
   ```

**Note**: The `queue_job` module, which is essential for asynchronous background tasks, is automatically installed as a dependency of the main OpenSPP modules. It is also pre-configured as a `server_wide_module`, ensuring that background workers can process jobs correctly after a service restart.

Once installed, the Social Registry becomes the central hub for managing beneficiary data that can be accessed by various social protection programs.

---
openspp:
  doc_status: draft
myst:
  html_meta:
    "title": "General module installation - OpenSPP"
    "description": "General guide for installing and configuring OpenSPP modules on Odoo 19"
    "keywords": "OpenSPP, modules, installation, Odoo, dependencies, troubleshooting"
---

# General module installation

OpenSPP's modular architecture allows organizations to deploy only the features they need. Built on Odoo 19, the platform extends functionality through specialized modules that can be mixed and matched to create tailored social protection solutions.

:::{important}
Before installing OpenSPP modules, ensure you have an **Odoo 19 instance** running and accessible. If not, follow the {doc}`Installation guide <../installation/docker>` in order to install it.
:::

## Installing OpenSPP base modules

OpenSPP comes with three configured base modules depending on your needs. The steps on how to install these can be found in {doc}`Installation of OpenSPP Social Registry <social_installation>`, {doc}`Installation of OpenSPP SP-MIS <spmis_installation>` and {doc}`Installation of OpenSPP Farmer Registry <farmer_installation>`. Additional products such as {doc}`DRIMS <drims_installation>` and the {doc}`Disability Registry <disability_installation>` can be installed alongside any base module.

:::{important}
The **SP-MIS** ({doc}`spp_starter_sp_mis </reference/modules/spp_starter_sp_mis>`), **Farmer Registry** ({doc}`spp_starter_farmer_registry </reference/modules/spp_starter_farmer_registry>`) and **Social Registry** ({doc}`spp_starter_social_registry </reference/modules/spp_starter_social_registry>`) modules are mutually exclusive. You can only have one of them installed in a single Odoo database. Attempting to install multiple base modules will result in an error.
:::

## Installing additional modules

After setting up your base system you can extend the functionality with additional modules. OpenSPP offers 60+ specialized modules covering various aspects of social protection delivery.

:::{note}
Additional modules automatically detect and respect your base configuration (SP-MIS or Farmer Registry). Some modules are specific to one configuration, while others work with both.
:::

## General installation process

Installing an Odoo module, including those for OpenSPP, follows a standard procedure:

1.  Navigate to the **Apps** menu.

2.  Search for the desired module by its technical name or title. If the module does not show up, clear the default "Apps" filter from the search bar.

3. Click the **Activate** button on the module's card to begin the installation.

![OpenSPP Apps menu interface](/_images/en-us/get_started/module_installation/01-apps-ui.png)

4. Restart OpenSPP after installing the modules:
   ```bash
   sudo systemctl restart openspp
   ```

**Note**: The `queue_job` module, which is essential for asynchronous background tasks, is automatically installed as a dependency of the main OpenSPP modules. It is also pre-configured as a `server_wide_module`, ensuring that background workers can process jobs correctly after a service restart.

## Module dependencies

OpenSPP modules often have dependencies that are automatically installed. Understanding these relationships helps with troubleshooting:

- **Core dependencies** are always installed (e.g., {doc}`spp_starter_sp_mis </reference/modules/spp_starter_sp_mis>` installs registry modules)
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
- Confirm Odoo version compatibility (19.0)

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

For detailed configuration guides for specific modules, see the {doc}`../../user_guide/index` and {doc}`../../reference/modules/index`.

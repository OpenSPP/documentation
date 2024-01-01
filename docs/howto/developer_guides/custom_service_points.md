# Customize Service Points

This guide provides a structured approach for implementing and customising the service points in OpenSPP through the development of a custom module.

## Prerequisites

- Knowledge in Python, Odoo, OOP, HTML, XML, Xpaths.
- A working OpenSPP installation
- Administrator access to the OpenSPP backend.

## Odoo Setup from Docker using doodba

- Existence of openg2p_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group.
- Existence of openspp_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: spp_service_points, spp_service_point_device, spp_area.
  Odoo Setup from source
- Existence of openg2p-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-registry.git) into odoo/custom, navigate to the openg2p-registry folder, and switch to the specified branch.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group.
- Existence of openspp-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, clone the repository from [here](https://github.com/OpenSPP/openspp-registry.git) into odoo/custom, navigate to the openspp-registry folder, and switch to the specified branch.
- Availability of modules: spp_service_points, spp_service_point_device, spp_area.

## Installation

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search for “OpenSPP Service Point Device” and initiate installation. This process will also install associated modules: OpenSPP Service Points

## Utilising the Service Points Module

- If a new Service Point is required to be added, Select “Service Point” menu.
- Select the Create button to add a new Service Point, ensuring all required fields are completed.
- Click the Save button. A Service Point record is now created.
- If a Service Point Device is required to view, Select “Devices” on the top right corner of the Service Point Page.
- Upon clicking, the page will be directed to the page consisting of a table of all the Terminal Devices of the Service Point.
- If a Service Point user is required, go back to the Service Point page, select the Edit button, and fill-up the company field.
- Upon adding value to the company field, a new button will appear in the top right corner named “Create SP Users”.
- Click “Create SP Users” to create users for all contacts under the company.

## Customise Service Point and Service Point Device

- To introduce new fields or functions in a new module, develop a Python file extending the “spp.service.point” for Service Point or “spp.service.point.device” for Service Point Device and integrate this file into `models/__init__.py`.
  - e.g. service_point_location = fields.Char(required=True) or
  - e.g. service_point_location = fields.Many2one(“service.point.location”, required=True) assuming there is a model for service point location.
- Upgrade the module incorporating the new Python file.
- To integrate new fields into the UI, developers should familiarise themselves with view, view inheritance and the use of xpath in Odoo.

## Additional References

- Below are some Odoo references that may help in adding the field both in models and in UI. For further guidance on model creation, inheritance, and UI integration, the following Odoo documentation may be useful:
  - [Views](https://www.odoo.com/documentation/15.0/developer/reference/backend/views.html)
  - [Chapter 4: Models And Basic Fields](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/04_basicmodel.html)
  - [Chapter 7: Basic Views](https://www.odoo.com/documentation/17.0/developer/tutorials/getting_started/07_basicviews.html#chapter-7-basic-views)
  - [Chapter 13: Inheritance](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/13_inheritance.html)
  - [Chapter 14: Interact With Other Modules](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/14_other_module.html)

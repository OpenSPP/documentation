# Customize Registry

This guide provides a structured approach for implementing and customising the registry in OpenSPP through the development of a custom module.

## Prerequisites

- Knowledge in Python, Odoo, OOP, HTML, XML, Xpaths.
- A functional OpenSPP installation.
- Administrative access to the OpenSPP backend.

## Odoo Setup from Docker using doodba

- Existence of openg2p_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership.
- Existence of web folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: web, web_domain_field.
- Existence of queue folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: queue_job

## Odoo Setup from source

- Existence of openg2p-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-registry.git) into odoo/custom, navigate to the openg2p-registry folder, and switch to the specified branch.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership.
- Existence of web folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/web.git) into odoo/custom, navigate to the web, and switch to the specified branch.
- Availability of modules: web, web_domain_field.
- Existence of queue folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/queue.git) into odoo/custom, navigate to the queue, and switch to the specified branch.
- Availability of modules: queue_job.

## Installation

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List ” to refresh the module list.
- Search for “G2P Registry: Membership” and initiate installation. This process will also install associated modules: G2P Registry: Groups, G2P Registry: Individual, G2P Registry: Base.

## Utilising the Registry Module

- If a new individual is required to be added, Under the “Registry” menu, select “Individuals”.
- If a new individual is required to be added, select the Create button to add new individuals, ensuring all required fields are completed.
- If a new group is required to be added, Navigate to “Groups” within the “Registry” menu.
- Create a new group and add members by using the “Add a line” option in the “Members” panel. Search and select individuals previously created.
- Save changes. Added members and groups will be visible in their respective panels.
- To add custom filter, navigate to the tree/list view of the registry in either Group or Individual then click the “Filter” button below the search field, then click custom filter.
- Select the field, operator, and the value for the custom filter.
- To add custom group by, navigate to the tree/lsit view of the registry page then click the “Group by” button then click the “Add Custom Group” and select the field you want to use in Group by.

## Customise Registry

- To introduce new fields or functions in a new module, develop a Python file extending the res.partner model and integrate this file into `models/__init__.py`.
- Upgrade the module incorporating the new Python file.
- Follow naming conventions for new registry fields:
  - Prefix individual-specific fields with `ind_` (e.g., “ind_hobbies”).
  - Prefix group-specific fields with `grp_` (e.g., “grp_number_of_members”).
  - Use no prefix for universally applicable fields (e.g., “name”, “address”).
- For relational fields like many2one to `res.partner`, apply appropriate domain parameters to filter registry records.
- To integrate new fields into the UI, developers should familiarise themselves with view, view inheritance and the use of xpath in Odoo.
- To add a new tab, inherit the form view of the registry page and then xpath to the “page” element under the “notebook” element with the position preferred.

## Additional References

- Below are some Odoo references that may help in adding the field both in models and in UI. For further guidance on model creation, inheritance, and UI integration, the following Odoo documentation may be useful:
  - [Views](https://www.odoo.com/documentation/15.0/developer/reference/backend/views.html)
  - [Chapter 4: Models And Basic Fields](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/04_basicmodel.html)
  - [Chapter 7: Basic Views](https://www.odoo.com/documentation/17.0/developer/tutorials/getting_started/07_basicviews.html#chapter-7-basic-views)
  - [Chapter 13: Inheritance](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/13_inheritance.html)
  - [Chapter 14: Interact With Other Modules](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/14_other_module.html)

# Customize Program

This guide provides a structured approach for implementing and customising the program in OpenSPP through the development of a custom module.

## Prerequisites

- Knowledge in Python, Odoo, OOP, HTML, XML, Xpaths.
- A functional OpenSPP installation.
- Administrative access to the OpenSPP backend.

## Odoo Setup from Docker using doodba

- Existence of openg2p_program folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_programs.
- Existence of openg2p_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership, g2p_bank.
- Existence of openspp_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: spp_programs, spp_programs_sp, g2p_entitlement_cash, spp_entitlement_inkind, spp_eligibility_sql, spp_eligibility_tags.
- Existence of queue folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: queue_job
- Existence of web folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: web, web_domain_field.

## Odoo Setup from source

- Existence of openg2p-program folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-program.git) into odoo/custom, navigate to the openg2p-program folder, and switch to the specified branch.
- Availability of modules: g2p_programs.
- Existence of openg2p-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-registry.git) into odoo/custom, navigate to the openg2p-program folder, and switch to the specified branch.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership, g2p_bank.
- Existence of openspp-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, clone the repository from [here](https://github.com/OpenSPP/openspp-registry.git) into odoo/custom, navigate to the openspp-registry folder, and switch to the specified branch.
- Availability of modules: spp_programs, spp_programs_sp, g2p_entitlement_cash, spp_entitlement_inkind, spp_eligibility_sql, spp_eligibility_tags, spp_area, spp_service_point.
- Existence of queue folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/queue.git) into odoo/custom, navigate to the queue, and switch to the specified branch.
- Availability of modules: queue_job.
- Existence of web folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/web.git) into odoo/custom, navigate to the web, and switch to the specified branch.
- Availability of modules: web, web_domain_field

## Installation

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search and initiate installation of the following modules, this process will also install all of their associated modules:
  - OpenSPP Program Entitlement (In-Kind)
  - SPP Program Entitlement (Cash)
  - OpenSPP Tag Based Eligibility Manager
  - OpenSPP SQL Query Eligibility Manager

## Utilising the Program Module

- If a new Program is required to be added, Select “Program” menu.
- Select the “Create Program” button and a modal to set the program settings will appear.
- Fill-up name field.
- Select a Target Type: Group is for Group Registry while Individual is for Individual Registry.
- In the “Configure the Default Eligibility Criteria” will set who are the individuals or groups that are eligible for this program.
- There are 3 Eligibility Managers that can be selected namely “Default”, “SQL-base Eligibility”, and “Tag-based Eligibility”
- In “Default”, a registry will be determined based on the filter that is setup on the domain. To set up the domain, Click the “Add filter” button.
- Upon clicking the button, 3 fields will appear. First field is the name of the model’s field, Second field is the operator, while the 3rd field is the value.
- Based on the filter that is setup is what will be the eligible registrant for this program
- In “SQL-base Eligibility”, a registry will be determined based on the SQL Query that will be input in the SQL Query field
- Upon inputting the SQL Query, click the “Validate Query” button to validate the query if it is a valid sql query
- The result if its valid or invalid will show and the registry record count if its valid.
- In “Tag-based Eligibility”, a registry will be determined based on the Tags and Area provided.
- In the “Configure the Cycle Manager” tab will set the recurrence, approvers, etc., of the program’s cycle.
- Check the One-time Distribution to only create one cycle and no recurrence to a program.
- In the “Configure the Entitlement Manager” tab will set the entitlements that the registry will receive.
- There are 3 Entitlement Managers that can be selected namely “Default”, “Cash”, and “In-kind”
- Upon setting up all of the managers of the program, click the Next button, model will redirect to the “Import Registrant” page
- In this page will set if the program will import the registrants after creating or not. Select “Yes” to import registrant, otherwise select “No”.
- Click Create button to create the Program.
- Inside the Program, there are many buttons in the top part of the page.
- “Import Eligible Registrants” button is to import all registrants based on the eligible criteria. This registrants is still not enrolled in the Program.
- “Enroll Eligible Registrants” button will enroll all imported registrants.
- “Verify eligibility” button will verify if all enrolled registrants is still eligible for the program. If they are not eligible anymore then they will be removed from the program.
- “Create New Cycle” will create a cycle and the cycle that was created will be added in the Cycles Tab.
- To modify the managers of the Program, go to the Configurations tab.
- In this tab will show all of the managers of the program, click the green button to modify the managers.
- Click the green button on Eligibility Managers to modify the eligibility criteria of the program.
- Click the green button on Cycle Managers to modify the settings of the program’s cycle.
- Click the green button on Entitlement Managers to modify the settings of the entitlements.

## Customise Program

- To introduce new fields or functions in a new module, develop a Python file extending the following models:
  - “g2p.program” for Program.
  - “g2p.program.create.wizard” for the creation of a Program.
  - “g2p.program_membership.manager.default” for the default eligibility criteria.
  - “g2p.program_membership.manager.tags” for the tag-based eligibility criteria.
  - “g2p.program_membership.manager.sql” for the sql-base eligibility criteria.
  - “g2p.cycle.manager.default” for the cycle manager.
  - “g2p.program.entitlement.manager.default” for the default entitlement manager.
  - “g2p.program.entitlement.manager.cash” for the cash entitlement manager.
  - “g2p.program.entitlement.manager.inkind” for the in-kind entitlement manager.
- Integrate this file into `models/__init__.py`.
- Upgrade the module incorporating the new Python file.
- To integrate new fields into the UI, developers should familiar themselves with the view, view inheritance, and the use of xpath in Odoo.

## Additional References

- Below are some Odoo references that may help in adding the field both in models and in UI. For further guidance on model creation, inheritance, and UI integration, the following Odoo documentation may be useful:
  - [Views](https://www.odoo.com/documentation/15.0/developer/reference/backend/views.html)
  - [Chapter 4: Models And Basic Fields](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/04_basicmodel.html)
  - [Chapter 7: Basic Views](https://www.odoo.com/documentation/17.0/developer/tutorials/getting_started/07_basicviews.html#chapter-7-basic-views)
  - [Chapter 13: Inheritance](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/13_inheritance.html)
  - [Chapter 14: Interact With Other Modules](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/14_other_module.html)

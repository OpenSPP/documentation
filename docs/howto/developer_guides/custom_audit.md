# Customize Audit Logs

This guide provides a structured approach for implementing and customising the audit log in OpenSPP through the development of a custom module.

## Prerequisites

- Knowledge in Python, Odoo, OOP, HTML, XML, Xpaths.
- A functional OpenSPP installation.
- Administrative access to the OpenSPP backend.

## Odoo Setup from Docker using doodba

- Existence of openg2p_program folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_programs.
- Existence of openg2p_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership.
- Existence of openspp_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: spp_audit_log, spp_audit_config, spp_audit_post, spp_programs, spp_service_points, spp_area.
- Existence of web folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: web, web_domain_field.
- Existence of queue folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: queue_job.

## Odoo Setup from source

- Existence of openg2p-program folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-program.git) into odoo/custom, navigate to the openg2p-program folder, and switch to the specified branch.
- Availability of modules: g2p_programs.
- Existence of openg2p-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-registry.git) into odoo/custom, navigate to the openg2p-program folder, and switch to the specified branch.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership.
- Existence of openspp-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, clone the repository from [here](https://github.com/OpenSPP/openspp-registry.git) into odoo/custom, navigate to the openspp-registry folder, and switch to the specified branch.
- Availability of modules: spp_audit_log, spp_audit_config, spp_audit_post, spp_programs, spp_service_points, spp_area.
- Existence of web folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/web.git) into odoo/custom, navigate to the web, and switch to the specified branch.
- Availability of modules: web, web_domain_field.
- Existence of queue folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/queue.git) into odoo/custom, navigate to the queue, and switch to the specified branch.
- Availability of modules: queue_job.

## Installation

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search and initiate installation of the following modules, this process will also install all of their associated modules:
  - SPP Audit Config
  - SPP Audit Log
  - SPP Audit Post

## Utilising the Audit Log Module

- Navigate to the “Rule” page inside the “Audit Log” menu.
- Audit rules are already in place. They are created when installing or upgrading the module “SPP Audit Config”.
- Select the Create button to add new rules.
- To test the Audit Rule, go to Individual or Group Registry.
- Create or Update Registry.
- An audit log will show in the bottom part of the page indicating the fields that were changed and their corresponding old and new values.
  ![](./custom_audit/1.png)
- Audit logs can also be viewed by navigating to Audit Log then Log menu.
- This page will show all of the audit logs from every model that is indicated in the audit rules.
  <img src="./custom_audit/2.png" width="327" height="333">
- Another way to see the audit logs is to enter a record and click Action then click the “View Logs”.
  ![](./custom_audit/3.png)
- It will redirect to the audit logs page that is automatically filtered to the record.
- When you add an audit rule to a model, it effectively patches a specialized function into the model's key events - create, write, and unlink. This function operates as a gatekeeper, first verifying if an audit rule is set for the specific model, then determining which events to log and which fields to display in the audit log. This integration transforms the model into recording and showcasing relevant changes and activities for enhanced data management and integrity.

## Customise Audit Log Module

- To introduce new fields or functions in a new module, develop a Python file extending the model “spp.audit.rule” for the Audit Rules while “spp.audit.log” for the Audit Logs and integrate this file into `models/__init__.py`.
- Upgrade the module incorporating the new Python file.
- To integrate new fields into the UI, developers should familiarise themselves with view, view inheritance and the use of xpath in Odoo.

## Additional References

- Below are some Odoo references that may help in adding the field both in models and in UI. For further guidance on model creation, inheritance, and UI integration, the following Odoo documentation may be useful:
  - [Views](https://www.odoo.com/documentation/15.0/developer/reference/backend/views.html)
  - [Chapter 4: Models And Basic Fields](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/04_basicmodel.html)
  - [Chapter 7: Basic Views](https://www.odoo.com/documentation/17.0/developer/tutorials/getting_started/07_basicviews.html#chapter-7-basic-views)
  - [Chapter 13: Inheritance](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/13_inheritance.html)
  - [Chapter 14: Interact With Other Modules](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/14_other_module.html)

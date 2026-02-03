---
openspp:
  doc_status: unverified
  products: [core]
---

# Customize Cycle

This guide provides a structured approach for implementing and customising the cycle in OpenSPP through the development of a custom module.

## Prerequisites

- Knowledge in Python, Odoo, OOP, HTML, XML, Xpaths.
- A functional OpenSPP installation.
- Administrative access to the OpenSPP backend.

## Odoo Setup from Docker using doodba

- Existence of openspp_programs folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: spp_programs.
- Existence of openspp_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: spp_registry, spp_banking.
- Existence of queue folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: queue_job
- Existence of web folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: web, web_domain_field.

## Odoo Setup from source

```{note}
These instructions are outdated. For OpenSPP V2 on Odoo 19, please refer to the [Development Setup Guide](/howto/developer_guides/development_setup.md).
```

- Clone the openspp-modules repository from [GitHub](https://github.com/OpenSPP/openspp-modules).
- Availability of modules: spp_programs, spp_registry, spp_banking.
- Existence of queue folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/queue.git) into odoo/custom, navigate to the queue, and switch to the specified branch.
- Availability of modules: queue_job.
- Existence of web folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/web.git) into odoo/custom, navigate to the web, and switch to the specified branch.
- Availability of modules: web, web_domain_field

## Installation

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search for “OpenOpenSPP Programs” and initiate installation. This process will also install associated modules: OpenSPP Registrys, OpenSPP Registry, OpenSPP Registry.

## Utilising the Cycle Module

- If a new Cycle is required to be added, enter one of the Programs.
- Click “Create New Cycle” in the top corner of the page.
- A cycle will be created and added to the table inside the Cycles tab.
- A program can create multiple cycles.
- Click on the green button beside the cycle name of a cycle.
- Upon clicking the green button, the system will be redirected to the cycle page where the information of the cycle can be seen.
- Several buttons can be seen in the top corner of the cycle page.
- “Copy Beneficiaries from Program” button will copy all of the enrolled registry from the program to the cycle.
- “Verify Eligibility” button will verify all of the enrolled registry in the cycle if they are still eligible for this cycle and program.
- “To Approve” button will change the state of the cycle from “Draft” to “To approve”.
- Once the cycle’s state is in “To Approve”, only the “Approve” and “Reset to Draft” button will be visible in the top corner of the page.
- “Approve” button will change the state of the cycle from “To approve” to “Approve”.
- “Reset to Draft” button will revert back the state of the cycle from “To approve” to “Draft”.
- Once the cycle’s state is in “Approve”, only the “Validate Entitlements” button will be visible in the top corner of the page.
- “Validate Entitlements” button changes the status of entitlements from “Draft” to “Pending Validation”.
- Start date and End date of a cycle depends on the Recurrence settings that were setup in Cycle Manager.

## Customise Cycle

- To introduce new fields or functions in a new module, develop a Python file extending the model “spp.cycle” and integrate this file into `models/__init__.py`.
- Upgrade the module incorporating the new Python file.
- To integrate new fields into the UI, developers should familiarise themselves with view, view inheritance and the use of xpath in Odoo.

## Additional References

- Below are some Odoo references that may help in adding the field both in models and in UI. For further guidance on model creation, inheritance, and UI integration, the following Odoo documentation may be useful:
  - [Views](https://www.odoo.com/documentation/15.0/developer/reference/backend/views.html)
  - [Chapter 4: Models And Basic Fields](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/04_basicmodel.html)
  - [Chapter 7: Basic Views](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/07_basicviews.html#chapter-7-basic-views)
  - [Chapter 13: Inheritance](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/13_inheritance.html)
  - [Chapter 14: Interact With Other Modules](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/14_other_module.html)

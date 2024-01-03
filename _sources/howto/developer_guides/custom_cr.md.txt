# Customize Change Request

This guide provides a structured approach for implementing and customising the Change Request in OpenSPP through the development of a custom module.

## Prerequisites

- Knowledge in Python, Odoo, OOP, HTML, XML, Xpaths.
- A functional OpenSPP installation.
- Administrative access to the OpenSPP backend.

## Odoo Setup from Docker using doodba

- Existence of openg2p_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership
- Existence of openspp_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: spp_change_request, spp_service_points, spp_area, spp_scan_id_document, spp_id_pass, spp_event_data.
- Existence of dms folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: dms_field, dms.
- Existence of web folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: web, web_domain_field.
- Existence of queue folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: queue_job

## Odoo Setup from source

- xistence of openg2p-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-registry.git) into odoo/custom, navigate to the openg2p-program folder, and switch to the specified branch.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership.
- Existence of openspp-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, clone the repository from [here](https://github.com/OpenSPP/openspp-registry.git) into odoo/custom, navigate to the openspp-registry folder, and switch to the specified branch.
- Availability of modules: spp_change_request, spp_service_points, spp_area, spp_scan_id_document, spp_id_pass, spp_event_data.
- Existence of dms folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/dms.git into odoo/custom), navigate to the dms, and switch to the specified branch.
- Availability of modules: dms_field, dms.
- Existence of web folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/web.git) into odoo/custom, navigate to the web, and switch to the specified branch.
- Availability of modules: web, web_domain_field.
- Existence of queue folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/queue.git) into odoo/custom, navigate to the queue, and switch to the specified branch.
- Availability of modules: queue_job.

## Installation

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search for “OpenSPP Change Request” and initiate installation. This process will also install all associated modules.

## Utilising the Change Request Module

- If a new Change Request is required to be added, Select “Change Request” menu.
- Select the Create button to add a new Change Request, ensuring all required fields are completed.
- At this point, Request Type dropdown field does not have any values yet since there is still no new module for the request type.

## Customise Change Request

- To add a value to the Request Type dropdown field, create a new module and a new model for the request type.
  ```python
  class ChangeRequestDeactivate(models.Model):
    _name = "pds.change.request.deactivate"
    _inherit = [
        "spp.change.request.source.mixin",
        "spp.change.request.validation.sequence.mixin",
    ]
    _description = "Deactivate Member Change Request Type"
    _order = "id desc"
  ```
- Add fields and functions to the newly created model that corresponds to the requirements of that particular request type.
- Inherit model “spp.change.request” then extend the function `_selection_request_type_ref_id` to add the newly created request type model to the Request Type dropdown field.

  ```python
  class ChangeRequestTypeCustomDeactivate(models.Model):
    _inherit = "spp.change.request"

    @api.model
    def _selection_request_type_ref_id(self):
        selection = super()._selection_request_type_ref_id()
        new_request_type = (
            "pds.change.request.deactivate",
            "Deactivate Members",
        )
        if new_request_type not in selection:
            selection.append(new_request_type)
        return selection
  ```

- Make sure that the python file where the newly created model and the inherited model is already added in the `models/__init__.py`.
- In the view part, create the following views for the request type.
  - Tree View
  - Form View
  - Validation Form View
  - Pending Validation Tree View
  - Pending Validation Form View
  - Filter
- Navigate to the “Apps” Menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search for the newly created module and initiate installation.
- Navigate again to the Change Request page and a new value to the Request Type dropdown field is now added.

## Additional References

- Below are some Odoo references that may help in adding the field both in models and in UI. For further guidance on model creation, inheritance, and UI integration, the following Odoo documentation may be useful:
  - [Views](https://www.odoo.com/documentation/15.0/developer/reference/backend/views.html)
  - [Chapter 4: Models And Basic Fields](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/04_basicmodel.html)
  - [Chapter 7: Basic Views](https://www.odoo.com/documentation/17.0/developer/tutorials/getting_started/07_basicviews.html#chapter-7-basic-views)
  - [Chapter 13: Inheritance](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/13_inheritance.html)
  - [Chapter 14: Interact With Other Modules](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/14_other_module.html)

# Customize Areas

This guide provides a structured approach for implementing and customising the area in OpenSPP through the development of a custom module.

## Prerequisites

- Knowledge in Python, Odoo, OOP, HTML, XML, Xpaths.
- A functional OpenSPP installation.
- Administrative access to the OpenSPP backend.

## Odoo Setup from Docker using doodba

- Existence of openg2p_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group.
- Existence of openspp_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: spp_area.
- Existence of queue folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: queue_job
- Existence of web folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: web, web_domain_field.

## Odoo Setup from source

- Existence of openg2p-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-registry.git) into odoo/custom, navigate to the openg2p-program folder, and switch to the specified branch.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group.
- Existence of openspp-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, clone the repository from [here](https://github.com/OpenSPP/openspp-registry.git) into odoo/custom, navigate to the openspp-registry folder, and switch to the specified branch.
- Availability of modules: spp_area.
- Existence of queue folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/queue.git) into odoo/custom, navigate to the queue, and switch to the specified branch.
- Availability of modules: queue_job.
- Existence of web folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/web.git) into odoo/custom, navigate to the web, and switch to the specified branch.
- Availability of modules: web, web_domain_field

## Installation

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search for “OpenSPP Area” and initiate installation. This process will also install associated modules: G2P Registry: Groups, G2P Registry: Individual, G2P Registry: Base.

## Utilising the Area Module

- If a new Area is required to be added, Select “Area” menu.
- Select the Create button to add a new Area, ensuring all required fields are completed.
- Click the Save button. An Area record is now created.
- An Area have a hierarchy mechanism by utilising the Parent field.
- Parent dropdown field consists of Area records.

## Customise Area

- To introduce new fields or functions in a new module, develop a Python file extending the “spp.area” and integrate this file into `models/__init__.py`.
- Upgrade the module incorporating the new Python file.
- To integrate new fields into the UI, developers should familiarise themselves with view, view inheritance and the use of xpath in Odoo.

## Sample Use-case

A city may be included in an area, below is the sample model for this scenario

```python
class City(models.Model):
   _name = "spp.city"

   name = fields.Char(required=True)
   area_id = fields.Many2one("spp.area")
```

A city may have multiple area, below is the sample model for this scenario

```python
class City(models.Model):
   _name = "spp.city"

   name = fields.Char(required=True)
   area_ids = fields.One2many("spp.area", "city_id")

class Area(models.Model):
   _inherit = "spp.area"

   city_id = fields.Many2one("spp.city")
```

## Additional References

- Below are some Odoo references that may help in adding the field both in models and in UI. For further guidance on model creation, inheritance, and UI integration, the following Odoo documentation may be useful:
  - [Views](https://www.odoo.com/documentation/15.0/developer/reference/backend/views.html)
  - [Chapter 4: Models And Basic Fields](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/04_basicmodel.html)
  - [Chapter 7: Basic Views](https://www.odoo.com/documentation/17.0/developer/tutorials/getting_started/07_basicviews.html#chapter-7-basic-views)
  - [Chapter 13: Inheritance](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/13_inheritance.html)
  - [Chapter 14: Interact With Other Modules](https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/14_other_module.html)

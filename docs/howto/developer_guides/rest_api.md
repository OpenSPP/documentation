# Implementing Custom REST API

This comprehensive guide is designed to assist you in implementing and customizing the REST API within OpenSPP by developing a custom module. It is tailored for individuals with a specific set of prerequisites, including proficiency in Python, Odoo, OOP, HTML, XML, Xpaths, REST API concepts, and tools like Postman or curl. Moreover, a functional OpenSPP installation and administrative backend access are essential.

## Odoo Setup from Docker using doodba

- Existence of openg2p_program folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_programs.
- Existence of openg2p_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership.
- Existence of openspp_registry folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: spp_api, spp_api_records, spp_oauth, spp_service_points, spp_service_point_device, spp_programs, g2p_entitlement_cash, spp_entitlement_in_kind, spp_ent_trans, spp_area, spp_programs_sp.
- Existence of queue folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: queue_job
- Existence of web folder in odoo/custom/src. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, notify OpenSPP docker admins to add the missing repo to repos.yaml and addons.yaml.
- Availability of modules: web, web_domain_field.

## Odoo Setup from source

- Existence of openg2p-program folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-program.git) into odoo/custom, navigate to the openg2p-program folder, and switch to the specified branch.
- Availability of modules: g2p_programs.
- Existence of openg2p-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0-1.0-develop, and update the branch. If absent, clone the repository from [here](https://github.com/OpenG2P/openg2p-registry.git) into odoo/custom, navigate to the openg2p-program folder, and switch to the specified branch.
- Availability of modules: g2p_registry_base, g2p_registry_individual, g2p_registry_group, g2p_registry_membership.
- Existence of openspp-registry folder in odoo/custom. If present, navigate to this folder, switch to branch 15.1.1-mono-repo, and update the branch. If absent, clone the repository from [here](https://github.com/OpenSPP/openspp-registry.git) into odoo/custom, navigate to the openspp-registry folder, and switch to the specified branch.
- Availability of modules: spp_api, spp_api_records, spp_oauth, spp_service_points, spp_service_point_device, spp_programs, g2p_entitlement_cash, spp_entitlement_in_kind, spp_ent_trans, spp_area, spp_programs_sp.
- Existence of queue folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/queue.git) into odoo/custom, navigate to the queue, and switch to the specified branch.
- Availability of modules: queue_job.
- Existence of web folder in odoo/custom. If present, navigate to this folder, switch to branch 15.0, and update the branch. If absent, clone the repository from [here](https://github.com/OCA/web.git) into odoo/custom, navigate to the web, and switch to the specified branch.
- Availability of modules: web, web_domain_field

## Installation

- Log into OpenSPP with administrative rights.
- Access the “Apps” menu from the dashboard to manage OpenSPP modules.
- Choose “Update Apps List” to refresh the module list.
- Search and initiate installation of the following modules, this process will also install all of their associated modules:
  - OpenSPP API: Oauth
  - OpenSPP REST API
  - OpenSPP REST API: API Records

## Utilising the REST API Module

- Navigate to OpenAPI then open the record “spp_api”.
- Check API Paths in the “Paths” tab and their respective models and methods.
- Check users in the Allowed Users.
- Navigate to Settings -> Users & Companies -> Users and search one user that is in the “Allowed Users” in the OpenAPI page then enter that record.
- Select the “Allowed APIs” tab and copy the value in the field OpenAPI Token.
- Browse https://www.base64encode.org/
- Encode the combination of database name and OpenAPI Token in this format <db_name>:<token>. e.g. odoo15:1d9fd9db-705a-42cc-830c-88d6edc7bfe5

  - Copy the encoded result.
  - Send a request to one of the paths by using the encoded token as authentication.
  - Open Postman and use the following information to send request.
    - url: http://localhost:8069/api/spp_api/1/Group
  - method: GET
  - parameters: request_id=<any unique alphanumeric value>
  - headers:
    - Authorization = Basic <encoded token>
    - Accept = application/json
  - Send a request.
    ![](./rest_api/3.png)

- Click the API Document Link in the OpenAPI page to learn more about REST API.

---
myst:
  html_meta:
    "title": "Social Registry 2 for Social Protection Programs"
    "description": "OpenSPP Social Registry product configuration for centralized beneficiary identification, registration, and needs assessment"
    "keywords": "OpenSPP, social registry, beneficiary identification, targeting, social protection, needs assessment"
---

# Social Registry

An OpenSPP-based Social Registry is a strategic national asset for a government. Instead of being just a list of beneficiaries, it serves as a foundational platform for building a more equitable society. This registry is a dynamic, living system designed to be a continuous gateway for inclusion that integrates data management and transparent governance mechanisms to provide a single source of truth.

## How it works

**Registration and data collection:** The process begins with an initial registration effort, which can be accomplished through a large-scale field campaign or a bulk import of existing data. The system is continuous and open, allowing anyone to register at any time through on-demand applications. When a household's circumstances change, for example when a new child is born, a family member becomes disabled, or a job is lost, citizens can report these changes through a structured workflow. Data collection can also be customized to specific local needs, such as tracking crop types for farmers or documenting specific climate risks for coastal communities. This continuous intake mechanism ensures the data remains current, making the registry a reliable and responsive source of information.

Read more about {doc}`Unified and hierarchical beneficiary registry <../features/unified_registry>` and {doc}`Key terminology <../concepts/registrant_concepts>`. 

**Targeting and integrated service delivery:** The registry serves as a central data repository that supports a wide array of government programs, from cash transfers to in-kind benefits and services for the elderly or persons with disabilities. It provides a flexible approach to eligibility and targeting allowing a government to automatically identify citizens who meet criteria for specific categorical programs, such as all elderly individuals or families with disabled members. For more complex needs, policymakers can define and automate eligibility rules based on multiple, intersecting criteria. This functionality ensures that the registry identifies "who receives what," preventing duplication and allowing for a coordinated, integrated approach to service delivery across different government agencies.

Read more about {doc}`Eligibility and targeting <../features/eligibility_targeting>`. 

**Monitoring, reporting, and public accountability:** A modern social registry must be transparent and accountable to build citizen trust. The system provides a suite of tools for oversight and public accountability. It tracks all data modifications and user actions, creating a secure and transparent record of every change. It also manages user access and permissions, ensuring data security and integrity. For high-level decision-making, the system provides data analysis tools and dashboards to inform policy and resource allocation. Citizens can be given secure access to review their own information in the system. The platform can also integrate with grievance redress mechanisms, allowing citizens to appeal eligibility decisions or report inaccuracies.

Read more about {doc}`Auditable change management <../features/change_management>` and {doc}`Grievance Redress Mechanism (GRM) <../features/grievance_redress>`. 

**Interoperability with other systems:** The registry is built with interoperability at its core, allowing it to seamlessly connect and exchange data with other government systems. This is a crucial feature that prevents data fragmentation and the creation of isolated information silos. The OpenSPP platform uses a well-documented RESTful API that enables the registry to share and receive information securely with other national databases, such as those for National IDs, health, and civil registration. By connecting these systems, the government can achieve a more comprehensive, whole-of-government approach to social services. For example, the registry could verify a person's identity and disability status by pulling information directly from the National ID and health records, ensuring that the right person receives the right benefits without requiring them to submit the same information multiple times.

Read more about {doc}`Data integration and interoperability (APIs) <../features/data_integration_apis>`. 

## OpenSPP modules included in the Social Registry

The preconfigured Social Registry product is intended to provide the basic use cases of a social registry. Note that in addition to the base product you will most likely want to add additional modules in order to match your specific needs.

The following modules are included in the OpenSPP Social Registry product:

- **{doc}`OpenSPP Base <../../reference/modules/spp_base>`**: Provides the fundamental core structure for all registrant profiles.
- **{doc}`OpenSPP Base Settings <../../reference/modules/spp_base_setting>`**: Provides essential settings and customizations.
- **{doc}`OpenSPP Custom Fields <../../reference/modules/spp_custom_field>`**: Allows for tailoring data collection to specific local needs.
- **{doc}`OpenSPP Area Management <../../reference/modules/spp_area>`**: Includes additional features for managing and organizing geographical areas within the system
- **{doc}`OpenSPP OpenID VCI Individual <../../reference/modules/spp_openid_vci_individual>`**: Enables the issuance of Verifiable Credentials (VCs) for individual registrants.
- **{doc}`OpenSPP Custom Filter <../../reference/modules/spp_custom_filter>`**: Allows control over fields displayed in filter dropdowns.
- **{doc}`OpenSPP User Roles <../../reference/modules/spp_user_roles>`**: Manages user access and permissions to the registry data, ensuring data security and integrity.

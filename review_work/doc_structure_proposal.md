# New OpenSPP Documentation Structure

This document outlines a revised structure for the OpenSPP documentation, designed to cater to different audiences (Decision Makers, Developers, Administrators/End-Users) and provide clear entry points for the platform's main use cases (Social Registry, Farmer Registry, SP-MIS). Features are grouped by functional area.

## High-Level Directory Structure

```
docs/
├── index.md                 # Main landing page (links to use cases)
│
├── overview/                # High-level info for Decision Makers &amp; new users
│   ├── index.md
│   ├── features/              # Features by Functional Area
│   │   ├── index.md           # High-level feature categories/overview
│   │   ├── registry_data_management.md  # (Example split)
│   │   ├── program_design_config.md     # (Example split)
│   │   ├── entitlement_payments.md      # (Example split)
│   │   ├── integrations_apis.md         # (Example split)
│   │   ├── administration_security.md   # (Example split)
│   │   └── reporting_monitoring.md      # (Example split)
│   ├── why_openspp.md         # (New) Benefits and use cases
│   ├── use_cases/             # Use-Case Entry Points
│   │   ├── index.md           # (Optional) Overview of use cases
│   │   ├── social_registry.md # Links to relevant SR docs
│   │   ├── farmer_registry.md # Links to relevant FR docs
│   │   └── sp_mis.md          # Links to relevant SP-MIS docs
│   ├── concepts/              # Renamed from 'explanation' for broader scope
│   │   ├── index.md
│   │   ├── digital_public_infrastructure.md
│   │   ├── social_registry.md
│   │   ├── farmer_registry.md
│   │   └── ... (other principles &amp; concepts files)
│   └── case_studies/          # (New) Examples of OpenSPP in action
│       └── index.md
│
├── getting_started/         # Initial setup for Admins &amp; Developers
│   ├── index.md
│   ├── installation_docker.md # Split from installation_guide.md
│   ├── installation_pypi.md   # Split from installation_guide.md
│   ├── initial_config.md      # (New) Basic post-install steps
│   └── poc_and_pilot.md
│
├── user_guide/              # Task-based guides for Admins &amp; End-Users
│   ├── index.md
│   ├── registry_management/   # How-to guides for registry tasks (Common/SR/FR)
│   │   ├── register_individual.md
│   │   ├── import_export_data.md # Combine import/export
│   │   └── ...
│   ├── program_management/    # How-to guides for program tasks (SP-MIS focused)
│   │   ├── create_program.md
│   │   ├── enroll_beneficiaries.md
│   │   ├── configure_entitlements.md # Combine cash/in-kind/etc.?
│   │   ├── create_cycle.md
│   │   ├── allocate_funds.md
│   │   └── ...
│   ├── administration/        # How-to guides for admin tasks (Common)
│   │   ├── user_access.md
│   │   ├── service_points.md
│   │   └── ...
│   ├── pos_usage.md           # How-to guide for POS (SP-MIS focused)
│   ├── reporting_dashboards.md # (Needs Content) How-to use reports (Common)
│   ├── grievance_management.md # (Needs Content) How-to handle grievances (Common)
│   └── consent_management.md   # (Needs Content) How-to manage consent (Common)
│
├── developer_guide/         # Technical guides for Developers
│   ├── index.md
│   ├── setup.md               # (Existing contributing/setup-build.md)
│   ├── architecture.md        # (Existing technical_reference/architecture.md)
│   ├── module_development.md  # (Existing howto/developer_guides/module.md)
│   ├── customization/         # How-to guides for customization (Link from use cases)
│   │   ├── index.md
│   │   ├── customizing_areas.md
│   │   ├── customizing_audit.md
│   │   ├── customizing_change_requests.md
│   │   ├── customizing_entitlements.md
│   │   ├── customizing_registry.md
│   │   ├── customizing_fields.md
│   │   └── ...
│   ├── integrations/          # How-to guides for integrations (Link from use cases)
│   │   ├── index.md
│   │   ├── dci.md
│   │   ├── esignet.md
│   │   ├── oidc.md
│   │   └── keycloak_beneficiary_portal.md
│   ├── api_usage/             # API guides (Common)
│   │   ├── index.md
│   │   ├── external_api_xmlrpc.md # (Existing technical_reference/external_api.rst)
│   │   └── rest_api.md          # (Existing howto/developer_guides/rest_api.md + Needs Expansion)
│   ├── troubleshooting.md     # (Existing howto/developer_guides/troubleshooting.md) (Common)
│   └── best_practices.md      # (Needs Content or integration) (Common)
│
├── reference/               # Detailed reference material
│   ├── index.md
│   ├── modules/               # Existing module documentation (Link from use cases)
│   │   ├── index.md
│   │   ├── spp_area.md
│   │   ├── g2p_programs.md
│   │   └── ... (all module files)
│   ├── api/                   # (New/Needs Expansion) Auto-generated or detailed API specs
│   │   └── index.md
│   ├── technical/             # Other technical reference (Common)
│   │   ├── index.md
│   │   ├── security.md
│   │   ├── backup.md
│   │   ├── performance.md
│   │   └── monitoring.md
│   └── glossary.rst
│
├── community/               # Contribution, support, license (Common)
│   ├── index.md             # Combined entry point
│   ├── contributing.md        # How to contribute code/docs
│   ├── code_of_conduct.md
│   ├── license.md
│   ├── security_reporting.md
│   └── support.md             # Support model, channels
│
└── _static/                 # Images, CSS, etc.
└── _templates/              # Sphinx templates
```

## Section Descriptions

1.  **Overview (`/overview/`)**
    * **Purpose:** Introduce OpenSPP, explain its value proposition, core concepts, features grouped by functional area, and provide entry points for specific use cases.
    * **Audience:** Primarily Decision Makers, new users.
    * **Content:** Introduction, feature overview/details (`features/`), use-case landing pages, conceptual explanations (`concepts/`), case studies.

2.  **Getting Started (`/getting_started/`)**
    * **Purpose:** Guide users through installing and setting up a working OpenSPP instance.
    * **Audience:** Administrators, Developers.
    * **Content:** Installation procedures, initial configuration steps, PoC/Pilot info.

3.  **User Guide (`/user_guide/`)**
    * **Purpose:** Provide practical, task-oriented instructions for using OpenSPP's features in day-to-day operations. Primarily *How-to Guides*.
    * **Audience:** Administrators, End-Users.
    * **Content:** Step-by-step guides for specific tasks like registering beneficiaries, creating programs, managing funds, using the POS, administration, etc.

4.  **Developer Guide (`/developer_guide/`)**
    * **Purpose:** Provide technical information and instructions for developers who need to customize, extend, integrate with, or contribute to OpenSPP. Contains both *How-to Guides* and *Reference* material relevant to development.
    * **Audience:** Developers.
    * **Content:** Setup, architecture, module development, customization guides, integration guides, API usage, troubleshooting.

5.  **Reference (`/reference/`)**
    * **Purpose:** Provide detailed, factual information about specific components like modules, APIs, and technical specifications. Designed for lookup.
    * **Audience:** Developers, Administrators.
    * **Content:** Module documentation, detailed API specifications, glossary, technical deep-dives.

6.  **Community (`/community/`)**
    * **Purpose:** Information about the OpenSPP project, community interaction, contribution processes, and legal information.
    * **Audience:** All users, potential contributors.
    * **Content:** Contribution guidelines, code of conduct, license, security policy, support channels.

## Key Changes &amp; Rationale

* **Folder Names:** Removed leading numbers from top-level directories (e.g., `overview/` instead of `1_overview/`) for cleaner paths. The logical order is maintained via `toctree` directives.
* **Features Section:** Features are grouped by functional area (e.g., `registry_data_management.md`) within `/overview/features/`.
* **Use-Case Entry Points:** Maintained the `/overview/use_cases/` directory for guiding users based on their primary goal (SR, FR, SP-MIS).
* **Guide Structure:** Kept the User/Developer guide separation and the linking approach from use-case pages to avoid duplication.
* **Concepts Renamed:** Renamed `explanation` to `concepts` to better reflect the inclusion of principles and broader context.


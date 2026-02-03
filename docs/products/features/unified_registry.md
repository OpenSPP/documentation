---
myst:
  html_meta:
    "title": "Unified and Hierarchical Beneficiary Registry"
    "description": "OpenSPP unified registry feature providing single source of truth for beneficiary data with hierarchical group management"
    "keywords": "OpenSPP, unified registry, beneficiary registry, hierarchical groups, data management, social protection"
---

# Unified and hierarchical beneficiary registry

OpenSPP's Unified and Hierarchical {term}`Beneficiary Registry` serves as the single source of truth for all program participants, managing both individual records and complex nested group structures within {term}`social protection` programs.

## The data fragmentation challenge

Social protection programs often struggle with data fragmentation, where beneficiary information is scattered across multiple systems, leading to duplication, inconsistencies, and inefficient service delivery. OpenSPP's unified registry solves this fundamental challenge by centralizing all registrant data into a single, authoritative database that can serve multiple programs simultaneously. This approach eliminates redundant data collection, reduces administrative overhead, and ensures that program managers work with accurate, up-to-date information.

The hierarchical nature of the registry is particularly powerful for managing complex social structures. Many social protection interventions target {term}`households <household>` or community groups rather than individuals. OpenSPP's registry can model these real-world relationships accurately, allowing programs to work with nested structures where groups can contain other groups, individuals can belong to multiple groups with different roles, and relationships between entities are explicitly defined and tracked. This flexibility enables the platform to adapt to diverse program requirements without forcing artificial constraints on how beneficiary data is organized.

## Core registry capabilities

* **Comprehensive data capture**: Records detailed demographic information, national IDs, contact details, and banking information for both individuals and groups
* **Flexible relationship management**: Defines and tracks relationships between registrants such as Head of Household, Dependent, Guardian, and custom relationship types specific to program needs
* **Multi-Level group hierarchies**: Supports nested group structures where groups can be members of other groups, enabling representation of complex organizational structures like cooperatives within districts
* **Unified identity management**: Maintains a single identity for each registrant that can be referenced across multiple programs, preventing duplication and ensuring consistency
* **Dynamic membership tracking**: Records time-bound memberships with start and end dates, allowing historical tracking of group composition changes
* **Banking and payment integration**: Stores multiple bank accounts per registrant with validation and verification capabilities for seamless payment processing
* **Custom field extension**: Allows programs to define additional data fields specific to their requirements without modifying core registry structure

## Technical architecture

The registry functionality is implemented through several specialized modules:

* **{doc}`spp_registry </reference/modules/spp_registry>`**: Core registry framework providing the foundational data models and business logic
* **spp_registry_group_hierarchy**: Advanced hierarchical group structures allowing groups within groups
* **{doc}`spp_banking </reference/modules/spp_banking>`**: Banking information management and validation for payment processing
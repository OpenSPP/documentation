---
myst:
  html_meta:
    "title": "Unified and Hierarchical Beneficiary Registry"
    "description": "OpenSPP unified registry feature providing single source of truth for beneficiary data with hierarchical group management"
    "keywords": "OpenSPP, unified registry, beneficiary registry, hierarchical groups, data management, social protection"
---

# Unified and Hierarchical Beneficiary Registry

OpenSPP's Unified and Hierarchical {term}`Beneficiary Registry` serves as the single source of truth for all program participants, managing both individual records and complex nested group structures within {term}`social protection` programs.

## The Data Fragmentation Challenge

Social protection programs often struggle with data fragmentation, where beneficiary information is scattered across multiple systems, leading to duplication, inconsistencies, and inefficient service delivery. OpenSPP's unified registry solves this fundamental challenge by centralizing all registrant data into a single, authoritative database that can serve multiple programs simultaneously. This approach eliminates redundant data collection, reduces administrative overhead, and ensures that program managers work with accurate, up-to-date information.

The hierarchical nature of the registry is particularly powerful for managing complex social structures. Many social protection interventions target {term}`households <household>` or community groups rather than individuals. OpenSPP's registry can model these real-world relationships accurately, allowing programs to work with nested structures where groups can contain other groups, individuals can belong to multiple groups with different roles, and relationships between entities are explicitly defined and tracked. This flexibility enables the platform to adapt to diverse program requirements without forcing artificial constraints on how beneficiary data is organized.

## Core Registry Capabilities

* **Comprehensive Data Capture**: Records detailed demographic information, national IDs, contact details, and banking information for both individuals and groups
* **Flexible Relationship Management**: Defines and tracks relationships between registrants such as Head of Household, Dependent, Guardian, and custom relationship types specific to program needs
* **Multi-Level Group Hierarchies**: Supports nested group structures where groups can be members of other groups, enabling representation of complex organizational structures like cooperatives within districts
* **Unified Identity Management**: Maintains a single identity for each registrant that can be referenced across multiple programs, preventing duplication and ensuring consistency
* **Dynamic Membership Tracking**: Records time-bound memberships with start and end dates, allowing historical tracking of group composition changes
* **Banking and Payment Integration**: Stores multiple bank accounts per registrant with validation and verification capabilities for seamless payment processing
* **Custom Field Extension**: Allows programs to define additional data fields specific to their requirements without modifying core registry structure

## Technical Architecture

The registry functionality is implemented through several specialized modules:

* **[g2p_registry_base](/reference/modules/g2p_registry_base.md)**: Core registry framework providing the foundational data models and business logic
* **[spp_registry_base](/reference/modules/spp_registry_base.md)**: OpenSPP-specific registry extensions adding enhanced functionality
* **[g2p_registry_individual](/reference/modules/g2p_registry_individual.md)**: Individual registrant management with personal information and identity documentation
* **[g2p_registry_group](/reference/modules/g2p_registry_group.md)**: Group registrant management supporting various group types and structures
* **[g2p_registry_membership](/reference/modules/g2p_registry_membership.md)**: Relationship and membership management between individuals and groups
* **[spp_registry_group_hierarchy](/reference/modules/spp_registry_group_hierarchy.md)**: Advanced hierarchical group structures allowing groups within groups
* **[g2p_bank](/reference/modules/g2p_bank.md)**: Banking information management and validation for payment processing
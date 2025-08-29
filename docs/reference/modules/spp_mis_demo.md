---
orphan: true
---

# OpenSPP Mis Demo

The OpenSPP Mis Demo module provides a comprehensive set of demonstration data and functionalities for the OpenSPP system. It populates the platform with pre-configured, realistic data, allowing users to explore the system's capabilities in managing social protection programs and registries without manual data entry.

## Purpose

The OpenSPP Mis Demo module accomplishes the following key objectives:

*   **Generates Realistic Sample Data:** It populates the system with diverse and realistic data for individuals, groups, and social protection programs, mimicking real-world scenarios for effective testing and exploration.
*   **Facilitates User Training and Exploration:** New users can quickly familiarize themselves with the OpenSPP interface, data structures, and workflows using pre-existing data, accelerating the learning curve.
*   **Showcases System Capabilities:** The module demonstrates the full potential of OpenSPP by illustrating how various modules interact, how data flows, and how programs are managed from enrollment to entitlement disbursement.
*   **Supports Development and Testing:** Developers and implementers gain a robust sandbox environment to test new features, validate configurations, and understand system behavior with a representative dataset.

This module is crucial for anyone looking to understand, train on, or test the OpenSPP platform without the overhead of creating extensive datasets from scratch. It provides immediate value by offering a fully functional, data-rich environment for hands-on experience.

## Dependencies and Integration

The OpenSPP Mis Demo module integrates deeply with several foundational OpenSPP components to generate its rich dataset:

*   **[OpenSPP Base Demo](spp_base_demo)**: It builds upon the core demonstration framework, providing the initial setup for demo data.
*   **[OpenSPP Base](spp_base)**: The module utilizes core OpenSPP functionalities and extensions to Odoo's base models.
*   **[G2P Registry: Base](g2p_registry_base)**, **[G2P Registry: Individual](g2p_registry_individual)**, **[G2P Registry: Group](g2p_registry_group)**, and **[G2P Registry: Membership](g2p_registry_membership)**: These modules are essential for generating comprehensive individual and group registrant profiles, including their demographic details and household structures.
*   **[G2P Programs](g2p_programs)**: This module is leveraged to create demonstration social protection programs, define their eligibility rules, and simulate program cycles and entitlements.
*   **[OpenSPP Custom Field](spp_custom_field)** and **[OpenSPP Custom Field Recompute Daily](spp_custom_field_recompute_daily)**: It populates various custom fields and vulnerability indicators on registrant profiles, which can then be dynamically recomputed to reflect changing conditions.
*   **[OpenSPP Area](spp_area)**: The module generates registrant data that can be linked to geographical areas, demonstrating how registrants are organized within a hierarchical administrative structure (e.g., country > province > district).
*   **[Queue Job](queue_job)**: For large-scale data generation, this module uses background processing to ensure that the system remains responsive, preventing performance bottlenecks.
*   **Product** and **Stock**: It creates sample products and inventory items, which can represent in-kind benefits distributed through social protection programs.
*   **[OpenSPP Custom Filter UI](spp_custom_filter_ui)**: This ensures that the user interface for filtering and searching through the generated demo data is intuitive and aligned with OpenSPP's customized views.

## Additional Functionality

The OpenSPP Mis Demo module offers several key features for generating and managing demonstration data:

### Registrant and Group Data Generation
Users can generate a specified number of individual registrants and groups (households) with diverse characteristics. This includes:
*   **Demographic Variety:** Creates individuals with varied names, genders, birthdates, and age groups (children, adults, elderly) using multilingual data.
*   **Vulnerability Indicators:** Populates custom fields for individuals and groups, such as disability levels, medical conditions, and indicators for pregnancy or lactation, showcasing OpenSPP's ability to capture nuanced data.
*   **Household Structures:** Establishes realistic group memberships, assigning individuals as heads of household or principal recipients within their respective groups.

### Program and Entitlement Simulation
The module allows for the generation of complete social protection programs, simulating their operational lifecycle:
*   **Program Creation:** Generates multiple programs with configurable target types, either for individuals or groups.
*   **Cycle Management:** Simulates multiple program cycles, including the automatic setup of eligibility and entitlement managers.
*   **Entitlement Processing:** Prepares and, optionally, approves entitlements for beneficiaries within each cycle, demonstrating the flow from program definition to benefit disbursement. This includes creating program funds to cover the generated entitlements.

### Derived Demographic and Vulnerability Reporting
Beyond raw data, the module populates summary fields on group records (`res.partner`), demonstrating how OpenSPP can derive key demographic insights:
*   **Household Composition:** Automatically calculates and populates indicators such as the number of children, children in specific age ranges (e.g., 0-11, 12 and above), and the presence of single-headed or female-headed households.
*   **Vulnerability Summaries:** Provides summary indicators for households with elderly members, disabled members, chronically ill members, or pregnant/lactating women, based on the individual member data. These derived fields are crucial for targeted program design and reporting.

## Conclusion

The OpenSPP Mis Demo module is an indispensable tool for understanding, training on, and testing the OpenSPP platform, providing a rich, pre-populated environment that mirrors real-world social protection program operations.
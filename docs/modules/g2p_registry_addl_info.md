# G2P Registry: Additional Info Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_registry_addl_info](g2p_registry_addl_info) module extends the OpenSPP platform by providing a flexible mechanism for capturing and managing additional, program-specific information for both individual and group registrants. 

## Purpose

This module aims to address the need for capturing data points that are not part of the core registrant information but are crucial for specific social protection programs. It achieves this by adding a dedicated "Additional Information" section to both individual and group registrant forms. 

## Functionality

The module introduces the following key features:

- **JSON Field for Additional Information:** A dedicated JSON field `additional_g2p_info` is added to the `res.partner` model. This field allows storing unstructured data, providing flexibility in capturing diverse program-specific information.
- **Customizable Input Widget:** A dedicated Javascript widget `g2p_registry_addl_info_widget` is used to render and manage the content of the `additional_g2p_info` field. This allows for dynamic and user-friendly data entry tailored to the specific requirements of different programs.
- **Integration with Registrant Forms:** The "Additional Information" section is seamlessly integrated into both the [g2p_registry_individual](g2p_registry_individual) and [g2p_registry_group](g2p_registry_group) forms, ensuring that program implementers can easily access and manage this additional data.

## Dependencies

The [g2p_registry_addl_info](g2p_registry_addl_info) module depends on the following modules:

- [g2p_registry_base](g2p_registry_base): Provides the foundational framework for the G2P registry.
- [g2p_registry_individual](g2p_registry_individual): Enables the registration and management of individual registrants.
- [g2p_registry_group](g2p_registry_group): Facilitates the registration and management of group registrants.

## Benefits

- **Enhanced Data Capture:** Enables capturing a wider range of data points relevant to specific social protection programs.
- **Program Flexibility:** Accommodates diverse data needs without requiring code-level modifications.
- **Improved Data Management:** Provides a structured approach to managing additional registrant information.

By providing a flexible and extensible mechanism for managing additional registrant information, the [g2p_registry_addl_info](g2p_registry_addl_info) module empowers program implementers to effectively tailor OpenSPP to the unique requirements of their social protection initiatives.

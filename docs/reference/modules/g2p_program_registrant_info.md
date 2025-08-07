---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# G2P Program: Registrant Info Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_program_registrant_info](g2p_program_registrant_info) module enhances the functionality of the OpenSPP by introducing the concept of program-specific application information for registrants. This module allows program managers to collect and store additional data from registrants during the application process, which can be used to assess eligibility, track progress, and manage program participation. 

## Features

* **Program-Specific Information:** Captures and stores program-specific information during the registrant's application process.
* **Application Tracking:** Assigns a unique application ID to each application and allows tracking of its status throughout the program lifecycle.
* **Integration with Programs and Memberships:** Seamlessly integrates with the [g2p_programs](g2p_programs) and [g2p_registry_individual](g2p_registry_individual) modules to associate application information with specific programs and registrants.
* **Dynamic Data Collection:** Employs a flexible JSON field to accommodate various data structures and program-specific requirements.
* **Improved Decision Making:** Provides program managers with comprehensive information to facilitate informed decisions regarding eligibility and enrollment.

## Functionality and Integration

The module introduces a new model, `g2p.program.registrant_info`, which stores program-specific information submitted by registrants. Each record in this model represents an application instance and is linked to:

* **Registrant:** The individual or group applying to the program (`res.partner` model).
* **Program:** The specific program to which the registrant is applying ([g2p.program](g2p_program) model).
* **Program Membership:** The registrant's membership in the program, if approved ([g2p.program_membership](g2p_program_membership) model).

The module also extends the functionality of the `g2p.program_membership` model to include a one-to-many relationship with `g2p.program.registrant_info`, enabling tracking of multiple applications by the same registrant to the same program.

The [g2p_program_registrant_info](g2p_program_registrant_info) module is designed to work in conjunction with the following modules:

* **[g2p_programs](g2p_programs):** Manages program definitions and lifecycles.
* **[g2p_registry_individual](g2p_registry_individual):** Manages individual registrant information.
* **[g2p_registry_group](g2p_registry_group):** Manages group registrant information.

## Benefits

* **Enhanced Data Collection:** Allows programs to capture specific data points relevant to their operations.
* **Improved Application Management:** Facilitates efficient tracking and processing of registrant applications.
* **Data-Driven Decision Making:** Provides program managers with the necessary information to make informed decisions regarding eligibility and enrollment.
* **Increased Transparency and Accountability:** Creates a clear and auditable record of the application process.

This module contributes to the overall efficiency and effectiveness of social protection programs by providing a structured and comprehensive approach to managing registrant information during the crucial application stage. 

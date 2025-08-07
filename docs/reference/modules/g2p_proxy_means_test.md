---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# G2P: Proxy Means Test Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module extends the OpenSPP system to incorporate **Proxy Means Testing (PMT)** functionality into social protection programs. It enables program administrators to define and configure PMT parameters, automatically calculate PMT scores for registrants, and leverage these scores for program targeting and enrollment.

## Features:

- **PMT Configuration:** Enables program administrators to enable PMT for specific programs and define the parameters used in the PMT calculation ([g2p_programs](g2p_programs)).
- **Parameter Definition:** Allows administrators to select specific fields from the registrant information form ([g2p_program_registrant_info](g2p_program_registrant_info)) and assign weightages to these fields, effectively defining the PMT formula.
- **Automatic Score Calculation:** Automatically calculates and stores the PMT score for each registrant based on their provided information and the defined PMT parameters.
- **Score Visibility:** Displays the calculated PMT score on relevant forms, including the registrant information form, program membership form, and individual/group views, providing stakeholders with easy access to this information.

## Integration and Dependencies:

- **[g2p_programs](g2p_programs):** This module integrates with the core `g2p_programs` module to add PMT configuration options to program definitions. 
- **[g2p_program_registrant_info](g2p_program_registrant_info):** This module extends the functionality of `g2p_program_registrant_info` to include:
    - Calculation and storage of the PMT score.
    - Dynamic retrieval of available fields for PMT parameter definition.
    - Logic to delete related PMT parameters when a field is deleted.

## Benefits:

- **Improved Targeting:** Enables programs to target beneficiaries more effectively based on their socio-economic status.
- **Enhanced Efficiency:** Automates the PMT calculation process, reducing administrative burden and potential for errors.
- **Increased Transparency:** Provides a clear and auditable method for determining program eligibility.
- **Data-Driven Decision Making:**  Empowers program administrators to make data-informed decisions regarding program enrollment and resource allocation. 

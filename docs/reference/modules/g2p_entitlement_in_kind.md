---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# OpenG2P Entitlement: In-Kind Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module extends the functionality of the OpenSPP platform specifically for managing **in-kind** entitlements within social protection programs. 

**Purpose:**

The primary purpose of the [g2p_entitlement_in_kind](g2p_entitlement_in_kind) module is to adapt the existing OpenSPP framework for programs that distribute benefits in the form of goods or services rather than cash transfers. 

**Key Features & Functionality:**

* **Modified Program Views:** The module customizes program views inherited from the [spp_programs](spp_programs) module to accommodate in-kind distribution workflows. This includes:
    * Hiding the "Import Eligible Registrants" button as it might not be directly applicable to in-kind programs.
    * Adjusting access rights for the "Enroll Eligible Registrants" button. Enrollment in in-kind programs might follow a different process requiring involvement from specific user roles like Program Validators, Cycle Approvers, and Program Managers (as defined by the [g2p_programs](g2p_programs) module).

**Integration with other Modules:**

* **[spp_programs](spp_programs):** This module builds upon the core program management features provided by [spp_programs](spp_programs), adapting them for in-kind distribution.
* **[spp_entitlement_in_kind](spp_entitlement_in_kind):** This module likely provides the foundational data models and logic specific to in-kind entitlements, which this module then extends with user interface elements and program-level integration.

**Note:** 

This module is part of a larger ecosystem aimed at providing flexible and configurable tools for managing diverse social protection programs. The specific configurations and adaptations offered by this module highlight its focus on supporting programs with in-kind benefit delivery mechanisms. 

---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# G2P Programs REST API Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [`g2p_programs_rest_api`](g2p_programs_rest_api) module extends the functionality provided by the [`g2p_registry_rest_api`](g2p_registry_rest_api) and [`g2p_programs`](g2p_programs) modules to expose program-related data and operations through a REST API. 

## Functionality

This module focuses on integrating program information with the registry data. It allows external systems to:

- **Manage program memberships:** Create, read, update, and delete program membership information for registrants.
- **Retrieve program-specific registrant data:** Access registrant information enriched with their program memberships, including enrollment and exit dates. 
- **Manage program memberships for groups:**  Handle program membership data within the context of groups registered in the system.

## Data Models

This module introduces new data structures and extends existing ones from the [`g2p_registry_rest_api`](g2p_registry_rest_api) module:

- **`RegistrantProgramMembershipIn`** and **`RegistrantProgramMembershipOut`**: Represent program membership information for individual registrants, including enrollment and exit dates.
- **`RegistrantProgramMemberInfoIn`** and **`RegistrantProgramMemberInfoOut`**: Extend the `RegistrantInfoIn` and `RegistrantInfoOut` models from [`g2p_registry_rest_api`](g2p_registry_rest_api) to include program membership details.
- **`GroupMembersInfoIn`**: Extends the `GroupMembersInfoIn` model from [`g2p_registry_rest_api`](g2p_registry_rest_api) to include program membership details for members of a group.

## Integration

The [`g2p_programs_rest_api`](g2p_programs_rest_api) module seamlessly integrates with:

- **[`g2p_registry_rest_api`](g2p_registry_rest_api)**: It leverages the existing API infrastructure and data models for registrants and groups.
- **[`g2p_programs`](g2p_programs)**: It interacts with this module to retrieve and manage program-related data within the DCI system. 

This module enables efficient data exchange and synchronization between the OpenSPP system and external systems that require access to program and beneficiary information. 

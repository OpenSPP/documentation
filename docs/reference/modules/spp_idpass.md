---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# spp_idpass Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [spp_idpass](spp_idpass) module extends the functionality of the OpenSPP system by providing a seamless way to generate and manage digital ID cards for registrants. It integrates with the existing registry system and leverages external ID Pass API services to produce printable ID cards. 

## Key Features

* **ID Card Generation:** Generates digital ID cards for individual registrants or groups using an external ID Pass API.
* **ID Card Storage:** Stores generated ID cards as PDF attachments on the registrant's profile within the system.
* **ID Pass API Integration:** Configurable settings for connecting with external ID Pass API services, including authentication and data transmission.
* **ID Card Design Customization:**  Allows for setting a file name prefix for generated ID cards and managing the expiry duration for issued IDs.

## Integration with Other Modules

* **[g2p_registry_base](g2p_registry_base):** The module relies on the base registry module for accessing and managing registrant information.
* **[g2p_registry_membership](g2p_registry_membership):**  Utilizes the membership module to handle ID card generation for groups, ensuring the correct identification of the group head. 

## Functionality and Workflow

1. **Configuration:** System administrators configure the connection to the ID Pass API by providing the necessary URLs, credentials, and other settings.
2. **ID Card Issuance:** Authorized users can initiate the ID card generation process for a registrant directly from the registrant's profile.
3. **Data Transmission:** The module securely transmits the required registrant data to the ID Pass API for card generation.
4. **ID Card Retrieval:** Upon successful generation, the module retrieves the ID card in PDF format from the API.
5. **ID Card Storage:**  The generated ID card is automatically attached to the corresponding registrant's profile and can be downloaded or printed as needed.

## Benefits

* **Improved Identification:**  Provides a standardized and verifiable identification method for program beneficiaries.
* **Enhanced Program Efficiency:** Streamlines the identification process, reducing administrative burden and potential errors.
* **Increased Transparency and Accountability:** Creates a digital record of issued ID cards, improving program monitoring and evaluation.

## Note:

This module requires an active subscription and integration with a compatible ID Pass API service.

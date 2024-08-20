# G2P Program: Program Registrant Info REST API 

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module extends the functionality of the [g2p_programs_rest_api](g2p_programs_rest_api) and [g2p_program_registrant_info](g2p_program_registrant_info) modules to expose program registrant information via a REST API. This allows external systems to interact with and manage program-specific data associated with registrants.

### Functionality:

- **Exposes Program Registrant Info:** Provides API endpoints to access and manipulate program-specific information of registrants within a program. This includes data such as enrollment status, benefit level, and other custom fields defined for the program.

### Integration:

- **[g2p_programs_rest_api](g2p_programs_rest_api):** This module extends the existing API endpoints for managing program memberships. It adds fields to include program registrant information when retrieving or updating memberships.
- **[g2p_program_registrant_info](g2p_program_registrant_info):** This module utilizes the data models defined in `g2p_program_registrant_info` to represent and handle program-specific information.

### Data Models:

- **ProgramRegistrantInfoOut:**  Represents the output format of program registrant information returned by the API. It includes fields like `state` and a dictionary or list of dictionaries for `program_registrant_info`. 
- **ProgramMembershipIn/Out:** Extends the existing input and output models for program memberships defined in [g2p_programs_rest_api](g2p_programs_rest_api). The `ProgramMembershipIn` model adds an optional field `program_registrant_info` for receiving program-specific data. The `ProgramMembershipOut` model includes a list of `ProgramRegistrantInfoOut` objects under the field `program_registrant_info_ids`.

### Benefits:

- **Seamless Integration:** Enables external applications to access and manage program-specific registrant data directly.
- **Enhanced Data Management:** Facilitates efficient handling and updating of program-related information for individual registrants.
- **Improved Interoperability:** Promotes interoperability between the OpenSPP system and other systems requiring access to program registrant details.

This module is essential for integrating OpenSPP with external systems that need to interact with program-specific information of registrants. It provides a structured and secure way to access and manage this data, further enhancing the efficiency and transparency of social protection programs. 

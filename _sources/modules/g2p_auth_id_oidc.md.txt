# g2p_auth_id_oidc Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module extends the OpenG2P Auth module to allow user authentication and registration using OIDC (OpenID Connect) while linking them to their existing G2P Registrant IDs. 

**Purpose:**

The primary goal of this module is to streamline the user registration and login process by leveraging existing G2P Registrant IDs within the OpenG2P system. Instead of creating new user accounts from scratch, this module allows users to authenticate using their OIDC credentials and then links them to their pre-existing G2P registration data. 

**Key Features:**

* **OIDC Integration for Authentication:**  Users can authenticate using their credentials from an OIDC provider.
* **G2P Registrant ID Mapping:**  The module maps the authenticated OIDC user to their corresponding G2P Registrant ID stored in the [g2p_registry_base](g2p_registry_base) module.
* **Automated Partner/User Creation:**  If a matching G2P Registrant ID is found, the module automatically creates a linked Partner and User in DCI, pulling relevant data from the registration record. 
* **Customizable Data Mapping:**  Administrators can configure how data from the OIDC provider and the G2P registry is mapped to DCI Partner and User fields.

**How it Works:**

1. **OIDC Authentication:**  A user initiates the login process via an OIDC provider. 
2. **G2P ID Lookup:**  The module extracts the user's ID from the OIDC response and attempts to find a matching G2P Registrant ID.
3. **Account Creation/Linking:**
    * **Match Found:**  If a match is found, the module retrieves the registration data and creates/updates the corresponding Partner and User records in DCI.
    * **No Match:** The module can be configured to either deny access or initiate a more detailed registration process, potentially pulling additional data from the OIDC provider. 
4. **User Login:**  Upon successful authentication and account linking, the user is logged into the OpenG2P system.

**Dependencies:**

* **[g2p_registry_base](g2p_registry_base):** This module depends on the base registry module for accessing and retrieving G2P Registrant data.

**Benefits:**

* **Simplified User Experience:**  Easier registration and login process for beneficiaries already registered within the OpenG2P system.
* **Improved Data Accuracy:**  Leveraging existing G2P Registrant data ensures consistency and reduces the risk of duplicate records.
* **Enhanced Security:**  Integration with trusted OIDC providers enhances the security of the OpenG2P platform. 

**Notes:**

* The module relies on a consistent and accurate mapping between OIDC user identifiers and G2P Registrant IDs. 
* Proper configuration of OIDC settings and data mapping is crucial for the module's functionality.

**TODOs:**

* The original module references an `auth_oidc` module that has been removed. A suitable replacement needs to be integrated into the codebase for the OIDC functionality. 
* The code comments highlight areas that require further improvement, such as refining the data mapping logic and enhancing error handling. 

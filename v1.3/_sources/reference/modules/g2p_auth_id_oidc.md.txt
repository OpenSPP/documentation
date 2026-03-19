---
orphan: true
---

# G2P Auth: OIDC - Reg ID

The `g2p_auth_id_oidc` module extends OpenSPP's OpenID Connect (OIDC) authentication capabilities to specifically manage and authenticate G2P registrant IDs. It bridges external identity provider verification with OpenSPP's registrant registry, ensuring that the identities of individuals and groups are securely linked and validated against official records.

## Purpose

This module provides critical functionality for securely identifying and managing OpenSPP registrants through OIDC, offering several key capabilities:

*   **Secure Registrant Identity Verification**: Leverages OIDC to authenticate and verify the identity of individuals and groups against external identity providers. This ensures that the registrant's provided ID (e.g., National ID, Passport Number) is officially validated.
*   **Automated Registrant ID Linking**: Automatically associates authenticated OIDC user IDs (claims) with existing `g2p.reg.id` records in OpenSPP. This streamlines the process of connecting external identities to internal registrant profiles.
*   **Streamlined Registrant Profile Population**: Utilizes data received from the OIDC provider, such as names and phone numbers, to automatically populate or update individual and group registrant profiles. For example, a registrant's given name and family name from OIDC can directly populate their OpenSPP profile.
*   **Authentication Status Tracking**: Records the authentication status and the last successful authentication timestamp directly on the `g2p.reg.id` record. This provides an audit trail and clear indication of a registrant's verified status.
*   **Configurable ID Type Integration**: Allows administrators to specify which type of G2P Registrant ID (e.g., National ID, Voter ID) an OIDC provider is configured to authenticate. This ensures flexibility in integrating various national identity schemes.

## Dependencies and Integration

The `g2p_auth_id_oidc` module is a crucial extension that integrates deeply with OpenSPP's core authentication and registry components:

*   **[G2P Auth Oidc](g2p_auth_oidc)**: This module builds upon the foundational OIDC authentication provided by `g2p_auth_oidc`. It customizes the OIDC login flow to specifically search for and interact with G2P registrant IDs and profiles during the authentication process.
*   **[G2P Registry Individual](g2p_registry_individual)** and **[G2P Registry Group](g2p_registry_group)**: It interacts directly with these modules to create or update individual and group registrant profiles based on data obtained during OIDC authentication. This ensures that validated external data seamlessly populates the relevant registrant fields.
*   **Auth OAuth Provider (`auth.oauth.provider`)**: It extends the OIDC provider configuration by adding a specific field to link an external OIDC provider to a designated G2P Registrant ID Type. This enables the system to understand which type of OpenSPP ID the external provider is verifying.
*   **G2P ID Type (`g2p.id.type`)** and **G2P Registrant ID (`g2p.reg.id`)**: This module directly works with these models. It maps OIDC claims to specific `g2p.reg.id` entries, updates their authentication status, and facilitates the re-authentication of these IDs.

## Additional Functionality

### Mapping OIDC Claims to Registrant IDs

This module allows administrators to configure how OIDC claims are mapped to OpenSPP registrant IDs. Upon successful authentication, the system can identify and link the OIDC `user_id` claim to a specific `g2p.reg.id` record. If the OIDC provider returns multiple `user_id` claims (e.g., `user_id123` for a specific ID type with ID `123`), the module can map these to corresponding `g2p.reg.id` entries, either updating existing ones or creating new ones if not found.

### Automated Registrant Profile Population

When a registrant successfully authenticates via OIDC, the module automatically populates or updates their OpenSPP profile. It processes OIDC claims such as the registrant's `name` (breaking it down into `given_name`, `family_name`, and `addl_name`) and `phone` to ensure the registrant's profile is accurate and complete. Additionally, it sets the `is_registrant` flag to true for individuals and `is_group` to false, confirming their status within the registry.

### Registrant ID Authentication Status Management

The module tracks the authentication status of each `g2p.reg.id` record. Upon successful OIDC authentication, the `authentication_status` field on the corresponding `g2p.reg.id` is updated to "Authenticated," and the `last_authentication_time` is recorded. This provides a clear, real-time indication of a registrant's verified identity. The system also supports initiating re-authentication for a specific registrant ID, guiding the user back to the appropriate OIDC provider.

## Conclusion

The `g2p_auth_id_oidc` module is essential for securely integrating external identity verification with OpenSPP's registrant management, streamlining the process of authenticating and maintaining accurate profiles for individuals and groups in social protection programs.
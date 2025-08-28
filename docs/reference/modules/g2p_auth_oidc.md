# G2P Auth Oidc

The `g2p_auth_oidc` module extends OpenSPP's authentication capabilities to support OpenID Connect (OIDC), enabling secure and flexible user logins through external identity providers. This module integrates OpenSPP with various OIDC-compliant services, streamlining user management and enhancing security.

## Purpose

This module provides robust OpenID Connect integration, offering several key capabilities:

*   **Enhanced Security**: Leverages OIDC's robust authentication protocols, including Proof Key for Code Exchange (PKCE), to provide a highly secure login experience for OpenSPP users. This protects sensitive user data and adheres to modern security standards.
*   **Flexible Identity Management**: Integrates OpenSPP with various OIDC-compliant identity providers, allowing organizations to centralize user management and leverage existing identity infrastructure. This reduces administrative overhead and ensures a consistent user experience.
*   **Streamlined User Onboarding**: Automates the creation of new OpenSPP user accounts and synchronizes essential user data and group memberships directly from the OIDC provider. This facilitates faster user access and ensures accurate profile information.
*   **Customizable User Data Mapping**: Provides tools to map specific OIDC claims (e.g., `name`, `email`, `groups`) to corresponding fields in OpenSPP user profiles. This ensures adaptability to different identity provider schemas and precise data population.
*   **Controlled User Signup**: Allows administrators to define policies for user registration, enabling or restricting automatic account creation based on OIDC authentication. This provides granular control over who can access the system.

## Dependencies and Integration

The `g2p_auth_oidc` module builds upon the core [Auth OAuth](auth_oauth) module, extending its functionality to specifically handle OpenID Connect protocols. It modifies the `auth.oauth.provider` model to include OIDC-specific configurations such as authentication flows, JWKS URLs, and client assertion details.

It also extends the `res.users` model to manage OIDC user attributes, ensuring seamless synchronization of user profiles and group memberships. This foundational integration allows OpenSPP to act as a Relying Party, trusting external OIDC Identity Providers for user authentication and authorization.

## Additional Functionality

### OpenID Connect Flow and Security Configuration

Administrators configure OIDC providers by selecting the appropriate authentication flow, such as the Authorization Code Flow for enhanced security or the Implicit Flow. The module automatically generates Proof Key for Code Exchange (PKCE) code verifiers to prevent authorization code interception attacks. It supports various client authentication methods like Client Secret (Basic/Post) and Private Key JWT, ensuring secure communication between OpenSPP and the identity provider.

### User Provisioning and Profile Synchronization

Upon successful authentication, the module can automatically create new user accounts in OpenSPP if enabled. For existing users, it updates their profiles with information received from the OIDC provider. Administrators can control whether user profile information and group memberships are synchronized on every login or only when explicitly reset by the user or administrator.

### Customizable Claim-to-Field Mapping

The `token_map` field allows administrators to define how claims from the OIDC `id_token` or `access_token` map to specific OpenSPP user fields. For example, `sub:user_id name:name email:email` maps the OIDC 'subject' claim to OpenSPP's 'user_id', the 'name' claim to the user's name, and the 'email' claim to the user's email address. This flexibility ensures that OpenSPP accurately populates user attributes like birthdate, gender, and phone number based on the identity provider's data.

### Granular Signup and Group Management

OpenSPP allows administrators to control user signup behavior, either permitting new user creation based on OIDC authentication, denying signup (invitation only), or deferring to system-wide signup settings. Default groups can be assigned to newly registered users, ensuring they have appropriate permissions from their first login. The module also processes groups or roles received from the OIDC provider, mapping them to existing OpenSPP user groups.

```{note}
When mapping claims to fields, ensure the `token_map` accurately reflects the claims provided by your OIDC Identity Provider to prevent data discrepancies.
```

## Conclusion

The `g2p_auth_oidc` module is crucial for integrating OpenSPP with modern identity management systems, providing secure, flexible, and automated user authentication and provisioning capabilities.
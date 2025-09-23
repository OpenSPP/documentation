---
orphan: true
---

# G2P Portal Auth

The `g2p_portal_auth` module in OpenSPP provides essential controls for managing which external authentication providers are available for different user portals. It allows administrators to precisely define which OpenID Connect (OIDC) services can be used by beneficiaries accessing the Self-Service Portal and by program staff or service providers using the Service Provider Portal.

## Purpose

This module ensures secure and differentiated access to OpenSPP's portals by enabling precise control over authentication sources. Its key capabilities include:

*   **Segmented Portal Access**: Designates specific OIDC providers for use with the Self-Service Portal, ensuring beneficiaries can only use approved login methods.
*   **Service Provider Authentication**: Controls which OIDC providers are available for program staff and service providers to access the Service Provider Portal, maintaining operational security.
*   **Enhanced Security Management**: Centralizes the management of external authentication options, reducing potential vulnerabilities and ensuring compliance with access policies.
*   **Streamlined User Experience**: Presents only relevant and authorized login options to users based on the portal they are accessing, simplifying the login process.
*   **Flexible Integration**: Adapts to various organizational security needs by allowing administrators to enable or disable OIDC providers for specific portals as required.

This module is crucial for maintaining a secure and intuitive login environment, ensuring that different user groups access the system through appropriate and trusted channels.

## Dependencies and Integration

The `g2p_portal_auth` module builds upon the foundational [G2P Auth OIDC](g2p_auth_oidc) module, which handles the core OpenID Connect authentication processes. While `g2p_auth_oidc` manages the technical aspects of integrating with OIDC providers, `g2p_portal_auth` extends this by adding critical flags to the `auth.oauth.provider` model.

These flags, `g2p_self_service_allowed` and `g2p_service_provider_allowed`, enable other portal-specific modules to query and display only the relevant OIDC login options. This ensures that the Self-Service Portal for beneficiaries and the Service Provider Portal for staff present a tailored and secure authentication experience.

## Additional Functionality

### Self-Service Portal Authentication Control

Administrators can explicitly enable or disable any configured OIDC provider for use with the Self-Service Portal. This allows programs to offer specific, trusted login options to beneficiaries, such as national ID systems or designated public services, ensuring controlled access to personal information and program benefits.

### Service Provider Portal Authentication Control

Similarly, the module allows administrators to select which OIDC providers are available for program staff and external service providers. This ensures that internal users and partners log in through appropriate, often institution-specific, identity providers, maintaining the integrity and security of program operations.

### Dynamic Portal Callback Management

The module supports dynamic management of OIDC callback URLs, which are essential for directing users back to the correct portal after successful authentication. This flexibility ensures that OpenSPP can seamlessly integrate with various OIDC providers across different deployment environments for both the Self-Service and Service Provider portals.

## Conclusion

The `g2p_portal_auth` module is fundamental for securely managing and differentiating access to OpenSPP's Self-Service and Service Provider portals, ensuring that beneficiaries and program staff utilize appropriate and authorized external authentication channels.
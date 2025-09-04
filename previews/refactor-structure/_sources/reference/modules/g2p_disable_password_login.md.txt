---
orphan: true
---

# G2P Disable Password Login

The `G2P Disable Password Login` module significantly enhances OpenSPP's security and streamlines user authentication by removing the traditional password-based login option. It enforces the use of pre-configured external identity providers (IdPs) for all user access to the platform.

## Purpose

This module ensures that all users authenticate through pre-configured external identity providers (IdPs), such as OAuth or Single Sign-On (SSO) systems, rather than OpenSPP's internal password mechanism.

*   **Enforces External Authentication:** Mandates that users log in exclusively via configured OAuth/SSO providers, eliminating the need for local password management within OpenSPP.
*   **Streamlines User Experience:** Simplifies the login process by presenting only external authentication options, reducing user confusion and ensuring a consistent login flow.
*   **Enhances Security Posture:** Prevents vulnerabilities associated with local password storage and brute-force attacks, centralizing authentication security to the external IdP.
*   **Facilitates Compliance:** Supports organizational security policies that require multi-factor authentication or integration with existing corporate or national identity systems.
*   **Reduces Administrative Overhead:** Minimizes the need for password resets and management within OpenSPP, shifting this responsibility to the external identity provider.

## Dependencies and Integration

This module relies on the `auth_oauth` module, which provides the foundational capabilities for integrating OpenSPP with various OAuth 2.0 and OpenID Connect identity providers. The `G2P Disable Password Login` module extends `auth_oauth` by actively modifying the user interface to remove the default password login fields. This ensures that once `auth_oauth` is configured, all login attempts are directed exclusively through the external authentication mechanisms, thereby enforcing a secure, centralized authentication strategy across the OpenSPP platform.

## Additional Functionality

### Enforced External Login
This feature ensures that all users, without exception, must authenticate through a pre-configured external identity provider. When users navigate to the OpenSPP login page, they will only see options to log in via services like Google, national ID systems, or other configured OAuth providers, rather than inputting a username and password directly into OpenSPP. This capability is critical for organizations that require centralized identity management and robust external security protocols.

### Simplified Login Interface
The module modifies the standard OpenSPP login screen to remove the username and password input fields. This creates a cleaner, less cluttered interface, guiding users directly to the available external login buttons. By eliminating the password field, it reduces potential user confusion and reinforces the organization's commitment to using secure, external authentication methods.

### Enhanced Security and Compliance
By disabling local password login, the module significantly strengthens OpenSPP's security. It mitigates risks associated with weak passwords, password reuse, and brute-force attacks against the OpenSPP system itself. This approach helps organizations comply with stringent security policies and regulatory requirements that often mandate the use of centralized, multi-factor, or enterprise-grade identity management solutions.

## Conclusion

The `G2P Disable Password Login` module is essential for OpenSPP deployments seeking to enhance security, streamline user authentication, and enforce external identity management for a more robust and compliant platform.
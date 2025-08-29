---
orphan: true
---

# G2P Openid Vci Rest Api

The `g2p_openid_vci_rest_api` module extends OpenSPP's capabilities by providing a standardized RESTful API for Verifiable Credential Issuance (VCI). This module enables external systems, such as digital wallets or other applications, to securely request and receive Verifiable Credentials (VCs) from OpenSPP.

## Purpose

This module establishes the necessary API layer for OpenSPP to act as a secure and interoperable issuer of digital credentials. It allows OpenSPP to participate in modern digital identity ecosystems by making its VCI capabilities externally accessible.

*   **Exposes Standardized VCI Endpoints:** Creates secure, industry-standard REST API endpoints that external applications can use to interact with OpenSPP's credential issuance services.
*   **Enables Programmatic Credential Requests:** Allows external systems, such as mobile wallets or other digital identity platforms, to programmatically initiate requests for Verifiable Credentials from OpenSPP.
*   **Facilitates OpenID4VP Integration:** Provides the API interface required to support OpenID Connect for Verifiable Presentations (OpenID4VP) flows, ensuring secure authorization and token exchange during credential issuance.
*   **Dynamic API Management:** Integrates with OpenSPP's API management framework, allowing administrators to activate and configure the VCI API endpoints directly within the OpenSPP system.
*   **Extends OpenSPP's Reach:** Transforms OpenSPP into an active participant in digital identity initiatives by making its rich data and credentialing logic available to external, decentralized identity applications.

## Dependencies and Integration

This module is a crucial integration layer, building upon and exposing the functionality of other core OpenSPP modules.

It primarily depends on the [G2P OpenID VCI](g2p_openid_vci) module, which contains the core logic for managing issuers and generating Verifiable Credentials. The `g2p_openid_vci_rest_api` module serves as the public interface for these underlying VCI services.

The module also integrates with `fastapi`, which provides the robust and performant web framework for building the REST API endpoints. Additionally, it leverages `extendable_fastapi` to allow for dynamic registration and management of these API endpoints within the OpenSPP administrative interface, ensuring flexibility and easy configuration.

## Additional Functionality

### Standardized API Endpoints for VCI

This module establishes secure, standardized REST API endpoints that conform to industry best practices for Verifiable Credential Issuance. These endpoints enable external applications, such as mobile wallets or other digital identity systems, to programmatically interact with OpenSPP to request and receive digital credentials. This ensures interoperability and secure communication with a wide range of external services.

### Seamless Integration with OpenID4VP Flows

The module provides the necessary API interface to support OpenID Connect for Verifiable Presentations (OpenID4VP) flows. This is critical for modern digital identity ecosystems, ensuring that the credential issuance process adheres to widely accepted standards for authorization, token exchange, and secure delivery of credentials. It handles the API-level interactions required for these secure identity flows.

### Configurable API Management

Leveraging OpenSPP's `fastapi` integration, the module allows administrators to enable and manage the VCI API endpoints directly within the system. This provides the flexibility to activate the VCI service, define its public-facing behavior, and integrate it seamlessly into the broader OpenSPP ecosystem without requiring code changes. Administrators can specify the application type as "VCI Endpoint" to activate the necessary routers.

### Exposing Core VCI Capabilities

By providing a programmatic interface, this API module makes OpenSPP's robust issuer management, credential definition, and secure signing features accessible to external digital identity initiatives. It allows the rich functionality of the underlying [G2P OpenID VCI](g2p_openid_vci) module to be consumed by external applications, enabling OpenSPP to serve as a central component in a decentralized identity infrastructure.

## Conclusion

The `g2p_openid_vci_rest_api` module is essential for enabling OpenSPP to securely and programmatically issue Verifiable Credentials to external systems, significantly enhancing its role in modern digital identity ecosystems.
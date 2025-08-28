# G2P Encryption Rest Api

The `g2p_encryption_rest_api` module provides a secure REST API interface to OpenSPP's core encryption and cryptographic services. It allows external systems and applications to securely interact with and leverage OpenSPP's underlying encryption capabilities.

## Purpose

This module accomplishes the crucial task of exposing OpenSPP's cryptographic functionalities to the outside world in a secure and standardized manner.

*   **Exposes Encryption Services**: Provides a dedicated, secure REST API endpoint for cryptographic operations, enabling external systems to utilize OpenSPP's encryption and digital signature services.
*   **Facilitates Secure Data Exchange**: Allows integrated applications to encrypt, decrypt, sign, and verify data using OpenSPP's configured encryption providers, ensuring data confidentiality and integrity during exchange.
*   **Supports Standard Security Practices**: Implements industry-standard `/.well-known` endpoints, which are essential for public security configurations such as JSON Web Key Set (JWKS) discovery.
*   **Enables Interoperability**: Ensures that OpenSPP can securely integrate with other platforms requiring cryptographic operations, for example, verifying identity tokens or securing data transfers.
*   **Manages API Endpoint Security**: Establishes a specific 'security' application endpoint within OpenSPP's API framework, ensuring that all encryption-related API calls are routed and managed securely.

## Dependencies and Integration

The `g2p_encryption_rest_api` module builds upon and extends other foundational OpenSPP components.

This module directly depends on the [G2P Encryption](g2p_encryption) module, which provides the core framework for managing encryption providers and defining generic encryption methods. The `g2p_encryption_rest_api` module then makes these underlying cryptographic services, such as JWT signing/verification and JWKS retrieval, accessible via a robust REST API.

It integrates with OpenSPP's `fastapi.endpoint` management system by adding a specific "Security Endpoint" application type. This ensures that the cryptographic API routes are properly registered, managed, and secured within the platform's overall API infrastructure, allowing for consistent control and discoverability of these vital services.

## Additional Functionality

### Dedicated Security Endpoint Management
This module establishes a specific 'security' application type for API endpoints within OpenSPP's framework. This segregation ensures that all API calls related to encryption and cryptographic services are routed and managed through a dedicated, secure channel, maintaining strict control over access to sensitive operations.

### Standard `/.well-known` Endpoint Support
The module implements support for the industry-standard `/.well-known` endpoint. This is critical for security and interoperability, as it allows external systems to automatically discover and retrieve public security configurations, such as JSON Web Key Sets (JWKS), which are essential for verifying digital signatures on tokens like JWTs issued by OpenSPP.

### External Access to Cryptographic Operations
By exposing the `g2p_encryption` module's capabilities via a REST API, this module enables authorized external applications to programmatically perform cryptographic operations. This includes capabilities like verifying JSON Web Tokens (JWTs) for authentication or retrieving public keys for secure communication, significantly enhancing OpenSPP's ability to integrate securely with external services.

### API Endpoint Synchronization
The module provides functionality to synchronize the exposed API endpoints with OpenSPP's registry. This ensures that any changes or updates to the security API endpoints are consistently reflected across the system, maintaining the integrity and discoverability of the cryptographic services.

## Conclusion

The `g2p_encryption_rest_api` module is essential for securely exposing OpenSPP's core cryptographic capabilities to external systems, facilitating secure data exchange and robust integration.
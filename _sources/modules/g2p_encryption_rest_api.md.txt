# G2P Encryption: Rest API Module

This document provides an overview of the `g2p_encryption_rest_api` module within the OpenSPP ecosystem.

### Overview

The `g2p_encryption_rest_api` module extends the functionality provided by the [g2p_encryption](./g2p_encryption.md) module by exposing its encryption and security functionalities through a RESTful API. This allows external systems and applications to securely interact with OpenSPP's encryption mechanisms.

### Purpose

The primary purpose of this module is to facilitate secure data exchange and integration with external systems that require access to OpenSPP's encryption capabilities. This could include:

- **Mobile Applications:** Allowing mobile apps used by beneficiaries or field agents to securely encrypt and decrypt data.
- **Third-party Systems:** Enabling integration with other government or partner systems that require secure communication channels.
- **Data Analytics:** Providing a secure way to extract encrypted data for analysis and reporting purposes.

### Functionality

The module exposes a set of REST endpoints under the `/api/v1/security/` path. These endpoints allow authorized clients to:

- **Encrypt Data:** Encrypt data payloads using configured encryption providers.
- **Decrypt Data:** Decrypt data previously encrypted by OpenSPP.
- **Generate JWT Tokens:** Generate JSON Web Tokens (JWTs) signed with OpenSPP's private key for secure authentication and authorization.
- **Verify JWT Tokens:** Verify the authenticity and integrity of JWTs received from external systems.
- **Retrieve JWKS:** Access OpenSPP's JSON Web Key Set (JWKS) for verifying JWT signatures.

### Integration

The `g2p_encryption_rest_api` module seamlessly integrates with the [g2p_encryption](./g2p_encryption.md) module, leveraging its existing encryption provider framework and configurations. It utilizes Odoo's `base_rest` module to expose the REST API endpoints.

### Dependencies

- [g2p_encryption](./g2p_encryption.md): Provides the core encryption functionalities and provider management.
- `base_rest`: Offers the framework for building RESTful APIs within Odoo.

### Security

The module inherits the security mechanisms provided by Odoo's `base_rest` module, including user authentication and authorization. Access to the API endpoints can be restricted based on user roles and permissions. Additionally, the module utilizes the encryption providers configured in the [g2p_encryption](./g2p_encryption.md) module to ensure secure data transmission.

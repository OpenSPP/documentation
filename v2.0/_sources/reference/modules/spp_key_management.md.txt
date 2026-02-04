---
openspp:
  doc_status: draft
---

# Key Management

**Module:** `spp_key_management`

## Overview

The OpenSPP Key Management module provides centralized cryptographic key management with pluggable providers. It supports multiple key storage backends from simple configuration-based keys for development to enterprise-grade solutions like HashiCorp Vault or cloud KMS services for production environments.

## Purpose

This module is designed to:

- **Centralize key management:** Provide a single interface for managing encryption keys across the platform
- **Support multiple providers:** Enable different key storage strategies based on deployment requirements
- **Enable key rotation:** Support versioned keys with rotation capabilities for security compliance
- **Protect sensitive data:** Manage data encryption keys (DEKs) used for encrypting PII and other sensitive information

## Module Dependencies

| Dependency       | Description                |
| ---------------- | -------------------------- |
| **base**         | Core Odoo framework        |
| **spp_security** | OpenSPP security framework |

### External Python Dependencies

| Package          | Description                          |
| ---------------- | ------------------------------------ |
| **cryptography** | Cryptographic primitives and recipes |

## Key Features

### Key Provider Architecture

The module implements a pluggable provider architecture with the following supported backends:

| Provider                           | Use Case      | Key Features                 |
| ---------------------------------- | ------------- | ---------------------------- |
| **Configuration File**             | Development   | Keys stored in `odoo.conf`   |
| **Database (Envelope Encryption)** | Production    | DEKs encrypted by master KEK |
| **HashiCorp Vault**                | Enterprise    | External secrets management  |
| **AWS KMS**                        | Cloud (AWS)   | AWS Key Management Service   |
| **Google Cloud KMS**               | Cloud (GCP)   | Google Cloud key management  |
| **Azure Key Vault**                | Cloud (Azure) | Azure secrets management     |

### Encryption Key Storage

The `spp.encryption.key` model stores encrypted data encryption keys with:

| Field         | Description                                  |
| ------------- | -------------------------------------------- |
| Key ID        | Unique identifier (e.g., 'pii', 'financial') |
| Version       | Version number for key rotation              |
| Is Current    | Marks the active version for encryption      |
| Encrypted Key | Base64-encoded encrypted key material        |
| Algorithm     | Encryption algorithm (default: AES-256-GCM)  |
| Purpose       | Description of key usage                     |
| Expires Date  | Optional expiration date                     |

### Key Versioning

The module supports key versioning for rotation:

- Each key can have multiple versions
- Only one version is marked as "current" for new encryptions
- Old versions remain available for decrypting existing data
- Keys cannot be deleted (only archived by clearing `is_current`)

### Key Purposes

Key purposes define the intended use for keys:

| Purpose Code  | Typical Use                         |
| ------------- | ----------------------------------- |
| **pii**       | Personally identifiable information |
| **financial** | Financial data and bank details     |
| **medical**   | Health-related information          |

### Provider Registry

The `spp.key.provider.registry` model allows configuring which provider handles which key purposes:

| Field             | Description                           |
| ----------------- | ------------------------------------- |
| Name              | Provider configuration name           |
| Provider Type     | Backend type selection                |
| Purposes          | Key purposes this provider handles    |
| Is Default        | Use when no specific provider matches |
| Connection Status | Current connection state              |

## Integration

### With Data Encryption

Other modules use the key management API to:

1. Request encryption keys by purpose
2. Encrypt sensitive data fields
3. Decrypt data for authorized access
4. Handle key rotation transparently

### Provider Selection Flow

```
1. Module requests key for purpose (e.g., 'pii')
2. Registry checks for provider configured for that purpose
3. If found, use that provider
4. Otherwise, use the default provider
5. If no default, fall back to database provider
```

## Configuration

### Setting Up Database Provider

For production deployments using envelope encryption:

1. Configure master key in system parameters or environment
2. Create encryption keys through the UI or API
3. Keys are automatically encrypted with the master key

### Testing Provider Connection

Use the "Test Connection" action on the provider registry to verify:

- Provider configuration is correct
- Backend service is accessible
- Authentication is working

## Security Considerations

- Master keys should be stored securely (environment variables, secrets manager)
- Key material is never logged or exposed in error messages
- Access to key management is restricted to system administrators
- Connection status helps identify configuration issues

## Technical Details

### Abstract Provider Interface

All providers implement the `spp.key.provider` abstract model with:

| Method                          | Description                          |
| ------------------------------- | ------------------------------------ |
| `get_data_key(key_id, version)` | Retrieve encryption key material     |
| `get_index_salt(purpose)`       | Get salt for blind index computation |
| `rotate_key(key_id)`            | Create new key version               |
| `list_key_versions(key_id)`     | List available versions              |
| `test_connection()`             | Verify backend connectivity          |

### Signature Utilities

The module includes utilities for digital signatures in `utils/signature.py`, supporting:

- Key pair generation
- Message signing
- Signature verification

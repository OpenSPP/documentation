# G2P Registry: Encryption Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_registry_encryption](g2p_registry_encryption) module adds an encryption layer to the OpenSPP registry system. It allows sensitive registry data to be stored securely, enhancing the system's overall privacy and security. This module builds upon the functionality provided by the [g2p_encryption](g2p_encryption), [g2p_registry_base](g2p_registry_base) and [g2p_registry_individual](g2p_registry_individual) modules.

## Features

- **Selective Encryption:**  Encrypts specific fields of the `res.partner` model that contain sensitive registrant information like name, address, and birth place.
- **Configurable Encryption Provider:**  Allows administrators to select and configure the desired encryption provider from the available options within OpenSPP.
- **On-the-fly Encryption and Decryption:**  Transparently encrypts data upon saving a record and decrypts it when retrieved, ensuring a seamless user experience.
- **Granular Control:**  Provides options to enable or disable encryption and decryption through system configuration settings.

## Integration

- **[g2p_encryption](g2p_encryption):**  Utilizes the encryption providers and functionalities provided by this module to perform the actual encryption and decryption operations.
- **[g2p_registry_base](g2p_registry_base) and [g2p_registry_individual](g2p_registry_individual):** Extends the existing registry data models and views to accommodate the encryption features.

## Configuration

The module can be configured through the OpenSPP settings interface:

1. **Encryption Provider:** Choose the preferred encryption provider from the list of configured providers.
2. **Enable Encryption:** Toggle the "Encrypt Registry fields" option to enable encryption for the specified fields.
3. **Enable Decryption (Caution):** This option allows decryption of registry fields. Use with caution, as enabling it might expose sensitive data. It is generally recommended to keep this disabled unless explicitly required.

## Security Considerations

While this module enhances data security, it is crucial to remember that the overall system's security relies on several factors:

- **Encryption Key Management:**  Securely store and manage the encryption keys used by the chosen provider.
- **Access Control:**  Implement strict access control measures to prevent unauthorized access to sensitive data and configuration settings.
- **Regular Security Audits:**  Conduct periodic security audits and updates to mitigate potential vulnerabilities.

By carefully configuring and integrating this module into the OpenSPP ecosystem, implementers can significantly improve the protection of sensitive registry data. 

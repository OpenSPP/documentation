# G2P Registry Encryption

The G2P Registry Encryption module provides robust data protection for sensitive registrant information within OpenSPP. It secures personal data by encrypting specified fields in the registry, ensuring privacy and compliance with data protection standards.

## Purpose

This module enhances the security and privacy of registrant data by implementing field-level encryption. It allows OpenSPP to handle sensitive information responsibly, safeguarding beneficiaries' personal details.

Key capabilities include:

*   **Secure Sensitive Data**: Encrypts critical personal information, such as names, addresses, and birth details, directly within the registrant's profile.
*   **Configurable Encryption**: Enables administrators to define precisely which registry fields require encryption, offering flexibility to meet specific privacy policies.
*   **Data Obfuscation**: Replaces encrypted data with a generic placeholder in the database, preventing unauthorized viewing of raw sensitive information.
*   **Controlled Access**: Facilitates authorized decryption of sensitive data for legitimate operational needs, ensuring that data remains accessible only to approved personnel.
*   **Compliance Support**: Helps OpenSPP deployments adhere to data protection regulations by providing a mechanism for securing personal identifying information (PII).

This module is essential for protecting the privacy of individuals served by social protection programs, reducing the risk of data breaches, and building trust in the OpenSPP platform.

## Dependencies and Integration

The `g2p_registry_encryption` module integrates deeply with core OpenSPP registry components and leverages a foundational encryption framework.

*   **[G2P Encryption](g2p_encryption)**: This module relies on the `g2p_encryption` module to provide the underlying encryption services. It utilizes the defined encryption providers to perform actual data encryption and decryption operations, abstracting the cryptographic complexities.
*   **[G2P Registry Base](g2p_registry_base)**: As an extension of the base registry, this module integrates with the `res.partner` model, which is the foundation for all registrants. It adds fields to `res.partner` to store encrypted values and manage encryption status.
*   **[G2P Registry Individual](g2p_registry_individual)**: Building upon the individual registry, this module specifically targets the individual-specific data fields introduced by `g2p_registry_individual` (e.g., family name, given name, birth place) for encryption, ensuring comprehensive protection of individual profiles.

## Additional Functionality

The `g2p_registry_encryption` module offers several key features to manage and secure registrant data effectively:

### Configurable Field Encryption

Administrators can specify which fields within the registrant's profile should be encrypted. This includes common fields like `name`, `family_name`, `given_name`, `addl_name`, `display_name`, `address`, and `birth_place`. This flexibility allows organizations to tailor data protection to their specific requirements and local regulations.

### Data Masking and Placeholder Values

When a field is encrypted, its original value is replaced in the database with a configurable placeholder, such as "encrypted." This ensures that even if the database is accessed directly without proper authorization, sensitive information remains masked and unreadable, enhancing data security.

### Secure Data Handling

The module automatically encrypts specified data fields when new registrant records are created or existing ones are updated. It also manages the decryption process when authorized users access registrant information, ensuring that data is only exposed when explicitly permitted.

### Encryption Provider Selection

Through system configuration, users can select and manage the specific encryption provider used for registry data. This integration with the `g2p_encryption` module allows for the use of various robust encryption methods, enabling organizations to choose the most suitable security solution.

### Controlled Decryption Access

The system provides a mechanism to control whether sensitive registry data is decrypted for viewing. This can be configured at a system level, allowing organizations to implement strict policies on who can access unencrypted registrant details for operational purposes.

## Conclusion

The G2P Registry Encryption module is vital for OpenSPP, providing essential capabilities to encrypt and secure sensitive registrant data, thereby upholding privacy and facilitating compliance with data protection mandates.
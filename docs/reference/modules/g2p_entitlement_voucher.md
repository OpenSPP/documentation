# G2P Entitlement Voucher

The G2P Entitlement Voucher module extends OpenSPP's core G2P framework to enable the generation and management of secure, printable vouchers for social protection program entitlements. This module allows programs to deliver benefits through a voucher system, integrating seamlessly with existing entitlement and payment processes.

## Purpose

This module streamlines the delivery of benefits through a robust voucher system by:

*   **Automating Voucher Generation:** Automatically creates unique vouchers for approved program entitlements, reducing manual effort and potential errors.
*   **Ensuring Secure Benefit Delivery:** Generates vouchers with integrated QR codes that can be encrypted, providing a secure and traceable method for beneficiaries to redeem benefits.
*   **Enabling Flexible Voucher Design:** Allows administrators to configure custom voucher templates, ensuring they meet specific program branding and information requirements.
*   **Streamlining Entitlement Workflows:** Integrates voucher generation directly into the entitlement approval process, ensuring a smooth and efficient workflow from eligibility to benefit delivery.
*   **Providing Centralized Document Management:** Securely stores all generated voucher documents, making them easily accessible for printing, auditing, and record-keeping.

## Dependencies and Integration

The G2P Entitlement Voucher module is built upon and extends several core OpenSPP components:

*   **[G2P Programs](g2p_programs):** This module integrates directly with the G2P Programs module by providing a specific "Voucher" entitlement manager. Program administrators can select this manager type to enable voucher-based benefit delivery for their social protection programs, extending the core entitlement process.
*   **[G2P Payment Files](g2p_payment_files):** It leverages the advanced payment file configuration and generation capabilities of G2P Payment Files. This allows the module to define and render customizable voucher templates, including the embedding of QR codes, based on program-specific requirements.
*   **[G2P Encryption](g2p_encryption):** To ensure data security, the module utilizes the G2P Encryption module to encrypt sensitive information embedded within the QR codes on the vouchers. This protects beneficiary data and enhances the overall security of the benefit delivery process.

## Additional Functionality

### Voucher Management for Approved Entitlements

Once an entitlement is approved, program staff can easily manage its associated voucher.
*   Users can generate a new voucher document for an approved entitlement that does not yet have one.
*   For entitlements with an existing voucher, users can directly access and print the voucher document as needed.
*   These actions are accessible through dedicated buttons on the entitlement record, simplifying the user experience.

### Configurable Voucher Generation Settings

Administrators have granular control over how vouchers are generated for each program.
*   Programs can be configured to automatically generate vouchers as soon as entitlements are approved, streamlining the benefit delivery process.
*   Administrators define the voucher's layout and content by linking a specific "Payment File Configuration" from the [G2P Payment Files](g2p_payment_files) module. This configuration determines the template, data fields, and QR code details.
*   A "Document Storage Backend" is selected to specify where the generated voucher documents are securely stored, ensuring compliance and easy retrieval.
*   An "Encryption Provider" from the [G2P Encryption](g2p_encryption) module can be chosen to encrypt sensitive data within the voucher's QR codes, enhancing data privacy and security.

### Efficient Batch Processing for Vouchers

The module is designed to handle large volumes of entitlements efficiently.
*   Voucher generation processes entitlements in optimized batches, preventing system slowdowns when dealing with many beneficiaries.
*   For very large programs, voucher generation can be initiated as an asynchronous background job, allowing users to continue their work without interruption while the system processes the vouchers.

## Conclusion

The G2P Entitlement Voucher module significantly enhances OpenSPP's capacity for flexible benefit delivery by providing a secure, automated, and customizable system for generating and managing program vouchers. It ensures efficient and traceable distribution of benefits to beneficiaries within social protection programs.
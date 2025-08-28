# G2P Payment Files

The `g2p_payment_files` module in OpenSPP enables the generation, customization, and secure management of payment-related documents. This includes creating printable vouchers, digital payment instructions, or data files for beneficiaries based on their entitlements.

## Purpose

This module provides essential capabilities for programs requiring physical or digital payment instruments:

*   **Custom Payment File Design**: Allows users to define and customize templates for various payment documents, such as vouchers or payment instructions, in formats like PDF or CSV.
*   **Dynamic Data Integration**: Automatically populates generated files with relevant data from payments, beneficiaries, and program cycles, ensuring accuracy and personalization.
*   **Secure Code Embedding**: Generates and embeds secure QR codes or Code 128 barcodes into payment files, which can contain plain text, JSON data, or signed JSON Web Tokens (JWTs) for verification.
*   **Automated Document Storage**: Integrates with OpenSPP's document management system to securely store all generated payment files, ensuring an auditable trail.
*   **Flexible Output**: Supports generating individual files for each payment or consolidated files for entire payment batches, adapting to diverse program requirements.

## Dependencies and Integration

The `g2p_payment_files` module integrates closely with other core OpenSPP components to deliver its functionality:

*   **[G2P Programs](g2p_programs)**: This module extends the core payment processing framework of `g2p_programs` by providing the mechanism to output physical or digital payment instruments. It integrates with the `g2p.program.payment.manager` to enable file-based payment methods.
*   **[G2P Program Documents](g2p_program_documents)**: It leverages the configured document storage backends from `g2p_program_documents` to securely save all generated payment files, linking them directly to the relevant program and payments.
*   **[G2P Encryption](g2p_encryption)**: For enhanced security, `g2p_payment_files` utilizes `g2p_encryption` to sign JSON Web Tokens (JWTs) when they are embedded in QR codes, ensuring the integrity and authenticity of the data.
*   **Mail**: The module uses Odoo's mail rendering capabilities (specifically `mail.render.mixin`) to process QWeb templates, allowing dynamic content generation within payment files.

## Additional Functionality

### Customizable Payment File Templates
Users can design various payment file templates, which serve as the blueprint for documents like payment vouchers or bulk data files. These templates support both PDF for printable documents and CSV for data export. Templates are dynamic, pulling specific data fields from payment, batch, and beneficiary records to ensure relevant and accurate information is displayed.

### Integrated QR Code and Barcode Generation
The module offers robust functionality for embedding scannable codes into payment files. Users can configure multiple QR codes or Code 128 barcodes per file, defining their content type (plain string, JSON, or secure JSON Web Token). QR codes can be customized with parameters such as error correction level, box size, and border, ensuring they are readable and meet specific program requirements.

### Flexible File Generation Logic
Programs have the flexibility to choose how payment files are generated. The module allows for configuration at the batch tag level to either generate a separate, unique file for each individual payment or a single, consolidated file for an entire payment batch. This ensures that the output format aligns with the program's disbursement and reconciliation processes.

### Secure Data Embedding with Encryption
When using JSON Web Tokens (JWTs) within QR codes, the module integrates with a designated encryption provider. This ensures that the data embedded in the QR code is cryptographically signed, providing a layer of security and allowing recipients or verifying parties to confirm the data's origin and integrity.

## Conclusion

The `g2p_payment_files` module is crucial for OpenSPP programs, enabling the flexible, secure, and auditable generation of payment-related documents. It streamlines the creation of physical or digital payment instruments, supporting efficient and transparent benefit disbursement.
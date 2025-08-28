# G2P Formio

The `g2p_formio` module integrates dynamic form building capabilities into OpenSPP's G2P programs, enabling flexible data collection, customizable application processes, and enhanced self-service options for beneficiaries.

## Purpose

The `g2p_formio` module provides a powerful framework for:

*   **Creating Dynamic Program Forms**: Design and manage custom digital forms for various program needs, such as applications, registrations, or surveys, without requiring technical development.
*   **Associating Forms with G2P Programs**: Link specific forms directly to individual social protection programs, ensuring relevant and targeted data collection for each initiative.
*   **Enabling Self-Service Applications**: Empower beneficiaries to complete and submit program forms independently, reducing administrative burden and improving accessibility to social protection services.
*   **Managing Multiple Submissions**: Configure programs to allow beneficiaries to submit forms multiple times, which is useful for re-applications, periodic updates, or submissions for different program components.
*   **Streamlining Data Collection and Validation**: Leverage Formio's robust features to collect structured data efficiently and apply necessary validations directly within program workflows, ensuring data quality.

This module enhances the flexibility of OpenSPP programs by allowing administrators to quickly adapt data collection methods to evolving program requirements and improve the beneficiary application experience.

## Dependencies and Integration

The `g2p_formio` module extends core OpenSPP functionalities by integrating with key components:

*   **Formio**: This module relies on the core `formio` module, which provides the underlying drag-and-drop form builder interface and rendering engine. `g2p_formio` leverages Formio to create and manage the structure and behavior of all dynamic forms.
*   **G2P Programs**: `g2p_formio` directly integrates with the [G2P Programs](g2p_programs) module. It extends the `g2p.program` model, allowing program administrators to associate a specific Formio builder instance as the "Program Form" for any given social protection program. This link enables programs to utilize custom forms for their operations.
*   **Formio Storage Filestore**: This module depends on `formio_storage_filestore` to manage the secure storage of form submission data. It ensures that all data collected through the dynamic forms is reliably saved and accessible within OpenSPP.

This integration allows `g2p_formio` to serve as the primary mechanism for collecting beneficiary data through customizable forms within the context of defined G2P programs.

## Additional Functionality

### Program-Specific Form Assignment

Administrators can easily assign a unique application or registration form to each social protection program. Within the [G2P Programs](g2p_programs) module, a dedicated field allows users to select an existing Formio builder, which then serves as the official "Program Form" for that specific program. This ensures that each program collects precisely the data it requires, tailored to its unique eligibility and operational needs.

### Self-Service Portal Integration

The assigned Program Forms are designed to be readily available for use in self-service portals. This capability empowers beneficiaries to complete applications, update information, or submit other required data independently through a user-friendly interface. This reduces the administrative burden on program staff and provides a more accessible and convenient experience for beneficiaries.

### Multiple Form Submissions

For programs that require beneficiaries to submit forms more than once, the `g2p_formio` module provides a configurable option. Administrators can enable "Multiple Form Submission" for a program, allowing a beneficiary to submit the associated Program Form multiple times. This is particularly useful for scenarios like re-applications, periodic updates, or when a beneficiary needs to apply for different components within the same program.

### Dynamic Form Validation

Leveraging the underlying Formio engine, all forms created and linked through this module support comprehensive validation rules. Administrators can configure field-level validations, ensuring data accuracy and completeness directly at the point of entry. This includes required fields, data type checks, and custom validation logic, streamlining the data quality process for program applications.

## Conclusion

The `g2p_formio` module is crucial for OpenSPP, providing the flexibility to create, manage, and integrate dynamic, program-specific forms, thereby streamlining data collection and enhancing beneficiary self-service capabilities.
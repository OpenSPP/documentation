---
orphan: true
---

# G2P Registry: Individual

The `g2p_registry_individual` module is a core component of OpenSPP, designed to manage detailed profiles for individual registrants. It extends the foundational registrant data established by `G2P Registry Base` with essential demographic and personal information, enabling comprehensive record-keeping for social protection programs.

## Purpose

This module establishes and maintains accurate individual registrant profiles, which are critical for determining program eligibility and delivering benefits effectively. It provides the following key capabilities:

*   **Captures Core Demographics**: Records essential personal details such as date of birth, age, and gender for each individual registrant.
*   **Manages Flexible Naming Conventions**: Supports the capture of family names, given names, and additional names, automatically compiling a standardized full name.
*   **Calculates Age Automatically**: Determines and displays a registrant's current age based on their date of birth, simplifying age-based eligibility checks.
*   **Defines Gender Classifications**: Allows for the customization and management of gender types, ensuring the system accommodates diverse classifications.
*   **Ensures Data Accuracy**: Implements validations to prevent errors, such as entering future dates for birthdates, thereby maintaining data integrity.

This module ensures that program administrators have a complete and reliable individual profile for every participant, streamlining the process of enrollment, assessment, and service delivery.

## Dependencies and Integration

The `g2p_registry_individual` module seamlessly integrates with and extends several other OpenSPP and Odoo core modules to provide its functionality:

*   **Base (base)**: As a fundamental Odoo module, `base` provides the core framework and essential functionalities upon which all other modules, including this one, are built.
*   **Mail (mail)**: This module leverages `mail` for standard communication and notification features associated with registrant records, such as activity tracking and messaging.
*   **Contacts (contacts)**: `g2p_registry_individual` significantly extends the `res.partner` model from the `contacts` module. This allows individual registrants to be managed as detailed contact records within the broader Odoo system, inheriting common contact management features.
*   **G2P Registry Base (g2p_registry_base)**: This module builds directly upon the [G2P Registry Base](g2p_registry_base) module. It takes the foundational registrant structure and adds the specific fields and logic required for individual-level data, such as names, birthdates, and gender, enriching the core registrant profile.

## Additional Functionality

The `g2p_registry_individual` module offers specific features to manage individual registrant data:

### Individual Name Management

Users can record a registrant's family name, given name, and any additional names. The system automatically combines these components to generate a standardized full name for the registrant, ensuring consistency across records. This structured approach supports diverse naming conventions while maintaining a unified identifier.

### Demographic Profile and Age Calculation

This module captures the registrant's exact Date of Birth and provides an option for an Approximate Birthdate if the exact date is unknown. The system automatically calculates and displays the registrant's current age based on their recorded birthdate, which is vital for age-sensitive program eligibility. It also includes the ability to record the birth place and validates that birthdates are not set in the future.

### Customizable Gender Classification

The module includes a `Gender Type` model, allowing administrators to define and manage a list of gender classifications. This ensures that the system can accurately reflect and categorize the gender of individuals according to specific program or country requirements. Each gender type is uniquely identified by a code and value, and duplicates are prevented.

## Conclusion

The `g2p_registry_individual` module is essential for OpenSPP, providing the robust framework needed to accurately capture, manage, and utilize detailed personal information for every individual participating in social protection programs.
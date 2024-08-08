# G2P Registry: Individual Module 

This document outlines the functionality of the **G2P Registry: Individual** module within the OpenSPP ecosystem. Building upon the foundation provided by the **[G2P Registry: Base](g2p_registry_base)** module, this module focuses specifically on managing **individual registrant** data.

### Purpose

The **G2P Registry: Individual** module aims to:

* Extend the base registrant model to incorporate data fields specific to individuals.
* Provide a dedicated interface for managing and viewing individual registrant profiles. 
* Enhance data integrity through validation rules and constraints related to individual attributes.

### Module Dependencies and Integration

1. **[G2P Registry: Base](g2p_registry_base)**:  This module inherits from the core functionalities provided by the base module, including:
    * **Registrant Management**: Leverages the base registrant model, inheriting features for managing registration dates, disabling/enabling registrants, tags, IDs, phone numbers, and relationships.
    * **Districts**:  Utilizes the district management features to associate individuals with specific geographical locations.

2. **Contacts (res.partner)**:  Further extends the Odoo Contacts module by adding individual-specific fields to the registrant profile, including:
    * **Family Name, Given Name, Additional Name**:  Allows for structured recording of individual names.
    * **Birthdate**:  Stores the registrant's date of birth, with options to mark it as approximate. 
    * **Age**: Calculates and displays the registrant's age based on their birthdate.
    * **Gender**:  Provides a field for recording gender information.

### Additional Functionality

The module introduces:

* **Gender Types (gender.type)**:  A new model to define and manage various gender options. This list is dynamically used in the gender selection field for individuals, allowing for customization and inclusivity.
* **Dynamic Name Concatenation**:  Automatically generates the full name of the individual in the 'name' field based on the entered family name, given name, and additional name, ensuring consistency in display. 
* **Age Calculation and Validation**:  Calculates the age of the individual based on their birthdate and includes validation to ensure the entered age is a valid number.
* **Birthdate Validation**:  Restricts the selection of future dates for the birthdate field. 

### Conclusion

The **G2P Registry: Individual** module enhances the OpenSPP platform by providing a dedicated and feature-rich system for managing individual registrant data. By extending the base registry functionality and integrating seamlessly with Odoo's Contacts module, it ensures comprehensive and efficient handling of individual profiles within social protection programs and farmer registries. 

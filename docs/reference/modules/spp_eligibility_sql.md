---
orphan: true
---

# OpenSPP Eligibility Sql

The OpenSPP Eligibility Sql module enables program administrators to define and manage complex program eligibility criteria using custom SQL queries. This provides a highly flexible and automated mechanism for identifying and enrolling beneficiaries within OpenSPP programs.

## Purpose

This module significantly enhances OpenSPP's ability to manage social protection programs by:

*   **Customizing Eligibility Rules**: Allows administrators to define precise eligibility rules using SQL, accommodating unique and evolving program requirements without requiring code modifications.
*   **Automating Beneficiary Identification**: Automatically identifies registrants who meet the defined SQL-based criteria, streamlining the process of populating program beneficiary lists.
*   **Ensuring Data-Driven Enrollment**: Leverages the full power of the underlying database to evaluate eligibility against various data points, ensuring accurate and consistent enrollment.
*   **Facilitating Dynamic Program Adaptation**: Provides the agility to modify eligibility conditions as program policies change, simply by updating the SQL query.
*   **Integrating with Program Management**: Seamlessly integrates with program creation and cycle management, allowing for the direct application of SQL-based eligibility during program setup and ongoing operations.

## Dependencies and Integration

The 'spp_eligibility_sql' module integrates with several core OpenSPP components to deliver its functionality:

*   **[G2P Registry Base](g2p_registry_base)**: This module relies on the foundational registrant data managed by the G2P Registry Base. It queries the `res.partner` model to identify individuals or groups eligible for programs, accessing their demographic and registration details.
*   **[G2P Programs](g2p_programs)**: The module extends the core program management capabilities of G2P Programs. It adds 'SQL-based Eligibility' as a selectable option within the eligibility manager, allowing programs to utilize custom SQL for beneficiary determination.
*   **[OpenSPP Programs](spp_programs)**: Building upon G2P Programs, this module provides a dedicated function to create new OpenSPP programs directly with an associated SQL eligibility query, alongside other program parameters like entitlement types (e.g., cash or in-kind).

## Additional Functionality

The 'spp_eligibility_sql' module offers several key features for defining and managing program eligibility:

### SQL Query Definition and Management

Administrators can directly input custom SQL queries into the system to define eligibility criteria. The module tracks the status of these queries, marking them as 'Needs Re-checking' whenever modifications are made, ensuring that validation is always up-to-date. For security, the system prevents the execution of data manipulation language (DML) commands like `INSERT`, `UPDATE`, or `DELETE` within eligibility queries.

### Query Validation and Testing

A dedicated "Test Query" feature allows users to validate the syntax and expected output of their SQL queries. Upon validation, the system provides immediate feedback on the query's status (e.g., 'Valid', 'Invalid', 'Needs Re-checking') and any associated error messages. It also displays the number of registrants the query identifies, helping administrators confirm their eligibility logic before enrollment.

```{note}
For a query to be considered valid for eligibility, it must return the `id` field from the `res_partner` model, representing the unique identifier of each registrant.
```

### Automated Beneficiary Identification and Enrollment

Once a SQL query is validated, the module can execute it to identify all eligible registrants. These identified registrants can then be automatically imported into the program as beneficiaries. The system efficiently handles large volumes of registrants, processing imports asynchronously to maintain system performance. This automation significantly reduces manual effort and potential errors in beneficiary selection.

### Program Creation with SQL Eligibility

The module allows for the direct creation of new programs with SQL-based eligibility. During program setup, administrators can specify the custom SQL query along with other program details like its name, target type (individual or group), and entitlement kind. This streamlines the setup of complex programs that require highly specific eligibility criteria from the outset.

## Conclusion

The OpenSPP Eligibility Sql module is a powerful tool that provides unparalleled flexibility for defining and automating beneficiary eligibility, making it an essential component for managing diverse social protection programs within OpenSPP.
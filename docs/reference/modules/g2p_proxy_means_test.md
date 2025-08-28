# G2P Proxy Means Test

The G2P Proxy Means Test module provides OpenSPP with a robust, configurable, and automated mechanism for objective eligibility assessment in social protection programs. It allows administrators to define and apply a quantifiable scoring system to evaluate program applicants based on their collected data.

## Purpose

The G2P Proxy Means Test module automates the calculation of a quantifiable score for program applicants based on predefined criteria, streamlining eligibility assessment for social protection programs. This module allows program administrators to define custom formulas, assign weights to various data points, and automatically calculate a PMT score for each registrant. It ensures a consistent and objective method for determining who qualifies for program benefits, reducing manual review and potential biases.

Key capabilities include:

*   **Customizable Eligibility Formulas**: Define specific criteria and their relative importance to create tailored eligibility assessments for each program.
*   **Automated Score Calculation**: Automatically compute a PMT score for each applicant based on their submitted data, reducing manual effort and potential errors.
*   **Dynamic Score Updates**: Ensure PMT scores remain current by automatically recalculating them when relevant registrant information or program parameters change.
*   **Program-Specific Activation**: Enable or disable the Proxy Means Test feature independently for each social protection program, offering flexibility in program design.
*   **Tracking Latest Eligibility**: Maintain an up-to-date record of a registrant's most recent PMT score, crucial for ongoing eligibility monitoring or multiple program cycles.

## Dependencies and Integration

This module seamlessly integrates with other core OpenSPP components to extend program management and registrant information capabilities.

*   **{ref}`g2p_programs`**: This module extends the core G2P Program functionality, allowing program managers to activate and customize the Proxy Means Test for individual social protection programs. It adds options to enable PMT and define the specific parameters used for scoring.
*   **{ref}`g2p_program_registrant_info`**: The module builds upon `g2p_program_registrant_info` by adding fields to store and compute the `pmt_score` and `latest_pmt_score` for each registrant's application record. It leverages the data collected through this module to perform the score calculations.
*   **Data Integrity**: The module ensures the integrity of PMT configurations by automatically adapting to changes in underlying data fields. If a field used in a PMT calculation is removed from the system, the corresponding PMT parameter is automatically de-linked or removed to prevent errors.

## Additional Functionality

### Configurable PMT Parameters

Program managers define which numeric fields from a registrant's application (e.g., household income, number of dependents, housing type) contribute to the PMT score. Each selected field is assigned a weightage to reflect its importance, allowing tailored eligibility criteria for diverse programs. For example, a field like 'Monthly Income' could have a negative weightage, while 'Number of Dependents' could have a positive weightage, reflecting their impact on vulnerability.

### Automated PMT Score Calculation

Once configured, the module automatically computes a PMT score for every registrant's application. This score updates dynamically if any underlying registrant data or PMT parameters change, ensuring assessments are always current. This automation significantly reduces the administrative burden of eligibility determination.

### Program-Specific PMT Activation

The PMT feature can be enabled or disabled independently for each social protection program. This flexibility allows administrators to apply PMT only where appropriate, supporting a range of program designs and eligibility models without imposing a single assessment method across all programs.

### Tracking Latest Eligibility Scores

For programs with ongoing eligibility reviews or multiple application periods, the system automatically tracks and displays the most recent PMT score for each registrant. This provides program staff with an up-to-date eligibility snapshot without manual recalculation, facilitating continuous monitoring and reassessment.

### Ensuring PMT Configuration Integrity

The module maintains the integrity of PMT configurations by automatically adapting to changes in underlying data fields. If a data field used in a PMT calculation is no longer available in the system, the corresponding PMT parameter is automatically de-linked or removed, preventing errors and ensuring data consistency.

## Conclusion

The G2P Proxy Means Test module provides OpenSPP with a robust, configurable, and automated mechanism for objective eligibility assessment, enhancing fairness and efficiency in social protection program delivery.
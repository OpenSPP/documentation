# g2p_program_autoenrol Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module extends the functionality of the [g2p_programs](g2p_programs) module to enable automatic enrollment of registrants into social protection programs based on predefined criteria. This feature simplifies program management by automating the enrollment process for eligible individuals.

### Purpose

The main purpose of the `g2p_program_autoenrol` module is to streamline and automate the process of enrolling beneficiaries into social protection programs. It achieves this by providing the following capabilities:

- **Automatic Enrollment:** When a new registrant is created in the system, the module automatically checks for programs configured with auto-enrollment rules.
- **Eligibility Criteria:** Program administrators can define specific eligibility criteria using Odoo's domain syntax. This allows them to target specific demographics or groups based on pre-defined attributes stored in registrant profiles.
- **Program-Specific Enrollment:** Auto-enrollment can be enabled or disabled on a per-program basis, providing flexibility in managing different types of programs.
- **Optional Removal of Ineligible Registrants:**  Administrators have the option to automatically remove registrants from a program's membership list if they do not meet the defined eligibility criteria. This ensures that only eligible individuals are considered beneficiaries.

### Functionality

The module introduces the following key features:

- **New Fields in Program Configuration:**
    - **Auto Enrol Partners:** A boolean field to enable or disable auto-enrollment for the specific program.
    - **Filter for Partners:** A text field utilizing Odoo's domain syntax to define the criteria for automatic enrollment. This allows administrators to specify which registrants should be automatically enrolled based on their profile attributes.
    - **Keep only Eligible Partners:**  A boolean field that, when checked, will automatically remove registrants from the program's membership if they do not meet the defined eligibility criteria.

- **Automatic Enrollment upon Registrant Creation:**
    - When a new registrant is created in the system, the module automatically checks for programs that have auto-enrollment enabled.
    - If the registrant meets the defined criteria for a specific program, they are automatically enrolled.
    - An automatic check for eligibility is performed, and if the  "Keep only Eligible Partners" option is activated, ineligible registrants are removed from the program membership.

- **Impact on Program Statistics:**
    - The module ensures that program statistics, such as the count of eligible and total beneficiaries, are updated dynamically to reflect the results of the automatic enrollment process.

### Integration

The [g2p_program_autoenrol](g2p_program_autoenrol) module works seamlessly with the [g2p_programs](g2p_programs) module. It leverages the existing program and registrant data structures and extends their functionality. 

### Benefits

- **Reduced Administrative Burden:** Automating the enrollment process significantly reduces the manual effort required by program administrators.
- **Improved Accuracy:** By automating enrollment based on pre-defined criteria, the module minimizes the risk of human error and ensures consistent application of eligibility rules.
- **Enhanced Targeting:** The ability to define specific eligibility criteria allows programs to effectively target the intended beneficiaries, maximizing impact and resource utilization.
- **Increased Efficiency:**  Automatic enrollment accelerates the process of onboarding eligible individuals into social protection programs.

By automating a crucial aspect of program management, the [g2p_program_autoenrol](g2p_program_autoenrol) module contributes to the overall efficiency and effectiveness of social protection initiatives. It empowers organizations to deliver timely and targeted support to those in need. 

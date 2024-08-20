# G2P Programs

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This document details the **G2P Programs** module within the OpenSPP platform. This module is responsible for defining and managing the core aspects of social protection programs, including eligibility criteria, program cycles, entitlement management, and payment processing.

### Purpose

The **G2P Programs** module provides a comprehensive framework for:

* **Defining Social Protection Programs**:  Allows administrators to create and configure programs with specific objectives, target populations, and operational processes.
* **Managing Program Cycles**:  Organizes program activities into distinct cycles, each with defined start and end dates, enrollment periods, and associated entitlements. 
* **Determining Eligibility**:  Provides a flexible mechanism for defining and evaluating eligibility criteria, ensuring that only qualified registrants receive program benefits.
* **Generating Entitlements**:  Automates the process of creating entitlements for eligible beneficiaries, tracking their validity periods and amounts. 
* **Facilitating Payments**:  Streamlines the disbursement of benefits to beneficiaries, either through cash transfers or other delivery mechanisms. 
* **Monitoring and Reporting**:  Offers tools for tracking program progress, beneficiary participation, and financial transactions, facilitating program evaluation and accountability.

### Module Dependencies and Integration

1. **G2P Registry: Base ([g2p_registry_base](g2p_registry_base))**:
    * Leverages the base registry module for core registrant management functionalities.
    * Accesses registrant data, such as demographics, contact information, and group affiliations, to evaluate eligibility and assign beneficiaries to programs.

2. **G2P Registry: Individual ([g2p_registry_individual](g2p_registry_individual))**:
    * Utilizes individual registrant data for eligibility determination, particularly for programs targeting individuals.
    * Extends individual registrant views to display program participation details. 

3. **G2P Registry: Group ([g2p_registry_group](g2p_registry_group))**:
    * Enables the enrollment of groups as beneficiaries, especially for programs designed for group participation.
    * Integrates with group registrant views to display program membership information.

4. **G2P Registry: Membership ([g2p_registry_membership](g2p_registry_membership))**:
    * Handles the relationships between individuals and groups, crucial for programs with group-based eligibility or delivery mechanisms.
    * Utilizes membership data to determine group eligibility and allocate benefits to individual members. 

5. **Account (account)**:
    * Integrates with Odoo's accounting module for financial management.
    * Records program-related transactions, tracks disbursement journals, and generates reports on program expenditures.

6. **Queue Job (queue_job)**:
    * Employs the queue job framework for asynchronous processing of computationally intensive tasks, such as eligibility verification, entitlement generation, and payment processing.
    * Improves system performance and user experience by delegating long-running operations to background jobs.

7. **G2P Bank ([g2p_bank](g2p_bank))**:
    * Facilitates the integration with financial service providers (FSPs) for electronic payment disbursements.
    * Manages bank account information for registrants and processes payments through pre-configured payment gateways.

8. **Calendar (calendar)**:
    * Utilizes Odoo's calendar module for scheduling program-related events, such as enrollment periods, payment cycles, and reporting deadlines.
    * Integrates with program and cycle views to display upcoming events and reminders.

9. **Event SMS (event_sms)**:
    * Enables SMS notifications for program-related events, including enrollment confirmations, eligibility updates, payment notifications, and reminders. 
    * Leverages the module's SMS gateway integration for efficient and timely communication with beneficiaries. 

### Additional Functionality

* **Program Model (g2p.program)**:
    * Defines the structure and attributes of social protection programs, including name, description, target type (individual or group), delivery mechanisms, and associated managers.
    * Offers a flexible system for configuring program-specific settings and workflows.

* **Program Membership (g2p.program_membership)**:
    * Creates a dedicated model to manage the association between registrants and programs, tracking enrollment status, enrollment dates, exit dates, and eligibility outcomes.
    * Provides a central location for managing program beneficiaries and monitoring their participation.

* **Program Cycle (g2p.cycle)**: 
    * Defines distinct periods within a program, with defined start and end dates, for organizing activities like enrollment, eligibility verification, entitlement generation, and payment disbursement.
    * Allows for structured management of program timelines and facilitates cycle-specific reporting and evaluation.

* **Entitlement (g2p.entitlement)**:
    * Models the right of a beneficiary to receive benefits within a specific cycle, defining the type of entitlement (cash, in-kind), amount, validity period, and disbursement details.
    * Offers a robust mechanism for tracking and managing the allocation of benefits to eligible beneficiaries.

* **Payment (g2p.payment)**:
    * Records details of individual payments made to beneficiaries, including payment method, amount, transaction date, status (success/failure), and associated fees.
    * Facilitates efficient payment processing, reconciliation, and auditing of program expenditures.

* **Program Managers**:
    * Defines various manager models for specific program functionalities, including:
        * **Eligibility Managers (g2p.eligibility.manager)**:  Responsible for defining and evaluating eligibility criteria based on program-specific rules.
        * **Cycle Managers (g2p.cycle.manager)**:  Manage the creation and execution of program cycles, including beneficiary enrollment and cycle-specific activities. 
        * **Entitlement Managers (g2p.program.entitlement.manager)**:  Oversee the generation, approval, and disbursement of entitlements to eligible beneficiaries.
        * **Payment Managers (g2p.program.payment.manager)**:  Handle payment processing, integration with FSPs, and reconciliation of payment transactions.
        * **Deduplication Managers (g2p.deduplication.manager)**:  Identify and resolve duplicate registrant entries to ensure accurate beneficiary identification and prevent fraud.
        * **Notification Managers (g2p.program.notification.manager)**:  Manage communication with beneficiaries, including SMS notifications and other forms of outreach. 

* **Customizable Workflows**: 
    * The module's flexible architecture allows administrators to define program-specific workflows, tailoring the sequence and execution of tasks like eligibility verification, entitlement generation, and payment processing.
    * Supports various program models and operational requirements.

### Conclusion

The **G2P Programs** module is the cornerstone of the OpenSPP platform, providing the essential tools for managing every stage of a social protection program's lifecycle. Its comprehensive functionality, integration with other core modules, and customizable workflows make it a powerful and adaptable solution for delivering social protection benefits effectively and efficiently. 

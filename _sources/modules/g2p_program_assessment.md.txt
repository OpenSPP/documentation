# g2p_program_assessment Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

This module enhances the OpenSPP system by adding assessment functionality to the [g2p_programs](g2p_programs) module. 

## Purpose

The primary purpose of this module is to facilitate the assessment process within social protection programs. It allows program managers to record assessments for individual beneficiaries at various stages of program participation.

## Functionality

The [g2p_program_assessment](g2p_program_assessment) module provides the following key features:

* **Assessment Recording:** Program staff can record assessments associated with a beneficiary's program membership. 
* **Assessment History:**  Maintains a history of all assessments conducted for a beneficiary, including the date, author, and content of each assessment.
* **Integration with Entitlements:** Assessments are linked to beneficiary entitlements, providing valuable context for entitlement decisions.
* **Rejection Workflow:** Offers a streamlined process to reject beneficiary applications based on assessments. 
* **Comments and Notes:** Enables program staff to add comments and notes to both assessments and beneficiary entitlements.

## Integration with other Modules

* **[g2p_programs](g2p_programs):** This module directly extends the functionality of [g2p_programs](g2p_programs) by adding assessment capabilities to program memberships.
* **mail:**  Leverages the **mail** module to facilitate communication, allowing users to post assessments as messages and add comments.

## Workflow

1. **Assessment Preparation:** Program staff can initiate the assessment process for beneficiaries, recording their findings and observations.
2. **Assessment Review:**  The module provides a centralized location to review all assessments associated with a beneficiary's program participation.
3. **Entitlement Decisions:**  Assessments provide valuable input for making informed decisions regarding beneficiary entitlements.
4. **Application Rejection:**  If necessary, program staff can reject a beneficiary's application based on the assessment outcomes. 
5. **Communication and Collaboration:** The module facilitates communication and collaboration among program staff through comments and messaging features.

By integrating assessments into the beneficiary management process, this module promotes transparency, accountability, and data-driven decision-making within DCI social protection programs. 


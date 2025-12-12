---
orphan: true
---

# Program: Manual Eligibility

This module introduces the capability to define and manage social protection programs where beneficiary eligibility is determined manually, rather than solely through automated rules. It provides essential flexibility for programs requiring direct administrative oversight in beneficiary selection and enrollment.

## Purpose

The **OpenSPP Manual Eligibility** module provides a crucial mechanism for programs that require human judgment or specific administrative decisions for beneficiary inclusion. It accomplishes the following:

*   **Enables Manual Beneficiary Selection:** Allows program administrators to designate specific programs or program cycles for manual eligibility determination. This is vital for scenarios where automated rules are insufficient, such as emergency aid, pilot programs, or highly targeted interventions.
*   **Supports Discretionary Program Enrollment:** Provides the functionality for staff to manually enroll or approve registrants into programs. This offers critical flexibility for unique program requirements, ensuring that programs can reach their intended populations effectively.
*   **Enhances Program Adaptability:** Facilitates the implementation of programs that need to quickly adapt to changing conditions or address specific, non-standard beneficiary criteria. It allows for a more responsive approach to program delivery.
*   **Provides Clear Identification of Manual Programs:** Flags programs, their associated cycles, and individual memberships as operating under manual eligibility. This ensures transparency and aids in effective program management, reporting, and auditing.

## Dependencies and Integration

The **OpenSPP Manual Eligibility** module integrates seamlessly with core OpenSPP components to extend program management capabilities:

*   **[G2P Registry: Base](g2p_registry_base)**: This module leverages the foundational registrant data provided by the base registry. It enables the association of manually eligible beneficiaries with their comprehensive registry profiles, ensuring all relevant information is linked.
*   **[G2P Programs](g2p_programs)**: It extends the core program management features, allowing administrators to configure programs and their cycles to operate with manual eligibility. This integration directly influences how eligibility rules are applied, supplementing or overriding automated criteria.
*   **[OpenSPP Programs](spp_programs)**: Building upon OpenSPP's specific program extensions, this module ensures that both cash and in-kind entitlement programs can utilize manual eligibility determination. It allows for flexibility across various benefit types.

## Additional Functionality

The module introduces key capabilities to manage manual eligibility effectively:

### Designating Programs for Manual Eligibility

Users can explicitly mark a program as having manual eligibility during its configuration. This critical flag indicates that beneficiary enrollment for this program will primarily involve direct administrative approval, rather than relying solely on predefined automated criteria. This setting automatically cascades to all associated program cycles and memberships, ensuring consistent operational procedures across the program.

### Manual Eligibility for Program Cycles

Individual program cycles inherit the manual eligibility status from their parent program. This feature provides granular control, allowing specific periods or iterations of a program to be managed with direct beneficiary selection, even if the overarching program might otherwise use automated rules. This flexibility is particularly useful for phased rollouts or targeted interventions within a longer program.

### Tracking Manual Membership Status

The module provides clear indicators within individual program membership records to show if a beneficiary's inclusion was determined manually. This transparency helps program staff understand the specific pathway of a beneficiary's enrollment, which is crucial for accurate reporting, auditing processes, and ensuring accountability for manually approved beneficiaries.

## Conclusion

The OpenSPP Manual Eligibility module provides essential flexibility for social protection programs, enabling administrators to manage beneficiary selection directly for programs or cycles where automated eligibility rules are not applicable or require human oversight.
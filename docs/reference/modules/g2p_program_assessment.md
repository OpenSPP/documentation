# G2P Program Assessment

The G2P Program Assessment module streamlines the process of evaluating and recording decisions about beneficiary participation in social protection programs. It enables program staff to document assessments, observations, and decisions directly within the OpenSPP platform, providing a clear audit trail and facilitating the management of entitlements.

## Purpose

This module provides essential capabilities for managing the decision-making process within G2P programs:

*   **Documents Beneficiary Assessments**: Captures detailed decisions, comments, and observations related to a beneficiary's program application or ongoing participation, ensuring a comprehensive record.
*   **Links Assessments to Program Elements**: Associates each assessment with a specific program membership or a particular entitlement, providing context and traceability.
*   **Facilitates Entitlement Generation**: Enables program administrators to trigger the creation of new entitlements based on positive assessments, automating the benefit allocation process.
*   **Manages Application Lifecycles**: Allows assessments to influence the state of a beneficiary's program application, such as moving from 'in-progress' to 'active' or 'rejected'.
*   **Maintains an Auditable Record**: Creates a clear and immutable history of all assessment activities, including who made the decision and when, which is critical for accountability and program evaluation.

## Dependencies and Integration

The G2P Program Assessment module integrates closely with core OpenSPP components to extend program management capabilities:

*   **[G2P Programs](g2p_programs)**: This module is foundational, as `g2p_program_assessment` directly extends and relies on the `g2p.program_membership` and `g2p.entitlement` models defined in the G2P Programs module. It uses program definitions, beneficiary enrollment status, and entitlement structures to contextualize assessments.
*   **Mail (mail)**: The module leverages OpenSPP's built-in mail and messaging system. Assessments are recorded as "remarks" or "comments" within this system, providing a robust, timestamped audit trail and enabling communication features around assessment activities.

This module primarily enhances the functionality of G2P Programs by adding a layer for systematic decision-making and record-keeping, ensuring that all beneficiary-related actions are well-documented and transparent.

## Additional Functionality

### Recording Program Decisions and Observations

Program staff can record detailed assessments and observations directly on a beneficiary's program membership or a specific entitlement record. This feature captures crucial information regarding eligibility, compliance, or any other program-specific evaluation. Each assessment includes the author, date, and comprehensive remarks, providing a complete historical context for all decisions.

### Streamlined Entitlement Generation

The module provides intuitive actions to facilitate the creation of new entitlements based on completed assessments. After program staff review and record necessary assessments, a dedicated "Create Entitlement" button becomes available on the program membership. This automates the process of generating new benefit entitlements for eligible beneficiaries, ensuring that only those with recent, positive assessments receive benefits.

### Managing Beneficiary Application Status

Assessments play a critical role in managing the lifecycle of a beneficiary's program application. The module supports actions such as "Reject Application," which updates the beneficiary's program status (e.g., from 'active' or 'in-progress' to 'rejected') and can automatically cancel any associated draft entitlements. This ensures that application statuses accurately reflect the latest assessment outcomes.

### Maintaining Historical Assessment Context

To provide continuity and comprehensive record-keeping, the module automatically associates relevant historical assessments with new entitlements. When a new entitlement is generated, the system identifies and links previous assessments that occurred between the creation of the prior entitlement and the current one. This ensures that all pertinent decision-making history is readily available for each benefit cycle.

## Conclusion

The G2P Program Assessment module is vital for ensuring transparent, accountable, and efficient decision-making within social protection programs by providing a structured way to record, manage, and link beneficiary assessments to program activities and entitlements.
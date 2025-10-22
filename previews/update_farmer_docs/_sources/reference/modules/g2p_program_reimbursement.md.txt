---
orphan: true
---

# G2P Program Reimbursement

The G2P Program Reimbursement module extends OpenSPP's core G2P Programs functionality to manage programs specifically designed for reimbursing beneficiaries or service providers for eligible expenses. It streamlines the process of submitting, tracking, and processing reimbursement claims.

## Purpose

This module provides a robust framework for managing programs where financial assistance is provided as a reimbursement for incurred costs, rather than a direct upfront payment. It enables OpenSPP users to:

*   **Designate Reimbursement Programs:** Clearly define and configure specific social protection programs as reimbursement-based, setting them apart from standard benefit distribution programs.
*   **Process Reimbursement Claims:** Facilitate the submission and creation of new entitlements that act as reimbursements for previously approved or original entitlements.
*   **Track Original Entitlements:** Maintain a clear link between a reimbursement claim and its original qualifying entitlement, ensuring transparency and auditability.
*   **Manage Service Provider Eligibility:** Adapt eligibility criteria to include service providers (e.g., healthcare facilities, educational institutions) as potential beneficiaries for services rendered.
*   **Tailor Program Workflows:** Adjust program and cycle management views to reflect the unique requirements and data points relevant to reimbursement processes.

## Dependencies and Integration

The G2P Program Reimbursement module seamlessly integrates with and extends core OpenSPP components:

*   **`g2p_programs`**: This is the foundational module for defining and managing all social protection programs, cycles, and entitlements. The G2P Program Reimbursement module builds directly upon `g2p_programs` by introducing the concept of reimbursement programs and modifying how entitlements and cycles are handled within that context. It extends models like `g2p.program`, `g2p.cycle`, and `g2p.entitlement` to support reimbursement-specific fields and logic.
*   **`g2p_program_assessment`**: While not directly altering its functionality, this module ensures that any assessment capabilities provided by `g2p_program_assessment` are available for the original entitlements that may later become eligible for reimbursement. This ensures a consistent assessment framework across all entitlement types.

## Additional Functionality

### Reimbursement Program Configuration

Administrators can easily designate any program as a "reimbursement program" through a simple setting. This flag automatically adjusts system behavior for that program, enabling specific reimbursement workflows. Furthermore, an administrator can link a reimbursement program to an *original* program, defining which program's entitlements are eligible for reimbursement under the new scheme.

### Streamlined Reimbursement Claim Submission

The module provides a clear process for submitting reimbursement claims. Users can initiate a claim against an existing, valid original entitlement by providing details such as the partner (beneficiary or service provider), the original entitlement's unique code, the claimed amount, and any associated supporting documents. The system then automatically creates a new reimbursement entitlement, linking it to the original for complete traceability.

### Adapted Eligibility for Service Providers

Unlike standard G2P programs that focus on individual or household beneficiaries, reimbursement programs often involve payments to service providers. This module intelligently adapts the eligibility criteria for reimbursement programs to identify and manage these service providers, ensuring that the correct entities are targeted for payments. For example, a program reimbursing medical expenses would target healthcare providers as eligible entities.

### Enhanced Entitlement Visibility and Tracking

Reimbursement entitlements are clearly marked within the system and display a direct link to the "Original Entitlement of this Reimbursement." This provides an immediate understanding of the claim's origin. The system also automatically suggests a "Recommended amount" for reimbursement, typically derived from the initial amount of the original entitlement, aiding in efficient claim processing.

## Conclusion

The G2P Program Reimbursement module is essential for OpenSPP implementations that require managing social protection programs involving the reimbursement of eligible expenses, providing a dedicated and integrated solution for these specialized workflows.
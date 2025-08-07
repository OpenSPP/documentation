---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# OpenG2P Programs: Reimbursement Module

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

The [g2p_program_reimbursement](g2p_program_reimbursement) module extends the OpenG2P platform to manage reimbursement programs. These programs differ from standard social assistance programs, focusing on reimbursing pre-approved service providers for delivering goods or services to beneficiaries. 

This module builds upon the core functionality of the [g2p_programs](g2p_programs) and [g2p_program_assessment](g2p_program_assessment) modules.

## Features

* **Reimbursement Program Designation:** Designate specific programs as "reimbursement programs" within the system.
* **Service Provider Management:** Manage service providers as participants in reimbursement programs. The module leverages the existing `res.partner` model, filtering and displaying partners designated as "Service Providers".
* **Reimbursement Claim Submission:** Enables service providers to submit reimbursement claims for services rendered to beneficiaries. 
* **Claim Validation and Approval:**  Provides a structured workflow to validate and approve submitted reimbursement claims.
* **Integration with Entitlements:**  Seamlessly integrates with the entitlement system to generate and track reimbursements.

## Key Concepts

* **Reimbursement Program:** A specialized type of program within OpenG2P that manages the reimbursement of pre-approved service providers.
* **Service Provider:**  A business or individual registered in the system to provide goods or services to beneficiaries and eligible for reimbursement.
* **Reimbursement Claim:** A formal request submitted by a service provider for reimbursement of rendered services.
* **Original Entitlement:** In cases where a reimbursement is directly linked to a beneficiary's existing entitlement, this refers to the initial entitlement against which the service was provided.

## Module Integration

The [g2p_program_reimbursement](g2p_program_reimbursement) module seamlessly integrates with the following modules:

* **[g2p_programs](g2p_programs):**  Inherits core program management features and extends them to accommodate reimbursement program specifics.
* **[g2p_program_assessment](g2p_program_assessment):** Leverages assessment functionalities to potentially support the validation of reimbursement claims. 

## Example Use Case

1. **Program Setup:** A government agency sets up a reimbursement program for agricultural inputs. They register fertilizer suppliers as service providers in the system.
2. **Beneficiary Entitlement:** A farmer is assessed and granted an entitlement for a specific type and quantity of fertilizer.
3. **Service Delivery & Claim:** The farmer redeems their entitlement from a registered fertilizer supplier. The supplier then submits a reimbursement claim through the system, referencing the farmer's original entitlement and providing necessary documentation.
4. **Claim Review & Approval:** The claim undergoes review and approval by the program administrators. 
5. **Reimbursement Processing:** Once approved, the system generates a reimbursement payment to the supplier.

This module streamlines the management of reimbursement programs, improves transparency, and ensures efficient service delivery to beneficiaries. 

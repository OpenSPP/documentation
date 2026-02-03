---
openspp:
  doc_status: draft
---

# OpenSPP MIS Demo V2


## Overview

The MIS Demo V2 module provides comprehensive demonstration data for SP-MIS deployments. It includes fixed demo stories, sample programs with eligibility criteria, change request configurations, approval workflows, and a volume generator for creating large datasets. This module is designed for training, demonstrations, and testing.

## Purpose

This module is designed to:

- **Demonstrate SP-MIS capabilities:** Showcase program management, enrollment, and cycles
- **Provide training data:** Pre-configured programs and registrants for user training
- **Enable volume testing:** Generate large datasets to test system performance
- **Illustrate workflows:** Show approval processes and change request handling

## Module Dependencies

| Dependency                | Description                                                           |
| ------------------------- | --------------------------------------------------------------------- |
| **spp_starter_sp_mis**    | Complete SP-MIS bundle with programs and service points               |
| **spp_cr_types_advanced** | Advanced change request types (Add/Remove Member, Exit, Split, Merge) |
| **spp_demo**              | Core demo data generator                                              |
| **spp_gis_report**        | Geographic visualization for reports                                  |
| **spp_claim_169**         | QR credentials for beneficiary verification                           |

### External Python Dependencies

| Package      | Description                           |
| ------------ | ------------------------------------- |
| **faker**    | Generates fake but realistic data     |
| **requests** | HTTP client for external integrations |

## Key Features

### Pre-Configured Demo Programs

Sample programs demonstrating different configurations:

| Program Type     | Description                                 |
| ---------------- | ------------------------------------------- |
| Cash Transfer    | Direct cash payments to eligible households |
| Food Assistance  | In-kind food distribution program           |
| Child Support    | Benefits for families with children         |
| Emergency Relief | Rapid response assistance program           |

### Demo Personas

Pre-created registrants with realistic stories:

| Persona      | Description                   |
| ------------ | ----------------------------- |
| Maria Santos | Single mother with 3 children |
| Ahmed Hassan | Elderly pensioner             |
| Lakshmi Devi | Rural farmer household head   |
| John Kamau   | Urban informal worker         |

### Demo Users

Users configured with different roles for testing:

| Role            | Username      | Purpose                   |
| --------------- | ------------- | ------------------------- |
| Administrator   | admin         | Full system access        |
| Program Manager | pm_demo       | Program configuration     |
| Field Officer   | officer_demo  | Data entry and enrollment |
| Approver        | approver_demo | Approval workflows        |

### Approval Definitions

Pre-configured approval workflows:

| Workflow            | Description                                 |
| ------------------- | ------------------------------------------- |
| Program Enrollment  | Two-level approval for new enrollments      |
| High-Value Payments | Additional approval for large disbursements |
| Change Requests     | Review chain for data modifications         |

### Event Types

Sample event types for tracking program activities:

| Event Type   | Description                            |
| ------------ | -------------------------------------- |
| Enrollment   | Beneficiary enrolled in program        |
| Disbursement | Payment or distribution made           |
| Verification | Identity or eligibility verified       |
| Graduation   | Beneficiary exits program successfully |

### Change Request Types

Advanced CR types for data maintenance:

| CR Type         | Description                      |
| --------------- | -------------------------------- |
| Add Member      | Add individual to household      |
| Remove Member   | Remove individual from household |
| Split Household | Divide one household into two    |
| Merge Household | Combine two households into one  |
| Exit Program    | Formal program exit              |

### GIS Reports

Geographic visualizations:

| Report            | Description                         |
| ----------------- | ----------------------------------- |
| Beneficiary Map   | Distribution of registrants by area |
| Service Point Map | Location of distribution centers    |
| Coverage Report   | Program coverage by region          |

### Volume Generator

Create large datasets for performance testing:

| Setting                 | Description                     |
| ----------------------- | ------------------------------- |
| Number of Households    | Total households to generate    |
| Members per Household   | Range of household sizes        |
| Program Enrollment Rate | Percentage enrolled in programs |
| Geographic Distribution | Spread across areas             |

## Integration

The MIS Demo V2 module integrates with:

- **All SP-MIS modules:** Uses full program management capabilities
- **spp_gis_report:** Generates geographic visualizations
- **spp_claim_169:** Creates QR-based beneficiary credentials

## Post-Installation

After installation, the module automatically:

1. Creates demo currencies (if not present)
2. Sets up demo personas and stories
3. Configures approval definitions
4. Creates sample programs with eligibility criteria
5. Sets up event types and change request configurations

## Are you stuck?

### Demo programs not appearing

**Symptom:** Sample programs are not visible after installation

**Cause:** The post-init hook may not have completed, or user lacks program access

**Solution:** Check the installation logs for errors during post_init_hook. Ensure your user has program viewer or manager role.

### Volume generation times out

**Symptom:** Generating large datasets fails or takes too long

**Cause:** Large batch sizes can exhaust server resources

**Solution:** Reduce the number of records per batch. Use queue jobs for background processing. Monitor server memory during generation.

### Demo users cannot log in

**Symptom:** Demo user credentials do not work

**Cause:** Passwords may have been changed or users deactivated

**Solution:** Reset demo user passwords through the Users menu. Verify demo users are active.

### Change requests not processing

**Symptom:** Submitted change requests stay in draft state

**Cause:** Approval workflow may require specific approvers

**Solution:** Log in as the approver_demo user to process pending approvals. Verify the approval definitions are correctly configured.

### GIS reports empty

**Symptom:** Geographic reports show no data

**Cause:** Registrants may not have geographic coordinates or area assignments

**Solution:** Ensure registrants have area_id assigned. The volume generator should populate areas automatically.

---
openspp:
  doc_status: draft
---

# OpenSPP Starter: SP-MIS


## Overview

The SP-MIS Starter module is a comprehensive bundle for Social Protection Management Information System deployments. It extends the Social Registry with full program management capabilities, including enrollment, payment cycles, service points, and approval workflows.

## Purpose

This module is designed to:

- **Provide complete SP-MIS functionality:** Install all modules needed for social protection program management in one step
- **Enable program management:** Define programs with eligibility criteria and manage beneficiary enrollment
- **Support payment cycles:** Manage distribution and payment cycle workflows
- **Track service delivery:** Manage service points and distribution locations

## Module Dependencies

| Dependency                      | Description                                        |
| ------------------------------- | -------------------------------------------------- |
| **spp_starter_social_registry** | Complete Social Registry foundation                |
| **spp_programs**                | Program management with eligibility and enrollment |
| **spp_approval**                | Multi-level approval workflows                     |
| **spp_event_data**              | Audit trail for program activities                 |

### Included from Social Registry

Everything in `spp_starter_social_registry`:

- Registry management for individuals and groups
- Change request system for data maintenance
- API V2 with consent-based access
- DCI integration for external registries
- Logic Studio for no-code expressions
- Standardized vocabularies

## Key Features

### Program Management

Define and manage social protection programs:

| Feature               | Description                                               |
| --------------------- | --------------------------------------------------------- |
| Program Definition    | Create programs with descriptions and configurations      |
| Eligibility Criteria  | Define who qualifies using expressions                    |
| Enrollment Management | Track beneficiary membership in programs                  |
| Target Groups         | Specify whether programs target individuals or households |

### Payment and Distribution Cycles

Manage recurring program activities:

| Feature                 | Description                                     |
| ----------------------- | ----------------------------------------------- |
| Cycle Creation          | Define payment or distribution periods          |
| Beneficiary Lists       | Generate lists of eligible recipients per cycle |
| Entitlement Calculation | Compute benefits based on program rules         |
| Disbursement Tracking   | Track payments and distributions                |

### Service Points

Manage locations where services are delivered:

| Feature             | Description                               |
| ------------------- | ----------------------------------------- |
| Location Management | Register service points with addresses    |
| Assignment          | Link service points to programs and areas |
| Capacity Tracking   | Monitor service point utilization         |

### Approval Workflows

Multi-level approval for sensitive operations:

| Feature              | Description                             |
| -------------------- | --------------------------------------- |
| Approval Definitions | Configure who can approve what          |
| Review Chains        | Set up sequential or parallel approvals |
| Audit Trail          | Track all approval decisions            |

### Event Data

Capture program activities with audit trails:

| Feature       | Description                               |
| ------------- | ----------------------------------------- |
| Event Types   | Define categories of program events       |
| Event Records | Log activities with timestamps and actors |
| Event Data    | Capture structured data for each event    |

### Registry Restrictions

The SP-MIS configuration can restrict direct registry editing:

| Setting                  | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| Restrict Registrant Edit | Users must use change requests instead of direct edits |

## Integration

The SP-MIS Starter integrates with:

- **All Social Registry modules:** Inherits full registry capabilities
- **spp_api_v2_cycles:** Exposes cycle management via REST API (auto-installs)
- **spp_service_points:** Manages distribution locations (transitive dependency)

## Use Cases

| Use Case                   | Description                              |
| -------------------------- | ---------------------------------------- |
| Cash Transfer Programs     | Direct cash payments to beneficiaries    |
| Conditional Cash Transfers | Payments tied to compliance requirements |
| Social Assistance Programs | General welfare assistance               |
| Food Distribution Programs | In-kind food aid management              |
| In-Kind Transfer Programs  | Non-cash benefit distribution            |

## Are you stuck?

### Cannot create programs

**Symptom:** Program menu is visible but cannot create new programs

**Cause:** User may lack the required permissions

**Solution:** Ensure you have the Program Manager or Administrator role. Contact your system administrator to assign appropriate permissions.

### Eligibility criteria not evaluating

**Symptom:** Beneficiaries not being correctly included or excluded from programs

**Cause:** The eligibility expression may have syntax errors or reference undefined fields

**Solution:** Test the eligibility expression in Logic Studio first. Verify all referenced fields exist on the target model.

### Cycle not generating beneficiary list

**Symptom:** Creating a cycle does not populate the beneficiary list

**Cause:** No registrants match the program's eligibility criteria, or the cycle has not been processed

**Solution:** Verify eligibility criteria match at least some registrants. Run the cycle processing action to generate the list.

### Service points not appearing

**Symptom:** Cannot assign service points to programs or cycles

**Cause:** No service points have been created for the program's geographic areas

**Solution:** Create service points in the areas where the program operates before attempting assignment.

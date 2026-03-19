---
openspp:
  doc_status: draft
---

# Demo

**Module:** `spp_dci_demo`

## Overview

DCI Demo: Birth Verification for Child Benefit Enrollment

## Purpose

This module is designed to:

- **Demonstrate DCI birth verification:** Add birth verification via DCI to the "Add Member" change request workflow, querying a CRVS registry (e.g., OpenCRVS) to verify birth registration numbers.
- **Auto-create verified registry IDs:** When a birth is verified, automatically create a BRN registry ID on the new individual with verification metadata.
- **Auto-enroll in programs:** After a member is added and verified, automatically enroll the household and its members in a configured program.

## Module Dependencies

| Dependency | Purpose |
| --- | --- |
| `spp_mis_demo_v2` | Demo Generator V2 for SP-MIS programs with fixed stories ... |
| `spp_dci_client` | Base DCI client infrastructure with OAuth2 and data sourc... |
| `spp_change_request_v2` | Configuration-driven change request system with UX improv... |
| `spp_programs` | Manage cash and in-kind entitlements, integrate with inve... |

## Key Features

### Birth Verification on Change Requests

Extends the "Add Member" change request detail (`spp.cr.detail.add_member`) with birth verification fields:

| Field | Type | Description |
| --- | --- | --- |
| `birth_registration_number` | Char | BRN entered by the social worker |
| `birth_verification_status` | Selection | unverified, verified, not_found, or error |
| `dci_data_match` | Boolean | Whether DCI response data matches CR fields |
| `birth_verification_date` | Datetime | When verification was performed |
| `birth_verification_response` | Text | Raw JSON response for audit |
| `dci_data_source_id` | Many2one | CRVS data source to verify against |

A "Verify Birth" button triggers a DCI search by BRN against the configured CRVS registry. Editing verified fields (name, DOB, gender, BRN) automatically invalidates the verification.

### Data Match Verification

After a successful DCI lookup, the module compares the returned person data against the change request fields:

- Given name (case-insensitive)
- Family name (case-insensitive)
- Birth date
- Gender/sex

Mismatches are logged and flagged for manual review.

### Change Request Reviewer UX

The main change request form (`spp.change.request`) is extended with computed DCI verification fields:

| Field | Description |
| --- | --- |
| `dci_verification_status` | Pulled from the detail record's birth verification status |
| `dci_verification_html` | HTML summary with status badge, BRN, and match indicator |
| `dci_data_match` | Whether the DCI data matches |

### Verified BRN Registry ID

When the change request is applied and the birth was verified, a `spp.registry.id` record is created on the new individual with:

- The BRN as the identifier value
- Status set to `valid`
- Verification method set to `dci_api`
- Verification source from the data source name
- Raw verification response stored for audit

### Auto-Enrollment

After applying the change request, if a program is configured via the `spp_dci_demo.enrollment_program_id` system parameter, the household and all its members (including the newly added child) are automatically enrolled.

## Integration

- **spp_dci_client:** Uses `DCIClient` to perform DCI search queries against configured CRVS data sources.
- **spp_change_request_v2:** Extends `spp.cr.detail.add_member` with verification fields and `spp.cr.apply.add_member` with post-apply logic for BRN creation and auto-enrollment.
- **spp_programs:** Creates `spp.program.membership` records for auto-enrollment of households and members.
- **spp_mis_demo_v2:** Depends on demo data for the target enrollment program (Conditional Child Grant).

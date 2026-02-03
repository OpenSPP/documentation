---
openspp:
  doc_status: draft
---

# DCI Client - Disability Registry

This module is for **developers** and **sys admins** who need to integrate OpenSPP with external disability registries using the DCI API standard.

## Overview

The DCI Client - Disability Registry module enables connection to disability registries via the DCI API standard. It allows social protection programs to verify disability status and retrieve disability assessment data for eligibility determination and targeted assistance.

Use this module when your program needs to:

- Verify disability registration status for individuals
- Retrieve disability assessment details and classifications
- Update registrant records with disability information
- Enable disability-based program eligibility criteria

## Module Dependencies

| Dependency | Purpose |
|------------|---------|
| `spp_dci_client` | Base DCI client infrastructure |
| `spp_dci_server` | DCI server for bidirectional exchange |
| `spp_registry` | Registrant data for updates |

## Data Models

| Model | Purpose |
|-------|---------|
| `spp.dci.disability.status` | Stores disability status records |
| `spp.dci.dr.sender` | DR request sender configuration |

## Disability Data Elements

The module retrieves and stores the following data elements from disability registries:

| Element | Description |
|---------|-------------|
| Registration ID | Official disability registration number |
| Disability Type | Classification of disability |
| Severity Level | Mild, moderate, severe, or profound |
| Assessment Date | When assessment was conducted |
| Expiry Date | When reassessment is required |
| Functional Limitations | Specific limitations documented |

### Disability Classifications

Common disability categories (may vary by registry):

| Category | Description |
|----------|-------------|
| Physical | Mobility and motor impairments |
| Visual | Vision impairments |
| Hearing | Hearing impairments |
| Intellectual | Cognitive and learning disabilities |
| Psychosocial | Mental health conditions |
| Multiple | Combination of disabilities |

## Configuration

### Step 1: Configure the DR Data Source

In the base DCI client, create a data source for the disability registry:

| Field | Example Value |
|-------|---------------|
| Name | National Disability Registry |
| Base URL | `https://api.ndr.gov.example/dci/v1` |
| Auth URL | `https://auth.ndr.gov.example/token` |

### Step 2: Configure the DR Sender

Navigate to **DCI > Disability Registry > Sender Configuration**:

| Field | Description |
|-------|-------------|
| Data Source | Select DR data source created in Step 1 |
| Sender ID | Your organization identifier |

## Query Operations

| Operation | Description |
|-----------|-------------|
| Verify Registration | Check if person has disability registration |
| Get Status | Retrieve current disability status |
| Get Assessment | Fetch full assessment details |
| Check Expiry | Verify if registration is still valid |

## Usage

### Query Disability Status

1. Navigate to a registrant record
2. Click **Action > Query Disability Registry**
3. System queries using the registrant's ID
4. Review and confirm results
5. Status is automatically added to the registrant

### Bulk Verification

1. Select multiple registrants
2. Click **Action > Bulk Disability Verification**
3. Process runs in background
4. Review results in verification log

## Integration

### With Registry

Disability data integrates with registrant records:

- Links disability status to individual registrants
- Stores verification source and date
- Tracks status changes over time

### With Programs

Disability data supports program targeting:

- Eligibility criteria can include disability status
- Benefit amounts may vary by disability severity
- Special assistance flags for service delivery

## Technical Details

| Property | Value |
|----------|-------|
| Technical Name | `spp_dci_client_dr` |
| Category | OpenSPP/Integration |
| Version | 19.0.1.0.0 |
| License | LGPL-3 |
| Application | No |
| Development Status | Alpha |

## Are you stuck?

### Registration not found

**Symptom:** Query returns "no registration found" for a known disabled person.

**Cause:** The person may not be registered in the disability system, or they may be registered under a different ID.

**Solution:**

1. Verify the national ID matches registry records
2. Check if the person is registered in the disability system
3. Advise the person to register with the disability registry first if needed

### Expired registration

**Symptom:** Status shows as expired or invalid.

**Cause:** Disability registration may require periodic reassessment.

**Solution:**

1. Check the expiry date in the retrieved data
2. Advise the registrant to renew their disability registration
3. Contact the disability registry for reassessment scheduling

### Connection timeout

**Symptom:** Query fails with timeout error.

**Cause:** Network issues or the external registry is unavailable.

**Solution:**

1. Check network connectivity to the registry endpoint
2. Verify the Base URL and Auth URL in the data source configuration
3. Contact the registry administrator to confirm service availability

## See Also

- {doc}`spp_dci_client` - Base DCI client infrastructure
- {doc}`spp_registry` - Registrant data management
- {doc}`spp_programs` - Program eligibility and targeting

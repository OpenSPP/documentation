---
openspp:
  doc_status: draft
---

# DCI Client - IBR

This module is for **developers** and **system administrators** who need to integrate OpenSPP with an Integrated Beneficiary Registry (IBR) for duplication checks via the DCI API standard.

## Overview

The DCI Client - IBR module enables OpenSPP to connect to external identity bureaus and beneficiary registries to detect and prevent duplicate enrollments across social protection programs. It implements the Digital Convergence Initiative (DCI) API standard for cross-registry communication.

Use this module when you need to:

- Check if a registrant exists in another program's registry
- Verify identities against authoritative sources
- Prevent duplicate benefit disbursements
- Support data quality and fraud prevention workflows

## Module Dependencies

| Dependency       | Purpose                                      |
| ---------------- | -------------------------------------------- |
| `spp_dci_client` | Base DCI client infrastructure and API layer |
| `spp_dci_server` | DCI server for bidirectional data exchange   |
| `spp_registry`   | Registrant data and identifier management    |

## Data Models

| Model                       | Purpose                                             |
| --------------------------- | --------------------------------------------------- |
| `spp.dci.duplication.check` | Stores duplication check requests and results       |
| `spp.dci.ibr.sender`        | Trusted IBR registry configuration for verification |

### Duplication Check Fields

| Field              | Type      | Description                                      |
| ------------------ | --------- | ------------------------------------------------ |
| `partner_id`       | Many2one  | The registrant being checked                     |
| `identifier_type`  | Char      | ID type used (UIN, BRN, MRN, DRN)                |
| `identifier_value` | Char      | Value of the identifier                          |
| `check_date`       | Datetime  | When the check was performed                     |
| `result`           | Selection | no_match, possible_match, or confirmed_match     |
| `matched_programs` | Text      | Programs where duplicates were found             |
| `state`            | Selection | ready, checking, completed, or failed            |
| `data_source_id`   | Many2one  | The IBR data source queried                      |
| `error_message`    | Text      | Error details if the check failed                |

### IBR Sender Fields

| Field            | Type      | Description                                   |
| ---------------- | --------- | --------------------------------------------- |
| `name`           | Char      | Friendly name for the IBR registry            |
| `sender_id`      | Char      | DCI sender identifier (e.g., ibr.national.gov)|
| `public_key`     | Text      | PEM-encoded public key for signature verification |
| `jwks_url`       | Char      | URL to the registry's JWKS endpoint           |
| `algorithm`      | Selection | Signature algorithm (ed25519 or rs256)        |
| `last_key_fetch` | Datetime  | When the public key was last fetched          |
| `active`         | Boolean   | Whether this sender is active                 |

## Configuration

### Step 1: Configure the DCI Data Source

First, create a data source in the base DCI client module. Navigate to **DCI > Configuration > Data Sources**.

| Field         | Example Value                        | Description                     |
| ------------- | ------------------------------------ | ------------------------------- |
| Name          | National ID Bureau                   | Descriptive name                |
| Registry Type | IBR                                  | Must be set to IBR              |
| Base URL      | https://api.idbureau.gov/dci         | API endpoint                    |
| Auth URL      | https://auth.idbureau.gov/token      | OAuth token endpoint            |
| Client ID     | openspp-client                       | OAuth client credentials        |
| Client Secret | (configured securely)                | OAuth client credentials        |

### Step 2: Configure the IBR Sender

Navigate to **DCI > Identity Bureau > Sender Configuration** to register trusted IBR registries.

| Field     | Example Value                        | Description                           |
| --------- | ------------------------------------ | ------------------------------------- |
| Name      | National Registry                    | Friendly name                         |
| Sender ID | ibr.national.gov                     | DCI identifier (alphanumeric, dots, hyphens) |
| JWKS URL  | https://ibr.national.gov/.well-known/jwks.json | For automatic key retrieval |

Click **Fetch Public Key** to automatically retrieve and store the registry's public key from the JWKS endpoint.

## Usage

### Programmatic Duplication Check

```python
# Create a duplication check record
check = env["spp.dci.duplication.check"].create({
    "partner_id": partner.id,
    "identifier_type": "UIN",
    "identifier_value": "123456789",
    "data_source_id": data_source.id,
})

# Run the check
check.action_run_check()

# Check results
if check.result == "confirmed_match":
    # Handle duplicate found
    matched_programs = check.matched_programs.split("\n")
```

### Using the IBR Service Directly

```python
from odoo.addons.spp_dci_client_ibr.services import IBRService

# Initialize service with data source
ibr_service = IBRService(data_source, env)

# Check for duplicates
result = ibr_service.check_duplication(partner)
if result["is_duplicate"]:
    print(f"Found in programs: {result['matched_programs']}")

# Search for a specific beneficiary
matches = ibr_service.search_beneficiary("UIN", "123456789")

# Get enrollment status
status = ibr_service.get_enrollment_status("UIN", "123456789")
if status["enrolled"]:
    print(f"Enrolled in: {status['programs']}")
```

### Duplication Check States

| State      | Description                          |
| ---------- | ------------------------------------ |
| `ready`    | Check created, not yet executed      |
| `checking` | Check in progress                    |
| `completed`| Check finished successfully          |
| `failed`   | Check failed (see error_message)     |

### Check Results

| Result           | Description                                      |
| ---------------- | ------------------------------------------------ |
| `no_match`       | No duplicates found in the IBR                   |
| `possible_match` | Potential match found, requires manual review    |
| `confirmed_match`| Confirmed duplicate exists in another program    |

## Technical Details

| Property       | Value                |
| -------------- | -------------------- |
| Technical Name | `spp_dci_client_ibr` |
| Category       | OpenSPP/Integration  |
| Version        | 19.0.1.0.0           |
| License        | LGPL-3               |
| Application    | No                   |
| Status         | Alpha                |

## Are you stuck?

### No active IBR data source found

**Symptom:** Error message when running a duplication check.

**Cause:** No DCI data source is configured with `registry_type = "ibr"`.

**Solution:**

1. Navigate to **DCI > Configuration > Data Sources**
2. Create a new data source or edit an existing one
3. Set Registry Type to **IBR**
4. Ensure the data source is marked as Active

### Partner has no identifiers configured

**Symptom:** Error when checking a registrant for duplicates.

**Cause:** The registrant has no ID documents in their registry record.

**Solution:**

1. Navigate to the registrant's record
2. Add at least one identifier (UIN, BRN, MRN, DRN, etc.)
3. Retry the duplication check

### Failed to fetch public key from JWKS URL

**Symptom:** Error when clicking Fetch Public Key on an IBR sender.

**Cause:** Network issues or invalid JWKS URL.

**Solution:**

1. Verify the JWKS URL is correct and accessible
2. Check that the URL returns valid JSON with a `keys` array
3. Ensure the `kid` (key ID) starts with the sender_id followed by a pipe character
4. Check server logs for detailed error messages

### Duplication check timing out

**Symptom:** Check stays in "checking" state or fails with timeout error.

**Cause:** Slow response from the external IBR or network issues.

**Solution:**

1. Check the IBR service status
2. Verify network connectivity to the IBR endpoint
3. Review Odoo server logs for connection errors
4. Consider implementing retry logic for batch operations

## See Also

- {doc}`spp_dci_client` - Base DCI client infrastructure
- {doc}`spp_dci_server` - DCI server for receiving requests
- {doc}`spp_registry` - Registrant data management

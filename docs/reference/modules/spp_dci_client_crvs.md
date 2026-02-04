---
openspp:
  doc_status: draft
---

# DCI Client - CRVS

**Module:** `spp_dci_client_crvs`
This module is for **developers** and **sys admins** who need to integrate OpenSPP with Civil Registration and Vital Statistics (CRVS) systems. It enables your social protection programs to verify and receive vital events data (births, deaths, marriages) from external CRVS registries using the DCI API standard.

## Overview

The DCI Client - CRVS module connects OpenSPP to government CRVS systems, allowing automatic verification of birth records, death status checks, and real-time event notifications. When a death is recorded in the national CRVS system, OpenSPP can automatically receive the notification and update beneficiary status.

## When You Need This

Use this module if you need to:

- Verify birth records against a national CRVS registry
- Check if a beneficiary is deceased before disbursement
- Receive automatic notifications when vital events occur
- Keep beneficiary data synchronized with civil registration records

If you only need basic registry management without external CRVS integration, see {doc}`spp_registry` instead.

## Dependencies

| Module | Purpose |
|--------|---------|
| `spp_dci_client` | Base DCI client infrastructure |
| `spp_registry` | Registrant data for matching and updates |

## Key Features

### Supported Vital Events

| Event Type | Description | Registry Impact |
|------------|-------------|-----------------|
| Birth | Birth registration records | Updates birth date, adds birth registration number |
| Death | Death registration records | Disables registrant, updates program memberships |
| Marriage | Marriage registration records | Updates civil status to married |
| Divorce | Divorce records | Updates civil status to divorced |

### CRVS Operations

| Operation | Method | Description |
|-----------|--------|-------------|
| Verify Birth | `verify_birth()` | Query CRVS for birth record by identifier |
| Check Death | `check_death()` | Check if person has a death record |
| Subscribe | `subscribe_events()` | Subscribe to receive vital event notifications |
| Unsubscribe | `unsubscribe_events()` | Stop receiving notifications |

## Data Models

| Model | Technical Name | Purpose |
|-------|----------------|---------|
| CRVS Event | `spp.dci.crvs.event` | Logs vital events received from CRVS |
| CRVS Sender | `spp.dci.crvs.sender` | Stores trusted CRVS registry public keys |

### CRVS Event Fields

| Field | Type | Description |
|-------|------|-------------|
| Event Type | Selection | Birth, death, marriage, or divorce |
| Identifier Type | Char | ID type (BRN, DRN, UIN, etc.) |
| Identifier Value | Char | The actual identifier value |
| Event Date | Date | When the vital event occurred |
| State | Selection | Received, processing, processed, or error |
| Person | Many2one | Matched registrant (if found) |
| Raw Data | Text | Original JSON from CRVS |

### CRVS Sender Fields

| Field | Type | Description |
|-------|------|-------------|
| Sender ID | Char | DCI sender identifier (e.g., `crvs.national.gov`) |
| Public Key | Text | PEM-encoded key for signature verification |
| JWKS URL | Char | URL to fetch public keys (`.well-known/jwks.json`) |
| Algorithm | Selection | Ed25519 or RSA-256 |

## Configuration

### Step 1: Configure CRVS Data Source

First, set up the CRVS registry as a DCI data source in `spp_dci_client`:

| Field | Example Value |
|-------|---------------|
| Code | `crvs_main` |
| Name | National CRVS Registry |
| Registry Type | CRVS |
| Base URL | `https://api.crvs.gov.example/dci/v1` |

### Step 2: Register CRVS Sender

Navigate to **DCI > CRVS > Sender Registry** and create a sender:

| Field | Example Value |
|-------|---------------|
| Name | National CRVS |
| Sender ID | `crvs.national.gov` |
| JWKS URL | `https://crvs.gov.example/.well-known/jwks.json` |

Click **Fetch Public Key** to retrieve the CRVS registry's public key for signature verification.

### Step 3: Subscribe to Events

Use the CRVS service to subscribe to vital events:

```python
from odoo.addons.spp_dci_client_crvs.services.crvs_service import CRVSService

# Initialize service
crvs = CRVSService(env, data_source_code="crvs_main")

# Subscribe to birth and death events
subscription_ids = crvs.subscribe_events(["BIRTH", "DEATH"])
```

## Usage

### Verify a Birth Record

```python
from odoo.addons.spp_dci_client_crvs.services.crvs_service import CRVSService

crvs = CRVSService(env, data_source_code="crvs_main")

# Verify by birth registration number
result = crvs.verify_birth(
    identifier_type="BRN",
    identifier_value="2020-12345"
)

if result:
    print(f"Birth verified: {result['person_name']}")
    print(f"Birth date: {result['birth_date']}")
```

### Check Death Status

```python
# Check if person is deceased
is_deceased = crvs.check_death(
    identifier_type="UIN",
    identifier_value="123456789"
)

if is_deceased:
    print("Person has a death record in CRVS")
```

### Process Incoming Notifications

The module includes a callback router that handles incoming CRVS notifications. When a notification arrives:

1. The signature is verified using the sender's public key
2. A `spp.dci.crvs.event` record is created
3. The event is automatically processed:
   - For death events: registrant is disabled
   - For birth events: birth date is updated
   - For marriage/divorce: civil status is updated

### Manual Event Processing

To retry processing a failed event:

```python
# Find failed events
failed_events = env["spp.dci.crvs.event"].search([("state", "=", "error")])

# Retry processing
failed_events.action_retry_processing()
```

## Technical Details

| Property | Value |
|----------|-------|
| Technical Name | `spp_dci_client_crvs` |
| Category | OpenSPP/Integration |
| Version | 19.0.1.0.0 |
| License | LGPL-3 |
| Development Status | Alpha |

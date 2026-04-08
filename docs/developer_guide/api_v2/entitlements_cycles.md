---
openspp:
  doc_status: draft
  products: [core]
---

# Entitlements and Cycles

This guide is for **developers** working with entitlement and cycle data through the OpenSPP API V2 extensions.

## Overview

These two extension modules expose program distribution data:

- **Entitlements** (`spp_api_v2_entitlements`) — Benefits (cash or in-kind) that beneficiaries are entitled to receive
- **Cycles** (`spp_api_v2_cycles`) — Distribution periods within a program

Both modules provide read-only search access. Entitlements and cycles are created through the OpenSPP admin interface or program workflows, not via the API.

## Prerequisites

- Install `spp_api_v2_entitlements` and/or `spp_api_v2_cycles` modules
- API client with `entitlement:read` and/or `cycle:read` scope

## Entitlement Endpoints

### Read Entitlement

```http
GET /api/v2/spp/Entitlement/{identifier}
Authorization: Bearer TOKEN
```

The identifier is the entitlement code (UUID format).

**Response:**

```json
{
  "identifier": "550e8400-e29b-41d4-a716-446655440000",
  "entitlementType": "cash",
  "state": "approved",
  "beneficiary": {
    "reference": "Individual/urn:gov:ph:psa:national-id|PH-123456789",
    "display": "Maria Santos"
  },
  "program": {
    "reference": "Program/4Ps",
    "display": "Pantawid Pamilyang Pilipino Program"
  },
  "cycle": {
    "reference": "Cycle/4Ps-2024-01",
    "display": "January 2024"
  },
  "validPeriod": {
    "start": "2024-01-01",
    "end": "2024-01-31"
  },
  "initialAmount": 5000.00,
  "balance": 5000.00,
  "approvedDate": "2024-01-05",
  "ern": "ENT-2024-00001234",
  "meta": {
    "versionId": "2",
    "lastUpdated": "2024-01-05T10:00:00Z"
  }
}
```

**Response headers:** `ETag` with version ID for caching.

### Search Entitlements

```http
GET /api/v2/spp/Entitlement?beneficiary=urn:gov:ph:psa:national-id|PH-123456789&state=approved
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `beneficiary` | string | Beneficiary identifier (`system\|value` format) |
| `program` | string | Program name |
| `cycle` | string | Cycle name |
| `state` | string | Entitlement state (e.g., `draft`, `approved`, `redeemed`) |
| `entitlementType` | string | `cash` or `inkind` |
| `validFrom` | date | Valid from date filter |
| `validUntil` | date | Valid until date filter |
| `_lastUpdated` | date | Modified since (with prefix: `ge2024-01-01`) |
| `_count` | integer | Results per page (1-100, default 20) |
| `_offset` | integer | Skip N results (default 0) |

**Example: Python**

```python
def get_beneficiary_entitlements(beneficiary_id, token, base_url, state=None):
    """Get entitlements for a beneficiary."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {"beneficiary": beneficiary_id}
    if state:
        params["state"] = state

    response = requests.get(
        f"{base_url}/Entitlement",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Get approved entitlements
result = get_beneficiary_entitlements(
    beneficiary_id="urn:gov:ph:psa:national-id|PH-123456789",
    token=token,
    base_url=base_url,
    state="approved"
)

for entry in result.get("entry", []):
    ent = entry["resource"]
    print(f"  {ent['ern']}: {ent['entitlementType']} - {ent['initialAmount']}")
```

## Cycle Endpoints

### Read Cycle

```http
GET /api/v2/spp/Cycle/{identifier}
Authorization: Bearer TOKEN
```

The identifier is the cycle name (URL-encoded).

**Response:**

```json
{
  "identifier": "4Ps-2024-01",
  "name": "January 2024",
  "sequence": 1,
  "program": {
    "reference": "Program/4Ps",
    "display": "Pantawid Pamilyang Pilipino Program"
  },
  "period": {
    "start": "2024-01-01",
    "end": "2024-01-31"
  },
  "state": "closed",
  "approvedDate": "2024-01-02",
  "approvedBy": "admin",
  "statistics": {
    "membersCount": 15000,
    "entitlementsCount": 15000,
    "paymentsCount": 14500,
    "totalAmount": 75000000.00,
    "currency": "PHP"
  },
  "previousCycle": {
    "reference": "Cycle/4Ps-2023-12"
  },
  "nextCycle": {
    "reference": "Cycle/4Ps-2024-02"
  },
  "meta": {
    "versionId": "5",
    "lastUpdated": "2024-02-01T00:00:00Z"
  }
}
```

### Search Cycles

```http
GET /api/v2/spp/Cycle?program=4Ps&state=active
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `program` | string | Program name filter |
| `state` | string | Cycle state (e.g., `draft`, `active`, `closed`) |
| `startDate` | date | Filter by start date |
| `endDate` | date | Filter by end date |
| `_lastUpdated` | date | Modified since (with prefix) |
| `_count` | integer | Results per page (1-100, default 20) |
| `_offset` | integer | Skip N results (default 0) |

**Example: Python**

```python
def get_program_cycles(program_name, token, base_url, state=None):
    """Get cycles for a program."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {"program": program_name}
    if state:
        params["state"] = state

    response = requests.get(
        f"{base_url}/Cycle",
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()

# Get active cycles
result = get_program_cycles("4Ps", token=token, base_url=base_url, state="active")

for entry in result.get("entry", []):
    cycle = entry["resource"]
    stats = cycle.get("statistics", {})
    print(f"  {cycle['name']}: {stats.get('membersCount', 0)} members, "
          f"{stats.get('totalAmount', 0)} {stats.get('currency', '')}")
```

## Are You Stuck?

**Getting 403 on entitlement/cycle endpoints?**

Your API client needs `entitlement:read` or `cycle:read` scope. Contact your administrator.

**Module not found (404 on endpoints)?**

The extension module may not be installed. Check `GET /metadata` to see which resources are available.

**How do I find the entitlement code (identifier)?**

Entitlement codes are UUIDs assigned when the entitlement is created. Search by beneficiary identifier instead of looking up individual entitlements directly.

**Cycle statistics show zero values?**

Statistics are computed when the cycle is processed. Draft cycles may not have statistics yet.

## Next Steps

- {doc}`resources` - Core Individual, Group, and Program resources
- {doc}`search` - Search and filtering patterns
- {doc}`batch` - Bulk export for multiple entitlements
- {doc}`errors` - Error handling

## See Also

- {doc}`overview` - API V2 design principles
- {doc}`authentication` - OAuth 2.0 setup and scopes

---
openspp:
  doc_status: draft
  products: [core]
---

# Data API

**For: developers**

Push and pull external data for OpenSPP's variable caching system through the Data API extension.

## Overview

The Data API (`spp_api_v2_data`) enables external systems to push and pull variable values into OpenSPP's variable cache. This is used for:

- **Importing data** from ministries (education enrollment, health records, etc.)
- **Syncing variables** from external databases
- **Reading cached values** for reporting or decision-making
- **Invalidating stale data** to trigger recomputation

Data providers are configured in the OpenSPP admin interface with ownership rules — each provider can only push values for variables it owns.

## Prerequisites

- Install `spp_api_v2_data` module
- API client with `data:read` and/or `data:write` scope
- Data provider configured in OpenSPP admin

## Push Data

Send variable values from an external system into OpenSPP's cache.

```http
POST /api/v2/spp/Data/push
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "provider_code": "edu_ministry",
  "values": [
    {
      "subject_external_id": "urn:gov:ph:psa:national-id|PH-123456789",
      "variable": "enrollment_status",
      "value": "enrolled",
      "period_key": "2024-01-01",
      "as_of": "2024-01-15T10:00:00Z"
    },
    {
      "subject_external_id": "urn:gov:ph:psa:national-id|PH-987654321",
      "variable": "enrollment_status",
      "value": "graduated",
      "period_key": "2024-01-01"
    }
  ]
}
```

**Request fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `provider_code` | string | Yes | Registered data provider code |
| `values` | array | Yes | Array of variable values to push |
| `values[].subject_external_id` | string | Yes | Subject identifier (`system\|value` format) |
| `values[].variable` | string | Yes | Variable name (must belong to provider) |
| `values[].value` | any | Yes | The value (number, string, boolean) |
| `values[].period_key` | string | No | Period key (e.g., `2024-01`, `current`) |
| `values[].as_of` | datetime | No | Timestamp when the value was recorded |

**Response:**

```json
{
  "success": true,
  "processed": 2,
  "inserted": 1,
  "updated": 1,
  "errors": []
}
```

If some values fail, errors are returned per-item:

```json
{
  "success": false,
  "processed": 2,
  "inserted": 1,
  "updated": 0,
  "errors": [
    {
      "index": 1,
      "subject_external_id": "urn:gov:ph:psa:national-id|PH-987654321",
      "variable": "enrollment_status",
      "error": "Subject not found"
    }
  ]
}
```

**Example: Python**

```python
def push_variable_data(provider_code, values, token, base_url):
    """Push variable values from external system."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        f"{base_url}/Data/push",
        headers=headers,
        json={"provider_code": provider_code, "values": values}
    )
    response.raise_for_status()
    return response.json()

# Push enrollment data
result = push_variable_data(
    provider_code="edu_ministry",
    values=[
        {
            "subject_external_id": "urn:gov:ph:psa:national-id|PH-123456789",
            "variable": "enrollment_status",
            "value": "enrolled",
            "period_key": "2024-01-01"
        }
    ],
    token=token,
    base_url=base_url
)
print(f"Inserted: {result['inserted']}, Updated: {result['updated']}, Errors: {len(result['errors'])}")
```

## Pull Data

Read cached variable values for specific subjects.

```http
GET /api/v2/spp/Data/pull?variable=enrollment_status&subject_external_ids=urn:gov:ph:psa:national-id|PH-123456789&period_key=current
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `variable` | string | Yes | Variable name to pull |
| `subject_external_ids` | string | Yes | Comma-separated subject identifiers |
| `period_key` | string | No | Period filter (default: `current`) |
| `_count` | integer | No | Max results (1-1000, default 100) |

**Response:**

```json
{
  "total": 1,
  "items": [
    {
      "variable": "enrollment_status",
      "subject_external_id": "urn:gov:ph:psa:national-id|PH-123456789",
      "value": "enrolled",
      "period_key": "current",
      "recorded_at": "2024-01-15T10:00:00",
      "expires_at": "2024-07-15T10:00:00",
      "is_stale": false,
      "source_type": "external"
    }
  ]
}
```

## Invalidate Data

Mark cached values as stale to trigger a refresh.

```http
POST /api/v2/spp/Data/invalidate
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "provider_code": "edu_ministry",
  "variable": "enrollment_status",
  "subject_external_ids": ["urn:gov:ph:psa:national-id|PH-123456789"],
  "period_key": "2024-01-01"
}
```

**Response:**

```json
{
  "success": true,
  "invalidated": 1
}
```

## List Variables

Discover which variables are configured for external data.

```http
GET /api/v2/spp/Data/variables?provider_code=edu_ministry
Authorization: Bearer TOKEN
```

**Query parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `provider_code` | string | Filter by data provider |
| `source_type` | string | Filter by source type (`external`, `computed`, etc.) |
| `_count` | integer | Page size (1-500, default 100) |
| `_lastId` | integer | Cursor for pagination |

**Response:**

```json
{
  "total": 3,
  "items": [
    {
      "name": "enrollment_status",
      "cel_accessor": "enrollment_status",
      "description": "Current school enrollment status",
      "value_type": "string",
      "source_type": "external",
      "cache_strategy": "ttl",
      "period_granularity": "monthly",
      "provider_code": "edu_ministry"
    }
  ],
  "nextPageId": 15
}
```

## Common mistakes

**Push returns "variable not owned by provider"?**

Each variable is owned by a specific data provider. Your provider code must match the variable's configured owner. Contact your administrator.

**Subject not found errors?**

The subject identifier must match an existing registrant. Use the same `system|value` format as the registry (e.g., `urn:gov:ph:psa:national-id|PH-123456789`).

**Pulled values show `is_stale: true`?**

The cached value has expired based on the provider's TTL setting. Push fresh data or wait for scheduled recomputation.

**How do I know which variables I can push?**

Use `GET /Data/variables?provider_code=your_code` to list variables your provider owns.

## What's next

- {doc}`studio_integration` - Studio variables and CEL expressions
- {doc}`resources` - Core API resources
- {doc}`authentication` - OAuth 2.0 setup and scopes

## See also

- {doc}`overview` - API V2 design principles
- {doc}`external_identifiers` - Identifier format for subject resolution

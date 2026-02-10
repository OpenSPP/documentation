---
openspp:
  doc_status: draft
  products: [core]
---

# Bulk Export

This guide covers the bulk export endpoint for retrieving multiple resources efficiently in a single request.

## Overview

The `/$bulk/export` endpoint lets you fetch up to **100 resources** by their identifiers in a single request.

| Operation | Method | Endpoint | Scope Required |
|-----------|--------|----------|----------------|
| Bulk export | POST | `/$bulk/export` | `{type}:read` |

## Request

`````{tab-set}

````{tab-item} HTTP
```http
POST /api/v2/spp/$bulk/export
Authorization: Bearer {token}
Content-Type: application/json

{
  "type": "Individual",
  "identifiers": [
    "urn:gov:ph:psa:national-id|PH-123456789",
    "urn:gov:ph:psa:national-id|PH-987654321",
    "urn:gov:ph:psa:national-id|PH-555555555"
  ],
  "_elements": "name,birthDate,gender"
}
```
````

````{tab-item} cURL
```bash
curl -X POST https://api.openspp.org/api/v2/spp/\$bulk/export \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "Individual",
    "identifiers": [
      "urn:gov:ph:psa:national-id|PH-123456789",
      "urn:gov:ph:psa:national-id|PH-987654321",
      "urn:gov:ph:psa:national-id|PH-555555555"
    ],
    "_elements": "name,birthDate,gender"
  }'
```
````

````{tab-item} Python
```python
import requests

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
data = {
    "type": "Individual",
    "identifiers": [
        "urn:gov:ph:psa:national-id|PH-123456789",
        "urn:gov:ph:psa:national-id|PH-987654321",
        "urn:gov:ph:psa:national-id|PH-555555555"
    ],
    "_elements": "name,birthDate,gender"
}
response = requests.post(
    f"{base_url}/$bulk/export",
    headers=headers,
    json=data
)
response.raise_for_status()
result = response.json()
print(f"Exported {result['successful']}/{result['total']} records")
```
````

````{tab-item} JavaScript
```javascript
const data = {
  type: "Individual",
  identifiers: [
    "urn:gov:ph:psa:national-id|PH-123456789",
    "urn:gov:ph:psa:national-id|PH-987654321",
    "urn:gov:ph:psa:national-id|PH-555555555"
  ],
  _elements: "name,birthDate,gender"
};
const response = await fetch(`${baseUrl}/$bulk/export`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${token}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify(data)
});
const result = await response.json();
console.log(`Exported ${result.successful}/${result.total} records`);
```
````

`````

## Response

```json
{
  "total": 3,
  "successful": 2,
  "failed": 1,
  "items": [
    {
      "identifier": "urn:gov:ph:psa:national-id|PH-123456789",
      "status": "success",
      "resource": {
        "type": "Individual",
        "identifier": [
          { "system": "urn:gov:ph:psa:national-id", "value": "PH-123456789" }
        ],
        "name": { "family": "SANTOS", "given": "Maria" },
        "birthDate": "1985-03-15"
      }
    },
    {
      "identifier": "urn:gov:ph:psa:national-id|PH-555555555",
      "status": "not_found",
      "error": "Individual not found"
    }
  ]
}
```

### Item Status Values

| Status | Description |
|--------|-------------|
| `success` | Resource found and returned |
| `not_found` | No resource exists with this identifier |
| `access_denied` | Consent/permissions prevent access |
| `error` | Unexpected error |

## Next Steps

- {doc}`individuals` -- Individual resource operations
- {doc}`groups` -- Group resource operations
- {doc}`search` -- Finding resources by criteria

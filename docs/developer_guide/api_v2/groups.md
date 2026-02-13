---
openspp:
  doc_status: draft
  products: [core]
---

# Working with Groups

This guide covers household and group management, including membership operations like adding/removing members, merging and splitting groups.

## Overview

The `Group` resource represents a household, family, organization, or other grouping of individuals.

| Operation | Method | Endpoint | Scope Required |
|-----------|--------|----------|----------------|
| Search | GET | `/Group` | `group:read` |
| Read | GET | `/Group/{identifier}` | `group:read` |
| Create | POST | `/Group` | `group:create` |
| Full update | PUT | `/Group/{identifier}` | `group:update` |
| Partial update | PATCH | `/Group/{identifier}` | `group:update` |
| Add member | POST | `/Group/{identifier}/$add-member` | `group:update` |
| Remove member | POST | `/Group/{identifier}/$remove-member` | `group:update` |
| Update member | PATCH | `/Group/{identifier}/member/{individual}` | `group:update` |
| Merge groups | POST | `/Group/$merge` | `group:update` |
| Split group | POST | `/Group/{identifier}/$split` | `group:create`, `group:update` |
| Membership history | GET | `/Group/{identifier}/membership-history` | `group:read` |

## Group Data Model

```json
{
  "type": "Group",
  "identifier": [
    { "system": "urn:openspp:group", "value": "HH-2024-001" }
  ],
  "active": true,
  "groupType": "household",
  "name": "Santos Household",
  "quantity": 4,
  "member": [
    {
      "entity": {
        "reference": "Individual/urn:gov:ph:psa:national-id|PH-123",
        "display": "Maria Santos"
      },
      "role": {
        "coding": [
          { "system": "urn:openspp:vocab:relationship", "code": "head", "display": "Head of Household" }
        ]
      },
      "period": { "start": "2024-01-01" },
      "inactive": false
    }
  ]
}
```

```{important}
Groups use `groupType` (not `type`) for the group classification. The `type` field is reserved for the resource discriminator (`"Group"`).
```

### Common Role Codes

| Code | Display |
|------|---------|
| `head` | Head of Household |
| `spouse` | Spouse |
| `child` | Child |
| `parent` | Parent |
| `sibling` | Sibling |
| `other` | Other Relative |

## Add a Member to a Group

`````{tab-set}

````{tab-item} HTTP
```http
POST /api/v2/spp/Group/urn:openspp:group|HH-2024-001/$add-member
Authorization: Bearer {token}
Content-Type: application/json

{
  "entity": {
    "reference": "Individual/urn:gov:ph:psa:national-id|PH-789",
    "display": "Ana Santos"
  },
  "role": {
    "coding": [
      { "system": "urn:openspp:vocab:relationship", "code": "child", "display": "Child" }
    ]
  },
  "startDate": "2024-06-01"
}
```
````

````{tab-item} cURL
```bash
curl -X POST https://api.openspp.org/api/v2/spp/Group/urn:openspp:group|HH-2024-001/\$add-member \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entity": {
      "reference": "Individual/urn:gov:ph:psa:national-id|PH-789",
      "display": "Ana Santos"
    },
    "role": {
      "coding": [
        {"system": "urn:openspp:vocab:relationship", "code": "child", "display": "Child"}
      ]
    },
    "startDate": "2024-06-01"
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
    "entity": {
        "reference": "Individual/urn:gov:ph:psa:national-id|PH-789",
        "display": "Ana Santos"
    },
    "role": {
        "coding": [
            {"system": "urn:openspp:vocab:relationship", "code": "child", "display": "Child"}
        ]
    },
    "startDate": "2024-06-01"
}
response = requests.post(
    f"{base_url}/Group/urn:openspp:group|HH-2024-001/$add-member",
    headers=headers,
    json=data
)
response.raise_for_status()
```
````

````{tab-item} JavaScript
```javascript
const data = {
  entity: {
    reference: "Individual/urn:gov:ph:psa:national-id|PH-789",
    display: "Ana Santos"
  },
  role: {
    coding: [
      { system: "urn:openspp:vocab:relationship", code: "child", display: "Child" }
    ]
  },
  startDate: "2024-06-01"
};
const response = await fetch(
  `${baseUrl}/Group/urn:openspp:group|HH-2024-001/$add-member`,
  {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  }
);
```
````

`````

## Remove a Member from a Group

`````{tab-set}

````{tab-item} HTTP
```http
POST /api/v2/spp/Group/urn:openspp:group|HH-2024-001/$remove-member
Authorization: Bearer {token}
Content-Type: application/json

{
  "entity": {
    "reference": "Individual/urn:gov:ph:psa:national-id|PH-789"
  },
  "endedDate": "2024-12-31",
  "reason": "Moved to another household"
}
```
````

````{tab-item} cURL
```bash
curl -X POST https://api.openspp.org/api/v2/spp/Group/urn:openspp:group|HH-2024-001/\$remove-member \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entity": {
      "reference": "Individual/urn:gov:ph:psa:national-id|PH-789"
    },
    "endedDate": "2024-12-31",
    "reason": "Moved to another household"
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
    "entity": {
        "reference": "Individual/urn:gov:ph:psa:national-id|PH-789"
    },
    "endedDate": "2024-12-31",
    "reason": "Moved to another household"
}
response = requests.post(
    f"{base_url}/Group/urn:openspp:group|HH-2024-001/$remove-member",
    headers=headers,
    json=data
)
response.raise_for_status()
```
````

````{tab-item} JavaScript
```javascript
const data = {
  entity: {
    reference: "Individual/urn:gov:ph:psa:national-id|PH-789"
  },
  endedDate: "2024-12-31",
  reason: "Moved to another household"
};
const response = await fetch(
  `${baseUrl}/Group/urn:openspp:group|HH-2024-001/$remove-member`,
  {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  }
);
```
````

`````

## Are You Stuck?

**What is the difference between `type` and `groupType`?**

`type` is always `"Group"` (the resource discriminator). `groupType` is the classification (`household`, `family`, `organization`, `other`).

## Next Steps

- {doc}`individuals` -- Manage individual registrants
- {doc}`programs` -- Enroll groups in programs
- {doc}`batch` -- Create groups with members atomically

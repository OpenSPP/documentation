---
openspp:
  doc_status: draft
  products: [core]
---

# Working with Individuals

This guide covers all operations for managing individual registrants through the OpenSPP API V2.

## Overview

The `Individual` resource represents a single person in the social protection registry. You can read, create, update, and search for individuals using the endpoints below.

| Operation | Method | Endpoint | Scope Required |
|-----------|--------|----------|----------------|
| Search | GET | `/Individual` | `individual:read` |
| Read | GET | `/Individual/{identifier}` | `individual:read` |
| Create | POST | `/Individual` | `individual:create` |
| Full update | PUT | `/Individual/{identifier}` | `individual:update` |
| Partial update | PATCH | `/Individual/{identifier}` | `individual:update` |
| Get groups | GET | `/Individual/{identifier}/groups` | `individual:read` |

## Individual Data Model

A complete Individual resource includes the following fields:

```json
{
  "type": "Individual",
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-123456789"
    }
  ],
  "active": true,
  "name": {
    "family": "SANTOS",
    "given": "Maria",
    "middle": "Dela Cruz",
    "prefix": "Mrs",
    "suffix": null,
    "text": "SANTOS, Maria Dela Cruz"
  },
  "birthDate": "1985-03-15",
  "birthDateEstimated": false,
  "gender": {
    "coding": [
      {
        "system": "urn:iso:std:iso:5218",
        "code": "2",
        "display": "Female"
      }
    ]
  },
  "telecom": [
    {
      "system": "phone",
      "value": "+639171234567",
      "use": "mobile",
      "rank": 1
    },
    {
      "system": "email",
      "value": "maria.santos@example.com",
      "use": "home"
    }
  ],
  "address": [
    {
      "type": "physical",
      "text": "123 Rizal St, Barangay 1, Manila",
      "line": ["123 Rizal St", "Barangay 1"],
      "city": "Manila",
      "district": "Tondo",
      "state": "Metro Manila",
      "postalCode": "1000",
      "country": "PH"
    }
  ],
  "meta": {
    "versionId": "3",
    "lastUpdated": "2024-11-28T10:30:00Z",
    "source": "urn:openspp:api-client:field-app"
  }
}
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Always `"Individual"` |
| `identifier` | array | Yes | At least one external identifier (see {doc}`external_identifiers`) |
| `active` | boolean | No | Whether record is active (default: `true`) |
| `name` | object | No | Human name with `family`, `given`, `middle`, `prefix`, `suffix`, `text` |
| `birthDate` | string | No | Birth date in `YYYY-MM-DD` format |
| `birthDateEstimated` | boolean | No | `true` if the birth date is an estimate |
| `gender` | CodeableConcept | No | Gender using ISO 5218 coding |
| `telecom` | array | No | Contact points (phone, email, fax, url, sms) |
| `address` | array | No | Physical or postal addresses |
| `photo` | string | No | Base64-encoded image |
| `groupMembership` | array | Read-only | Group memberships (populated on read) |
| `extension` | object | No | Module-specific extension data |
| `meta` | object | Read-only | Version ID, last updated timestamp, source system |

### Gender Codes (ISO 5218)

| Code | Display | Description |
|------|---------|-------------|
| `0` | Not known | Gender is not recorded |
| `1` | Male | Male |
| `2` | Female | Female |
| `9` | Not applicable | Not applicable |

## Read an Individual

Fetch a single individual by their external identifier.

`````{tab-set}

````{tab-item} HTTP
```http
GET /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789
Authorization: Bearer {token}
```
````

````{tab-item} cURL
```bash
curl https://api.openspp.org/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(
    f"{base_url}/Individual/urn:gov:ph:psa:national-id|PH-123456789",
    headers=headers
)
response.raise_for_status()
individual = response.json()
print(f"Name: {individual['name']['given']} {individual['name']['family']}")
```
````

````{tab-item} JavaScript
```javascript
const response = await fetch(
  `${baseUrl}/Individual/urn:gov:ph:psa:national-id|PH-123456789`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const individual = await response.json();
console.log(`Name: ${individual.name.given} ${individual.name.family}`);
```
````

`````

**Optional query parameters:**

| Parameter | Description | Example |
|-----------|-------------|---------|
| `_elements` | Return only specific fields | `name,birthDate,gender` |
| `_extensions` | Include extension data | `farmer,disability` or `*` for all |

**Response headers:**

| Header | Value | Meaning |
|--------|-------|---------|
| `ETag` | `"3"` | Version ID for optimistic locking |
| `X-Consent-Status` | `active` | Consent was verified |
| `X-Consent-Scope` | `individual:all` | Full data access granted |

## Search Individuals

Search across the registry with query parameters. Results use the `SearchResult` format.

`````{tab-set}

````{tab-item} HTTP
```http
GET /api/v2/spp/Individual?name=Santos&_count=20&_offset=0
Authorization: Bearer {token}
```
````

````{tab-item} cURL
```bash
curl "https://api.openspp.org/api/v2/spp/Individual?name=Santos&_count=20&_offset=0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(
    f"{base_url}/Individual",
    headers=headers,
    params={"name": "Santos", "_count": 20, "_offset": 0}
)
response.raise_for_status()
results = response.json()
print(f"Found {results['meta']['total']} individuals")
```
````

````{tab-item} JavaScript
```javascript
const params = new URLSearchParams({
  name: "Santos", _count: "20", _offset: "0"
});
const response = await fetch(
  `${baseUrl}/Individual?${params}`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const results = await response.json();
console.log(`Found ${results.meta.total} individuals`);
```
````

`````

**Search parameters:**

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `identifier` | string | Identifier in `system\|value` format | `urn:gov:ph:psa:national-id\|PH-123` |
| `name` | string | Name search (case-insensitive, contains) | `Santos` |
| `birthdate` | string | Birth date with prefix (`eq`, `ge`, `le`, `gt`, `lt`) | `ge1990-01-01` |
| `gender` | string | Gender in `system\|code` format | `urn:iso:std:iso:5218\|2` |
| `address` | string | Address text search (any field) | `Manila` |
| `group` | string | Group identifier, or `none` for orphans | `urn:openspp:group\|HH-001` |
| `membership-role` | string | Role code within a group | `head` |
| `_lastUpdated` | string | Filter by modification date | `ge2024-01-01` |
| `_count` | integer | Page size (default: 20, max: 100) | `50` |
| `_offset` | integer | Records to skip | `0` |
| `_sort` | string | Sort field (prefix `-` for descending) | `-birthDate` |
| `_elements` | string | Comma-separated fields to return | `name,birthDate` |
| `_extensions` | string | Extensions to include | `farmer` or `*` |

**Response (HTTP 200):**

```json
{
  "data": [
    {
      "type": "Individual",
      "identifier": [
        { "system": "urn:gov:ph:psa:national-id", "value": "PH-123" }
      ],
      "name": { "family": "SANTOS", "given": "Maria" },
      "birthDate": "1985-03-15"
    }
  ],
  "meta": {
    "total": 47,
    "count": 1,
    "offset": 0
  },
  "links": {
    "self": "/api/v2/spp/Individual?name=Santos&_count=20",
    "next": "/api/v2/spp/Individual?name=Santos&_count=20&_offset=20",
    "prev": null
  }
}
```

## Create an Individual

Register a new person in the system.

`````{tab-set}

````{tab-item} HTTP
```http
POST /api/v2/spp/Individual
Authorization: Bearer {token}
Content-Type: application/json

{
  "type": "Individual",
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-NEW-001"
    }
  ]
}
```
````

````{tab-item} cURL
```bash
curl -X POST https://api.openspp.org/api/v2/spp/Individual \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "Individual",
    "identifier": [
      {"system": "urn:gov:ph:psa:national-id", "value": "PH-NEW-001"}
    ]
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
    "identifier": [
        {"system": "urn:gov:ph:psa:national-id", "value": "PH-NEW-001"}
    ]
}
response = requests.post(
    f"{base_url}/Individual",
    headers=headers,
    json=data
)
response.raise_for_status()
created = response.json()
print(f"Created: {created['identifier'][0]['value']}")
```
````

````{tab-item} JavaScript
```javascript
const data = {
  type: "Individual",
  identifier: [
    { system: "urn:gov:ph:psa:national-id", value: "PH-NEW-001" }
  ]
};
const response = await fetch(`${baseUrl}/Individual`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${token}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify(data)
});
const created = await response.json();
console.log(`Created: ${created.identifier[0].value}`);
```
````

`````

**Success response (HTTP 201):**

The response body contains the created resource. The `Location` header contains the URL for the new resource.

## Partial Update (PATCH)

Update only specific fields without replacing the entire resource. Uses JSON Merge Patch ([RFC 7396](https://datatracker.ietf.org/doc/html/rfc7396)).

**Rules:**
- Only specified fields are updated
- Omitted fields remain unchanged
- Set a field to `null` to clear it

`````{tab-set}

````{tab-item} HTTP
```http
PATCH /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123
Authorization: Bearer {token}
Content-Type: application/json
If-Match: "3"

{
  "name": {
    "given": "Maria Elena"
  },
  "telecom": [
    {
      "system": "phone",
      "value": "+639179999999",
      "use": "mobile",
      "rank": 1
    }
  ]
}
```
````

````{tab-item} cURL
```bash
curl -X PATCH https://api.openspp.org/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -H 'If-Match: "3"' \
  -d '{
    "name": {"given": "Maria Elena"},
    "telecom": [
      {"system": "phone", "value": "+639179999999", "use": "mobile", "rank": 1}
    ]
  }'
```
````

````{tab-item} Python
```python
import requests

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "If-Match": '"3"'
}
data = {
    "name": {"given": "Maria Elena"},
    "telecom": [
        {"system": "phone", "value": "+639179999999", "use": "mobile", "rank": 1}
    ]
}
response = requests.patch(
    f"{base_url}/Individual/urn:gov:ph:psa:national-id|PH-123",
    headers=headers,
    json=data
)
response.raise_for_status()
updated = response.json()
print(f"Updated to version: {updated['meta']['versionId']}")
```
````

````{tab-item} JavaScript
```javascript
const data = {
  name: { given: "Maria Elena" },
  telecom: [
    { system: "phone", value: "+639179999999", use: "mobile", rank: 1 }
  ]
};
const response = await fetch(
  `${baseUrl}/Individual/urn:gov:ph:psa:national-id|PH-123`,
  {
    method: "PATCH",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json",
      "If-Match": '"3"'
    },
    body: JSON.stringify(data)
  }
);
const updated = await response.json();
console.log(`Updated to version: ${updated.meta.versionId}`);
```
````

`````

```{important}
Always include the `If-Match` header with the current `versionId` (from the `ETag` response header or `meta.versionId`). This prevents overwriting changes made by another client. If the version does not match, the API returns **409 Conflict**.
```

## Get Group Memberships

Find all groups an individual belongs to.

`````{tab-set}

````{tab-item} HTTP
```http
GET /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123/groups
Authorization: Bearer {token}
```
````

````{tab-item} cURL
```bash
curl https://api.openspp.org/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123/groups \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
import requests

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(
    f"{base_url}/Individual/urn:gov:ph:psa:national-id|PH-123/groups",
    headers=headers
)
response.raise_for_status()
groups = response.json()
```
````

````{tab-item} JavaScript
```javascript
const response = await fetch(
  `${baseUrl}/Individual/urn:gov:ph:psa:national-id|PH-123/groups`,
  { headers: { "Authorization": `Bearer ${token}` } }
);
const groups = await response.json();
```
````

`````

## Working with Extensions

Extensions add module-specific fields to individuals (for example, farmer registry data or disability information).

### Requesting Extensions

```bash
# Request a specific extension
curl ".../Individual/urn:gov:ph:psa:national-id|PH-123?_extensions=farmer"

# Request all available extensions
curl ".../Individual/urn:gov:ph:psa:national-id|PH-123?_extensions=*"
```

See {doc}`studio_integration` for details on Studio custom fields.

## Are You Stuck?

**Getting 404 Not Found?**

Check that the identifier is correctly formatted as `{system}|{value}` and that the system namespace is URL-encoded in the path. See {doc}`external_identifiers`.

**Getting 409 Conflict on update?**

Another client modified the record after you read it. Fetch the latest version (note the new `ETag` / `versionId`), merge your changes, and retry.

**Getting empty responses or only identifiers?**

This usually means no consent is on file for your organization. Check the `X-Consent-Status` response header. See {doc}`consent`.

## Next Steps

- {doc}`groups` -- Manage households and group membership
- {doc}`search` -- Advanced search and filtering
- {doc}`batch` -- Create or update multiple individuals at once
- {doc}`errors` -- Handle errors gracefully

---
openspp:
  doc_status: draft
  products: [core]
---

# Quick Start Guide

Get up and running with the OpenSPP API V2 in minutes. This guide walks you through authentication, your first API call, and common integration patterns.

## What You Will Need

Before you begin, make sure you have:

- An OpenSPP instance (production, staging, or local development)
- API client credentials (`client_id` and `client_secret`) from your administrator
- A tool for making HTTP requests (curl, Postman, or your programming language of choice)

```{tip}
Download the [Postman collection](postman_collection.json) for a pre-built set of API requests you can import and start testing immediately.
```

## Step 1: Get Your Access Token

All API requests require a Bearer token. Obtain one using your client credentials:

`````{tab-set}

````{tab-item} curl
```bash
curl -X POST https://api.openspp.org/api/v2/spp/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "client_credentials",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret"
  }'
```
````

````{tab-item} Python
```python
import requests

response = requests.post(
    "https://api.openspp.org/api/v2/spp/oauth/token",
    json={
        "grant_type": "client_credentials",
        "client_id": "your-client-id",
        "client_secret": "your-client-secret"
    }
)
token_data = response.json()
TOKEN = token_data["access_token"]
print(f"Token expires in {token_data['expires_in']} seconds")
```
````

````{tab-item} JavaScript
```javascript
const response = await fetch(
  "https://api.openspp.org/api/v2/spp/oauth/token",
  {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      grant_type: "client_credentials",
      client_id: "your-client-id",
      client_secret: "your-client-secret"
    })
  }
);
const { access_token, expires_in } = await response.json();
console.log(`Token expires in ${expires_in} seconds`);
```
````

`````

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "individual:read individual:create group:read"
}
```

| Field | Description |
|-------|-------------|
| `access_token` | JWT token to include in all subsequent requests |
| `token_type` | Always `Bearer` |
| `expires_in` | Token lifetime in seconds (default: 3600 = 1 hour) |
| `scope` | Permissions granted to your client |

```{important}
Tokens expire after 1 hour. Your application should request a new token before the current one expires. See {doc}`authentication` for a token refresh strategy.
```

## Step 2: Make Your First API Call

Use your token to fetch an individual registrant:

`````{tab-set}

````{tab-item} curl
```bash
curl https://api.openspp.org/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.get(
    "https://api.openspp.org/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789",
    headers=headers
)
individual = response.json()
print(f"Name: {individual['name']['given']} {individual['name']['family']}")
```
````

````{tab-item} JavaScript
```javascript
const response = await fetch(
  "https://api.openspp.org/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789",
  {
    headers: { "Authorization": `Bearer ${access_token}` }
  }
);
const individual = await response.json();
console.log(`Name: ${individual.name.given} ${individual.name.family}`);
```
````

`````

**Response:**

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
    "text": "SANTOS, Maria"
  },
  "birthDate": "1985-03-15",
  "gender": {
    "coding": [
      {
        "system": "urn:iso:std:iso:5218",
        "code": "2",
        "display": "Female"
      }
    ]
  },
  "meta": {
    "versionId": "3",
    "lastUpdated": "2024-11-28T10:30:00Z"
  }
}
```

```{note}
All resources use `type` (not `resourceType`) as the discriminator field. This follows the ADR-019 modernized response format.
```

## Step 3: Search for Individuals

Search across the registry using query parameters:

`````{tab-set}

````{tab-item} cURL
```bash
curl "https://api.openspp.org/api/v2/spp/Individual?name=Santos&_count=10" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
````

````{tab-item} Python
```python
headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.get(
    "https://api.openspp.org/api/v2/spp/Individual",
    headers=headers,
    params={"name": "Santos", "_count": 10}
)
results = response.json()
print(f"Found {results['meta']['total']} individuals")
for item in results["data"]:
    print(f"  {item['name']['given']} {item['name']['family']}")
```
````

````{tab-item} JavaScript
```javascript
const response = await fetch(
  "https://api.openspp.org/api/v2/spp/Individual?name=Santos&_count=10",
  {
    headers: { "Authorization": `Bearer ${access_token}` }
  }
);
const results = await response.json();
console.log(`Found ${results.meta.total} individuals`);
results.data.forEach(item => {
  console.log(`  ${item.name.given} ${item.name.family}`);
});
```
````

`````

**Response -- SearchResult format:**

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
    },
    {
      "type": "Individual",
      "identifier": [
        { "system": "urn:gov:ph:psa:national-id", "value": "PH-456" }
      ],
      "name": { "family": "SANTOS", "given": "Juan" },
      "birthDate": "1988-07-22"
    }
  ],
  "meta": {
    "total": 47,
    "count": 2,
    "offset": 0
  },
  "links": {
    "self": "/api/v2/spp/Individual?name=Santos&_count=2",
    "next": "/api/v2/spp/Individual?name=Santos&_count=2&_offset=2",
    "prev": null
  }
}
```

| Field | Description |
|-------|-------------|
| `data[]` | Array of matching resources (no wrapper objects) |
| `meta.total` | Total number of matches across all pages |
| `meta.count` | Number of results in this response |
| `meta.offset` | Current page offset |
| `links.next` | URL for the next page (`null` if on the last page) |
| `links.prev` | URL for the previous page (`null` if on the first page) |

## Step 4: Create a New Individual

Register a new person in the system:

`````{tab-set}

````{tab-item} cURL
```bash
curl -X POST https://api.openspp.org/api/v2/spp/Individual \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "Individual",
    "identifier": [
      {
        "system": "urn:gov:ph:psa:national-id",
        "value": "PH-NEW-001"
      }
    ],
    "active": true,
    "name": {
      "family": "REYES",
      "given": "Ana"
    },
    "birthDate": "1992-08-10",
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
        "use": "mobile"
      }
    ]
  }'
```
````

````{tab-item} Python
```python
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "type": "Individual",
    "identifier": [
        {"system": "urn:gov:ph:psa:national-id", "value": "PH-NEW-001"}
    ],
    "active": True,
    "name": {"family": "REYES", "given": "Ana"},
    "birthDate": "1992-08-10",
    "gender": {
        "coding": [
            {"system": "urn:iso:std:iso:5218", "code": "2", "display": "Female"}
        ]
    },
    "telecom": [
        {"system": "phone", "value": "+639171234567", "use": "mobile"}
    ]
}
response = requests.post(
    "https://api.openspp.org/api/v2/spp/Individual",
    headers=headers,
    json=data
)
created = response.json()
print(f"Created: {created['name']['text']}")
```
````

````{tab-item} JavaScript
```javascript
const data = {
  type: "Individual",
  identifier: [
    { system: "urn:gov:ph:psa:national-id", value: "PH-NEW-001" }
  ],
  active: true,
  name: { family: "REYES", given: "Ana" },
  birthDate: "1992-08-10",
  gender: {
    coding: [
      { system: "urn:iso:std:iso:5218", code: "2", display: "Female" }
    ]
  },
  telecom: [
    { system: "phone", value: "+639171234567", use: "mobile" }
  ]
};
const response = await fetch(
  "https://api.openspp.org/api/v2/spp/Individual",
  {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${access_token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  }
);
const created = await response.json();
console.log(`Created: ${created.name.text}`);
```
````

`````

**Success response (HTTP 201 Created):**

```json
{
  "type": "Individual",
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-NEW-001"
    }
  ],
  "active": true,
  "name": {
    "family": "REYES",
    "given": "Ana",
    "text": "REYES, Ana"
  },
  "birthDate": "1992-08-10",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2024-11-28T14:00:00Z",
    "source": "urn:openspp:api-client:your-client-id"
  }
}
```

**Error response (HTTP 422 Validation Error):**

```json
{
  "type": "urn:openspp:error:validation",
  "title": "Validation Error",
  "status": 422,
  "detail": "Request data contains validation errors",
  "instance": "/api/v2/spp/Individual",
  "errors": [
    {
      "field": "identifier",
      "code": "required",
      "message": "At least one identifier is required"
    }
  ]
}
```

## Common Integration Scenario: Mobile Data Collection

A typical workflow for a mobile data collection app (such as ODK, KoboToolbox, or a custom app) follows this pattern:

```
Mobile App                          OpenSPP API
    |                                    |
    |--- 1. Authenticate --------------->|
    |<-- Access token -------------------|
    |                                    |
    |--- 2. Search for individual ------>|
    |<-- Individual data (or not found) -|
    |                                    |
    |--- 3a. Create new individual ----->|  (if not found)
    |<-- Created individual -------------|
    |                                    |
    |--- 3b. Update existing ----------->|  (if found)
    |<-- Updated individual -------------|
    |                                    |
    |--- 4. Create household group ----->|
    |<-- Created group ------------------|
    |                                    |
    |--- 5. Add member to group -------->|
    |<-- Membership confirmed -----------|
```

### Python: Complete Mobile Sync Example

```python
import requests

class OpenSPPSync:
    """Sync data from a mobile collection app to OpenSPP."""

    def __init__(self, base_url, client_id, client_secret):
        self.base_url = base_url
        self.client_id = client_id
        self.token = None
        self._authenticate(client_secret)

    def _authenticate(self, client_secret):
        """Get access token."""
        resp = requests.post(
            f"{self.base_url}/oauth/token",
            json={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": client_secret
            }
        )
        resp.raise_for_status()
        self.token = resp.json()["access_token"]

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def find_individual(self, id_system, id_value):
        """Search for an individual by identifier. Returns None if not found."""
        resp = requests.get(
            f"{self.base_url}/Individual",
            headers=self._headers(),
            params={"identifier": f"{id_system}|{id_value}"}
        )
        resp.raise_for_status()
        result = resp.json()
        if result["meta"]["total"] > 0:
            return result["data"][0]
        return None

    def create_individual(self, data):
        """Create a new individual."""
        resp = requests.post(
            f"{self.base_url}/Individual",
            headers=self._headers(),
            json=data
        )
        resp.raise_for_status()
        return resp.json()

    def sync_form_submission(self, form_data):
        """
        Sync a single form submission from a mobile app.

        Args:
            form_data: Dict with keys: national_id, given_name, family_name,
                       birth_date, gender_code, phone
        """
        id_system = "urn:gov:ph:psa:national-id"
        id_value = form_data["national_id"]

        # Step 1: Check if individual already exists
        existing = self.find_individual(id_system, id_value)

        if existing:
            print(f"Found existing: {existing['name']['text']}")
            return existing

        # Step 2: Create new individual
        new_individual = {
            "type": "Individual",
            "identifier": [
                {"system": id_system, "value": id_value}
            ],
            "name": {
                "given": form_data["given_name"],
                "family": form_data["family_name"]
            },
            "birthDate": form_data["birth_date"],
            "gender": {
                "coding": [{
                    "system": "urn:iso:std:iso:5218",
                    "code": form_data["gender_code"]
                }]
            },
            "telecom": [{
                "system": "phone",
                "value": form_data["phone"],
                "use": "mobile"
            }]
        }

        created = self.create_individual(new_individual)
        print(f"Created: {created['name']['text']}")
        return created


# Usage
sync = OpenSPPSync(
    base_url="https://api.openspp.org/api/v2/spp",
    client_id="mobile-collection-app",
    client_secret="your-secret"
)

# Simulate form submissions from a mobile app
submissions = [
    {
        "national_id": "PH-2024-001",
        "given_name": "Maria",
        "family_name": "SANTOS",
        "birth_date": "1985-03-15",
        "gender_code": "2",
        "phone": "+639171234567"
    },
    {
        "national_id": "PH-2024-002",
        "given_name": "Juan",
        "family_name": "SANTOS",
        "birth_date": "1983-11-20",
        "gender_code": "1",
        "phone": "+639179876543"
    }
]

for submission in submissions:
    result = sync.sync_form_submission(submission)
```

## Key Concepts to Remember

### External Identifiers

OpenSPP never exposes database IDs. Every resource is identified by a `system|value` pair:

```
urn:gov:ph:psa:national-id|PH-123456789
|_________________________| |__________|
       System (namespace)       Value
```

See {doc}`external_identifiers` for full details.

### Consent-Based Access

API responses may be filtered based on registrant consent. Check the response headers:

| Header | Meaning |
|--------|---------|
| `X-Consent-Status: active` | Full data access granted |
| `X-Consent-Status: no_consent` | Only identifiers returned |
| `X-Consent-Status: scope_mismatch` | Partial data returned |

See {doc}`consent` for full details.

### Error Handling

All errors use the RFC 9457 ProblemDetail format:

```json
{
  "type": "urn:openspp:error:not-found",
  "title": "Not Found",
  "status": 404,
  "detail": "Individual not found with identifier national-id|PH-999"
}
```

See {doc}`errors` for complete error reference.

## API Base URLs

| Environment | URL |
|-------------|-----|
| Production | `https://api.openspp.org/api/v2/spp` |
| Staging | `https://staging-api.openspp.org/api/v2/spp` |
| Development | `http://localhost:8069/api/v2/spp` |

## What to Read Next

| Your Goal | Read This |
|-----------|-----------|
| Understand API design principles | {doc}`overview` |
| Set up secure authentication | {doc}`authentication` |
| Work with individual registrants | {doc}`individuals` |
| Manage households and groups | {doc}`groups` |
| Query programs and enrollments | {doc}`programs` |
| Search and filter large datasets | {doc}`search` |
| Create multiple records at once | {doc}`batch` |
| Export data in bulk | {doc}`bulk_export` |
| Handle errors properly | {doc}`errors` |
| Use Studio custom fields | {doc}`studio_integration` |

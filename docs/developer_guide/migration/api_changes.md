---
openspp:
  doc_status: draft
---

# API Changes

This guide is for **developers** migrating API integrations and REST endpoints from OpenSPP V1 to V2.

## Overview

V2 changes API endpoints to match the new namespace:

- Endpoint paths: `/api/v1/g2p/*` → `/api/v2/spp/*`
- Model references in payloads
- Authentication (enhanced OAuth 2.0)
- External identifiers (UUIDs instead of DB IDs)

## Endpoint Path Changes

### Registry API Endpoints

| V1 Endpoint | V2 Endpoint | Description |
|-------------|-------------|-------------|
| `GET /api/v1/g2p/registry/registrant` | `GET /api/v2/spp/registry/registrant` | List registrants |
| `GET /api/v1/g2p/registry/registrant/{id}` | `GET /api/v2/spp/registry/registrant/{ext_id}` | Get registrant (now uses UUID) |
| `POST /api/v1/g2p/registry/registrant` | `POST /api/v2/spp/registry/registrant` | Create registrant |
| `PUT /api/v1/g2p/registry/registrant/{id}` | `PUT /api/v2/spp/registry/registrant/{ext_id}` | Update registrant |

### Program API Endpoints

| V1 Endpoint | V2 Endpoint | Description |
|-------------|-------------|-------------|
| `GET /api/v1/g2p/programs` | `GET /api/v2/spp/programs` | List programs |
| `GET /api/v1/g2p/programs/{id}` | `GET /api/v2/spp/programs/{ext_id}` | Get program |
| `POST /api/v1/g2p/programs/{id}/enroll` | `POST /api/v2/spp/programs/{ext_id}/enroll` | Enroll beneficiary |
| `GET /api/v1/g2p/programs/{id}/cycles` | `GET /api/v2/spp/programs/{ext_id}/cycles` | List program cycles |

### Entitlement API Endpoints

| V1 Endpoint | V2 Endpoint | Description |
|-------------|-------------|-------------|
| `GET /api/v1/g2p/entitlements` | `GET /api/v2/spp/entitlements` | List entitlements |
| `GET /api/v1/g2p/entitlements/{id}` | `GET /api/v2/spp/entitlements/{ext_id}` | Get entitlement |
| `POST /api/v1/g2p/entitlements/{id}/approve` | `POST /api/v2/spp/entitlements/{ext_id}/approve` | Approve entitlement |

## Request/Response Changes

### Database IDs → External Identifiers

**V1 used database IDs (integers):**

```json
// V1 Request
GET /api/v1/g2p/registry/registrant/42

// V1 Response
{
  "id": 42,
  "name": "John Doe",
  "program_id": 5
}
```

**V2 uses external IDs (UUIDs):**

```json
// V2 Request
GET /api/v2/spp/registry/registrant/a1b2c3d4-e5f6-4a5b-8c9d-0e1f2a3b4c5d

// V2 Response
{
  "ext_id": "a1b2c3d4-e5f6-4a5b-8c9d-0e1f2a3b4c5d",
  "name": "John Doe",
  "program_ext_id": "5f6a7b8c-9d0e-4f5a-6b7c-8d9e0f1a2b3c"
}
```

**Why?** External IDs are safe to share between systems and don't expose database internals.

### Model Names in Responses

```json
// V1 Response
{
  "id": 42,
  "model": "g2p.program",
  "registrant_id": 10,
  "registrant_model": "g2p.registrant"
}

// V2 Response
{
  "ext_id": "a1b2c3d4...",
  "model": "spp.program",
  "registrant_ext_id": "5f6a7b8c...",
  "registrant_model": "spp.registrant"
}
```

## Authentication Changes

### V1 Authentication (Basic/Session)

```python
# V1 - Basic auth or session cookies
import requests

response = requests.get(
    'http://localhost:8069/api/v1/g2p/registry/registrant',
    auth=('admin', 'password')
)
```

### V2 Authentication (OAuth 2.0)

```python
# V2 - OAuth 2.0 token-based
import requests

# 1. Get access token
token_response = requests.post(
    'http://localhost:8069/oauth2/token',
    data={
        'grant_type': 'client_credentials',
        'client_id': 'your_client_id',
        'client_secret': 'your_client_secret',
        'scope': 'registry:read program:read'
    }
)
access_token = token_response.json()['access_token']

# 2. Use token in requests
response = requests.get(
    'http://localhost:8069/api/v2/spp/registry/registrant',
    headers={'Authorization': f'Bearer {access_token}'}
)
```

### OAuth 2.0 Scopes

V2 introduces granular scopes:

| Scope | Access |
|-------|--------|
| `registry:read` | Read registrant data |
| `registry:write` | Create/update registrants |
| `program:read` | Read program data |
| `program:write` | Manage programs |
| `entitlement:read` | Read entitlements |
| `entitlement:write` | Create/approve entitlements |
| `payment:read` | Read payments |
| `payment:write` | Process payments |

## Migration Examples

### Example 1: List Registrants

```python
# Before (V1)
import requests

response = requests.get(
    'http://localhost:8069/api/v1/g2p/registry/registrant',
    auth=('admin', 'password'),
    params={'limit': 10}
)

for registrant in response.json():
    print(f"ID: {registrant['id']}, Name: {registrant['name']}")

# After (V2)
import requests

# Get OAuth token first
token_response = requests.post(
    'http://localhost:8069/oauth2/token',
    data={
        'grant_type': 'client_credentials',
        'client_id': 'your_client_id',
        'client_secret': 'your_client_secret',
        'scope': 'registry:read'
    }
)
access_token = token_response.json()['access_token']

# Use token
response = requests.get(
    'http://localhost:8069/api/v2/spp/registry/registrant',
    headers={'Authorization': f'Bearer {access_token}'},
    params={'limit': 10}
)

for registrant in response.json()['data']:  # Note: wrapped in 'data'
    print(f"Ext ID: {registrant['ext_id']}, Name: {registrant['name']}")
```

### Example 2: Create Registrant

```python
# Before (V1)
response = requests.post(
    'http://localhost:8069/api/v1/g2p/registry/registrant',
    auth=('admin', 'password'),
    json={
        'name': 'Jane Smith',
        'birthdate': '1990-05-15',
        'gender': 'female'
    }
)
new_id = response.json()['id']

# After (V2)
response = requests.post(
    'http://localhost:8069/api/v2/spp/registry/registrant',
    headers={'Authorization': f'Bearer {access_token}'},
    json={
        'name': 'Jane Smith',
        'birthdate': '1990-05-15',
        'gender': 'female'
    }
)
new_ext_id = response.json()['data']['ext_id']  # UUID, not integer
```

### Example 3: Enroll in Program

```python
# Before (V1)
response = requests.post(
    f'http://localhost:8069/api/v1/g2p/programs/{program_id}/enroll',
    auth=('admin', 'password'),
    json={
        'registrant_id': 42
    }
)

# After (V2)
response = requests.post(
    f'http://localhost:8069/api/v2/spp/programs/{program_ext_id}/enroll',
    headers={'Authorization': f'Bearer {access_token}'},
    json={
        'registrant_ext_id': 'a1b2c3d4-e5f6-4a5b-8c9d-0e1f2a3b4c5d'
    }
)
```

## Change Request API

The Change Request API was significantly refactored in V2:

### V1 Change Request (Multiple Endpoints)

```python
# V1 had separate endpoints for each change type
POST /api/v1/g2p/change_request/add_farmer
POST /api/v1/g2p/change_request/edit_farmer
POST /api/v1/g2p/change_request/create_farm
# ... 10+ different endpoints
```

### V2 Change Request (Unified Endpoint)

```python
# V2 has single endpoint with type parameter
POST /api/v2/spp/change_request

{
  "type": "add_farmer",  # or edit_farmer, create_farm, etc.
  "data": {
    # type-specific data
  }
}
```

**Migration:**

```python
# Before (V1)
response = requests.post(
    'http://localhost:8069/api/v1/g2p/change_request/add_farmer',
    auth=('admin', 'password'),
    json={
        'farmer_name': 'John Farmer',
        'farm_size': 10.5
    }
)

# After (V2)
response = requests.post(
    'http://localhost:8069/api/v2/spp/change_request',
    headers={'Authorization': f'Bearer {access_token}'},
    json={
        'type': 'add_farmer',
        'data': {
            'farmer_name': 'John Farmer',
            'farm_size': 10.5
        }
    }
)
```

## Error Response Changes

### V1 Error Response

```json
{
  "error": "Registrant not found",
  "error_code": "NOT_FOUND"
}
```

### V2 Error Response (RFC 7807 Problem Details)

```json
{
  "type": "https://openspp.org/errors/not-found",
  "title": "Registrant Not Found",
  "status": 404,
  "detail": "No registrant found with ext_id: a1b2c3d4...",
  "instance": "/api/v2/spp/registry/registrant/a1b2c3d4..."
}
```

## Pagination Changes

### V1 Pagination

```python
# V1 - Simple limit/offset
GET /api/v1/g2p/registry/registrant?limit=10&offset=20
```

### V2 Pagination (Cursor-based)

```python
# V2 - Cursor-based pagination for better performance
GET /api/v2/spp/registry/registrant?limit=10&cursor=eyJpZCI6MjB9

# Response includes next cursor
{
  "data": [...],
  "pagination": {
    "next_cursor": "eyJpZCI6MzB9",
    "has_more": true
  }
}
```

## Compatibility Layer

V2 provides a temporary compatibility layer for V1 endpoints:

```python
# V1 endpoints still work (with deprecation warnings)
GET /api/v1/g2p/registry/registrant  # Still works, logs warning

# Response includes deprecation header
Deprecation: true
Sunset: 2026-12-31
Link: <https://docs.openspp.org/migration>; rel="deprecation"
```

**Deprecation timeline:**
- V2.0 (Dec 2025): V1 endpoints work with warnings
- V2.5 (Jun 2026): V1 endpoints return 410 Gone
- V3.0 (Dec 2026): V1 endpoints removed

## Testing API Migration

```python
# tests/test_api_migration.py

import requests
from odoo.tests import TransactionCase

class TestAPIMigration(TransactionCase):
    def setUp(self):
        super().setUp()
        # Get OAuth token
        self.token = self._get_oauth_token()

    def _get_oauth_token(self):
        """Helper to get OAuth token"""
        # Implementation depends on your setup
        return "test_token"

    def test_list_registrants_v2(self):
        """Test V2 registrant listing"""
        response = requests.get(
            f'{self.base_url}/api/v2/spp/registry/registrant',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('data', data)

    def test_external_ids_used(self):
        """Verify external IDs are used, not DB IDs"""
        response = requests.get(
            f'{self.base_url}/api/v2/spp/registry/registrant',
            headers={'Authorization': f'Bearer {self.token}'},
            params={'limit': 1}
        )
        registrant = response.json()['data'][0]
        self.assertIn('ext_id', registrant)
        self.assertNotIn('id', registrant)  # DB ID not exposed
```

## See Also

- {doc}`namespace_changes` - Module and model renames
- {doc}`model_renames` - Model reference changes
- [OpenSPP API v2 Reference](../../reference/api/index.md)

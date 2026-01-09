---
openspp:
  doc_status: draft
  products: [core]
---

# API V2 Overview

This guide is for **developers** integrating external applications with OpenSPP using the REST API V2.

## What is API V2?

OpenSPP API V2 is a modern REST API that provides programmatic access to social protection registry data. It enables:

- **Interoperability** with G2P Connect, DCI, and national identity systems
- **Consent-based** data sharing with field-level privacy controls
- **Extensibility** for module-specific fields (farmer registry, disability, etc.)
- **Scale** to 50M+ registrants with acceptable performance
- **Standards alignment** using FHIR-inspired patterns

## Why V2?

API V2 completely replaces the legacy XML-RPC API with modern standards:

| Feature | V1 (XML-RPC) | V2 (REST) |
|---------|--------------|-----------|
| Authentication | Basic auth | OAuth 2.0 |
| Data format | XML | JSON |
| Identifiers | Database IDs | External IDs (UUIDs) |
| Privacy | No consent | Field-level consent |
| Discovery | None | Capability statement |
| Batch ops | No | Transaction bundles |

## Base URL

```
Production:  https://api.openspp.org/api/v2/spp
Staging:     https://staging-api.openspp.org/api/v2/spp
Development: http://localhost:8069/api/v2/spp
```

## Core Principles

### 1. External Identifiers Only

Never expose internal database IDs. All resources use external identifiers:

```json
// ❌ WRONG - Database ID exposed
{
  "id": 12345,
  "name": "Maria Santos"
}

// ✅ CORRECT - External identifier
{
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-123456789"
    }
  ],
  "name": {
    "given": "Maria",
    "family": "Santos"
  }
}
```

### 2. Namespace URIs

All coded values use URN namespaces for unambiguous identification:

| Type | Example |
|------|---------|
| National ID | `urn:gov:ph:psa:national-id` |
| Gender (ISO 5218) | `urn:iso:std:iso:5218` |
| Relationship | `urn:openspp:vocab:relationship` |
| Extension | `urn:openspp:extension:farmer` |

### 3. Consent by Default

All data access requires either:
- Explicit consent from the registrant, OR
- Legal basis documented in the API client configuration

See {doc}`consent` for details.

### 4. Fail Closed

When in doubt (missing consent, ambiguous permissions), the API denies access and returns minimal data.

## FHIR-Inspired Patterns

OpenSPP API V2 adopts these patterns from FHIR without full compliance:

### Capability Statement

Discover what the API supports:

```http
GET /api/v2/spp/metadata
```

Returns available resources, operations, search parameters, and installed extensions.

### Bundle Transactions

Create multiple related resources atomically:

```http
POST /api/v2/spp/$batch
```

All operations succeed or all fail (rollback).

### CodeableConcept

Represent coded values with their vocabulary:

```json
{
  "gender": {
    "coding": [
      {
        "system": "urn:iso:std:iso:5218",
        "code": "2",
        "display": "Female"
      }
    ],
    "text": "Female"
  }
}
```

## Available Resources

| Resource | Description | Endpoint |
|----------|-------------|----------|
| Individual | Person in the registry | `/Individual` |
| Group | Household or other group | `/Group` |
| Program | Social protection program | `/Program` |
| ProgramMembership | Enrollment in a program | `/ProgramMembership` |
| Consent | Data sharing consent | `/Consent` |

See {doc}`resources` for complete documentation.

## Quick Start

### 1. Register Your Application

Contact your OpenSPP administrator to register your application and receive:
- Client ID
- Client secret
- Authorized scopes

### 2. Get an Access Token

```bash
curl -X POST https://api.openspp.org/api/v2/spp/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "client_credentials",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret"
  }'
```

Response:
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "individual:read individual:search"
}
```

### 3. Make Your First Request

```bash
curl https://api.openspp.org/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789 \
  -H "Authorization: Bearer YOUR_TOKEN"
```

Response:
```json
{
  "resourceType": "Individual",
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-123456789"
    }
  ],
  "name": {
    "given": "Maria",
    "family": "Santos"
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
  }
}
```

## Python Example

```python
import requests

# Get token
token_response = requests.post(
    "https://api.openspp.org/api/v2/spp/oauth/token",
    json={
        "grant_type": "client_credentials",
        "client_id": "your-client-id",
        "client_secret": "your-client-secret"
    }
)
token = token_response.json()["access_token"]

# Fetch individual
headers = {"Authorization": f"Bearer {token}"}
individual = requests.get(
    "https://api.openspp.org/api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789",
    headers=headers
)
print(individual.json())
```

## Performance Characteristics

| Operation | P95 Latency | Throughput |
|-----------|-------------|------------|
| Read single resource | 100ms | 1000 req/s |
| Search (≤100 results) | 500ms | 200 req/s |
| Create single | 200ms | 100 req/s |
| Batch (100 operations) | 2s | 20 req/s |

## API Versioning

The API version is in the URL path: `/api/v2/spp/...`

Major version changes indicate breaking changes. Minor updates are backward-compatible.

Response headers indicate the exact API version:

```http
X-API-Version: 2.0.0
```

## Are You Stuck?

**Getting 401 Unauthorized?**

Check that your access token hasn't expired (tokens last 1 hour). Request a new token.

**Getting 403 Forbidden?**

Your API client may not have the required scopes, or the registrant hasn't consented to data sharing. Check consent status in response headers:

```http
X-Consent-Status: no_consent
```

**Getting empty/minimal responses?**

The API may be filtering fields due to consent restrictions. Use the `X-Consent-Scope` header to see what's allowed.

**Rate limit errors?**

Your client has exceeded rate limits. Check headers:

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1638360000
```

## Next Steps

- {doc}`authentication` - OAuth 2.0 setup and token management
- {doc}`external_identifiers` - Working with external IDs
- {doc}`resources` - Complete resource documentation
- {doc}`search` - Advanced search and filtering
- {doc}`batch` - Batch and transaction operations

## See Also

- [G2P Connect Protocol](https://g2pconnect.cdpi.dev/) - Social protection interoperability
- [FHIR HTTP Interactions](https://www.hl7.org/fhir/http.html) - HTTP patterns we adopt
- [OAuth 2.0 RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) - OAuth standard

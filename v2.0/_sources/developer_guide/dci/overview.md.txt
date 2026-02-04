---
openspp:
  doc_status: draft
  products: [core]
---

# DCI Overview

This guide is for **developers** who need to understand the Digital Convergence Initiative (DCI) architecture and how OpenSPP implements it.

## What is DCI?

The **Digital Convergence Initiative (DCI)** is a set of open API standards designed for interoperability between social protection systems. DCI enables governments and organizations to:

- Exchange beneficiary data between different registries
- Avoid duplication across programs
- Enable data portability and consent-based sharing
- Standardize communication between CRVS, social registries, and program management systems

## Why DCI Matters for OpenSPP

OpenSPP is often deployed as part of a larger ecosystem of government systems:

| System Type | Example | Integration Need |
|-------------|---------|------------------|
| **Civil Registration** | National CRVS | Import birth/death records to update registry |
| **Beneficiary Registries** | National IBR | Check if person is enrolled elsewhere to prevent duplication |
| **MIS/Dashboards** | Ministry dashboard | Query OpenSPP registry for reporting and analytics |
| **Disability Registries** | National DR | Query disability status for eligibility targeting |
| **Other Social Registries** | Provincial registries | Federated beneficiary lookups |

Without DCI, each integration requires custom API development. With DCI, OpenSPP uses standardized protocols that work across different systems.

## DCI Architecture

```{mermaid}
graph TB
    subgraph "OpenSPP as DCI Server"
        A[External System] -->|DCI Search Request| B[DCI Server Module]
        B -->|Query| C[OpenSPP Registry]
        C -->|Results| B
        B -->|DCI Response| A
    end

    subgraph "OpenSPP as DCI Client"
        D[DCI Client Module] -->|DCI Search Request| E[External Registry]
        E -->|Results| D
        D -->|Import| F[OpenSPP Registry]
    end
```

### Key Concepts

#### Three-Part Message Envelope

Every DCI message has three parts:

```json
{
  "signature": "Signature: namespace=\"dci\", kidId=\"...\", ...",
  "header": {
    "version": "1.0.0",
    "message_id": "uuid",
    "action": "search",
    "sender_id": "openspp.example.org",
    "receiver_id": "crvs.national.gov"
  },
  "message": {
    "transaction_id": "uuid",
    "search_request": [...]
  }
}
```

- **Signature** - HTTP Signature for message authenticity (Ed25519 or RSA)
- **Header** - Metadata about the message (sender, receiver, action)
- **Message** - The actual request/response payload

#### Registry Types

DCI defines standard registry types:

| Registry Type | Code | OpenSPP Role | Purpose |
|---------------|------|--------------|---------|
| Social Registry | `SOCIAL_REGISTRY` | Server | Expose beneficiary/household data |
| CRVS | `CRVS` | Client | Import birth/death events |
| IBR | `IBR` | Client | Check enrollments in other programs |
| Disability Registry | `DR` | Client | Query disability status |
| Farmer Registry | `FR` | Server | Expose farmer registrants |

#### Interaction Patterns

**Synchronous Search:**
```{mermaid}
sequenceDiagram
    Client->>Server: POST /registry/sync/search
    Note over Server: Process immediately
    Server-->>Client: 200 OK with results
```

**Asynchronous Search:**
```{mermaid}
sequenceDiagram
    Client->>Server: POST /registry/search (with callback_uri)
    Server-->>Client: 202 Accepted
    Note over Server: Process in background via queue_job
    Server->>Client: POST {callback_uri}/on-search
    Client-->>Server: 200 OK
```

**Subscribe/Notify:**
```{mermaid}
sequenceDiagram
    Subscriber->>Registry: POST /registry/subscribe
    Registry-->>Subscriber: 202 Accepted
    Note over Registry: Event occurs (e.g., new registration)
    Registry->>Subscriber: POST {callback_uri}/notify
    Subscriber-->>Registry: 200 OK
```

## OpenSPP DCI Architecture

### Module Structure

```
spp_dci/                      # Core infrastructure
├── models/
│   ├── dci_envelope.py       # Message envelope schemas
│   └── dci_signing_key.py    # Key management
└── services/
    ├── signature.py          # HTTP signature creation/verification
    └── mapper.py             # DCI ↔ OpenSPP data mapping

spp_dci_server/               # Server implementation
├── routers/
│   ├── auth.py               # OAuth2 token endpoint
│   ├── registry.py           # Search/subscribe endpoints
│   └── wellknown.py          # JWKS and metadata
└── services/
    ├── search_service.py     # Search logic
    └── subscription_service.py # Event subscriptions

spp_dci_client/               # Client implementation
├── models/
│   └── dci_data_source.py    # External registry config
└── services/
    └── dci_client.py         # Generic DCI client

spp_dci_client_crvs/          # CRVS-specific client
spp_dci_client_ibr/           # IBR-specific client
spp_dci_client_dr/            # DR-specific client
```

### Integration with Existing Infrastructure

DCI builds on OpenSPP's existing API V2 infrastructure:

| Component | Reused From | Purpose |
|-----------|-------------|---------|
| Authentication | `spp_oauth` | OAuth2 client credentials flow |
| External IDs | `spp_api_v2` | UUID-based identifiers for data exchange |
| Consent Management | `spp_consent` | Privacy-preserving data sharing |
| Background Jobs | `queue_job` | Async request processing |
| FastAPI | `fastapi` OCA module | REST endpoint framework |

## Use Cases

### Server Use Cases

**1. MIS Reporting Dashboard**

A national MIS needs to query OpenSPP for beneficiary counts by region:

```python
# External system queries OpenSPP
response = await dci_client.search_by_expression(
    conditions=[
        {"attribute": "is_registrant", "operator": "=", "value": True},
        {"attribute": "area_id.code", "operator": "=", "value": "REGION_01"}
    ]
)
```

**2. Inter-Program Coordination**

Another program wants to check if households are already enrolled:

```python
# Query OpenSPP IBR server for enrollment status
response = await ibr_client.check_enrollment(
    identifier_type="urn:gov:national-id",
    identifier_value="12345678"
)
```

### Client Use Cases

**1. CRVS Birth Import**

Automatically import birth registrations from national CRVS:

```python
# Query CRVS for recent births
from odoo.addons.spp_dci_client_crvs.services.crvs_client import CRVSClient

crvs_client = CRVSClient(env['spp.dci.data.source'].browse(1))
births = await crvs_client.search_births(
    date_from=date(2024, 1, 1),
    date_to=date(2024, 12, 31)
)

# Import into OpenSPP registry
for birth in births:
    partner_id = crvs_client.import_person(birth, env)
```

**2. Duplication Prevention**

Before enrolling in a cash transfer program, check IBR for existing enrollments:

```python
# Check if person is already enrolled elsewhere
from odoo.addons.spp_dci_client_ibr.services.ibr_client import IBRClient

ibr_client = IBRClient(env['spp.dci.data.source'].browse(2))
enrollments = await ibr_client.check_enrollment(
    identifier_type="urn:gov:national-id",
    identifier_value=partner.registry_id_ids[0].value
)

if enrollments:
    # Show warning or block enrollment
    raise UserError(f"Already enrolled in: {enrollments[0].programme_name}")
```

**3. Disability Targeting**

Query disability registry for PWD status to determine eligibility:

```python
# Check disability status from external DR
from odoo.addons.spp_dci_client_dr.services.dr_client import DRClient

dr_client = DRClient(env['spp.dci.data.source'].browse(3))
response = await dr_client.search_by_identifier(
    identifier_type="urn:gov:national-id",
    identifier_value=partner.registry_id_ids[0].value
)

disability_info = response.message.search_response[0].data['reg_records'][0].get('disability_info', [])
has_severe_disability = any(d['functional_severity'] >= 3 for d in disability_info)
```

## Data Schemas

DCI uses JSON-LD schemas for data exchange:

### Person Schema

```json
{
  "@context": "https://schema.spdci.org/core/v1",
  "@type": "Person",
  "identifier": [
    {
      "identifier_type": "urn:gov:national-id",
      "identifier_value": "12345678"
    }
  ],
  "name": {
    "given_name": "John",
    "surname": "Doe"
  },
  "sex": "male",
  "birth_date": "1990-05-15",
  "address": [...],
  "phone_number": ["+1234567890"],
  "registration_date": "2024-01-15T10:30:00Z"
}
```

### Group/Household Schema

```json
{
  "@context": "https://schema.spdci.org/core/v1",
  "@type": "Group",
  "group_identifier": [...],
  "group_type": "Household",
  "group_head_info": {...},
  "group_size": 5,
  "member_list": [...],
  "poverty_score": 0.75
}
```

## Authentication and Security

DCI supports two authentication methods:

### OAuth 2.0 Client Credentials

Used for bearer token authentication:

```bash
# Get access token
curl -X POST https://openspp.example.org/api/v2/dci/oauth2/client/token \
  -d "grant_type=client_credentials" \
  -d "client_id=external_system" \
  -d "client_secret=secret"

# Use token for API calls
curl -X POST https://openspp.example.org/api/v2/dci/registry/sync/search \
  -H "Authorization: Bearer {token}" \
  -d @search_request.json
```

### HTTP Signatures

Used for message-level signing:

```python
# Messages are signed with sender's private key
signature = sign_message(header, message, private_key)

# Receiver verifies using sender's public key from JWKS
public_key = fetch_jwks(sender_id)
verify_signature(signature, header, message, public_key)
```

## Next Steps

- **{doc}`server_role`** - Implement OpenSPP as a DCI server
- **{doc}`client_role`** - Integrate with external DCI registries
- **{doc}`protocol`** - Detailed protocol specifications

## References

- [DCI API Standards](https://github.com/spdci/api-standards)
- [G2P Connect Specifications](https://g2pconnect.cdpi.dev)
- [DCI Schemas Repository](https://github.com/spdci/schemas)

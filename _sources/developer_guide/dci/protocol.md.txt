---
openspp:
  doc_status: draft
  products: [core]
---

# DCI Protocol Details

This guide is for **developers** who need detailed specifications of the DCI protocol, message formats, endpoints, and authentication.

## Message Envelope Structure

Every DCI message uses a three-part envelope:

```json
{
  "signature": "Signature: namespace=\"dci\", ...",
  "header": {...},
  "message": {...}
}
```

### Header Schema

```python
# Request Header
{
  "version": "1.0.0",
  "message_id": "550e8400-e29b-41d4-a716-446655440000",  # UUID
  "message_ts": "2024-01-15T10:30:00Z",  # ISO 8601
  "action": "search",  # search, subscribe, notify, unsubscribe
  "sender_id": "openspp.example.org",
  "sender_uri": "https://openspp.example.org/api/v2/dci/callback",  # For async
  "receiver_id": "crvs.national.gov",
  "total_count": 1,
  "is_msg_encrypted": false,
  "meta": {}  # Optional metadata
}

# Response/Callback Header (adds status fields)
{
  ...same as above...,
  "action": "on-search",  # on-search, on-subscribe, etc.
  "status": "succ",  # rcvd, pdng, succ, rjct
  "status_reason_code": "ERR_001",  # Optional error code
  "status_reason_message": "Invalid query",  # Optional error message
  "completed_count": 1
}
```

### HTTP Signature

Messages are signed using HTTP Signature specification:

```
Signature: namespace="dci",
           kidId="openspp.example.org|key1|ed25519",
           algorithm="ed25519",
           created="1705315800",
           expires="1705319400",
           headers="(created) (expires) digest",
           signature="base64_encoded_signature"
```

#### Signing Process

```python
# spp_dci/services/signature.py
import hashlib
import base64
import time
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

def sign_message(header: dict, message: dict, private_key: Ed25519PrivateKey, sender_id: str) -> str:
    """Generate DCI HTTP Signature"""
    # 1. Create digest of header + message
    content = json.dumps({"header": header, "message": message}, sort_keys=True)
    digest = hashlib.sha256(content.encode()).digest()
    digest_b64 = base64.b64encode(digest).decode()

    # 2. Create signing string
    created = int(time.time())
    expires = created + 3600
    signing_string = f"(created): {created}\n(expires): {expires}\ndigest: SHA-256={digest_b64}"

    # 3. Sign with private key
    signature = private_key.sign(signing_string.encode())
    signature_b64 = base64.b64encode(signature).decode()

    # 4. Format signature header
    return (
        f'Signature: namespace="dci", '
        f'kidId="{sender_id}|key1|ed25519", '
        f'algorithm="ed25519", '
        f'created="{created}", '
        f'expires="{expires}", '
        f'headers="(created) (expires) digest", '
        f'signature="{signature_b64}"'
    )
```

#### Verification Process

```python
# spp_dci/services/signature.py
def verify_signature(envelope: dict, public_key) -> bool:
    """Verify DCI HTTP Signature"""
    signature_header = envelope['signature']

    # Parse signature header
    parts = parse_signature_header(signature_header)
    created = int(parts['created'])
    expires = int(parts['expires'])
    signature_b64 = parts['signature']

    # Check expiration
    now = int(time.time())
    if now > expires:
        raise HTTPException(401, "Signature expired")

    # Recreate signing string
    content = json.dumps({
        "header": envelope['header'],
        "message": envelope['message']
    }, sort_keys=True)
    digest = hashlib.sha256(content.encode()).digest()
    digest_b64 = base64.b64encode(digest).decode()

    signing_string = f"(created): {created}\n(expires): {expires}\ndigest: SHA-256={digest_b64}"

    # Verify signature
    signature_bytes = base64.b64decode(signature_b64)
    try:
        public_key.verify(signature_bytes, signing_string.encode())
        return True
    except Exception:
        raise HTTPException(401, "Invalid signature")
```

## API Endpoints

### Authentication

```yaml
POST /oauth2/client/token

Request Body (application/x-www-form-urlencoded):
  grant_type: client_credentials
  client_id: string
  client_secret: string

Response (200 OK):
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### Synchronous Search

```yaml
POST /registry/sync/search

Headers:
  Authorization: Bearer {access_token}
  Content-Type: application/json

Request Body:
{
  "signature": "...",
  "header": {
    "version": "1.0.0",
    "message_id": "uuid",
    "message_ts": "2024-01-15T10:30:00Z",
    "action": "search",
    "sender_id": "openspp.example.org",
    "receiver_id": "crvs.national.gov",
    "total_count": 1
  },
  "message": {
    "transaction_id": "uuid",
    "search_request": [{
      "reference_id": "uuid",
      "timestamp": "2024-01-15T10:30:00Z",
      "search_criteria": {
        "version": "1.0.0",
        "reg_type": "SOCIAL_REGISTRY",
        "query_type": "idtype-value",
        "query": {
          "type": "urn:gov:national-id",
          "value": "12345678"
        },
        "pagination": {
          "page_size": 100,
          "page_number": 1
        }
      }
    }]
  }
}

Response (200 OK):
{
  "signature": "...",
  "header": {
    "version": "1.0.0",
    "message_id": "uuid",
    "message_ts": "2024-01-15T10:30:01Z",
    "action": "on-search",
    "status": "succ",
    "sender_id": "crvs.national.gov",
    "receiver_id": "openspp.example.org",
    "completed_count": 1
  },
  "message": {
    "transaction_id": "uuid",
    "correlation_id": "uuid",
    "search_response": [{
      "reference_id": "uuid",
      "timestamp": "2024-01-15T10:30:01Z",
      "status": "succ",
      "data": {
        "reg_type": "SOCIAL_REGISTRY",
        "reg_record_type": "PERSON",
        "reg_records": [...]
      },
      "pagination": {
        "page_size": 100,
        "page_number": 1,
        "total_count": 1
      }
    }]
  }
}
```

### Asynchronous Search

```yaml
POST /registry/search

# Same request as sync search, but includes sender_uri in header

Response (202 Accepted):
{
  "signature": "...",
  "header": {
    "action": "on-search",
    "status": "rcvd",
    ...
  },
  "message": {
    "transaction_id": "uuid"
  }
}

# Later, server POSTs results to sender_uri:
POST {sender_uri}/on-search

Body: Same as sync search 200 OK response
```

### Subscribe

```yaml
POST /registry/subscribe

Request Body:
{
  "signature": "...",
  "header": {...},
  "message": {
    "transaction_id": "uuid",
    "subscribe_criteria": {
      "version": "1.0.0",
      "reg_type": "SOCIAL_REGISTRY",
      "reg_event_type": "REGISTRATION",
      "filter": {
        "expression": {
          "seq": [
            {"attribute": "area_id.code", "operator": "=", "value": "REGION_01"}
          ]
        }
      },
      "frequency": {
        "frequency": "0 0 * * *",  # Cron expression
        "start_time": "2024-01-15T00:00:00Z",
        "end_time": "2024-12-31T23:59:59Z"
      }
    }
  }
}

Response (202 Accepted):
{
  "signature": "...",
  "header": {
    "action": "on-subscribe",
    "status": "succ"
  },
  "message": {
    "subscription_code": "SUB-123456",
    "expires": "2024-12-31T23:59:59Z"
  }
}
```

### Well-Known Endpoints

```yaml
GET /.well-known/jwks.json

Response (200 OK):
{
  "keys": [
    {
      "kty": "OKP",
      "kid": "openspp.example.org|key1|ed25519",
      "use": "sig",
      "alg": "EdDSA",
      "crv": "Ed25519",
      "x": "base64_public_key"
    }
  ]
}

GET /.well-known/locations.json

Response (200 OK):
{
  "locations": [
    {
      "id": "REGION_01",
      "name": "Central Region",
      "type": "region",
      "parent_id": null
    },
    ...
  ]
}
```

## Query Types

### 1. idtype-value (Simple Identifier Lookup)

```json
{
  "query_type": "idtype-value",
  "query": {
    "type": "urn:gov:national-id",
    "value": "12345678"
  }
}
```

**Use Case:** Lookup person by national ID

### 2. expression (Complex Conditional Query)

#### AND Conditions

```json
{
  "query_type": "expression",
  "query": {
    "expression": {
      "seq": [
        {"attribute": "birth_date", "operator": ">=", "value": "1990-01-01"},
        {"attribute": "birth_date", "operator": "<=", "value": "1990-12-31"},
        {"attribute": "sex", "operator": "=", "value": "female"}
      ]
    }
  }
}
```

**Use Case:** Find all females born in 1990

#### OR Conditions

```json
{
  "query_type": "expression",
  "query": {
    "expression": {
      "or": [
        {"seq": [{"attribute": "area_id.code", "operator": "=", "value": "REGION_01"}]},
        {"seq": [{"attribute": "area_id.code", "operator": "=", "value": "REGION_02"}]}
      ]
    }
  }
}
```

**Use Case:** Find registrants in Region 1 or Region 2

#### Nested Conditions

```json
{
  "query_type": "expression",
  "query": {
    "expression": {
      "seq": [
        {"attribute": "is_disabled", "operator": "=", "value": true},
        {
          "or": [
            {"seq": [{"attribute": "disability_level", "operator": ">=", "value": 3}]},
            {"seq": [{"attribute": "requires_assistance", "operator": "=", "value": true}]}
          ]
        }
      ]
    }
  }
}
```

**Use Case:** Find disabled persons with severe disability OR requiring assistance

### Supported Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equal | `{"attribute": "sex", "operator": "=", "value": "male"}` |
| `>` | Greater than | `{"attribute": "age", "operator": ">", "value": 18}` |
| `<` | Less than | `{"attribute": "age", "operator": "<", "value": 65}` |
| `>=` | Greater or equal | `{"attribute": "birth_date", "operator": ">=", "value": "2020-01-01"}` |
| `<=` | Less or equal | `{"attribute": "birth_date", "operator": "<=", "value": "2020-12-31"}` |
| `in` | In list | `{"attribute": "area_id.code", "operator": "in", "value": ["REGION_01", "REGION_02"]}` |
| `contains` | String contains | `{"attribute": "name", "operator": "contains", "value": "John"}` |

## Data Schemas

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
    "surname": "Doe",
    "given_name": "John",
    "second_name": "Michael",
    "prefix": "Mr",
    "suffix": "Jr"
  },
  "sex": "male",
  "birth_date": "1990-05-15",
  "death_date": null,
  "address": [
    {
      "address_line_1": "123 Main St",
      "address_line_2": "Apt 4B",
      "locality": "Capital City",
      "sub_region_code": "DISTRICT_01",
      "region_code": "REGION_01",
      "postal_code": "12345",
      "country_code": "XX",
      "geo_location": {
        "plus_code": {
          "global_code": "8FVC9G8F+6X",
          "geometry": {
            "location": {
              "latitude": -1.2345,
              "longitude": 36.7890
            }
          }
        }
      }
    }
  ],
  "phone_number": ["+1234567890"],
  "email": ["john.doe@example.com"],
  "registration_date": "2024-01-15T10:30:00Z",
  "last_updated": "2024-01-15T10:30:00Z"
}
```

### Group/Household Schema

```json
{
  "@context": "https://schema.spdci.org/core/v1",
  "@type": "Group",
  "group_identifier": [
    {
      "identifier_type": "urn:gov:household-id",
      "identifier_value": "HH-12345"
    }
  ],
  "group_type": "Household",
  "geographical_location": {
    "name": "Capital City, Central District",
    "code": "DISTRICT_01"
  },
  "address": [...],
  "poverty_score": 0.75,
  "poverty_score_type": "PMT",
  "group_head_info": {
    "member_identifier": [...],
    "demographic_info": {...}
  },
  "group_size": 5,
  "member_list": [
    {
      "member_identifier": [...],
      "demographic_info": {...},
      "related_person": [
        {
          "relationship_type": "spouse",
          "related_member": {...}
        }
      ],
      "is_disabled": false,
      "marital_status": "M",
      "employment_status": "employed",
      "education_level": "secondary"
    }
  ],
  "additional_attributes": [
    {
      "key": "dwelling_type",
      "value": "permanent"
    }
  ],
  "registration_date": "2024-01-15T10:30:00Z",
  "last_updated": "2024-01-15T10:30:00Z"
}
```

### Disability Info

```json
{
  "disability_limitation_type": "Mobility",
  "functional_severity": 3
}
```

**Limitation Types:**
- `Vision`
- `Hearing`
- `Mobility`
- `Cognition`
- `SelfCare`
- `Communication`

**Severity Levels:**
- `1` - No difficulty
- `2` - Some difficulty
- `3` - A lot of difficulty
- `4` - Cannot do it at all

## Field Mappings

### DCI Person ↔ res.partner

| DCI Field | OpenSPP Field | Notes |
|-----------|---------------|-------|
| `identifier[].identifier_type` | `registry_id_ids.id_type_id.namespace_uri` | Namespace URI mapping |
| `identifier[].identifier_value` | `registry_id_ids.value` | Direct mapping |
| `name.given_name` | `given_name` | Direct mapping |
| `name.surname` | `family_name` | Direct mapping |
| `name.prefix` | `name_prefix` | May need to add field |
| `name.suffix` | `name_suffix` | May need to add field |
| `sex` | `gender_id.code` | Vocabulary mapping |
| `birth_date` | `birthdate` | Date format conversion |
| `death_date` | `deathdate` | Date format conversion |
| `address[]` | `address_ids` | Complex mapping |
| `phone_number[]` | `phone_ids` | One-to-many |
| `email[]` | `email` | First email only |
| `registration_date` | `create_date` | System field |
| `last_updated` | `write_date` | System field |

### DCI Group ↔ res.partner (is_group=True)

| DCI Field | OpenSPP Field | Notes |
|-----------|---------------|-------|
| `group_identifier[]` | `registry_id_ids` | Same as Person |
| `group_type` | Computed from `is_group` | Always "Household" |
| `poverty_score` | `poverty_score` | Add field if missing |
| `group_head_info` | Via `group_membership_ids.is_head=True` | Relationship |
| `group_size` | `group_membership_count` | Computed field |
| `member_list[]` | `group_membership_ids` | One-to-many |
| `geographical_location` | `address_ids[0].geo_location` | First address |

## Error Handling

### Error Response Format

```json
{
  "signature": "...",
  "header": {
    "action": "on-search",
    "status": "rjct",
    "status_reason_code": "ERR_INVALID_QUERY",
    "status_reason_message": "Invalid query operator: 'regex'"
  },
  "message": {
    "transaction_id": "uuid"
  }
}
```

### Standard Error Codes

| Code | Description |
|------|-------------|
| `ERR_INVALID_QUERY` | Query syntax or operator not supported |
| `ERR_INVALID_SIGNATURE` | Message signature verification failed |
| `ERR_EXPIRED_SIGNATURE` | Message signature has expired |
| `ERR_UNAUTHORIZED` | Client not authorized for this operation |
| `ERR_NOT_FOUND` | Resource not found |
| `ERR_CONSENT_REQUIRED` | Data access requires consent |
| `ERR_RATE_LIMIT` | Rate limit exceeded |
| `ERR_INTERNAL` | Internal server error |

## Example: Complete Search Flow with curl

### 1. Get Access Token

```bash
curl -X POST https://openspp.example.org/api/v2/dci/oauth2/client/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=external_system" \
  -d "client_secret=secret123"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### 2. Execute Sync Search

```bash
curl -X POST https://openspp.example.org/api/v2/dci/registry/sync/search \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  -H "Content-Type: application/json" \
  -d @search_request.json
```

**search_request.json:**
```json
{
  "signature": "",
  "header": {
    "version": "1.0.0",
    "message_id": "550e8400-e29b-41d4-a716-446655440000",
    "message_ts": "2024-01-15T10:30:00Z",
    "action": "search",
    "sender_id": "external.system.org",
    "receiver_id": "openspp.example.org",
    "total_count": 1
  },
  "message": {
    "transaction_id": "550e8400-e29b-41d4-a716-446655440001",
    "search_request": [{
      "reference_id": "550e8400-e29b-41d4-a716-446655440002",
      "timestamp": "2024-01-15T10:30:00Z",
      "search_criteria": {
        "version": "1.0.0",
        "reg_type": "SOCIAL_REGISTRY",
        "query_type": "idtype-value",
        "query": {
          "type": "urn:gov:national-id",
          "value": "12345678"
        },
        "pagination": {
          "page_size": 100,
          "page_number": 1
        }
      }
    }]
  }
}
```

## Example: Python Client

```python
import httpx
import json
from datetime import datetime

class DCIClient:
    def __init__(self, base_url, client_id, client_secret, sender_id):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.sender_id = sender_id
        self.token = None

    async def authenticate(self):
        """Get OAuth2 access token"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/oauth2/client/token",
                data={
                    "grant_type": "client_credentials",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret
                }
            )
            response.raise_for_status()
            self.token = response.json()["access_token"]
            return self.token

    async def search_by_id(self, id_type: str, id_value: str):
        """Search by identifier"""
        if not self.token:
            await self.authenticate()

        request = {
            "signature": "",
            "header": {
                "version": "1.0.0",
                "message_id": str(uuid.uuid4()),
                "message_ts": datetime.utcnow().isoformat(),
                "action": "search",
                "sender_id": self.sender_id,
                "receiver_id": "openspp.example.org",
                "total_count": 1
            },
            "message": {
                "transaction_id": str(uuid.uuid4()),
                "search_request": [{
                    "reference_id": str(uuid.uuid4()),
                    "timestamp": datetime.utcnow().isoformat(),
                    "search_criteria": {
                        "version": "1.0.0",
                        "reg_type": "SOCIAL_REGISTRY",
                        "query_type": "idtype-value",
                        "query": {
                            "type": id_type,
                            "value": id_value
                        },
                        "pagination": {
                            "page_size": 100,
                            "page_number": 1
                        }
                    }
                }]
            }
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/registry/sync/search",
                json=request,
                headers={
                    "Authorization": f"Bearer {self.token}",
                    "Content-Type": "application/json"
                }
            )
            response.raise_for_status()
            return response.json()

# Usage
client = DCIClient(
    base_url="https://openspp.example.org/api/v2/dci",
    client_id="external_system",
    client_secret="secret123",
    sender_id="external.system.org"
)

result = await client.search_by_id("urn:gov:national-id", "12345678")
persons = result["message"]["search_response"][0]["data"]["reg_records"]
print(f"Found {len(persons)} persons")
```

## References

- [DCI API Standards Repository](https://github.com/spdci/api-standards)
- [DCI Schemas Repository](https://github.com/spdci/schemas)
- [G2P Connect Protocol Specifications](https://g2pconnect.cdpi.dev/protocol)
- [HTTP Signature Specification](https://datatracker.ietf.org/doc/html/draft-cavage-http-signatures)
- [JSON-LD Specification](https://json-ld.org/)

## See Also

- {doc}`overview` - DCI overview and architecture
- {doc}`server_role` - OpenSPP as DCI server
- {doc}`client_role` - OpenSPP as DCI client

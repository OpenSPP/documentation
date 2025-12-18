---
openspp:
  doc_status: draft
---

# Consent Management

This guide is for **developers** implementing consent-based data access in OpenSPP API V2 integrations.

## Why Consent Matters

OpenSPP API V2 implements **privacy-by-design** with consent-based access control. This ensures:

- **Data sovereignty**: Registrants control who accesses their data
- **Compliance**: GDPR, national data protection laws
- **Trust**: Transparent data sharing builds community trust
- **Field-level control**: Share only what's needed for each purpose

## How Consent Works

```
┌────────────┐     ┌──────────────┐     ┌───────────────┐
│  API Call  │────►│ Check Consent│────►│ Filter Fields │
│            │     │              │     │   Based on    │
│            │     │ - Registrant │     │   Consent     │
│            │     │ - API Client │     │   Scope       │
│            │     │ - Resource   │     │               │
└────────────┘     └──────────────┘     └───────────────┘
                           │
                           │ No Consent?
                           ▼
                   ┌──────────────┐
                   │Return Minimal│
                   │  (ID only)   │
                   └──────────────┘
```

When you request a registrant's data:

1. API checks for **active consent** from the registrant to your organization
2. If consent exists, API checks the **consent scope** (which fields allowed)
3. API **filters the response** to only include consented fields
4. If no consent exists, API returns **minimal data** (identifiers only)

## Consent Response Headers

Every API response includes consent status headers:

```http
X-Consent-Status: active
X-Consent-Scope: individual:basic
X-Consent-Expires: 2025-06-30
X-Consent-Purpose: service_delivery
```

| Header | Description |
|--------|-------------|
| `X-Consent-Status` | `active`, `no_consent`, `expired`, `scope_mismatch` |
| `X-Consent-Scope` | Which consent scope applies |
| `X-Consent-Expires` | When consent expires (ISO 8601 date) |
| `X-Consent-Purpose` | Purpose for data access |

## Response Filtering

### Full Consent

When consent is active and covers the requested data:

```http
GET /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789
Authorization: Bearer TOKEN
```

Response:
```http
HTTP/1.1 200 OK
X-Consent-Status: active
X-Consent-Scope: individual:full
X-Consent-Expires: 2025-06-30

{
  "resourceType": "Individual",
  "identifier": [...],
  "name": {"given": "Maria", "family": "Santos"},
  "birthDate": "1985-03-15",
  "gender": {...},
  "telecom": [...],
  "address": [...]
}
```

### Basic Consent (Limited Fields)

When consent allows only basic information:

```http
HTTP/1.1 200 OK
X-Consent-Status: active
X-Consent-Scope: individual:basic
X-Consent-Expires: 2025-06-30

{
  "resourceType": "Individual",
  "identifier": [...],
  "name": {"given": "Maria", "family": "Santos"},
  "active": true
}
```

**Note:** Only `identifier`, `name`, and `active` fields returned.

### No Consent

When no consent exists:

```http
HTTP/1.1 200 OK
X-Consent-Status: no_consent

{
  "resourceType": "Individual",
  "identifier": [
    {
      "system": "urn:gov:ph:psa:national-id",
      "value": "PH-123456789"
    }
  ],
  "_consent": {
    "status": "no_consent",
    "message": "No active consent for this data access"
  }
}
```

**Note:** Only identifiers returned. This allows you to know the record exists without exposing personal data.

### Consent Expired

```http
HTTP/1.1 200 OK
X-Consent-Status: expired
X-Consent-Expires: 2024-12-31

{
  "resourceType": "Individual",
  "identifier": [...],
  "_consent": {
    "status": "expired",
    "message": "Consent expired on 2024-12-31",
    "expiredDate": "2024-12-31"
  }
}
```

## Consent Scopes

Consent is granted at different levels:

| Scope | Fields Included |
|-------|----------------|
| `individual:basic` | identifier, name, active |
| `individual:demographic` | basic + birthDate, gender |
| `individual:contact` | demographic + telecom, address |
| `individual:full` | All fields |
| `individual:custom` | Administrator-defined field list |

### Extension Fields

Module extensions require explicit consent:

```http
GET /api/v2/spp/Individual/...?_extensions=farmer
```

If consent doesn't include the `farmer` extension:

```json
{
  "resourceType": "Individual",
  "identifier": [...],
  "name": {...},
  "_consent": {
    "status": "active",
    "message": "Extension 'farmer' not included in consent scope",
    "allowedExtensions": []
  }
}
```

## Legal Basis (No Consent Required)

Some API clients operate under **legal basis** that doesn't require individual consent:

| Legal Basis | Example | Consent Required |
|-------------|---------|------------------|
| `consent` | Mobile app for beneficiaries | Yes |
| `legal_obligation` | Tax authority audit | No |
| `vital_interest` | Emergency health services | No |
| `public_task` | Government statistical office | No |
| `contract` | Payment processor | No |

API clients with legal basis bypass consent checks but still respect scope restrictions.

## Checking Consent Programmatically

### Example: Python

```python
import requests

def check_consent_status(identifier, token, base_url):
    """Check consent status from API response headers."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{base_url}/Individual/{identifier}",
        headers=headers
    )

    consent_status = response.headers.get("X-Consent-Status")
    consent_scope = response.headers.get("X-Consent-Scope")
    consent_expires = response.headers.get("X-Consent-Expires")

    return {
        "status": consent_status,
        "scope": consent_scope,
        "expires": consent_expires,
        "data": response.json()
    }

# Usage
result = check_consent_status(
    identifier="urn:gov:ph:psa:national-id|PH-123456789",
    token=token,
    base_url="https://api.openspp.org/api/v2/spp"
)

if result["status"] == "active":
    print(f"Consent active until {result['expires']}")
    print(f"Scope: {result['scope']}")
    print(f"Data: {result['data']}")
elif result["status"] == "no_consent":
    print("No consent on file. Request consent from registrant.")
else:
    print(f"Consent status: {result['status']}")
```

### Example: JavaScript

```javascript
async function checkConsentStatus(identifier, token, baseUrl) {
  const response = await fetch(`${baseUrl}/Individual/${identifier}`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });

  const consentStatus = response.headers.get('X-Consent-Status');
  const consentScope = response.headers.get('X-Consent-Scope');
  const consentExpires = response.headers.get('X-Consent-Expires');

  const data = await response.json();

  return {
    status: consentStatus,
    scope: consentScope,
    expires: consentExpires,
    data: data
  };
}

// Usage
const result = await checkConsentStatus(
  'urn:gov:ph:psa:national-id|PH-123456789',
  token,
  'https://api.openspp.org/api/v2/spp'
);

if (result.status === 'active') {
  console.log(`Consent active until ${result.expires}`);
  console.log(`Scope: ${result.scope}`);
} else if (result.status === 'no_consent') {
  console.log('No consent on file');
}
```

## Managing Consents via API

### List Consents for a Registrant

**Note:** Requires `consent:read` scope and appropriate permissions.

```http
GET /api/v2/spp/Consent?registrant=Individual/urn:gov:ph:psa:national-id|PH-123456789
Authorization: Bearer TOKEN
```

Response:
```json
{
  "resourceType": "Bundle",
  "type": "searchset",
  "total": 2,
  "entry": [
    {
      "resource": {
        "resourceType": "Consent",
        "status": "active",
        "registrant": {
          "reference": "Individual/urn:gov:ph:psa:national-id|PH-123456789"
        },
        "grantee": {
          "reference": "Organization/ministry-of-agriculture",
          "display": "Ministry of Agriculture"
        },
        "scope": [
          {
            "resourceType": "individual",
            "fieldAccess": "full",
            "includeExtensions": true,
            "allowedExtensions": ["farmer"]
          }
        ],
        "effectiveDate": "2024-01-15",
        "expiryDate": "2025-06-30",
        "purpose": "service_delivery"
      }
    }
  ]
}
```

### Create Consent

**Note:** Requires `consent:create` scope. Usually performed by authorized personnel after obtaining consent from registrant.

```http
POST /api/v2/spp/Consent
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "resourceType": "Consent",
  "registrant": {
    "reference": "Individual/urn:gov:ph:psa:national-id|PH-123456789"
  },
  "grantee": {
    "reference": "Organization/ministry-of-agriculture"
  },
  "scope": [
    {
      "resourceType": "individual",
      "fieldAccess": "basic",
      "purpose": "eligibility_verification"
    }
  ],
  "effectiveDate": "2024-11-28",
  "expiryDate": "2025-11-27",
  "collectionMethod": "electronic",
  "evidence": {
    "description": "Mobile app consent form signed via digital signature"
  }
}
```

### Revoke Consent

```http
POST /api/v2/spp/Consent/{consent-id}/$revoke
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "reason": "Beneficiary requested revocation via support ticket #12345"
}
```

Response:
```http
HTTP/1.1 200 OK

{
  "resourceType": "Consent",
  "status": "revoked",
  "revokedDate": "2024-11-28T14:30:00Z",
  "revokedBy": {
    "reference": "User/admin",
    "display": "System Administrator"
  },
  "revocationReason": "Beneficiary requested revocation via support ticket #12345"
}
```

## Consent Collection Methods

When creating consent, specify how it was obtained:

| Method | Description |
|--------|-------------|
| `written` | Paper form with signature |
| `verbal` | Verbal consent (witnessed) |
| `electronic` | Digital signature, checkbox, etc. |
| `implied` | Implied by service request |

```json
{
  "collectionMethod": "electronic",
  "evidence": {
    "description": "Mobile app consent screen",
    "timestamp": "2024-11-28T10:15:00Z",
    "ipAddress": "192.168.1.100",
    "userAgent": "OpenSPP-Mobile/2.1.0 (Android 12)"
  }
}
```

## Purpose Limitation

Consent is purpose-specific:

| Purpose | Description |
|---------|-------------|
| `service_delivery` | Delivering program benefits |
| `eligibility_verification` | Checking program eligibility |
| `analytics` | Anonymized statistics |
| `research` | Academic research |
| `audit` | Compliance audits |

The API tracks and logs the stated purpose for each access:

```http
X-Consent-Purpose: eligibility_verification
```

## Handling Consent Errors

### 403 Forbidden: Insufficient Consent

```http
HTTP/1.1 403 Forbidden

{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "forbidden",
      "details": {
        "coding": [
          {
            "system": "urn:openspp:error",
            "code": "CONSENT_REQUIRED"
          }
        ],
        "text": "No active consent for this data access"
      },
      "diagnostics": "Registrant has not consented to data sharing with your organization"
    }
  ]
}
```

### Consent Scope Mismatch

Requesting fields not covered by consent:

```http
GET /api/v2/spp/Individual/...?_elements=identifier,name,telecom,address
```

With consent only for `basic` scope (identifier, name):

```json
{
  "resourceType": "Individual",
  "identifier": [...],
  "name": {...},
  "_consent": {
    "status": "active",
    "scope": "individual:basic",
    "message": "Requested fields 'telecom', 'address' not included in consent scope",
    "allowedFields": ["identifier", "name", "active"]
  }
}
```

## Best Practices

### 1. Always Check Consent Headers

```python
def fetch_with_consent_check(url, token):
    """Fetch data and handle consent status."""
    response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    response.raise_for_status()

    consent_status = response.headers.get("X-Consent-Status")

    if consent_status == "no_consent":
        print("Warning: No consent. Limited data returned.")
    elif consent_status == "expired":
        print("Warning: Consent expired. Limited data returned.")
    elif consent_status != "active":
        print(f"Warning: Consent status: {consent_status}")

    return response.json()
```

### 2. Request Only What You Need

Don't request all fields if you only need basic info:

```http
# ✅ Good - Request only needed fields
GET /api/v2/spp/Individual/...?_elements=identifier,name

# ❌ Bad - Request everything
GET /api/v2/spp/Individual/...
```

### 3. Handle Partial Data Gracefully

Always check if expected fields are present:

```python
individual = fetch_individual(identifier, token, base_url)

# ✅ Good - Check before accessing
if "telecom" in individual:
    phone = individual["telecom"][0]["value"]
else:
    phone = None  # Not consented

# ❌ Bad - Assume field exists
phone = individual["telecom"][0]["value"]  # May crash
```

### 4. Respect Consent Expiration

Track consent expiration and prompt for renewal:

```python
consent_expires = response.headers.get("X-Consent-Expires")

if consent_expires:
    from datetime import datetime, timedelta
    expires_date = datetime.fromisoformat(consent_expires)
    days_remaining = (expires_date - datetime.now()).days

    if days_remaining < 30:
        print(f"Warning: Consent expires in {days_remaining} days")
        # Trigger renewal process
```

### 5. Document Your Purpose

Always specify why you're accessing data:

```python
# In your application documentation
PURPOSE = "eligibility_verification"
PURPOSE_DESCRIPTION = "Checking eligibility for farmer subsidy program"

# Include in audit logs
logger.info(f"Accessing individual {identifier} for purpose: {PURPOSE}")
```

## Complete Example

```python
import requests
from datetime import datetime, timedelta

class ConsentAwareClient:
    """API client with consent awareness."""

    def __init__(self, client_id, client_secret, base_url):
        self.base_url = base_url
        self.token = None  # Implement token management

    def get_individual_with_consent(self, identifier):
        """Fetch individual with consent checking."""
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
            f"{self.base_url}/Individual/{identifier}",
            headers=headers
        )
        response.raise_for_status()

        # Check consent status
        consent_status = response.headers.get("X-Consent-Status")
        consent_expires = response.headers.get("X-Consent-Expires")

        data = response.json()

        # Add consent metadata to response
        data["_consentInfo"] = {
            "status": consent_status,
            "expires": consent_expires,
            "scope": response.headers.get("X-Consent-Scope"),
            "purpose": response.headers.get("X-Consent-Purpose")
        }

        # Warn if consent issues
        if consent_status == "no_consent":
            data["_consentInfo"]["warning"] = "No consent on file. Limited data returned."
        elif consent_status == "expired":
            data["_consentInfo"]["warning"] = f"Consent expired on {consent_expires}"
        elif consent_status == "active" and consent_expires:
            expires_date = datetime.fromisoformat(consent_expires)
            days_remaining = (expires_date - datetime.now()).days
            if days_remaining < 30:
                data["_consentInfo"]["warning"] = f"Consent expires in {days_remaining} days"

        return data

    def request_consent(self, registrant_identifier, scope, purpose, expires_days=365):
        """Request consent creation (requires appropriate permissions)."""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        effective_date = datetime.now().date().isoformat()
        expiry_date = (datetime.now() + timedelta(days=expires_days)).date().isoformat()

        consent_data = {
            "resourceType": "Consent",
            "registrant": {
                "reference": f"Individual/{registrant_identifier}"
            },
            "grantee": {
                "reference": f"Organization/{self.client_id}"
            },
            "scope": [scope],
            "effectiveDate": effective_date,
            "expiryDate": expiry_date,
            "purpose": purpose,
            "collectionMethod": "electronic"
        }

        response = requests.post(
            f"{self.base_url}/Consent",
            headers=headers,
            json=consent_data
        )
        response.raise_for_status()
        return response.json()

# Usage
client = ConsentAwareClient(
    client_id="ministry-of-agriculture",
    client_secret="your-secret",
    base_url="https://api.openspp.org/api/v2/spp"
)

# Fetch with consent checking
individual = client.get_individual_with_consent(
    "urn:gov:ph:psa:national-id|PH-123456789"
)

if individual["_consentInfo"]["status"] == "active":
    print(f"Full data available: {individual['name']['text']}")
elif individual["_consentInfo"]["status"] == "no_consent":
    print(f"Limited data. Consider requesting consent.")
    # Request consent if appropriate
    # client.request_consent(...)
```

## Are You Stuck?

**Getting only identifiers in responses?**

This indicates no consent. Check the `X-Consent-Status` header. If `no_consent`, the registrant needs to provide consent.

**How do I know what fields are allowed?**

Check the `_consent.allowedFields` array in responses with consent restrictions.

**Can I bypass consent for emergencies?**

If your API client has `legal_basis: vital_interest`, consent checks are relaxed. Contact your administrator to configure this.

**Consent expired—what now?**

The registrant must renew consent. Use the consent management endpoints to create a new consent record.

**Can registrants revoke consent themselves?**

Yes, through the beneficiary portal or mobile app. Your integration should handle `consent:revoked` events gracefully.

## Next Steps

- {doc}`resources` - Learn about available API resources
- {doc}`search` - Advanced search capabilities
- {doc}`errors` - Error handling
- {doc}`authentication` - OAuth 2.0 setup

## See Also

- [GDPR Principles](https://gdpr-info.eu/art-5-gdpr/) - Data protection principles
- [G2P Connect: Consent](https://g2pconnect.cdpi.dev/protocol/consent) - Consent in social protection
- [FHIR Consent Resource](https://www.hl7.org/fhir/consent.html) - FHIR consent model

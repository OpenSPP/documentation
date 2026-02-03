---
openspp:
  doc_status: draft
  products: [core]
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

API responses include consent status headers:

```text
X-Consent-Status: active
X-Consent-Scope: individual
```

| Header             | Description                                                        |
| ------------------ | ------------------------------------------------------------------ |
| `X-Consent-Status` | `active`, `no_consent`, `expired`, `legal_basis`, `scope_mismatch` |
| `X-Consent-Scope`  | Resource type the consent applies to (e.g., `individual`, `group`) |

## Response Filtering

### Full Consent

When consent is active and covers the requested data:

```text
GET /api/v2/spp/Individual/urn:gov:ph:psa:national-id|PH-123456789
Authorization: Bearer TOKEN
```

Response:

```text
HTTP/1.1 200 OK
X-Consent-Status: active
X-Consent-Scope: individual

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

```text
HTTP/1.1 200 OK
X-Consent-Status: active
X-Consent-Scope: individual

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

```text
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

```text
HTTP/1.1 200 OK
X-Consent-Status: expired

{
  "resourceType": "Individual",
  "identifier": [...],
  "_consent": {
    "status": "expired",
    "message": "Consent has expired"
  }
}
```

## Consent Scopes

Consent is granted at different levels:

| Scope                    | Fields Included                  |
| ------------------------ | -------------------------------- |
| `individual:basic`       | identifier, name, active         |
| `individual:demographic` | basic + birthDate, gender        |
| `individual:contact`     | demographic + telecom, address   |
| `individual:full`        | All fields                       |
| `individual:custom`      | Administrator-defined field list |

### Extension Fields

Module extensions require explicit consent:

```text
GET /api/v2/spp/Individual/...?_extensions=farmer
```

If consent doesn't include the `farmer` extension:

```text
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

| Legal Basis        | Example                       | Consent Required |
| ------------------ | ----------------------------- | ---------------- |
| `consent`          | Mobile app for beneficiaries  | Yes              |
| `legal_obligation` | Tax authority audit           | No               |
| `vital_interest`   | Emergency health services     | No               |
| `public_task`      | Government statistical office | No               |
| `contract`         | Payment processor             | No               |

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

    return {
        "status": consent_status,
        "scope": consent_scope,
        "data": response.json()
    }

# Usage
result = check_consent_status(
    identifier="urn:gov:ph:psa:national-id|PH-123456789",
    token=token,
    base_url="https://api.openspp.org/api/v2/spp"
)

if result["status"] == "active":
    print(f"Consent active, scope: {result['scope']}")
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
      Authorization: `Bearer ${token}`,
    },
  });

  const consentStatus = response.headers.get("X-Consent-Status");
  const consentScope = response.headers.get("X-Consent-Scope");

  const data = await response.json();

  return {
    status: consentStatus,
    scope: consentScope,
    data: data,
  };
}

// Usage
const result = await checkConsentStatus(
  "urn:gov:ph:psa:national-id|PH-123456789",
  token,
  "https://api.openspp.org/api/v2/spp",
);

if (result.status === "active") {
  console.log(`Consent active, scope: ${result.scope}`);
} else if (result.status === "no_consent") {
  console.log("No consent on file");
}
```

## Consent API Endpoints

{note}
Consent records are created and managed through the OpenSPP user interface, not via the API. The API provides read-only access to consent status and supports consent revocation.

### Available Operations

| Operation       | Endpoint                            | Description                   |
| --------------- | ----------------------------------- | ----------------------------- |
| Get Status      | `GET /Consent/{id}`                 | Check consent status          |
| Revoke          | `POST /Consent/{id}/$revoke`        | Revoke consent (GDPR Art 7.3) |
| Revoke (DELETE) | `DELETE /Consent/{id}`              | Alternative revocation method |
| Receipt         | `GET /Consent/{id}/$receipt`        | Generate ISO 29184 receipt    |
| History         | `GET /Consent/{id}/$history`        | View consent version history  |
| Access Summary  | `GET /Consent/{id}/$access-summary` | View data access logs         |

### Get Consent Status

```text
GET /api/v2/spp/Consent/{consent-id}
Authorization: Bearer TOKEN
```

Response:

```json
{
  "consent_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "given",
  "grantee": "Ministry of Agriculture",
  "effective_date": "2024-01-15",
  "expiry_date": "2025-06-30",
  "scopes": [
    {
      "resource_type": "individual",
      "field_access": "full",
      "purpose": "service_delivery",
      "include_extensions": true
    }
  ],
  "legal_basis": null
}
```

### Revoke Consent

```text
POST /api/v2/spp/Consent/{consent-id}/$revoke
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "reason": "Beneficiary requested revocation via support ticket #12345"
}
```

Response:

```text
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

When consent is created through the OpenSPP UI, the collection method is recorded:

| Method       | Description                       |
| ------------ | --------------------------------- |
| `written`    | Paper form with signature         |
| `verbal`     | Verbal consent (witnessed)        |
| `electronic` | Digital signature, checkbox, etc. |
| `implied`    | Implied by service request        |

## Purpose Limitation

Consent is purpose-specific. When created through the UI, administrators specify the purpose:

| Purpose                    | Description                  |
| -------------------------- | ---------------------------- |
| `service_delivery`         | Delivering program benefits  |
| `eligibility_verification` | Checking program eligibility |
| `analytics`                | Anonymized statistics        |
| `research`                 | Academic research            |
| `audit`                    | Compliance audits            |

## Handling Consent Errors

### 403 Forbidden: Insufficient Consent

```text
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

```text
GET /api/v2/spp/Individual/...?_elements=identifier,name,telecom,address
```

With consent only for `basic` scope (identifier, name):

```text
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

```text
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

### 4. Handle Expired Consent

Check the `X-Consent-Status` header for expiration:

```python
consent_status = response.headers.get("X-Consent-Status")

if consent_status == "expired":
    print("Warning: Consent has expired. Contact registrant for renewal.")
    # Limited data will be returned
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

class ConsentAwareClient:
    """API client with consent awareness."""

    def __init__(self, client_id, client_secret, base_url):
        self.base_url = base_url
        self.client_id = client_id
        self.token = None  # Implement token management

    def get_individual_with_consent(self, identifier):
        """Fetch individual with consent checking."""
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
            f"{self.base_url}/Individual/{identifier}",
            headers=headers
        )
        response.raise_for_status()

        # Check consent status from headers
        consent_status = response.headers.get("X-Consent-Status")
        consent_scope = response.headers.get("X-Consent-Scope")

        data = response.json()

        # Add consent metadata to response
        data["_consentInfo"] = {
            "status": consent_status,
            "scope": consent_scope,
        }

        # Warn if consent issues
        if consent_status == "no_consent":
            data["_consentInfo"]["warning"] = "No consent on file. Limited data returned."
        elif consent_status == "expired":
            data["_consentInfo"]["warning"] = "Consent has expired. Limited data returned."

        return data

    def revoke_consent(self, consent_id, reason=None):
        """Revoke a consent via API."""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        payload = {"reason": reason} if reason else {}

        response = requests.post(
            f"{self.base_url}/Consent/{consent_id}/$revoke",
            headers=headers,
            json=payload
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
    print("Limited data. Consent must be obtained through OpenSPP UI.")
```

## Are You Stuck?

**Getting only identifiers in responses?**

This indicates no consent. Check the `X-Consent-Status` header. If `no_consent`, the registrant needs to provide consent through the OpenSPP user interface.

**How do I know what fields are allowed?**

Check the `_consent.allowedFields` array in responses with consent restrictions.

**Can I bypass consent for emergencies?**

If your API client has `legal_basis: vital_interest`, consent checks are relaxed. Contact your administrator to configure this.

**Consent expired—what now?**

The registrant must renew consent through the OpenSPP user interface. Contact your program administrator.

**Can registrants revoke consent themselves?**

Yes, through the beneficiary portal or mobile app. Your integration should handle revoked consent gracefully (you'll receive limited data).

## Next Steps

- {doc}`resources` - Learn about available API resources
- {doc}`search` - Advanced search capabilities
- {doc}`errors` - Error handling
- {doc}`authentication` - OAuth 2.0 setup

## See Also

- [GDPR Principles](https://gdpr-info.eu/art-5-gdpr/) - Data protection principles
- [G2P Connect: Consent](https://g2pconnect.cdpi.dev/protocol/consent) - Consent in social protection
- [FHIR Consent Resource](https://www.hl7.org/fhir/consent.html) - FHIR consent model

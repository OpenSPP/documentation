---
openspp:
  doc_status: draft
  products: [core]
---

# API consent filtering

This guide is for **implementers** understanding how consent controls API data access. OpenSPP uses a fail-closed design where data cannot be shared via API without valid consent.

## How it works

```
Partner API Request → Check consent_summary → Filter response → Return data
```

1. Partner makes API request for beneficiary data
2. System checks beneficiary's cached `consent_summary` field
3. Consent determines if partner can access data
4. API returns data only if consent allows

## Consent summary cache

Each registrant has a `consent_summary` JSON field that caches their active consents for fast API filtering. This enables O(1) consent checks instead of querying consent records on every request.

**Structure:**
```json
{
  "organization_types": ["government", "ngo", "un"],
  "purposes": ["SPRegistration", "SPBenefitDelivery"],
  "specific_recipients": [123, 456],
  "last_updated": "2024-03-15T10:30:00"
}
```

The cache updates automatically when:
- A new consent is recorded
- Consent status changes
- Consent expires or is withdrawn

## Consent matching modes

### Category-based consent

Beneficiary consents to share with **types** of organizations (e.g., "all NGOs").

**Example consent record:**

| Field | Value |
|-------|-------|
| Recipient Mode | Organization Categories |
| Allowed Organization Types | Government Agency, NGO, UN Agency |

**API behavior:**
- Requests from partners with matching org type → Data returned
- Requests from partners without matching org type → Minimal data only

### Specific organization consent

Beneficiary consents to share with **named** organizations.

**Example consent record:**

| Field | Value |
|-------|-------|
| Recipient Mode | Specific Organizations |
| Data Recipients | UNICEF Kenya, Red Cross |

**API behavior:**
- Requests from listed partners → Data returned
- Requests from unlisted partners → Minimal data only

## Fail-closed design

When consent is missing or invalid, the API fails closed:

| Situation | API behavior |
|-----------|--------------|
| No consent record | Minimal data only |
| Consent expired | Minimal data only |
| Consent withdrawn | Access denied |
| Consent refused | Access denied |
| Valid consent | Full data access |

**Minimal data** typically includes only the identifier to confirm the record exists.

## Purpose-based filtering

Consent can be limited to specific purposes. The API checks if the requesting purpose matches the consent.

**Example:**
- Consent purposes: Beneficiary Registration, Benefit Delivery
- API request purpose: Research → Access denied
- API request purpose: Benefit Delivery → Access granted

## Configuring consent for API access

### Step 1: Create consent record

Record consent for the beneficiary with appropriate settings:

| Field | Value for API access |
|-------|---------------------|
| Status | Given |
| Legal Basis | Consent (or appropriate basis) |
| Purposes | Select purposes the partner needs |
| Recipient Mode | Category OR Specific |
| Recipients | Select org types or specific partners |
| Expiry Date | Set appropriate validity period |

### Step 2: Verify consent summary

After saving, check the beneficiary's record to confirm `consent_summary` updated.

### Step 3: Test API access

Use the API V2 endpoint to verify access:
```
GET /api/v2/spp/Individual/{identifier}
```

Check that:
- Response includes expected fields
- Partner without consent gets minimal response
- Expired consent blocks access

## Organization type codes

Use these codes when checking consent programmatically:

| Organization Type | Code |
|-------------------|------|
| Government Agency | `government` |
| NGO / Non-Profit | `ngo` |
| International NGO | `ingo` |
| UN Agency | `un` |
| Private Sector | `private` |
| Research Institution | `research` |
| Other | `other` |

## Best practices

1. **Set reasonable expiry dates** - Consent should expire and require renewal (1-2 years typical)

2. **Use category-based consent** for flexibility - Allows new partners of same type without re-consenting

3. **Document the purpose** - Clear purposes help with audit and compliance

4. **Monitor expired consents** - Use the Expired Consents view to track renewals

5. **Test with different partners** - Verify consent filtering works correctly

## Are you stuck?

**Partner getting empty responses?**

Check:
- Consent status is "Given" or "Renewed"
- Consent hasn't expired (check expiry date)
- Partner's organization type matches allowed types
- OR partner is in the specific recipients list
- Purpose in API request matches consent purposes

**How do I grant different access to different partners?**

Use category-based consent with organization types. Partners in different categories get different access based on consent.

**Can I change consent without re-collecting?**

You can change consent only while status is "Requested". Once status is "Given", consent terms are locked. Create a new consent record if changes are needed.

**What if a beneficiary has multiple consent records?**

The most permissive active consent applies. The `consent_summary` aggregates all valid consents, combining organization types, purposes, and recipients.

## See also

- {doc}`overview` - Consent concepts and lifecycle
- {doc}`recording_consent` - How to record consent

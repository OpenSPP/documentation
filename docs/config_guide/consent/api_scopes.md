---
openspp:
  doc_status: draft
  products: [core]
---

# Configuring API Scopes

This guide is for **implementers** configuring field-level API access control based on consent. API scopes determine what data external systems can access.

## What are API Scopes?

API scopes define:
- Which resource types a partner can access (Individual, Group, Program Enrollment)
- Which fields within those resources
- For what purpose

This enables **field-level consent** - sharing only the data beneficiaries agreed to share.

## How It Works

```
Partner API Request → Check Consent → Apply Scope → Return Filtered Data
```

1. Partner makes API request for beneficiary data
2. System checks beneficiary's consent record
3. Consent scope determines allowed fields
4. API returns only permitted data

## Configuring Scopes on Consent Records

### Step 1: Open Consent Record

Navigate to a consent record with status "Given".

### Step 2: Add API Scope

In the **API Scopes** tab, click **Add a line**.

### Step 3: Configure Scope

| Field | Value | Notes |
|-------|-------|-------|
| Resource Type | Individual Data | What type of data |
| Field Access | All Fields / Basic Info Only / Custom Field List | Level of access |
| Purpose | Service Delivery | Why access is needed |

**Resource Types:**

| Type | Description |
|------|-------------|
| Individual Data | Person records |
| Group/Household Data | Household/group records |
| Program Enrollment | Program membership data |
| All Data | All resource types |

**Field Access Levels:**

| Level | Fields Included |
|-------|-----------------|
| **All Fields** | Complete record |
| **Basic Info Only** | Name, ID numbers, active status |
| **Custom Field List** | Specific fields you define |

### Step 4: Custom Fields (Optional)

If Field Access is "Custom Field List", specify fields in **Custom Fields**:

```
name
birthdate
gender
phone
```

### Step 5: Extensions (Optional)

| Field | Value |
|-------|-------|
| Include Extensions | Yes/No |
| Allowed Extensions | farmer, disability (if yes) |

Extensions are additional data modules (e.g., farmer registry data).

## Field Access Examples

### Example 1: Basic Verification

Partner needs only to verify identity.

| Setting | Value |
|---------|-------|
| Resource Type | Individual Data |
| Field Access | Basic Info Only |
| Purpose | Eligibility Verification |

**API Response includes:**
- Identifier
- Name
- Active status

### Example 2: Service Delivery

Partner needs full beneficiary data for service delivery.

| Setting | Value |
|---------|-------|
| Resource Type | Individual Data |
| Field Access | All Fields |
| Purpose | Service Delivery |

**API Response includes:**
- All fields in the record
- Contact information
- Demographics

### Example 3: Research (Anonymized)

Research partner needs demographic data without identifiers.

| Setting | Value |
|---------|-------|
| Resource Type | Individual Data |
| Field Access | Custom Field List |
| Custom Fields | birthdate, gender, area_id |
| Purpose | Research |

**API Response includes:**
- Birthdate
- Gender
- Area (no name or ID)

## Consent Summary Caching

OpenSPP caches consent information on each registrant for fast API filtering:

- `consent_summary` field on res.partner
- Contains allowed org types, purposes, recipients
- Updated when consent changes

This enables efficient API queries without checking every consent record.

## Fail-Closed Design

When consent is missing or invalid:

| Situation | API Behavior |
|-----------|--------------|
| No consent record | Minimal data only |
| Consent expired | Minimal data only |
| Consent withdrawn | Access denied |
| Consent refused | Access denied |
| Consent given | Full scope access |

**Minimal data** typically includes only the identifier to confirm the record exists.

## Testing API Scopes

### Step 1: Create Test Consent

1. Create consent record for a test beneficiary
2. Configure API scope with specific field access
3. Set status to "Given"

### Step 2: Make API Request

Use the API V2 endpoint:
```
GET /api/v2/spp/Individual/{identifier}
```

### Step 3: Verify Response

Check that:
- Only permitted fields are returned
- Extensions are included/excluded per scope
- Unauthorized fields return empty or are omitted

## Are You Stuck?

**Partner getting empty responses?**

Check:
- Consent status is "Given"
- Consent hasn't expired
- API scope is configured for the right resource type
- Partner's organization type matches allowed recipients

**How do I grant different access to different partners?**

Create separate consent records for each partner, or use Organization Categories with different scopes per category.

**Can I change scopes without re-collecting consent?**

You can add scopes within what the privacy notice covers. You cannot expand beyond what the beneficiary agreed to without new consent.

**What if a beneficiary has multiple consent records?**

The most permissive active consent applies. If one consent allows all fields and another allows basic info only, all fields are returned.

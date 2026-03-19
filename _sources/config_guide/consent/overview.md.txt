---
openspp:
  doc_status: draft
  products: [core]
---

# Consent management overview

This guide is for **implementers** configuring consent management in OpenSPP. You should understand your program's data protection requirements but don't need programming knowledge.

## Mental model

Consent in OpenSPP has three layers:

| Layer | What it does | Example |
|-------|--------------|---------|
| **Privacy Notice** | Explains what data is collected and why | "Program Enrollment Notice" |
| **Consent Record** | Tracks individual's permission | "Maria Santos gave consent on 2024-03-15" |
| **Consent Summary** | Cached consent for API filtering | Aggregated purposes and recipients |

Think of it like this:
- **Privacy Notice** = The form explaining data use (defines maximum scope)
- **Consent Record** = The signed agreement (must be within notice scope)
- **Consent Summary** = Cached JSON on registrant for fast API filtering

## Why Consent Management?

OpenSPP uses a **fail-closed design** - data cannot be shared without explicit consent. This ensures compliance with data protection regulations like GDPR, Kenya DPA, and similar laws.

| Without Consent | With Consent |
|-----------------|--------------|
| API returns minimal data | API returns full authorized data |
| Data sharing blocked | Data sharing enabled per scope |
| Partner access denied | Partner access granted |

## Key Concepts

### Legal Basis

Every consent record requires a legal basis for processing:

| Legal Basis | When to Use |
|-------------|-------------|
| **Consent** | Beneficiary freely gives permission (most common) |
| **Contract** | Processing needed to deliver a service |
| **Legal Obligation** | Required by law (e.g., mandatory reporting) |
| **Vital Interest** | Protecting someone's life (emergencies) |
| **Public Interest** | Official government function |
| **Legitimate Interest** | Organizational need (rarely used) |

### Consent Status Lifecycle

```
Requested → Given → Renewed
                 ↘ Withdrawn
                 ↘ Expired
                 ↘ Invalidated
         → Refused
```

| Status | Meaning | Data Processing |
|--------|---------|-----------------|
| **Requested** | Awaiting response | Not allowed |
| **Given** | Actively consented | Allowed |
| **Renewed** | Re-confirmed after expiry | Allowed |
| **Refused** | Declined to consent | Not allowed |
| **Withdrawn** | Previously given, now revoked | Must stop |
| **Expired** | Past validity date | Not allowed |
| **Invalidated** | Voided due to breach/error | Not allowed |

### Privacy Notices

Privacy notices explain to beneficiaries:
- What data is collected
- Why it's collected (purposes)
- Who it may be shared with
- How long it's kept
- How to withdraw consent

Notices are versioned - when you update a notice, existing consents reference the version they agreed to.

### Consent purposes

Purposes define why data is processed. OpenSPP includes pre-configured purposes aligned with W3C Data Privacy Vocabulary (DPV):

**Top-level DPV purposes:**

| Purpose | Description |
|---------|-------------|
| **Service Provision** | Processing for providing a service |
| **Identity Verification** | Verifying identity |
| **Research and Development** | Research and development |
| **Legal Compliance** | Compliance with legal obligations |
| **Record Management** | Managing records |

**Social protection-specific purposes:**

| Purpose | Description |
|---------|-------------|
| **Beneficiary Registration** | Registering individuals in programs |
| **Eligibility Assessment** | Determining program eligibility |
| **Program Enrollment** | Enrolling in specific programs |
| **Benefit Delivery** | Delivering cash/in-kind benefits |
| **Grievance Handling** | Managing complaints |
| **Case Management** | Referrals and case tracking |
| **Monitoring & Evaluation** | Program monitoring and evaluation |
| **Deduplication** | Detecting duplicate registrations |
| **Inter-Agency Data Sharing** | Sharing data between agencies |

## Navigation

Consent configuration is in **Registry → Configuration → Consent Management**.

| Menu | Purpose |
|------|---------|
| **Consent Records** | View and manage individual consents |
| **Configuration → Privacy Notices** | Create and manage notice templates |
| **Configuration → Purposes (DPV)** | Configure processing purposes |
| **Configuration → Personal Data Categories** | Define personal data types |
| **Configuration → Processing Operations** | Define allowed processing operations |
| **Configuration → Organization Types** | Configure recipient categories |

```{note}
The Configuration submenu is only visible to administrators (spp_security.group_spp_admin).
```

Additionally, **Registry → Configuration → Expired Consents** provides a view of consents needing renewal.

## Common Use Cases

### Use Case 1: Basic Program Enrollment

**Goal:** Collect consent when registering beneficiaries.

**Setup:**
1. Create Privacy Notice for your program
2. Configure relevant purposes (Registration, Enrollment, Benefit Delivery)
3. Record consent during registration

### Use Case 2: Data Sharing with Partners

**Goal:** Share beneficiary data with partner organizations.

**Setup:**
1. Create Privacy Notice explaining data sharing
2. Add partner organization types
3. Record consent with specific recipients or categories
4. Configure API scopes for partner access

### Use Case 3: Research and Evaluation

**Goal:** Use program data for impact studies.

**Setup:**
1. Create separate Privacy Notice for research
2. Use "Research and Development" purpose
3. Collect explicit consent for research use
4. Configure anonymization where required

## Standards Compliance

OpenSPP's consent module follows:

| Standard | Implementation |
|----------|----------------|
| **ISO 27560** | Consent record structure and receipts |
| **W3C DPV** | Data Privacy Vocabulary for purposes, processing |
| **GDPR** | Legal basis, withdrawal, data subject rights |

## Key design patterns

### Notice as boundary

Privacy notices define the **maximum scope** of what can be consented to. When creating a consent record:

- Selected purposes must be within the notice's purpose list
- Selected data categories must be within the notice's data categories
- Selected organization types must be within the notice's allowed types

This ensures beneficiaries cannot consent to terms not described in the notice they were shown (informed consent compliance).

### Immutability after consent given

Once a consent status changes to "Given", the following fields become **immutable**:

- Parties (signatory, controller, recipients)
- Processing terms (purposes, data categories, legal basis)
- Privacy notice reference
- Validity period
- Collection method

To correct errors in a given consent, you must **invalidate** it and create a new consent record. This preserves the audit trail.

## Next steps

1. {doc}`privacy_notices` - Create your first privacy notice
2. {doc}`recording_consent` - Record consent for registrants
3. {doc}`api_consent_filtering` - Understand API consent filtering

## Are You Stuck?

**Where do I configure consent?**

Go to **Registry → Configuration → Consent Management**. Privacy notices and purposes are under the "Configuration" submenu within Consent Management. Consent is NOT configured in Studio.

**What's the difference between Privacy Notice and Consent Record?**

Privacy Notice is the template/document explaining data use. Consent Record is the individual's response to that notice (given, refused, etc.).

**Do I need consent for every beneficiary?**

Yes, if using consent as your legal basis. Alternatively, you may use "Legal Obligation" or "Public Interest" for government programs where participation is mandatory.

**How do I handle child beneficiaries?**

For children under 16, consent must come from a parent or guardian. Use the "Delegation Type" field to record who signed on behalf of the child.

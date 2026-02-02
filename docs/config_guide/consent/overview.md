---
openspp:
  doc_status: draft
  products: [core]
---

# Consent Management Overview

This guide is for **implementers** configuring consent management in OpenSPP. You should understand your program's data protection requirements but don't need programming knowledge.

## Mental Model

Consent in OpenSPP has three layers:

| Layer | What It Does | Example |
|-------|--------------|---------|
| **Privacy Notice** | Explains what data is collected and why | "Program Enrollment Notice" |
| **Consent Record** | Tracks individual's permission | "Maria Santos gave consent on 2024-03-15" |
| **Consent Scope** | Controls API access to data | "Partner X can access basic fields only" |

Think of it like this:
- **Privacy Notice** = The form explaining data use
- **Consent Record** = The signed agreement
- **Consent Scope** = The access permissions that result

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

### Consent Purposes

Purposes define why data is processed. OpenSPP includes pre-configured purposes:

| Purpose | Description |
|---------|-------------|
| **Beneficiary Registration** | Registering individuals in programs |
| **Eligibility Assessment** | Determining program eligibility |
| **Program Enrollment** | Enrolling in specific programs |
| **Benefit Delivery** | Delivering cash/in-kind benefits |
| **Grievance Handling** | Managing complaints |
| **Case Management** | Referrals and case tracking |
| **Research and Evaluation** | Program impact studies |

## Navigation

Consent configuration is in **Registry → Configuration → Consent Management**.

| Menu | Purpose |
|------|---------|
| **Consent Records** | View and manage individual consents |
| **Configuration → Privacy Notices** | Create and manage notice templates |
| **Configuration → Purposes (DPV)** | Configure processing purposes |
| **Configuration → Personal Data Categories** | Define personal data types |
| **Configuration → Organization Types** | Configure recipient categories |

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

## Next Steps

1. {doc}`privacy_notices` - Create your first privacy notice
2. {doc}`recording_consent` - Record consent for registrants
3. {doc}`api_scopes` - Configure API access control

## Are You Stuck?

**Where do I configure consent?**

Go to **Registry → Configuration → Consent Management**. Privacy notices and purposes are under the "Configuration" submenu within Consent Management. Consent is NOT configured in Studio.

**What's the difference between Privacy Notice and Consent Record?**

Privacy Notice is the template/document explaining data use. Consent Record is the individual's response to that notice (given, refused, etc.).

**Do I need consent for every beneficiary?**

Yes, if using consent as your legal basis. Alternatively, you may use "Legal Obligation" or "Public Interest" for government programs where participation is mandatory.

**How do I handle child beneficiaries?**

For children under 16, consent must come from a parent or guardian. Use the "Delegation Type" field to record who signed on behalf of the child.

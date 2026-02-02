---
openspp:
  doc_status: draft
  products: [core]
---

# Consent Configuration

**For: Implementers**

The consent system manages data sharing permissions with field-level granularity. OpenSPP V2 uses a fail-closed design - data cannot be shared without explicit consent, ensuring compliance with data protection regulations.

## What You'll Learn

This guide shows you how to create privacy notices, record beneficiary consent, manage consent lifecycles, and configure API scopes for controlled data sharing with partners.

```{toctree}
:maxdepth: 1

overview
privacy_notices
recording_consent
api_scopes
```

## Quick Links

| Topic | When to Use |
|-------|-------------|
| {doc}`overview` | Understand consent concepts, legal basis, and status lifecycle |
| {doc}`privacy_notices` | Create privacy notice templates explaining data use |
| {doc}`recording_consent` | Record individual or bulk consent from beneficiaries |
| {doc}`api_scopes` | Configure field-level API access for partners |

## Prerequisites

Before configuring consent, you should:

- Have access to **Registry → Configuration → Consent Management**
- Understand your program's data protection requirements
- Know which partner organizations need data access
- Have your privacy policy content ready for notices

## What's New in V2

OpenSPP V2 introduces comprehensive consent management:

- **Fail-Closed Design** - No data sharing without explicit consent
- **ISO 27560 Compliance** - Standards-based consent records
- **Field-Level Scopes** - Granular control over API data access
- **W3C DPV Purposes** - Pre-configured processing purposes
- **Consent Summary Caching** - Fast API filtering without per-request lookups
- **Delegation Support** - Parent/guardian consent for children
- **Multi-Language Notices** - Privacy notices in 5 languages

## Navigation

Consent configuration is in **Registry → Configuration → Consent Management**.

| Menu | Purpose |
|------|---------|
| Consent Records | View/manage individual consents |
| Configuration → Privacy Notices | Create notice templates |
| Configuration → Purposes (DPV) | Define processing purposes |
| Configuration → Personal Data Categories | Define data categories |
| Configuration → Organization Types | Define recipient types |

Additionally, **Registry → Configuration → Expired Consents** provides a view of consents needing renewal.

## Standards

OpenSPP consent follows:
- **ISO 27560** - Consent record structure
- **W3C DPV** - Data Privacy Vocabulary
- **GDPR** - General Data Protection Regulation principles

---

*This documentation covers OpenSPP V2 consent configuration for implementers.*

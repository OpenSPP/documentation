---
openspp:
  doc_status: draft
  products: [core]
---

# Consent configuration

This guide is for **implementers** configuring data sharing permissions and consent management for regulatory compliance.

## What you'll find here

- **{doc}`overview`** - Consent concepts, legal basis, and status lifecycle
- **{doc}`privacy_notices`** - Create notice templates explaining data use
- **{doc}`recording_consent`** - Record individual or bulk consent from beneficiaries
- **{doc}`api_consent_filtering`** - How consent controls API data access

```{toctree}
:hidden:
:maxdepth: 1

overview
privacy_notices
recording_consent
api_consent_filtering
```

## Quick start

To configure consent management:

1. Navigate to **Registry → Configuration → Consent Management**
2. Create a **Privacy Notice** under Configuration → Privacy Notices
3. Configure **Purposes** and **Personal Data Categories** (pre-loaded with DPV defaults)
4. Record consent from beneficiaries using the wizard or bulk import
5. Consent summary is automatically cached on registrants for API filtering

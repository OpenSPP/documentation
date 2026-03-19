---
openspp:
  doc_status: draft
---

# Consent

**Module:** `spp_consent`

## Overview

This reference is for **implementers** and **sys admins** who need to understand consent management capabilities and configuration options.

The Consent module provides standards-compliant consent management for social protection programs. It tracks explicit consent from individuals and groups, supporting both GDPR compliance and international data privacy standards.

Use this module when your program needs to:

- Record and track beneficiary consent for data collection and sharing
- Support category-based consent (e.g., "share with all NGOs")
- Maintain audit trails for accountability requirements
- Export consent records in interoperable formats

## Standards Compliance

| Standard              | Description                           |
| --------------------- | ------------------------------------- |
| ISO/IEC TS 27560:2023 | Consent record information structure  |
| ISO/IEC 29184:2020    | Online privacy notices and consent    |
| W3C DPV v2            | Data Privacy Vocabulary for semantics |
| GDPR                  | Articles 6, 7, and 9 compliance       |

## Module Dependencies

| Dependency     | Purpose                              |
| -------------- | ------------------------------------ |
| `base`         | Odoo core framework                  |
| `mail`         | Communication and activity tracking  |
| `spp_registry` | Registrant data for consent subjects |
| `spp_security` | Security groups and access control   |

## Key Features

### Consent Record Structure

Implements ISO 27560's four-section structure:

| Section           | Contents                                           |
| ----------------- | -------------------------------------------------- |
| Header/Metadata   | External ID, schema version, timestamps            |
| Parties           | Data subject, controller, recipients, delegation   |
| Processing        | Purposes, legal basis, data categories, operations |
| Consent Specifics | Status, validity period, withdrawal mechanism      |

### Consent Status Lifecycle

| Status      | Description                           |
| ----------- | ------------------------------------- |
| Requested   | Consent has been requested            |
| Given       | Consent actively granted              |
| Renewed     | Consent renewed after expiry          |
| Refused     | Consent explicitly refused            |
| Withdrawn   | Previously given consent withdrawn    |
| Expired     | Consent validity period has ended     |
| Invalidated | Consent invalidated for other reasons |

### Two-Mode Consent Matching

**Specific Organization Mode:**
Traditional consent where beneficiaries explicitly consent to named organizations.

**Category-Based Mode:**
Flexible consent where beneficiaries consent to organization categories:

| Example                                                              |
| -------------------------------------------------------------------- |
| "I consent to share with all NGOs and UN agencies"                   |
| "I consent to share with government agencies but not private sector" |

### DPV Taxonomies

**Purpose Hierarchy:**

| Category          | Examples                     |
| ----------------- | ---------------------------- |
| Service Provision | Enrollment, benefit delivery |
| Personalisation   | Targeting, recommendations   |
| Research          | Analytics, impact evaluation |

**Personal Data Categories:**

| Type              | Examples                              |
| ----------------- | ------------------------------------- |
| Regular           | Name, address, phone                  |
| Sensitive (Art.9) | Health, biometric, racial/ethnic data |

**Processing Operations:**

| Operation | Risk Level |
| --------- | ---------- |
| Collect   | Low        |
| Store     | Low        |
| Use       | Medium     |
| Share     | High       |
| Delete    | Low        |

### Collection Methods

| Method           | Description                    |
| ---------------- | ------------------------------ |
| Written          | Signed paper form              |
| Verbal Witnessed | Verbal consent with witness    |
| Electronic       | Digital consent via system     |
| Biometric        | Fingerprint or other biometric |

## Data Models

| Model                       | Purpose                                 |
| --------------------------- | --------------------------------------- |
| `spp.consent`               | Main consent record (ISO 27560)         |
| `spp.consent.history`       | Version history for audit trail         |
| `spp.consent.purpose`       | DPV-aligned purpose taxonomy            |
| `spp.consent.personal.data` | DPV-aligned data categories             |
| `spp.consent.processing`    | DPV-aligned processing operations       |
| `spp.consent.notice`        | ISO 29184 privacy notices               |
| `spp.consent.org.type`      | Organization type categories            |
| `spp.consent.mixin`         | Mixin to add consent tracking to models |

## Security Model

Follows the three-tier access control pattern:

| Role    | Permissions                                |
| ------- | ------------------------------------------ |
| Viewer  | Read-only access to consent records        |
| Officer | Create and modify consent records          |
| Manager | Full CRUD including taxonomy configuration |

## Technical Details

| Property       | Value         |
| -------------- | ------------- |
| Technical Name | `spp_consent` |
| Category       | OpenSPP       |
| Version        | 19.0.2.0.0    |
| License        | LGPL-3        |
| Application    | No            |

## Integration

### Checking Consent Programmatically

Use the `check_consent()` method to validate consent before data sharing:

```python
consent_valid = registrant.check_consent(
    purpose='service_provision',
    recipient_org_type='ngo'
)
```

### Export Formats

| Format          | Description                      |
| --------------- | -------------------------------- |
| JSON-LD         | W3C standard with DPV vocabulary |
| Consent Receipt | ISO 27560 standardized receipt   |

## User Interface

| Feature              | Description                                    |
| -------------------- | ---------------------------------------------- |
| Recording Wizard     | User-friendly consent recording with filtering |
| Expired Consent View | Identify and manage expired consents           |
| Bulk Recording       | Record consent for multiple registrants        |

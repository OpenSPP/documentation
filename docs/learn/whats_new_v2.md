---
openspp:
  doc_status: draft
  products: [core]
---

# What's New in OpenSPP V2

**For:** All audiences

OpenSPP V2 is a major platform evolution bringing modern architecture, enhanced security, and powerful new features for social protection programs.

## Executive Summary

| Area | What's New |
|------|------------|
| **Foundation** | Odoo 19 with improved performance |
| **Architecture** | Unified `spp.*` namespace, streamlined modules |
| **API** | REST API V2 with OAuth 2.0 and bundle transactions |
| **Standards** | DCI integration, W3C Verifiable Credentials |
| **Security** | Data classification, PII encryption, field-level access |
| **Configuration** | OpenSPP Studio for no-code customization |
| **Data Management** | Configuration-driven change requests, enhanced event tracking |
| **Grievances** | Built-in GRM module for complaints and appeals |

## Platform Changes

### Odoo 19 Upgrade

OpenSPP V2 runs on Odoo 19:

- **Performance**: 2-3x faster database queries with PostgreSQL 17/18
- **UI/UX**: Modern interface with improved mobile support
- **Security**: Updated cryptography and security patches
- **Requirements**: Python 3.11+, PostgreSQL 12+ (17/18 recommended)

### New Namespace

All modules now use the unified `spp.*` namespace.

| Before | After |
|--------|-------|
| Mixed `g2p.*` and `spp.*` | Everything is `spp.*` |
| Unclear ownership | Clear OpenSPP identity |

**Migration**: Automatic database scripts handle the rename. External integrations need to update model references from `g2p.*` to `spp.*`.

## New Features

### API V2

A complete API redesign using FastAPI and FHIR-inspired patterns:

- **External identifiers only**: Never exposes database IDs
- **Consent-based filtering**: Field-level access based on user consent
- **Bundle transactions**: Atomic multi-operation requests
- **OAuth 2.0**: JWT tokens with scoped access
- **Performance**: <100ms for single reads, <500ms for 100-result searches

### DCI Compliance

Native Digital Convergence Initiative (DCI) integration for government interoperability:

- **Social Registry Server**: Expose beneficiary data to MIS systems
- **CRVS Client**: Import birth/death events from civil registration
- **IBR Client**: Check enrollment in other programs (prevent duplication)
- **Federated Lookups**: Query other social registries

### Verifiable Credentials

Issue cryptographically verifiable credentials for beneficiaries:

| Credential Type | Purpose |
|-----------------|---------|
| Entitlement | Prove benefit eligibility |
| Program Membership | Prove enrollment |
| Profile/Identity | Prove identity |

Features selective disclosure (holder chooses what to reveal), offline verification, and efficient revocation checking.

### OpenSPP Studio

No-code configuration for implementers who work with tools like KoBoToolbox:

- **Registry Field Builder**: Add custom fields without developers
- **Event Type Designer**: Create event types, import from Kobo
- **Change Request Builder**: Define modification workflows
- **Eligibility Rule Builder**: Visual criteria, auto-generates CEL

See {doc}`/config_guide/studio/index` for details.

### Change Request V2

Replaces 10+ specialized modules with one configurable system:

- Configuration-driven: Create types without code
- 11 built-in types: Add/remove member, split/merge household, etc.
- Approval workflows with audit trails
- Event tracking for full history

See {doc}`/config_guide/change_request_types/index` for configuration.

### Grievance Redress Mechanism

Built-in module for complaints, appeals, and feedback:

- Multi-channel intake (portal, call center, field staff)
- Configurable SLAs with auto-escalation
- Appeals process with independent review
- Confidentiality handling for sensitive cases

## Security Enhancements

### Data Classification & PII Encryption

Comprehensive data protection with four sensitivity levels:

| Level | Examples | Protection |
|-------|----------|------------|
| **Public** | Program names | None |
| **Internal** | Gender, status | Audit logging |
| **Confidential** | Names, DOB | Masking, recommended encryption |
| **Restricted** | National IDs, bank accounts | Required encryption, strict access |

**Encryption features:**
- AES-256-GCM with searchable blind indexes
- Key management: Vault, AWS/GCP/Azure KMS, or config file
- Transparent to users

### Vocabulary System

Replace hardcoded selection lists with international standards:

| Domain | Standard |
|--------|----------|
| Gender | ISO 5218 |
| Disability | WHO ICF |
| Occupation | ILO ISCO-08 |
| Country | ISO 3166-1 |

Extensible via UI, multi-language, hierarchical. See {doc}`/config_guide/vocabulary/index`.

## Breaking Changes

### API

- V1 endpoints deprecated (compatibility layer available)
- Database IDs no longer exposed in responses

### Models

- All `g2p.*` models renamed to `spp.*` (automatic migration)
- Change request modules consolidated into `spp_change_request_v2`
- Some selection fields replaced with vocabulary references

### Security

- PII fields require data classification
- Field-level access control enforced
- New security groups for Studio

### Requirements

- Python 3.11+ (was 3.10+)
- PostgreSQL 12+ (17/18 recommended)

## Migration Path

### Existing V1 Deployments

**Preparation:**
1. Document current customizations and dependencies
2. Upgrade to latest V1 minor version
3. Backup database and filestore

**Database Migration:**
1. Run namespace migration scripts (`g2p.*` → `spp.*`)
2. Migrate change request data to V2 format
3. Classify existing PII fields
4. Verify data integrity

**Configuration:**
1. Update external integrations to API V2
2. Review and update security groups
3. Update custom reports and dashboards

**Deployment:**
1. Test critical workflows in staging
2. Train users on new features
3. Deploy with rollback plan

### New Deployments

1. Choose deployment profile (Agriculture, Social Protection, etc.)
2. Install core modules (typically 10-15)
3. Configure via Studio
4. Import master data (areas, programs, vocabularies)
5. Set up security and go live

See {doc}`/get_started/index` to begin.

## Next Steps

- {doc}`/get_started/index` - Install and set up your first program
- {doc}`/config_guide/index` - Configure OpenSPP for your needs
- {doc}`/learn/concepts/index` - Understand core concepts

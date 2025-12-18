---
openspp:
  doc_status: draft
---

# What's New in OpenSPP V2

**For:** All audiences (overview document)

OpenSPP V2 represents a major evolution of the platform, bringing modern architecture, enhanced security, and powerful new features for social protection programs worldwide.

## Executive Summary

V2 delivers significant improvements across the entire platform:

- **Modern Foundation**: Odoo 19 with improved performance and user experience
- **Clean Architecture**: Unified `spp.*` namespace and streamlined module structure
- **Standards Compliance**: REST API V2, DCI integration, and W3C Verifiable Credentials
- **Enhanced Security**: Data classification, PII encryption, and field-level access control
- **Better Interoperability**: International vocabulary standards and flexible data exchange
- **No-Code Configuration**: OpenSPP Studio for customization without developers
- **Improved Data Management**: Configuration-driven change requests and enhanced event tracking
- **Grievance Handling**: Built-in GRM module for complaints and appeals

## What's New

### Odoo 19 Upgrade

OpenSPP V2 runs on Odoo 19, bringing:

- **Performance improvements**: 2-3x faster database queries with PostgreSQL 17/18 async I/O
- **Better UI/UX**: Modern interface with improved mobile support
- **Security enhancements**: Updated cryptography and security patches
- **Developer experience**: Improved debugging and development tools

**Migration note**: Odoo 19 requires Python 3.11+ and PostgreSQL 12+ (17/18 recommended).

### New Namespace: spp.*

All modules now use the unified `spp.*` namespace (98% complete).

**Before:**
- Mixed `g2p.*` and `spp.*` namespaces
- Unclear ownership
- Confusing module dependencies

**After:**
- Everything is `spp.*`
- Clear OpenSPP identity
- Simpler architecture

**Migration path**: Automatic database migration scripts handle the rename. External integrations need to update model references from `g2p.*` to `spp.*`.

**See**: {doc}`/technical_reference/architecture/adr-001-namespace-migration`

### API V2: Modern REST Interface

A complete redesign of the external API using FastAPI and FHIR-inspired patterns.

**Key Features:**

- **External identifiers only**: Never exposes database IDs for security
- **Consent-based filtering**: Field-level data access control based on user consent
- **Bundle transactions**: Atomic multi-operation requests with placeholder resolution
- **Capability discovery**: `/metadata` endpoint describes available resources and operations
- **OAuth 2.0**: Secure authentication with JWT tokens and scoped access
- **Extension-friendly**: Dynamically discovers fields added by modules

**Example: Bundle Transaction**
```json
POST /api/v2/spp/$batch
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "request": {"method": "POST", "url": "Individual"},
      "resource": {
        "identifier": [{"system": "urn:gov:ph:psa", "value": "123456"}],
        "name": {"given": "Maria", "family": "Santos"}
      },
      "fullUrl": "urn:uuid:temp-1"
    },
    {
      "request": {"method": "POST", "url": "ProgramMembership"},
      "resource": {
        "beneficiary": {"reference": "urn:uuid:temp-1"},
        "program": {"reference": "Program/4Ps"}
      }
    }
  ]
}
```

**Performance**: Targets <100ms for single read, <500ms for 100-result search.

**See**: {doc}`/technical_reference/architecture/adr-010-api-v2-architecture`

### DCI Compliance: Digital Public Infrastructure Integration

Native integration with Digital Convergence Initiative (DCI) standards for government interoperability.

**What it enables:**

- **Social Registry Server**: Expose beneficiary data to MIS systems
- **CRVS Client**: Import birth/death events from civil registration systems
- **IBR Client**: Check if beneficiaries are enrolled in other programs (prevent duplication)
- **Disability Registry Client**: Query PWD status for eligibility targeting
- **Federated Lookups**: Query other social registries in the ecosystem

**Architecture:**
```
OpenSPP can be both:
- Server: Expose registry via DCI API (/registry/search, /registry/subscribe)
- Client: Consume data from CRVS, IBR, disability registries
```

**Standards**: Implements DCI message envelope with HTTP Signature (ed25519/RSA256), async request/response patterns, and webhook notifications.

**See**: {doc}`/technical_reference/architecture/adr-015-dci-api-integration`

### Verifiable Credentials: Digital Identity for Beneficiaries

Issue cryptographically verifiable credentials that beneficiaries can use to prove their status.

**Supported Standards:**
- W3C Verifiable Credentials Data Model 2.0
- OpenID for Verifiable Credential Issuance (OpenID4VCI) 1.0
- SD-JWT VC (Selective Disclosure JWT)
- Bitstring Status List 1.0 (revocation)

**Credential Types:**

| Type | Purpose | Disclosable Fields |
|------|---------|-------------------|
| Entitlement Credential | Prove benefit eligibility | Amount, program, validity period |
| Program Membership | Prove enrollment | Program, status, enrollment date |
| Profile/Identity | Prove identity | Name, DOB, national ID |

**Security Features:**
- **Selective Disclosure**: Holder chooses what to reveal (via SD-JWT)
- **Key Binding JWT**: Prevents credential theft and replay attacks
- **Revocation**: Efficient status checking via compressed bitstring
- **Offline Verification**: No need to contact registry in real-time

**Implementation Status**: Alpha (Phase 1-2 complete). Core infrastructure production-ready.

**See**: {doc}`/technical_reference/architecture/adr-006-verifiable-credentials`

### Enhanced Security: Data Classification and PII Encryption

V2 introduces comprehensive data protection for sensitive information.

#### Data Classification System

Four sensitivity levels with automated detection:

| Level | Example Fields | Encryption | Masking | Audit |
|-------|---------------|------------|---------|-------|
| **PUBLIC** | Program names | No | No | No |
| **INTERNAL** | Gender, status | No | No | Yes |
| **CONFIDENTIAL** | Names, DOB | Recommended | Yes | Yes |
| **RESTRICTED** | National IDs, bank accounts | Required | Yes | Yes |

**Auto-Detection**: Scans field names for patterns (e.g., `*_id`, `phone`, `birthdate`) and suggests classifications.

**Policy Enforcement**: Automatically applies masking, access control, and audit logging based on classification.

**See**: {doc}`/technical_reference/architecture/adr-011-data-classification`

#### PII Encryption

Application-level encryption for high-value fields:

- **Algorithm**: AES-256-GCM with random nonce
- **Blind Indexes**: Searchable encryption via HMAC-SHA256 indexes
- **Key Management**: 6 providers (config file, database, Vault, AWS KMS, GCP KMS, Azure Key Vault)
- **Transparent UX**: Users work normally, encryption is invisible

**What's Encrypted:**
- National IDs and identity documents
- Bank account numbers
- Phone numbers (with partial matching)
- Addresses for registrants

**Implementation Status**: Phase 1 complete (~75-80%). Core infrastructure production-ready, payment data encryption pending.

**See**: {doc}`/technical_reference/architecture/adr-012-pii-encryption`

### Vocabulary System: International Standards

Replace hardcoded selection lists with flexible vocabulary codes based on international standards.

**Before:**
```python
gender = fields.Selection([
    ("male", "Male"),
    ("female", "Female"),
])
```

**After:**
```python
gender_id = fields.Many2one(
    "spp.vocabulary.code",
    domain="[('namespace_uri', '=', 'urn:iso:std:iso:5218')]"
)
```

**Supported Standards:**

| Domain | Standard | Namespace |
|--------|----------|-----------|
| Gender | ISO 5218 | `urn:iso:std:iso:5218` |
| Disability | WHO ICF | `urn:who:icf:b` |
| Occupation | ILO ISCO-08 | `urn:ilo:isco-08` |
| Country | ISO 3166-1 | `urn:iso:std:iso:3166-1` |
| Currency | ISO 4217 | `urn:iso:std:iso:4217` |
| Crops | FAO AGROVOC | `urn:fao:agrovoc` |
| Education | UNESCO ISCED | `urn:unesco:isced:2011` |

**Benefits:**
- **Extensible**: Add codes via UI without code changes
- **Interoperable**: Map between different vocabularies
- **Translatable**: Multi-language support via Odoo i18n
- **Hierarchical**: Support for parent/child relationships
- **Cacheable**: O(1) lookups with `@ormcache`

**See**: {doc}`/technical_reference/architecture/adr-009-terminology-system`

### OpenSPP Studio: No-Code Configuration

A user-friendly interface for program staff to customize OpenSPP without developer involvement.

**Target User**: "The Program Configurator" - someone who builds KoboToolbox forms, manages ODK projects, comfortable with spreadsheets but not a developer.

**What You Can Configure:**

#### Registry Field Builder
- Add custom fields to Individual and Group registries
- Choose field type (text, number, date, selection, yes/no)
- Place fields in existing tabs and sections
- Set validation rules (required, read-only, conditional visibility)

#### Event Type Designer
- Create new event/survey data types
- Import field definitions from KoBoToolbox forms
- Configure lifecycle rules (one active per registrant, auto-expire)
- Link to change request workflows

#### Change Request Builder
- Define new types of registry modification requests
- Map form fields to registry updates
- Configure approval workflows (simple, two-level, custom)
- Set auto-apply on approval

#### Eligibility Rule Builder
- Visual interface for program eligibility criteria
- Condition types: registry fields, event data, group membership, location
- Automatically generates CEL expressions
- Test rules with live match counts

**Studio Packages**: Pre-built configuration templates for common use cases (Cash Transfer Basic, Vulnerability Assessment, 4Ps/Pantawid, etc.)

**Implementation Status**: Draft specification. Module structure defined, implementation in progress.

**See**: {doc}`/howto/configurator_guides/studio_overview`

### Change Request V2: Configuration-Driven

Replaces 10+ specialized change request modules with one configurable system.

**Key Improvements:**

- **Configuration-driven**: Create CR types without code via Studio
- **Real Odoo fields**: Uses actual database fields, not JSON storage
- **11 built-in types**: Add/remove member, split/merge household, update details, etc.
- **Detail-model pattern**: Each CR type has its own detail model for type safety
- **Apply strategies**: Field mapping, method-based, or custom Python code
- **Approval integration**: Built-in workflow with audit trails
- **Event tracking**: State transitions create `spp.event.data` records for full audit trail

**Implementation Status**: Implemented and complete. Old CR modules deprecated.

**See**: {doc}`/howto/implementer_guides/change_requests`

### Event Data Improvements

Enhanced event tracking system integrated with change requests and approvals.

**New Features:**

- **Audit Events**: All change request state transitions automatically logged
- **Event Types**: Configurable via Studio, including JSON-based storage
- **Change Request Integration**: Events can trigger CRs when data differs from registry
- **Lifecycle Management**: One active event per registrant, auto-expiration, approval workflows
- **External Sources**: Import from KoboToolbox/ODK with field mapping

**Event Categories:**
- Survey/Assessment
- Field Visit
- Data Sync
- Change Request Audit
- Manual Entry

**See**: {doc}`/technical_reference/architecture/adr-002-change-request-event-integration`

### Grievance Redress Mechanism (GRM)

Built-in module for handling complaints, appeals, and feedback.

**Core Features:**

- **Multi-Channel Intake**: Portal, call center, field staff, paper forms, bulk imports
- **Classification System**: Categories, subcategories, severity, sensitivity levels
- **Configurable SLAs**: Different timelines per category/severity with auto-escalation
- **Appeals Process**: Complainants can appeal decisions with independent review
- **Case Management Integration**: Link grievances to case records when appropriate
- **Confidentiality**: Special handling for sensitive cases (GBV, child abuse, corruption)

**Workflow States:**
Draft → Registered → In Review → Pending Information → Escalated → Decision Pending → Resolved → Closed

**Implementation Status**: Specification complete, implementation planned.

**See**: {doc}`/technical_reference/architecture/grm_module_specification`

### Module Consolidation

Simplifying the module structure from 153 to ~77 modules (23% complete).

**Principle**: Merge modules that ALWAYS go together, keep modules that represent real user choices.

**Completed Consolidations:**

| Before | After | Status |
|--------|-------|--------|
| 10+ `spp_change_request_*` | `spp_change_request_v2` | ✅ Done |
| 7 registry modules | `spp_registry` | ✅ Done |
| 3 approval modules | `spp_approval` | ✅ Done |
| 3 registry approval modules | `spp_registry_approval` | ✅ Done |
| 3 audit modules | `spp_audit` | ✅ Done |
| 4 custom filter modules | `spp_custom_filter` | ✅ Done |
| 2 programs modules | `spp_programs` | ✅ Done |

**Deployment Profiles**: Clear guidance for Agriculture, Social Protection, Emergency Response, DPI-Integrated, Case Management, and Education use cases.

**See**: {doc}`/technical_reference/architecture/adr-013-module-consolidation`

## Migration Path

### For Existing OpenSPP V1 Deployments

**Phase 1: Preparation**
1. Review current customizations and document dependencies
2. Upgrade to latest V1 minor version
3. Backup database and filestore
4. Test backup restoration

**Phase 2: Database Migration**
1. Run namespace migration scripts (`g2p.*` → `spp.*`)
2. Migrate change request data to V2 format
3. Classify existing PII fields (optional but recommended)
4. Verify data integrity

**Phase 3: Configuration Migration**
1. Update external integrations to use API V2 endpoints
2. Migrate custom fields to Studio (optional)
3. Review and update security groups
4. Update custom reports and dashboards

**Phase 4: Testing and Deployment**
1. Test critical workflows in staging environment
2. Train users on new features
3. Deploy to production with rollback plan
4. Monitor performance and logs

**Estimated Timeline**: 2-4 weeks for small deployments, 2-3 months for large/complex deployments with extensive customizations.

### For New Deployments

New deployments start with V2 directly:

1. **Choose Deployment Profile**: Agriculture, Social Protection, Emergency Response, etc.
2. **Install Core Modules**: Based on profile (typically 10-15 modules)
3. **Configure via Studio**: Add custom fields, event types, eligibility rules
4. **Import Master Data**: Areas, programs, vocabularies
5. **Set Up Security**: Users, roles, data classification
6. **Go Live**: Start registering beneficiaries

**Getting Started**: {doc}`/tutorials/getting_started`

## Release Timeline

| Milestone | Target | Status |
|-----------|--------|--------|
| Odoo 19 Upgrade | Q4 2024 | ✅ Complete |
| Namespace Migration | Q4 2024 | ✅ 98% Complete |
| Change Request V2 | Q4 2024 | ✅ Complete |
| Registry Consolidation | Q1 2025 | ✅ Complete |
| API V2 Core | Q1 2025 | ✅ Complete |
| DCI Integration | Q1 2025 | ✅ Complete |
| Verifiable Credentials | Q1 2025 | ⚠️ Alpha |
| Data Classification | Q1 2025 | ✅ Complete |
| PII Encryption | Q1 2025 | ⚠️ Phase 1 Complete |
| Vocabulary System | Q1 2025 | ✅ Complete |
| OpenSPP Studio | Q2 2025 | 🚧 In Progress |
| GRM Module | Q2 2025 | 📋 Planned |
| Module Consolidation | Q3 2025 | ⚠️ 23% Complete |
| V2 Production Release | Q3 2025 | 🎯 Target |

## Breaking Changes

**API:**
- V1 API endpoints deprecated (6-month transition period with compatibility layer)
- Database IDs no longer exposed in API responses

**Models:**
- All `g2p.*` models renamed to `spp.*` (automatic migration)
- Change request modules consolidated into `spp_change_request_v2`
- Selection fields replaced with vocabulary references in some models

**Security:**
- PII fields now require data classification
- Field-level access control enforced based on classification
- New security groups for Studio configuration

**Python/Code:**
- Python 3.11+ required (was 3.10+)
- PostgreSQL 12+ required (17/18 recommended)
- Some deprecated Odoo 17 patterns removed

## Performance Improvements

- **Database Queries**: 2-3x faster with PostgreSQL 17/18 async I/O
- **API Response**: <100ms target for single resource reads
- **Batch Operations**: Optimized with queue_job for large-scale operations
- **Caching**: O(1) vocabulary lookups with `@ormcache`
- **Connection Pooling**: PgBouncer support for high concurrency

## Documentation Updates

All documentation has been updated for V2:

- **Tutorials**: New user getting started guides
- **How-To Guides**: Updated for all audiences (Users, Implementers, Developers, Sys Admins)
- **Technical Reference**: Complete API documentation and ADRs
- **Explanation**: Architecture overviews and design decisions

**See**: {doc}`/index`

## Community and Support

- **Source Code**: [GitHub - OpenSPP](https://github.com/OpenSPP/openspp-modules-v2)
- **Discussion**: [GitHub Discussions](https://github.com/OpenSPP/openspp-modules/discussions)
- **Bug Reports**: [GitHub Issues](https://github.com/OpenSPP/openspp-modules/issues)
- **Documentation**: [OpenSPP Docs](https://docs.openspp.org)

## Credits

OpenSPP V2 represents contributions from:

- OpenSPP Core Team
- Government implementing agencies
- UN agencies and NGO partners
- Open-source community contributors

Thank you to everyone who made V2 possible!

---

**Next Steps:**
- Review the {doc}`/technical_reference/architecture/v2_architecture` for technical details
- Check out {doc}`/tutorials/getting_started` to begin using V2
- Join our [community discussions](https://github.com/OpenSPP/openspp-modules/discussions) to share feedback

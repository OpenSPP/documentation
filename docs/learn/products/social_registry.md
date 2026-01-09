---
openspp:
  doc_status: draft
  products: [core]
---

# Social Registry

A Social Registry is a centralized database of households and individuals used for identifying, registering, and assessing vulnerable populations. OpenSPP's Social Registry provides the foundation for all social protection programs.

**Who is this for:** National governments building population registries, humanitarian organizations managing beneficiary databases, registration agencies needing interoperability with external systems.

## What Social Registry Does

When deploying social protection programs, you need to know who is eligible and how to reach them. Social Registry provides:

- **Unified registration** for individuals and households with flexible data collection
- **Deduplication** to prevent duplicate registrations across programs
- **Eligibility assessment** using configurable rules and proxy means testing
- **Change request workflows** for managing data updates and corrections
- **External integration** with CRVS, national ID, and other government systems
- **Standards-aligned API** for secure data sharing with authorized systems

## Core Workflows

| Workflow | Purpose | Key Users |
|----------|---------|-----------|
| **Registration** | Collect demographic, socioeconomic, and household data | Registrars, Enumerators |
| **Deduplication** | Identify and merge duplicate records | Data Managers |
| **Eligibility Assessment** | Apply criteria to identify eligible populations | Program Managers |
| **Data Maintenance** | Process updates, corrections, and appeals | Registrars, Validators |

## Key Capabilities

### Registry Management

- **Individuals and groups** - Register both individuals and households/groups
- **Flexible data model** - Custom fields for country-specific requirements
- **Geographic hierarchy** - Organize by administrative areas (region, district, village)
- **Document management** - Store and verify identity documents

### Change Request System

OpenSPP includes 11 change request types for managing data throughout the beneficiary lifecycle:

| Change Request | Purpose |
|----------------|---------|
| New Registration | Add new individuals or groups |
| Add Member | Add members to existing groups |
| Update Info | Modify demographic or contact data |
| Update Live Status | Record births, deaths, migrations |
| Split Group | Divide a household into separate units |
| Merge Group | Combine multiple households |
| Assign to Program | Request enrollment in a program |

All changes flow through configurable approval workflows.

### API & Integration

- **DCI-compliant API** - Standards-aligned integration with Digital Convergence Initiative
- **CRVS integration** - Connect to civil registration systems (OpenCRVS compatible)
- **National ID lookup** - Verify identity against national ID databases
- **Consent management** - Track and enforce data sharing consent

### Search & Filtering

- **CEL expressions** - Build powerful filters using Common Expression Language
- **Saved searches** - Store and reuse complex search criteria
- **Bulk operations** - Apply actions to filtered result sets

## How It Works

```{mermaid}
graph LR
    A[Data<br/>Collection] --> B[Validation &<br/>Deduplication]
    B --> C[Eligibility<br/>Assessment]
    C --> D[Enroll in<br/>Programs]
    E[Change<br/>Requests] --> B
```

1. **Data collection** - Registrants provide information via surveys, field registration, or self-registration
2. **Validation** - Data is verified against documents and cross-checked with other systems
3. **Deduplication** - Matching algorithms identify potential duplicates for review
4. **Eligibility assessment** - Configurable rules (including proxy means testing) rank households
5. **Program enrollment** - Eligible registrants are enrolled in social protection programs
6. **Ongoing updates** - Change requests maintain data accuracy over time

## Security & Access Control

| Role | Access Level | Typical Users |
|------|--------------|---------------|
| Registry Viewer | Read-only access to registry data | Coordination staff, auditors |
| Registrar | Create and update registrations | Field officers, enumerators |
| Validator | Approve registrations and changes | Supervisors, data managers |
| Registry Manager | Full administration and configuration | System administrators |

## Dependencies

Social Registry is the foundation module that other products build upon:

- **spp_registry** - Core registry data model
- **spp_change_request_v2** - Change request workflows
- **spp_dci_client** - External registry integration
- **spp_api_v2** - REST API for data exchange
- **spp_studio** - No-code expression builder
- **spp_area** - Geographic hierarchy management
- **spp_consent** - Data sharing consent tracking

## Next Steps

**New to Social Registry?**
- {doc}`/get_started/installation/docker` - Install OpenSPP with demo data
- {doc}`/user_guide/index` - Learn the interface

**Setting up for your organization?**
- {doc}`/config_guide/index` - Configuration overview

**Understanding the concepts?**
- {doc}`/learn/concepts/registry` - Registry concepts explained

## Learn More

- [World Bank Social Registries Sourcebook](https://openknowledge.worldbank.org/entities/publication/c44dc506-72dd-5428-a088-6fb7aea53095) - Comprehensive guidance on social registry design
- [Digital Convergence Initiative](https://spdci.org/) - Interoperability standards for social protection
- [GIZ Dynamic Inclusion](https://socialprotection.org/sites/default/files/publications_files/GIZ_DataUpdatingForSocialAssistance_3.pdf) - On-demand registration approaches

## Global Examples

Social registries are used in over 50 countries:

| Country | Registry | Notable Features |
|---------|----------|------------------|
| Brazil | Cadastro Único | Dynamic registration, used by 27+ programs |
| Pakistan | NSER | National scale, biometric integration |
| Indonesia | DTKS | Integrated with multiple welfare programs |
| Colombia | Sisbén | Multidimensional targeting |

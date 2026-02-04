---
openspp:
  doc_status: draft
  products: [core]
---

# Security

This guide is for **sys admins** deploying and maintaining OpenSPP production systems.

OpenSPP handles sensitive personal data for vulnerable populations. This section covers the security infrastructure you need to configure and maintain.

## What's in This Section

| Topic | What You'll Configure |
|-------|----------------------|
| {doc}`access_control` | User roles, permissions, RBAC hierarchy |
| {doc}`data_classification` | Data sensitivity levels, PII tagging |
| {doc}`pii_encryption` | Field-level encryption for sensitive data |
| {doc}`key_management` | Encryption keys, rotation, backup |
| {doc}`audit` | Access logging, compliance reporting |
| {doc}`scanning` | Security scanning (SAST, SCA, DAST) |

## Security Architecture Overview

OpenSPP uses a layered security approach:

```{mermaid}
flowchart TB
    L5["<b>Layer 5: Audit & Compliance</b><br/>Access logging, DSAR handling, compliance reports"]
    L4["<b>Layer 4: Application Encryption</b><br/>AES-256-GCM field encryption, blind indexes"]
    L3["<b>Layer 3: Access Control</b><br/>RBAC, field-level permissions, record rules"]
    L2["<b>Layer 2: Database Security</b><br/>PostgreSQL TDE, connection encryption"]
    L1["<b>Layer 1: Infrastructure</b><br/>Network security, firewalls, SSL/TLS"]

    L5 --> L4 --> L3 --> L2 --> L1
```

## Quick Security Checklist

Before going to production:

- [ ] Configure user roles and permissions ({doc}`access_control`)
- [ ] Tag all PII fields with classification levels ({doc}`data_classification`)
- [ ] Enable encryption for RESTRICTED fields ({doc}`pii_encryption`)
- [ ] Set up key management provider ({doc}`key_management`)
- [ ] Enable audit logging ({doc}`audit`)
- [ ] Configure database TDE
- [ ] Enable SSL/TLS for all connections
- [ ] Set up backup encryption
- [ ] Test DSAR export procedures
- [ ] Run security scans ({doc}`scanning`)
- [ ] Review security logs

## Deployment Tiers

| Tier | Use Case | Key Management | Encryption |
|------|----------|----------------|------------|
| Development | Testing only | Config file | Optional |
| Standard | Small deployments | Database + master key | Required for RESTRICTED |
| Enterprise | Large/regulated | HashiCorp Vault | Required for all PII |
| Cloud | AWS/Azure/GCP | Cloud KMS | Required for all PII |

```{toctree}
:maxdepth: 2
:hidden:

access_control
data_classification
pii_encryption
key_management
audit
scanning
```

## Related Documentation

- Network security and firewall configuration: See deployment guides
- Backup security: See {doc}`../backup/index`
- SSL/TLS setup: See {doc}`../deployment/index`

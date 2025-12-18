---
openspp:
  doc_status: draft
---

# Data Classification

This guide is for **sys admins** configuring data sensitivity levels in OpenSPP.

Data classification tags fields by sensitivity level. This drives encryption, masking, and access policies.

## Why Classify Data

Without classification:
- Don't know which fields contain PII
- Can't enforce encryption policies
- Can't comply with GDPR/regulations
- Can't answer "what data do we have?"

With classification:
- Fields tagged by sensitivity
- Encryption auto-applied to RESTRICTED fields
- Access controls based on clearance
- DSAR (Data Subject Access Request) exports work

## Classification Levels

OpenSPP defines 4 default levels:

| Level | Code | Encryption | Masking | Audit | Examples |
|-------|------|------------|---------|-------|----------|
| Public | `PUBLIC` | No | No | No | Program names, public stats |
| Internal | `INTERNAL` | No | No | Yes | Gender, enrollment status |
| Confidential | `CONFIDENTIAL` | Recommended | Yes | Yes | Names, DOB, addresses |
| Restricted | `RESTRICTED` | Required | Yes | Yes | National IDs, bank accounts |

## Checking Current Classifications

### Via Web UI

Navigate to **Settings → Data Classification → Field Classifications**

Filter by:
- Model (e.g., `res.partner`)
- Classification level
- PII category

### Via Shell

```bash
odoo-bin shell -d openspp_prod

# List all classified fields
classifications = env['spp.field.classification'].search([])
for c in classifications:
    print(f"{c.model_id.model}.{c.field_id.name}: {c.classification_id.code}")

# Find RESTRICTED fields
restricted = env.ref('spp_data_classification.level_restricted')
fields = env['spp.field.classification'].search([
    ('classification_id', '=', restricted.id)
])
for f in fields:
    print(f"  - {f.model_id.model}.{f.field_id.name}")

# Find unclassified likely-PII fields
detector = env['spp.field.classification.detector'].create({})
detector.action_detect()
print(f"Found {len(detector.suggestion_ids)} suggestions")
```

### Via Database

```sql
-- List classified fields by level
SELECT
    m.model,
    f.name as field_name,
    l.code as level,
    fc.pii_category
FROM spp_field_classification fc
JOIN ir_model m ON m.id = fc.model_id
JOIN ir_model_fields f ON f.id = fc.field_id
JOIN spp_data_classification_level l ON l.id = fc.classification_id
ORDER BY l.sequence DESC, m.model;

-- Count classifications by level
SELECT l.name, COUNT(*) as field_count
FROM spp_field_classification fc
JOIN spp_data_classification_level l ON l.id = fc.classification_id
GROUP BY l.name
ORDER BY l.sequence DESC;
```

## Adding Classifications

### Via Web UI

1. Navigate to **Settings → Data Classification → Field Classifications**
2. Click **New**
3. Select:
   - **Model**: The model (e.g., `res.partner`)
   - **Field**: The field name (e.g., `birthdate`)
   - **Classification**: Level (e.g., `CONFIDENTIAL`)
   - **PII Category**: Type of data (e.g., `quasi_id`)
4. Configure:
   - **Mask Pattern**: How to display (e.g., `****-**-##` for dates)
   - **Search Strategy**: How to search encrypted data
   - **Legal Basis**: Why you process this data
5. Click **Save**

### Via XML Data

```xml
<!-- In custom module's data files -->
<odoo noupdate="1">
    <record id="classify_custom_field" model="spp.field.classification">
        <field name="model_id" ref="base.model_res_partner"/>
        <field name="field_id" ref="module_name.field_res_partner__custom_field"/>
        <field name="classification_id" ref="spp_data_classification.level_confidential"/>
        <field name="pii_category">contact</field>
        <field name="mask_pattern">****####</field>
        <field name="search_strategy">partial_index</field>
        <field name="legal_basis">consent</field>
    </record>
</odoo>
```

### Via Shell

```bash
odoo-bin shell -d openspp_prod

# Get model and field
model = env['ir.model'].search([('model', '=', 'res.partner')])
field = env['ir.model.fields'].search([
    ('model_id', '=', model.id),
    ('name', '=', 'phone')
])
level = env.ref('spp_data_classification.level_confidential')

# Create classification
env['spp.field.classification'].create({
    'model_id': model.id,
    'field_id': field.id,
    'classification_id': level.id,
    'pii_category': 'contact',
    'mask_pattern': '***-***-####',
    'search_strategy': 'partial_index',
})
```

## PII Categories

Classify by data type:

| Category | Examples | Special Handling |
|----------|----------|------------------|
| `direct_id` | National ID, passport, SSN | Exact match index |
| `quasi_id` | DOB, gender, location | Can re-identify when combined |
| `sensitive` | Religion, ethnicity, political views | GDPR Art. 9 special category |
| `financial` | Bank accounts, income | Restricted access |
| `contact` | Phone, email, address | Partial match index |
| `biometric` | Fingerprints, face ID | No search allowed |
| `health` | Disability status, medical info | GDPR Art. 9 special category |
| `location` | GPS coordinates, precise address | Geofencing policies |

## Search Strategies

When fields are encrypted, search needs special handling:

| Strategy | Use Case | How It Works |
|----------|----------|--------------|
| `none` | Biometric data | No search allowed |
| `blind_index` | National IDs | Exact match only via HMAC |
| `partial_index` | Phone numbers | Search by last N digits |
| `phonetic` | Names | Soundex/Metaphone matching |
| `range` | Dates | Store year/month unencrypted |
| `full` | Not encrypted | Normal SQL search |

## Auto-Detection

OpenSPP can scan for likely-PII fields:

### Via Web UI

1. Navigate to **Settings → Data Classification → Auto-Detect PII**
2. Select models to scan
3. Click **Detect**
4. Review suggestions
5. Click **Apply** for fields you want to classify

### Via Shell

```bash
odoo-bin shell -d openspp_prod

# Auto-detect in specific module
detector = env['spp.field.classification.detector'].create({
    'model_ids': [(6, 0, env['ir.model'].search([
        ('model', 'like', 'spp.%')
    ]).ids)],
})
detector.action_detect()

# Review suggestions
for suggestion in detector.suggestion_ids:
    print(f"{suggestion.model_id.model}.{suggestion.field_id.name}")
    print(f"  Suggested: {suggestion.suggested_level_id.code} ({suggestion.pii_category})")
    print(f"  Confidence: {suggestion.confidence}")

# Apply accepted suggestions
detector.action_apply_suggestions()
```

## Detection Patterns

Auto-detection uses regex patterns:

| Pattern | Detects | Suggested Level |
|---------|---------|-----------------|
| `(national\|passport\|ssn).*id` | ID numbers | RESTRICTED |
| `(birth\|dob)` | Birth dates | CONFIDENTIAL |
| `(phone\|mobile\|tel)` | Phone numbers | CONFIDENTIAL |
| `email` | Email addresses | INTERNAL |
| `(account\|iban\|bank)` | Account numbers | RESTRICTED |
| `(family\|given).*name` | Personal names | CONFIDENTIAL |
| `(disability\|health\|medical)` | Health data | RESTRICTED |

Add custom patterns:

```bash
env['spp.classification.pattern'].create({
    'name': 'Custom ID Pattern',
    'pattern': 'custom.*identifier',
    'classification_id': env.ref('spp_data_classification.level_restricted').id,
    'pii_category': 'direct_id',
    'priority': 100,
})
```

## Field-Level Access Control

Classifications can restrict field access by group:

```bash
# Require Registry Manager to view unmasked national IDs
classification = env['spp.field.classification'].search([
    ('model_id.model', '=', 'spp.registry.id'),
    ('field_id.name', '=', 'value'),
])
classification.classification_id.min_group_id = env.ref('spp_registry_base.group_registry_manager')
```

Users below minimum group see masked values.

## Classification Reports

### Coverage Report

```bash
odoo-bin shell -d openspp_prod

# Get classification coverage
total_fields = env['ir.model.fields'].search_count([
    ('model', 'like', 'spp.%'),
    ('store', '=', True),
])
classified = env['spp.field.classification'].search_count([
    ('model_id.model', 'like', 'spp.%')
])
print(f"Coverage: {classified}/{total_fields} ({100*classified/total_fields:.1f}%)")
```

### By Level

```bash
# Count by classification level
for level in env['spp.data.classification.level'].search([]):
    count = env['spp.field.classification'].search_count([
        ('classification_id', '=', level.id)
    ])
    print(f"{level.name}: {count} fields")
```

### Export for Compliance

```bash
# Generate PII inventory CSV
classifications = env['spp.field.classification'].search([])
import csv
with open('/tmp/pii_inventory.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Model', 'Field', 'Level', 'Category', 'Legal Basis'])
    for c in classifications:
        writer.writerow([
            c.model_id.model,
            c.field_id.name,
            c.classification_id.code,
            c.pii_category,
            c.legal_basis,
        ])
```

## Data Subject Access Requests (DSAR)

Classifications enable GDPR Article 15 data exports:

```bash
# Create DSAR export for beneficiary
partner = env['res.partner'].search([('ref', '=', 'BEN-12345')])
dsar = env['spp.dsar.request'].create({
    'partner_id': partner.id,
    'request_type': 'access',
})
dsar.action_generate_export()

# Download export file
print(f"Export ready: {dsar.export_filename}")
```

## Troubleshooting

**Field not showing in classification list**

```bash
# Check field exists and is stored
field = env['ir.model.fields'].search([
    ('model', '=', 'res.partner'),
    ('name', '=', 'custom_field'),
])
print(f"Field exists: {bool(field)}")
print(f"Stored: {field.store}")  # Must be True
```

**Auto-detect not finding PII fields**

Add custom detection pattern or manually classify.

**Field masking not working**

Check:
1. Classification has `requires_masking = True`
2. User's group is below `min_group_id`
3. Field widget set to `masked_pii` in view

**Search not working on encrypted field**

Check `search_strategy` setting. If set to `none`, search is disabled by design.

## Best Practices

1. **Classify before encrypting**: Classification determines what gets encrypted
2. **Start conservative**: Mark as RESTRICTED if unsure
3. **Document legal basis**: Required for GDPR compliance
4. **Run auto-detect regularly**: New modules may add PII fields
5. **Test DSAR exports**: Ensure all personal data is included
6. **Review quarterly**: Data types change over time

## Security Checklist

- [ ] All PII fields classified
- [ ] Auto-detection run on all modules
- [ ] RESTRICTED fields have search strategy configured
- [ ] Legal basis documented for each classification
- [ ] Field-level access groups assigned
- [ ] DSAR export tested
- [ ] Classification coverage > 90%
- [ ] No unclassified fields matching PII patterns

## Related Documentation

- Field encryption: {doc}`pii_encryption`
- Access control: {doc}`access_control`
- Audit logging: {doc}`audit`

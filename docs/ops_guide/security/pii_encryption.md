---
openspp:
  doc_status: draft
---

# PII Encryption

This guide is for **sys admins** configuring field-level encryption for OpenSPP.

OpenSPP encrypts sensitive PII fields using AES-256-GCM. Encryption is transparent to users but protects data at rest and from SQL injection.

## Architecture

```
┌────────────────────────────────────────────────────────────┐
│ User Interface                                             │
│   - Sees decrypted values (if authorized)                  │
│   - Masked display for unauthorized users                  │
└────────────────────────────────────────────────────────────┘
                          ▼
┌────────────────────────────────────────────────────────────┐
│ Application Layer (spp_pii_encryption)                     │
│   - Encrypts on write                                      │
│   - Decrypts on read                                       │
│   - Maintains blind indexes for search                     │
└────────────────────────────────────────────────────────────┘
                          ▼
┌────────────────────────────────────────────────────────────┐
│ Database (PostgreSQL)                                      │
│   - Stores base64-encoded ciphertext                       │
│   - Stores blind indexes (HMAC hashes)                     │
│   - TDE for additional protection                          │
└────────────────────────────────────────────────────────────┘
```

## What Gets Encrypted

Based on data classification:

| Classification Level | Encryption | Module |
|---------------------|------------|--------|
| PUBLIC | No | - |
| INTERNAL | No | - |
| CONFIDENTIAL | Optional | `spp_pii_encryption` |
| RESTRICTED | Required | `spp_pii_encryption` |

Currently encrypted fields:

| Model | Field | Why |
|-------|-------|-----|
| `spp.registry.id` | `value` | National IDs, passports |
| `spp.phone.number` | `phone_no` | Contact information |
| `res.partner` | `email` | Email addresses (if `is_registrant`) |
| `res.partner` | `street`, `street2` | Physical addresses (if `is_registrant`) |

## Checking Encryption Status

### Via Web UI

Navigate to **Settings → Data Classification → Field Classifications**

Filter by **Classification = RESTRICTED** to see encrypted fields.

### Via Shell

```bash
odoo-bin shell -d openspp_prod

# Check if encryption enabled
config_provider = env['spp.key.provider'].get_active_provider()
print(f"Key provider: {config_provider._name}")

# List encrypted fields
encrypted_fields = env['spp.field.classification'].search([
    ('classification_id.requires_encryption', '=', True)
])
for field in encrypted_fields:
    print(f"  - {field.model_id.model}.{field.field_id.name}")

# Test encryption on a record
reg_id = env['spp.registry.id'].search([], limit=1)
if reg_id:
    print(f"Encrypted value: {reg_id.value_encrypted[:20]}...")
    print(f"Decrypted value: {reg_id.value}")
    print(f"Blind index: {reg_id.value_blind_index[:20]}...")
```

### Via Database

```sql
-- Check encryption on registry IDs
SELECT
    id,
    LEFT(value_encrypted, 30) as encrypted,
    value_blind_index,
    value_last4
FROM spp_registry_id
LIMIT 5;

-- Count encrypted vs. plaintext
SELECT
    CASE
        WHEN value_encrypted IS NOT NULL THEN 'encrypted'
        ELSE 'plaintext'
    END as status,
    COUNT(*) as count
FROM spp_registry_id
GROUP BY status;
```

## Enabling Encryption

Encryption is automatically enabled when:
1. `spp_pii_encryption` module is installed
2. Key provider is configured
3. Field has classification with `requires_encryption = True`

### Installation

```bash
# Install encryption module
odoo-bin -d openspp_prod -c /etc/odoo/odoo.conf -i spp_pii_encryption --stop-after-init

# Verify installation
odoo-bin shell -d openspp_prod
env['ir.module.module'].search([('name', '=', 'spp_pii_encryption')]).state
# Should return: 'installed'
```

### Configuration Check

```bash
# Check odoo.conf has encryption settings
grep -A 5 "^\[encryption\]" /etc/odoo/odoo.conf

# Should show:
# [encryption]
# key_provider = config
# encryption_key_master = <base64_key>
# encryption_key_pii = <base64_key>
```

## Encryption Algorithms

| Component | Algorithm | Key Size |
|-----------|-----------|----------|
| Field encryption | AES-256-GCM | 256 bits |
| Blind index | HMAC-SHA256 | 256 bits |
| Key wrapping | AES-256-KW | 256 bits |

**Why AES-256-GCM:**
- Authenticated encryption (prevents tampering)
- Random nonce per record (prevents pattern analysis)
- Fast (hardware-accelerated on modern CPUs)
- FIPS 140-2 compliant

## Blind Indexes for Search

Encrypted fields can't be searched directly. Blind indexes enable lookups.

### How Blind Indexes Work

```
Plaintext: "ABC-123-456"
    ↓ Normalize (remove formatting)
"ABC123456"
    ↓ HMAC-SHA256 with salt
"8f3e9a2b..."  ← stored in value_blind_index column
```

Search computes same HMAC and compares:

```bash
# Search by ID value
id_value = "ABC-123-456"
records = env['spp.registry.id'].search_by_id_value(id_value)
```

### Index Types

| Type | Use Case | What's Indexed |
|------|----------|----------------|
| Exact | National IDs, account numbers | Normalized full value |
| Partial | Phone numbers | Last 4 digits (plaintext) |
| Phonetic | Names | Soundex/Metaphone hash |
| Range | Dates | Year and month (plaintext) |

Example: Phone number with partial index

```sql
SELECT
    phone_no_encrypted,      -- Full encrypted number
    phone_no_blind_index,   -- HMAC of full number
    phone_no_last4          -- Last 4 digits (plaintext)
FROM spp_phone_number;

-- Search by full number: uses blind_index
-- Search by last 4: uses phone_no_last4
```

## Encrypting Existing Data

When you first enable encryption, existing data is plaintext.

### Migration Script

```bash
# Run migration for registry IDs
odoo-bin shell -d openspp_prod

# Create migration wizard
wizard = env['spp.pii.encryption.migration'].create({
    'model_id': env.ref('spp_registry_base.model_spp_registry_id').id,
    'field_name': 'value',
    'batch_size': 1000,
})

# Start migration (runs in background)
wizard.action_migrate()

# Check progress
wizard.refresh()
print(f"State: {wizard.state}")
print(f"Progress: {wizard.progress}%")
```

### Manual Migration

```bash
odoo-bin shell -d openspp_prod

# Encrypt in batches
model = env['spp.registry.id']
batch_size = 1000
offset = 0

while True:
    records = model.search([], limit=batch_size, offset=offset)
    if not records:
        break

    for record in records:
        # Write triggers encryption
        if record.value and not record.value_encrypted:
            record.value = record.value  # Re-save to encrypt

    env.cr.commit()  # Commit each batch
    offset += batch_size
    print(f"Encrypted {offset} records")
```

## Testing Encryption

### Verify Encryption Works

```bash
odoo-bin shell -d openspp_prod

# Create test record
test_id = env['spp.registry.id'].create({
    'partner_id': env['res.partner'].search([], limit=1).id,
    'id_type_id': env['spp.id.type'].search([], limit=1).id,
    'value': 'TEST-123-456',
})

# Check encryption
print(f"Plaintext access: {test_id.value}")  # Should be: TEST-123-456
print(f"Encrypted storage: {test_id.value_encrypted[:30]}...")  # Should be base64
print(f"Blind index: {test_id.value_blind_index}")  # Should be hex hash

# Test search
found = env['spp.registry.id'].search_by_id_value('TEST-123-456')
print(f"Search found: {found.id == test_id.id}")  # Should be True

# Clean up
test_id.unlink()
```

### Verify Search Works

```bash
# Test exact match
results = env['spp.registry.id'].search_by_id_value('ABC-123-456')
print(f"Found {len(results)} records")

# Test partial match (phone numbers)
results = env['spp.phone.number'].search([('phone_no_last4', '=', '5678')])
print(f"Found {len(results)} phone numbers ending in 5678")
```

### Verify Masking Works

```bash
# Test as different users
admin = env.ref('base.user_admin')
viewer = env['res.users'].search([
    ('groups_id', 'in', env.ref('spp_registry_base.group_registry_viewer').id)
], limit=1)

reg_id = env['spp.registry.id'].search([], limit=1)

# Admin sees full value
print(f"Admin sees: {reg_id.with_user(admin).value}")

# Viewer sees masked
print(f"Viewer sees: {reg_id.with_user(viewer).value}")  # Should be ****-***-456
```

## Performance Impact

Encryption adds latency:

| Operation | Overhead | Mitigation |
|-----------|----------|------------|
| Read single record | ~1-5ms | Acceptable |
| Read 100 records | ~50-100ms | Use `read()` not looping |
| Search by encrypted field | ~10-20ms | Blind index is fast |
| Write record | ~5-10ms | Batch writes |

### Optimization Tips

```python
# BAD: Loops decrypt each record individually
for record in records:
    print(record.national_id)  # N decryption calls

# GOOD: Batch decrypt
values = records.mapped('national_id')  # 1 decryption call

# BAD: Search on encrypted field directly
records = env['spp.registry.id'].search([
    ('value', '=', 'ABC-123')  # Won't work!
])

# GOOD: Use search method with blind index
records = env['spp.registry.id'].search_by_id_value('ABC-123')
```

## Database TDE (Additional Layer)

Application encryption protects from SQL injection and backup exposure. Add database TDE for physical disk protection.

### PostgreSQL 16+ Native TDE

```bash
# Enable TDE when creating cluster
initdb --data-encryption-key-file=/secure/path/db.key /var/lib/postgresql/data

# Verify TDE enabled
sudo -u postgres psql openspp_prod -c "SHOW data_encryption_key;"
```

### AWS RDS Encryption

```bash
# Enable via AWS Console or CLI
aws rds modify-db-instance \
    --db-instance-identifier openspp-prod \
    --storage-encrypted \
    --kms-key-id arn:aws:kms:region:account:key/key-id \
    --apply-immediately
```

### Azure PostgreSQL Encryption

Encryption at rest is automatic. Configure customer-managed keys:

```bash
az postgres server key create \
    --server-name openspp-prod \
    --resource-group openspp-rg \
    --kid https://vault.azure.net/keys/openspp-key/version
```

## Backup Considerations

Encrypted fields remain encrypted in backups:

```bash
# Standard pg_dump
pg_dump openspp_prod > backup.sql

# Encrypted fields in backup are still encrypted:
grep "value_encrypted" backup.sql
# Shows: base64-encoded ciphertext

# To restore, you need:
# 1. Backup file
# 2. Encryption keys (from key provider)
```

**Critical:** Back up encryption keys separately from database backups.

## Troubleshooting

**Decryption fails after restore**

Check key provider has correct keys:

```bash
odoo-bin shell -d openspp_prod

provider = env['spp.key.provider'].get_active_provider()
key = provider.get_data_key('pii')
print(f"Key available: {bool(key)}")
```

**Search not finding encrypted records**

Verify blind index exists:

```bash
# Check if index columns exist
env.cr.execute("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'spp_registry_id'
    AND column_name LIKE '%index%'
""")
print(env.cr.fetchall())
```

**Performance degradation**

Check query plans:

```sql
EXPLAIN ANALYZE
SELECT * FROM spp_registry_id
WHERE value_blind_index = 'abc123...';

-- Should use index scan, not seq scan
```

**Encryption key lost**

If master key is lost, **encrypted data is unrecoverable**. This is by design.

Recovery options:
1. Restore from key backup
2. Use key escrow (if configured)
3. Contact key management service support

Prevention:
- Back up keys to separate secure location
- Use key escrow for enterprise deployments
- Document key recovery procedures

## Security Checklist

- [ ] Encryption module installed
- [ ] Key provider configured
- [ ] Encryption keys backed up separately
- [ ] RESTRICTED fields all encrypted
- [ ] Blind indexes created for searchable fields
- [ ] Search functions tested
- [ ] Masking tested for different user roles
- [ ] Database TDE enabled
- [ ] Backup encryption verified
- [ ] Key rotation procedure documented

## Related Documentation

- Key management: {doc}`key_management`
- Data classification: {doc}`data_classification`
- Access control: {doc}`access_control`

---
openspp:
  doc_status: draft
---

# Key Management

This guide is for **sys admins** managing encryption keys for OpenSPP.

Encryption keys protect your data. Lose the keys, lose the data. This guide covers key generation, storage, rotation, and recovery.

## Key Types

OpenSPP uses multiple keys:

| Key | Purpose | Rotation |
|-----|---------|----------|
| Master Key | Encrypts other keys (envelope encryption) | Annually |
| PII Key | Encrypts personal data fields | Annually |
| Index Salt | HMAC for blind indexes | Never (breaks search) |

## Key Providers

OpenSPP supports 6 key providers:

| Provider | Use Case | Security | Complexity |
|----------|----------|----------|------------|
| Config | Development/testing | Low | Minimal |
| Database | Small production | Medium | Low |
| Vault | Enterprise | High | Medium |
| AWS KMS | AWS deployments | High | Medium |
| GCP KMS | GCP deployments | High | Medium |
| Azure KV | Azure deployments | High | Medium |

### Selecting a Provider

Set in `odoo.conf`:

```ini
[encryption]
key_provider = config  # or: database, vault, aws_kms, gcp_kms, azure_kv
```

## Config Provider (Development)

**Use for:** Development, testing, proof-of-concept

**Do not use for:** Production with real data

### Configuration

```ini
# /etc/odoo/odoo.conf
[encryption]
key_provider = config

# Generate keys with: python3 -c "import secrets; print(secrets.token_urlsafe(32))"
encryption_key_master = <base64_encoded_32_byte_key>
encryption_key_pii = <base64_encoded_32_byte_key>
index_salt_default = <base64_encoded_32_byte_salt>
```

### Generating Keys

```bash
# Generate master key
python3 -c "import secrets; print('encryption_key_master =', secrets.token_urlsafe(32))"

# Generate PII key
python3 -c "import secrets; print('encryption_key_pii =', secrets.token_urlsafe(32))"

# Generate index salt
python3 -c "import secrets; print('index_salt_default =', secrets.token_urlsafe(32))"

# Add to odoo.conf
sudo nano /etc/odoo/odoo.conf
```

### Backing Up Config Keys

```bash
# Extract keys from config
grep "encryption_key\|index_salt" /etc/odoo/odoo.conf > /secure/backup/keys_$(date +%Y%m%d).conf

# Encrypt backup
gpg --symmetric --cipher-algo AES256 /secure/backup/keys_*.conf

# Store encrypted backup securely (off-site)
```

## Database Provider (Standard Production)

**Use for:** Small to medium production deployments

**How it works:** Keys stored in database, encrypted with master key from config

### Configuration

```ini
# /etc/odoo/odoo.conf
[encryption]
key_provider = database
encryption_key_master = <base64_key_from_config>
```

### Initial Setup

```bash
odoo-bin shell -d openspp_prod

# Create PII data key
master = env['spp.key.provider.database']._get_master_key()
pii_key = env['spp.encryption.key'].generate_key(
    key_id='pii',
    purpose='Encrypt PII fields',
    algorithm='AES-256-GCM',
)

# Create index salt
index_salt = env['spp.encryption.key'].generate_key(
    key_id='index_salt_default',
    purpose='Blind index salt',
    algorithm='HMAC-SHA256',
)

# Verify keys created
keys = env['spp.encryption.key'].search([])
for key in keys:
    print(f"{key.key_id} v{key.version}: {key.purpose}")
```

### Checking Keys

```bash
odoo-bin shell -d openspp_prod

# List all keys
keys = env['spp.encryption.key'].search([])
for key in keys:
    status = "CURRENT" if key.is_current else "archived"
    print(f"{key.key_id} v{key.version} [{status}]: {key.purpose}")
    print(f"  Created: {key.created_date}")
    print(f"  Expires: {key.expires_date or 'never'}")
```

Via database:

```sql
SELECT
    key_id,
    version,
    is_current,
    algorithm,
    purpose,
    created_date,
    expires_date
FROM spp_encryption_key
ORDER BY key_id, version DESC;
```

## Vault Provider (Enterprise)

**Use for:** Enterprise deployments requiring HSM, audit trails, centralized key management

**Requires:** HashiCorp Vault with Transit secrets engine

### Vault Setup

```bash
# Enable Transit secrets engine
vault secrets enable transit

# Create encryption key
vault write -f transit/keys/openspp-pii \
    type=aes256-gcm96

# Create policy
vault policy write openspp-encryption - <<EOF
path "transit/encrypt/openspp-pii" {
  capabilities = ["update"]
}
path "transit/decrypt/openspp-pii" {
  capabilities = ["update"]
}
path "transit/datakey/plaintext/openspp-pii" {
  capabilities = ["update"]
}
EOF

# Create AppRole for OpenSPP
vault auth enable approle
vault write auth/approle/role/openspp \
    secret_id_ttl=0 \
    token_ttl=1h \
    token_max_ttl=4h \
    policies="openspp-encryption"

# Get credentials
vault read auth/approle/role/openspp/role-id
vault write -f auth/approle/role/openspp/secret-id
```

### OpenSPP Configuration

```ini
# /etc/odoo/odoo.conf
[encryption]
key_provider = vault
vault_url = https://vault.example.com:8200
vault_auth_method = approle
vault_role_id = <role_id_from_vault>
vault_secret_id = <secret_id_from_vault>
vault_transit_mount = transit
```

### Kubernetes Integration

For Kubernetes deployments:

```ini
[encryption]
key_provider = vault
vault_url = http://vault.vault.svc.cluster.local:8200
vault_auth_method = kubernetes
vault_k8s_role = openspp-prod
vault_transit_mount = transit
```

Kubernetes service account token is auto-discovered.

### Testing Vault Connection

```bash
odoo-bin shell -d openspp_prod

provider = env['spp.key.provider.vault']
try:
    key = provider.get_data_key('openspp-pii')
    print(f"Vault connection OK, got key: {len(key)} bytes")
except Exception as e:
    print(f"Vault connection failed: {e}")
```

## AWS KMS Provider

**Use for:** AWS deployments (EC2, RDS, EKS)

**Requires:** AWS KMS key, IAM permissions

### AWS Setup

```bash
# Create KMS key
aws kms create-key \
    --description "OpenSPP PII encryption" \
    --key-usage ENCRYPT_DECRYPT \
    --origin AWS_KMS

# Get key ARN
aws kms describe-key --key-id <key-id> --query 'KeyMetadata.Arn'

# Create alias
aws kms create-alias \
    --alias-name alias/openspp-pii \
    --target-key-id <key-id>

# Grant permissions to EC2 instance role
aws kms create-grant \
    --key-id <key-id> \
    --grantee-principal arn:aws:iam::account:role/openspp-instance-role \
    --operations Encrypt Decrypt GenerateDataKey
```

### OpenSPP Configuration

```ini
# /etc/odoo/odoo.conf
[encryption]
key_provider = aws_kms
aws_region = us-east-1
aws_kms_key_pii = arn:aws:kms:us-east-1:account:key/key-id

# If not using instance role, provide credentials:
aws_access_key_id = <access_key>
aws_secret_access_key = <secret_key>
```

### Testing AWS KMS

```bash
odoo-bin shell -d openspp_prod

provider = env['spp.key.provider.aws_kms']
try:
    key = provider.get_data_key('pii')
    print(f"AWS KMS OK, got {len(key)} byte key")
except Exception as e:
    print(f"AWS KMS failed: {e}")
```

## GCP KMS Provider

**Use for:** GCP deployments (GCE, CloudSQL, GKE)

### GCP Setup

```bash
# Create key ring
gcloud kms keyrings create openspp \
    --location global

# Create key
gcloud kms keys create pii-encryption \
    --keyring openspp \
    --location global \
    --purpose encryption

# Grant permissions
gcloud kms keys add-iam-policy-binding pii-encryption \
    --keyring openspp \
    --location global \
    --member serviceAccount:openspp@project.iam.gserviceaccount.com \
    --role roles/cloudkms.cryptoKeyEncrypterDecrypter
```

### OpenSPP Configuration

```ini
[encryption]
key_provider = gcp_kms
gcp_project_id = your-project-id
gcp_kms_location = global
gcp_kms_keyring = openspp
gcp_kms_key_pii = pii-encryption

# If not using service account:
gcp_credentials_file = /etc/odoo/gcp-credentials.json
```

## Azure Key Vault Provider

**Use for:** Azure deployments (VMs, Azure Database)

### Azure Setup

```bash
# Create Key Vault
az keyvault create \
    --name openspp-vault \
    --resource-group openspp-rg \
    --location eastus

# Create key
az keyvault key create \
    --vault-name openspp-vault \
    --name pii-encryption \
    --protection software \
    --ops encrypt decrypt

# Grant access to managed identity
az keyvault set-policy \
    --name openspp-vault \
    --object-id <managed-identity-id> \
    --key-permissions get unwrapKey wrapKey
```

### OpenSPP Configuration

```ini
[encryption]
key_provider = azure_kv
azure_vault_url = https://openspp-vault.vault.azure.net/
azure_key_name_pii = pii-encryption

# If not using managed identity:
azure_tenant_id = <tenant-id>
azure_client_id = <client-id>
azure_client_secret = <client-secret>
```

## Key Rotation

Rotate keys annually or after suspected compromise.

### Rotation Process

1. **Create new key version**
2. **Encrypt new data with new key**
3. **Re-encrypt existing data** (background job)
4. **Archive old key version**

### Database Provider Rotation

```bash
odoo-bin shell -d openspp_prod

# Create new key version
new_version = env['spp.encryption.key'].rotate_key('pii')
print(f"Created key version {new_version}")

# Mark old version as archived
old_keys = env['spp.encryption.key'].search([
    ('key_id', '=', 'pii'),
    ('is_current', '=', False),
])
print(f"Archived {len(old_keys)} old versions")

# Re-encrypt data (background job)
wizard = env['spp.key.rotation.wizard'].create({
    'key_id': 'pii',
    'old_version': 1,
    'new_version': new_version,
})
wizard.action_rotate()
```

### Vault Provider Rotation

```bash
# Rotate in Vault
vault write -f transit/keys/openspp-pii/rotate

# Update OpenSPP to use new version (automatic)
# Old ciphertext can still be decrypted with old version
```

### AWS KMS Rotation

```bash
# Enable automatic rotation
aws kms enable-key-rotation --key-id <key-id>

# Check rotation status
aws kms get-key-rotation-status --key-id <key-id>
```

## Key Backup and Recovery

### Config Provider Backup

```bash
# Backup config file
sudo cp /etc/odoo/odoo.conf /secure/backup/odoo.conf.$(date +%Y%m%d)

# Encrypt backup
gpg --symmetric --cipher-algo AES256 /secure/backup/odoo.conf.*

# Store off-site
rsync -av /secure/backup/*.gpg backup-server:/openspp-backups/
```

### Database Provider Backup

```bash
# Export keys (encrypted with master key)
odoo-bin shell -d openspp_prod

keys = env['spp.encryption.key'].search([])
import json
key_export = []
for key in keys:
    key_export.append({
        'key_id': key.key_id,
        'version': key.version,
        'encrypted_key': key.encrypted_key.decode('latin-1'),
        'algorithm': key.algorithm,
        'purpose': key.purpose,
    })

with open('/tmp/keys_backup.json', 'w') as f:
    json.dump(key_export, f, indent=2)

# Encrypt export
gpg --symmetric --cipher-algo AES256 /tmp/keys_backup.json
rm /tmp/keys_backup.json

# Store master key separately (from odoo.conf)
```

### Vault Provider Backup

Vault handles backups. Ensure Vault itself is backed up:

```bash
# Backup Vault data
vault operator raft snapshot save backup.snap

# Store snapshot securely
gpg --symmetric --cipher-algo AES256 backup.snap
```

### Cloud KMS Backup

AWS/GCP/Azure KMS keys are automatically backed up by the cloud provider. Document key ARNs/IDs:

```bash
# AWS
aws kms describe-key --key-id <key-id> > /secure/backup/aws_kms_info.json

# GCP
gcloud kms keys describe pii-encryption \
    --keyring openspp \
    --location global > /secure/backup/gcp_kms_info.txt
```

## Key Recovery

### Lost Master Key (Config/Database Provider)

If master key is lost, **encrypted data is unrecoverable**.

Recovery options:
1. Restore from key backup
2. Restore database from backup before key loss

### Lost Cloud KMS Access

If you lose access to cloud KMS:

1. Restore IAM permissions
2. Restore KMS key from cloud provider backup
3. Contact cloud provider support

### Testing Key Recovery

```bash
# 1. Backup current keys
# 2. Remove keys from system
# 3. Restore from backup
# 4. Verify decryption works

odoo-bin shell -d openspp_prod

# Test decryption
reg_id = env['spp.registry.id'].search([], limit=1)
try:
    value = reg_id.value  # Should decrypt successfully
    print("Key recovery successful")
except Exception as e:
    print(f"Key recovery failed: {e}")
```

## Key Escrow

For regulated environments, set up key escrow:

### Manual Escrow

1. Export keys to encrypted file
2. Split into key shares (Shamir's Secret Sharing)
3. Distribute shares to trusted parties
4. Document recovery procedure

### Vault Auto-Unseal

Use cloud KMS to auto-unseal Vault:

```bash
# Configure Vault with AWS KMS auto-unseal
vault operator init \
    -recovery-shares=5 \
    -recovery-threshold=3

# Recovery keys stored in AWS KMS
# Vault unseals automatically on restart
```

## Security Checklist

- [ ] Keys generated with cryptographically secure RNG
- [ ] Master key stored separately from database backups
- [ ] Key backups encrypted and stored off-site
- [ ] Key rotation schedule documented
- [ ] Key recovery procedure tested
- [ ] Access to keys restricted (file permissions, IAM)
- [ ] Key access audited
- [ ] Index salts never rotated (breaks search)
- [ ] Old key versions retained for decryption
- [ ] Key escrow configured (if required)

## Troubleshooting

**Key not found error**

```bash
# Check key exists
odoo-bin shell -d openspp_prod
env['spp.encryption.key'].search([('key_id', '=', 'pii')])

# Check config has key
grep "encryption_key_pii" /etc/odoo/odoo.conf
```

**Vault connection failed**

```bash
# Test Vault access
vault login -method=approle \
    role_id=$VAULT_ROLE_ID \
    secret_id=$VAULT_SECRET_ID

# Test key access
vault write transit/datakey/plaintext/openspp-pii bits=256
```

**AWS KMS access denied**

```bash
# Check IAM permissions
aws kms describe-key --key-id <key-id>

# Check instance role
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

**Re-encryption job stuck**

```bash
# Check job status
odoo-bin shell -d openspp_prod
jobs = env['queue.job'].search([('name', 'like', 'rotate_key')])
for job in jobs:
    print(f"{job.state}: {job.exc_info}")
```

## Related Documentation

- PII encryption: {doc}`pii_encryption`
- Data classification: {doc}`data_classification`
- Audit logging: {doc}`audit`

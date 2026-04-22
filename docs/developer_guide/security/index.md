---
openspp:
  doc_status: draft
  products: [core]
---

# Security and Encryption

**For: developers**

Services OpenSPP provides for securing data at rest, managing cryptographic keys, recording consent, and scanning uploads — plus the security checks that run in CI.

## How to use this section

1. Read **What's in scope** first — several security topics live in other pages
2. Read the feature section(s) you need: encryption, key management, consent, antivirus scanning, or CI security
3. See **Common mistakes** before shipping

## Prerequisites

- Familiarity with Odoo models and services (`self.env["..."]`)
- For key management: basic understanding of symmetric vs asymmetric cryptography
- For consent: awareness of GDPR Article 6 lawful bases (the model uses these labels directly)

## What's in scope (and what isn't)

This page covers:

- **PII encryption** — encrypting sensitive field values with `spp_encryption` and `spp_key_management`
- **Key management** — the pluggable key provider system (local config, database, Vault, AWS/GCP/Azure KMS)
- **Consent** — the `spp.consent` data model (ISO 27560 / DPV-aligned)
- **Antivirus scanning** — `spp_attachment_av_scan` auto-scanning of uploads
- **Security checks in CI** — the pre-commit hooks that block insecure code

It does **not** cover:

- Security groups, privileges, and ACL patterns — see {doc}`/developer_guide/custom_modules/security`
- API-level consent filtering and scope enforcement — see {doc}`/developer_guide/api_v2/consent`
- Audit logging — see the Audit section in the developer guide
- User roles (area-based access via `spp_user_roles`) — brief note below, but not the focus

## The security modules

| Module | Purpose |
|--------|---------|
| `spp_security` | Foundation — security categories, the `spp_admin` group, shared privilege definitions referenced by every other module |
| `spp_encryption` | Cryptographic provider (`spp.encryption.provider`) — JWCrypto-based encryption, JWT signing, JSON-LD credential signing, JWKS output |
| `spp_key_management` | Key lifecycle (`spp.key.manager`) — pluggable providers (config / database / Vault / AWS KMS / GCP KMS / Azure KeyVault), rotation, blind-index salts |
| `spp_consent` | `spp.consent` model — ISO 27560 / DPV-aligned consent records, GDPR Article 6 legal bases, lifecycle (requested → given / refused / withdrawn / expired) |
| `spp_attachment_av_scan` | ClamAV scanner for `ir.attachment` — auto-queued on upload, infected files encrypted and quarantined |
| `spp_user_roles` | Area-based roles — extends `base_user_role` with `role_type` of `local` or `global`; local roles restrict access by geographic area via `spp_area` |
| `spp_oauth` | Odoo-wide OAuth 2.0 configuration (private/public keys in `res.config.settings`); the **API V2** bearer/signature auth (see {doc}`/developer_guide/api_v2/authentication`) is separate |

## PII encryption

`spp_encryption` + `spp_key_management` together provide application-layer encryption for sensitive fields. Encryption is **not transparent at the ORM level** — your code calls `encrypt()` and `decrypt()` explicitly. This is deliberate: it keeps the cryptographic boundary visible in code review and avoids the "I thought this column was encrypted" class of bugs.

### Encrypting a value

```python
key_mgr = self.env["spp.key.manager"]

# Encrypt — returns a base64 string ready to store in a Char/Text column
national_id_plain = "1234567890"
national_id_cipher = key_mgr.encrypt(
    plaintext=national_id_plain,
    purpose="pii",           # Which logical key to use (mapped to a provider)
    key_id="national_id",    # Which concrete key within that purpose
    aad=None,                # Optional additional authenticated data
)

# Store national_id_cipher in your field

# Decrypt later
recovered = key_mgr.decrypt(
    ciphertext_b64=national_id_cipher,
    purpose="pii",
    key_id="national_id",
    aad=None,
)
```

Encryption uses **AES-256-GCM** under the hood. The `purpose` argument routes the operation to a key provider (see [Key management](#key-management) below) — so the same code works whether the key lives in `odoo.conf`, a database column, HashiCorp Vault, or a cloud KMS.

### Searching encrypted fields

Standard SQL `WHERE ciphertext = '...'` doesn't work against GCM-encrypted data — each encryption produces a different ciphertext because of the nonce. Use **blind indexes** to support equality and prefix search:

```python
# Compute a deterministic hash for indexing
blind_index = key_mgr.compute_blind_index(
    value="john@example.com",
    purpose="pii",
    salt_id="email",
    index_type="exact",    # or "partial" (last-4), "phonetic"
)

# Store the blind index in a separate Char column (call it email_blind_index)
# Search by that column, not by the encrypted value
matches = self.env["res.partner"].search([("email_blind_index", "=", blind_index)])
```

Three index types are supported (`spp_key_management/models/key_manager.py`):

| Index type | Method | Use case |
|------------|--------|----------|
| `exact` | Full HMAC-SHA256 of the value | Exact match (email, national ID) |
| `partial` | HMAC of the last N characters | Prefix/suffix search |
| `phonetic` | Soundex + HMAC | Fuzzy name search |

Blind indexes use per-purpose salts — call `key_mgr.get_salt(purpose, salt_id)` to retrieve the salt if you need to verify an index manually.

### Data classification

The ops-side convention divides data into four levels: **PUBLIC**, **INTERNAL**, **CONFIDENTIAL**, **RESTRICTED**. Only `RESTRICTED` requires encryption; `CONFIDENTIAL` is optional. These levels are documented in the ops guide — there is no classification model in code. As a developer, decide per-field whether to encrypt, and be consistent across modules that handle the same data type.

## Key management

`spp_key_management` centralizes cryptographic key handling and provides a pluggable backend system.

### The key manager service

`spp.key.manager` is the service developers use. Its public methods:

| Method | Purpose |
|--------|---------|
| `get_key(purpose, key_id, version=None)` | Retrieve a data-encryption key as bytes |
| `get_salt(purpose, salt_id)` | Retrieve a salt for blind indexing |
| `rotate_key(purpose, key_id)` | Rotate to a new version; returns new version number |
| `encrypt(plaintext, purpose, key_id, aad=None)` | AES-256-GCM encrypt; returns base64 |
| `decrypt(ciphertext_b64, purpose, key_id, aad=None)` | AES-256-GCM decrypt |
| `compute_blind_index(value, purpose, salt_id, index_type="exact")` | HMAC-based searchable hash; returns `None` when `value` is empty |

All methods check access via `_check_key_access()` — non-admin users get `AccessError`. The service uses `@ormcache` for hot keys so repeated calls don't thrash the provider.

### Key providers (pluggable backends)

The module ships six provider implementations via `spp.key.provider.registry`:

| Provider | Storage | Use case |
|----------|---------|----------|
| `config` | `odoo.conf` parameters | Local development only |
| `database` | Envelope-encrypted key rows | Small production deployments |
| `vault` | HashiCorp Vault | Enterprise on-prem |
| `aws_kms` | AWS KMS | AWS deployments |
| `gcp_kms` | Google Cloud KMS | GCP deployments |
| `azure_keyvault` | Azure Key Vault | Azure deployments |

The registry routes each `purpose` to a provider (e.g., `pii` → `aws_kms`, while `blind_index_salt` → `config` for deterministic salts). Administrators configure this mapping; developers don't need to know which provider their code hits at runtime.

### Registering a custom provider

To integrate a provider the module doesn't ship (e.g., an HSM-on-premises box), you need **three pieces** — the abstract model implementation, a Selection extension on the registry, and a patch to the registry's model lookup.

**1. Implement the abstract model** (`get_data_key` and `get_index_salt` are required; `rotate_key` is optional):

```python
from odoo import models


class MyHSMProvider(models.AbstractModel):
    _name = "spp.key.provider.myhsm"
    _inherit = "spp.key.provider"
    _description = "My on-prem HSM provider"

    def get_data_key(self, key_id, version=None):
        """Return the data-encryption key for the given key_id as bytes (32 bytes for AES-256)."""
        return fetch_key_from_hsm(key_id, version)

    def get_index_salt(self, purpose):
        """Return the blind-index salt for the given purpose (32 bytes)."""
        return fetch_salt_from_hsm(purpose)

    def rotate_key(self, key_id):
        """Optional. Rotate the key and return the new version number."""
        return rotate_key_on_hsm(key_id)
```

**2. Extend the registry's `provider_type` Selection** so administrators can choose your provider:

```python
class KeyProviderRegistry(models.Model):
    _inherit = "spp.key.provider.registry"

    provider_type = fields.Selection(
        selection_add=[("myhsm", "My HSM")],
        ondelete={"myhsm": "cascade"},
    )

    def _get_provider_model(self, provider_type):
        """Map the new provider_type to its abstract model name."""
        if provider_type == "myhsm":
            return "spp.key.provider.myhsm"
        return super()._get_provider_model(provider_type)
```

**3. Create a registry record** (XML data) mapping one or more purposes to your provider. Administrators can do this in the UI, but a shipped record looks like:

```xml
<record id="key_provider_myhsm_pii" model="spp.key.provider.registry">
    <field name="purpose">pii</field>
    <field name="provider_type">myhsm</field>
</record>
```

The `spp.key.manager` routes each `purpose` through its registry entry, so the same `encrypt()` / `decrypt()` calls in application code work unchanged.

### Asymmetric keys

For JWT signing, JSON-LD credential signing, and JWKS publishing, use `spp.asymmetric.key` via `spp.encryption.provider`. The provider supports RSA (2048/3072/4096), EC (P-256/P-384/P-521/secp256k1), and Ed25519. Generate keys with `provider.generate_key(key_type="rsa", key_size=2048)`; sign JWTs with `provider.jwt_sign(payload)`; publish public keys via `provider.get_jwks()`.

## Consent

`spp_consent` is the underlying consent data model. It's aligned with ISO/IEC TS 27560:2023 and the W3C Data Privacy Vocabulary (DPV). The `spp.consent` record captures who, what, why, when, and for how long.

### Core fields

| Field | Purpose |
|-------|---------|
| `signatory_id` | The data subject (a `res.partner`) |
| `group_id` | Optional — if consent covers a household |
| `controller_id` | The organization responsible for processing |
| `recipient_mode` | `specific` (named recipients) or `category` (by organization type) |
| `recipient_ids` / `allowed_recipient_types` | Who may receive the data |
| `purpose_ids` | What the data will be used for |
| `personal_data_ids` | Which categories of data are covered |
| `processing_ids` | What operations are permitted (read, export, match, etc.) |
| `legal_basis` | One of `consent`, `contract`, `legal_obligation`, `vital_interest`, `public_interest`, `legitimate_interest` |
| `status` | `requested`, `given`, `refused`, `renewed`, `withdrawn`, `expired`, `invalidated` |
| `effective_date`, `expiry` | Validity window |
| `delegation_type` | `self`, `guardian`, `parent`, `poa`, `representative` — when consent is given on someone's behalf |

### Checking consent from code

Before processing a registrant's data for a new recipient, call `check_consent()`:

```python
Consent = self.env["spp.consent"]

valid_consent = Consent.check_consent(
    registrant_id=partner.id,
    recipient_id=sharing_org.id,       # Specific recipient lookup
    # OR category-based lookup — pass the code string, not an id:
    recipient_org_type="ngo",          # e.g., "ngo", "government", "healthcare"
    controller_id=our_org.id,
    purpose_code="service_delivery",
)

if valid_consent:
    # Returns the matching spp.consent record(s) — proceed
    ...
else:
    # Empty recordset — stop; no valid consent
    raise UserError(_("No valid consent for this operation."))
```

`check_consent()` verifies `status in ('given', 'renewed')`, the effective/expiry date window, and purpose/recipient match (including category-based matching via `allowed_recipient_types`). It returns a recordset — either the matching consent records or empty.

The `spp.consent.mixin` adds a `consent_ids` Many2many and an `open_record_consent_wizard()` action; inherit it on any model that needs to present its consent records to users.

For the API V2 side — how consent filters response payloads and how `require_consent` on an API client interacts with per-registrant consent — see {doc}`/developer_guide/api_v2/consent`.

## Antivirus scanning

`spp_attachment_av_scan` automatically scans `ir.attachment` records with binary content using ClamAV. No developer code is required to opt in — the module patches `ir.attachment.create()` and `write()` to enqueue a scan job on the worker queue whenever binary data arrives.

### What happens on detection

The attachment's `scan_status` becomes `infected`, the `threat_name` is populated, `is_quarantined` goes to `True`, and an encrypted copy of the original file is stored in `quarantine_data` (using `spp.encryption.provider`). The SHA-256 of the original is stored in `quarantine_hash` for chain-of-custody. The original attachment is **not deleted** — it remains accessible to administrators for forensic review, and every download of a quarantined file sets `is_forensic_download=True` on a generated audit attachment.

### Controlling scanning from code

If you create attachments programmatically and know they're safe (e.g., generated reports), set `scan_status='skipped'` at create time to bypass the queue. Otherwise, leave the scanner alone — it is designed to be invisible to application code.

### Backend configuration

Administrators configure the `spp.av.scanner.backend` record (socket path or host/port for ClamAV, max file size, timeout). Only admin UI, no developer action required.

## User roles (brief)

`spp_user_roles` extends Odoo's `base_user_role` with a `role_type` field (`local` or `global`). Local roles pair with `spp_area` to restrict data access by geographic area — a caseworker role scoped to "North Region" sees only registrants in that area, independent of any feature-level groups they have. Groups answer "can this user see the menu?"; roles answer "which records can this user see?"

This is an administrator-facing concept more than a developer one. The relevant developer pattern (writing `ir.rule` records tied to area) is covered in {doc}`/developer_guide/custom_modules/security`.

## Security checks in CI

Every pull request runs a pre-commit pipeline (`.pre-commit-config.yaml`) that includes security scanning. As a developer, your code must pass these checks:

| Tool / check | What it catches |
|--------------|-----------------|
| **Gitleaks** | Hardcoded secrets (API keys, passwords, private keys) in source or history |
| **Bandit** (`-ll`) | High-confidence Python security issues (eval, exec, `shell=True`, weak crypto) |
| **Semgrep** | Pattern-based issues using `.semgrep/` rules |
| No-PII-in-logs check | Blocks logging of `national_id`, `phone`, `email`, `birthdate`, and similar fields |
| Naming convention check | Enforces `is_`/`has_`/`can_` prefixes on booleans and other naming rules |
| ACL check | Validates `ir.model.access.csv` rows reference real models and groups |
| Compliance check | Validates modules against their `security/compliance.yaml` declaration |
| API-auth check | All API V2 endpoints must require authentication (with an explicit allowlist for genuinely public endpoints like `/metadata`) |
| Performance anti-patterns | N+1 queries, `cr.commit()` in loops, unbounded list views |

Running pre-commit locally before pushing catches nearly all these. See `.pre-commit-config.yaml` for the complete rule set.

## Common mistakes

**Assuming encryption is transparent at the ORM level.** It isn't — `spp_key_management.encrypt()` and `decrypt()` are explicit calls. A developer who adds a Char field called `national_id_encrypted` and assigns `partner.national_id_encrypted = "raw value"` has stored plaintext with a misleading column name. If you want encryption, call `encrypt()` before assignment. Consider writing a small mixin if you have many fields with the same pattern.

**Losing track of `purpose` / `key_id` pairs.** Encryption is deterministic per `(purpose, key_id)`: you must decrypt with the same pair you used to encrypt. If your code encrypts with `purpose="pii"`, `key_id="national_id"` but stores only the ciphertext, a later refactor that changes the key_id orphans the data. Either record the `purpose` and `key_id` alongside each encrypted value (for encrypt-once, decrypt-later workflows) or document the invariant explicitly.

**Using blind-index type `exact` when the data is high-cardinality and long.** Every search becomes a deterministic hash lookup — fine for exact equality, bad for fuzzy/substring search. If users will search by prefix, use `partial`. If by fuzzy name, use `phonetic`. Plan the access pattern before choosing the index type.

**Checking consent once at login and caching the result.** Consent can be withdrawn at any time. Always call `check_consent()` at the moment of processing, not at session start. `spp.consent` updates trigger cache invalidation in the downstream API consent service but not in your ad-hoc caches.

**Storing plaintext PII for "just this one case".** The CI no-PII-in-logs check catches logging, but nothing catches a plaintext database column created by a module that forgot to encrypt. Code review is the only defense — flag any field whose name ends in `_id`, `_number`, `_phone`, `_email`, or similar.

**Creating custom `ir.attachment` records that bypass AV scanning.** The scanner hooks `create()` and `write()` on the Odoo model, but if you insert directly via SQL or through `sudo()` with `scan_status="skipped"`, you bypass detection. Only skip scanning when you generated the file yourself and trust the pipeline that produced it.

**Using `spp_oauth` when you mean API V2 authentication.** `spp_oauth` provides a system-wide JWT key configuration for generic OAuth integrations. The API V2 bearer/signature authentication is separate and documented in {doc}`/developer_guide/api_v2/authentication`. New API clients should follow the API V2 pattern; `spp_oauth` is foundation infrastructure.

## See also

- {doc}`/developer_guide/custom_modules/security` — security groups, privileges, ACL patterns, compliance.yaml
- {doc}`/developer_guide/api_v2/consent` — how consent filters API V2 responses
- {doc}`/developer_guide/api_v2/authentication` — API V2 bearer + signature authentication (different from `spp_oauth`)
- [ISO/IEC TS 27560:2023](https://www.iso.org/standard/82217.html) — consent record schema
- [W3C Data Privacy Vocabulary](https://www.w3.org/TR/dpv/) — DPV terms used by `spp_consent`

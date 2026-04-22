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
| `exact` | Full HMAC-SHA256, hex-encoded | Exact match (email, national ID) |
| `partial` | HMAC-SHA256 of the last 4 characters, truncated to 16 hex chars | Suffix search |
| `phonetic` | Soundex code + HMAC, truncated to 16 hex chars | Fuzzy name search |

All three index types **lowercase the input** before hashing, so queries must also lowercase before calling `compute_blind_index`. Blind indexes use per-purpose salts; `key_mgr.get_salt(purpose, salt_id)` returns the raw salt bytes but is rarely needed — always call `compute_blind_index` instead. Salt bytes are sensitive material; do not log them or surface them in API responses.

### Recipe: an encrypted, searchable field on your model

Putting the pieces together, here's the pattern for adding a searchable encrypted field (e.g., a national ID) to a custom model:

```python
from odoo import api, fields, models


class Applicant(models.Model):
    _name = "myorg.applicant"
    _description = "Benefits applicant"

    name = fields.Char(required=True)

    # The ciphertext column — base64 bytes of the AES-256-GCM output.
    national_id_cipher = fields.Char(string="National ID (encrypted)", groups="myorg.group_pii_reader")

    # The blind index column — searchable deterministic hash.
    national_id_index = fields.Char(string="National ID (index)", index=True)

    # A transient view field for writing. Data only lives here during a write;
    # it is never stored. Users fill this in the form, the ORM writes it out
    # encrypted + indexed, and the field is cleared on read.
    national_id_input = fields.Char(string="National ID", store=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            self._apply_pii_fields(vals)
        return super().create(vals_list)

    def write(self, vals):
        self._apply_pii_fields(vals)
        return super().write(vals)

    def _apply_pii_fields(self, vals):
        plain = vals.pop("national_id_input", None)
        if plain is None:
            return
        key_mgr = self.env["spp.key.manager"]
        vals["national_id_cipher"] = key_mgr.encrypt(
            plaintext=plain,
            purpose="pii",
            key_id="national_id",
        )
        vals["national_id_index"] = key_mgr.compute_blind_index(
            value=plain,
            purpose="pii",
            salt_id="national_id",
            index_type="exact",
        )

    def read_national_id(self):
        """Return the decrypted national ID. Requires PII reader permission."""
        self.ensure_one()
        if not self.national_id_cipher:
            return ""
        return self.env["spp.key.manager"].decrypt(
            ciphertext_b64=self.national_id_cipher,
            purpose="pii",
            key_id="national_id",
        )

    @api.model
    def find_by_national_id(self, national_id):
        """Lookup by national ID — hits the blind index, not the ciphertext."""
        key_mgr = self.env["spp.key.manager"]
        index = key_mgr.compute_blind_index(
            value=national_id,
            purpose="pii",
            salt_id="national_id",
            index_type="exact",
        )
        return self.search([("national_id_index", "=", index)])
```

**Key patterns:**

- **Input via a `store=False` field.** The user-facing `national_id_input` never hits the database. `create()` / `write()` intercept it, encrypt, compute the index, and persist only the derived values.
- **Two columns, not one.** The ciphertext and the index serve different purposes (display + search).
- **Access control on the ciphertext column.** `groups="..."` restricts read access at the ORM level, adding defense in depth — most users shouldn't even see the ciphertext column exists.
- **A dedicated read method.** `read_national_id()` is the explicit decrypt path. A ribbon of `ensure_one()` + group check makes every decrypt intentional.
- **Search via a classmethod that hashes the query.** `find_by_national_id()` does the same lowercasing (via `compute_blind_index`) that was done on write, so user input and stored hash match.

### Exceptions to catch

Security operations raise a small set of exceptions. Handle them explicitly:

| Operation | Exception | When |
|-----------|-----------|------|
| `encrypt()`, `decrypt()`, `get_key()`, `get_salt()` | `AccessError` | User lacks key-management group membership |
| `decrypt()` | `ValueError` | Wrong key, wrong AAD, or corrupted ciphertext |
| `rotate_key()` | `NotImplementedError` | Provider doesn't support rotation (e.g., `config` provider) |
| `rotate_key()` | `AccessError` | User lacks `group_key_admin` |
| `check_consent()` | returns empty recordset | No valid consent — don't catch an exception, check the result |
| `spp.encryption.provider.jwt_sign()` | `ValueError` | Missing or invalid key on the provider record |

A generic `except Exception` around encryption code is an anti-pattern — each exception tells you something specific. Let unexpected ones propagate.

### Testing encryption

Unit tests should exercise the encrypt → decrypt round trip plus the search path. The simplest setup uses the `config` provider, which reads keys from `odoo.conf` parameters — in tests, set the parameters directly on the env:

```python
from odoo.tests import TransactionCase
from odoo.tools import config


class TestApplicantPII(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # In real deployments, keys come from the configured provider.
        # For tests, the default `database` provider works with auto-generated
        # keys — or you can seed a known key for deterministic assertions.
        cls.Applicant = cls.env["myorg.applicant"]

    def test_round_trip(self):
        applicant = self.Applicant.create({
            "name": "Jane Doe",
            "national_id_input": "PH-123456789",
        })
        # Ciphertext stored, plaintext input discarded
        self.assertTrue(applicant.national_id_cipher)
        self.assertFalse(hasattr(applicant, "_national_id_input_stored"))

        # Round trip works
        self.assertEqual(applicant.read_national_id(), "PH-123456789")

    def test_search_by_blind_index(self):
        applicant = self.Applicant.create({
            "name": "Jane Doe",
            "national_id_input": "PH-123456789",
        })
        found = self.Applicant.find_by_national_id("PH-123456789")
        self.assertEqual(found, applicant)

    def test_search_is_case_insensitive(self):
        """Blind indexes lowercase the input — queries must too, and this is built in."""
        applicant = self.Applicant.create({
            "name": "Jane Doe",
            "national_id_input": "PH-123456789",
        })
        # compute_blind_index lowercases both — the search works either way
        self.assertEqual(self.Applicant.find_by_national_id("ph-123456789"), applicant)
```

### Data classification

The ops-side convention divides data into four levels: **PUBLIC**, **INTERNAL**, **CONFIDENTIAL**, **RESTRICTED**. Only `RESTRICTED` requires encryption; `CONFIDENTIAL` is optional. There is no classification model in code — decide per-field whether to encrypt, and be consistent across modules that handle the same data type.

### Trust model

Encryption with `spp_key_management` protects against threats like database theft, DB-only access (e.g., a read-only replica leak), or an operator with PostgreSQL access but no Odoo login. It **does not** protect against:

- A compromised Odoo process (plaintext is in memory during every encrypt/decrypt call)
- An administrator with `group_key_admin` who can call `decrypt()` directly
- Keys stored via the `config` provider when the `odoo.conf` file is readable to the attacker

For stronger threat models, use a cloud KMS or HSM-backed provider and restrict who holds the key-management groups.

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

All methods check access via `_check_key_access()` — non-privileged users get `AccessError`. Read access is granted to `spp_key_management.group_key_operator_officer` and `spp_key_management.group_key_admin`; rotation requires `group_key_admin`; system/sudo always passes. The service uses `@ormcache` on its internal `_get_key_cached` and `_get_salt_cached` helpers so repeated calls don't thrash the provider.

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

The registry routes each `purpose` to a provider (e.g., `pii` → `database`, `financial` → `aws_kms`). Administrators configure this mapping; developers don't need to know which provider their code hits at runtime.

### Purposes (controlled vocabulary)

`purpose` is **not** an arbitrary string — it's a record code on `spp.key.purpose`. The module ships five default purposes in `data/key_purposes.xml`:

| Code | Name | Rotation | Hardware key required |
|------|------|:-------:|:---------------------:|
| `pii` | PII Data | 365 days | No |
| `financial` | Financial Data | 180 days | Yes |
| `credentials` | Credentials (VCs, certificates) | 365 days | Yes |
| `api` | API Security (JWT signing, tokens) | 90 days | No |
| `backup` | Backup Encryption | 365 days | No |

Pass the `code` to `encrypt()`/`decrypt()`/`get_key()` (e.g., `purpose="pii"`). If you pass a code that doesn't exist, the registry **silently falls back to the default provider** — so a typo like `purpose="pii_data"` won't raise; it will just use whichever provider is marked `is_default=True`. Watch for this when writing tests.

Custom purposes can be added as XML records:

```xml
<record id="purpose_biometric" model="spp.key.purpose">
    <field name="name">Biometric Templates</field>
    <field name="code">biometric</field>
    <field name="key_rotation_days">730</field>
    <field name="require_hardware_key" eval="True" />
</record>
```

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

**2. Extend the registry's `provider_type` Selection** and its model lookup:

```python
from odoo import fields, models


class KeyProviderRegistry(models.Model):
    _inherit = "spp.key.provider.registry"

    provider_type = fields.Selection(
        selection_add=[("myhsm", "My HSM")],
        ondelete={"myhsm": "cascade"},
    )

    def _get_provider_model(self):
        """Override: return the env model for our custom provider_type."""
        if self.provider_type == "myhsm":
            return self.env["spp.key.provider.myhsm"]
        return super()._get_provider_model()
```

Notice `_get_provider_model` takes **no argument** (it reads `self.provider_type`) and returns an **env proxy**, not a string. Matching the real signature is important — the base returns `self.env[...]`, and callers use it as a recordset.

**3. Create a registry record** (XML data) mapping one or more purposes to your provider. `spp.key.provider.registry` has a required `name` field and a `purpose_ids` Many2many (not a `purpose` Char) pointing at `spp.key.purpose` records:

```xml
<record id="key_provider_myhsm_pii" model="spp.key.provider.registry">
    <field name="name">My HSM (PII)</field>
    <field name="provider_type">myhsm</field>
    <field name="purpose_ids" eval="[(4, ref('spp_key_management.purpose_pii'))]" />
</record>
```

The `spp.key.manager` routes each `purpose` through its registry entry, so the same `encrypt()` / `decrypt()` calls in application code work unchanged.

### Asymmetric keys

For JWT signing, JSON-LD credential signing, and JWKS publishing, use `spp.asymmetric.key` via `spp.encryption.provider`. The provider supports RSA (2048/3072/4096), EC (P-256/P-384/P-521/secp256k1), and Ed25519.

Call these methods on a specific provider **record**, not on the model directly — `provider.ensure_one()` is enforced:

```python
provider = self.env["spp.encryption.provider"].browse(provider_id)

# Generate a new key (creates a spp.asymmetric.key record)
provider.generate_key(key_type="rsa", key_size=2048)

# Sign a claims dict as a JWT — returns a compact JWT string
token = provider.jwt_sign(
    data={"sub": partner.id, "exp": exp_timestamp, "iat": iat_timestamp},
    include_payload=True,        # Pass the payload inside the JWT (vs signing only)
    include_certificate=False,   # Set True to embed the signing cert in the JWS header (x5c)
    include_cert_hash=False,     # Set True to embed a cert hash instead (x5t#S256)
)

# Publish public keys as JWKS — returns {"keys": [...]}
jwks = provider.get_jwks()
```

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

`check_consent()` verifies `status in ('given', 'renewed')`, the effective/expiry date window, and purpose/recipient match (including category-based matching via `allowed_recipient_types`). It returns a recordset — either the matching consent records or empty. The function **fails closed** if you supply neither `recipient_id` nor `recipient_org_type` — it returns empty with a logged warning rather than matching any consent. This is intentional; don't pattern-match around it.

The `spp.consent.mixin` adds a `consent_ids` Many2many and an `open_record_consent_wizard()` action; inherit it on any model that needs to present its consent records to users.

For the API V2 side — how consent filters response payloads and how `require_consent` on an API client interacts with per-registrant consent — see {doc}`/developer_guide/api_v2/consent`.

## Antivirus scanning

`spp_attachment_av_scan` automatically scans `ir.attachment` records with binary content using ClamAV. No developer code is required to opt in — the module patches `ir.attachment.create()` and `write()` to enqueue a scan job on the worker queue whenever binary data arrives.

### What happens on detection

The attachment's `scan_status` becomes `infected`, the `threat_name` is populated, `is_quarantined` goes to `True`, and an encrypted copy of the original file is stored in `quarantine_data` (using `spp.encryption.provider`). The SHA-256 of the original is stored in `quarantine_hash` for chain-of-custody. The original attachment is **not deleted** — it remains accessible to administrators for forensic review. When an administrator downloads a quarantined file for analysis, the module creates a **separate temporary `ir.attachment`** with `is_forensic_download=True` holding the decrypted binary; a cron job (`_cron_cleanup_forensic_downloads`) purges these after 24 hours.

### Controlling scanning from code

There is no supported developer-facing opt-out for scanning at create time — the `create()` override queues a scan for every binary attachment regardless of `scan_status` or context flags. In practice, scans are fast (the backend returns `clean` for known-good content), so treat scanning as invisible.

If you have a legitimate need to bypass scanning on a specific `write()` (e.g., restoring from quarantine), pass `skip_av_scan_queue=True` in the context — this is used internally by the quarantine-restore path and is not a general-purpose developer API.

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
| No-PII-in-logs check | Blocks logging of `name`, `national_id`, `phone`, `mobile`, `email`, `address`, `birth_date`, `tax_id`, `bank_account` via `_logger.*` calls |
| Naming convention check | Enforces `is_`/`has_`/`can_` prefixes on booleans and other naming rules |
| ACL check | Validates `ir.model.access.csv` rows reference real models and groups |
| Compliance check | Validates modules against their `security/compliance.yaml` declaration |
| API-auth check | All FastAPI router endpoints must depend on a known auth dependency (bearer, signature, authenticated client) with an allowlist for genuinely public endpoints (`/metadata`, DCI JWKS, OAuth token) |
| Performance anti-patterns | N+1 query patterns, `cr.commit()` in loops, offset-based pagination (prefer cursors) |
| UI-patterns check | List view limits, sample data, XPath syntax, statusbar/extension points |

Running pre-commit locally before pushing catches nearly all these. See `.pre-commit-config.yaml` for the complete rule set.

## Common mistakes

**Losing track of `purpose` / `key_id` pairs.** You must decrypt with the same pair you used to encrypt. If code encrypts with `purpose="pii"`, `key_id="national_id"` but stores only the ciphertext, a later refactor that changes the key_id orphans the data. Either record the `purpose` / `key_id` alongside each encrypted value (for encrypt-once-decrypt-later workflows) or document the invariant explicitly.

**Typoing a purpose code.** `purpose="pii_data"` (typo) does not raise — the registry silently falls back to the default provider. Your data encrypts successfully under the wrong key and decrypts with the wrong key going forward. Treat purpose codes like any other identifier: store them as module constants, not string literals scattered through the code.

**Choosing `exact` for every blind index.** `exact` only matches whole values. For prefix or fuzzy searches, use `partial` or `phonetic`. For free-text or multi-word search, blind indexing isn't the right tool — consider a separate tokenized search index instead.

**Forgetting that blind indexes lowercase input.** The hash is over the lowercased value. Queries must also lowercase: `compute_blind_index("JOHN@EXAMPLE.COM", ...)` and `compute_blind_index("john@example.com", ...)` produce the same hash, but `WHERE blind_index = 'hash_of_lowercased'` means your query code must lowercase the search term too.

**Checking consent once at session start.** Consent can be withdrawn at any time. Always call `check_consent()` at the moment of processing, not when the user logs in.

**Storing plaintext PII for "just this one case".** The CI no-PII-in-logs check catches logging, but nothing catches a plaintext database column created by a module that forgot to encrypt. Code review is the only defense — flag any field whose name ends in `_id`, `_number`, `_phone`, `_email`, or similar.

## See also

- {doc}`/developer_guide/custom_modules/security` — security groups, privileges, ACL patterns, compliance.yaml
- {doc}`/developer_guide/api_v2/consent` — how consent filters API V2 responses
- {doc}`/developer_guide/api_v2/authentication` — API V2 bearer + signature authentication (different from `spp_oauth`)
- [ISO/IEC TS 27560:2023](https://www.iso.org/standard/82217.html) — consent record schema
- [W3C Data Privacy Vocabulary](https://www.w3.org/TR/dpv/) — DPV terms used by `spp_consent`

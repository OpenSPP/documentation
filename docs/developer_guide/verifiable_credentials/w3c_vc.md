---
openspp:
  doc_status: draft
  products: [core]
---

# W3C Verifiable Credentials Data Model

This guide is for **developers** implementing or extending OpenSPP's W3C Verifiable Credentials support.

## Overview

OpenSPP implements the [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/), which defines a standard format for expressing credentials on the web in a way that is cryptographically secure, privacy-respecting, and machine-verifiable.

## Core Concepts

### Verifiable Credential Structure

A verifiable credential is a set of claims about a subject, issued by an issuer, with cryptographic proof.

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2"
  ],
  "type": ["VerifiableCredential", "EntitlementCredential"],
  "issuer": "did:web:registry.example",
  "validFrom": "2024-01-01T00:00:00Z",
  "validUntil": "2024-12-31T23:59:59Z",
  "credentialSubject": {
    "id": "did:web:registry.example:beneficiary:abc123",
    "entitlementId": "ENT-2024-001234",
    "programName": "Cash Transfer Program",
    "amount": {
      "value": 5000,
      "currency": "USD"
    }
  },
  "credentialStatus": {
    "type": "BitstringStatusListEntry",
    "statusPurpose": "revocation",
    "statusListIndex": "12345",
    "statusListCredential": "https://registry.example/status/1"
  }
}
```

### Required Fields

| Field | Description | Example |
|-------|-------------|---------|
| `@context` | JSON-LD context defining terms | `["https://www.w3.org/ns/credentials/v2"]` |
| `type` | Credential types (always includes `VerifiableCredential`) | `["VerifiableCredential", "EntitlementCredential"]` |
| `issuer` | DID or URI of the credential issuer | `did:web:registry.example` |
| `validFrom` | Start of credential validity period | `2024-01-01T00:00:00Z` |
| `credentialSubject` | Claims about the subject | `{"id": "did:...", ...}` |

### Optional but Recommended

| Field | Description | Example |
|-------|-------------|---------|
| `validUntil` | End of credential validity period | `2024-12-31T23:59:59Z` |
| `credentialStatus` | Revocation/suspension information | See status section below |
| `id` | Unique credential identifier | `urn:uuid:3fa85f64-5717-4562-b3fc-2c963f66afa6` |

## OpenSPP Implementation

### Credential Types

OpenSPP supports three primary credential types out of the box:

#### 1. Entitlement Credential

Issued when a beneficiary receives an approved entitlement.

```python
# Defined in spp_verifiable_credentials/models/credential_type.py
credential_type = env['spp.credential.type'].search([
    ('code', '=', 'EntitlementCredential')
])

entitlement = env['spp.entitlement'].browse(entitlement_id)
vc = entitlement.issue_credential(credential_type.id)
```

**Credential Subject Claims:**

```json
{
  "entitlementId": "ENT-2024-001234",
  "programName": "Cash Transfer Program",
  "cycle": "2024-Q1",
  "amount": {"value": 5000, "currency": "USD"},
  "status": "approved",
  "validFrom": "2024-01-01",
  "validUntil": "2024-03-31"
}
```

#### 2. Program Membership Credential

Issued when a beneficiary enrolls in a program.

```python
membership = env['spp.program.membership'].browse(membership_id)
vc = membership.issue_credential(credential_type.id)
```

**Credential Subject Claims:**

```json
{
  "programId": "urn:openspp:program:health-insurance-2024",
  "programName": "National Health Insurance",
  "enrollmentDate": "2024-01-15",
  "membershipStatus": "active",
  "coverageType": "family"
}
```

#### 3. Registrant Profile Credential

Issued to verify beneficiary identity attributes.

```python
partner = env['res.partner'].browse(partner_id)
vc = partner.issue_credential(credential_type.id)
```

**Credential Subject Claims (with selective disclosure):**

```json
{
  "id": "did:web:registry.example:beneficiary:abc123",
  "givenName": "Jane",
  "familyName": "Doe",
  "birthDate": "1985-03-15",
  "nationalId": "PH-1234567890",
  "address": {
    "streetAddress": "123 Main St",
    "city": "Manila",
    "region": "NCR"
  }
}
```

### Credential Subject Mixin

Any Odoo model can become a credential subject by inheriting the mixin:

```python
# In your custom module
from odoo import models, fields

class CustomModel(models.Model):
    _name = "custom.model"
    _inherit = ["custom.model", "spp.credential.subject.mixin"]

    name = fields.Char()
    value = fields.Float()

    def get_credential_claims(self, credential_type):
        """Return claims dict for this record"""
        return {
            'customId': self.id,
            'name': self.name,
            'value': self.value,
        }

    def get_credential_subject_id(self):
        """Return DID or URI for this subject"""
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return f"did:web:{base_url.replace('https://', '').replace('http://', '')}:custom:{self.id}"
```

## SD-JWT VC Format

OpenSPP uses SD-JWT (Selective Disclosure JWT) as the default credential format, implementing [draft-ietf-oauth-sd-jwt-vc](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/).

### Structure

An SD-JWT VC consists of three parts separated by tildes (`~`):

```
<Issuer-signed JWT>~<Disclosure 1>~<Disclosure 2>~...~<KB-JWT>
```

**Example:**
```
eyJhbGciOiJFUzI1NiIsInR5cCI6InZjK3NkLWp3dCJ9.eyJpc3MiOiJkaWQ6d2ViOnJl...
~WyJzYWx0MSIsICJnaXZlbk5hbWUiLCAiSmFuZSJd
~WyJzYWx0MiIsICJmYW1pbHlOYW1lIiwgIkRvZSJd
~eyJhbGciOiJFUzI1NiIsInR5cCI6ImtiK2p3dCJ9.eyJub25jZSI6IjEyMzQ1Njc4...
```

### Issuer-Signed JWT

The main JWT contains always-disclosed claims and hashes of selectively-disclosable claims:

```json
{
  "iss": "did:web:registry.example",
  "iat": 1704067200,
  "exp": 1735689599,
  "vct": "https://registry.example/credentials/EntitlementCredential",
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "...",
      "y": "..."
    }
  },
  "entitlementId": "ENT-2024-001234",
  "status": "approved",
  "_sd": [
    "sha256hashofclaim1...",
    "sha256hashofclaim2...",
    "sha256hashofclaim3..."
  ]
}
```

### Disclosures

Each disclosure is a base64url-encoded JSON array:

```json
["salt", "claimName", "claimValue"]
```

**Example:**
```json
["a1b2c3d4e5f6", "givenName", "Jane"]
["f6e5d4c3b2a1", "amount", {"value": 5000, "currency": "USD"}]
```

The holder chooses which disclosures to include when presenting the credential.

### Key Binding JWT (KB-JWT)

Proves the holder possesses the credential by signing a challenge:

```json
{
  "iat": 1704067200,
  "aud": "did:web:verifier.example",
  "nonce": "random-challenge-string",
  "sd_hash": "sha256-hash-of-sd-jwt-body"
}
```

## Configuring Credential Types

### Via UI

Navigate to **Settings → Verifiable Credentials → Credential Types**:

| Field | Description |
|-------|-------------|
| **Name** | Human-readable credential type name |
| **Code** | Technical identifier (e.g., `EntitlementCredential`) |
| **Source Model** | Odoo model that can be credentialed |
| **Format** | `sd_jwt_vc` (recommended) |
| **Validity Days** | How long credentials remain valid |
| **Always Disclosed Claims** | Claims always visible (e.g., `entitlementId`, `status`) |
| **Selectively Disclosable Claims** | Claims holder can choose to reveal |

### Via Data File

```xml
<!-- data/credential_types.xml -->
<odoo>
  <record id="credential_type_entitlement" model="spp.credential.type">
    <field name="name">Entitlement Credential</field>
    <field name="code">EntitlementCredential</field>
    <field name="source_model">spp.entitlement</field>
    <field name="format">sd_jwt_vc</field>
    <field name="validity_days">365</field>
    <field name="always_disclosed_claims">entitlementId,status,validFrom,validUntil</field>
    <field name="selectively_disclosable_claims">amount,programName,beneficiaryName</field>
  </record>
</odoo>
```

### Claim Mapping with JQ

Complex claim mappings use JQ expressions:

```python
# In credential type configuration
claim_mapping = """
{
  "entitlementId": .code,
  "programName": .program_id.name,
  "amount": {
    "value": .initial_amount,
    "currency": .currency_id.name
  },
  "validFrom": .valid_from | strftime("%Y-%m-%d"),
  "validUntil": .valid_to | strftime("%Y-%m-%d")
}
"""
```

## Credential Status

OpenSPP implements [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/) for efficient revocation.

### Status List Structure

```json
{
  "@context": ["https://www.w3.org/ns/credentials/v2"],
  "type": ["VerifiableCredential", "BitstringStatusListCredential"],
  "issuer": "did:web:registry.example",
  "validFrom": "2024-01-01T00:00:00Z",
  "credentialSubject": {
    "type": "BitstringStatusList",
    "statusPurpose": "revocation",
    "encodedList": "H4sIAAAAAAAA/+3BMQEAAADCoPVPbQwfoAAAAAAAAAAAAAAAAAAAAIC3AYbSVKsAQAAA"
  }
}
```

The `encodedList` is a compressed bitstring where each bit represents one credential's status.

### Checking Revocation

```python
# In verifier code
from odoo import http
import requests
import gzip
import base64

def check_credential_status(credential):
    status = credential.get('credentialStatus')
    if not status:
        return True  # No status = not revoked

    # Fetch status list credential
    response = requests.get(status['statusListCredential'])
    status_list_vc = response.json()

    # Decode bitstring
    encoded = status_list_vc['credentialSubject']['encodedList']
    compressed = base64.b64decode(encoded)
    bitstring = gzip.decompress(compressed)

    # Check bit at index
    index = int(status['statusListIndex'])
    byte_index = index // 8
    bit_index = index % 8

    is_revoked = bool(bitstring[byte_index] & (1 << bit_index))
    return not is_revoked
```

### Revoking Credentials

```python
# Revoke an entitlement credential
entitlement = env['spp.entitlement'].browse(entitlement_id)
wallet_credential = env['spp.wallet.credential'].search([
    ('credential_subject_id', '=', entitlement.id),
    ('credential_subject_model', '=', 'spp.entitlement'),
])

wallet_credential.action_revoke(reason="Entitlement cancelled")
```

## DID:web Method

OpenSPP uses the `did:web` method for issuer and subject identifiers.

### DID Format

```
did:web:registry.example:beneficiary:abc123
```

Maps to HTTPS URL:
```
https://registry.example/beneficiary/abc123/did.json
```

### DID Document

```json
{
  "@context": ["https://www.w3.org/ns/did/v1"],
  "id": "did:web:registry.example",
  "verificationMethod": [{
    "id": "did:web:registry.example#key-1",
    "type": "JsonWebKey2020",
    "controller": "did:web:registry.example",
    "publicKeyJwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "...",
      "y": "..."
    }
  }],
  "authentication": ["did:web:registry.example#key-1"],
  "assertionMethod": ["did:web:registry.example#key-1"]
}
```

### Resolving DIDs in OpenSPP

```python
# Get DID document for issuer
did_service = env['spp.did.service']
did_document = did_service.resolve_did('did:web:registry.example')

# Extract public key
verification_method = did_document['verificationMethod'][0]
public_key_jwk = verification_method['publicKeyJwk']
```

## Testing

### Unit Test Example

```python
# tests/test_credential_issuance.py
from odoo.tests import TransactionCase

class TestCredentialIssuance(TransactionCase):
    def setUp(self):
        super().setUp()
        self.credential_type = self.env.ref('spp_verifiable_credentials.credential_type_entitlement')
        self.partner = self.env['res.partner'].create({'name': 'Test Beneficiary'})

    def test_issue_entitlement_credential(self):
        """Test issuing an entitlement credential"""
        entitlement = self.env['spp.entitlement'].create({
            'partner_id': self.partner.id,
            'initial_amount': 5000.0,
            'state': 'approved',
        })

        # Issue credential
        vc = entitlement.issue_credential(self.credential_type.id)

        # Verify structure
        self.assertIn('VerifiableCredential', vc['type'])
        self.assertIn('EntitlementCredential', vc['type'])
        self.assertEqual(vc['credentialSubject']['entitlementId'], entitlement.code)

    def test_selective_disclosure(self):
        """Test SD-JWT selective disclosure"""
        entitlement = self.env['spp.entitlement'].create({
            'partner_id': self.partner.id,
            'initial_amount': 5000.0,
        })

        # Issue SD-JWT VC
        sd_jwt_service = self.env['spp.sd.jwt']
        sd_jwt = sd_jwt_service.issue_sd_jwt_vc(
            entitlement,
            self.credential_type,
            always_disclosed=['entitlementId', 'status'],
            selectively_disclosable=['amount', 'programName']
        )

        # Parse and verify
        parsed = sd_jwt_service.parse_sd_jwt(sd_jwt)
        self.assertIn('_sd', parsed['jwt_payload'])
        self.assertEqual(len(parsed['disclosures']), 2)
```

## Are You Stuck?

**Getting "Invalid context" errors?**

Ensure your `@context` includes the W3C credentials context:
```text
{
  "@context": ["https://www.w3.org/ns/credentials/v2"],
  ...
}
```

For custom claims, add your own context:
```text
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://registry.example/contexts/entitlement/v1"
  ],
  ...
}
```

**Credential verification failing?**

Check these common issues:
1. Credential expired (`validUntil` in the past)
2. Signature invalid (wrong public key or tampered data)
3. Status list shows revoked
4. Issuer DID cannot be resolved

Use the verification service to debug:
```python
sd_jwt_service = env['spp.sd.jwt']
result = sd_jwt_service.verify_sd_jwt_vc(sd_jwt, expected_nonce, expected_audience)
if not result['valid']:
    print(result['error'])
```

**How do I add custom claims?**

Implement `get_credential_claims()` in your model:
```python
def get_credential_claims(self, credential_type):
    claims = super().get_credential_claims(credential_type)
    claims.update({
        'customField': self.custom_field,
        'calculatedValue': self._compute_special_value(),
    })
    return claims
```

**Selective disclosure not working?**

Verify the credential type configuration:
- `format` must be `sd_jwt_vc` (not `jwt_vc` or `ldp_vc`)
- Claims must be listed in `selectively_disclosable_claims`
- Always-disclosed claims should be in `always_disclosed_claims`

## See Also

- {doc}`overview` - Verifiable Credentials Overview
- {doc}`oidc4vci` - OpenID for Verifiable Credential Issuance
- {doc}`implementation` - Implementation Guide
- [W3C VC Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [SD-JWT Specification](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/)
- [Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/)

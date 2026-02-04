---
openspp:
  doc_status: draft
---

# QR Credentials (Claim 169)

**Module:** `spp_claim_169`

## Overview

This module is for **developers** and **sys admins** who need to generate and verify MOSIP Claim 169 QR code credentials for beneficiary identity verification.

QR Credentials implements the MOSIP Claim 169 specification for generating verifiable digital identity credentials. It enables social protection programs to issue QR code-based credentials that can be scanned and verified offline, useful for field verification where internet connectivity is limited.

**What it does:**

- Generates signed QR codes containing identity information
- Maps OpenSPP registrant fields to Claim 169 numbered attributes
- Tracks issued credentials with expiration and revocation status
- Provides APIs for offline credential verification
- Supports multiple credential issuers for different programs

## Dependencies

| Module | Purpose |
|--------|---------|
| `base` | Odoo core framework |
| `mail` | Communication and notifications |
| `spp_security` | Security groups and access control |
| `spp_registry` | Registrant data source |
| `spp_key_management` | Cryptographic key storage |
| `spp_audit` | Audit trail for credential operations |
| `spp_cel_domain` | CEL expressions for transformations |

### External Python Packages

| Package | Purpose |
|---------|---------|
| `qrcode` | QR code generation |
| `Pillow` | Image processing |
| `claim169` | Claim 169 encoding/decoding |

## Claim 169 Attribute Specification

The module implements the MOSIP Claim 169 numbered attribute system:

| Attribute | Name | Description |
|-----------|------|-------------|
| 1 | ID | Unique identifier |
| 4 | Full Name | Complete name |
| 5 | First Name | Given name |
| 7 | Last Name | Family name |
| 8 | Date of Birth | Format: YYYYMMDD |
| 9 | Gender | 1=Male, 2=Female, 3=Others |
| 10 | Address | Physical address |
| 12 | Phone | Phone number |
| 13 | Nationality | ISO 3166-1 country code |
| 16 | Photo | Binary image data |

## Configuration

### 1. Create a Signing Key

Navigate to **Key Management** and create a signing key:

| Field | Value |
|-------|-------|
| Algorithm | ES256 (ECDSA with SHA-256) |
| Format | PEM or JWK |
| Usage | Signing |

### 2. Configure the Issuer

Go to **Claim 169 > Configuration > Issuer Configurations**:

| Field | Description |
|-------|-------------|
| Name | Issuer display name |
| Issuer ID | DID or URI identifier |
| Signing Key | Reference to private key |
| Validity Period | Default credential lifetime |

### 3. Configure Attribute Mappings

Go to **Claim 169 > Configuration > Attribute Mappings** to define how OpenSPP fields map to Claim 169 attributes:

| Transform Type | Description |
|----------------|-------------|
| Direct | Use field value as-is |
| Date YYYYMMDD | Convert date to integer format |
| Gender Code | Map to Claim 169 gender codes |
| Address Combined | Combine multiple address fields |
| CEL Expression | Custom transformation using CEL |

## How QR Generation Works

The QR code generation follows this pipeline:

```
Partner Data -> Attribute Mapping -> CBOR Claims -> CWT Signing -> Compression -> Base45 -> QR Code
```

### Generation Modes

| Mode | Behavior |
|------|----------|
| New Only | Skip partners with existing credentials |
| Replace Expired | Only replace expired credentials |
| Replace All | Replace all existing credentials |

## Data Models

| Model | Purpose |
|-------|---------|
| `spp.claim169.attribute.mapping` | Field-to-attribute configuration |
| `spp.claim169.issuer.config` | Issuer configurations |
| `spp.claim169.credential` | Stored credentials with QR codes |
| `spp.claim169.service` | Service for credential operations |

## Security Groups

| Group | Permissions |
|-------|-------------|
| Claim 169 User | View credentials, generate QR codes |
| Claim 169 Manager | Manage configurations, revoke credentials |

## Usage

### Generate Credentials

1. Navigate to **Registry > Partners**
2. Select one or more partners
3. Click **Action > Generate QR Credentials**
4. Select issuer and validity period
5. Choose generation mode
6. Click **Generate**

### View and Manage Credentials

Go to **Claim 169 > Credentials** to:

- View QR code images
- Download CWT data
- Check expiration status
- Revoke credentials

## Technical Details

| Property | Value |
|----------|-------|
| Technical Name | `spp_claim_169` |
| Category | OpenSPP/Identity |
| Version | 19.0.1.1.0 |
| License | LGPL-3 |
| Development Status | Beta |

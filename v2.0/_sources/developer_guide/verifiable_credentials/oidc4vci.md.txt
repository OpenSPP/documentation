---
openspp:
  doc_status: draft
  products: [core]
---

# OpenID for Verifiable Credential Issuance

This guide is for **developers** implementing credential issuance using the OpenID4VCI protocol in OpenSPP or integrating with OpenSPP as a credential issuer.

## Overview

OpenID for Verifiable Credential Issuance (OpenID4VCI) is a protocol that enables wallets to request and receive verifiable credentials from issuers using OAuth 2.0 flows. OpenSPP implements [OpenID4VCI 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html).

## Why OpenID4VCI?

Traditional credential issuance requires custom protocols and tight integration. OpenID4VCI provides:

**Standardized Flow**
- Wallet-agnostic protocol
- OAuth 2.0 security model
- Well-known discovery endpoints

**Multiple Grant Types**
- Pre-authorized code (push model)
- Authorization code (pull model)
- Combined flows

**Metadata Discovery**
- Issuers advertise capabilities
- Wallets discover supported credentials
- Automatic configuration

## Protocol Flow

### Pre-Authorized Code Flow

This is the most common flow in OpenSPP. The issuer generates a credential offer that the wallet can redeem without user interaction.

```{mermaid}
sequenceDiagram
    participant R as Registry/OpenSPP
    participant B as Beneficiary
    participant W as Wallet

    R->>B: 1. Credential Offer (QR/Link)
    Note over R,B: Contains pre-authorized code

    B->>W: 2. Scan/Open Offer

    W->>R: 3. POST /token
    Note over W,R: Exchange code for access token
    R-->>W: Access Token

    W->>R: 4. POST /credential
    Note over W,R: Present access token
    R-->>W: Verifiable Credential (SD-JWT)

    W->>W: 5. Store in Wallet
```

#### Step-by-Step

**1. Generate Credential Offer**

```python
# In OpenSPP
entitlement = env['spp.entitlement'].browse(entitlement_id)
credential_type = env['spp.credential.type'].search([
    ('code', '=', 'EntitlementCredential')
], limit=1)

# Create credential offer
offer_service = env['spp.credential.offer']
offer = offer_service.create_offer(
    credential_subject=entitlement,
    credential_type=credential_type,
    holder_wallet_did='did:web:wallet.example:holder123'
)

# Generate QR code or deep link
credential_offer_uri = offer.get_credential_offer_uri()
# Returns: openid-credential-offer://?credential_offer=...
```

**2. Credential Offer Format**

```json
{
  "credential_issuer": "https://registry.example",
  "credential_configuration_ids": ["EntitlementCredential"],
  "grants": {
    "urn:ietf:params:oauth:grant-type:pre-authorized_code": {
      "pre-authorized_code": "eyJhbGciOiJFUzI1NiJ9...",
      "tx_code": {
        "input_mode": "numeric",
        "length": 6,
        "description": "Enter the PIN sent to your mobile"
      }
    }
  }
}
```

**3. Token Exchange**

```bash
# Wallet makes request
curl -X POST https://registry.example/api/v1/openid4vci/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=urn:ietf:params:oauth:grant-type:pre-authorized_code" \
  -d "pre-authorized_code=eyJhbGciOiJFUzI1NiJ9..." \
  -d "tx_code=123456"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJFUzI1NiJ9...",
  "token_type": "Bearer",
  "expires_in": 86400,
  "c_nonce": "random-challenge-for-key-binding",
  "c_nonce_expires_in": 86400
}
```

**4. Credential Request**

```bash
curl -X POST https://registry.example/api/v1/openid4vci/credential \
  -H "Authorization: Bearer eyJhbGciOiJFUzI1NiJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "format": "vc+sd-jwt",
    "credential_definition": {
      "type": ["VerifiableCredential", "EntitlementCredential"]
    },
    "proof": {
      "proof_type": "jwt",
      "jwt": "eyJhbGciOiJFUzI1NiJ9..."
    }
  }'
```

Response:
```json
{
  "format": "vc+sd-jwt",
  "credential": "eyJhbGciOiJFUzI1NiIsInR5cCI6InZjK3NkLWp3dCJ9.eyJpc3MiOi...~WyJzYWx0MSIsICJnaXZlbk5hbWUiLCAiSmFuZSJd~..."
}
```

### Authorization Code Flow

For user-initiated credential requests (wallet pulls from issuer).

```{mermaid}
sequenceDiagram
    participant W as Wallet
    participant R as Registry/OpenSPP
    participant B as Beneficiary

    W->>R: 1. Authorization Request
    Note over W,R: With scope, redirect_uri

    R->>B: 2. Authentication & Consent
    B-->>R: Approve

    R-->>W: 3. Authorization Code
    Note over R,W: Via redirect

    W->>R: 4. POST /token
    Note over W,R: Exchange code
    R-->>W: Access Token + c_nonce

    W->>R: 5. POST /credential
    Note over W,R: With proof of possession
    R-->>W: Verifiable Credential
```

**Authorization Request:**

```
https://registry.example/api/v1/openid4vci/authorize
  ?response_type=code
  &client_id=wallet.example
  &redirect_uri=https://wallet.example/callback
  &scope=EntitlementCredential
  &state=random-state-value
```

## Issuer Metadata

OpenSPP publishes issuer metadata at the well-known endpoint.

### Discovery Endpoint

```
GET /.well-known/openid-credential-issuer
```

Response:
```json
{
  "credential_issuer": "https://registry.example",
  "credential_endpoint": "https://registry.example/api/v1/openid4vci/credential",
  "batch_credential_endpoint": "https://registry.example/api/v1/openid4vci/batch_credential",
  "deferred_credential_endpoint": "https://registry.example/api/v1/openid4vci/deferred_credential",
  "display": [
    {
      "name": "OpenSPP Social Registry",
      "locale": "en-US",
      "logo": {
        "uri": "https://registry.example/logo.png",
        "alt_text": "OpenSPP Logo"
      }
    }
  ],
  "credential_configurations_supported": {
    "EntitlementCredential": {
      "format": "vc+sd-jwt",
      "scope": "EntitlementCredential",
      "cryptographic_binding_methods_supported": ["jwk"],
      "cryptographic_suites_supported": ["ES256"],
      "display": [
        {
          "name": "Entitlement Credential",
          "locale": "en-US",
          "logo": {
            "uri": "https://registry.example/credentials/entitlement.png"
          },
          "background_color": "#12107c",
          "text_color": "#FFFFFF"
        }
      ],
      "credential_definition": {
        "type": ["VerifiableCredential", "EntitlementCredential"],
        "credentialSubject": {
          "entitlementId": {
            "mandatory": true,
            "display": [{"name": "Entitlement ID", "locale": "en-US"}]
          },
          "amount": {
            "mandatory": false,
            "display": [{"name": "Amount", "locale": "en-US"}]
          }
        }
      }
    }
  }
}
```

### Configuring Metadata

Metadata is generated from credential type configurations:

```python
# spp_verifiable_credentials/models/credential_type.py
class CredentialType(models.Model):
    _name = "spp.credential.type"

    # Display metadata
    display_name = fields.Char()
    display_locale = fields.Char(default='en-US')
    display_logo_uri = fields.Char()
    background_color = fields.Char(default='#12107c')
    text_color = fields.Char(default='#FFFFFF')

    def get_credential_configuration(self):
        """Generate OpenID4VCI credential configuration"""
        return {
            'format': 'vc+sd-jwt',
            'scope': self.code,
            'cryptographic_binding_methods_supported': ['jwk'],
            'cryptographic_suites_supported': ['ES256'],
            'display': [{
                'name': self.display_name or self.name,
                'locale': self.display_locale,
                'logo': {'uri': self.display_logo_uri} if self.display_logo_uri else None,
                'background_color': self.background_color,
                'text_color': self.text_color,
            }],
            'credential_definition': self._get_credential_definition(),
        }
```

## Implementation in OpenSPP

### Module Structure

```
spp_openid_vci/                        # Base module
├── models/
│   ├── credential_offer.py            # Offer generation
│   └── openid_issuer.py               # Issuer configuration
└── data/
    └── issuer_config.xml

spp_openid_vci_rest_api/               # REST endpoints
├── routers/
│   └── openid_vci.py                  # FastAPI router
└── controllers/
    └── main.py                        # Odoo controller
```

### REST API Endpoints

Implemented using FastAPI in `spp_openid_vci_rest_api`:

```python
# routers/openid_vci.py
from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/openid4vci")

class TokenRequest(BaseModel):
    grant_type: str
    pre_authorized_code: str | None = None
    tx_code: str | None = None

@router.post("/token")
def token_endpoint(request: TokenRequest, env=Depends(get_odoo_env)):
    """Exchange authorization code or pre-authorized code for access token"""
    if request.grant_type == "urn:ietf:params:oauth:grant-type:pre-authorized_code":
        # Validate pre-authorized code
        offer = env['spp.credential.offer'].validate_pre_authorized_code(
            request.pre_authorized_code,
            request.tx_code
        )

        # Generate access token
        token_service = env['spp.token.service']
        access_token = token_service.create_token(
            offer_id=offer.id,
            scope=offer.credential_type_id.code
        )

        return {
            "access_token": access_token,
            "token_type": "Bearer",
            "expires_in": 86400,
            "c_nonce": token_service.generate_nonce(),
            "c_nonce_expires_in": 86400,
        }

    raise HTTPException(status_code=400, detail="Unsupported grant type")


class CredentialRequest(BaseModel):
    format: str
    credential_definition: dict
    proof: dict | None = None

@router.post("/credential")
def credential_endpoint(
    request: CredentialRequest,
    authorization: str = Header(...),
    env=Depends(get_odoo_env)
):
    """Issue credential in exchange for access token"""
    # Validate bearer token
    token = authorization.replace("Bearer ", "")
    token_service = env['spp.token.service']
    token_data = token_service.validate_token(token)

    # Get credential offer
    offer = env['spp.credential.offer'].browse(token_data['offer_id'])

    # Verify proof of possession (KB-JWT)
    if request.proof:
        env['spp.sd.jwt'].verify_key_binding_jwt(
            request.proof['jwt'],
            token_data['c_nonce']
        )

    # Issue credential
    credential_subject = offer.get_credential_subject()
    vc = credential_subject.issue_credential(
        offer.credential_type_id.id,
        holder_did=offer.holder_wallet_did
    )

    return {
        "format": "vc+sd-jwt",
        "credential": vc
    }
```

### Credential Offer Service

```python
# spp_openid_vci/models/credential_offer.py
class CredentialOffer(models.Model):
    _name = "spp.credential.offer"

    credential_type_id = fields.Many2one('spp.credential.type', required=True)
    credential_subject_model = fields.Char()
    credential_subject_id = fields.Integer()
    holder_wallet_did = fields.Char()
    pre_authorized_code = fields.Char()
    tx_code = fields.Char()  # Optional PIN
    state = fields.Selection([
        ('pending', 'Pending'),
        ('redeemed', 'Redeemed'),
        ('expired', 'Expired'),
    ], default='pending')

    def create_offer(self, credential_subject, credential_type, holder_wallet_did=None):
        """Create credential offer for a subject"""
        # Generate pre-authorized code (JWT)
        jwt_service = self.env['spp.jwt.service']
        pre_auth_code = jwt_service.encode({
            'offer_id': self.id,
            'exp': datetime.now() + timedelta(days=7),
        })

        self.write({
            'credential_subject_model': credential_subject._name,
            'credential_subject_id': credential_subject.id,
            'credential_type_id': credential_type.id,
            'holder_wallet_did': holder_wallet_did,
            'pre_authorized_code': pre_auth_code,
        })

        return self

    def get_credential_offer_uri(self):
        """Generate credential offer URI for QR code"""
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        offer_json = {
            'credential_issuer': base_url,
            'credential_configuration_ids': [self.credential_type_id.code],
            'grants': {
                'urn:ietf:params:oauth:grant-type:pre-authorized_code': {
                    'pre-authorized_code': self.pre_authorized_code,
                }
            }
        }

        if self.tx_code:
            offer_json['grants']['urn:ietf:params:oauth:grant-type:pre-authorized_code']['tx_code'] = {
                'input_mode': 'numeric',
                'length': len(self.tx_code),
            }

        import json
        import urllib.parse
        encoded = urllib.parse.quote(json.dumps(offer_json))
        return f"openid-credential-offer://?credential_offer={encoded}"

    def get_credential_subject(self):
        """Get the record this offer is for"""
        return self.env[self.credential_subject_model].browse(self.credential_subject_id)
```

## Security Considerations

### Token Security

**Short-lived Access Tokens**
- Default: 24 hours
- Single-use for credential requests
- Bound to specific credential offer

**Nonce Management**
- Fresh nonce (`c_nonce`) with each token
- Required in proof of possession
- Prevents replay attacks

### Proof of Possession

Wallets must prove they control the key pair:

```json
{
  "proof": {
    "proof_type": "jwt",
    "jwt": "eyJhbGciOiJFUzI1NiIsInR5cCI6ImtiK2p3dCJ9.eyJub25jZSI6ImMtbm9uY2UtdmFsdWUiLCJhdWQiOiJodHRwczovL3JlZ2lzdHJ5LmV4YW1wbGUiLCJpYXQiOjE3MDQwNjcyMDB9..."
  }
}
```

KB-JWT payload:
```json
{
  "nonce": "c-nonce-value-from-token-response",
  "aud": "https://registry.example",
  "iat": 1704067200
}
```

### PIN Protection (TX Code)

For high-value credentials, add PIN requirement:

```python
offer = offer_service.create_offer(
    credential_subject=entitlement,
    credential_type=credential_type,
    holder_wallet_did='did:web:wallet.example:holder123',
    tx_code='123456'  # 6-digit PIN
)

# Send PIN to beneficiary via SMS
sms_service.send_pin(entitlement.partner_id.phone, '123456')
```

## Testing

### Test Credential Issuance Flow

```python
# tests/test_openid4vci.py
from odoo.tests import TransactionCase
import json

class TestOpenID4VCI(TransactionCase):
    def setUp(self):
        super().setUp()
        self.credential_type = self.env.ref('spp_verifiable_credentials.credential_type_entitlement')
        self.entitlement = self.env['spp.entitlement'].create({
            'partner_id': self.env.ref('base.res_partner_1').id,
            'initial_amount': 5000.0,
            'state': 'approved',
        })

    def test_pre_authorized_code_flow(self):
        """Test complete pre-authorized code flow"""
        # 1. Create offer
        offer_service = self.env['spp.credential.offer']
        offer = offer_service.create({
            'credential_type_id': self.credential_type.id,
        })
        offer = offer.create_offer(
            self.entitlement,
            self.credential_type,
            holder_wallet_did='did:web:wallet.test:holder1'
        )

        pre_auth_code = offer.pre_authorized_code
        self.assertTrue(pre_auth_code)

        # 2. Exchange for access token
        token_service = self.env['spp.token.service']
        token_response = token_service.exchange_pre_authorized_code(
            pre_auth_code,
            tx_code=None
        )

        self.assertIn('access_token', token_response)
        self.assertIn('c_nonce', token_response)

        # 3. Request credential
        from fastapi.testclient import TestClient
        client = TestClient(app)  # FastAPI app

        response = client.post(
            '/api/v1/openid4vci/credential',
            headers={
                'Authorization': f"Bearer {token_response['access_token']}"
            },
            json={
                'format': 'vc+sd-jwt',
                'credential_definition': {
                    'type': ['VerifiableCredential', 'EntitlementCredential']
                }
            }
        )

        self.assertEqual(response.status_code, 200)
        credential = response.json()['credential']
        self.assertTrue(credential.startswith('eyJ'))  # JWT format

    def test_issuer_metadata(self):
        """Test well-known metadata endpoint"""
        from fastapi.testclient import TestClient
        client = TestClient(app)

        response = client.get('/.well-known/openid-credential-issuer')
        self.assertEqual(response.status_code, 200)

        metadata = response.json()
        self.assertIn('credential_issuer', metadata)
        self.assertIn('credential_configurations_supported', metadata)
        self.assertIn('EntitlementCredential', metadata['credential_configurations_supported'])
```

## Are You Stuck?

**Getting "invalid_grant" error during token exchange?**

Check:
1. Pre-authorized code hasn't expired (default: 7 days)
2. Code hasn't been redeemed already (single-use)
3. TX code (PIN) matches if required

Debug:
```python
offer = env['spp.credential.offer'].search([
    ('pre_authorized_code', '=', 'your-code-here')
])
print(f"State: {offer.state}")
print(f"Expires: {offer.expiration_date}")
```

**Proof of possession verification failing?**

Common issues:
1. Wrong `c_nonce` - must match value from token response
2. Expired nonce (default: 24 hours)
3. Wrong audience - must be issuer's base URL
4. Clock skew - ensure wallet time is synchronized

Verify KB-JWT:
```python
sd_jwt_service = env['spp.sd.jwt']
result = sd_jwt_service.verify_key_binding_jwt(
    kb_jwt='eyJ...',
    expected_nonce='c-nonce-value',
    expected_audience='https://registry.example'
)
print(result)
```

**Metadata endpoint returning 404?**

Ensure:
1. `spp_openid_vci_rest_api` module is installed
2. FastAPI app is mounted in Odoo
3. Base URL configured: `Settings → System Parameters → web.base.url`

Test:
```bash
curl https://registry.example/.well-known/openid-credential-issuer
```

**How do I customize credential display in wallets?**

Update credential type display metadata:

```python
credential_type = env['spp.credential.type'].browse(type_id)
credential_type.write({
    'display_name': 'My Custom Credential',
    'display_logo_uri': 'https://registry.example/logo.png',
    'background_color': '#FF5733',
    'text_color': '#FFFFFF',
})
```

Wallets will fetch metadata and render credentials accordingly.

## See Also

- {doc}`overview` - Verifiable Credentials Overview
- {doc}`w3c_vc` - W3C VC Data Model
- {doc}`implementation` - Implementation Guide
- [OpenID4VCI Specification](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)
- [OAuth 2.0 RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)

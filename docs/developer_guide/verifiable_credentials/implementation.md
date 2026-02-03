---
openspp:
  doc_status: draft
  products: [core]
---

# Verifiable Credentials Implementation Guide

This guide is for **developers** implementing verifiable credentials functionality in OpenSPP or creating custom credential types.

## Prerequisites

Before implementing VCs, ensure you understand:
- {doc}`/howto/developer_guides/development_setup` - Development setup
- {doc}`/developer_guide/extending/custom_modules` - Creating Odoo modules
- {doc}`overview` - VC concepts and architecture
- {doc}`w3c_vc` - W3C VC data model

## Quick Start

### 1. Install Required Modules

```bash
# In your OpenSPP instance
odoo-bin -i spp_verifiable_credentials,spp_openid_vci,spp_openid_vci_rest_api -d your_database
```

**Module Dependencies:**
- `spp_verifiable_credentials` - Core VC functionality
- `spp_encryption` - Cryptographic signing
- `spp_openid_vci` - OpenID4VCI protocol
- `spp_openid_vci_rest_api` - REST API endpoints

### 2. Configure Issuer Identity

```python
# Set base URL (used for DID:web)
env['ir.config_parameter'].sudo().set_param(
    'web.base.url',
    'https://registry.example'
)

# Configure signing key
key_service = env['spp.key.service']
issuer_key = key_service.create_key(
    key_type='ES256',
    name='VC Issuer Key',
    purpose='signing'
)
```

### 3. Issue Your First Credential

```python
# Get credential type
credential_type = env['spp.credential.type'].search([
    ('code', '=', 'EntitlementCredential')
], limit=1)

# Get subject (e.g., entitlement)
entitlement = env['spp.entitlement'].browse(entitlement_id)

# Issue credential
vc = entitlement.issue_credential(credential_type.id)

print(vc)  # SD-JWT VC string
```

## Creating Custom Credential Types

### Step 1: Define Credential Type

Create a credential type configuration for your domain object.

**Option A: Via UI**

Navigate to **Settings → Verifiable Credentials → Credential Types → Create**:

| Field | Value |
|-------|-------|
| Name | Assessment Credential |
| Code | AssessmentCredential |
| Source Model | spp.event.data |
| Format | SD-JWT VC |
| Validity Days | 180 |

**Option B: Via Data File**

```xml
<!-- my_module/data/credential_types.xml -->
<odoo>
  <record id="credential_type_assessment" model="spp.credential.type">
    <field name="name">Assessment Credential</field>
    <field name="code">AssessmentCredential</field>
    <field name="source_model">spp.event.data</field>
    <field name="format">sd_jwt_vc</field>
    <field name="validity_days">180</field>
    <field name="always_disclosed_claims">assessmentId,date,status</field>
    <field name="selectively_disclosable_claims">score,vulnerabilityIndex,recommendations</field>
    <field name="display_name">Vulnerability Assessment</field>
    <field name="display_logo_uri">https://registry.example/logos/assessment.png</field>
    <field name="background_color">#4A90E2</field>
    <field name="text_color">#FFFFFF</field>
  </record>
</odoo>
```

### Step 2: Implement Credential Subject Mixin

Make your model credentialable by inheriting the mixin:

```python
# my_module/models/event_data.py
from odoo import models, fields, api

class EventData(models.Model):
    _name = "spp.event.data"
    _inherit = ["spp.event.data", "spp.credential.subject.mixin"]

    # Add VC-related computed fields if needed
    can_issue_credential = fields.Boolean(
        compute='_compute_can_issue_credential',
        string="Can Issue Credential"
    )

    @api.depends('state', 'event_type')
    def _compute_can_issue_credential(self):
        """Determine if this assessment can be credentialed"""
        for record in self:
            record.can_issue_credential = (
                record.state == 'completed' and
                record.event_type == 'vulnerability_assessment'
            )

    def get_credential_claims(self, credential_type):
        """Return claims dict for this assessment"""
        self.ensure_one()

        # Get base claims from parent if any
        claims = {}
        if hasattr(super(), 'get_credential_claims'):
            claims = super().get_credential_claims(credential_type)

        # Add assessment-specific claims
        claims.update({
            'assessmentId': self.name,
            'date': self.event_date.isoformat() if self.event_date else None,
            'status': self.state,
            'score': self.score,
            'vulnerabilityIndex': self._compute_vulnerability_index(),
            'assessor': {
                'name': self.assessor_id.name,
                'id': self.assessor_id.external_id,
            },
            'recommendations': self._get_recommendations(),
        })

        return claims

    def get_credential_subject_id(self):
        """Return DID for this assessment subject"""
        self.ensure_one()
        # Use the beneficiary's DID
        if self.partner_id.wallet_did:
            return self.partner_id.wallet_did

        # Fallback to generating DID
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        domain = base_url.replace('https://', '').replace('http://', '')
        return f"did:web:{domain}:beneficiary:{self.partner_id.id}"

    def _compute_vulnerability_index(self):
        """Calculate vulnerability index from assessment data"""
        # Your business logic here
        return 0.75

    def _get_recommendations(self):
        """Get list of recommendations from assessment"""
        return [
            'Enroll in food security program',
            'Access healthcare services',
        ]
```

### Step 3: Add UI Actions

Add button to issue credentials from the form view:

```xml
<!-- my_module/views/event_data_views.xml -->
<odoo>
  <record id="view_event_data_form_inherit_vc" model="ir.ui.view">
    <field name="name">spp.event.data.form.vc</field>
    <field name="model">spp.event.data</field>
    <field name="inherit_id" ref="spp_event_data.view_event_data_form"/>
    <field name="arch" type="xml">
      <xpath expr="//header" position="inside">
        <button name="action_issue_credential"
                type="object"
                string="Issue Credential"
                class="oe_highlight"
                invisible="not can_issue_credential"/>
      </xpath>
    </field>
  </record>
</odoo>
```

Implement the action:

```python
def action_issue_credential(self):
    """Wizard to issue credential for this assessment"""
    self.ensure_one()

    # Get credential type
    credential_type = self.env['spp.credential.type'].search([
        ('code', '=', 'AssessmentCredential')
    ], limit=1)

    if not credential_type:
        raise UserError("Assessment credential type not configured")

    # Open wizard
    return {
        'type': 'ir.actions.act_window',
        'name': 'Issue Assessment Credential',
        'res_model': 'spp.credential.issue.wizard',
        'view_mode': 'form',
        'target': 'new',
        'context': {
            'default_credential_type_id': credential_type.id,
            'default_credential_subject_model': self._name,
            'default_credential_subject_id': self.id,
        }
    }
```

### Step 4: Configure Claim Mapping (Optional)

For complex claim transformations, use JQ expressions:

```python
# In credential type configuration
credential_type.write({
    'claim_mapping_jq': '''
    {
      "assessmentId": .name,
      "date": .event_date | strftime("%Y-%m-%d"),
      "score": .score | tonumber,
      "category": (
        if .score > 0.8 then "high-risk"
        elif .score > 0.5 then "medium-risk"
        else "low-risk"
        end
      ),
      "location": {
        "region": .partner_id.area_id.name,
        "coordinates": {
          "lat": .partner_id.latitude,
          "lon": .partner_id.longitude
        }
      }
    }
    '''
})
```

## Implementing Issuance Flows

### Push Model: Registry-Initiated Issuance

When the registry approves an entitlement, automatically generate a credential offer:

```python
# my_module/models/entitlement.py
class SPPEntitlement(models.Model):
    _inherit = "spp.entitlement"

    def action_approve(self):
        """Approve entitlement and issue credential offer"""
        res = super().action_approve()

        # Generate credential offer for approved entitlements
        for entitlement in self:
            if entitlement.state == 'approved':
                entitlement._issue_credential_offer()

        return res

    def _issue_credential_offer(self):
        """Create and send credential offer to beneficiary"""
        self.ensure_one()

        # Get credential type
        credential_type = self.env['spp.credential.type'].search([
            ('code', '=', 'EntitlementCredential')
        ], limit=1)

        if not credential_type:
            return

        # Get or create wallet for beneficiary
        wallet = self.env['spp.wallet'].get_or_create_wallet(self.partner_id)

        # Create offer
        offer_service = self.env['spp.credential.offer']
        offer = offer_service.create({
            'credential_type_id': credential_type.id,
        })
        offer = offer.create_offer(
            credential_subject=self,
            credential_type=credential_type,
            holder_wallet_did=wallet.wallet_did
        )

        # Generate QR code
        qr_uri = offer.get_credential_offer_uri()

        # Send to beneficiary (SMS, email, or app notification)
        self._send_credential_offer(qr_uri)

        # Log the offer
        self.message_post(
            body=f"Credential offer created: {offer.id}",
            subject="Verifiable Credential Issued"
        )

    def _send_credential_offer(self, qr_uri):
        """Send credential offer to beneficiary"""
        # Option 1: SMS with deep link
        if self.partner_id.mobile:
            sms_service = self.env['spp.sms.service']
            sms_service.send_sms(
                self.partner_id.mobile,
                f"Your entitlement credential is ready: {qr_uri}"
            )

        # Option 2: Email with QR code image
        if self.partner_id.email:
            qr_image = self._generate_qr_image(qr_uri)
            self.env['mail.mail'].create({
                'email_to': self.partner_id.email,
                'subject': 'Your Entitlement Credential',
                'body_html': f'''
                    <p>Your entitlement has been approved.</p>
                    <p>Scan this QR code with your wallet app:</p>
                    <img src="data:image/png;base64,{qr_image}" />
                ''',
            }).send()

        # Option 3: Push notification to mobile app
        if hasattr(self.partner_id, 'fcm_token'):
            notification_service = self.env['spp.notification.service']
            notification_service.send_push(
                self.partner_id.fcm_token,
                title='Credential Available',
                body='Your entitlement credential is ready',
                data={'credential_offer_uri': qr_uri}
            )
```

### Pull Model: Beneficiary-Initiated Request

Allow beneficiaries to request credentials through a portal:

```python
# my_module/controllers/portal.py
from odoo import http
from odoo.http import request

class CredentialPortal(http.Controller):

    @http.route('/my/credentials', type='http', auth='user', website=True)
    def my_credentials(self, **kwargs):
        """List available credentials for current user"""
        partner = request.env.user.partner_id

        # Get credentialable records
        entitlements = request.env['spp.entitlement'].search([
            ('partner_id', '=', partner.id),
            ('state', '=', 'approved'),
        ])

        memberships = request.env['spp.program.membership'].search([
            ('partner_id', '=', partner.id),
            ('state', '=', 'enrolled'),
        ])

        return request.render('my_module.portal_my_credentials', {
            'entitlements': entitlements,
            'memberships': memberships,
        })

    @http.route('/my/credentials/request/<model>/<int:record_id>',
                type='http', auth='user', website=True)
    def request_credential(self, model, record_id, **kwargs):
        """Request credential for a specific record"""
        partner = request.env.user.partner_id

        # Validate access
        record = request.env[model].browse(record_id)
        if record.partner_id != partner:
            return request.redirect('/my/credentials?error=access_denied')

        # Get wallet DID (or create wallet)
        wallet = request.env['spp.wallet'].get_or_create_wallet(partner)

        # Determine credential type
        type_mapping = {
            'spp.entitlement': 'EntitlementCredential',
            'spp.program.membership': 'ProgramMembershipCredential',
        }
        credential_code = type_mapping.get(model)
        credential_type = request.env['spp.credential.type'].search([
            ('code', '=', credential_code)
        ], limit=1)

        # Create offer
        offer_service = request.env['spp.credential.offer']
        offer = offer_service.create({})
        offer = offer.create_offer(
            credential_subject=record,
            credential_type=credential_type,
            holder_wallet_did=wallet.wallet_did
        )

        # Return QR code page
        qr_uri = offer.get_credential_offer_uri()
        return request.render('my_module.credential_offer_qr', {
            'qr_uri': qr_uri,
            'record': record,
        })
```

## Testing

### Unit Tests

```python
# my_module/tests/test_assessment_credentials.py
from odoo.tests import TransactionCase
from odoo.exceptions import UserError

class TestAssessmentCredentials(TransactionCase):

    def setUp(self):
        super().setUp()
        self.credential_type = self.env['spp.credential.type'].create({
            'name': 'Test Assessment Credential',
            'code': 'TestAssessmentCredential',
            'source_model': 'spp.event.data',
            'format': 'sd_jwt_vc',
            'validity_days': 180,
            'always_disclosed_claims': 'assessmentId,date',
            'selectively_disclosable_claims': 'score,recommendations',
        })
        self.partner = self.env['res.partner'].create({
            'name': 'Test Beneficiary',
        })
        self.assessment = self.env['spp.event.data'].create({
            'partner_id': self.partner.id,
            'event_type': 'vulnerability_assessment',
            'state': 'completed',
            'score': 0.75,
        })

    def test_get_credential_claims(self):
        """Test assessment claim generation"""
        claims = self.assessment.get_credential_claims(self.credential_type)

        self.assertIn('assessmentId', claims)
        self.assertIn('score', claims)
        self.assertEqual(claims['score'], 0.75)
        self.assertIn('recommendations', claims)
        self.assertIsInstance(claims['recommendations'], list)

    def test_issue_credential(self):
        """Test issuing assessment credential"""
        vc = self.assessment.issue_credential(self.credential_type.id)

        # Verify it's a valid SD-JWT
        self.assertTrue(isinstance(vc, str))
        self.assertTrue('~' in vc)  # SD-JWT contains tildes

        # Parse and verify structure
        sd_jwt_service = self.env['spp.sd.jwt']
        parsed = sd_jwt_service.parse_sd_jwt(vc)

        self.assertIn('iss', parsed['jwt_payload'])
        self.assertIn('vct', parsed['jwt_payload'])
        self.assertEqual(
            parsed['jwt_payload']['vct'],
            'https://registry.example/credentials/TestAssessmentCredential'
        )

    def test_cannot_issue_for_incomplete_assessment(self):
        """Test that incomplete assessments cannot be credentialed"""
        incomplete = self.env['spp.event.data'].create({
            'partner_id': self.partner.id,
            'event_type': 'vulnerability_assessment',
            'state': 'draft',
        })

        self.assertFalse(incomplete.can_issue_credential)

    def test_selective_disclosure(self):
        """Test selective disclosure configuration"""
        vc = self.assessment.issue_credential(self.credential_type.id)

        sd_jwt_service = self.env['spp.sd.jwt']
        parsed = sd_jwt_service.parse_sd_jwt(vc)

        # Always disclosed claims should be in JWT payload
        self.assertIn('assessmentId', parsed['revealed_claims'])

        # Selectively disclosable claims should be in disclosures
        disclosure_names = [d[1] for d in parsed['disclosures']]
        self.assertIn('score', disclosure_names)
        self.assertIn('recommendations', disclosure_names)
```

### Integration Tests

```python
# my_module/tests/test_credential_issuance_flow.py
from odoo.tests import TransactionCase

class TestCredentialIssuanceFlow(TransactionCase):

    def test_end_to_end_issuance(self):
        """Test complete credential issuance flow"""
        # 1. Create assessment
        assessment = self.env['spp.event.data'].create({
            'partner_id': self.partner.id,
            'event_type': 'vulnerability_assessment',
            'state': 'completed',
            'score': 0.85,
        })

        # 2. Get wallet for beneficiary
        wallet = self.env['spp.wallet'].get_or_create_wallet(self.partner)
        self.assertTrue(wallet)

        # 3. Create credential offer
        credential_type = self.env.ref('my_module.credential_type_assessment')
        offer = self.env['spp.credential.offer'].create({})
        offer = offer.create_offer(
            credential_subject=assessment,
            credential_type=credential_type,
            holder_wallet_did=wallet.wallet_did
        )

        self.assertEqual(offer.state, 'pending')
        self.assertTrue(offer.pre_authorized_code)

        # 4. Simulate wallet redeeming offer
        token_service = self.env['spp.token.service']
        token_data = token_service.exchange_pre_authorized_code(
            offer.pre_authorized_code
        )

        self.assertIn('access_token', token_data)
        self.assertIn('c_nonce', token_data)

        # 5. Issue credential
        credential_subject = offer.get_credential_subject()
        vc = credential_subject.issue_credential(
            credential_type.id,
            holder_did=wallet.wallet_did
        )

        self.assertTrue(vc)
        self.assertEqual(offer.state, 'redeemed')

        # 6. Verify credential stored in wallet
        wallet_credential = self.env['spp.wallet.credential'].search([
            ('wallet_id', '=', wallet.id),
            ('credential_subject_id', '=', assessment.id),
        ])
        self.assertEqual(len(wallet_credential), 1)
        self.assertEqual(wallet_credential.state, 'valid')
```

## Performance Considerations

### Batch Credential Issuance

When issuing credentials for many beneficiaries:

```python
def batch_issue_credentials(self, entitlements):
    """Issue credentials for multiple entitlements efficiently"""
    credential_type = self.env['spp.credential.type'].search([
        ('code', '=', 'EntitlementCredential')
    ], limit=1)

    # Pre-fetch related data
    entitlements = entitlements.with_context(prefetch_fields=True)
    partners = entitlements.mapped('partner_id')
    wallets = self.env['spp.wallet'].get_or_create_wallets_batch(partners)

    # Create offers in batch
    offer_vals = []
    for entitlement in entitlements:
        wallet = wallets.get(entitlement.partner_id.id)
        if wallet:
            offer_vals.append({
                'credential_type_id': credential_type.id,
                'credential_subject_model': 'spp.entitlement',
                'credential_subject_id': entitlement.id,
                'holder_wallet_did': wallet.wallet_did,
            })

    offers = self.env['spp.credential.offer'].create(offer_vals)

    # Generate pre-authorized codes
    for offer in offers:
        offer.create_offer(
            offer.get_credential_subject(),
            credential_type,
            offer.holder_wallet_did
        )

    return offers
```

### Caching Status Lists

Status list verification can be expensive. Cache aggressively:

```python
# Enable caching in production
@tools.ormcache('status_list_id')
def get_status_list_bitstring(self, status_list_id):
    """Get cached bitstring for status list"""
    status_list = self.browse(status_list_id)
    return status_list.get_decoded_bitstring()
```

## Are You Stuck?

**Model doesn't have `issue_credential()` method?**

Ensure you've inherited the mixin:
```python
_inherit = ["your.model", "spp.credential.subject.mixin"]
```

And implemented required methods:
- `get_credential_claims(credential_type)`
- `get_credential_subject_id()`

**Getting "Credential type not found" error?**

Check:
1. Credential type record exists in database
2. Code matches exactly (case-sensitive)
3. Module with credential type data is installed

Debug:
```python
types = env['spp.credential.type'].search([])
for t in types:
    print(f"{t.code}: {t.name}")
```

**Credential offer QR code not working in wallet?**

Verify:
1. QR contains valid `openid-credential-offer://` URI
2. JSON is properly URL-encoded
3. `credential_issuer` URL is accessible
4. Wallet supports OpenID4VCI protocol

Test offer manually:
```python
offer = env['spp.credential.offer'].browse(offer_id)
uri = offer.get_credential_offer_uri()
print(uri)

# Decode and inspect
import urllib.parse
import json
decoded = urllib.parse.unquote(uri.split('credential_offer=')[1])
print(json.dumps(json.loads(decoded), indent=2))
```

**How do I add custom validation before issuance?**

Override `issue_credential` in your model:
```python
def issue_credential(self, credential_type_id, holder_did=None):
    """Add custom validation"""
    self.ensure_one()

    # Custom checks
    if not self.is_eligible_for_credential():
        raise UserError("Record not eligible for credential")

    if self.has_pending_issues():
        raise UserError("Resolve pending issues before issuing")

    # Call parent implementation
    return super().issue_credential(credential_type_id, holder_did)
```

## Next Steps

- **Wallet Integration**: Integrate with mobile wallet apps
- **Verification**: Implement verifier endpoints
- **Revocation**: Set up automated revocation workflows
- **Monitoring**: Add logging and metrics for credential issuance

## See Also

- {doc}`overview` - Verifiable Credentials Overview
- {doc}`w3c_vc` - W3C VC Data Model
- {doc}`oidc4vci` - OpenID4VCI Protocol
- {doc}`/developer_guide/extending/custom_modules` - Creating Custom Modules

---
openspp:
  doc_status: draft
  products: [core]
---

# OpenSPP as DCI Server

**For: developers**

Expose OpenSPP registry data to external DCI-compliant systems — a national MIS querying beneficiary data, other programs checking for duplicates, or research platforms pulling anonymized records.

```{warning}
**This page contains significant inaccuracies and is scheduled for a full rewrite.** Specific problems include:

- **Fictional modules** referenced as real (`spp_dci_server_social`, `spp_dci_api_server`) — the actual search implementation is a stub that returns `501` when the optional `spp_dci_server_social` module is missing
- **Wrong authentication model** — this page describes OAuth 2.0 client-credentials; the real server uses Bearer token (validated against the `dci.api_tokens` system parameter allowlist) + HTTP Message Signature (draft-cavage), with no OAuth2 token endpoint on the DCI server
- **Wrong base URL** — code examples show `/api/v2/dci/...`; the real root path is `/dci_api/v1/...` (set in `spp_dci_server/data/fastapi_endpoint_data.xml`)
- **Wrong endpoint paths** — real endpoints are nested under `/social/registry/` (e.g., `/dci_api/v1/social/registry/sync/search`), not `/registry/`
- **Class names drift** — the `SearchService` shown is fictional; the real implementation is `DCISocialSearchService` in a separate `spp_dci_server_social` module that isn't present in the current repo
- **Signing string format is wrong** in multiple places (see {doc}`protocol` for details)

**Until rewritten, use this page only as a high-level conceptual guide.** For actual implementation, read the source in `openspp-modules-v2/spp_dci_server/` directly.
```

## Prerequisites

- The core DCI modules installed: `spp_dci`, `spp_dci_server`
- A registered signing key (`spp.dci.signing.key`) and sender registry entry (`spp.dci.sender.registry`)
- Familiarity with FastAPI routers and Odoo's `fastapi` module integration
- Understanding of {doc}`protocol` — message envelope, HTTP Signature, endpoints

## Overview

When acting as a DCI server, OpenSPP exposes its beneficiary registry to authorized external systems such as:

- National MIS dashboards (reporting and analytics)
- Other social protection programs (coordination and deduplication)
- Research institutions (anonymized data for analysis)
- Audit systems (compliance verification)

## Architecture

```{mermaid}
sequenceDiagram
    participant External as External System
    participant Auth as OAuth2 Endpoint
    participant API as DCI Server
    participant Service as Search Service
    participant DB as res.partner

    External->>Auth: POST /oauth2/client/token
    Auth-->>External: access_token

    External->>API: POST /registry/sync/search<br/>(Authorization: Bearer token)
    API->>Service: execute_search(request)
    Service->>DB: search([domain])
    DB-->>Service: partners
    Service->>Service: map to DCI Person
    Service-->>API: DCISearchResponse
    API-->>External: 200 OK with results
```

## Module Structure

### Core Server Modules

| Module | Purpose |
|--------|---------|
| `spp_dci_server` | Base server infrastructure with sync/async search endpoints |
| `spp_dci_server_social` | Social Registry-specific implementation |
| `spp_dci_api_server` | FastAPI endpoint registration |

### Key Components

```python
spp_dci_server/
├── routers/
│   ├── auth.py           # OAuth2 token endpoint
│   ├── registry.py       # Search, subscribe, notify endpoints
│   └── wellknown.py      # JWKS and location metadata
├── services/
│   ├── search_service.py         # Query execution and result mapping
│   ├── subscription_service.py   # Event subscription management
│   └── consent_adapter.py        # Privacy and consent checks
├── models/
│   ├── dci_client.py             # API client credentials
│   ├── dci_transaction.py        # Async transaction tracking
│   └── dci_subscription.py       # Event subscriptions
└── schemas/
    ├── envelope.py       # DCI message envelope
    ├── search.py         # Search request/response schemas
    └── person.py         # Person/Group data schemas
```

## Implementing Sync Search

### 1. Define the Router

```python
# spp_dci_server/routers/registry.py
from fastapi import APIRouter, Depends, HTTPException
from ..schemas.search import DCISearchRequest, DCISearchResponse
from ..services.search_service import SearchService
from ..middleware.auth import verify_token
from ..services.signature import verify_signature, sign_message

router = APIRouter(prefix="/registry", tags=["Registry"])

@router.post("/sync/search", response_model=DCISearchResponse)
async def sync_search(
    request: DCISearchRequest,
    token: dict = Depends(verify_token),
    env = Depends(get_env)
):
    """
    Synchronous registry search.

    Supports query types:
    - idtype-value: Simple identifier lookup
    - expression: Complex conditional queries
    - predicate: Predicate-based filtering
    """
    # Verify signature if present
    if request.signature:
        await verify_signature(request, env)

    # Execute search
    service = SearchService(env, token['client_id'])
    response = await service.execute_search(request)

    # Sign response
    response.signature = sign_message(response.header, response.message, env)

    return response
```

### 2. Implement Search Service

```python
# spp_dci_server/services/search_service.py
from odoo import api
from ..schemas.search import DCISearchRequest, DCISearchResponse
from ..services.mapper import DCIPersonMapper

class SearchService:
    """Execute DCI search requests against OpenSPP registry"""

    def __init__(self, env, client_id: str):
        self.env = env
        self.client = env['spp.api.client'].search([('client_id', '=', client_id)], limit=1)
        self.consent_adapter = DCIConsentAdapter(env, self.client)
        self.mapper = DCIPersonMapper()

    async def execute_search(self, request: DCISearchRequest) -> DCISearchResponse:
        """Execute search and return DCI-formatted results"""
        responses = []

        for search_req in request.message.search_request:
            criteria = search_req.search_criteria

            # Build Odoo domain from DCI query
            domain = self._build_domain(criteria)

            # Apply pagination
            page_size = criteria.pagination.page_size
            page_number = criteria.pagination.page_number
            offset = (page_number - 1) * page_size

            # Execute search
            partners = self.env['res.partner'].search(
                domain,
                limit=page_size,
                offset=offset
            )

            # Filter by consent
            allowed_partners = self.consent_adapter.filter_by_consent(partners)

            # Convert to DCI format
            records = [
                self.mapper.to_dci(p)
                for p in allowed_partners
            ]

            # Apply field-level consent filtering
            records = [
                self.consent_adapter.filter_dci_response(p.id, record)
                for p, record in zip(allowed_partners, records)
            ]

            responses.append({
                "reference_id": search_req.reference_id,
                "timestamp": datetime.utcnow().isoformat(),
                "status": "succ",
                "data": {
                    "reg_type": criteria.reg_type,
                    "reg_record_type": "PERSON",
                    "reg_records": records
                },
                "pagination": {
                    "page_size": page_size,
                    "page_number": page_number,
                    "total_count": len(allowed_partners)
                }
            })

        return DCISearchResponse(
            signature="",  # Will be filled by router
            header=self._build_response_header(request),
            message={
                "transaction_id": request.message.transaction_id,
                "correlation_id": str(uuid.uuid4()),
                "search_response": responses
            }
        )

    def _build_domain(self, criteria) -> list:
        """Convert DCI search criteria to Odoo domain"""
        domain = [('is_registrant', '=', True)]

        if criteria.query_type == "idtype-value":
            # Simple identifier lookup
            query = criteria.query
            domain.extend([
                ('registry_id_ids.id_type_id.namespace_uri', '=', query.type),
                ('registry_id_ids.value', '=', query.value)
            ])

        elif criteria.query_type == "expression":
            # Complex expression query
            expression = criteria.query.expression

            if 'seq' in expression:
                # AND conditions
                for condition in expression['seq']:
                    domain.append(
                        self._condition_to_domain(condition)
                    )

            elif 'or' in expression:
                # OR conditions
                or_domains = []
                for sub_expr in expression['or']:
                    for condition in sub_expr.get('seq', []):
                        or_domains.append(
                            self._condition_to_domain(condition)
                        )
                domain.append(('|',) * (len(or_domains) - 1))
                domain.extend(or_domains)

        return domain

    def _condition_to_domain(self, condition: dict) -> tuple:
        """Convert DCI condition to Odoo domain clause"""
        attribute = condition['attribute']
        operator = condition['operator']
        value = condition['value']

        # Map DCI attributes to Odoo fields
        field_mapping = {
            'birth_date': 'birthdate',
            'sex': 'gender_id.code',
            'given_name': 'given_name',
            'surname': 'family_name',
        }

        field = field_mapping.get(attribute, attribute)

        # Map DCI operators to Odoo operators
        operator_mapping = {
            '=': '=',
            '>': '>',
            '<': '<',
            '>=': '>=',
            '<=': '<=',
            'in': 'in',
            'contains': 'ilike'
        }

        odoo_operator = operator_mapping.get(operator, '=')

        return (field, odoo_operator, value)
```

### 3. Implement Data Mapper

```python
# spp_dci_server/services/mapper.py
class DCIPersonMapper:
    """Bidirectional mapping between DCI Person and res.partner"""

    def to_dci(self, partner) -> dict:
        """Convert Odoo partner to DCI Person schema"""
        return {
            "@context": "https://schema.spdci.org/core/v1",
            "@type": "Person",
            "identifier": [
                {
                    "identifier_type": id.id_type_id.namespace_uri or id.id_type_id.name,
                    "identifier_value": id.value
                }
                for id in partner.registry_id_ids
            ],
            "name": {
                "given_name": partner.given_name,
                "surname": partner.family_name,
                "prefix": partner.name_prefix or None,
                "suffix": partner.name_suffix or None
            },
            "sex": self._map_gender(partner.gender_id),
            "birth_date": partner.birthdate.isoformat() if partner.birthdate else None,
            "death_date": partner.deathdate.isoformat() if partner.deathdate else None,
            "address": [self._map_address(a) for a in partner.address_ids],
            "phone_number": [p.value for p in partner.phone_ids],
            "email": [partner.email] if partner.email else [],
            "registration_date": partner.create_date.isoformat(),
            "last_updated": partner.write_date.isoformat()
        }

    def _map_gender(self, gender) -> str:
        """Map OpenSPP gender to DCI sex"""
        if not gender:
            return "unknown"

        mapping = {
            "male": "male",
            "female": "female",
            "other": "other"
        }
        return mapping.get(gender.code.lower(), "unknown")

    def _map_address(self, address) -> dict:
        """Convert Odoo address to DCI Address"""
        return {
            "address_line_1": address.street,
            "address_line_2": address.street2,
            "locality": address.city,
            "sub_region_code": address.district_id.code if address.district_id else None,
            "region_code": address.state_id.code if address.state_id else None,
            "postal_code": address.zip,
            "country_code": address.country_id.code if address.country_id else None,
            "geo_location": {
                "plus_code": {
                    "geometry": {
                        "location": {
                            "latitude": address.partner_latitude,
                            "longitude": address.partner_longitude
                        }
                    }
                }
            } if address.partner_latitude and address.partner_longitude else None
        }
```

## Implementing Async Search

For large queries, use async search with background processing:

```python
# spp_dci_server/routers/registry.py
@router.post("/search", status_code=202)
async def async_search(
    request: DCISearchRequest,
    background_tasks: BackgroundTasks,
    token: dict = Depends(verify_token),
    env = Depends(get_env)
):
    """
    Asynchronous search - returns 202 immediately.

    Results sent to sender_uri callback endpoint.
    """
    # Create transaction record
    transaction = env['spp.dci.transaction'].create({
        'transaction_id': request.message.transaction_id,
        'message_id': request.header.message_id,
        'action': 'search',
        'sender_id': request.header.sender_id,
        'callback_uri': request.header.sender_uri,
        'request_payload': request.json(),
        'state': 'received'
    })

    # Queue background job
    transaction.with_delay(
        channel='root.dci',
        description=f"DCI Search {request.message.transaction_id}"
    ).process_async_search()

    # Return immediate acknowledgment
    return {
        "signature": "",
        "header": {
            "version": "1.0.0",
            "message_id": str(uuid.uuid4()),
            "message_ts": datetime.utcnow().isoformat(),
            "action": "on-search",
            "status": "rcvd",
            "sender_id": env['ir.config_parameter'].get_param('dci.sender_id'),
            "receiver_id": request.header.sender_id
        },
        "message": {
            "transaction_id": request.message.transaction_id
        }
    }
```

### Background Processing

```python
# spp_dci_server/models/dci_transaction.py
from odoo import models, fields
from odoo.addons.queue_job.job import job

class DCITransaction(models.Model):
    _name = 'spp.dci.transaction'
    _description = 'DCI Async Transaction'

    transaction_id = fields.Char(required=True, index=True)
    callback_uri = fields.Char()
    request_payload = fields.Text()
    response_payload = fields.Text()
    state = fields.Selection([
        ('received', 'Received'),
        ('processing', 'Processing'),
        ('success', 'Success'),
        ('rejected', 'Rejected'),
        ('callback_sent', 'Callback Sent'),
    ], default='received')

    @job(default_channel='root.dci')
    def process_async_search(self):
        """Process search request asynchronously"""
        self.state = 'processing'

        try:
            # Execute search
            service = SearchService(self.env, self.sender_id.client_id)
            request = DCISearchRequest(**json.loads(self.request_payload))
            response = service.execute_search(request)

            self.response_payload = response.json()
            self.state = 'success'

            # Send callback
            self._send_callback(response)

        except Exception as e:
            self.state = 'rejected'
            self.error_message = str(e)
            _logger.exception("DCI async search failed: %s", self.transaction_id)

    def _send_callback(self, response):
        """Send response to caller's callback URI"""
        if not self.callback_uri:
            return

        try:
            callback_data = self._build_callback_envelope(response)

            resp = requests.post(
                self.callback_uri,
                json=callback_data,
                timeout=30,
                headers={"Content-Type": "application/json"}
            )
            resp.raise_for_status()
            self.state = 'callback_sent'

        except Exception as e:
            self.state = 'callback_failed'
            # Retry with exponential backoff
            self.with_delay(eta=60, max_retries=3)._send_callback(response)
```

## Implementing Subscriptions

Allow external systems to subscribe to registry events:

```python
# spp_dci_server/routers/registry.py
@router.post("/subscribe", status_code=202)
async def subscribe(
    request: DCISubscribeRequest,
    token: dict = Depends(verify_token),
    env = Depends(get_env)
):
    """Subscribe to registry events"""
    service = SubscriptionService(env)
    subscription_code = service.create_subscription(request)

    return {
        "signature": "",
        "header": {
            "version": "1.0.0",
            "message_id": str(uuid.uuid4()),
            "message_ts": datetime.utcnow().isoformat(),
            "action": "on-subscribe",
            "status": "succ",
            "sender_id": env['ir.config_parameter'].get_param('dci.sender_id'),
            "receiver_id": request.header.sender_id
        },
        "message": {
            "subscription_code": subscription_code,
            "expires": request.message.subscribe_criteria.frequency.end_time
        }
    }
```

### Subscription Service

```python
# spp_dci_server/services/subscription_service.py
class SubscriptionService:
    """Manage DCI event subscriptions"""

    def create_subscription(self, request: DCISubscribeRequest) -> str:
        """Create new subscription, return subscription_code"""
        subscription = self.env['spp.dci.subscription'].create({
            'subscriber_id': request.header.sender_id,
            'callback_uri': request.header.sender_uri,
            'reg_type': request.message.subscribe_criteria.reg_type,
            'reg_event_type': request.message.subscribe_criteria.reg_event_type,
            'filter_expression': json.dumps(request.message.subscribe_criteria.filter),
            'start_time': request.message.subscribe_criteria.frequency.start_time,
            'end_time': request.message.subscribe_criteria.frequency.end_time,
            'state': 'active'
        })
        return subscription.code

    def notify_subscribers(self, event_type: str, records: list):
        """Triggered by Odoo signals when records change"""
        subscriptions = self.env['spp.dci.subscription'].search([
            ('reg_event_type', '=', event_type),
            ('state', '=', 'active')
        ])

        for sub in subscriptions:
            # Queue notification job
            sub.with_delay(
                channel='root.dci'
            )._send_notification(event_type, records)
```

### Trigger Notifications

```python
# spp_dci_server/models/res_partner.py
from odoo import models, api

class ResPartnerDCI(models.Model):
    _inherit = 'res.partner'

    @api.model_create_multi
    def create(self, vals_list):
        """Trigger DCI notifications on registrant creation"""
        records = super().create(vals_list)
        registrants = records.filtered(lambda r: r.is_registrant)

        if registrants:
            self.env['spp.dci.subscription']._trigger_notifications(
                'REGISTRATION', registrants
            )

        return records

    def write(self, vals):
        """Trigger DCI notifications on registrant update"""
        result = super().write(vals)

        if self.filtered(lambda r: r.is_registrant):
            self.env['spp.dci.subscription']._trigger_notifications(
                'UPDATE', self
            )

        return result
```

## Testing

### Unit Test: Search Service

```python
# spp_dci_server/tests/test_search_service.py
from odoo.tests.common import TransactionCase

class TestSearchService(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env['res.partner'].create({
            'name': 'Test Person',
            'given_name': 'John',
            'family_name': 'Doe',
            'birthdate': '1990-01-15',
            'is_registrant': True
        })
        cls.id_type = cls.env['spp.id.type'].create({
            'name': 'National ID',
            'namespace_uri': 'urn:gov:national-id'
        })
        cls.env['spp.registry.id'].create({
            'partner_id': cls.partner.id,
            'id_type_id': cls.id_type.id,
            'value': 'TEST-123456'
        })

    def test_search_by_identifier(self):
        """Test idtype-value search"""
        service = SearchService(self.env, 'test_client')
        request = self._build_search_request(
            query_type='idtype-value',
            query={
                'type': 'urn:gov:national-id',
                'value': 'TEST-123456'
            }
        )
        response = service.execute_search(request)

        self.assertEqual(response.message.search_response[0].status, 'succ')
        records = response.message.search_response[0].data['reg_records']
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]['name']['given_name'], 'John')
```

## Deployment

### Configuration

```bash
# Environment variables
DCI_SENDER_ID=openspp.example.org
DCI_JWT_SECRET=<secure-random-string>
DCI_SIGNING_KEY_PATH=/etc/openspp/dci_key.pem

# System parameters (via Odoo UI or ir.config_parameter)
dci.sender_id = openspp.example.org
dci.callback_base_url = https://openspp.example.org/api/v2/dci
```

### API Endpoint Registration

```python
# spp_dci_api_server/__manifest__.py
{
    'name': 'OpenSPP DCI API Server',
    'depends': ['spp_dci_server', 'fastapi'],
    'data': ['data/fastapi_endpoint.xml'],
    'auto_install': True,
}
```

```xml
<!-- spp_dci_api_server/data/fastapi_endpoint.xml -->
<odoo>
    <record id="fastapi_endpoint_dci" model="fastapi.endpoint">
        <field name="name">DCI Registry API</field>
        <field name="root_path">/api/v2/dci</field>
        <field name="app">spp_dci_server.app:app</field>
        <field name="user_id" ref="base.public_user"/>
    </record>
</odoo>
```

## Common mistakes

**Forgetting to verify the incoming HTTP Signature.** Every DCI request includes a signature covering `(created) (expires) digest`. If you skip verification (or trust only the OAuth token), the server accepts forged or replayed messages. The signature middleware in `spp_dci_server/middleware/signature.py` handles this — don't bypass it.

**Using OAuth token alone for authorization.** OAuth 2.0 verifies the caller is an authenticated client, but DCI requires per-sender verification via the sender registry (`spp.dci.sender.registry`). The `sender_id` in the header must match a registered sender with an active public key.

**Returning unfiltered registry data.** Use `DCIConsentAdapter` (`spp_dci_server/services/consent_adapter.py`) to filter responses based on consent and the sender's legal basis. Returning the raw `res.partner` fields bypasses privacy controls.

**Treating async search as sync.** The `/registry/search` endpoint returns `202 Accepted` with a transaction ID. The caller polls `/registry/txn/status` or waits for a callback to `sender_uri`. Do not block the request thread waiting for results.

**Storing signing key private material in cleartext.** Signing keys should be stored encrypted at rest or in a secrets manager. The `spp.dci.signing.key` model has hooks for this — follow the existing pattern in `spp_dci/models/signing_key.py`.

**Hardcoding `sender_id` or endpoint URLs.** Use Odoo system parameters (`dci.sender_id`, `dci.callback_base_url`) so deployments can override them per environment.

## See also

- {doc}`client_role` — OpenSPP as DCI client
- {doc}`protocol` — DCI protocol details (message envelope, endpoints, signatures)
- [DCI API Standards](https://github.com/spdci/api-standards)

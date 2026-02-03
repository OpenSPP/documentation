---
openspp:
  doc_status: draft
  products: [core]
---

# OpenSPP as DCI Client

This guide is for **developers** implementing OpenSPP as a DCI client to consume data from external registries.

## Overview

When acting as a DCI client, OpenSPP queries external DCI-compliant systems to:

- Import birth/death records from national CRVS
- Check enrollment status in other programs (IBR) to prevent duplication
- Query disability status from national Disability Registry (DR)
- Perform federated beneficiary lookups across multiple social registries

## Architecture

```{mermaid}
sequenceDiagram
    participant OpenSPP as OpenSPP DCI Client
    participant External as External Registry
    participant Registry as res.partner

    OpenSPP->>External: POST /oauth2/client/token
    External-->>OpenSPP: access_token

    OpenSPP->>External: POST /registry/sync/search<br/>(Authorization: Bearer token)
    External-->>OpenSPP: DCI Search Response

    OpenSPP->>OpenSPP: Map DCI Person → partner vals
    OpenSPP->>Registry: create(vals) or write(vals)
    Registry-->>OpenSPP: partner_id
```

## Module Structure

### Client Modules

| Module | Purpose |
|--------|---------|
| `spp_dci_client` | Base client with OAuth, signing, and search |
| `spp_dci_client_crvs` | CRVS-specific client for birth/death imports |
| `spp_dci_client_ibr` | IBR client for enrollment duplication checks |
| `spp_dci_client_dr` | Disability Registry client for PWD queries |
| `spp_dci_indicators` | DCI data integration with eligibility CEL expressions |

### Key Components

```text
spp_dci_client/
├── models/
│   ├── dci_data_source.py        # External registry connection config
│   ├── dci_signing_key.py        # Client signing keys
│   └── dci_import_log.py         # Audit trail of imports
├── services/
│   ├── dci_client.py             # Generic DCI client
│   ├── auth_service.py           # OAuth token management
│   └── mapper.py                 # DCI → Odoo data mapping
└── wizards/
    └── fetch_wizard.py           # UI for manual imports
```

## Base DCI Client

### Data Source Configuration

```python
# spp_dci_client/models/dci_data_source.py
from odoo import models, fields

class DCIDataSource(models.Model):
    _name = 'spp.dci.data.source'
    _description = 'DCI External Registry Connection'

    name = fields.Char(required=True)
    registry_type = fields.Selection([
        ('crvs', 'CRVS - Civil Registration'),
        ('social', 'Social Registry'),
        ('ibr', 'Integrated Beneficiary Registry'),
        ('fr', 'Farmer Registry'),
        ('dr', 'Disability Registry')
    ], required=True)

    # Connection
    base_url = fields.Char(required=True)
    auth_endpoint = fields.Char(default='/oauth2/client/token')
    search_endpoint = fields.Char(default='/registry/sync/search')
    jwks_endpoint = fields.Char(default='/.well-known/jwks.json')

    # Credentials
    client_id = fields.Char(required=True)
    client_secret = fields.Char(required=True)

    # Our identity
    our_sender_id = fields.Char(required=True)
    our_callback_uri = fields.Char()

    # Signing
    signing_key_id = fields.Many2one('spp.dci.signing.key')

    # State
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('error', 'Error')
    ], default='draft')

    def action_test_connection(self):
        """Test connection to external registry"""
        self.ensure_one()
        client = self._get_client()

        try:
            token = client.authenticate()
            self.state = 'active'
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Success',
                    'message': 'Connection successful!',
                    'type': 'success'
                }
            }
        except Exception as e:
            self.state = 'error'
            raise UserError(f"Connection failed: {e}")
```

### Generic Client Service

```python
# spp_dci_client/services/dci_client.py
import httpx
from datetime import datetime
from ..schemas import DCISearchRequest, DCISearchResponse

class DCIClient:
    """Generic DCI client for any registry type"""

    def __init__(self, data_source):
        self.data_source = data_source
        self._token = None
        self._token_expires = None

    async def authenticate(self) -> str:
        """Get OAuth2 access token"""
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.data_source.base_url}{self.data_source.auth_endpoint}",
                data={
                    "grant_type": "client_credentials",
                    "client_id": self.data_source.client_id,
                    "client_secret": self.data_source.client_secret
                }
            )
            response.raise_for_status()
            data = response.json()
            self._token = data["access_token"]
            self._token_expires = datetime.now().timestamp() + data.get("expires_in", 3600)
            return self._token

    async def search_by_identifier(
        self,
        identifier_type: str,
        identifier_value: str
    ) -> DCISearchResponse:
        """Search by identifier type and value"""
        return await self.search(
            query_type="idtype-value",
            query={
                "type": identifier_type,
                "value": identifier_value
            }
        )

    async def search_by_expression(
        self,
        conditions: list,
        logic: str = "and"
    ) -> DCISearchResponse:
        """Search with complex expression"""
        if logic == "and":
            expression = {"seq": conditions}
        else:
            expression = {"or": [{"seq": [c]} for c in conditions]}

        return await self.search(
            query_type="expression",
            query={"expression": expression}
        )

    async def search(
        self,
        query_type: str,
        query: dict,
        reg_type: str = None,
        page_size: int = 100
    ) -> DCISearchResponse:
        """Execute sync search"""
        token = await self._get_token()

        request = self._build_search_request(
            query_type=query_type,
            query=query,
            reg_type=reg_type or self._default_reg_type(),
            page_size=page_size
        )

        # Sign request
        request = self._sign_request(request)

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{self.data_source.base_url}{self.data_source.search_endpoint}",
                json=request.dict(),
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                }
            )
            response.raise_for_status()
            return DCISearchResponse(**response.json())

    def _build_search_request(
        self,
        query_type: str,
        query: dict,
        reg_type: str,
        page_size: int
    ) -> DCISearchRequest:
        """Build DCI search request"""
        now = datetime.utcnow()
        return DCISearchRequest(
            signature="",
            header={
                "version": "1.0.0",
                "message_id": str(uuid.uuid4()),
                "message_ts": now.isoformat(),
                "action": "search",
                "sender_id": self.data_source.our_sender_id,
                "receiver_id": self._extract_receiver_id(),
                "total_count": 1
            },
            message={
                "transaction_id": str(uuid.uuid4()),
                "search_request": [{
                    "reference_id": str(uuid.uuid4()),
                    "timestamp": now.isoformat(),
                    "search_criteria": {
                        "version": "1.0.0",
                        "reg_type": reg_type,
                        "query_type": query_type,
                        "query": query,
                        "pagination": {
                            "page_size": page_size,
                            "page_number": 1
                        }
                    }
                }]
            }
        )

    def _sign_request(self, request: DCISearchRequest) -> DCISearchRequest:
        """Add signature to request"""
        if self.data_source.signing_key_id:
            request.signature = self.data_source.signing_key_id.sign(
                request.header,
                request.message
            )
        return request
```

## CRVS Client

Import birth and death records from national Civil Registration systems.

### Client Implementation

```python
# spp_dci_client_crvs/services/crvs_client.py
from datetime import date
from odoo.addons.spp_dci_client.services.dci_client import DCIClient

class CRVSClient(DCIClient):
    """Specialized client for CRVS systems"""

    async def search_births(
        self,
        date_from: date,
        date_to: date,
        location: str = None,
        page_size: int = 100
    ) -> list:
        """Search for birth registrations in date range"""
        conditions = [
            {"attribute": "birth_date", "operator": ">=", "value": date_from.isoformat()},
            {"attribute": "birth_date", "operator": "<=", "value": date_to.isoformat()}
        ]

        if location:
            conditions.append({
                "attribute": "birth_place.name",
                "operator": "=",
                "value": location
            })

        response = await self.search_by_expression(conditions)

        if response.message.search_response:
            return response.message.search_response[0].data.get("reg_records", [])
        return []

    async def search_deaths(
        self,
        date_from: date,
        date_to: date
    ) -> list:
        """Search for death registrations"""
        conditions = [
            {"attribute": "death_date", "operator": ">=", "value": date_from.isoformat()},
            {"attribute": "death_date", "operator": "<=", "value": date_to.isoformat()}
        ]

        response = await self.search_by_expression(conditions)

        if response.message.search_response:
            return response.message.search_response[0].data.get("reg_records", [])
        return []

    def import_person(self, crvs_person: dict, env) -> int:
        """Import CRVS person into OpenSPP registry"""
        mapper = CRVSPersonMapper()
        vals = mapper.from_dci(crvs_person, env)

        # Check for existing by identifier
        for identifier in crvs_person.get("identifier", []):
            existing = env['res.partner'].search([
                ('registry_id_ids.id_type_id.namespace_uri', '=', identifier['identifier_type']),
                ('registry_id_ids.value', '=', identifier['identifier_value'])
            ], limit=1)

            if existing:
                existing.write(vals)
                return existing.id

        # Create new
        partner = env['res.partner'].create(vals)

        # Link parent relationships
        self._link_parents(partner, crvs_person, env)

        return partner.id

    def _link_parents(self, partner, crvs_person: dict, env):
        """Link parent identifiers to existing partners"""
        for parent_field in ['parent1_identifier', 'parent2_identifier']:
            parent_id = crvs_person.get(parent_field)
            if parent_id:
                parent = env['res.partner'].search([
                    ('registry_id_ids.id_type_id.namespace_uri', '=', parent_id['identifier_type']),
                    ('registry_id_ids.value', '=', parent_id['identifier_value'])
                ], limit=1)

                if parent:
                    env['spp.family.relationship'].create({
                        'individual_id': partner.id,
                        'related_individual_id': parent.id,
                        'relationship_type_id': env.ref('spp_base.relationship_parent').id
                    })
```

### Usage Example

```python
# Import births from last month
from datetime import date, timedelta
from odoo.addons.spp_dci_client_crvs.services.crvs_client import CRVSClient

# Configure CRVS data source
crvs_source = env['spp.dci.data.source'].search([('registry_type', '=', 'crvs')], limit=1)
client = CRVSClient(crvs_source)

# Query births
today = date.today()
last_month = today - timedelta(days=30)
births = await client.search_births(date_from=last_month, date_to=today)

# Import each birth
for birth in births:
    partner_id = client.import_person(birth, env)
    _logger.info("Imported birth: partner_id=%s", partner_id)
```

## IBR Client

Check enrollment status in other programs to prevent duplication.

### Client Implementation

```python
# spp_dci_client_ibr/services/ibr_client.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class ExternalEnrollment:
    """Represents an enrollment in an external program"""
    programme_name: str
    programme_id: str
    enrollment_status: str  # active, suspended, graduated, deceased
    benefit_type: str
    implementing_institution: str
    enrollment_date: Optional[str] = None
    last_benefit_date: Optional[str] = None

class IBRClient(DCIClient):
    """Client for Integrated Beneficiary Registry"""

    async def check_enrollment(
        self,
        identifier_type: str,
        identifier_value: str
    ) -> list[ExternalEnrollment]:
        """
        Check if person is enrolled in any programs in the IBR.

        Returns list of external enrollments.
        """
        # Use IBR-specific /sync/enrolled endpoint
        response = await self._call_enrolled_endpoint(identifier_type, identifier_value)

        enrollments = []
        for record in response.get('enrolled_programmes', []):
            enrollments.append(ExternalEnrollment(
                programme_name=record.get('programme_name'),
                programme_id=record.get('programme_identifier'),
                enrollment_status=record.get('enrollment_status'),
                benefit_type=record.get('benefit', {}).get('benefit_type'),
                implementing_institution=record.get('implementing_institution'),
                enrollment_date=record.get('enrollment_date'),
                last_benefit_date=record.get('last_benefit_date')
            ))
        return enrollments

    async def _call_enrolled_endpoint(
        self,
        identifier_type: str,
        identifier_value: str
    ) -> dict:
        """Call IBR-specific /registry/sync/enrolled endpoint"""
        token = await self._get_token()

        request = self._build_enrolled_request(identifier_type, identifier_value)
        request = self._sign_request(request)

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.data_source.base_url}/registry/sync/enrolled",
                json=request.dict(),
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                }
            )
            response.raise_for_status()
            return response.json().get('message', {})
```

### Integration with Enrollment Workflow

```python
# spp_dci_client_ibr/models/program_membership.py
from odoo import models, fields, api
from odoo.exceptions import UserError

class ProgramMembershipIBRCheck(models.Model):
    _inherit = 'spp.program.membership'

    # IBR check results
    ibr_checked = fields.Boolean(default=False)
    ibr_check_date = fields.Datetime()
    ibr_enrollments_found = fields.Integer()
    ibr_duplicate_warning = fields.Text()

    @api.model_create_multi
    def create(self, vals_list):
        """Check IBR before creating enrollment"""
        for vals in vals_list:
            if vals.get('partner_id'):
                self._check_ibr_enrollment(vals)
        return super().create(vals_list)

    def _check_ibr_enrollment(self, vals: dict):
        """Check IBR and add warnings/blocks"""
        # Get IBR data source
        ibr_source = self.env['spp.dci.data.source'].search([
            ('registry_type', '=', 'ibr'),
            ('state', '=', 'active')
        ], limit=1)

        if not ibr_source:
            return  # No IBR configured, skip check

        partner = self.env['res.partner'].browse(vals['partner_id'])
        primary_id = partner.registry_id_ids.filtered(lambda r: r.id_type_id.is_primary)[:1]

        if not primary_id:
            return

        # Check IBR
        from odoo.addons.spp_dci_client_ibr.services.ibr_client import IBRClient
        client = IBRClient(ibr_source)
        enrollments = asyncio.run(
            client.check_enrollment(
                primary_id.id_type_id.namespace_uri,
                primary_id.value
            )
        )

        vals['ibr_checked'] = True
        vals['ibr_check_date'] = fields.Datetime.now()
        vals['ibr_enrollments_found'] = len(enrollments)

        # Filter active enrollments
        active = [e for e in enrollments if e.enrollment_status == 'active']

        if active:
            program_names = [e.programme_name for e in active]
            vals['ibr_duplicate_warning'] = (
                f"Warning: Already enrolled in: {', '.join(program_names)}"
            )

            # Optionally block enrollment
            if self.env['ir.config_parameter'].get_param('ibr.block_duplicates') == 'true':
                raise UserError(
                    f"Cannot enroll {partner.name}: Already enrolled in {program_names[0]}"
                )
```

### Usage Example

```python
# Check enrollment before creating membership
partner = env['res.partner'].browse(123)

# Create enrollment (will trigger IBR check automatically)
membership = env['spp.program.membership'].create({
    'partner_id': partner.id,
    'program_id': env.ref('spp_programs.program_cash_transfer').id
})

# Check results
if membership.ibr_duplicate_warning:
    _logger.warning("Duplicate enrollment: %s", membership.ibr_duplicate_warning)
```

## Disability Registry Client

Query external Disability Registries for PWD status.

### Client Implementation

```python
# spp_dci_client_dr/services/dr_client.py
class DRClient(DCIClient):
    """Client for Disability Registry"""

    async def get_disability_status(
        self,
        identifier_type: str,
        identifier_value: str
    ) -> dict:
        """
        Query disability status for a person.

        Returns disability_info with limitation types and severity levels.
        """
        response = await self.search_by_identifier(identifier_type, identifier_value)

        if response.message.search_response:
            records = response.message.search_response[0].data.get("reg_records", [])
            if records:
                return records[0].get('disability_info', [])

        return []

    def has_severe_disability(self, disability_info: list) -> bool:
        """Check if person has severe disability (level 3 or 4)"""
        return any(d.get('functional_severity', 0) >= 3 for d in disability_info)

    def get_disability_types(self, disability_info: list) -> list[str]:
        """Extract disability limitation types"""
        return [d.get('disability_limitation_type') for d in disability_info]
```

### Integration with Eligibility

```python
# Using DR data in eligibility checks
from odoo.addons.spp_dci_client_dr.services.dr_client import DRClient

# Query DR for disability status
dr_source = env['spp.dci.data.source'].search([('registry_type', '=', 'dr')], limit=1)
client = DRClient(dr_source)

partner = env['res.partner'].browse(123)
national_id = partner.registry_id_ids.filtered(lambda r: r.id_type_id.is_primary)[:1]

disability_info = await client.get_disability_status(
    national_id.id_type_id.namespace_uri,
    national_id.value
)

# Check eligibility
is_eligible = client.has_severe_disability(disability_info)
```

## DCI-Indicators Integration

Integrate DCI data with OpenSPP's indicator system for CEL-based eligibility.

### Available Metrics

```python
# spp_dci_indicators/services/dci_metrics.py

# Register DCI metrics for CEL expressions
METRICS = {
    'dci.crvs.is_alive': {
        'source': 'crvs',
        'type': 'boolean',
        'description': 'Person is alive per CRVS',
        'ttl': 86400  # 24 hours
    },
    'dci.ibr.is_enrolled': {
        'source': 'ibr',
        'type': 'boolean',
        'description': 'Enrolled in any IBR program',
        'ttl': 3600  # 1 hour
    },
    'dci.ibr.program_count': {
        'source': 'ibr',
        'type': 'number',
        'description': 'Number of active enrollments',
        'ttl': 3600
    },
    'dci.dr.has_disability': {
        'source': 'dr',
        'type': 'boolean',
        'description': 'Has any registered disability',
        'ttl': 86400
    },
    'dci.dr.disability_level': {
        'source': 'dr',
        'type': 'number',
        'description': 'Highest disability severity level (1-4)',
        'ttl': 86400
    }
}
```

### CEL Expressions with DCI Data

```python
# Example eligibility expressions using DCI metrics

# PWD Cash Transfer Program
"dci.dr.has_disability == true and dci.dr.disability_level >= 3 and dci.ibr.is_enrolled == false"

# Senior Citizen Allowance
"dci.crvs.is_alive == true and age_years(r.birthdate) >= 60"

# Poverty-targeted (exclude already enrolled)
"poverty_score >= 0.7 and dci.ibr.program_count == 0"

# Household with disabled member
"members.exists(m, m.dci.dr.has_disability == true)"
```

## Testing

### Unit Test: CRVS Client

```python
# spp_dci_client_crvs/tests/test_crvs_client.py
from odoo.tests.common import TransactionCase
from unittest.mock import patch, AsyncMock

class TestCRVSClient(TransactionCase):

    def setUp(self):
        super().setUp()
        self.data_source = self.env['spp.dci.data.source'].create({
            'name': 'Test CRVS',
            'registry_type': 'crvs',
            'base_url': 'https://test-crvs.example.org',
            'client_id': 'test_client',
            'client_secret': 'test_secret',
            'our_sender_id': 'openspp.test'
        })

    @patch('httpx.AsyncClient.post')
    async def test_search_births(self, mock_post):
        """Test birth search returns results"""
        mock_post.return_value = AsyncMock(
            status_code=200,
            json=lambda: {
                "message": {
                    "search_response": [{
                        "data": {
                            "reg_records": [
                                {
                                    "name": {"given_name": "John", "surname": "Doe"},
                                    "birth_date": "2024-01-15"
                                }
                            ]
                        }
                    }]
                }
            }
        )

        from odoo.addons.spp_dci_client_crvs.services.crvs_client import CRVSClient
        client = CRVSClient(self.data_source)

        births = await client.search_births(
            date_from=date(2024, 1, 1),
            date_to=date(2024, 12, 31)
        )

        self.assertEqual(len(births), 1)
        self.assertEqual(births[0]['name']['given_name'], 'John')
```

## See Also

- {doc}`server_role` - OpenSPP as DCI server
- {doc}`protocol` - DCI protocol details
- [DCI API Standards](https://github.com/spdci/api-standards)

---
openspp:
  doc_status: draft
---

# Extending DRIMS

This guide shows **developers** how to extend DRIMS with custom functionality using Odoo inheritance patterns.

If you're looking to configure DRIMS without writing code (adding warehouses, setting alert thresholds, etc.), see {doc}`/config_guide/drims/index`.

## Before You Start

**Prerequisites:**
- Development environment set up (see OpenSPP development docs)
- Familiarity with Odoo 19 model inheritance
- Understanding of DRIMS data model ({doc}`architecture`)
- Python 3.11+, git basics

**What You'll Learn:**
- How to add custom fields to DRIMS models
- How to extend vocabulary codes via XML data
- How to create custom alert types with automated checks
- How to add custom KPIs to incident dashboards
- How to create country-specific modules (like `spp_drims_sl`)

## Extension Patterns

### Adding Custom Fields

Extend DRIMS models using Odoo's model inheritance pattern.

**Pattern:**

```python
# my_custom_drims/models/drims_request.py

from odoo import models, fields

class DrimsRequestExtension(models.Model):
    _inherit = "spp.drims.request"

    custom_field = fields.Char(
        string="Custom Field",
        help="Your custom field description"
    )
```

**Example: Add Local Government Approval**

```python
# spp_drims_local_approval/models/drims_request.py

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DrimsRequestLocalApproval(models.Model):
    _inherit = "spp.drims.request"

    local_govt_approval = fields.Selection(
        [
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        string="Local Government Approval",
        default='pending',
        tracking=True,
    )
    local_govt_approver_id = fields.Many2one(
        'res.users',
        string="Local Approver",
        tracking=True,
    )
    local_govt_approval_date = fields.Date(
        string="Local Approval Date",
        readonly=True,
    )

    def action_local_approve(self):
        """Approve request at local government level."""
        for rec in self:
            if not self.env.user.has_group('spp_drims.group_drims_local_approver'):
                raise ValidationError("You don't have permission to approve requests.")
            rec.write({
                'local_govt_approval': 'approved',
                'local_govt_approver_id': self.env.user.id,
                'local_govt_approval_date': fields.Date.today(),
            })
```

**Testing:**

```python
# spp_drims_local_approval/tests/test_local_approval.py

from odoo.tests import tagged
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

@tagged('post_install', '-at_install')
class TestLocalApproval(TransactionCase):

    def setUp(self):
        super().setUp()
        self.request = self.env['spp.drims.request'].create({
            'incident_id': self.ref('spp_hazard.demo_incident_1'),
            'destination_area_id': self.ref('spp_area.area_province_1'),
        })
        self.approver = self.env['res.users'].create({
            'name': 'Local Approver',
            'login': 'local_approver',
            'groups_id': [(4, self.ref('spp_drims.group_drims_local_approver'))],
        })

    def test_local_approval_success(self):
        """Test successful local approval."""
        self.request.with_user(self.approver).action_local_approve()
        self.assertEqual(self.request.local_govt_approval, 'approved')
        self.assertEqual(self.request.local_govt_approver_id, self.approver)
        self.assertIsNotNone(self.request.local_govt_approval_date)

    def test_local_approval_permission_denied(self):
        """Test approval fails without permission."""
        regular_user = self.env['res.users'].create({
            'name': 'Regular User',
            'login': 'regular_user',
        })
        with self.assertRaises(ValidationError):
            self.request.with_user(regular_user).action_local_approve()
```

### Adding Vocabulary Codes

Vocabularies in DRIMS use `spp_vocabulary` for controlled value lists. Extend them via XML data files.

**Pattern:**

```xml
<!-- my_custom_drims/data/vocabulary_codes.xml -->
<odoo>
    <record id="my_custom_code" model="spp.vocabulary.code">
        <field name="code">my_code</field>
        <field name="display">{"en_US": "My Custom Code"}</field>
        <field name="vocabulary_id" ref="spp_drims.vocab_drims_priority"/>
    </record>
</odoo>
```

**Example: Add "Urgent - Emergency" Priority**

```xml
<!-- spp_drims_emergency_priority/data/priority_codes.xml -->
<odoo>
    <record id="priority_urgent_emergency" model="spp.vocabulary.code">
        <field name="code">urgent_emergency</field>
        <field name="display">{"en_US": "Urgent - Emergency", "es_ES": "Urgente - Emergencia"}</field>
        <field name="vocabulary_id" ref="spp_drims.vocab_drims_priority"/>
        <field name="sequence">5</field>
    </record>
</odoo>
```

**Manifest Declaration:**

```python
# spp_drims_emergency_priority/__manifest__.py
{
    'name': 'DRIMS Emergency Priority',
    'version': '19.0.1.0.0',
    'depends': ['spp_drims'],
    'data': [
        'data/priority_codes.xml',
    ],
}
```

**Using the New Code:**

```python
# In your code
request = env['spp.drims.request'].create({
    'priority_id': env.ref('spp_drims_emergency_priority.priority_urgent_emergency').id,
    # ... other fields
})
```

### Creating Custom Alert Types

Custom alerts require:
1. Adding vocabulary code for the alert type
2. Implementing cron check method
3. Registering the cron job

**Pattern:**

```python
class CustomAlert(models.Model):
    _inherit = "spp.drims.alert"

    def _cron_check_custom_alert(self):
        """Scheduled check for custom alert conditions."""
        # Your check logic here
        alerts_to_create = []

        # Check conditions
        if condition_met:
            alerts_to_create.append({
                'alert_type_id': self.env.ref('module.alert_type_code').id,
                'title': 'Alert Title',
                'description': 'Alert description',
                'priority': 'high',
                # ... other fields
            })

        # Create alerts in batch
        if alerts_to_create:
            self.create(alerts_to_create)
```

**Example: Temperature Monitoring Alert**

```python
# spp_drims_temperature/models/drims_alert.py

from odoo import models, fields, api
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)

class DrimsAlertTemperature(models.Model):
    _inherit = "spp.drims.alert"

    warehouse_temp_celsius = fields.Float(
        string="Warehouse Temperature (°C)",
        help="Current temperature reading"
    )

    def _cron_check_temperature_alerts(self):
        """Check for warehouses with temperature outside safe range."""
        _logger.info("Running temperature alert check")

        # Get DRIMS warehouses with temperature sensors
        warehouses = self.env['stock.warehouse'].search([
            ('is_drims_warehouse', '=', True),
            ('temp_sensor_enabled', '=', True),
        ])

        alerts_to_create = []
        alert_type = self.env.ref('spp_drims_temperature.alert_type_temp_warning')

        for warehouse in warehouses:
            # Get latest temperature reading
            temp = warehouse.get_current_temperature()

            # Check if outside safe range (2°C - 8°C for cold chain)
            if temp < 2.0 or temp > 8.0:
                # Check if alert already exists
                existing = self.search([
                    ('warehouse_id', '=', warehouse.id),
                    ('alert_type_id', '=', alert_type.id),
                    ('state', 'in', ['active', 'acknowledged']),
                ])

                if existing:
                    # Update existing alert
                    existing.write({
                        'warehouse_temp_celsius': temp,
                        'current_value': temp,
                    })
                else:
                    # Create new alert
                    priority = 'critical' if temp < 0 or temp > 10 else 'high'
                    alerts_to_create.append({
                        'alert_type_id': alert_type.id,
                        'warehouse_id': warehouse.id,
                        'title': f'Temperature Alert: {warehouse.name}',
                        'description': f'Temperature {temp}°C outside safe range (2-8°C)',
                        'priority': priority,
                        'current_value': temp,
                        'threshold_value': 8.0 if temp > 8 else 2.0,
                        'warehouse_temp_celsius': temp,
                    })

        if alerts_to_create:
            self.create(alerts_to_create)
            _logger.info(f"Created {len(alerts_to_create)} temperature alerts")
```

**Vocabulary Code:**

```xml
<!-- spp_drims_temperature/data/alert_types.xml -->
<odoo>
    <record id="alert_type_temp_warning" model="spp.vocabulary.code">
        <field name="code">temp_warning</field>
        <field name="display">{"en_US": "Temperature Warning"}</field>
        <field name="vocabulary_id" ref="spp_drims.vocab_alert_types"/>
    </record>
</odoo>
```

**Cron Job:**

```xml
<!-- spp_drims_temperature/data/ir_cron.xml -->
<odoo>
    <record id="cron_check_temperature" model="ir.cron">
        <field name="name">DRIMS: Check Temperature Alerts</field>
        <field name="model_id" ref="spp_drims.model_spp_drims_alert"/>
        <field name="state">code</field>
        <field name="code">model._cron_check_temperature_alerts()</field>
        <field name="interval_number">15</field>
        <field name="interval_type">minutes</field>
        <field name="numbercall">-1</field>
        <field name="active">True</field>
    </record>
</odoo>
```

**Testing:**

```python
# spp_drims_temperature/tests/test_temperature_alerts.py

from odoo.tests import tagged
from odoo.tests.common import TransactionCase
from unittest.mock import patch

@tagged('post_install', '-at_install')
class TestTemperatureAlerts(TransactionCase):

    def setUp(self):
        super().setUp()
        self.warehouse = self.env['stock.warehouse'].create({
            'name': 'Cold Storage Warehouse',
            'code': 'COLD',
            'is_drims_warehouse': True,
            'temp_sensor_enabled': True,
        })
        self.alert_model = self.env['spp.drims.alert']

    @patch('odoo.addons.spp_drims_temperature.models.stock_warehouse.Warehouse.get_current_temperature')
    def test_temperature_too_high_creates_alert(self, mock_temp):
        """Test alert creation when temperature is too high."""
        mock_temp.return_value = 12.0  # Above 8°C threshold

        self.alert_model._cron_check_temperature_alerts()

        alert = self.alert_model.search([
            ('warehouse_id', '=', self.warehouse.id),
            ('alert_type_id.code', '=', 'temp_warning'),
        ])

        self.assertEqual(len(alert), 1)
        self.assertEqual(alert.priority, 'critical')
        self.assertEqual(alert.warehouse_temp_celsius, 12.0)

    @patch('odoo.addons.spp_drims_temperature.models.stock_warehouse.Warehouse.get_current_temperature')
    def test_temperature_in_range_no_alert(self, mock_temp):
        """Test no alert when temperature is within safe range."""
        mock_temp.return_value = 5.0  # Within 2-8°C range

        self.alert_model._cron_check_temperature_alerts()

        alert = self.alert_model.search([
            ('warehouse_id', '=', self.warehouse.id),
            ('alert_type_id.code', '=', 'temp_warning'),
        ])

        self.assertEqual(len(alert), 0)
```

### Adding Custom KPIs

DRIMS displays KPIs on incident cards. Extend the incident model to add custom metrics.

**Pattern:**

```python
class HazardIncidentExtension(models.Model):
    _inherit = "spp.hazard.incident"

    custom_kpi = fields.Float(
        string="Custom KPI",
        compute="_compute_custom_kpi",
        store=True,
    )

    @api.depends('drims_donation_ids', 'drims_request_ids')
    def _compute_custom_kpi(self):
        for rec in self:
            # Your calculation logic
            rec.custom_kpi = calculated_value
```

**Example: Average Response Time KPI**

```python
# spp_drims_response_time/models/hazard_incident.py

from odoo import models, fields, api
from datetime import timedelta

class HazardIncidentResponseTime(models.Model):
    _inherit = "spp.hazard.incident"

    avg_request_response_hours = fields.Float(
        string="Avg Response Time (hours)",
        compute="_compute_avg_response_time",
        store=True,
        help="Average time from request creation to first dispatch"
    )

    @api.depends('drims_request_ids.date_requested', 'drims_request_ids.picking_ids.date_departed')
    def _compute_avg_response_time(self):
        for incident in self:
            requests_with_dispatch = incident.drims_request_ids.filtered(
                lambda r: r.picking_ids and r.picking_ids[0].date_departed
            )

            if not requests_with_dispatch:
                incident.avg_request_response_hours = 0.0
                continue

            total_hours = 0
            count = 0

            for request in requests_with_dispatch:
                first_dispatch = min(request.picking_ids, key=lambda p: p.date_departed or fields.Datetime.now())
                if first_dispatch.date_departed:
                    delta = first_dispatch.date_departed - request.date_requested
                    total_hours += delta.total_seconds() / 3600
                    count += 1

            incident.avg_request_response_hours = total_hours / count if count > 0 else 0.0
```

**Add to Dashboard View:**

```xml
<!-- spp_drims_response_time/views/hazard_incident_views.xml -->
<odoo>
    <record id="view_spp_hazard_incident_kanban_inherit" model="ir.ui.view">
        <field name="name">spp.hazard.incident.kanban.response_time</field>
        <field name="model">spp.hazard.incident</field>
        <field name="inherit_id" ref="spp_drims.view_spp_hazard_incident_kanban"/>
        <field name="arch" type="xml">
            <xpath expr="//div[@name='drims_kpis']" position="inside">
                <div class="col-6 col-md-3 mb-2">
                    <div class="card bg-info text-white">
                        <div class="card-body p-2">
                            <div class="text-center">
                                <strong><field name="avg_request_response_hours" widget="float_time"/></strong>
                            </div>
                            <div class="text-center small">Avg Response Time</div>
                        </div>
                    </div>
                </div>
            </xpath>
        </field>
    </record>
</odoo>
```

**Testing:**

```python
# spp_drims_response_time/tests/test_response_time_kpi.py

from odoo.tests import tagged
from odoo.tests.common import TransactionCase
from datetime import datetime, timedelta

@tagged('post_install', '-at_install')
class TestResponseTimeKPI(TransactionCase):

    def setUp(self):
        super().setUp()
        self.incident = self.env['spp.hazard.incident'].create({
            'name': 'Test Incident',
            'incident_category_id': self.ref('spp_hazard.category_flood'),
        })

    def test_avg_response_time_calculation(self):
        """Test average response time is calculated correctly."""
        # Create request at time T
        request_time = datetime(2025, 1, 1, 10, 0, 0)
        request = self.env['spp.drims.request'].create({
            'incident_id': self.incident.id,
            'date_requested': request_time,
            'destination_area_id': self.ref('spp_area.area_province_1'),
        })

        # Create dispatch 6 hours later
        dispatch_time = request_time + timedelta(hours=6)
        picking = self.env['stock.picking'].create({
            'drims_request_id': request.id,
            'incident_id': self.incident.id,
            'date_departed': dispatch_time,
            'picking_type_id': self.ref('stock.picking_type_out'),
        })

        # Trigger computation
        self.incident._compute_avg_response_time()

        # Should be 6 hours
        self.assertAlmostEqual(self.incident.avg_request_response_hours, 6.0, places=1)

    def test_no_dispatches_returns_zero(self):
        """Test KPI returns 0 when no dispatches exist."""
        self.env['spp.drims.request'].create({
            'incident_id': self.incident.id,
            'destination_area_id': self.ref('spp_area.area_province_1'),
        })

        self.incident._compute_avg_response_time()

        self.assertEqual(self.incident.avg_request_response_hours, 0.0)
```

### Creating Country Modules

Country-specific modules extend DRIMS with localized data and workflows. Use `spp_drims_sl` (Sri Lanka) as a reference pattern.

**Module Structure:**

```
spp_drims_country/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── (custom model extensions)
├── data/
│   ├── spp_area_data.xml          # Country admin boundaries
│   ├── vocabulary_codes.xml        # Country-specific vocabularies
│   ├── res_partner_data.xml        # Government agencies, NGOs
│   └── stock_warehouse_data.xml    # Warehouse network
└── security/
    └── ir.model.access.csv
```

**Example: Create spp_drims_ke (Kenya)**

```python
# spp_drims_ke/__manifest__.py
{
    'name': 'DRIMS - Kenya Localization',
    'version': '19.0.1.0.0',
    'category': 'OpenSPP/DRIMS',
    'summary': 'Kenya-specific DRIMS configuration',
    'author': 'Your Organization',
    'depends': [
        'spp_drims',
        'spp_area',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/spp_area_data.xml',
        'data/vocabulary_codes.xml',
        'data/res_partner_data.xml',
        'data/stock_warehouse_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
```

**Area Hierarchy (Counties):**

```xml
<!-- spp_drims_ke/data/spp_area_data.xml -->
<odoo>
    <!-- Country Level -->
    <record id="area_kenya" model="spp.area">
        <field name="name">Kenya</field>
        <field name="code">KE</field>
        <field name="area_type_id" ref="spp_area.area_type_country"/>
    </record>

    <!-- Counties -->
    <record id="area_county_nairobi" model="spp.area">
        <field name="name">Nairobi County</field>
        <field name="code">KE-30</field>
        <field name="parent_id" ref="area_kenya"/>
        <field name="area_type_id" ref="area_type_county"/>
    </record>

    <record id="area_county_mombasa" model="spp.area">
        <field name="name">Mombasa County</field>
        <field name="code">KE-01</field>
        <field name="parent_id" ref="area_kenya"/>
        <field name="area_type_id" ref="area_type_county"/>
    </record>

    <!-- Sub-counties can be added here -->
</odoo>
```

**National Warehouse Network:**

```xml
<!-- spp_drims_ke/data/stock_warehouse_data.xml -->
<odoo>
    <record id="warehouse_national_nairobi" model="stock.warehouse">
        <field name="name">National Strategic Reserve - Nairobi</field>
        <field name="code">NSR-NRB</field>
        <field name="is_drims_warehouse">True</field>
        <field name="tier">central</field>
        <field name="area_id" ref="area_county_nairobi"/>
    </record>

    <record id="warehouse_county_mombasa" model="stock.warehouse">
        <field name="name">Mombasa County Warehouse</field>
        <field name="code">CW-MBA</field>
        <field name="is_drims_warehouse">True</field>
        <field name="tier">regional</field>
        <field name="area_id" ref="area_county_mombasa"/>
    </record>
</odoo>
```

**Government Agencies:**

```xml
<!-- spp_drims_ke/data/res_partner_data.xml -->
<odoo>
    <record id="partner_ndma" model="res.partner">
        <field name="name">National Drought Management Authority</field>
        <field name="is_company">True</field>
        <field name="is_drims_organization">True</field>
        <field name="drims_organization_role_id" ref="spp_drims.org_role_government"/>
    </record>

    <record id="partner_krcs" model="res.partner">
        <field name="name">Kenya Red Cross Society</field>
        <field name="is_company">True</field>
        <field name="is_drims_organization">True</field>
        <field name="drims_organization_role_id" ref="spp_drims.org_role_ngo"/>
    </record>
</odoo>
```

## Testing Extensions

### Unit Tests

Place tests in `tests/` directory with `test_` prefix:

```python
# my_custom_drims/tests/test_custom_feature.py

from odoo.tests import tagged
from odoo.tests.common import TransactionCase

@tagged('post_install', '-at_install')
class TestCustomFeature(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Set up test data once for all tests
        cls.incident = cls.env['spp.hazard.incident'].create({
            'name': 'Test Incident',
        })

    def test_feature_works(self):
        """Test your feature works as expected."""
        # Arrange
        # Act
        # Assert
        self.assertTrue(True)
```

### Running Tests

**Single module:**

```bash
./scripts/test_single_module.sh my_custom_drims
```

**Specific test class:**

```bash
odoo-bin -c config.conf -d test_db --test-enable --test-tags my_custom_drims.TestCustomFeature --stop-after-init
```

### Test Coverage

Aim for 85%+ coverage on custom code:

```bash
coverage run --source=addons/my_custom_drims odoo-bin -c config.conf -d test_db --test-enable --stop-after-init
coverage report
coverage html  # Open htmlcov/index.html
```

## See Also

- {doc}`architecture` - DRIMS data model and architecture reference
- {doc}`/developer_guide/api_v2/index` - API integration patterns
- {doc}`/config_guide/drims/index` - Configuration without code
- {gh-spp}`docs/principles/` - Module development guidelines

---
openspp:
  doc_status: draft
  products: [core]
---

# Audit Logging

This guide is for **sys admins** configuring audit trails and compliance logging for OpenSPP.

Audit logging tracks who accessed what data, when, and why. This is required for GDPR, donor compliance, and security monitoring.

## What Gets Audited

OpenSPP logs:

| Event Type | What's Logged | Use Case |
|------------|---------------|----------|
| PII Access | Field views, reveals | GDPR compliance |
| Data Changes | Create, update, delete | Change tracking |
| User Actions | Login, logout, role changes | Security monitoring |
| Sensitive Operations | Export, delete, anonymize | Compliance |
| System Events | Config changes, key rotation | System security |

## Audit Modules

| Module | What It Audits |
|--------|----------------|
| `spp_audit` | Model changes, CRUD operations |
| `spp_pii_encryption` | PII field access, masked field reveals |
| `spp_data_classification` | DSAR requests, consent changes |
| `base` (Odoo) | User logins, password changes |

## PII Access Logging

### How It Works

When a user reveals a masked PII field, it's logged:

```
User: jane.doe@example.org
Action: Reveal PII field
Model: res.partner
Record: BEN-12345
Field: national_id
Timestamp: 2025-01-15 14:23:45 UTC
IP: 10.0.1.42
```

### Checking PII Access Logs

Via Web UI:

Navigate to **Settings → Security → PII Access Logs**

Filter by:
- User
- Date range
- Model
- Access type (view, reveal, export)

Via Shell:

```bash
odoo-bin shell -d openspp_prod

# Recent PII access
logs = env['spp.pii.access.log'].search([], limit=50, order='create_date DESC')
for log in logs:
    print(f"{log.create_date} | {log.user_id.name} | {log.model}:{log.res_id} | {log.field_name}")

# Access by specific user
user = env['res.users'].search([('login', '=', 'jane.doe@example.org')])
user_logs = env['spp.pii.access.log'].search([('user_id', '=', user.id)])
print(f"User accessed PII {len(user_logs)} times")

# Access to specific beneficiary
partner_id = 123
partner_logs = env['spp.pii.access.log'].search([
    ('model', '=', 'res.partner'),
    ('res_id', '=', partner_id),
])
for log in partner_logs:
    print(f"{log.user_id.name} accessed {log.field_name} at {log.create_date}")
```

Via Database:

```sql
-- Recent PII access
SELECT
    pal.create_date,
    u.login as user,
    pal.model,
    pal.res_id,
    pal.field_name,
    pal.access_type,
    pal.ip_address
FROM spp_pii_access_log pal
JOIN res_users u ON u.id = pal.user_id
ORDER BY pal.create_date DESC
LIMIT 50;

-- Access by user in last 30 days
SELECT
    u.login,
    COUNT(*) as access_count,
    COUNT(DISTINCT pal.res_id) as unique_records
FROM spp_pii_access_log pal
JOIN res_users u ON u.id = pal.user_id
WHERE pal.create_date > NOW() - INTERVAL '30 days'
GROUP BY u.login
ORDER BY access_count DESC;
```

### Configuring PII Logging

Control what gets logged:

```bash
odoo-bin shell -d openspp_prod

# Get classification
classification = env['spp.field.classification'].search([
    ('model_id.model', '=', 'res.partner'),
    ('field_id.name', '=', 'national_id'),
])

# Enable audit logging
classification.classification_id.requires_audit = True
```

All fields with `requires_audit = True` log access automatically.

## Model Change Auditing

### Odoo Chatter (Built-in)

All OpenSPP models inherit mail tracking. Changes are logged in chatter:

```python
# Models with tracking
class Registrant(models.Model):
    _inherit = ['res.partner', 'mail.thread']

    # Tracked fields
    name = fields.Char(tracking=True)
    is_registrant = fields.Boolean(tracking=True)
```

View change history:

```bash
odoo-bin shell -d openspp_prod

partner = env['res.partner'].browse(123)
for message in partner.message_ids:
    if message.tracking_value_ids:
        print(f"{message.date} | {message.author_id.name}:")
        for tracking in message.tracking_value_ids:
            print(f"  {tracking.field_desc}: {tracking.old_value_char} → {tracking.new_value_char}")
```

### Enhanced Audit Module

For detailed audit trails beyond chatter:

```bash
# Install audit module
odoo-bin -d openspp_prod -i spp_audit --stop-after-init
```

Configure audit rules:

```bash
odoo-bin shell -d openspp_prod

# Create audit rule for registrants
rule = env['spp.audit.rule'].create({
    'name': 'Registrant Changes',
    'model_id': env.ref('base.model_res_partner').id,
    'log_create': True,
    'log_write': True,
    'log_unlink': True,
    'log_read': False,  # Too verbose
})

# Track specific fields only
rule.field_ids = env['ir.model.fields'].search([
    ('model_id', '=', rule.model_id.id),
    ('name', 'in', ['name', 'is_registrant', 'is_group', 'disabled']),
])
```

View audit logs:

```bash
# Recent changes
logs = env['spp.audit.log'].search([], limit=50, order='create_date DESC')
for log in logs:
    print(f"{log.create_date} | {log.user_id.name} | {log.method} | {log.model_id.model}:{log.res_id}")

# Changes to specific record
record_logs = env['spp.audit.log'].search([
    ('model_id.model', '=', 'res.partner'),
    ('res_id', '=', 123),
])
for log in record_logs:
    print(f"{log.create_date} | {log.method} | {log.user_id.name}")
    for line in log.line_ids:
        print(f"  {line.field_id.name}: {line.old_value} → {line.new_value}")
```

## User Activity Logging

### Login/Logout Tracking

Odoo logs authentication events:

```sql
-- Recent logins
SELECT
    l.create_date as login_time,
    u.login,
    l.ip,
    l.create_uid
FROM res_users_log l
JOIN res_users u ON u.id = l.create_uid
ORDER BY l.create_date DESC
LIMIT 50;

-- Failed login attempts
SELECT
    create_date,
    login,
    ip
FROM auth_attempt
WHERE success = false
ORDER BY create_date DESC;
```

### Session Tracking

```bash
odoo-bin shell -d openspp_prod

# Active sessions
sessions = env['ir.http'].session_store.list()
print(f"Active sessions: {len(sessions)}")

# Session details
for sid, session_data in sessions:
    print(f"Session {sid}: User {session_data.get('uid')}")
```

## DSAR (Data Subject Access Request) Audit

Track GDPR Article 15 requests:

```bash
odoo-bin shell -d openspp_prod

# List DSAR requests
requests = env['spp.dsar.request'].search([])
for req in requests:
    print(f"{req.create_date} | {req.partner_id.name} | {req.request_type} | {req.state}")

# DSAR activity for beneficiary
partner = env['res.partner'].browse(123)
partner_requests = env['spp.dsar.request'].search([('partner_id', '=', partner.id)])
print(f"Beneficiary has {len(partner_requests)} DSAR requests")
```

Via Database:

```sql
-- DSAR requests summary
SELECT
    request_type,
    state,
    COUNT(*) as count,
    AVG(EXTRACT(EPOCH FROM (completed_date - create_date))/86400) as avg_days_to_complete
FROM spp_dsar_request
WHERE completed_date IS NOT NULL
GROUP BY request_type, state;

-- Pending DSAR requests
SELECT
    dr.create_date,
    p.name as beneficiary,
    dr.request_type,
    dr.due_date,
    CASE
        WHEN dr.due_date < CURRENT_DATE THEN 'OVERDUE'
        ELSE 'PENDING'
    END as status
FROM spp_dsar_request dr
JOIN res_partner p ON p.id = dr.partner_id
WHERE dr.state IN ('submitted', 'verified', 'in_progress')
ORDER BY dr.due_date;
```

## Export and Reporting

### Export Audit Logs (CSV)

```bash
odoo-bin shell -d openspp_prod

import csv
from datetime import datetime, timedelta

# Export last 30 days of PII access
start_date = datetime.now() - timedelta(days=30)
logs = env['spp.pii.access.log'].search([
    ('create_date', '>=', start_date)
])

with open(f'/tmp/pii_access_{datetime.now():%Y%m%d}.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'User', 'Model', 'Record ID', 'Field', 'Action', 'IP'])
    for log in logs:
        writer.writerow([
            log.create_date,
            log.user_id.login,
            log.model,
            log.res_id,
            log.field_name,
            log.access_type,
            log.ip_address,
        ])
```

### Export Model Changes

```bash
# Export registrant changes
changes = env['spp.audit.log'].search([
    ('model_id.model', '=', 'res.partner'),
    ('create_date', '>=', start_date),
])

with open(f'/tmp/partner_changes_{datetime.now():%Y%m%d}.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'User', 'Action', 'Record ID', 'Field', 'Old Value', 'New Value'])
    for log in changes:
        for line in log.line_ids:
            writer.writerow([
                log.create_date,
                log.user_id.login,
                log.method,
                log.res_id,
                line.field_id.name,
                line.old_value,
                line.new_value,
            ])
```

### Compliance Reports

Generate monthly compliance reports:

```bash
odoo-bin shell -d openspp_prod

from datetime import datetime

# PII Access Summary
print("=== PII Access Summary ===")
logs = env['spp.pii.access.log'].search([])
print(f"Total PII accesses: {len(logs)}")

by_user = {}
for log in logs:
    by_user[log.user_id.login] = by_user.get(log.user_id.login, 0) + 1

print("\nAccess by user:")
for user, count in sorted(by_user.items(), key=lambda x: x[1], reverse=True):
    print(f"  {user}: {count}")

# DSAR Summary
print("\n=== DSAR Summary ===")
requests = env['spp.dsar.request'].search([])
print(f"Total DSAR requests: {len(requests)}")

by_type = {}
for req in requests:
    by_type[req.request_type] = by_type.get(req.request_type, 0) + 1

print("\nRequests by type:")
for req_type, count in by_type.items():
    print(f"  {req_type}: {count}")
```

## Retention Policies

Configure how long to keep audit logs:

```bash
odoo-bin shell -d openspp_prod

# Set retention for PII access logs
env['ir.config_parameter'].set_param('audit.pii_access_retention_days', '365')

# Set retention for model changes
env['ir.config_parameter'].set_param('audit.change_retention_days', '2555')  # 7 years

# Archive old logs
retention_days = int(env['ir.config_parameter'].get_param('audit.pii_access_retention_days'))
cutoff_date = datetime.now() - timedelta(days=retention_days)

old_logs = env['spp.pii.access.log'].search([('create_date', '<', cutoff_date)])
print(f"Archiving {len(old_logs)} old logs")
old_logs.write({'active': False})  # Archive, don't delete
```

## Automated Alerts

Set up alerts for suspicious activity:

### Alert: Excessive PII Access

```bash
# Daily job to check for excessive access
odoo-bin shell -d openspp_prod

from datetime import datetime, timedelta

# Check last 24 hours
start = datetime.now() - timedelta(hours=24)
logs = env['spp.pii.access.log'].search([('create_date', '>=', start)])

# Alert if user accessed > 100 records
by_user = {}
for log in logs:
    by_user[log.user_id] = by_user.get(log.user_id, set())
    by_user[log.user_id].add((log.model, log.res_id))

for user, records in by_user.items():
    if len(records) > 100:
        # Send alert
        env['mail.mail'].create({
            'subject': f'Alert: Excessive PII Access by {user.name}',
            'body_html': f'{user.name} accessed {len(records)} records in 24h',
            'email_to': 'security@example.org',
        }).send()
```

### Alert: After-Hours Access

```bash
# Alert for access outside business hours
from datetime import datetime

for log in env['spp.pii.access.log'].search([('create_date', '>=', start)]):
    hour = log.create_date.hour
    if hour < 6 or hour > 22:  # Outside 6am-10pm
        print(f"After-hours access: {log.user_id.name} at {log.create_date}")
```

## Log Storage and Performance

### Database Size

Check audit log table sizes:

```sql
SELECT
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE tablename LIKE '%audit%' OR tablename LIKE '%log%'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```

### Archiving Old Logs

```bash
# Export to archive before deleting
pg_dump openspp_prod \
    --table=spp_pii_access_log \
    --table=spp_audit_log \
    > /backup/audit_archive_$(date +%Y%m%d).sql

# Delete archived logs from database
psql openspp_prod -c "
DELETE FROM spp_pii_access_log
WHERE create_date < NOW() - INTERVAL '1 year';
"
```

### Separate Audit Database

For large deployments, use separate database for audits:

```ini
# /etc/odoo/odoo.conf
[audit]
db_name = openspp_audit
db_host = audit-db.example.com
db_port = 5432
db_user = odoo_audit
db_password = <password>
```

## SIEM Integration

Send audit logs to Security Information and Event Management (SIEM) systems:

### Syslog Export

```python
# In custom module
import syslog

class PIIAccessLog(models.Model):
    _inherit = 'spp.pii.access.log'

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            # Send to syslog
            syslog.syslog(
                syslog.LOG_INFO,
                f"PII_ACCESS user={record.user_id.login} "
                f"model={record.model} res_id={record.res_id} "
                f"field={record.field_name} ip={record.ip_address}"
            )
        return records
```

### JSON Export for Splunk/ELK

```bash
# Export logs as JSON for ingestion
odoo-bin shell -d openspp_prod

import json
from datetime import datetime, timedelta

start = datetime.now() - timedelta(hours=1)
logs = env['spp.pii.access.log'].search([('create_date', '>=', start)])

with open('/var/log/openspp/pii_access.json', 'a') as f:
    for log in logs:
        event = {
            'timestamp': log.create_date.isoformat(),
            'user': log.user_id.login,
            'model': log.model,
            'res_id': log.res_id,
            'field': log.field_name,
            'action': log.access_type,
            'ip': log.ip_address,
        }
        f.write(json.dumps(event) + '\n')
```

## Compliance Checklist

- [ ] PII access logging enabled
- [ ] All RESTRICTED fields configured with `requires_audit = True`
- [ ] Model change tracking enabled for key models
- [ ] DSAR request tracking active
- [ ] User login/logout logging verified
- [ ] Audit log retention policy defined
- [ ] Automated alerts configured
- [ ] Monthly compliance reports generated
- [ ] Logs exported to SIEM (if required)
- [ ] Audit log backups tested

## Troubleshooting

**PII access not being logged**

Check field classification:

```bash
odoo-bin shell -d openspp_prod
classification = env['spp.field.classification'].search([
    ('model_id.model', '=', 'res.partner'),
    ('field_id.name', '=', 'national_id'),
])
print(f"Requires audit: {classification.classification_id.requires_audit}")
```

**Audit logs growing too fast**

Check what's being logged:

```sql
-- Log volume by model
SELECT
    model,
    COUNT(*) as log_count,
    pg_size_pretty(SUM(pg_column_size(row(al.*)))) as size
FROM spp_audit_log al
GROUP BY model
ORDER BY log_count DESC;
```

Reduce logging:
- Disable `log_read` on high-volume models
- Increase retention cleanup frequency
- Archive old logs to separate database

**Missing change history in chatter**

Verify field has tracking enabled:

```bash
field = env['ir.model.fields'].search([
    ('model', '=', 'res.partner'),
    ('name', '=', 'name'),
])
print(f"Tracking: {field.tracking}")
```

## Related Documentation

- Access control: {doc}`access_control`
- Data classification: {doc}`data_classification`
- PII encryption: {doc}`pii_encryption`

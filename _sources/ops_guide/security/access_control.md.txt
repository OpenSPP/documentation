---
openspp:
  doc_status: draft
  products: [core]
---

# Access Control

This guide is for **sys admins** configuring user access to OpenSPP.

OpenSPP uses a three-tier Role-Based Access Control (RBAC) system. You assign users to groups that control what they can see and do.

## Architecture Overview

```
TIER 1: ROLES (Composite - Optional)
├── SPP Field Officer    → Registry + Change Request + Program viewing
├── SPP Program Officer  → Program management + Entitlements
└── SPP Supervisor       → All domains (manager level)

TIER 2: FUNCTIONAL PRIVILEGES (What Users See)
├── Registry
│   ├── Viewer    → Read only
│   ├── Officer   → Create and edit
│   └── Manager   → Full access + delete
├── Programs
│   ├── Viewer
│   ├── Officer
│   └── Manager
└── Other domains (GRM, Approvals, etc.)

TIER 3: BASE PERMISSIONS (Technical)
├── Registry: Read, Write, Create, Delete
├── Programs: Read, Write, Create
└── API: Read, Write
```

## Security Modules

OpenSPP's access control is split across modules:

| Module | What It Provides |
|--------|------------------|
| `spp_security` | Category hierarchy, admin group |
| `spp_registry_base` | Registry domain groups (always installed) |
| `spp_programs_base` | Program domain groups (if using programs) |
| `spp_grm` | GRM domain groups (if using case management) |
| `spp_roles` | Pre-built composite roles (optional) |

**Key principle:** Groups only exist when their domain module is installed. If you don't install programs, users won't see program privileges.

## Assigning User Access

### Via Web UI

1. Navigate to **Settings → Users & Companies → Users**
2. Select the user
3. Go to the **OpenSPP** tab
4. Enable privileges based on role:

| For This Role | Enable These Privileges |
|---------------|------------------------|
| Field Officer | Registry Officer, Change Request Agent, Programs Viewer |
| Data Entry Clerk | Registry Officer |
| Program Officer | Programs Officer, Registry Viewer |
| Supervisor | Registry Manager, Programs Manager, GRM Manager |
| System Admin | OpenSPP Administrator |

### Via Command Line

Create users with groups assigned:

```bash
# Using Odoo shell
odoo-bin shell -d openspp_prod -c /etc/odoo/odoo.conf

# In Python shell
user = env['res.users'].create({
    'name': 'Jane Doe',
    'login': 'jane.doe@example.org',
    'email': 'jane.doe@example.org',
    'groups_id': [(6, 0, [
        env.ref('spp_registry_base.group_registry_officer').id,
        env.ref('spp_change_request.group_cr_agent').id,
    ])]
})
```

### Via XML Data

```xml
<!-- In a custom module -->
<record id="user_field_officer_1" model="res.users">
    <field name="name">Field Officer</field>
    <field name="login">officer@example.org</field>
    <field name="groups_id" eval="[
        Command.link(ref('spp_registry_base.group_registry_officer')),
        Command.link(ref('spp_change_request.group_cr_agent')),
        Command.link(ref('spp_programs_base.group_program_viewer')),
    ]"/>
</record>
```

## Domain Groups Reference

### Registry Domain

Always available (core module).

| Group | Can Do | XML ID |
|-------|--------|--------|
| Viewer | View beneficiaries and groups | `spp_registry_base.group_registry_viewer` |
| Officer | Create and edit beneficiaries | `spp_registry_base.group_registry_officer` |
| Manager | Full access including delete | `spp_registry_base.group_registry_manager` |

### Programs Domain

Available when `spp_programs_base` installed.

| Group | Can Do | XML ID |
|-------|--------|--------|
| Viewer | View programs and cycles | `spp_programs_base.group_program_viewer` |
| Officer | Manage cycles and enrollment | `spp_programs_base.group_program_officer` |
| Manager | Full program configuration | `spp_programs_base.group_program_manager` |

### Change Request Domain

Available when `spp_change_request` installed.

| Group | Can Do | XML ID |
|-------|--------|--------|
| Agent | Submit change requests | `spp_change_request.group_cr_agent` |
| Validator | Review and approve CRs | `spp_change_request.group_cr_validator` |
| Admin | Full CR configuration | `spp_change_request.group_cr_admin` |

### GRM Domain

Available when `spp_grm` installed.

| Group | Can Do | XML ID |
|-------|--------|--------|
| Viewer | View cases/tickets | `spp_grm.group_grm_viewer` |
| Officer | Create and manage cases | `spp_grm.group_grm_officer` |
| Manager | Full GRM access | `spp_grm.group_grm_manager` |

### API Access

Available when API modules installed.

| Group | Can Do | XML ID |
|-------|--------|--------|
| Read | GET requests only | `spp_api.group_api_read` |
| Write | POST, PUT, DELETE | `spp_api.group_api_write` |

**Note:** API users need BOTH api access AND functional domain access (e.g., `group_api_read` + `group_registry_viewer`).

## Administrative Access

| Group | Purpose | XML ID |
|-------|---------|--------|
| OpenSPP Administrator | Full system access | `spp_security.group_spp_admin` |
| Odoo System | Technical settings | `base.group_system` |

**Warning:** OpenSPP Admin gets all OpenSPP groups automatically. Only assign to trusted users.

## Checking User Permissions

### From Shell

```bash
# Check user's groups
odoo-bin shell -d openspp_prod

user = env['res.users'].search([('login', '=', 'jane.doe@example.org')])
for group in user.groups_id:
    print(f"  - {group.full_name}")

# Check if user has specific group
user.has_group('spp_registry_base.group_registry_officer')  # True/False
```

### From Database

```sql
-- List user's groups
SELECT u.login, g.name
FROM res_users u
JOIN res_groups_users_rel r ON r.uid = u.id
JOIN res_groups g ON g.id = r.gid
WHERE u.login = 'jane.doe@example.org'
ORDER BY g.name;

-- Count users per group
SELECT g.name, COUNT(r.uid) as user_count
FROM res_groups g
LEFT JOIN res_groups_users_rel r ON r.gid = g.id
WHERE g.name LIKE 'SPP%' OR g.name LIKE '%Registry%'
GROUP BY g.name
ORDER BY user_count DESC;
```

## Record Rules (Row-Level Security)

Record rules filter which records users can see.

### Multi-Company Rule

Users only see records from their company:

```python
# Automatically applied to most models
domain: [
    '|',
    ('company_id', '=', False),
    ('company_id', 'in', company_ids)
]
```

### Own Records Only

Change Request agents only see their own requests:

```python
# Applied to CR agents
domain: [('created_by', '=', user.id)]
```

### Role-Based Visibility

CR validators see all requests:

```python
# Applied to CR validators
domain: [(1, '=', 1)]  # See all
```

## Auditing Access Changes

All group changes are logged via Odoo's chatter:

```bash
# View group assignment history
odoo-bin shell -d openspp_prod

user = env['res.users'].search([('login', '=', 'jane.doe@example.org')])
for message in user.message_ids.filtered(lambda m: 'groups_id' in m.body):
    print(f"{message.date}: {message.body}")
```

## Troubleshooting

**User can't see menu item**

Check privilege assignment:

```bash
user = env['res.users'].search([('login', '=', 'user@example.org')])
print("Groups:", [g.name for g in user.groups_id])

# Menu requires this group:
menu = env.ref('spp_registry_base.menu_registry')
print("Menu groups:", [g.name for g in menu.groups_id])
```

**User can't access specific model**

Check ACL (Access Control List):

```bash
# Find ACL entries for model
acls = env['ir.model.access'].search([
    ('model_id.model', '=', 'res.partner')
])
for acl in acls:
    print(f"{acl.name}: {acl.group_id.name} - Read:{acl.perm_read} Write:{acl.perm_write}")
```

**User sees records they shouldn't**

Check record rules:

```bash
# Find rules for model
rules = env['ir.rule'].search([
    ('model_id.model', '=', 'spp.change.request')
])
for rule in rules:
    print(f"{rule.name}:")
    print(f"  Groups: {[g.name for g in rule.groups]}")
    print(f"  Domain: {rule.domain_force}")
```

## Security Checklist

Before production deployment:

- [ ] All users assigned to appropriate groups
- [ ] No users with System Admin unless necessary
- [ ] Multi-company rules enabled
- [ ] Record rules tested for each role
- [ ] API users have limited scope
- [ ] Group assignments logged and audited
- [ ] Test users can only see their own company data
- [ ] Field-level security configured (see {doc}`data_classification`)

## Related Documentation

- Data classification and field-level security: {doc}`data_classification`
- Audit logging: {doc}`audit`
- Full access rights spec: See `openspp-modules-v2/docs/specs/access-rights/`

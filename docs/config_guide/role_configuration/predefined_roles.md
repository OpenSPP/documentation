---
openspp:
  doc_status: draft
  products: [core]
---

# Predefined roles

This guide is for **implementers** understanding the default roles included with OpenSPP.

## Global roles

Global roles provide system-wide access without area restrictions.

| Role | Description | Key permissions |
|------|-------------|-----------------|
| **System Admin** | Full system access | All system data and features |
| **Registry Viewer** | Read-only registry access | View registrants (no edit) |
| **Global Finance** | Financial data access | Finance data across all areas |
| **Global Program Manager** | Program coordination | All area-specific data for program management |
| **Global Registrar** | Registry data entry | Create and edit registrants across all areas |
| **Global Support** | Support request handling | View and respond to support requests |
| **Global Support Manager** | Support oversight | Manage all support requests and activities |

### System Admin

The most privileged role with universal access:

- Full system configuration
- User and role management
- All registry and program data
- All security settings

**Implied groups:**
- `base.group_user` (Internal User)
- `base.group_system` (System Configuration)
- `base.group_partner_manager` (Contact Manager)
- `spp_security.group_spp_admin` (SPP Administrator)

### Registry Viewer

Read-only access for monitoring and reporting:

- View all registry records
- Cannot create or edit registrants
- Useful for auditors and report viewers

**Implied groups:**
- `base.group_user` (Internal User)
- `spp_registry.group_registry_viewer` (Registry Viewer)

### Global Registrar

Data entry role for registration staff:

- Create new registrants
- Edit existing registrant data
- Access across all geographic areas

**Implied groups:**
- `base.group_user` (Internal User)
- `spp_registry.group_registry_officer` (Registry Officer)

### Global Finance

Financial operations access:

- Access to financial data
- Payment processing visibility
- Cross-area financial reporting

**Implied groups:**
- `base.group_user` (Internal User)

### Global Program Manager

Program coordination and oversight:

- Access to all program data
- Cross-area program management
- Enrollment and benefit visibility

**Implied groups:**
- `base.group_user` (Internal User)

### Global Support

Support request handling:

- View and respond to support requests
- Access support ticket system
- Cross-area support visibility

**Implied groups:**
- `base.group_user` (Internal User)

### Global Support Manager

Support team oversight:

- Manage all support activities
- Supervise support staff
- Cross-area support management

**Implied groups:**
- `base.group_user` (Internal User)

## Local roles

Local roles restrict access to specific geographic areas.

| Role | Description | Key permissions |
|------|-------------|-----------------|
| **Local Registrar** | Area-restricted data entry | Create and edit registrants in assigned areas only |
| **Local Support** | Area-restricted support | Support requests in assigned areas only |

### Local Registrar

Same capabilities as Global Registrar, but limited to assigned areas:

- Create and edit registrants
- Only sees records in assigned Center Areas
- Ideal for field staff

**Implied groups:**
- `base.group_user` (Internal User)
- `spp_registry.group_registry_officer` (Registry Officer)

**Required:** Must assign at least one Center Area when assigning this role.

### Local Support

Same capabilities as Global Support, but limited to assigned areas:

- View and respond to support requests
- Only sees tickets from assigned areas
- Ideal for regional support teams

**Implied groups:**
- `base.group_user` (Internal User)

**Required:** Must assign at least one Center Area when assigning this role.

## Role comparison

| Role | Type | Registry | Finance | Programs | Support |
|------|------|----------|---------|----------|---------|
| System Admin | Global | Full | Full | Full | Full |
| Registry Viewer | Global | Read | - | - | - |
| Global Finance | Global | - | Full | - | - |
| Global Program Manager | Global | Read | - | Full | - |
| Global Registrar | Global | Full | - | - | - |
| Global Support | Global | - | - | - | Full |
| Global Support Manager | Global | - | - | - | Full |
| Local Registrar | Local | Full* | - | - | - |
| Local Support | Local | - | - | - | Full* |

*Limited to assigned areas

## Viewing role details

To see the complete permission set for any role:

1. Go to **Settings → Users & Companies → Roles**
2. Click on a role
3. View the **Groups** tab for implied groups
4. Click **Access Rights** button to see ACL permissions
5. Click **Record Rules** button to see domain restrictions

## See also

- {doc}`overview` - Understanding role architecture
- {doc}`assigning_roles` - How to assign roles
- {doc}`creating_roles` - Create custom roles

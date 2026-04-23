---
openspp:
  doc_status: draft
  products: [core]
---

# Security

**For: developers**

OpenSPP uses a three-tier group architecture for access control. This is the most important OpenSPP-specific pattern to understand — it differs significantly from typical Odoo module security.

## The three-tier group architecture

Every OpenSPP module defines security groups in three tiers:

### Tier 3 — Technical groups

These are internal groups used only in ACL (`ir.model.access.csv`) definitions. Users never see them. They represent individual CRUD permissions:

```xml
<!-- security/groups.xml -->
<record id="group_myfeature_read" model="res.groups">
    <field name="name">My Feature: Read</field>
    <field name="comment">Technical group for read access.</field>
</record>

<record id="group_myfeature_write" model="res.groups">
    <field name="name">My Feature: Write</field>
    <field name="comment">Technical group for write access.</field>
    <field name="implied_ids" eval="[Command.link(ref('group_myfeature_read'))]" />
</record>

<record id="group_myfeature_create" model="res.groups">
    <field name="name">My Feature: Create</field>
    <field name="comment">Technical group for create access.</field>
    <field name="implied_ids" eval="[Command.link(ref('group_myfeature_read'))]" />
</record>
```

Note the inheritance chain: both `write` and `create` are siblings that each imply `read`. The user-facing (Tier 2) groups explicitly compose the technical groups they need (e.g., an Officer gets both `create` and `write` via the Tier 2 record).

### Tier 2 — User-facing groups

These are the groups that administrators assign to users. Each is linked to a `res.groups.privilege` record (an Odoo 17+ feature) and composed from Tier 3 technical groups.

```{note}
By convention, OpenSPP modules split security records across two files: `security/privileges.xml` (the `res.groups.privilege` records) and `security/groups.xml` (the `res.groups` and admin linkage). `privileges.xml` is loaded **before** `groups.xml` so the groups can reference the privileges. Make sure your `__manifest__.py` lists them in that order.
```

```{note}
Pick a domain-specific category (from `spp_security`) rather than `category_spp_admin`. Examples: `category_spp_registry`, `category_spp_programs`, `category_spp_grm`. The category controls where your groups appear in the user permissions UI — putting everything under Administration buries them. See `spp_security/README.rst` for the full list.
```

```xml
<!-- security/privileges.xml -->
<record id="privilege_myfeature_viewer" model="res.groups.privilege">
    <field name="name">Viewer</field>
    <field name="category_id" ref="spp_security.category_spp_registry" />
    <field name="sequence">200</field>
</record>

<record id="group_myfeature_viewer" model="res.groups">
    <field name="name">My Feature Viewer</field>
    <field name="privilege_id" ref="privilege_myfeature_viewer" />
    <field name="comment">Can view but not modify.</field>
    <field name="implied_ids" eval="[Command.link(ref('group_myfeature_read'))]" />
</record>

<!-- Officer: read + write + create -->
<record id="privilege_myfeature_officer" model="res.groups.privilege">
    <field name="name">Officer</field>
    <field name="category_id" ref="spp_security.category_spp_registry" />
    <field name="sequence">210</field>
</record>

<record id="group_myfeature_officer" model="res.groups">
    <field name="name">My Feature Officer</field>
    <field name="privilege_id" ref="privilege_myfeature_officer" />
    <field name="comment">Can create and modify records.</field>
    <field name="implied_ids" eval="[
        Command.link(ref('group_myfeature_read')),
        Command.link(ref('group_myfeature_write')),
        Command.link(ref('group_myfeature_create')),
    ]" />
</record>

<!-- Manager: full CRUD including delete -->
<record id="privilege_myfeature_manager" model="res.groups.privilege">
    <field name="name">Manager</field>
    <field name="category_id" ref="spp_security.category_spp_registry" />
    <field name="sequence">220</field>
</record>

<record id="group_myfeature_manager" model="res.groups">
    <field name="name">My Feature Manager</field>
    <field name="privilege_id" ref="privilege_myfeature_manager" />
    <field name="comment">Full access including delete and configuration.</field>
    <field name="implied_ids" eval="[Command.link(ref('group_myfeature_officer'))]" />
</record>
```

### Tier 1 — Admin linkage

The SPP admin group automatically gets full access to your module:

```xml
<!-- Link Manager to SPP Admin -->
<record id="spp_security.group_spp_admin" model="res.groups">
    <field name="implied_ids" eval="[Command.link(ref('group_myfeature_manager'))]" />
</record>
```

### The complete inheritance chain

```
spp_security.group_spp_admin
    └── group_myfeature_manager (Tier 2: full CRUD)
            └── group_myfeature_officer (Tier 2: read + write + create)
            │       ├── group_myfeature_read   (Tier 3)
            │       ├── group_myfeature_write  (Tier 3) → implies read
            │       └── group_myfeature_create (Tier 3) → implies read
            └── group_myfeature_viewer (Tier 2: read only)
                    └── group_myfeature_read   (Tier 3)
```

Tier 3 groups `write` and `create` are **siblings** — both imply `read` directly. They do not imply each other. Tier 2 user-facing groups compose whichever Tier 3 groups they need.

## Model access rules (ACL)

The `security/ir.model.access.csv` file maps groups to CRUD permissions on each model:

```text
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_spp_my_feature_system,System Admin,model_spp_my_feature,base.group_system,1,1,1,1
access_spp_my_feature_spp_admin,SPP Admin,model_spp_my_feature,spp_security.group_spp_admin,1,1,1,1
access_spp_my_feature_read,Read,model_spp_my_feature,group_myfeature_read,1,0,0,0
access_spp_my_feature_write,Write,model_spp_my_feature,group_myfeature_write,1,1,0,0
access_spp_my_feature_create,Create,model_spp_my_feature,group_myfeature_create,1,1,1,0
access_spp_my_feature_manager,Manager,model_spp_my_feature,group_myfeature_manager,1,1,1,1
```

### ACL naming convention

The `id` column follows this pattern: `access_{model_name}_{group_suffix}`

- `model_spp_my_feature` — dots in the model name are replaced with underscores
- Always include rows for `base.group_system` and `spp_security.group_spp_admin`

### ACL file is mandatory

The `openspp-check-acl` pre-commit hook verifies that every installable module has a `security/ir.model.access.csv` file.

## Record rules

Record rules filter which records a user can access. The most common pattern is multi-company isolation:

```xml
<!-- security/rules.xml -->
<?xml version="1.0" encoding="utf-8" ?>
<odoo noupdate="1">
    <record id="rule_my_feature_multi_company" model="ir.rule">
        <field name="name">My Feature: Multi-Company</field>
        <field name="model_id" ref="model_spp_my_feature" />
        <field name="domain_force">[
            '|',
            ('company_id', '=', False),
            ('company_id', 'in', company_ids)
        ]</field>
        <field name="global" eval="True" />
    </record>
</odoo>
```

Key points:

- Use `noupdate="1"` so the rules aren't overwritten on module upgrade
- `global="True"` means the rule applies to all users (not group-specific)
- The `company_ids` variable represents the user's allowed companies
- Always include the `('company_id', '=', False)` fallback for records without a company

## XML ID naming conventions

The pre-commit hook `openspp-check-xml-ids` enforces these patterns:

| Type         | Pattern                      | Example                         |
| ------------ | ---------------------------- | ------------------------------- |
| Groups       | `group_{domain}_{level}`     | `group_myfeature_viewer`        |
| Privileges   | `privilege_{domain}_{level}` | `privilege_myfeature_manager`   |
| Record rules | `rule_{model}_{purpose}`     | `rule_my_feature_multi_company` |
| ACL IDs      | `access_{model}_{group}`     | `access_spp_my_feature_read`    |

## Menu visibility

Use the `groups` attribute on menu items to control visibility:

```xml
<menuitem
    id="menu_spp_my_feature"
    name="My Feature"
    parent="menu_spp_my_feature_root"
    action="action_spp_my_feature"
    groups="group_myfeature_viewer"
/>
```

Using the viewer group ensures anyone with viewer, officer, or manager access can see the menu (since officer and manager inherit from viewer).

## Compliance check

Each OpenSPP module ships a `security/compliance.yaml` that declares the security posture of the module (which models are secured, which audit logs are produced, etc.). The `openspp-compliance-check` pre-commit hook validates modules against it. New custom modules should include a minimal `compliance.yaml` — see an existing module's copy for the format.

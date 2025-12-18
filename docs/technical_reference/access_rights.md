---
openspp:
  doc_status: unverified
---

# Access rights and roles

OpenSPP builds on Odoo 19’s security model (users, groups, ACLs, record rules) and standardizes how OpenSPP modules define and expose permissions.

## Key concepts (Odoo 19 + OpenSPP)

**Groups** (`res.groups`) grant permissions through:

- **ACLs** (`ir.model.access.csv`) which control CRUD permissions per model
- **Record rules** (`ir.rule`) which filter which records a user can see or modify

**Privileges** (`res.groups.privilege`) are an Odoo 19 feature used to organize groups in the Settings UI. In OpenSPP, domain modules define privileges so administrators see a consistent “Viewer / Officer / Manager …” choice per domain.

**Roles** (`res.users.role`) are a convenient way to assign a bundle of groups to a user. A role implies one or more groups; users receive the union of all groups implied by their enabled roles.

## OpenSPP’s three-tier structure

OpenSPP modules follow a three-tier access model:

- **Tier 1 — Roles (optional):** cross-domain bundles (for example “Field Officer”)
- **Tier 2 — Functional privileges:** user-facing levels per domain (for example “Registry: Officer”)
- **Tier 3 — Base permissions:** technical/granular groups (read/write/create…) used to build Tier 2 groups

This structure keeps permissions modular: a group only exists when its domain module is installed, and administrators configure access using consistent privilege levels.

## Administrator workflows

- Prefer assigning access through **Roles** on the user form (rather than editing user groups directly).
- If your deployment uses **local roles**, roles can be scoped by **Center Areas** (from the Areas module). Domain modules can use the user’s computed center areas in record rules to restrict visibility.
- If menus do not appear right after changing roles/groups, ask the user to **log out and log back in** (menu visibility is cached at login).

For step-by-step UI guidance, see {doc}`../tutorial/access_management`.

## Implementer and developer guidelines

OpenSPP security definitions are intended to be implemented in modules (XML/CSV) and reviewed like code.

### Principles

- **Least privilege:** grant only what is required for the job.
- **Explicit configuration:** define privileges, groups, ACLs, and record rules explicitly (don’t rely on defaults).
- **Domain isolation:** each functional domain owns its group hierarchy and record rules.
- **Extend, don’t override:** modules should extend security definitions rather than modifying core ones.

### Record rule requirements

When defining `ir.rule` entries:

- Do not use an **empty domain** (`[]`) together with write/create/unlink permissions.
- Always scope rules with **groups** or mark them explicitly as **global**.
- When a role needs “see all” behavior, use an explicit always-true domain (for example `[(1, '=', 1)]`) rather than `[]`.
- Wrap record rule definitions in a `<data noupdate="1">` block.
- For multi-company models, add company isolation rules.

### Naming conventions (recommended)

- Privilege: `privilege_{domain}_{level}`
- Tier 2 group: `group_{domain}_{level}`
- Tier 3 group: `group_{domain}_{action}`
- ACL entry id: `access_{model}_{group}`
- Record rule id: `rule_{model}_{purpose}`

## Access-control “linters” and compliance checks

OpenSPP includes tooling to validate access control definitions and prevent common security mistakes.

### Declarative specs (`security/compliance.yaml`)

Modules can declare expected access control in `security/compliance.yaml` (groups, ACL expectations, record rules, menu restrictions, action restrictions). This is used for automated validation.

### Static checker

Run the compliance checker from the OpenSPP modules repository root:

```bash
# Check a single module
python -m scripts.compliance.checker spp_registry

# Check all modules that declare compliance.yaml
python -m scripts.compliance.checker --all
```

### Generated runtime tests

The test generator can create runtime tests from `security/compliance.yaml` to validate behavior in an Odoo test environment:

```bash
python -m scripts.compliance.test_generator spp_registry
```

### Quick security audit script

For a fast, repository-wide audit of common pitfalls, OpenSPP also provides a shell audit script:

```bash
./scripts/audit-security.sh
```


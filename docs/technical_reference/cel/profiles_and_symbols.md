---
openspp:
  doc_status: unverified
---

# Profiles and symbols

CEL “profiles” define what data is available to an expression in a given context: the root model (“current record”), related collections (members/enrollments/entitlements/events…), and available helper functions.

Profiles are loaded by the CEL registry and can be extended by modules.

```{seealso}
If you want to understand how a specific OpenSPP feature uses CEL (which profile it uses, and whether it compiles to a domain or evaluates at runtime), see {doc}`usage_by_feature`.
```

## Default profiles (core)

The CEL service exposes these profiles by default:

- `registry_individuals` (root model: `res.partner` for individual registrants)
- `registry_groups` (root model: `res.partner` for group/household registrants)
- `program_memberships` (root model: `spp.program.membership`)
- `entitlements` (root model: `spp.entitlement`)
- `grm_tickets` (root model: `spp.grm.ticket`)

## Symbols you can use

### Root record

Most profiles include a root record symbol. In OpenSPP you may see either of these used in examples:

- `me`: current record (preferred in newer screens)
- `r`: current record (often used in older help texts)

Both may be available depending on how profiles are merged in your deployment.

### Registry profiles

**Individuals (`registry_individuals`)**

- `me` / `r`: the registrant (`res.partner`)
- `groups`: group memberships for the individual (via `spp.group.membership`)
- `enrollments`: program memberships (`spp.program.membership`)
- `entitlements`: entitlements (`spp.entitlement`)

**Groups/households (`registry_groups`)**

- `me` / `r`: the group registrant (`res.partner`)
- `members`: household members (via `spp.group.membership`)
- `enrollments`: program memberships (`spp.program.membership`)
- `entitlements`: entitlements (`spp.entitlement`)

### Event data (when installed)

If the event/CEL integration is installed, the registry profiles are extended with:

- `events`: the registrant’s event records (`spp.event.data`)
- event helper functions like `event(...)`, `has_event(...)`, `events_count(...)`, `events_sum(...)`, …

See {doc}`events`.

## Discovering profiles and symbols (in the UI)

Most CEL-enabled configuration screens use the CEL editor widget. It can show:

- the list of **available profiles**
- the **symbols** and their fields for the selected profile
- built-in and registered functions

This information is also exposed via JSON-RPC endpoints used by the widget (`/spp_cel/profiles`, `/spp_cel/symbols/<profile>`). See {doc}`widget_and_validation`.

## Where profiles come from (and how modules extend them)

Profiles are assembled from multiple sources (highest priority first):

1. System parameters (deployment overrides)
2. `data/cel_profiles.yaml` shipped by modules (extensions)
3. Defaults in the CEL registry (fallback)

In core, OpenSPP also ships a template YAML file that defines the common registry symbols and “me” conventions.

```{note}
Developer reference (source code):
- Profile registry and merge logic: `openspp-modules-v2/spp_cel_domain/models/cel_registry.py`
- Default profile template: `openspp-modules-v2/spp_cel_domain/data/cel_symbols.template.yaml`
- Event profile extension: `openspp-modules-v2/spp_cel_event/data/cel_profiles.yaml`
```

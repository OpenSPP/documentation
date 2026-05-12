---
openspp:
  doc_status: draft
  products: [core]
---

# Studio

**For: developers**

OpenSPP Studio is the no-code configuration layer — custom fields, business logic, change request types, and event types designed by administrators through wizards instead of code. This page covers what Studio is, the pattern for making your own models Studio-aware, and the extension points available to developers.

## How to use this section

1. Read the first few sections to understand what Studio is and what the four modules provide
2. Read **Making a model Studio-aware** if you're building a new configurable feature
3. Read **Custom fields**, **Logic packs**, **CR builder**, or **Event designer** for the specific feature area you're extending
4. See {doc}`/developer_guide/api_v2/studio_integration` for exposing Studio configurations over API V2

## Prerequisites

- Familiarity with Odoo models, views, and the `TransientModel` (wizard) pattern
- Understanding of `ir.model.fields` and `ir.ui.view` — Studio creates these records dynamically
- For logic work: familiarity with {doc}`/developer_guide/cel/index`

## What Studio is

Studio has two faces:

**For end users** — an in-browser configuration UI that lets administrators:

- Add custom fields to `res.partner` and related registry models without writing code
- Define business logic (eligibility, scoring, validation) using CEL expressions with visual testing
- Build change request types by selecting which registrant fields can be modified
- Design event types for data collection (surveys, assessments, visits)
- Install pre-built **logic packs** (bundled sets of variables and expressions for common program types)

**For developers** — a pattern built around a single mixin (`spp.studio.mixin`) that provides a consistent `draft → active → inactive` lifecycle with audit tracking and lifecycle hooks. Studio-created configurations are stored as Odoo records (not JSON blobs), so they participate in the usual ORM, security, and audit systems.

## The Studio modules

| Module | Purpose |
|--------|---------|
| `spp_studio` | Core — the `spp.studio.mixin` lifecycle, custom fields, business logic (extends `spp.cel.expression` and `spp.cel.variable`), placement zones, logic packs, wizards |
| `spp_studio_change_requests` | Wizard to build change request types without code — generates an `spp.change.request.type` record plus a dynamic detail model |
| `spp_studio_events` | Wizard to design event types for data collection — generates an `spp.event.type` record with field groups and templates |
| `spp_studio_api_v2` | Bridge that exposes activated Studio fields and variables through the API V2 `/Studio/*` endpoints (see {doc}`/developer_guide/api_v2/studio_integration`) |

All four modules depend on `spp_studio` and auto-install when their domain companion (`spp_change_request_v2`, `spp_event_data`, `spp_api_v2`) is present.

## Making a model Studio-aware

The core pattern is inheriting `spp.studio.mixin` and implementing lifecycle hooks. There is **no registry** to write to — just ORM records with a shared lifecycle.

### The mixin

`spp.studio.mixin` (`spp_studio/models/studio_mixin.py`) provides:

- `state` — selection of `draft`, `active`, `inactive`
- `created_by_id`, `activated_by_id`, `deactivated_by_id` — audit fields populated automatically
- `activated_date`, `deactivated_date` — timestamps
- `program_ids` — optional Many2many to `spp.program` for scoping a configuration to specific programs
- Action methods: `action_activate()`, `action_deactivate()`, `action_reactivate()`, `action_set_draft()`
- Override hooks: `_pre_activate()`, `_post_activate()`, `_pre_deactivate()`, `_post_deactivate()`, `_get_deactivation_impact()`, `_get_studio_config_type()`

### Example: a custom Studio-aware model

```python
from odoo import fields, models


class ProgramPolicy(models.Model):
    _name = "myorg.program.policy"
    _inherit = ["spp.studio.mixin", "mail.thread"]
    _description = "Custom program policy"

    name = fields.Char(required=True)
    program_id = fields.Many2one("spp.program", required=True)
    threshold = fields.Float()

    def _pre_activate(self):
        """Validate before going live."""
        for rec in self:
            if not rec.threshold:
                raise UserError(_("Set a threshold before activating."))

    def _post_activate(self):
        """Side effects after activation."""
        self.env["myorg.rule.registry"].register_policy(self)

    def _pre_deactivate(self):
        """Check for dependencies before deactivating."""
        # Called before the record moves to 'inactive'.

    def _get_deactivation_impact(self):
        """Return a human-readable string describing impact, or None.

        The deactivation wizard renders this string in its confirmation
        dialog. Return None (or an empty string) if there is no impact.
        """
        affected = self.env["myorg.thing"].search_count([
            ("policy_id", "=", self.id),
        ])
        if not affected:
            return None
        return _(
            "This policy is used by %d active records. "
            "Deactivating it will disable the dependent rules.",
            affected,
        )
```

### Lifecycle hooks

| Hook | Called | Purpose |
|------|--------|---------|
| `_pre_activate()` | Before state transitions to `active` | Validate; raise `UserError` to abort |
| `_post_activate()` | After state transitions to `active` | Side effects (create dependent records, register, etc.) |
| `_pre_deactivate()` | Before state transitions to `inactive` | Validate |
| `_post_deactivate()` | After state transitions to `inactive` | Cleanup (hide views, unregister, etc.) |
| `_get_deactivation_impact()` | When showing the deactivation confirmation dialog | Return a human-readable string (or `None`) describing what will be affected |
| `_get_studio_config_type()` | In UI and audit logs | Return the human-readable category name |

Hooks are synchronous — they run inside the transaction that triggered the state change. If `_pre_activate()` raises, the state change rolls back.

All action methods (`action_activate`, `action_deactivate`, `action_reactivate`, `action_set_draft`) use `ensure_one()` — they must be called on a single record, not a recordset. Calling `action_deactivate` while already in `draft` state raises a `UserError` (not a no-op) — the mixin treats this as a user error because the admin probably meant to delete the draft, not deactivate it.

On every state change, the mixin also writes an audit log entry via `_create_audit_log()` (integrated with `spp_audit`), so who activated/deactivated what and when is queryable without you doing anything.

### Form view for a Studio-aware model

Studio configurations need a form view with the lifecycle buttons and a statusbar. The pattern matches the one used by `spp.studio.field` itself. Replace `myorg.program.policy` and `myorg.group_policy_manager` with your own:

```xml
<record id="view_program_policy_form" model="ir.ui.view">
    <field name="name">myorg.program.policy.form</field>
    <field name="model">myorg.program.policy</field>
    <field name="arch" type="xml">
        <form string="Program Policy">
            <header>
                <button
                    name="action_activate"
                    string="Activate"
                    type="object"
                    class="btn-primary"
                    invisible="state != 'draft'"
                    groups="myorg.group_policy_manager"
                />
                <button
                    name="action_deactivate"
                    string="Deactivate"
                    type="object"
                    class="btn-warning"
                    invisible="state != 'active'"
                    groups="myorg.group_policy_manager"
                />
                <button
                    name="action_reactivate"
                    string="Reactivate"
                    type="object"
                    class="btn-primary"
                    invisible="state != 'inactive'"
                    groups="myorg.group_policy_manager"
                />
                <button
                    name="action_set_draft"
                    string="Set to Draft"
                    type="object"
                    class="btn-secondary"
                    invisible="state != 'inactive'"
                    groups="myorg.group_policy_manager"
                />
                <field
                    name="state"
                    widget="statusbar"
                    statusbar_visible="draft,active,inactive"
                />
            </header>
            <sheet>
                <group>
                    <field name="name" readonly="state != 'draft'" />
                    <field name="program_id" readonly="state != 'draft'" />
                    <field name="threshold" readonly="state != 'draft'" />
                </group>
            </sheet>
            <chatter />
        </form>
    </record>
</record>
```

**Key patterns to notice:**

- The four lifecycle buttons map 1-to-1 to the mixin's action methods (`action_activate`, `action_deactivate`, `action_reactivate`, `action_set_draft`) and each has a state-specific `invisible` condition.
- `statusbar_visible="draft,active,inactive"` shows all three states on the bar so users see their position in the lifecycle.
- Data fields use `readonly="state != 'draft'"` so the record becomes read-only once activated. This is a convention — enforce it in form views, not via Python constraints, so administrators can still correct data after reverting to `draft` via `action_set_draft`.
- `action_deactivate()` may open the deactivation-confirmation wizard if `_get_deactivation_impact()` returns a non-empty string. The wizard renders the string and asks for confirmation before completing the state change.

### Testing a Studio-aware model

Three kinds of tests cover the lifecycle safely: hook validation, state transitions, and deactivation impact.

```python
"""Tests for the Studio-aware ProgramPolicy model."""

from odoo.exceptions import UserError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestProgramPolicyLifecycle(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Policy = cls.env["myorg.program.policy"]
        cls.program = cls.env["spp.program"].create({"name": "Test Program"})

    def _make_policy(self, **overrides):
        vals = {
            "name": "Test Policy",
            "program_id": self.program.id,
            "threshold": 100.0,
        }
        vals.update(overrides)
        return self.Policy.create(vals)

    # --- Hook validation ---

    def test_pre_activate_blocks_without_threshold(self):
        """_pre_activate() raises UserError if threshold is missing."""
        policy = self._make_policy(threshold=0.0)
        with self.assertRaises(UserError):
            policy.action_activate()
        self.assertEqual(policy.state, "draft")

    # --- State transitions ---

    def test_activation_flow(self):
        """draft → active → inactive → active (via reactivate)."""
        policy = self._make_policy()
        self.assertEqual(policy.state, "draft")

        policy.action_activate()
        self.assertEqual(policy.state, "active")
        self.assertTrue(policy.activated_date)
        self.assertEqual(policy.activated_by_id, self.env.user)

        # Deactivate may return an action if _get_deactivation_impact() is
        # truthy; in that case we'd open the wizard. For a policy with no
        # dependent records, deactivation completes directly.
        policy.action_deactivate()
        self.assertEqual(policy.state, "inactive")

        policy.action_reactivate()
        self.assertEqual(policy.state, "active")

    def test_set_draft_from_inactive(self):
        """An inactive policy can be returned to draft for editing."""
        policy = self._make_policy()
        policy.action_activate()
        policy.action_deactivate()

        policy.action_set_draft()
        self.assertEqual(policy.state, "draft")

    # --- Deactivation impact ---

    def test_deactivation_impact_empty_for_unused_policy(self):
        """_get_deactivation_impact() returns None when nothing depends on the policy."""
        policy = self._make_policy()
        policy.action_activate()
        self.assertIsNone(policy._get_deactivation_impact())

    def test_deactivation_impact_mentions_affected_count(self):
        """Impact message mentions the number of affected records."""
        policy = self._make_policy()
        policy.action_activate()
        # Create a dependent record — implementation-specific.
        self.env["myorg.thing"].create({"policy_id": policy.id, "name": "A"})

        impact = policy._get_deactivation_impact()
        self.assertIsNotNone(impact)
        self.assertIn("1", impact)
```

**Key patterns to notice:**

- Tests call the action methods (`action_activate`, `action_deactivate`, etc.) directly rather than going through the wizard. This keeps tests fast and focused on the lifecycle contract.
- `_pre_activate()` raising is the right way to block invalid activation — the test asserts the exception AND that the state didn't change.
- The `activated_date` and `activated_by_id` audit fields are populated automatically by the mixin — tests can assert them without any extra setup.
- `_get_deactivation_impact()` is a plain Python method — test it independently of the wizard by calling it directly.

## Custom fields

Studio custom fields are a three-layer structure:

1. **`spp.studio.field` record** — the Studio configuration: label, technical name, type, target model, placement zone, visibility conditions, help text, state (draft/active/inactive).
2. **`ir.model.fields` record** — the real Odoo field, created automatically by `_pre_activate()` when the Studio field is activated. Always named with the `x_` prefix.
3. **`ir.ui.view` extension** — the view inheritance record that injects the field into the appropriate form view at the configured placement zone.

Deactivating a Studio field hides the view extension but **leaves the `ir.model.fields` record in place** so historical data is preserved.

### Available field types

| Studio type | Odoo type | Notes |
|-------------|-----------|-------|
| `text` | Char | |
| `long_text` | Text | |
| `integer` | Integer | |
| `decimal` | Float | |
| `date` | Date | |
| `datetime` | Datetime | |
| `boolean` | Boolean | |
| `selection` | Selection | Options configured on the `spp.studio.field` record via `selection_options` (format `value|Label`, one per line) |
| `multi_select` | Text (JSON array, `many2many_tags` widget) | Same `selection_options` format as `selection`; values are persisted as a JSON array |
| `link` | Many2one | Target model and domain configured on the Studio field record |

```{note}
The field type list is hardcoded in `FIELD_TYPE_MAPPING` (`spp_studio/models/studio_field.py`). There is no extension point for registering custom field types — for specialized inputs, use `selection` with a controlled list or `link` to a custom model.
```

### Field visibility conditions

Field visibility is configured as a simple condition on another field (not a CEL expression). Four fields control it:

- `visibility_condition` — selection of `always` (default) or `conditional`. **Must be set to `conditional` for the other visibility fields to take effect.**
- `visibility_field_id` — the field whose value gates visibility
- `visibility_operator` — one of `set`, `not_set`, `equals`, `not_equals`
- `visibility_value` — the value to compare against (for `equals`/`not_equals`)

Studio compiles this to an Odoo `invisible="..."` attribute on the view extension.

## Logic packs

A **logic pack** (`spp.studio.pack`) is a pre-built bundle of CEL variables and expressions for a common program type. `spp_studio` ships with 13 packs in `data/packs/`:

- `cash_transfer_basic`, `pmt_targeting`, `child_benefit`, `social_pension`, `disability_assistance`, `ovc_support`, `cct_program`, `vulnerability_assessment`, `geographic_targeting`, `guaranteed_minimum_income`, `public_works`, `benefit_adjustments`, `exclusion_criteria`

Each pack contains `spp.studio.pack.item` records — individual variables or expressions of type `filter`, `formula`, `scoring`, `validation`, or `other`. The pack install wizard (`spp.studio.pack.install.wizard`) lets administrators install a pack's items into their configuration.

### Shipping your own pack

Your module can ship additional packs as XML data:

```xml
<record id="my_custom_pack" model="spp.studio.pack">
    <field name="name">My Custom Program Pack</field>
    <field name="code">my_custom_pack</field>
    <field name="category">cash_transfer</field>
    <field name="description">Eligibility and scoring for custom program.</field>
    <field name="required_modules">spp_programs,spp_cel_domain</field>
</record>

<record id="my_pack_item_eligibility" model="spp.studio.pack.item">
    <field name="pack_id" ref="my_custom_pack" />
    <field name="name">Household Below Poverty Line</field>
    <field name="expression_type">filter</field>
    <field name="context_type">group</field>
    <field name="logic_data">{"cel": "income &lt; poverty_line"}</field>
</record>
```

For a full list of pack categories and item types, study the packs in `spp_studio/data/packs/`.

## The change request type builder

`spp_studio_change_requests` provides a 3-step wizard (`spp.studio.cr.type.wizard`) that turns field selections into a working CR type:

1. **Basic info** — name, target type, approval settings
2. **Field selection** — pick which `res.partner` fields this CR type can modify
3. **Review** — preview the generated CR type

On activation (`spp.studio.change.request.type._pre_activate()`), it:

- Creates a dynamic detail model named `x_spp_cr_detail_<technical_name>` with one field per selected mapping
- Creates the `spp.change.request.type` record pointing at that detail model
- Creates `spp.change.request.type.mapping` records that describe how each detail field maps to a registrant field at apply time

Studio-created CR types and code-defined CR types (the pattern in {doc}`/developer_guide/change_request_types/index`) interoperate through the same `spp.change.request.type` table. A Studio CR type is not a second-class citizen — it's just one produced by a wizard instead of by hand.

For custom apply logic or complex validation, you still need a code-defined CR type — Studio CR types are limited to the field-mapping apply strategy.

## The event type designer

`spp_studio_events` provides a wizard (`spp.studio.event.type.wizard`) for designing event types used in data collection workflows — surveys, health screenings, visits.

Key models:

- `spp.studio.event.type` — the Studio configuration record
- `spp.studio.event.field.group` — groups fields into tabs in the generated wizard view
- `spp.studio.event.field.template` — reusable field patterns you can apply to multiple event types

On activation, the module creates an `spp.event.type` record and a generated form view (`wizard_view_id`) that collectors use to enter event data.

## Shipping Studio configurations with your module

Because Studio configurations are ORM records, you can pre-seed them with XML data the same way you seed any other records. Wrap the records in `<data noupdate="1">`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">

        <record id="studio_field_farm_size" model="spp.studio.field">
            <field name="label">Farm Size (hectares)</field>
            <field name="technical_name">x_farm_size</field>
            <field name="target_type">individual</field>
            <field name="field_type">decimal</field>
            <field name="placement_zone_id" ref="spp_studio.zone_registrant_extras" />
            <field name="is_required" eval="False" />
            <field name="state">draft</field>
        </record>

    </data>
</odoo>
```

### Why `noupdate="1"` matters

Without `noupdate="1"`, every module upgrade re-applies the XML record — overwriting any edits the administrator made. A Studio field shipped without `noupdate` that the admin renames from "Farm Size (hectares)" to "Farm Area (ha)" will silently revert on the next upgrade. With `noupdate="1"`, the record is created on first install and never touched again by module upgrades.

### Ship as `state="draft"`, not `state="active"`

Activation is a deliberate administrator action — it creates `ir.model.fields` and `ir.ui.view` records owned by your module's XML ID. Shipping `state="active"` does two things you don't want:

1. **It runs `_pre_activate()` during module install**, creating an actual database column immediately. If the field has defaults that assume existing data, or if the model has millions of rows, install time can spike.
2. **Module uninstall can silently drop the column.** Because the underlying `ir.model.fields` record is owned by your module's XML ID, uninstalling the module removes it — along with any user data in that column. Shipping as `draft` and letting an admin activate breaks that ownership chain: activation creates new records that are *not* owned by your module's XML ID.

### What happens on uninstall

With `noupdate="1"` and `state="draft"`:

- Uninstall removes the `spp.studio.field` record (your XML-owned record)
- If the admin had activated it, the `ir.model.fields` and `ir.ui.view` records remain (they aren't owned by your module), so the database column and user data survive
- An admin who reinstalls your module gets a fresh Studio field record in `draft` state and can re-activate if they want the old view extension back (though the existing column is already usable)

## API V2 bridge

When `spp_studio_api_v2` is installed, activated `spp.studio.field` records with `api_exposed=True` are automatically added to the Individual or Group extension in API V2. Each activation adds the field to the extension; each deactivation removes it.

The module also exposes four endpoints (documented in detail at {doc}`/developer_guide/api_v2/studio_integration`):

- `GET /Studio/fields` — list all exposed Studio fields
- `GET /Studio/fields/{technical_name}/schema` — JSON Schema validation rules for a single Studio field
- `GET /Studio/variables` — list CEL variables available in Studio
- `GET /Studio/variables/{resource_type}/{identifier}` — fetch cached variable values for a specific subject (e.g., `/Studio/variables/Individual/urn:gov:ph:psa:national-id|PH-123456789`)

## Common mistakes

**Forgetting `_pre_activate()` validation.** The mixin calls `_pre_activate()` before state transition. If you do expensive validation elsewhere (in a `@api.constrains` triggered by a later write), you get a half-activated state. Put activation-gate validation in `_pre_activate()` so the state change rolls back atomically on failure.

**Deleting `ir.model.fields` on deactivate.** Deactivating a Studio field must not delete the underlying `ir.model.fields` record — existing registrant data lives in that column. The mixin's default `_post_deactivate()` for `spp.studio.field` correctly sets `view_inherit_id.active = False` but leaves the column in place. If you override `_post_deactivate()`, preserve this invariant.

**Shipping configurations as `state="active"`.** Module data that installs pre-activated Studio configurations runs `_pre_activate()` at install time — for a `spp.studio.field`, that creates `ir.model.fields` and `ir.ui.view` records owned by your module's XML ID. Upgrades and uninstalls can then remove those records, silently deleting a column users have data in. Ship configurations as `state="draft"` and let administrators activate.

**Expecting a plugin mechanism for custom field types.** `FIELD_TYPE_MAPPING` is hardcoded. If you need a specialized input (phone with country code, currency amount), either use `selection` with an enumerated list, `link` to a model that represents your type, or extend `spp.studio.field` and modify the mapping in your own module.

**Assuming Studio CR types support custom apply logic.** Studio CR types use the field-mapping apply strategy only. If you need custom logic (create related records, multi-step changes, integration calls), build a code-defined CR type instead — see {doc}`/developer_guide/change_request_types/tutorial`.

**Confusing the `spp_studio_events` "events" with Odoo/system events.** This module designs **data-collection event types** (surveys, visits), not framework-level event subscribers. For CEL-based aggregation over collected events, see `spp_cel_event` and {doc}`/developer_guide/cel/index`.

## See also

- {doc}`/developer_guide/cel/index` — CEL expressions used by Studio logic
- {doc}`/developer_guide/change_request_types/index` — code-defined change request types
- {doc}`/developer_guide/api_v2/studio_integration` — exposing Studio fields and variables through the API V2
- {doc}`/developer_guide/custom_modules/index` — general Odoo module scaffold

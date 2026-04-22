---
openspp:
  doc_status: draft
  products: [core]
---

# Audit and Versioning

**For: developers**

How OpenSPP records who changed what (audit logging) and how configuration artifacts can ship future versions that activate on a schedule (versioning). Also covers two adjacent stores: structured event data (`spp_event_data`) and a clarifying note on what `spp_session_tracking` is — and isn't.

## How to use this section

1. Read **Audit logging** if you need records of changes to your module's models, or want to write custom audit entries from code
2. Read **Versioning** if you're building a configuration artifact that needs draft/scheduled/current states
3. Read **Event data** if you need to record registrant-centric events (surveys, visits, field syncs) that downstream CEL rules can aggregate over
4. See the **Session tracking** note below to avoid confusing it with login/API tracking

## Prerequisites

- Familiarity with Odoo models and `ir.cron`
- For versioning: understanding of JSON snapshots and polymorphic references
- For event data: basic familiarity with {doc}`/developer_guide/cel/index` (CEL aggregation is the most common consumer)

## The modules at a glance

| Module | Purpose | Developer entry point |
|--------|---------|-----------------------|
| `spp_audit` | Immutable audit log with 4 backends (DB, file, syslog, HTTP) | Configure an `spp.audit.rule`, or call `log_lifecycle_action()` |
| `spp_versioning` | Snapshot-based versioning with scheduled activation via cron | Inherit `spp.versioned.mixin` |
| `spp_event_data` | Registrant-centric event store (surveys, visits, syncs) | `env["spp.event.data"].create(...)` |
| `spp_session_tracking` | **Training attendance** — not login/API tracking | `spp.session` and `spp.session.attendance` records |
| `spp_source_tracking` | Data provenance mixin (source system, collection method) | Inherit `spp.mixin.source.tracking` — see {doc}`/developer_guide/custom_modules/mixins` |

## Audit logging

`spp_audit` is OpenSPP's immutable audit trail. It is **configured through rules**, not through a model mixin — to audit a model, you create an `spp.audit.rule` record, and the module auto-applies `create` / `write` / `unlink` decorators at registry load. Developers rarely need to touch audit code; most auditing is configured, not programmed.

### Concepts

- **`spp.audit.rule`** — configuration record that says "audit these fields on this model for these operations." Fields include `model_id`, `field_to_log_ids`, `is_log_create` / `is_log_write` / `is_log_unlink`, lifecycle flags (`is_log_activate`, `is_log_deactivate`, `is_log_state_change`), and a `is_post_to_thread` flag (default false — enable only for low-volume, human-reviewed records).
- **`spp.audit.log`** — the entries themselves. Stores `user_id`, `model_id`, `res_id`, `method` (create/write/unlink + lifecycle verbs), `data` (old/new values), and `create_date`. `ALLOW_DELETE = False` — entries are immutable.
- **Audit backends** — four storage backends that each receive every entry: `database` (UI-visible `spp.audit.log` rows), `file` (daily-rotated JSONL), `syslog` (configurable facility), `http` (webhook POST with optional auth headers). Dispatch is sequential with per-backend error isolation — if one backend raises, the remaining backends still receive the entry.

### Setting up auditing for your model

No code changes needed — create an `spp.audit.rule` record, either manually in the UI or as module data:

```xml
<record id="audit_rule_applicant" model="spp.audit.rule">
    <field name="name">Applicant audit</field>
    <field name="model_id" ref="model_myorg_applicant" />
    <field name="is_log_create" eval="True" />
    <field name="is_log_write" eval="True" />
    <field name="is_log_unlink" eval="True" />
    <field name="field_to_log_ids"
        eval="[(6, 0, [ref('field_myorg_applicant__status'), ref('field_myorg_applicant__amount')])]" />
    <field name="is_post_to_thread" eval="False" />
</record>
```

On next module load, `spp_audit._register_hook()` rewraps the model's `create` / `write` / `unlink` with auditing decorators. You do not inherit a mixin or change your model code.

### Writing custom audit entries from code

For state changes that aren't pure ORM operations (approvals, downloads, exports, lifecycle actions), use `log_lifecycle_action()`:

```python
self.env["spp.audit.rule"].log_lifecycle_action(
    model_name="myorg.applicant",
    record_id=applicant.id,
    action="approve",                        # Any string: approve, reject, download, export, etc.
    old_values={"status": "pending"},
    new_values={"status": "approved"},
)
```

The method writes an `spp.audit.log` row with the action as `method` and dispatches to all enabled backends.

```{important}
`log_lifecycle_action` **requires an `spp.audit.rule` to exist for the model**, and the corresponding action flag on the rule (`is_log_activate`, `is_log_deactivate`, `is_log_state_change`, `is_log_download`, `is_log_preview`, `is_log_export`) must be enabled. If no rule exists or the flag is disabled, the call returns `False` silently and no log entry is written. Ship the rule as module data if your module depends on lifecycle logging.
```

This is how `spp.studio.mixin` records every activate / deactivate / set_draft transition automatically — your Studio-aware models inherit audit logging for free (once an audit rule is configured).

### Reading the audit log for a record

```python
logs = self.env["spp.audit.log"].search([
    ("model_id.model", "=", "myorg.applicant"),
    ("res_id", "=", applicant.id),
], order="create_date desc")

for log in logs:
    print(f"{log.create_date}  {log.user_id.name}  {log.method}")
    print(log.data)       # repr of {"old": {...}, "new": {...}}
    print(log.data_html)  # Pre-formatted HTML table for display
```

Reading requires `spp_audit.group_audit_manager` (included in `spp_security.group_spp_admin`). Users without that group see an `AccessError`. Audit logs are read-only even for the manager group — there is no supported "edit history" operation.

### Configuring backends

Backends are configured through system parameters and `spp.audit.backend` records. Administrators enable/disable each backend and configure endpoints (file paths, syslog facility, HTTP URL). Configuration in `odoo.conf` takes precedence over database-stored config — this tamper-resistance pattern means an attacker who gains admin access can't silently redirect the audit stream by editing database records.

## Versioning

`spp_versioning` supports **snapshot versioning** — each version is a full JSON snapshot of selected fields, not a diff — with an **immutable lifecycle** and **scheduled activation** via cron. The canonical use case is configuration artifacts that need to be reviewed and approved before going live: Studio logic expressions, rule sets, program configurations.

### Concepts

- **`spp.artifact.version`** — the version record. Polymorphic: `model` (string) + `res_id` (Many2oneReference) point to the parent artifact. Fields include `version` (integer), `data_snapshot` (JSON), `effective_date` (scheduled activation), `state`, `change_summary`, `supersedes_id`.
- **Lifecycle states:** `draft` → `pending` → `approved` → `scheduled` → `current` → `superseded` (with `cancelled` and `archived` as off-ramps). Only one `current` version per artifact at a time — enforced by an `@api.constrains` validation on `(state, model, res_id)`.
- **Scheduled activation cron** — `_cron_activate_scheduled_versions()` runs daily, finds versions in `state=scheduled` with `effective_date <= today`, supersedes the previous `current`, and transitions the new version to `current`.

### Making your model versioned

Inherit `spp.versioned.mixin` and, optionally, override `_get_version_snapshot_fields()` to control what gets captured:

```python
from odoo import models


class ProgramPolicy(models.Model):
    _name = "myorg.program.policy"
    _inherit = ["myorg.program.policy", "spp.versioned.mixin"]

    def _get_version_snapshot_fields(self):
        """Return fields to include in every version snapshot."""
        return [
            "name",
            "threshold",
            "formula",
            # For relational fields, pass a dict specifying how to serialize:
            ("category_id", {"strategy": "embed", "fields": ["name", "code"]}),
        ]
```

The mixin provides helper methods that avoid computed fields (computed fields interact badly with the audit decorator): `get_version_count()`, `get_current_version()`, `get_usage_count()`, `get_is_in_use()`. Call these explicitly instead of relying on `@api.depends`.

### Creating and scheduling a version

Don't create `spp.artifact.version` records manually. Use the supported API — either the convenience action on the mixin (which returns a draft version) or `create_version()` on the artifact-version model:

```python
# Option 1: from the versioned record
version = policy.action_create_version(
    change_summary="Raise threshold from 1000 to 1500",
)
# Returns a spp.artifact.version in state="draft" with data_snapshot populated
# from _get_version_snapshot_fields()

# Option 2: programmatic create via the version model
version = self.env["spp.artifact.version"].create_version(
    model="myorg.program.policy",
    res_id=policy.id,
    change_summary="Raise threshold from 1000 to 1500",
)
```

Both paths serialize the fields returned by `_get_version_snapshot_fields()` into `data_snapshot` for you — you don't build the snapshot by hand. The returned record is in `state="draft"`.

Move it through the lifecycle:

```python
# After review and approval:
version.state = "approved"

# Schedule for activation next Monday
version.write({
    "state": "scheduled",
    "effective_date": next_monday,
})
```

On `effective_date`, the cron transitions `version.state` to `current` and the previous current version to `superseded`. If your model needs to apply the snapshot back onto the parent artifact at activation time (so live reads reflect the scheduled values), define an **`_apply_version_snapshot(snapshot)` method on your versioned model** — `spp.artifact.version._apply_snapshot_to_artifact()` internally calls it if present:

```python
class ProgramPolicy(models.Model):
    _inherit = "myorg.program.policy"

    def _apply_version_snapshot(self, snapshot):
        """Called by the versioning cron when a scheduled version activates."""
        self.write({
            "threshold": snapshot.get("threshold"),
            "formula": snapshot.get("formula"),
            # Handle relational fields as needed
        })
```

### Using versioning with Studio

`spp.studio.mixin` already integrates with versioning — Studio-configured logic expressions and variable definitions can be versioned by inheriting `spp.versioned.mixin` alongside `spp.studio.mixin`. The two mixins compose cleanly because they target different lifecycles (Studio's is active/inactive; versioning's is the approval pipeline leading up to active).

## Event data

`spp_event_data` is a **structured event store for registrant-centric events**, not an audit log. Use cases:

- Survey responses collected through ODK or KoBoToolbox
- Field visit records
- Data sync events from external systems (CRVS births, IBR enrollments)
- Any "something happened to this registrant at this time" data that downstream logic needs to aggregate or filter

It overlaps with audit in one place: `spp_change_request_v2` writes `cr_audit` events to `spp.event.data` on every CR state transition, giving CEL rules a way to count "how many CRs did this registrant have in the last 30 days" without querying the audit log. Treat that as a domain-specific dual use — don't replace `spp_audit` with `spp_event_data` as a general audit mechanism.

### Core models

- **`spp.event.type`** — event type configuration: `code`, `category` (`survey`, `visit`, `sync`, `manual`), `target_type` (`individual` / `group` / `both`), `source_type` (`internal` / `odk` / `kobo` / `api`), optional `data_model_id` (if the event has a dedicated Odoo model) or `field_ids` (custom fields on the event).
- **`spp.event.data`** — the event record: `event_type_id`, `partner_id` (the registrant), `collection_date`, `collector_id`, `state`, `data_json` (for free-form payloads) OR `data_record_id` (for typed storage), `expiry_date`, `superseded_by_id`.

### Recording an event

```python
event_type = self.env.ref("myorg.event_type_health_screening")

self.env["spp.event.data"].sudo().create({
    "event_type_id": event_type.id,
    "partner_id": registrant.id,
    "collection_date": fields.Date.today(),
    "state": "active",
    "data_json": {
        "bmi": 22.3,
        "bp_systolic": 120,
        "bp_diastolic": 80,
        "notes": "Routine check",
    },
})
```

### Integration with CEL

Events are accessible from CEL expressions through `spp_cel_event`, which adds an `events` aggregate target. A variable definition like "health screenings in the last 90 days" aggregates over `spp.event.data` filtered by event type, date range, and state. See {doc}`/developer_guide/cel/index` for the CEL side of this.

## Session tracking — scope clarification

```{important}
`spp_session_tracking` tracks **attendance at required sessions and trainings** (VSLA group meetings, beneficiary orientation, conditionality compliance sessions). It is **not** login session tracking or API call auditing.
```

If you're looking for "who logged in when," that isn't in any single OpenSPP module. Login tracking is handled by Odoo's core `res.users` framework (the `login_date` field and mail activities) and by `spp_audit` when the `res.users` model has an audit rule. API call auditing is in `spp_api_v2`'s per-client request logging, not here.

The `spp.session` model in this module represents a real-world meeting or training event:

- `session_type_id`, `date`, `start_time`, `end_time`, `facilitator_id`, `expected_participant_ids`
- `attendance_ids` is a One2many to `spp.session.attendance`, one row per participant recording `is_attended`, `attendance_time`, `is_excused`, `excuse_reason`

This is a business-domain model, not infrastructure. A program with conditionality rules ("beneficiary must attend 4 sessions per month") uses this module and reads attendance records from CEL to determine eligibility. Don't build login or API-audit features on top of it.

## Source tracking (brief)

`spp_source_tracking` provides the `spp.mixin.source.tracking` mixin that stamps `source_system`, `source_reference`, `collection_method` (values: `manual`, `import`, `api`, `mobile`, `migration`, `merge`), and `collection_date` on record creation, plus `last_update_system` / `last_update_reference` on updates. The full developer API is documented in {doc}`/developer_guide/custom_modules/mixins`.

## Common mistakes

**Creating an audit mixin on your model instead of a rule.** Models don't inherit an audit mixin in OpenSPP. Create an `spp.audit.rule` record (XML data or UI) and the audit decorators are auto-applied at registry load. If you want audit logging from day one, ship the rule record as module data.

**Enabling `is_post_to_thread` on high-volume models.** The chatter integration posts a message on every audited change. For a high-write model, that floods the chatter and slows down every save. Leave `is_post_to_thread=False` (the default) unless the model is low-volume and human-reviewed.

**Querying `spp.audit.log` without a group check.** A normal user gets `AccessError` when reading audit logs. If you're building a UI that shows audit history, either wrap reads in `sudo()` with a careful user-facing filter, or require the caller to have `spp_audit.group_audit_manager`.

**Using `@api.depends` on a versioned model.** The audit decorator wraps `write`, which triggers computed-field recomputation, which triggers `write` again, which the audit decorator wraps. This can produce infinite recursion or phantom audit entries. The versioned mixin provides explicit helper methods (`get_version_count()`, `get_current_version()`) for this reason — use them instead of declaring computed fields that look at version history.

**Using `spp.event.data` as a general audit log.** Event data is for registrant-centric business events that CEL aggregates over. Use `spp_audit` for change tracking, not `spp_event_data`. The only reason `spp_change_request_v2` writes CR state transitions to `spp.event.data` is because CEL rules need to count them — if that's your use case, great; otherwise, use audit.

**Confusing `spp_session_tracking` with login tracking.** If someone asks "who's been logging into the system?", don't look here — this module tracks beneficiary attendance at meetings. User login tracking comes from Odoo core plus an audit rule on `res.users`.

**Forgetting that scheduled versions activate at 00:00 deployment-time.** The cron runs daily, not hourly. A version scheduled for today only activates on the next cron tick, which (by default) is midnight. If you need intra-day activation, shorten the cron interval — but consider whether you actually need it: scheduled versioning is for deliberate, reviewable configuration rollouts, not real-time changes.

## See also

- {doc}`/developer_guide/custom_modules/mixins` — the source-tracking mixin in detail
- {doc}`/developer_guide/cel/index` — CEL aggregation over event data
- {doc}`/developer_guide/security/index` — the `spp.studio.mixin` automatic audit logging on state changes
- {doc}`/developer_guide/studio/index` — how Studio configurations use versioning and audit

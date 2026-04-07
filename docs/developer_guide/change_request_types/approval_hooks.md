---
openspp:
  doc_status: draft
  products: [core]
---

# Approval hooks

The CR system provides lifecycle hooks that run at each stage of the approval workflow. Override these hooks in a custom module to add side effects like notifications, external API calls, or additional validation.

If you have not built a CR type before, start with the {doc}`tutorial`.

## Lifecycle

A change request moves through these states:

```text
           ┌─────────────────────────────────────┐
           │                                     │
           ▼                                     │
Draft ──► Submit ──► Pending ──► Approve ──► Apply
                       │                         
                       ├──► Reject                
                       │                         
                       └──► Request Revision ──► Revision ──► Resubmit ──► Pending
                                                                              │
                                                                              └─►...
```

Each transition triggers a hook method on the `spp.change.request` model.

## Available hooks

| Hook | When it runs | What it does by default |
|------|-------------|------------------------|
| `_on_submit()` | User submits CR from draft or revision | Runs conflict checks, creates audit event |
| `_on_approve()` | Approver approves the CR | Re-checks conflicts, triggers auto-apply if configured, creates audit event |
| `_on_reject(reason)` | Approver rejects the CR | Logs rejection with the reason, creates audit event |
| `_on_request_revision(notes)` | Approver requests changes | Sets stage back to "review", creates audit event |
| `_on_reset_to_draft()` | Manager resets CR to draft | Sets stage back to "details", creates audit event |
| `_check_can_submit()` | Before `_on_submit()` | Validates the CR is in a submittable state (draft or revision) |

## Extending a hook

To add custom behavior, override the hook in a model that inherits `spp.change.request`. Always call `super()` to preserve the default behavior:

```python
from odoo import models


class ChangeRequestCustom(models.Model):
    _inherit = "spp.change.request"

    def _on_approve(self):
        # Run before the default approval logic
        for rec in self:
            if rec.request_type_id.code == "transfer_member":
                # Custom pre-approval logic for this CR type
                rec._notify_source_group_manager()

        # Call the default implementation
        super()._on_approve()

        # Run after the default approval logic
        for rec in self:
            if rec.request_type_id.code == "transfer_member":
                rec._notify_target_group_manager()
```

**Filter by CR type.** The hooks are called for all CR types, so check `request_type_id.code` if your logic only applies to a specific type.

### Hook execution order

When a CR is submitted, the system calls:

1. `_check_can_submit()` — validates the CR can be submitted
2. `_on_submit()` — which internally calls `_run_conflict_checks()`

When a CR is approved:

1. `_on_approve()` — which internally calls `_run_conflict_checks()` again (to catch conflicts that appeared after submission)
2. If `auto_apply_on_approve` is enabled on the CR type, `action_apply()` is called automatically

## Auto-apply

If a CR type has `auto_apply_on_approve = True`, the system calls `action_apply()` immediately after `_on_approve()` completes. This is useful for low-risk, pre-validated changes where a manual apply step adds no value.

Configure this on the CR type record:

```xml
<record id="cr_type_example" model="spp.change.request.type">
    <!-- ... other fields ... -->
    <field name="auto_apply_on_approve" eval="True" />
</record>
```

## Dynamic approval

Dynamic approval routes a CR to different approval workflows based on the value of a specific field. For example, a name change might require a different approval chain than an address change.

This feature uses CEL (Common Expression Language) conditions on approval definition candidates. The system evaluates each candidate's condition against the CR's field values and uses the first match.

Dynamic approval is configured on the CR type, not in code:

| Field | Purpose |
|-------|---------|
| `use_dynamic_approval` | Enable dynamic approval routing |
| `candidate_definition_ids` | Ordered list of approval definitions with CEL conditions |

When `use_dynamic_approval` is enabled, the CR requires the user to select which field they are modifying (via `selected_field_name`). The system then evaluates:

```python
def _resolve_dynamic_approval(self):
    for candidate in self.request_type_id.candidate_definition_ids:
        if not candidate.cel_condition:
            return candidate.approval_definition_id  # Catch-all
        if self._evaluate_cel_condition(candidate.cel_condition):
            return candidate.approval_definition_id
    return None
```

For details on CEL expressions, see {doc}`/developer_guide/cel/index`.

## Conflict detection hooks

The CR system runs conflict detection on submission and approval. By default, it checks for other active CRs that affect the same registrant, group, or fields.

To add custom conflict logic for a specific CR type, override `_check_custom_conflicts()` on the conflict mixin:

```python
class ChangeRequestCustomConflicts(models.Model):
    _inherit = "spp.change.request"

    def _check_custom_conflicts(self, candidates, rule):
        """Filter candidates to those that actually conflict.

        Args:
            candidates: Recordset of potentially conflicting CRs
            rule: The spp.cr.conflict.rule being evaluated

        Returns:
            Filtered recordset of actual conflicts
        """
        if self.request_type_id.code != "transfer_member":
            return super()._check_custom_conflicts(candidates, rule)

        # Only flag as conflict if another CR targets the same individual
        detail = self.get_detail()
        if not detail or not detail.individual_id:
            return self.env["spp.change.request"]

        conflicting = self.env["spp.change.request"]
        for candidate in candidates:
            candidate_detail = candidate.get_detail()
            if (candidate_detail and
                    hasattr(candidate_detail, "individual_id") and
                    candidate_detail.individual_id == detail.individual_id):
                conflicting |= candidate
        return conflicting
```

This hook is called when a conflict rule has `scope = "custom"`. For configuring conflict rules through the UI, see {doc}`/config_guide/change_request_types/conflict_detection`.

### Conflict actions

Each conflict rule specifies an action:

| Action | Behavior |
|--------|----------|
| `block` | Prevents submission until the conflict is resolved or overridden |
| `warn` | Allows submission but displays a warning to the reviewer |
| `log` | Records the conflict silently — no user-facing impact |

If a blocking conflict exists, the user must either resolve the conflicting CR or request an override from a user with the `group_cr_conflict_approver` permission.

## Audit events

The CR system automatically creates `spp.event.data` records for every state transition. Each audit event captures:

| Field | Content |
|-------|---------|
| `action` | `created`, `submitted`, `approved`, `rejected`, `applied` |
| `old_state` / `new_state` | The state before and after the transition |
| `user_id` / `user_name` | Who performed the action |
| `change_request_id` | Link to the CR |
| `create_date` | When the transition occurred |

To create a custom audit event from within a hook override:

```python
def _on_approve(self):
    super()._on_approve()
    for rec in self:
        if rec.request_type_id.code == "transfer_member":
            rec._create_audit_event(
                action="custom_notification_sent",
                old_state="pending",
                new_state="approved",
            )
```

The `_create_audit_event()` method is provided by the base CR model and handles event creation with the current user and timestamp.

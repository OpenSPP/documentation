---
openspp:
  doc_status: draft
  products: [core]
  applies_to:
    - social_registry
    - sp_mis
---

# Change Requests

**Applies to:** Social Registry, SP-MIS

Change Requests allow staff to propose updates to registrant information through a structured approval workflow. Instead of editing records directly, staff submit change requests that go through review and approval before being applied.

## Why use change requests?

Change requests provide:

- **Audit trail** - Every change is tracked with who requested it and who approved it
- **Data quality** - Supervisors can verify changes before they take effect
- **Accountability** - Clear record of what was changed, when, and why
- **Workflow control** - Different change types can require different approval levels

## Request status flow

All change requests follow this workflow:

```
Draft → Under Review → Approved → [Finalize] → Completed
                    ↘ Needs Changes → (edit) → Under Review
                    ↘ Declined
```

```{note}
**Finalization Step**: After a change request is approved, it must be finalized using the "Finalize & Record Changes" action before the changes are actually applied to the registrant's record. This provides an additional safety check before making permanent changes.
```

| Status | What it means |
|--------|---------------|
| **Draft** | Request is being created, not yet submitted |
| **Under Review** | Waiting for a validator to review |
| **Needs Changes** | Sent back to submitter for corrections |
| **Approved** | Approved and ready to finalize (requires "Finalize & Record Changes" action) |
| **Completed** | Changes have been recorded to the registrant |
| **Declined** | Request was rejected |

## Who can do what?

| Role | Can do |
|------|--------|
| **User** | Create and submit change requests |
| **Validator** | Review, approve, or decline requests |
| **Manager** | All of the above, plus configure request types |

## Topics covered

```{toctree}
:maxdepth: 2
:hidden:

submit_change_request
review_change_request
change_request_types
```

- {doc}`submit_change_request` - Create and submit a change request
- {doc}`review_change_request` - Review and approve or decline requests
- {doc}`change_request_types` - Reference of available request types

---
openspp:
  doc_status: draft
---

# Approval Workflows

**Module:** `spp_approval`

## Overview

The Approval module (`spp_approval`) provides standardized approval workflows with multi-tier sequencing and CEL-based rules. It enables organizations to implement maker-checker processes, multi-level authorization, and conditional approval routing across any OpenSPP model.

## Purpose

This module is designed to:

- **Standardize approvals:** Consistent workflow across all approvable records
- **Support multi-tier review:** Sequential approval through multiple authorization levels
- **Enable conditional routing:** CEL expressions determine which approval path applies
- **Maintain audit trail:** Full history of submissions, approvals, and rejections
- **Integrate with activities:** Odoo mail activities for approver notifications

## Module Dependencies

| Dependency        | Description                                     |
| ----------------- | ----------------------------------------------- |
| `base`            | Odoo core framework                             |
| `mail`            | Mail thread and activities for notifications    |
| `spp_base_common` | Common OpenSPP utilities                        |
| `spp_cel_domain`  | CEL expression evaluation for conditional rules |
| `spp_security`    | Security groups and access control              |

## Key Features

### Approval Mixin

Add approval capability to any model:

```python
class MyModel(models.Model):
    _name = "my.model"
    _inherit = ["mail.thread", "mail.activity.mixin", "spp.approval.mixin"]

    def _on_approve(self):
        # Custom logic after approval
        self.state = "active"
```

### Approval States

| State    | Description                    |
| -------- | ------------------------------ |
| Draft    | Initial state, can be edited   |
| Pending  | Submitted, awaiting approval   |
| Revision | Returned for corrections       |
| Approved | Approved by authorized user(s) |
| Rejected | Rejected with reason           |

### Approval Definitions

Configure approval workflows:

| Setting                | Description                            |
| ---------------------- | -------------------------------------- |
| Name                   | Definition identifier                  |
| Model                  | Target model for this workflow         |
| Approval Group         | Security group with approval rights    |
| Auto-approve Same User | Skip approval if submitter is approver |
| SLA Days               | Expected approval timeframe            |
| Notify on Submit       | Send activity to approvers             |
| Respect System Freeze  | Block during freeze periods            |

### Multi-Tier Approvals

Sequential approval through multiple levels:

| Tier               | Configuration                         |
| ------------------ | ------------------------------------- |
| Tier Name          | Display name (e.g., "Manager Review") |
| Sequence           | Order of tiers (1, 2, 3, ...)         |
| Approval Group     | Who can approve at this tier          |
| Required Approvers | Minimum approvals needed              |
| All Must Approve   | Require every group member            |

Example workflow:

```
Tier 1: Supervisor (1 approval required)
    ↓
Tier 2: Manager (1 approval required)
    ↓
Tier 3: Director (1 approval required)
```

### CEL-Based Routing

Conditional approval definitions using CEL expressions:

```
# High-value entitlements require director approval
r.amount >= 10000

# Cross-area transfers need regional approval
r.source_area_id.parent_id != r.dest_area_id.parent_id
```

Multiple definitions can exist for the same model; the first matching condition applies.

### Approval Reviews

Track individual approval actions:

| Field          | Description                     |
| -------------- | ------------------------------- |
| Requested By   | User who submitted for approval |
| Requested Date | When submitted                  |
| Reviewed By    | User who approved/rejected      |
| Review Date    | When reviewed                   |
| Status         | Pending, Approved, Rejected     |
| Comment        | Reviewer's notes                |

### Revision Requests

Approvers can request changes instead of rejecting:

| Action           | Result                          |
| ---------------- | ------------------------------- |
| Request Revision | Returns to submitter with notes |
| Revision Notes   | Explanation of needed changes   |
| Resubmit         | Submitter can fix and resubmit  |

### System Freeze

Temporarily block approvals:

| Setting     | Description                      |
| ----------- | -------------------------------- |
| Freeze Name | Identifier for the freeze period |
| Start Date  | When freeze begins               |
| End Date    | When freeze ends                 |
| Models      | Which models are affected        |
| Companies   | Which companies are affected     |
| Reason      | Explanation for the freeze       |

Use cases: Month-end close, system maintenance, regulatory holds.

### Optimistic Locking

Prevents concurrent approval conflicts:

- Version number increments on each state change
- Concurrent approval attempts are detected
- User receives "modified by another user" message

## Integration

### Submission Workflow

```python
# Submit for approval
record.action_submit_for_approval()

# Approve (by authorized user)
record.action_approve()

# Reject (opens wizard for reason)
record.action_reject()

# Request revision (opens wizard for notes)
record.action_request_revision()

# Reset to draft (after rejection/revision)
record.action_reset_to_draft()
```

### Custom Hooks

Override for model-specific behavior:

```python
def _on_submit(self):
    """Validate before submission"""
    if not self.required_field:
        raise UserError("Required field is missing")

def _on_approve(self):
    """Post-approval actions"""
    self.state = "active"
    self.send_confirmation_email()

def _on_reject(self, reason):
    """Post-rejection actions"""
    self.log_rejection(reason)
```

### Activity Integration

Approvers receive Odoo activities:

- Activity type: "Approval Required"
- Due date: Based on SLA days
- Summary: Record display name
- Feedback: Recorded when approved/rejected

### Batch Operations

Approve multiple records at once:

```python
MyModel.action_approve_batch(record_ids, comment="Batch approved")
```

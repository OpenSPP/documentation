---
openspp:
  doc_status: draft
  products: [drims]
---

# Configuring Approval Workflows

This guide is for **implementers** setting up multi-tier approval workflows for disaster relief requests. You should be comfortable configuring access rights and understanding basic workflow concepts, but you don't need to write code.

## Mental Model

DRIMS uses the `spp_approval` module to manage request approvals. Each request flows through a two-dimensional state model:

**Approval States** (what we're configuring here):

```{mermaid}
stateDiagram-v2
    [*] --> draft
    draft --> pending: Submit
    pending --> approved: Approve
    pending --> rejected: Reject
    pending --> revision: Request Changes
    revision --> pending: Re-submit
    revision --> rejected: Abandon
    rejected --> draft: Reset
    approved --> [*]
```

| State | Description | Who Can Act |
|-------|-------------|-------------|
| `draft` | Being prepared by requester | Request creator |
| `pending` | Awaiting approval decision | Request Approvers |
| `approved` | Approved for fulfillment | Warehouse staff |
| `rejected` | Denied with reason | Request creator (can reset) |
| `revision` | Returned for changes | Request creator |

**Key Concepts:**

- **Approval is separate from fulfillment** - Once approved, requests move to fulfillment states (allocated → dispatched → delivered)
- **Multiple approvers can act** - Any user with the Request Approver role can approve pending requests
- **Self-approval prevention** - Requesters cannot approve their own requests (enforced by `spp.approval.mixin`)
- **Audit trail** - All approval decisions are logged in the request's chatter

## Assigning Approvers

### Step 1: Give Users the Request Approver Role

Go to **Settings → Users & Companies → Users** and edit the user who should approve requests.

In the **DRIMS** section, check:

| Group | Purpose |
|-------|---------|
| **DRIMS Request Approver** | Can approve/reject requests (read-only otherwise) |

```{note}
Request Approvers can see all requests across all areas, but they can only **view and approve** them. They cannot create or edit requests unless they also have the DRIMS Officer or Field Officer role.
```

### Step 2: Assign Geographic Scope (Optional)

If approvers should only see requests from certain areas, assign them in **Areas** tab:

| Field | Value |
|-------|-------|
| **DRIMS Areas** | Select provinces/districts/divisions |

This uses area hierarchy, so assigning "Western Province" gives access to all districts within it.

### Step 3: Verify Access

Ask the approver to log in and check:
1. **DRIMS → Requests → Pending Approval** menu is visible
2. They can see pending requests
3. The **Approve**, **Reject**, and **Request Revision** buttons appear on requests

## Example: Three-Tier Approval

Many organizations use tiered approval based on request value or priority:

| Tier | Approver | Threshold |
|------|----------|-----------|
| **Tier 1** | District Coordinator | Requests up to $5,000 |
| **Tier 2** | Provincial Director | Requests $5,001 to $25,000 |
| **Tier 3** | National Director | Requests over $25,000 |

### Implementation

DRIMS doesn't enforce threshold rules automatically—you implement this through role assignment and training:

**District Coordinator Setup:**

| Field | Value |
|-------|-------|
| Groups | DRIMS District Coordinator, DRIMS Request Approver |
| DRIMS Areas | Colombo District |

**Training guideline:** "Approve requests up to $5,000. Escalate higher-value requests to Provincial Director."

**Provincial Director Setup:**

| Field | Value |
|-------|-------|
| Groups | DRIMS District Coordinator, DRIMS Request Approver |
| DRIMS Areas | Western Province |

**Training guideline:** "Approve requests $5,001 to $25,000. Escalate higher-value requests to National Director."

**National Director Setup:**

| Field | Value |
|-------|-------|
| Groups | DRIMS Manager |
| DRIMS Areas | (none - sees all via manager rule) |

**Training guideline:** "Approve all requests over $25,000."

```{important}
**Workflow enforcement is procedural.** DRIMS logs all approval actions in the audit trail and chatter, but it doesn't automatically route requests based on value. Train your team on approval thresholds and monitor the audit logs for compliance.
```

## Life-Threatening Request Bypass

Requests marked as **Life-Threatening** are intended to bypass normal approval thresholds and receive immediate attention.

### Setting the Flag

When creating a request, the requester checks:

| Field | Purpose |
|-------|---------|
| **Is Life-Threatening** | Emergency flag for immediate escalation |

Combined with Priority:

| Priority | Checkbox | Response Time |
|----------|----------|---------------|
| Critical | ✓ Life-Threatening | Immediate |
| High | (optional) | Within 24 hours |
| Medium | (not used) | 48-72 hours |
| Low | (not used) | Can wait |

### Emergency Approval Process

Train approvers on emergency protocols:

1. **Monitor the dashboard** - Life-threatening requests appear prominently
2. **Immediate notification** - Set up email alerts for life-threatening requests using Odoo Automated Actions
3. **Fast-track approval** - Approve immediately, even if above normal threshold
4. **Document justification** - Add notes in chatter explaining emergency approval

```{note}
The life-threatening flag is visible in the request list view and on the form. It's a visual indicator—you still need to approve the request manually.
```

## Common Patterns

### Single-Tier Approval

**Use case:** Small organization with one approval authority

**Setup:**
- Assign **DRIMS Request Approver** to the program manager
- All field officers create requests
- Program manager approves all requests

| Role | Groups |
|------|--------|
| Field Officer | DRIMS Field Officer |
| Program Manager | DRIMS Request Approver, DRIMS Manager |

### Multi-Tier with Area-Based Approval

**Use case:** Regional approvers for their areas, national approver for all

**Setup:**

| User | Groups | Areas |
|------|--------|-------|
| Western Regional Coordinator | DRIMS District Coordinator, DRIMS Request Approver | Western Province |
| Southern Regional Coordinator | DRIMS District Coordinator, DRIMS Request Approver | Southern Province |
| National Director | DRIMS Manager | (none - sees all) |

### Emergency-Only Fast Track

**Use case:** Normal requests follow full approval, but life-threatening requests go straight to national level

**Setup:**
- Train district coordinators to **not approve** life-threatening requests
- National director monitors life-threatening requests filter
- Use dashboard alerts to flag life-threatening requests

**Dashboard filter:**

| Filter | Value |
|--------|-------|
| Approval State | Pending |
| Is Life-Threatening | ✓ |

## Approval Workflow in Practice

### Approving a Request

1. Go to **DRIMS → Requests → Pending Approval**
2. Open the request
3. Review:
   - Justification and affected population
   - Requested items and quantities
   - Priority and date needed
4. Click **Approve**, **Reject**, or **Request Revision**
5. Add notes in the chatter explaining your decision

### Requesting Revisions

If a request needs changes:

1. Click **Request Revision**
2. Add a message in chatter: "Please update the quantity justification for tarpaulins"
3. State changes to `revision`
4. Requester receives notification
5. Requester edits the request and clicks **Re-submit**
6. State returns to `pending` for re-approval

### Rejecting a Request

1. Click **Reject**
2. Add rejection reason in chatter: "Request duplicates REQ-2025-001"
3. State changes to `rejected`
4. Requester can **Reset to Draft** to fix and re-submit

## Are You Stuck?

**Don't see the Pending Approval menu?**

You may not have the **DRIMS Request Approver** group. Contact your administrator to add it to your user account.

**Can't approve a request you created?**

DRIMS prevents self-approval. The `spp.approval.mixin` enforces this rule. Ask a colleague with the Request Approver role to approve it.

**Approver can see requests but buttons are missing?**

Check that:
1. The request is in `pending` state (not `draft` or `approved`)
2. The user has **DRIMS Request Approver** group (not just Viewer)
3. The user isn't the request creator (self-approval blocked)

**Need to configure automatic approval rules?**

DRIMS doesn't support automatic approval based on thresholds. You can implement this with custom code using CEL expressions and the `spp_approval` module's approval manager, but that's a developer task. For most implementations, procedural approval with trained staff is sufficient.

**Want email notifications when requests need approval?**

Set up email alerts in **Settings → Technical → Automation → Automated Actions**. Create an action on `spp.drims.request` that triggers when `approval_state` changes to `pending`, and send email to users with the Request Approver role.

**Life-threatening requests aren't being prioritized?**

The life-threatening flag is a visual indicator, not an automatic escalation. Train approvers to:
1. Monitor the dashboard for life-threatening requests
2. Set up email alerts for immediate notification
3. Establish a protocol for 24/7 approval coverage during active disasters

## See Also

- {doc}`/config_guide/drims/index` - DRIMS configuration overview
- {doc}`/config_guide/drims/warehouses` - Warehouse configuration
- {doc}`/user_guide/drims/requests` - User guide for creating requests

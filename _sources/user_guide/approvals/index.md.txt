---
openspp:
  doc_status: draft
  products: [core]
  applies_to:
    - sp_mis
    - drims
---

# Approvals

**Applies to:** SP-MIS, DRIMS

This guide is for **users** who review and approve requests, entitlements, or other items that require authorization before they take effect.

## Overview

OpenSPP uses approval workflows to ensure proper oversight of sensitive operations. Before changes to beneficiary data, payment batches, or supply requests take effect, they must be reviewed and approved by authorized users.

Depending on your organization's configuration, some items may require approval from multiple people at different levels. This is called multi-tier approval. For example, a large payment batch might need approval from a supervisor first, then a finance manager.

## What Gets Approved

| Type | Description | Common In |
|------|-------------|-----------|
| **Change Requests** | Updates to beneficiary information | Social Registry, SP-MIS |
| **Entitlement Batches** | Benefit calculations for a cycle | SP-MIS |
| **Payment Batches** | Payment runs ready for disbursement | SP-MIS |
| **Supply Requests** | Requests for relief supplies | DRIMS |
| **Program Cycles** | Moving cycles to the next stage | SP-MIS |

## Approval Status

Every item that requires approval has a status:

| Status | What It Means |
|--------|---------------|
| **Draft** | Not yet submitted for approval |
| **Pending Approval** | Waiting for someone to review and approve |
| **Revision Requested** | Reviewer asked for changes before approving |
| **Approved** | Approved and ready to take effect |
| **Rejected** | Declined with a reason |

## Who Can Approve

Your administrator configures who can approve different types of items. You can only see and act on items assigned to you or your team.

| Role | What You Can Do |
|------|-----------------|
| **Viewer** | See approval records, but not take action |
| **Approver** | Approve or reject items assigned to you |
| **Manager** | Full access including configuration |

If you cannot see items you expect to approve, check with your administrator about your permissions.

## In This Section

```{toctree}
:maxdepth: 1

manage_approvals
```

## Are You Stuck?

**Cannot see the Approvals menu?**
You need at least Viewer permissions for approvals. Contact your administrator to get access.

**No items in your approval queue?**
Either there are no pending items, or they have been assigned to another approver. Check with your supervisor.

**Need to delegate approvals while you are away?**
Contact your administrator to set up delegation rules.

**Approved or rejected something by mistake?**
Contact your supervisor immediately. Some actions can be reversed, depending on the workflow stage and your organization's policies.

---
openspp:
  doc_status: draft
  products: [core]
---

# Approval tiers

This guide is for **implementers** configuring multi-step approval chains where records must pass through sequential review stages.

## Mental model

Tiers create a sequential approval pipeline:

```
Submit → Tier 1 (Field Office) → Tier 2 (Regional) → Tier 3 (Central) → Approved
```

Each tier must complete before the next tier begins. If any tier rejects, the entire process stops.

## Tier configuration

Each tier within an approval definition has these settings:

| Field | What it means |
|-------|---------------|
| **Tier Name** | Label for this step (e.g., "Field Office Review") |
| **Sequence** | Order in the chain (lower = earlier) |
| **Approver Type** | Who approves at this tier (Group, Users, Manager, Dynamic) |
| **Approval Group** | Security group whose members can approve (if type = Security Group) |
| **Specific Users** | Named approvers (if type = Specific Users) |
| **Require All Approvers** | All designated approvers must approve vs. any one |
| **Minimum Count** | Minimum number of approvals needed (if not requiring all) |
| **Self-approval** | Whether the submitter can approve at this tier |
| **Blocking** | Whether this tier blocks progress (vs. informational/FYI) |
| **SLA Hours** | Time allowed for this tier before escalation |

## Setting up tiers

### Step 1: Open the approval definition

Navigate to **Configuration > Approval Definitions** and open the definition you want to add tiers to.

### Step 2: Add tiers

In the **Tiers** tab:

1. Click **Add a line**
2. Set the **Sequence** (10, 20, 30 for easy reordering)
3. Give the tier a **Name**
4. Select the **Approver Type** and configure the approver

### Step 3: Configure tier behavior

For each tier, decide:

| Decision | Options |
|----------|---------|
| **Who must approve?** | All approvers, or minimum count |
| **Can submitter self-approve?** | Yes or No |
| **Is this blocking?** | Yes (must approve to proceed) or No (FYI only) |
| **SLA deadline?** | Hours before escalation |

## Tier patterns

### Pattern 1: Sequential group approval

Three groups approve in order. Any member of each group can approve.

| Tier | Sequence | Type | Group | Blocking |
|------|----------|------|-------|----------|
| Field Review | 10 | Group | Field Officers | Yes |
| Regional Review | 20 | Group | Regional Managers | Yes |
| Central Approval | 30 | Group | Central Admin | Yes |

### Pattern 2: Parallel review then final approval

Two reviewers work simultaneously, then a director gives final approval.

| Tier | Sequence | Type | Details | Blocking |
|------|----------|------|---------|----------|
| Technical Review | 10 | Specific Users | Tech Lead | Yes |
| Compliance Review | 10 | Specific Users | Compliance Officer | Yes |
| Director Approval | 20 | Specific Users | Program Director | Yes |

```{note}
Tiers with the same sequence number run in parallel. Both must complete before the next sequence begins.
```

### Pattern 3: Review with FYI notification

A manager approves while the finance team is notified (but doesn't need to approve).

| Tier | Sequence | Type | Blocking |
|------|----------|------|----------|
| Manager Approval | 10 | Manager of Submitter | Yes |
| Finance Notification | 10 | Group: Finance | No (FYI) |

## Escalation

When a tier's SLA hours expire without a decision:

1. The system checks the escalation configuration on the parent definition
2. If escalation is configured, the pending approval routes to the escalation target
3. The original approver is notified that the item was escalated

## Are You Stuck?

**Tiers not executing in order?**

Check the **Sequence** values. Lower numbers execute first. Tiers with equal sequence numbers run in parallel.

**Need to skip a tier for certain records?**

Create separate approval definitions with different tier structures for different situations. Use the **Domain** field on each definition to control which records it applies to. You cannot conditionally skip individual tiers.

**Approver rejects at tier 2 - what happens?**

The record is rejected. The submitter can make corrections and resubmit, which restarts the approval from tier 1.

**Can I add a tier after the workflow is already running?**

New tiers apply to future submissions only. Active approval processes continue with the original tier structure.

## Next steps

- {doc}`overview` - Approval workflow fundamentals
- {doc}`batch_approvals` - Batch processing configuration

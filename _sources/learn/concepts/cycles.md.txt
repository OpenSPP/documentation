---
openspp:
  doc_status: draft
  products: [core]
---

# Cycles

**For:** All audiences

A cycle is a single distribution round within a program—typically a week, month, or quarter during which benefits are calculated and paid out. If a program defines "who gets what," a cycle is when beneficiaries actually receive their entitlements.

## What is a cycle?

Think of a cycle as one payment period. For example:

- A monthly cash transfer program runs 12 cycles per year (one per month)
- A quarterly food distribution program runs 4 cycles per year (one per quarter)
- An emergency relief program might run a single cycle (one-time distribution)

Each cycle has:

- **Start and end dates** - When the cycle begins and ends
- **Beneficiaries** - The specific people enrolled for this distribution round
- **Entitlements** - What each beneficiary is entitled to receive
- **State** - Where the cycle is in its lifecycle
- **Payment batches** - How payments are organized and disbursed

## Relationship between programs and cycles

A program can have many cycles, but each cycle belongs to exactly one program.

```{mermaid}
graph TD
    P[Program: Monthly Cash Transfer] --> C1[Cycle 1: January 2025]
    P --> C2[Cycle 2: February 2025]
    P --> C3[Cycle 3: March 2025]
    P --> C4[...]
```

The program defines the rules (eligibility criteria, entitlement formulas, payment methods), while each cycle applies those rules to a specific distribution period.

## Cycle lifecycle

A cycle moves through several states from creation to completion:

```{mermaid}
stateDiagram-v2
    direction LR
    [*] --> Draft: Create cycle
    Draft --> ToApprove: Submit for approval
    Draft --> Cancelled: Cancel
    ToApprove --> Approved: Approve
    ToApprove --> Cancelled: Cancel
    Approved --> Distributed: Mark as distributed
    Distributed --> Ended: Mark as ended
    Ended --> [*]
    Cancelled --> [*]

    Draft: Draft
    ToApprove: To Approve
    Approved: Approved
    Distributed: Distributed
    Ended: Ended
    Cancelled: Cancelled
```

There's also a **Cancelled** state that can be reached from Draft or To Approve if the cycle needs to be stopped.

### State descriptions

| State | Description | What you can do |
|-------|-------------|-----------------|
| **Draft** | Initial state when creating a cycle | Add beneficiaries, prepare entitlements, edit configuration |
| **To approve** | Submitted for approval | Review entitlements, approve or reject the cycle |
| **Approved** | Cycle is approved and ready | Prepare payments, begin distribution |
| **Distributed** | Payments have been sent | Monitor payment status, mark as ended when complete |
| **Ended** | Cycle is complete | View final reports, archive data |
| **Cancelled** | Cycle was stopped | View records, no further actions |

## Cycle operations

### 1. Copy beneficiaries from program

When you start a new cycle, you typically want to include beneficiaries who are already enrolled in the program.

**What it does:**
- Copies program members into the cycle as cycle members
- Creates a snapshot of who is eligible at this moment
- Allows you to add or remove beneficiaries for this specific cycle

**When to use:**
- Starting a new cycle for an ongoing program
- Continuing from previous cycle enrollments

### 2. Check eligibility

Before finalizing beneficiaries, you may want to verify they still meet eligibility criteria.

**What it does:**
- Runs eligibility rules against current beneficiary data
- Updates enrollment status based on current criteria
- Identifies beneficiaries who no longer qualify

**When to use:**
- Before approving a cycle
- When eligibility criteria depend on frequently changing data (income, household size, etc.)
- For programs with conditional eligibility

### 3. Prepare entitlements

Once beneficiaries are confirmed, you calculate what each beneficiary should receive.

**What it does:**
- Applies entitlement formulas to each beneficiary
- Creates entitlement records showing amounts or items
- Calculates totals for budgeting and approval

**When to use:**
- After beneficiaries are confirmed
- Before submitting for approval
- When you need to review what will be distributed

### 4. Submit for approval

When the cycle is ready, submit it for review and approval.

**What it does:**
- Changes state from Draft to To Approve
- Notifies approvers that the cycle needs review
- Locks certain fields to prevent changes during review

**When to use:**
- After beneficiaries are enrolled and entitlements are prepared
- When you're confident the cycle is configured correctly

### 5. Approve cycle

Authorized users review and approve the cycle.

**What it does:**
- Changes state from To Approve to Approved
- May auto-approve individual entitlements (if configured)
- Records who approved and when
- Makes the cycle ready for payment preparation

**When to use:**
- After reviewing beneficiaries and entitlements
- When you're ready to proceed with distribution

### 6. Prepare payments

Convert approved entitlements into payment instructions.

**What it does:**
- Creates payment records for each entitlement
- Organizes payments into batches
- Prepares data for payment service providers

**When to use:**
- After cycle is approved
- Before sending payments
- To review payment details before disbursement

### 7. Send payments

Disburse payments to beneficiaries.

**What it does:**
- Sends payment instructions to payment service providers
- Updates payment status
- Tracks successful and failed payments

**When to use:**
- After payments are prepared and reviewed
- When you're ready to actually disburse funds

### 8. Mark as distributed

Indicate that the distribution is complete.

**What it does:**
- Changes state from Approved to Distributed
- Signals that payments have been sent
- Allows tracking of post-distribution activities

**When to use:**
- After payments have been successfully sent
- Before final reconciliation

### 9. Mark as ended

Close the cycle after all activities are complete.

**What it does:**
- Changes state from Distributed to Ended
- Finalizes the cycle
- Prevents further modifications

**When to use:**
- After all payments are reconciled
- When no further actions are needed for this cycle

## Common cycle patterns

### Monthly cycles

Programs that distribute benefits every month.

**Example:** Monthly cash transfer program
- 12 cycles per year
- Each cycle runs for one month
- Beneficiaries may remain consistent across cycles
- Entitlements are calculated fresh each month

**Typical timeline:**
- Days 1-5: Create cycle, copy beneficiaries
- Days 6-10: Check eligibility, prepare entitlements
- Days 11-15: Review and approve
- Days 16-20: Prepare and send payments
- Days 21-30: Monitor payments, mark distributed and ended

### Quarterly cycles

Programs that distribute benefits four times per year.

**Example:** Seasonal agricultural support program
- 4 cycles per year (one per quarter)
- Each cycle runs for three months
- May align with planting/harvest seasons
- Entitlements may vary by season

**Typical timeline:**
- Week 1: Create cycle, copy beneficiaries
- Week 2-3: Check eligibility, prepare entitlements
- Week 4: Review and approve
- Week 5-6: Prepare and send payments
- Week 7-12: Monitor payments, mark distributed and ended

### One-time cycles

Programs that run a single distribution.

**Example:** Emergency relief program after a natural disaster
- 1 cycle total
- Duration varies (days to weeks)
- Often needs rapid execution
- May require special eligibility verification

**Typical timeline:**
- Day 1-2: Create cycle, enroll beneficiaries (often through rapid assessment)
- Day 3-4: Verify eligibility, prepare entitlements
- Day 5: Approve cycle
- Day 6-7: Prepare and send payments
- Day 8+: Monitor and reconcile payments

### Conditional cycles

Programs where cycles only run when conditions are met.

**Example:** Drought response program
- Cycles triggered by drought indicators
- Irregular frequency (only when needed)
- Beneficiaries verified each cycle
- Entitlements may vary by severity

**Typical pattern:**
- Trigger condition is met (e.g., rainfall below threshold)
- Create cycle with affected area beneficiaries
- Rapid eligibility check and entitlement calculation
- Fast-track approval process
- Quick payment distribution

## Multiple cycles in a program

A program typically runs multiple cycles over its lifetime. Here's how they relate:

### Sequential cycles

Most common pattern - cycles run one after another.

```{mermaid}
graph LR
    C1[Cycle 1: Jan 2025<br/>ended] --> C2[Cycle 2: Feb 2025<br/>ended]
    C2 --> C3[Cycle 3: Mar 2025<br/>distributed]
    C3 --> C4[Cycle 4: Apr 2025<br/>draft]
    style C4 fill:#fff3cd
```

**Key points:**
- Previous cycles are complete before starting the next
- Lessons learned from one cycle inform the next
- Historical data builds up over time

### Overlapping cycles

Some programs have cycles that overlap in preparation.

```{mermaid}
gantt
    title Overlapping Cycle Timeline
    dateFormat YYYY-MM
    section Cycle 1
        Preparation    :c1prep, 2024-12, 1M
        Distribution   :c1dist, 2025-01, 1M
        Completion     :c1comp, 2025-02, 1M
    section Cycle 2
        Preparation    :c2prep, 2025-01, 1M
        Distribution   :c2dist, 2025-02, 1M
        Completion     :c2comp, 2025-03, 1M
```

**Key points:**
- Allows continuous pipeline of work
- Requires careful coordination
- Reduces gaps between distributions

### Parallel cycles

Different beneficiary groups may have separate concurrent cycles.

```{mermaid}
graph TD
    P[Program: Regional Support<br/>January 2025] --> C1A[Cycle 1A<br/>Region North]
    P --> C1B[Cycle 1B<br/>Region South]
```

**Key points:**
- Different beneficiary populations
- May have different approval chains
- Requires careful tracking

## Are you stuck?

### Why can't I edit my cycle?

**Possible reasons:**
- The cycle state doesn't allow edits (To Approve, Approved, Distributed, or Ended)
- The cycle is locked due to background processing
- You don't have permission to edit cycles in this program

**Solution:**
- Check the cycle state - only Draft cycles can be freely edited
- Wait for background jobs to complete if locked
- Contact your program administrator for permissions

### Why don't I see any beneficiaries in my cycle?

**Possible reasons:**
- You haven't copied beneficiaries from the program yet
- The program has no enrolled members
- Eligibility check removed all beneficiaries

**Solution:**
- Use "Copy Beneficiaries from Program" button
- Check that the program has enrolled members
- Review eligibility criteria if beneficiaries were removed

### Why are entitlements zero or incorrect?

**Possible reasons:**
- Entitlements haven't been prepared yet
- Entitlement formulas have errors
- Required data is missing from beneficiary records

**Solution:**
- Click "Prepare Entitlements" button
- Review entitlement manager configuration
- Check that beneficiaries have all required data fields
- Test formulas with sample beneficiary data

### Why can't I approve the cycle?

**Possible reasons:**
- Cycle is not in "To Approve" state
- You don't have approval permissions
- There are validation errors

**Solution:**
- Submit the cycle for approval first (if in Draft state)
- Check with program administrator about permissions
- Review any error messages and fix issues

### What happens if I cancel a cycle?

**Effects:**
- Cycle state changes to Cancelled
- No payments will be processed
- Entitlements are cancelled
- Data is preserved for records

**Note:** You can only cancel Draft or To Approve cycles. Once approved and distributed, cycles cannot be cancelled.

## Next steps

**Learn more about concepts:**
- {doc}`programs` - The parent container for cycles
- {doc}`eligibility` - Rules that determine who qualifies
- {doc}`entitlements` - What beneficiaries receive
- {doc}`payments` - How benefits are disbursed

**For configuration:**
- See the Configuration Guide for setting up cycles

**For developers:**
- See the Developer Guide for custom cycle managers

---
openspp:
  doc_status: draft
  products: [core]
---

# Entitlements

An entitlement is a specific benefit that a beneficiary is entitled to receive in a particular cycle. It represents what each person or household should get—whether cash, vouchers, or physical goods.

**For:** All audiences

## What is an entitlement?

An entitlement is a record that specifies:

- **Who** receives the benefit (the beneficiary)
- **What** they receive (amount or items)
- **When** it's valid (validity period)
- **Status** (draft, approved, paid, etc.)

**Examples:**

| Program | Entitlement |
|---------|-------------|
| Monthly cash transfer | $50 cash payment |
| Food assistance | 10kg rice + 2L cooking oil |
| School feeding | Daily meal voucher |
| Agricultural support | Seeds (5kg) + fertilizer (25kg) |

## Entitlements vs. benefits

| Concept | Meaning |
|---------|---------|
| **Benefit** | What the program offers (defined in policy) |
| **Entitlement** | What a specific beneficiary receives in a specific cycle |

A benefit is the general definition; an entitlement is the concrete instance for a particular person and time period.

## Entitlement types

### Cash entitlements

Monetary payments to beneficiaries:

| Field | Description |
|-------|-------------|
| **Initial amount** | The calculated payment amount |
| **Transfer fee** | Any fees deducted (if applicable) |
| **Currency** | Payment currency |
| **Balance** | Remaining amount (for partial payments) |

Cash entitlements are processed through the payment system and can be delivered via:
- Bank transfer
- Mobile money
- Cash pickup
- Other payment channels

### In-kind entitlements

Physical goods or commodities:

| Field | Description |
|-------|-------------|
| **Product** | The item to be distributed |
| **Quantity** | Amount of the product |
| **Unit of measure** | How quantity is measured (kg, pieces, etc.) |
| **Warehouse** | Source location for inventory |

In-kind entitlements integrate with inventory management for:
- Stock tracking
- Distribution planning
- Delivery confirmation

### Voucher entitlements

Redeemable tokens for goods or services:

| Field | Description |
|-------|-------------|
| **Voucher code** | Unique redemption code |
| **Value** | Monetary or item value |
| **Valid until** | Expiration date |
| **Redemption points** | Where voucher can be used |

## Entitlement lifecycle

```{mermaid}
stateDiagram-v2
    direction LR
    [*] --> Draft: Prepare entitlements
    Draft --> PendingApproval: Submit for approval
    PendingApproval --> Approved: Approve
    PendingApproval --> Rejected: Reject
    Approved --> Transferred: Transfer to FSP
    Transferred --> Paid: Confirm payment
    Approved --> Cancelled: Cancel
    Draft --> Cancelled: Cancel
    Approved --> Expired: Validity expires

    Draft: Draft
    PendingApproval: Pending Approval
    Approved: Approved
    Transferred: Transferred to FSP
    Paid: Paid to Beneficiary
    Rejected: Rejected
    Cancelled: Cancelled
    Expired: Expired
```

### Entitlement states

| State | Description | Next steps |
|-------|-------------|------------|
| **Draft** | Created but not submitted | Review, edit, submit for approval |
| **Pending Approval** | Awaiting approval | Approve or reject |
| **Approved** | Ready for payment | Transfer to payment provider |
| **Transferred to FSP** | Sent to financial service provider | Await payment confirmation |
| **Paid to Beneficiary** | Successfully delivered | Complete |
| **Rejected** | Declined | Review reason, may recreate |
| **Cancelled** | Manually cancelled | No further action |
| **Expired** | Validity period passed | May need new entitlement |

### Rejection reasons

| Rejection type | Description |
|---------------|-------------|
| **Beneficiary declined** | Recipient didn't want the entitlement |
| **Account doesn't exist** | Payment account invalid |
| **Other reason** | Other issues (documented in notes) |

## How entitlements are created

### The entitlement manager

The entitlement manager calculates what each beneficiary receives. OpenSPP supports multiple manager types:

| Manager type | Description | Use Case |
|-------------|-------------|----------|
| **Cash** | Fixed or calculated monetary amounts | Cash transfer programs |
| **In-kind** | Physical goods from inventory | Food distribution |
| **Default** | Simple fixed amounts | Basic programs |
| **CEL-based** | Complex calculations using expressions | Variable benefits |

### Entitlement calculation flow

```{mermaid}
graph TD
    C[Cycle with beneficiaries] --> E[Entitlement Manager]
    E --> R[For each beneficiary]
    R --> I[Apply entitlement items/rules]
    I --> A[Calculate amount/quantity]
    A --> |Condition met| EN[Create entitlement]
    A --> |Condition not met| S[Skip]
    EN --> D[Draft entitlement ready]

    style E fill:#fff3e0
    style EN fill:#e8f5e9
```

### Entitlement items

Entitlement managers can have multiple items with conditions:

| Item | Condition | Amount |
|------|-----------|--------|
| Base amount | (none - all beneficiaries) | $30 |
| Per child under 5 | `children_under_5 > 0` | $10 per child |
| Elderly supplement | `has_elderly_member == true` | $5 |

**Example calculation:**
```
Household: 2 children under 5, 1 elderly member
= $30 (base) + $20 (2 × $10) + $5 (elderly)
= $55 total entitlement
```

### CEL-Based calculations

For complex calculations, use CEL expressions:

```cel
# Fixed amount
30.0

# Per-member calculation
10.0 * members.size()

# Conditional calculation
me.has_disability ? 50.0 : 30.0

# Complex formula
base_amount + (children_under_5 * child_rate) + (is_femaleheaded ? fhh_bonus : 0)
```

## Entitlement approval

### Why approval matters

Approval ensures:
- Amounts are correctly calculated
- Beneficiaries are properly verified
- Budget is available
- Audit trail exists

### Approval workflow

```{mermaid}
graph LR
    D[Draft] --> S[Submit]
    S --> R{Review}
    R --> |Valid| A[Approve]
    R --> |Issues| RJ[Reject]
    RJ --> D
    A --> P[Ready for payment]

    style A fill:#e8f5e9
    style RJ fill:#ffebee
```

### Bulk approval

For efficiency, entitlements can be approved in bulk:
- By cycle (approve all in a cycle)
- By selection (approve selected records)
- Automatic (if configured, based on rules)

## Entitlement data

### Key fields

| Field | Description |
|-------|-------------|
| **Code** | Unique entitlement identifier |
| **ERN** | Entitlement Reference Number (generated on approval) |
| **Partner** | The beneficiary (registrant) |
| **Cycle** | The distribution cycle |
| **Program** | The parent program |
| **Initial amount** | Calculated benefit amount |
| **Valid from/until** | Validity period |
| **State** | Current lifecycle state |

### Validity period

Entitlements have a validity window:

| Field | Purpose |
|-------|---------|
| **Valid from** | When entitlement becomes active |
| **Valid until** | When entitlement expires |

Expired entitlements cannot be paid. The validity period allows for:
- Delayed payment collection
- Scheduled distributions
- Grace periods

## Working with entitlements

### Preparing entitlements

From a cycle, click "Prepare Entitlements" to:

1. Run the entitlement manager
2. Calculate amounts for all cycle members
3. Create draft entitlement records
4. Apply any conditions or formulas

### Reviewing entitlements

Before approval, review:
- Total amounts and counts
- Individual entitlement details
- Any flagged issues
- Budget availability

### Modifying entitlements

In draft state, you can:
- Adjust amounts manually
- Change validity dates
- Add notes
- Cancel if not needed

After approval, modifications require:
- Cancellation and recreation, or
- Administrative override (if permitted)

## Best practices

### Calculation design

| Practice | Reason |
|----------|--------|
| **Keep formulas simple** | Easier to audit and explain |
| **Document conditions** | Clear rationale for variations |
| **Test with sample data** | Verify calculations before bulk creation |
| **Use standard rates** | Consistency across beneficiaries |

### Approval process

| Practice | Reason |
|----------|--------|
| **Separate preparer/approver** | Segregation of duties |
| **Review before bulk approval** | Catch errors early |
| **Document rejections** | Clear audit trail |
| **Set appropriate validity** | Match distribution timeline |

### Data quality

| Practice | Reason |
|----------|--------|
| **Verify beneficiary data** | Accurate calculations depend on it |
| **Check for duplicates** | Prevent double payments |
| **Validate amounts** | Catch outliers and errors |
| **Monitor rejection rates** | Identify systematic issues |

## Are you stuck?

### Why are entitlements $0 or missing?

**Possible causes:**
- Entitlement items not configured
- Conditions exclude all beneficiaries
- Required data fields are empty
- Formula errors

**Solutions:**
1. Check entitlement manager configuration
2. Verify item conditions match beneficiary data
3. Test conditions with sample beneficiaries
4. Review calculation formulas

### Why can't I approve entitlements?

**Possible causes:**
- Not in "Pending Approval" state
- Missing approval permissions
- Validation errors exist

**Solutions:**
1. Submit entitlements for approval first
2. Check your user group/role
3. Review error messages
4. Contact program administrator

### How do I change an approved entitlement?

**Options:**
1. **Cancel and recreate** - Cancel the entitlement, create a new one
2. **Adjustment entitlement** - Create a supplementary entitlement (positive or negative)
3. **Administrative override** - If permitted by your role

### Why is my entitlement expired?

The entitlement's "Valid Until" date has passed. Expired entitlements cannot be paid.

**Solutions:**
1. Create a new entitlement with updated validity
2. Extend validity before expiration (if in draft/approved state)
3. Review validity period settings in entitlement manager

### How do I handle partial payments?

If a beneficiary received partial payment:
1. The balance field tracks remaining amount
2. Additional payments can be made against the same entitlement
3. Mark as fully paid when complete

## Next steps

**Learn more about concepts:**
- {doc}`cycles` - Where entitlements are created
- {doc}`programs` - How entitlement managers are configured
- {doc}`payments` - How entitlements become payments

**For configuration:**
- See the Configuration Guide for setting up entitlement managers

**For developers:**
- See the Developer Guide for creating custom entitlement managers

---
openspp:
  doc_status: draft
---

# Payments

Payments are the final step in benefit delivery—converting approved entitlements into actual disbursements to beneficiaries. OpenSPP manages the full payment lifecycle from preparation through reconciliation.

**For:** All audiences

## What is a Payment?

A payment is a record of an actual or attempted disbursement:

| Field | Description |
|-------|-------------|
| **Entitlement** | The approved benefit being paid |
| **Beneficiary** | Who receives the payment |
| **Amount Issued** | The payment amount |
| **Account Number** | Payment destination |
| **Status** | Paid, failed, or pending |

## Payments vs. Entitlements

| Concept | Purpose |
|---------|---------|
| **Entitlement** | What the beneficiary should receive (approved benefit) |
| **Payment** | The actual disbursement transaction |

One entitlement can have multiple payment attempts (if initial attempts fail) or partial payments.

## Payment Lifecycle

```{mermaid}
stateDiagram-v2
    [*] --> Issued: Prepare payments
    Issued --> Sent: Send to FSP
    Sent --> Reconciled: Receive confirmation

    state Reconciled {
        [*] --> Paid: Success
        [*] --> Failed: Error
    }

    Paid --> [*]
    Failed --> Issued: Retry
```

### Payment States

| State | Description | Next Steps |
|-------|-------------|------------|
| **Issued** | Payment created, ready to send | Send to payment provider |
| **Sent** | Transmitted to financial service provider | Await confirmation |
| **Reconciled** | Response received | Check status (paid/failed) |

### Payment Status

After reconciliation, payments have a final status:

| Status | Meaning | Action |
|--------|---------|--------|
| **Paid** | Successfully delivered | Complete |
| **Failed** | Could not be delivered | Investigate and retry |

## Payment Batches

Payments are organized into batches for efficient processing:

```{mermaid}
graph TD
    C[Cycle] --> B1[Batch 1<br/>500 payments]
    C --> B2[Batch 2<br/>500 payments]
    C --> B3[Batch 3<br/>250 payments]

    B1 --> FSP[Financial Service Provider]
    B2 --> FSP
    B3 --> FSP

    style C fill:#e3f2fd
    style FSP fill:#e8f5e9
```

### Why Batches?

| Benefit | Description |
|---------|-------------|
| **Manageable size** | Easier to track and troubleshoot |
| **Parallel processing** | Multiple batches can process simultaneously |
| **Error isolation** | Problems in one batch don't affect others |
| **Reporting** | Clear statistics per batch |

### Batch Configuration

| Setting | Description |
|---------|-------------|
| **Max Batch Size** | Maximum payments per batch (default: 500) |
| **Batch Tags** | Categories for organizing batches |
| **Auto-create** | Automatically create batches from entitlements |

### Batch Statistics

Each batch tracks:

| Metric | Description |
|--------|-------------|
| **Issued transactions** | Payments created |
| **Issued amount** | Total value issued |
| **Sent transactions** | Payments transmitted |
| **Paid transactions** | Successful payments |
| **Paid amount** | Total value delivered |
| **Failed transactions** | Unsuccessful payments |
| **Failed amount** | Value not delivered |

## Payment Flow

### 1. Prepare Payments

Convert approved entitlements into payment records:

```{mermaid}
graph LR
    E[Approved<br/>Entitlements] --> P[Prepare<br/>Payments]
    P --> R[Payment<br/>Records]
    R --> B[Organize<br/>into Batches]

    style E fill:#e3f2fd
    style R fill:#fff3e0
    style B fill:#f3e5f5
```

**What happens:**
- Creates payment records for each entitlement
- Captures beneficiary account information
- Organizes into batches based on configuration
- Sets initial amount from entitlement

### 2. Send Payments

Transmit batches to financial service providers:

**What happens:**
- Batch is marked as started
- Payments are sent to payment gateway/FSP
- State changes from "Issued" to "Sent"
- External reference numbers are recorded

### 3. Reconcile Payments

Receive and process payment confirmations:

**What happens:**
- FSP returns payment status
- Successful payments marked as "Paid"
- Failed payments marked for investigation
- Entitlement status is updated
- Statistics are calculated

## Payment Manager

The Payment Manager controls how payments are processed:

| Manager Type | Description |
|-------------|-------------|
| **Default** | File-based export for manual processing |
| **Bank Integration** | Direct API to banking systems |
| **Mobile Money** | Integration with mobile wallet providers |
| **Custom** | Developer-defined payment logic |

### Manager Configuration

| Setting | Purpose |
|---------|---------|
| **Auto-create batch** | Automatically batch payments |
| **Batch tags** | Categorization rules |
| **Validation rules** | Account validation before sending |

## Payment Methods

OpenSPP supports multiple payment channels:

### Bank Transfer

| Aspect | Details |
|--------|---------|
| **Data required** | Bank account number, bank code |
| **Processing** | Batch file or API |
| **Confirmation** | Bank reconciliation file |

### Mobile Money

| Aspect | Details |
|--------|---------|
| **Data required** | Mobile phone number |
| **Processing** | API integration |
| **Confirmation** | Real-time or webhook |

### Cash Pickup

| Aspect | Details |
|--------|---------|
| **Data required** | ID document, pickup location |
| **Processing** | Voucher/code generation |
| **Confirmation** | Point-of-sale confirmation |

### Vouchers

| Aspect | Details |
|--------|---------|
| **Data required** | Redemption location |
| **Processing** | Voucher printing/digital |
| **Confirmation** | Merchant redemption |

## Handling Payment Failures

### Common Failure Reasons

| Reason | Description | Resolution |
|--------|-------------|------------|
| **Invalid account** | Account doesn't exist | Update beneficiary data |
| **Inactive account** | Account is closed/dormant | Get new account details |
| **Incorrect details** | Name/number mismatch | Verify and correct |
| **Insufficient funds** | Program account underfunded | Add funds |
| **Technical error** | System/network issue | Retry |

### Recovery Process

```{mermaid}
graph TD
    F[Failed Payment] --> I[Investigate]
    I --> |Data issue| U[Update Data]
    I --> |Technical| R[Retry]
    I --> |Permanent| C[Cancel & Create New]
    U --> R
    R --> S[Send Again]
    C --> N[New Entitlement]

    style F fill:#ffebee
    style S fill:#e8f5e9
```

### Retry Workflow

1. **Identify failures** - Filter payments by failed status
2. **Investigate cause** - Check error messages
3. **Correct data** - Update account information if needed
4. **Reset state** - Move payment back to "Issued"
5. **Retry** - Include in new batch

## Payment Security

### Data Protection

| Measure | Purpose |
|---------|---------|
| **Account encryption** | Protect payment details |
| **Access control** | Limit who can process payments |
| **Audit logging** | Track all payment actions |

### Fraud Prevention

| Control | Description |
|---------|-------------|
| **Duplicate detection** | Prevent double payments |
| **Amount limits** | Flag unusual amounts |
| **Approval workflow** | Require authorization |
| **Reconciliation** | Match sent vs. received |

## Reporting

### Payment Reports

| Report | Contents |
|--------|----------|
| **Payment summary** | Totals by status |
| **Batch status** | Progress of each batch |
| **Failure analysis** | Breakdown of failures |
| **Reconciliation** | Matching with FSP records |

### Key Metrics

| Metric | Description |
|--------|-------------|
| **Payment success rate** | % of payments that succeed |
| **Average processing time** | Time from issue to paid |
| **Failure rate by type** | Which errors are most common |
| **Amount disbursed** | Total value delivered |

## Best Practices

### Preparation

| Practice | Reason |
|----------|--------|
| **Validate accounts first** | Reduce failures |
| **Verify amounts** | Catch errors early |
| **Test with small batch** | Confirm integration works |
| **Document process** | Clear procedures |

### Processing

| Practice | Reason |
|----------|--------|
| **Process in batches** | Manageable, traceable |
| **Monitor progress** | Catch issues early |
| **Keep records** | Audit trail |
| **Have fallback** | Alternative if FSP fails |

### Reconciliation

| Practice | Reason |
|----------|--------|
| **Reconcile promptly** | Timely failure handling |
| **Investigate all failures** | Understand root causes |
| **Update beneficiary data** | Reduce future failures |
| **Report discrepancies** | Catch fraud/errors |

## Are You Stuck?

### Why are payments failing?

**Common causes:**
- Invalid or outdated account numbers
- Mismatched beneficiary names
- FSP technical issues
- Insufficient program funds

**Debug steps:**
1. Check failure message/code
2. Verify beneficiary account data
3. Confirm FSP connectivity
4. Check program journal balance

### How do I retry failed payments?

1. Go to Payment Batches
2. Filter for failed payments
3. Correct any data issues
4. Create new batch with failed payments
5. Send the new batch

### Can I cancel a payment?

**If state is "Issued"** (not yet sent):
- Yes, you can delete the payment record

**If state is "Sent":**
- Cannot cancel in OpenSPP
- Must coordinate with FSP to reverse

### How do I handle partial payments?

If a beneficiary should receive payment in installments:
1. Create separate entitlements for each installment, or
2. Process multiple payments against same entitlement
3. Track balance remaining on entitlement

### Why don't I see payment options?

Payment features only appear for cash entitlement programs. Check:
- Is the entitlement manager a Cash type?
- Is the journal configured on the program?
- Do you have payment manager permissions?

## Next Steps

**Learn more about concepts:**
- {doc}`entitlements` - What payments are based on
- {doc}`cycles` - Where payment processing happens
- {doc}`programs` - How payment managers are configured

**For configuration:**
- See the Configuration Guide for setting up payment managers and FSP integrations

**For developers:**
- See the Developer Guide for creating custom payment managers

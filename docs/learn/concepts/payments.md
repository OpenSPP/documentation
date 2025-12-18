---
openspp:
  doc_status: draft
---

# Payments

Payments are the final step in the social protection delivery chain - the actual transfer of benefits from the program to beneficiaries. While {doc}`entitlements` represent what a beneficiary is entitled to receive, payments represent the execution of that entitlement through actual disbursement.

**For:** All audiences

Understanding how payments work is essential for anyone involved in delivering social protection programs, whether you're distributing benefits, managing programs, or integrating payment systems.

## What Are Payments?

A **payment** is the physical or digital transfer of benefits to a beneficiary. It transforms an approved entitlement into actual value that the beneficiary can use.

The relationship between entitlements and payments:

- **Entitlement** - "The Santos family should receive 3,000 PHP for January 2025"
- **Payment** - "3,000 PHP was transferred to the Santos family's account on January 15, 2025"

One entitlement can generate one or more payments, depending on your payment process. For example, if a bank transfer fails, you might retry it, creating a second payment attempt for the same entitlement.

## The Payment Flow

Understanding the complete payment flow helps you see how entitlements become actual benefits in beneficiaries' hands.

### 1. Entitlement Generation

After a {doc}`cycle <cycles>` runs and eligibility is determined, the system generates entitlement records. Each entitlement specifies:
- Who should receive benefits (the beneficiary)
- How much they should receive
- For which cycle period

At this stage, no money has moved. Entitlements are like IOUs waiting to be paid.

### 2. Payment Batch Creation

To efficiently process many payments at once, entitlements are grouped into **payment batches**. A batch is a collection of payments that will be processed together through the same payment method.

For example, you might create:
- A batch of 500 bank transfers to be sent to ABC Bank
- A batch of 200 mobile money transfers via GCash
- A batch of 50 cash distributions at Barangay Service Point

Batching allows you to:
- Process payments efficiently in bulk
- Track groups of payments together
- Submit files to payment service providers
- Reconcile payments as a unit

### 3. Payment Disbursement

Disbursement is when the payment is actually executed - money leaves the program and reaches the beneficiary (or an intermediary like a service point).

The disbursement process varies by payment method:
- **Bank transfers** - A payment file is sent to the bank, which processes the transfers
- **Mobile money** - An API call initiates the transfer to the beneficiary's mobile wallet
- **Cash at service point** - Funds are allocated to a service point, which physically distributes cash
- **Vouchers** - Vouchers are generated and distributed to beneficiaries

### 4. Payment Reconciliation

After disbursement, the payment needs to be reconciled - confirming that the intended payment was actually completed successfully.

Reconciliation involves:
- Matching payment records with bank confirmations or receipts
- Identifying failed or bounced payments
- Tracking which beneficiaries successfully received funds
- Updating payment statuses

### 5. Payment Verification

The final step is verifying that the beneficiary actually received the payment. This can happen through:
- Automated confirmations (SMS from mobile money provider)
- Beneficiary signatures or receipts at service points
- Follow-up surveys or spot checks
- Grievance system monitoring for non-receipt complaints

## Payment Methods

OpenSPP supports multiple payment methods to match how benefits are actually delivered in different contexts.

### Cash Transfer

Cash payments are physical currency distributed to beneficiaries. This method is common in areas with limited banking infrastructure or for populations without bank accounts.

**How it works**:
1. Program allocates cash to designated service points
2. Beneficiaries visit the service point during distribution period
3. Staff verify beneficiary identity
4. Cash is counted and handed to beneficiary
5. Beneficiary signs receipt or provides fingerprint
6. Service point reconciles distributed cash with allocation

**Advantages**:
- No bank account required
- Immediate access to funds
- Works in areas without digital infrastructure
- Familiar and trusted by beneficiaries

**Challenges**:
- Security risks (theft, robbery)
- Requires secure transport of cash
- More labor-intensive to distribute
- Harder to track and reconcile
- Can involve long queues at distribution points

### Bank Transfer

Electronic transfers directly to beneficiary bank accounts are efficient for populations with banking access.

**How it works**:
1. Payment batch generates a bank transfer file
2. File is submitted to the bank (often in a standard format like NACHA or ISO 20022)
3. Bank processes transfers to individual accounts
4. Bank returns confirmation file with success/failure status
5. System reconciles confirmations against original payment batch

**Advantages**:
- Secure and traceable
- Efficient for large volumes
- No cash handling needed
- Beneficiaries access funds through normal banking
- Reduces transport and security costs

**Challenges**:
- Requires beneficiaries to have bank accounts
- May involve bank fees
- Failed transfers need investigation (wrong account number, closed account, etc.)
- Some beneficiaries may not trust banks or have access

### Mobile Money

Mobile money transfers to beneficiary mobile wallets (like GCash, M-Pesa, or PayMaya) combine digital efficiency with accessibility.

**How it works**:
1. Payment batch triggers API calls to mobile money provider
2. Provider transfers funds to registered mobile numbers
3. Beneficiaries receive SMS notification
4. Funds available immediately in mobile wallet
5. Provider returns transaction confirmations
6. System reconciles based on provider responses

**Advantages**:
- Very accessible - only needs a mobile phone
- Fast and efficient
- Lower fees than traditional banking
- Good digital trail for reconciliation
- Beneficiaries can use funds via mobile payment or cash out at agents

**Challenges**:
- Requires mobile phone ownership and basic digital literacy
- Network coverage needed in beneficiary areas
- Mobile money agent liquidity issues in remote areas
- Transaction limits may apply
- Some populations may not be familiar with mobile money

### Vouchers

Vouchers are documents (paper or digital) that beneficiaries can exchange for cash or specific goods/services.

**Types of vouchers**:
- **Cash vouchers** - Can be exchanged for cash at designated locations
- **Commodity vouchers** - Can be exchanged for specific items (food, supplies)
- **Restricted vouchers** - Can only be used with certain merchants or for certain categories

**How it works**:
1. System generates vouchers with unique codes
2. Vouchers are printed or sent digitally (SMS, app)
3. Beneficiaries present vouchers at authorized locations
4. Merchants/agents verify voucher validity
5. Value is redeemed (cash given or goods provided)
6. Vouchers are marked as redeemed in the system
7. Merchants submit vouchers for reimbursement

**Advantages**:
- Can restrict spending to intended purposes (food, education, etc.)
- No bank account needed
- Can work with local merchants to stimulate economy
- Provides choice within constraints
- Good for in-kind or restricted cash programs

**Challenges**:
- Risk of fraud or duplication (especially paper vouchers)
- Merchant participation and training needed
- Reconciliation and reimbursement process required
- Limited to areas with participating merchants
- May have security features needed (watermarks, QR codes)

## Service Points

**Service points** are physical locations where payments are distributed to beneficiaries. They're critical infrastructure for cash-based programs and voucher distribution.

### What Is a Service Point?

A service point is a designated location where:
- Funds or vouchers are made available to beneficiaries
- Staff verify beneficiary identity
- Payments are physically distributed
- Receipts and records are collected

Common service point types:
- Government offices (barangay halls, municipal buildings)
- Schools or community centers
- Temporary distribution sites
- Post offices
- Partner organization offices
- Mobile service points (for remote areas)

### Service Point Operations

**Fund Allocation**:
Before distribution, funds must be allocated to the service point. This involves:
- Determining how much each service point needs based on beneficiaries assigned to it
- Securing and transporting cash to the service point
- Recording the allocation in the system
- Ensuring proper security and custody

**Distribution Process**:
During distribution:
1. Beneficiary arrives and joins queue
2. Staff verify identity (ID, biometrics, or other method)
3. Staff look up beneficiary in system or list
4. Staff confirm entitlement amount
5. Cash is counted and given to beneficiary
6. Beneficiary signs receipt or provides confirmation
7. Payment is marked as distributed in system

**Reconciliation**:
After distribution:
- Count remaining cash
- Compare distributed amounts with remaining funds
- Match signed receipts with payment records
- Report discrepancies for investigation
- Return unspent funds if applicable

### Service Point Management

Effective service point operations require:

**Staff training**:
- Identity verification procedures
- Using the payment system or distribution lists
- Cash handling and security protocols
- Dealing with disputes or questions
- Recording keeping requirements

**Security measures**:
- Secure storage for cash before and during distribution
- Multiple staff for cash handling (no single person unsupervised)
- Security personnel if needed
- Cameras or monitoring where possible
- Defined protocols for incidents

**Beneficiary management**:
- Clear communication about when and where to collect
- Organized queuing system
- Provisions for elderly or disabled beneficiaries
- Language support if needed
- Grievance handling at the service point

## Payment States

Payments move through different states as they're processed. Understanding these states helps you track payment progress and identify issues.

### Common Payment States

**Draft/Pending**:
- Payment has been created but not yet processed
- Can still be edited or cancelled
- No funds have been disbursed

**Submitted/In Process**:
- Payment has been submitted to payment provider (bank, mobile money, etc.)
- Waiting for processing to complete
- Cannot be cancelled easily

**Completed/Paid**:
- Payment has been successfully disbursed
- Beneficiary should have access to funds
- Confirmed by payment provider

**Failed**:
- Payment attempt was unsuccessful
- Reasons might include: invalid account, insufficient funds, technical error
- Requires investigation and possibly retry or alternative method

**Reconciled**:
- Payment has been matched with confirmation records
- Verified that beneficiary received the payment
- Ready for reporting and closure

**Cancelled**:
- Payment was cancelled before disbursement
- Funds returned to program (if applicable)
- May need to create new payment

**Bounced/Returned**:
- Payment was sent but returned by recipient's bank or provider
- Common reasons: closed account, incorrect details
- Needs correction and resubmission

### State Transitions

Typical progression for a successful payment:
```
Draft → Submitted → Completed → Reconciled
```

For a failed payment that's retried:
```
Draft → Submitted → Failed → (corrected) → Draft → Submitted → Completed → Reconciled
```

## Payment Reconciliation

**Reconciliation** is the process of ensuring that payments were actually completed as intended and matching payment records with external confirmations.

### Why Reconciliation Matters

Without proper reconciliation:
- You don't know if beneficiaries actually received funds
- Fraud or errors may go undetected
- Financial reports are unreliable
- Audit trails are incomplete
- Problems accumulate and become harder to fix

### What Gets Reconciled

**Payment records vs. provider confirmations**:
- Match each payment in your system with a confirmation from the bank, mobile money provider, or service point
- Identify any payments that were sent but not confirmed
- Identify any confirmations that don't match a payment record

**Amounts**:
- Verify that the amount sent matches what was confirmed
- Check that fees or deductions match expectations
- Ensure totals add up correctly

**Timing**:
- Track when payments were initiated vs. when they completed
- Identify delayed payments
- Monitor whether payments are within expected timeframes

**Beneficiary confirmation**:
- Beyond provider confirmation, verify beneficiary actually received funds
- Use receipts, signatures, biometrics, or follow-up surveys
- Track complaints about non-receipt

### Reconciliation Process

1. **Collect confirmation data**:
   - Bank confirmation files
   - Mobile money transaction reports
   - Service point distribution lists with signatures
   - Provider status updates via API

2. **Match records**:
   - Automatically match using transaction IDs or reference numbers
   - Manually review unmatched items
   - Update payment states based on confirmations

3. **Investigate discrepancies**:
   - Failed payments - Why did they fail? Can they be retried?
   - Missing confirmations - Was payment lost in processing?
   - Unexpected confirmations - Is there an error in records?
   - Amount mismatches - Were fees not accounted for?

4. **Resolve issues**:
   - Retry failed payments with corrections
   - Contact payment providers for missing confirmations
   - Adjust records if errors found
   - Create new payments if originals are lost

5. **Document and report**:
   - Record reconciliation results
   - Generate reports on payment success rates
   - Track unresolved items for follow-up
   - Prepare data for audits

## Payment Verification and Receipts

Beyond system reconciliation, verifying that the intended beneficiary received the payment is important for accountability and detecting fraud.

### Verification Methods

**Electronic receipts**:
- SMS confirmation sent to beneficiary
- Email receipt with transaction details
- In-app notification with payment record
- Digital signature captured on tablet

**Physical receipts**:
- Signed paper receipt at service point
- Thumbprint on distribution list
- Photo of beneficiary receiving payment
- Pre-signed acknowledgment form

**Post-distribution verification**:
- Phone surveys asking beneficiaries to confirm receipt
- Spot checks at beneficiary homes
- Community monitoring and feedback
- Grievance system monitoring for complaints

### Receipt Information

A good payment receipt includes:
- Beneficiary name and ID number
- Program and cycle information
- Payment amount
- Payment date
- Payment method
- Transaction reference number
- Who distributed the payment (for service points)
- Beneficiary signature or confirmation

This creates an audit trail and helps resolve disputes about whether payment occurred.

### Handling Non-Receipt Issues

If a beneficiary reports not receiving a payment:

1. **Check payment status**:
   - Was payment marked as completed?
   - Is there a confirmation from provider?
   - Was it sent to correct account/phone/location?

2. **Verify beneficiary information**:
   - Is account number or phone number correct?
   - Did beneficiary check all their accounts?
   - Did mobile money agent have liquidity?

3. **Investigate with provider**:
   - Request transaction details from bank or mobile money
   - Check if payment is pending or delayed
   - Determine if there was a technical issue

4. **Take corrective action**:
   - If payment failed, create new payment
   - If details were wrong, update and resend
   - If fraud suspected, investigate before retrying
   - Document the issue and resolution

## Payment Security and Fraud Prevention

Payments are a common target for fraud, so security measures are essential.

### Common Fraud Risks

- Ghost beneficiaries (fake registrations receiving payments)
- Identity theft (someone else collecting payment meant for real beneficiary)
- Collusion between staff and beneficiaries to inflate amounts
- Diversion of funds before reaching beneficiaries
- Duplicate payments to same beneficiary
- Manipulation of bank account or phone numbers to redirect payments

### Security Measures

**Identity verification**:
- Check photo ID against beneficiary record
- Use biometrics (fingerprint, facial recognition) where available
- Require beneficiary to answer security questions
- Cross-check with family or community members

**System controls**:
- Segregation of duties (different people approve and disburse)
- Audit trails of all payment actions
- Alerts for unusual patterns (duplicate accounts, multiple payments)
- Regular reconciliation and monitoring

**Physical security**:
- Secure transport and storage of cash
- Multiple staff present during distribution
- Cameras at service points
- Security personnel where needed

**Beneficiary education**:
- Inform beneficiaries of their entitlement amounts
- Tell them when to expect payments
- Encourage reporting of non-receipt or incorrect amounts
- Establish accessible grievance channels

## Linking to Operational Details

This document covers the conceptual understanding of payments. For operational guidance on actually processing and managing payments in OpenSPP, see:

- {doc}`/user_guide/payments/index` - Complete payment processing guides
- {doc}`/get_started/first_program/06_distribute_entitlements` - Step-by-step entitlement and payment preparation

## Summary

Payments are the culmination of the social protection delivery process:

- **Payments execute entitlements** - transforming "should receive" into "did receive"
- **Multiple payment methods** - cash, bank transfer, mobile money, vouchers - each with trade-offs
- **Service points** are critical infrastructure for physical distribution
- **Payment states** track progress from creation to completion
- **Reconciliation ensures** payments were completed successfully
- **Verification confirms** beneficiaries actually received funds
- **Security measures** protect against fraud and errors

Understanding how payments work helps everyone involved in social protection programs ensure that benefits reach intended beneficiaries efficiently, securely, and with full accountability.

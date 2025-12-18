---
openspp:
  doc_status: draft
---

# Entitlements

Entitlements define what benefits a beneficiary receives from a social protection program. They are the bridge between eligibility (who qualifies) and payments (what they actually receive).

**For:** All audiences

## What is an Entitlement?

An entitlement is a record that specifies what a beneficiary is entitled to receive during a program cycle. When a cycle begins, OpenSPP generates entitlement records for all eligible beneficiaries. Each entitlement contains:

- **Who** receives the benefit (the beneficiary)
- **What** they receive (amount, voucher, or goods)
- **When** they receive it (the cycle period)
- **How much** they receive (calculated amount or fixed value)
- **Status** of the entitlement (draft, approved, paid)

## How Entitlements Work

```
Program Cycle Starts
         ↓
   Eligibility Check
         ↓
  Entitlements Generated ← Entitlement Manager calculates amounts
         ↓
  Entitlements Approved
         ↓
   Payments Created
         ↓
   Payments Disbursed
```

Entitlements act as a "promise to pay" before actual payment occurs. This separation allows program managers to review and approve entitlements before funds are disbursed.

## Entitlement Types

OpenSPP supports different types of benefits through entitlements:

### Cash Entitlements

Direct monetary transfers to beneficiaries. The entitlement records the amount in the local currency.

**Example:**
- A household is entitled to 5,000 KES per month
- The entitlement record shows: Amount = 5,000 KES
- Payment is made via bank transfer or mobile money

### In-Kind Entitlements

Physical goods or commodities provided to beneficiaries. The entitlement specifies the items and quantities.

**Example:**
- A household is entitled to 50 kg of rice and 10 liters of cooking oil
- The entitlement record lists these items
- Distribution occurs at a designated location

### Voucher Entitlements

Vouchers that can be redeemed for goods or services. The entitlement generates a unique voucher code.

**Example:**
- A beneficiary receives a voucher worth 3,000 KES
- The voucher can be used at authorized merchants
- Redemption is tracked in the system

### Restricted Cash Entitlements

Vouchers that function like cash but can only be used for specific goods or at specific vendors.

**Example:**
- A voucher for 2,000 KES redeemable only for food items
- Merchants use Point of Sale systems integrated with OpenSPP
- System tracks what was purchased against the voucher

## Entitlement Manager

The Entitlement Manager is the component that generates and calculates entitlements. Different programs can use different Entitlement Managers depending on their needs.

### What the Entitlement Manager Does

1. **Identifies eligible beneficiaries** for the cycle
2. **Calculates the entitlement amount** for each beneficiary
3. **Generates entitlement records** in the system
4. **Applies program rules** such as caps, floors, or adjustments

### Types of Entitlement Managers

#### Default Entitlement Manager

The standard manager that creates entitlements based on fixed amounts or simple formulas.

**Use when:**
- All beneficiaries receive the same amount
- Simple calculations based on household size
- Straightforward program designs

#### Formula-Based Entitlement Manager

Uses CEL (Common Expression Language) expressions to calculate entitlements based on beneficiary data.

**Use when:**
- Amounts vary based on household characteristics
- Complex calculations involving multiple factors
- Graduated benefits based on income or need

**Example formula:**
```cel
base_amount + (household_size * per_person_amount) - (household_income * reduction_rate)
```

#### Custom Entitlement Managers

Organizations can develop custom managers for specialized program logic.

**Use when:**
- Integration with external systems is required
- Complex business rules that exceed formula capabilities
- Special calculation methods unique to your programs

## Entitlement Calculation

### Fixed Amount

The simplest approach where every beneficiary receives the same amount.

**Configuration:**
- Set a fixed amount in the program settings
- All eligible beneficiaries receive this amount
- No variation based on household characteristics

**Example:** Every eligible household receives 10,000 KES per cycle.

### Formula-Based Calculation

Amounts are calculated using formulas that consider beneficiary data.

**Common calculation patterns:**

| Pattern | Formula Example | Result |
|---------|----------------|--------|
| Per capita | `household_size * 1000` | More members = higher amount |
| Income-adjusted | `5000 - (monthly_income * 0.1)` | Lower income = higher amount |
| Graduated | `if(children_count > 3, 8000, 5000)` | Different amounts by threshold |
| Capped | `min(household_size * 1000, 15000)` | Maximum limit applied |

### Variables in Formulas

Formulas can reference:

- **Registry data**: Age, gender, location, household size
- **Custom fields**: Income, disability status, vulnerability scores
- **Calculated variables**: Age groups, dependency ratios
- **Event data**: Recent assessments or surveys

For detailed formula configuration, see the Configuration Guide on Entitlement Formulas.

## Entitlement States

Entitlements move through a lifecycle from creation to payment:

### Draft

**Initial state when created**

- Entitlement has been calculated and recorded
- Not yet reviewed or approved
- Can be modified or recalculated
- No payments can be made

**Actions available:**
- Review amounts
- Adjust if needed
- Run validations
- Recalculate if formulas change

### Approved

**Ready for payment**

- Entitlement has been reviewed and approved
- Locked against changes
- Payments can now be created
- Creates an audit trail

**Actions available:**
- Create payment
- Cancel if needed (with reason)
- View approval history

### Paid

**Payment completed**

- Payment has been successfully disbursed
- Entitlement is fulfilled
- Record is closed for the cycle
- Included in reporting

**Actions available:**
- View payment details
- Generate receipts
- Include in reconciliation reports

### Additional States

Some programs may include additional states:

- **Pending Review**: Awaiting manager approval
- **Rejected**: Entitlement denied after review
- **Cancelled**: Entitlement voided before payment
- **Partially Paid**: Some but not all of the entitlement disbursed

## The Relationship: Cycle → Entitlements → Payments

Understanding how these three concepts connect is essential:

### Program Cycle

A time-bound period when benefits are distributed (e.g., January 2025, Q1 2025).

**Contains:**
- Start and end dates
- List of eligible beneficiaries
- Budget allocation
- Distribution schedule

### Entitlements

Records of what each beneficiary should receive during the cycle.

**Created when:** Cycle is started
**One entitlement per:** Beneficiary per cycle
**Contains:** Amount/items, beneficiary ID, calculation details

### Payments

The actual disbursement of entitlements to beneficiaries.

**Created when:** Entitlements are approved
**One or more payments per:** Entitlement (if split payments)
**Contains:** Payment method, transaction ID, date, status

### Example Flow

1. **January 2025 Cycle begins**
   - 1,000 beneficiaries are eligible

2. **Entitlement Manager runs**
   - Creates 1,000 entitlement records
   - Calculates amounts based on household data
   - Total: 5,000,000 KES in entitlements

3. **Program Manager reviews**
   - Checks entitlement list
   - Approves all entitlements

4. **Payment Manager creates payments**
   - Generates 1,000 payment records
   - Submits to bank or mobile money provider
   - Tracks payment status

5. **Payments complete**
   - Beneficiaries receive funds
   - Entitlements marked as "Paid"
   - Cycle reporting generated

## Multiple Entitlements per Beneficiary

In some scenarios, a beneficiary may have multiple entitlements:

### Multiple Programs

A beneficiary can be enrolled in several programs simultaneously.

**Example:**
- Child nutrition program: 2,000 KES/month
- School feeding voucher: 1,500 KES/month
- Total entitlements: Two separate records

### Top-Up or Supplements

Base entitlements may have additional supplements added.

**Example:**
- Base cash transfer: 5,000 KES
- Disability supplement: 1,000 KES
- Emergency top-up: 2,000 KES
- Total: Three entitlement records for one cycle

### Split Payments

A single entitlement may result in multiple payments.

**Example:**
- Entitlement: 10,000 KES for the quarter
- Payment 1: 5,000 KES in January
- Payment 2: 5,000 KES in March
- One entitlement, two payments

## Entitlement Adjustments

Sometimes entitlements need to be modified after creation:

### Recalculation

If beneficiary data changes before approval, entitlements can be recalculated.

**Triggers:**
- Updated household size
- Corrected income data
- Changed program parameters

### Manual Adjustments

Program managers can manually adjust specific entitlements.

**Reasons:**
- Special circumstances
- Error corrections
- Discretionary supplements
- Appeals or grievances

### Adjustments are audited and logged to maintain transparency.

## Common Questions

### Can entitlements be deleted?

Entitlements in "Draft" state can be deleted and regenerated. Once approved, they should be cancelled rather than deleted to preserve the audit trail.

### What happens if a beneficiary becomes ineligible during a cycle?

The entitlement can be cancelled before payment. Once paid, the entitlement remains as a historical record, but the beneficiary may be removed from future cycles.

### Can entitlements be partially paid?

Yes. Programs can split entitlements into multiple payments, or make partial payments if full amounts aren't available.

### How do entitlements handle currency?

Entitlements store amounts in the program's configured currency. For international programs, exchange rates can be applied at payment time.

### What if the calculated amount is zero or negative?

- **Zero amounts**: May be valid (beneficiary receives no cash but remains enrolled)
- **Negative amounts**: Usually indicates an error in the formula that should be corrected

## Entitlement Reporting

Entitlements provide critical data for program monitoring:

### Key Metrics

- **Total entitlements** per cycle
- **Average entitlement** amount
- **Distribution by region** or demographic
- **Approval rates** and timing
- **Payment completion** rates

### Common Reports

| Report | Purpose |
|--------|---------|
| Entitlement Summary | Overview of amounts by cycle |
| Beneficiary Statement | Individual entitlement history |
| Variance Report | Differences between cycles |
| Payment Reconciliation | Match entitlements to payments |
| Audit Report | Track approvals and changes |

## Security and Access Control

Entitlements contain sensitive beneficiary and financial data:

### Who can view entitlements?

- Program managers
- Finance officers
- Authorized M&E staff
- Auditors (read-only)

### Who can approve entitlements?

- Program managers
- Designated approvers
- Finance managers (depending on configuration)

### Who can adjust entitlements?

- Program managers (with reasons logged)
- System administrators (with audit trail)

Access is controlled through OpenSPP's role-based permission system.

## Next Steps

Now that you understand entitlements conceptually:

- **Users**: See the User Guide for step-by-step instructions on viewing and managing entitlements
- **Implementers**: Review the Configuration Guide on entitlement formulas to set up calculations
- **Developers**: Check the Developer Guide for creating custom Entitlement Managers
- **Sys Admins**: See the Operations Guide for entitlement data management and backups

## Related Concepts

- **{doc}`programs`** - Programs contain the rules that generate entitlements
- **Cycles** - Time periods during which entitlements are created and paid
- **Eligibility** - Determines who receives entitlements
- **Payments** - The fulfillment of entitlements through disbursement

---
openspp:
  doc_status: draft
  products: [core]
---

# Programs

A program defines a social protection intervention—who receives benefits, what they receive, and how benefits are delivered. Programs are the core organizing unit in OpenSPP, connecting registrants to entitlements through eligibility rules and distribution cycles.

**For:** All audiences

## What is a program?

A program represents a social protection initiative with defined:

- **Target population** - Individuals or groups (households) eligible for benefits
- **Eligibility criteria** - Rules that determine who qualifies
- **Benefits** - What beneficiaries receive (cash, vouchers, in-kind goods)
- **Distribution schedule** - How often benefits are delivered (through cycles)
- **Delivery mechanism** - How benefits reach beneficiaries (bank transfer, mobile money, etc.)

**Examples of programs:**

| Program type | Target | Benefit | Frequency |
|-------------|--------|---------|-----------|
| Unconditional cash transfer | Poor households | Fixed monthly payment | Monthly |
| Child grant | Families with children under 5 | Per-child payment | Quarterly |
| Emergency food assistance | Disaster-affected households | Food vouchers | One-time |
| School feeding | Enrolled students | Daily meals | Daily during school |
| Farmer input subsidy | Smallholder farmers | Seeds and fertilizer | Seasonal |

## Program structure

A program connects several components:

```{mermaid}
graph TD
    P[Program] --> M[Program Memberships<br/>Beneficiaries]
    P --> C[Cycles<br/>Distribution rounds]
    P --> MG[Managers<br/>Business logic]
    C --> E[Entitlements<br/>What each beneficiary receives]
    E --> PM[Payments<br/>Disbursements]

    style P fill:#e1f5fe
    style M fill:#fff3e0
    style C fill:#f3e5f5
    style E fill:#e8f5e9
    style PM fill:#fce4ec
```

| Component | Purpose |
|-----------|---------|
| **Program** | Container defining rules and configuration |
| **Program memberships** | Links registrants to the program with enrollment status |
| **Cycles** | Time-bound distribution periods (see {doc}`cycles`) |
| **Entitlements** | Specific benefits calculated for each beneficiary per cycle |
| **Payments** | Actual disbursements to beneficiaries |
| **Managers** | Configurable components that control program behavior |

## Program configuration

### Target type

Programs target either individuals or groups:

| Target type | Use when | Examples |
|-------------|----------|----------|
| **Individual** | Benefits are person-specific | Pensions, scholarships, disability grants |
| **Group** | Benefits are household-level | Family cash transfers, housing subsidies |

The target type determines which registrants can be enrolled and how entitlements are calculated.

### Program managers

Managers are pluggable components that control how the program operates. Each manager type handles a specific aspect of program execution:

| Manager | Purpose | When It Runs |
|---------|---------|--------------|
| **Eligibility manager** | Determines who qualifies for the program | During enrollment and eligibility verification |
| **Program manager** | Controls enrollment workflow and cycle creation | When adding beneficiaries or creating cycles |
| **Cycle manager** | Manages cycle lifecycle and transitions | During cycle operations |
| **Entitlement manager** | Calculates what each beneficiary receives | When preparing entitlements for a cycle |
| **Deduplication manager** | Identifies duplicate registrations | Before enrollment or on-demand |
| **Notification manager** | Sends messages to beneficiaries | At key program events |
| **Payment manager** | Handles payment preparation and disbursement | When processing payments |
| **Compliance manager** | Enforces program conditions | During eligibility checks and cycle processing |

Each manager type has a default implementation that works for most cases. Administrators can configure manager settings or developers can create custom managers for specialized requirements.

## Program lifecycle

Programs move through a simple lifecycle:

```{mermaid}
graph LR
    Start(( )) --> Active
    Active -->|Run cycles| Active
    Active -->|End program| Ended
    Ended -->|Reactivate| Active
    Ended --> Stop(( ))

    style Start fill:#000,stroke:#000
    style Stop fill:#000,stroke:#000
    style Active fill:#e8f5e9
    style Ended fill:#ffebee
```

| State | Description | What You Can Do |
|-------|-------------|-----------------|
| **Active** | Program is operational | Enroll beneficiaries, create cycles, process payments |
| **Ended** | Program has concluded | View historical data, reactivate if needed |

When a program is archived (deactivated), all draft, pending, and approved cycles are automatically cancelled.

## Program memberships

A program membership links a registrant to a program. It tracks:

- **Enrollment status** - Where the registrant is in the enrollment process
- **Enrollment date** - When they were enrolled
- **Exit date** - When they left the program (if applicable)
- **Deduplication status** - Whether they've been checked for duplicates

### Membership states

```{mermaid}
graph LR
    Start(( )) -->|Add to program| Draft
    Draft -->|Verify eligibility| Enrolled
    Draft -->|Fails criteria| NotEligible
    Draft -->|Duplicate found| Duplicated
    Enrolled -->|Pause benefits| Paused
    Enrolled -->|Exit program| Exited
    Paused -->|Resume| Enrolled
    Paused -->|Exit program| Exited
    NotEligible -->|Re-evaluate| Draft
    Duplicated -->|Resolve duplicate| Draft
    Exited --> Stop(( ))

    style Start fill:#000,stroke:#000
    style Stop fill:#000,stroke:#000
    style Draft fill:#fff3e0
    style Enrolled fill:#e8f5e9
    style Paused fill:#e3f2fd
    style Exited fill:#ffebee
    style NotEligible fill:#ffebee
    style Duplicated fill:#ffebee
```

| State | Description | Next Steps |
|-------|-------------|------------|
| **Draft** | Added to program, not yet verified | Run eligibility check |
| **Enrolled** | Actively receiving benefits | Include in cycles |
| **Paused** | Temporarily suspended | Resume when ready |
| **Exited** | Left the program | No further benefits |
| **Not Eligible** | Failed eligibility criteria | Re-evaluate if circumstances change |
| **Duplicated** | Identified as a duplicate | Resolve and retry |

## Key program operations

### 1. Import eligible registrants

Populate the program with registrants who potentially qualify.

**What it does:**
- Runs eligibility criteria against the registry
- Creates draft memberships for matching registrants
- Does not automatically enroll—allows review first

**When to use:**
- Starting a new program
- Expanding program coverage
- Refreshing the beneficiary pool

### 2. Verify eligibility

Check whether current members still qualify.

**What it does:**
- Re-runs eligibility rules against current data
- Updates membership status (enrolled, not_eligible)
- Identifies people who no longer qualify

**When to use:**
- Before each cycle
- After major data updates
- For programs with changing criteria

### 3. Enroll eligible registrants

Move verified registrants to enrolled status.

**What it does:**
- Changes draft members to enrolled status
- Records enrollment date
- Makes them eligible for cycle inclusion

**When to use:**
- After eligibility verification
- When ready to start benefits

### 4. Deduplicate beneficiaries

Identify and flag duplicate registrations.

**What it does:**
- Compares beneficiaries using configured matching rules
- Flags potential duplicates for review
- Prevents double-dipping across programs

**When to use:**
- Before enrollment finalization
- Periodically for ongoing programs
- After data imports

### 5. Create new cycle

Start a new distribution period.

**What it does:**
- Creates a new cycle for the program
- Optionally copies enrolled beneficiaries to the cycle
- Prepares for entitlement calculation

**When to use:**
- At the start of each distribution period
- Monthly, quarterly, or as scheduled

## Entitlements

Entitlements represent what a beneficiary is entitled to receive in a specific cycle.

### Entitlement types

| Type | Description | Example |
|------|-------------|---------|
| **Cash** | Monetary payment | $50 monthly transfer |
| **In-Kind** | Physical goods | 10kg rice, cooking oil |
| **Voucher** | Redeemable token | Food voucher worth $30 |

### Entitlement states

| State | Description |
|-------|-------------|
| **Draft** | Created, not yet approved |
| **Pending Approval** | Submitted for review |
| **Approved** | Ready for payment |
| **Transferred to FSP** | Sent to financial service provider |
| **Paid to Beneficiary** | Successfully delivered |
| **Rejected** | Declined (various reasons) |
| **Cancelled** | Cancelled before payment |
| **Expired** | Validity period passed |

### Entitlement calculation

The Entitlement manager calculates entitlements using:

- **Fixed amounts** - Same amount for everyone
- **Formula-based** - Calculated from beneficiary data (household size, number of children, etc.)
- **CEL expressions** - Complex rules using Common Expression Language

**Example formula:**
```
Base amount: $30
Per child under 5: +$10
Per elderly member: +$5

Household with 2 children under 5 and 1 elderly = $30 + $20 + $5 = $55
```

## Program types by use case

### Unconditional Cash Transfer (UCT)

Regular payments without conditions.

| Aspect | Typical configuration |
|--------|----------------------|
| Target | Households below poverty line |
| Eligibility | Income/asset-based (often PMT score) |
| Entitlement | Fixed amount per household or scaled by size |
| Frequency | Monthly or quarterly |
| Compliance | None required |

### Conditional Cash Transfer (CCT)

Payments contingent on meeting conditions.

| Aspect | Typical configuration |
|--------|----------------------|
| Target | Households with children or pregnant women |
| Eligibility | Income-based plus household composition |
| Entitlement | Base amount plus per-child supplements |
| Frequency | Monthly or bi-monthly |
| Compliance | School attendance, health checkups |

### Emergency Response

One-time or short-term crisis assistance.

| Aspect | Typical configuration |
|--------|----------------------|
| Target | Disaster-affected households |
| Eligibility | Geographic targeting, vulnerability assessment |
| Entitlement | One-time payment or in-kind package |
| Frequency | One-time or limited cycles |
| Compliance | None (emergency context) |

### Agricultural Support

Seasonal support for farmers.

| Aspect | Typical configuration |
|--------|----------------------|
| Target | Smallholder farmers |
| Eligibility | Land size, crop type, vulnerability |
| Entitlement | Input vouchers, cash for inputs |
| Frequency | Seasonal (planting, harvest) |
| Compliance | Land registration, crop reporting |

## Data model overview

```{mermaid}
erDiagram
    PROGRAM {
        string name
        string target_type
        string state
        date date_ended
    }
    PROGRAM_MEMBERSHIP {
        string state
        date enrollment_date
        date exit_date
    }
    CYCLE {
        string name
        string state
        date start_date
        date end_date
    }
    ENTITLEMENT {
        string code
        decimal initial_amount
        string state
        date valid_from
        date valid_until
    }
    REGISTRANT {
        string name
        boolean is_group
    }

    PROGRAM ||--o{ PROGRAM_MEMBERSHIP : "has"
    PROGRAM ||--o{ CYCLE : "has"
    REGISTRANT ||--o{ PROGRAM_MEMBERSHIP : "enrolled in"
    CYCLE ||--o{ ENTITLEMENT : "contains"
    REGISTRANT ||--o{ ENTITLEMENT : "receives"
```

## Are you stuck?

### How do I add beneficiaries to a program?

**Options:**
1. **Import eligible registrants** - Use the "Import Eligible Registrants" button to find matching registrants from the registry
2. **Manual enrollment** - Add individual registrants through the beneficiaries list
3. **Bulk import** - Upload a CSV/Excel file with registrant IDs

### Why aren't my beneficiaries showing as enrolled?

**Check:**
- Are they in "Draft" state? Run eligibility verification to enroll them
- Did they fail eligibility? Check the "Not Eligible" filter
- Were duplicates found? Check the "Duplicated" filter

### Can a registrant be in multiple programs?

Yes. A registrant can be enrolled in multiple programs simultaneously. Each program has its own membership record. Use deduplication to identify overlaps if needed.

### How do I change what beneficiaries receive?

Entitlement amounts are controlled by the Entitlement Manager:
1. Go to program configuration
2. Find the Entitlement Manager section
3. Adjust the calculation rules (fixed amount, formula, or CEL expression)

Changes apply to future cycles—existing entitlements are not automatically recalculated.

### What happens when I end a program?

When you end a program:
- State changes to "Ended"
- No new cycles can be created
- Existing cycles continue to their conclusion
- Historical data is preserved
- You can reactivate if needed

### How do I handle beneficiaries who no longer qualify?

**Options:**
1. **Re-verify eligibility** - Run eligibility check; non-qualifying members move to "Not Eligible"
2. **Manual exit** - Mark individual members as "Exited" with an exit date
3. **Pause** - Temporarily suspend benefits without exiting

## Next steps

**Learn more about concepts:**
- {doc}`cycles` - Distribution periods within programs
- {doc}`registry` - Source of beneficiary data

**For configuration:**
- See the Configuration Guide for setting up eligibility rules, entitlement formulas, and managers

**For developers:**
- See the Developer Guide for creating custom managers and extending program functionality

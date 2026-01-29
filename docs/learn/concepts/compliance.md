---
openspp:
  doc_status: draft
  products: [core]
---

# Compliance

Compliance refers to the conditions that beneficiaries must meet to continue receiving benefits. It's the enforcement mechanism for conditional cash transfer (CCT) and other programs where benefits depend on specific behaviors or activities.

**For:** All audiences

## What is compliance?

Compliance conditions are requirements that beneficiaries must fulfill to maintain their eligibility or receive their full entitlement. These conditions typically aim to encourage behaviors that improve long-term outcomes.

**Examples of compliance conditions:**

| Condition type | Example requirements |
|---------------|---------------------|
| **Health** | Regular health checkups, vaccination schedules, prenatal visits |
| **Education** | Minimum school attendance (e.g., 85%), enrollment verification |
| **Training** | Attendance at family development sessions, skills training |
| **Documentation** | Submitting required forms, updating registration data |

## Compliance vs. eligibility

| Concept | When checked | Purpose |
|---------|-------------|---------|
| **Eligibility** | At enrollment and periodically | Determines who qualifies for the program |
| **Compliance** | Each cycle | Determines if enrolled beneficiaries receive benefits |

Eligibility asks "Should this person be in the program?" while compliance asks "Has this beneficiary met the conditions to receive their payment this cycle?"

## Why compliance matters

Compliance mechanisms serve multiple purposes:

| Purpose | Description |
|---------|-------------|
| **Behavior change** | Encourage activities that improve outcomes (health visits, school attendance) |
| **Accountability** | Ensure program resources reach those meeting conditions |
| **Program integrity** | Verify ongoing participation and engagement |
| **Impact measurement** | Track whether beneficiaries are engaging with complementary services |

## How compliance works in OpenSPP

### Compliance manager

The Compliance manager is a configurable component that checks whether beneficiaries meet program conditions:

```{mermaid}
graph LR
    B[Beneficiaries] --> CM[Compliance Manager]
    CM --> |Check conditions| CR[Compliance Records]
    CR --> |Met| E[Eligible for payment]
    CR --> |Not met| S[Suspended/Reduced]

    style CM fill:#fff3e0
    style E fill:#e8f5e9
    style S fill:#ffebee
```

### When compliance is checked

Compliance can be verified at different points:

| Timing | Configuration | Effect |
|--------|--------------|--------|
| **When adding beneficiaries to cycle** | Automated filtering = 1 | Non-compliant beneficiaries excluded from cycle |
| **When preparing entitlements** | Automated filtering = 2 | Non-compliant beneficiaries don't receive entitlements |
| **Manual review** | Automated filtering = 0 | Staff manually review compliance status |

### Compliance workflow

```{mermaid}
graph TD
    subgraph Recording
        A[Compliance activity occurs] --> B[Record in system]
        B --> C[Health visit / School attendance / Training]
    end

    subgraph Verification
        D[Cycle starts] --> E[Check compliance records]
        E --> F{Conditions met?}
    end

    subgraph Outcome
        F --> |Yes| G[Include in entitlements]
        F --> |No| H[Exclude or reduce]
        F --> |Partial| I[Partial payment]
    end

    C --> D

    style G fill:#e8f5e9
    style H fill:#ffebee
    style I fill:#fff3e0
```

## Types of compliance conditions

### Health compliance

Track health-related requirements:

| Requirement | Typical target | Verification method |
|-------------|---------------|---------------------|
| Prenatal checkups | Pregnant women | Health facility records |
| Growth monitoring | Children under 5 | Clinic visit records |
| Vaccination | Children by age | Immunization registry |
| Health education | All beneficiaries | Session attendance |

### Education compliance

Track school-related requirements:

| Requirement | Typical target | Verification method |
|-------------|---------------|---------------------|
| School enrollment | School-age children | Enrollment records |
| Attendance rate | Enrolled students | School attendance records |
| Grade progression | Students | Report cards |

### Training/session compliance

Track participation in program activities:

| Requirement | Typical target | Verification method |
|-------------|---------------|---------------------|
| Family development sessions | Household representatives | Attendance sheets |
| Skills training | Working-age adults | Training records |
| Community meetings | All beneficiaries | Sign-in logs |

### Attendance-based compliance

OpenSPP supports detailed attendance tracking:

| Feature | Description |
|---------|-------------|
| **Attendance types** | Configure different activity types (health, education, training) |
| **Attendance locations** | Track where activities occurred |
| **Group membership attendance** | Track attendance by household members |
| **Cycle-level tracking** | Associate attendance with specific cycles |

## Compliance data

### Compliance records

Each compliance record captures:

| Field | Description |
|-------|-------------|
| **Beneficiary** | Who the record applies to |
| **Condition type** | Health, education, training, etc. |
| **Period** | Time period covered |
| **Status** | Compliant, non-compliant, partial, pending |
| **Verification** | How compliance was verified |
| **Notes** | Additional details or exceptions |

### Compliance periods

Programs define compliance periods that align with cycles:

| Period type | Duration | Example |
|------------|----------|---------|
| **Monthly** | One month | Monthly attendance threshold |
| **Quarterly** | Three months | Quarterly health checkups |
| **Semester** | Six months | School semester attendance |
| **Annual** | One year | Annual re-certification |

## Compliance outcomes

### Full compliance

Beneficiary meets all conditions:
- Receives full entitlement
- Continues in program
- No additional action needed

### Partial compliance

Beneficiary meets some conditions:
- May receive reduced payment
- Warning issued
- Grace period may apply

### Non-compliance

Beneficiary fails to meet conditions:
- Payment may be suspended
- Case review triggered
- Possible program exit after repeated non-compliance

### Exemptions

Some beneficiaries may be exempt from certain conditions:

| Exemption type | Example |
|---------------|---------|
| **Age-based** | Elderly exempt from school attendance |
| **Health-based** | Disabled exempt from physical activities |
| **Geographic** | Remote areas with no health facility |
| **Temporary** | Illness, natural disaster, etc. |

## Common compliance programs

### Conditional Cash Transfer (CCT)

| Component | Conditions |
|-----------|------------|
| **Health grant** | Regular health checkups, vaccinations, prenatal visits |
| **Education grant** | 85% school attendance, enrollment |
| **Rice subsidy** | Attendance at family development sessions |

### School feeding

| Component | Conditions |
|-----------|------------|
| **Daily meals** | School attendance on meal days |
| **Take-home rations** | Monthly attendance threshold |

### Skills training programs

| Component | Conditions |
|-----------|------------|
| **Training stipend** | Attendance at training sessions |
| **Completion bonus** | Successful course completion |

## Best practices

### Condition design

| Practice | Reason |
|----------|--------|
| **Keep conditions achievable** | Unrealistic requirements cause dropouts |
| **Align with program goals** | Conditions should support desired outcomes |
| **Consider local context** | Account for service availability |
| **Build in flexibility** | Allow for legitimate exceptions |

### Verification

| Practice | Reason |
|----------|--------|
| **Use existing systems** | Integrate with health/education databases |
| **Automate where possible** | Reduce manual verification burden |
| **Allow corrections** | Enable fixing data entry errors |
| **Audit regularly** | Ensure data quality |

### Communication

| Practice | Reason |
|----------|--------|
| **Clear requirements** | Beneficiaries must understand conditions |
| **Advance notice** | Warn before suspending benefits |
| **Appeals process** | Allow beneficiaries to contest decisions |
| **Regular reminders** | Help beneficiaries stay compliant |

## Are you stuck?

### Why aren't beneficiaries being filtered by compliance?

**Check:**
- Is automated filtering enabled in system settings?
- Are compliance managers configured on the program?
- Do beneficiaries have compliance records for the current period?

**Configuration:**
- Setting `0` = Manual review (no automatic filtering)
- Setting `1` = Filter when adding to cycle
- Setting `2` = Filter when preparing entitlements

### How do I record compliance data?

**Options:**
1. **Manual entry** - Staff enter records in OpenSPP
2. **Import** - Upload compliance data from external systems
3. **Integration** - Connect to health/education databases via API
4. **Mobile collection** - Use ODK/CommCare for field data collection

### How do I handle exceptions?

**For individual cases:**
1. Create an exemption record with reason and duration
2. Document supporting evidence
3. Set exemption end date if temporary

**For program-wide exceptions:**
- Configure exemption rules in the compliance manager
- Use domains to exclude specific groups from conditions

### Can compliance affect payment amounts?

Yes. The entitlement manager can:
- **Reduce payments** for partial compliance
- **Suspend payments** for non-compliance
- **Apply graduated penalties** based on compliance level

Configure this in the entitlement manager's calculation rules.

### How do I track compliance over time?

**Reports available:**
- Compliance rate by area/period
- Non-compliance reasons breakdown
- Compliance trends over cycles
- Individual compliance history

## Next steps

**Learn more about concepts:**
- {doc}`eligibility` - Initial qualification for programs
- {doc}`programs` - How compliance managers are configured
- {doc}`entitlements` - How compliance affects payments
- {doc}`cycles` - Where compliance is verified

**For configuration:**
- See the Configuration Guide for setting up compliance managers

**For developers:**
- See the Developer Guide for creating custom compliance managers

---
openspp:
  doc_status: draft
  products: [core]
---

# Deduplication

Deduplication identifies and handles duplicate registrations to ensure program integrity. It prevents individuals from receiving benefits multiple times through fraudulent or accidental duplicate enrollments.

**For:** All audiences

## What is Deduplication?

Deduplication is the process of finding and managing cases where the same person appears multiple times in a program—either directly or through multiple household memberships.

**Why it matters:**

| Risk | Impact |
|------|--------|
| **Double-dipping** | Same person receives benefits twice |
| **Inflated numbers** | Inaccurate beneficiary counts |
| **Budget leakage** | Resources go to duplicates instead of eligible people |
| **Program integrity** | Undermines trust in the system |

## Types of Duplicates

### Individual in Multiple Groups

The same person registered as a member of multiple households:

```{mermaid}
graph LR
    I[Individual: John] --> G1[Household A]
    I --> G2[Household B]

    style I fill:#ffebee
    style G1 fill:#e3f2fd
    style G2 fill:#e3f2fd
```

**Common causes:**
- Person moves but old registration not updated
- Intentional fraud to receive double benefits
- Data entry errors creating duplicate records

### Duplicate ID Documents

Different registrations sharing the same ID number:

| Registration | Name | ID Number |
|-------------|------|-----------|
| Person A | John Smith | ID-12345 |
| Person B | J. Smith | ID-12345 |

**Common causes:**
- Same person registered under variations of their name
- Typos in ID entry
- Intentional identity fraud

### Duplicate Phone Numbers

Multiple registrants using the same phone number:

| Registration | Name | Phone |
|-------------|------|-------|
| Person A | Mary Jones | +1234567890 |
| Person B | M. Jones | +1234567890 |

**Common causes:**
- Family members sharing a phone
- Same person registered multiple times
- Agent's phone used during registration

## How Deduplication Works

### Deduplication Manager

The Deduplication Manager is a configurable component that checks for duplicates:

```{mermaid}
graph LR
    B[Program Beneficiaries] --> DM[Deduplication Manager]
    DM --> |Check matching rules| C{Duplicates found?}
    C --> |Yes| D[Record & Flag]
    C --> |No| OK[Continue]
    D --> R[Review & Resolve]

    style DM fill:#fff3e0
    style D fill:#ffebee
    style OK fill:#e8f5e9
```

### Manager Types

| Manager | What It Checks | Best For |
|---------|---------------|----------|
| **Default** | Same individual in multiple groups | Group-targeted programs |
| **ID Document** | Matching ID numbers | Programs requiring ID verification |
| **Phone Number** | Matching phone numbers | Programs using mobile payments |

### Deduplication Workflow

```{mermaid}
graph TD
    subgraph Detection
        A[Run deduplication check] --> B[Compare beneficiaries]
        B --> C[Find matches]
    end

    subgraph Recording
        C --> D[Create duplicate record]
        D --> E[Flag beneficiaries]
    end

    subgraph Resolution
        E --> F{Review}
        F --> |Keep one| G[Mark others as duplicated]
        F --> |False positive| H[Mark as not duplicate]
        F --> |Merge| I[Consolidate records]
    end

    style D fill:#ffebee
    style G fill:#e8f5e9
    style H fill:#e8f5e9
```

## Duplicate States

When duplicates are found, program memberships are updated:

| State | Meaning | Effect |
|-------|---------|--------|
| **Enrolled** | Verified beneficiary | Receives benefits |
| **Duplicated** | Flagged as duplicate | Excluded from benefits until resolved |

### Resolution Logic

When duplicates are detected:

1. **If one is already enrolled** → Keep enrolled, mark others as duplicated
2. **If multiple enrolled** → Flag for manual review
3. **If none enrolled** → Mark all as duplicated for review

## Configuring Deduplication

### Program Setup

Add deduplication managers to your program:

| Setting | Description |
|---------|-------------|
| **Manager type** | Which deduplication method to use |
| **Supported ID types** | For ID dedup: which document types to check |
| **Run timing** | When to check (enrollment, cycle, on-demand) |

### ID Document Deduplication

Configure which ID types to compare:

| ID Type | Check Enabled |
|---------|--------------|
| National ID | Yes |
| Passport | Yes |
| Voter Card | No |
| Birth Certificate | No |

Only non-expired documents are checked.

## When to Run Deduplication

| Timing | Use Case |
|--------|----------|
| **Before enrollment** | Catch duplicates early |
| **After data import** | Check bulk-imported data |
| **Periodically** | Ongoing monitoring |
| **Before payment** | Final verification |

## Duplicate Records

When duplicates are found, a record is created:

| Field | Description |
|-------|-------------|
| **Beneficiaries** | List of duplicate memberships |
| **Reason** | Why flagged (duplicate individuals, IDs, phones) |
| **State** | duplicate, resolved, not_duplicate |
| **Manager** | Which deduplication manager found it |

## Best Practices

### Prevention

| Practice | Reason |
|----------|--------|
| **Require valid ID** | Unique identifier for each person |
| **Validate at registration** | Catch duplicates before they enter |
| **Use biometrics** | When available, most reliable |
| **Standardize data entry** | Consistent formats reduce false matches |

### Detection

| Practice | Reason |
|----------|--------|
| **Multiple methods** | Different checks catch different duplicates |
| **Regular checks** | Ongoing monitoring catches new duplicates |
| **Cross-program checks** | Detect duplicates across programs |

### Resolution

| Practice | Reason |
|----------|--------|
| **Clear process** | Staff know how to handle duplicates |
| **Verification** | Confirm duplicates before action |
| **Documentation** | Record decisions and reasons |
| **Appeals process** | Allow legitimate cases to be restored |

## Are You Stuck?

### Why are duplicates not being detected?

**Check:**
- Is deduplication manager configured on the program?
- Are you running the check on the right beneficiary states?
- For ID dedup: Are the ID types configured in "Supported ID Types"?
- For phone dedup: Do registrants have phone numbers recorded?

### How do I resolve a duplicate?

**Options:**
1. **Keep the enrolled one** - If one is clearly the correct record
2. **Merge records** - Combine information from duplicates
3. **Mark as not duplicate** - If it's a false positive (different people)
4. **Remove incorrect one** - If one is clearly wrong

### What if the same person should be in multiple programs?

That's allowed. Deduplication checks within a single program. A person can be legitimately enrolled in multiple programs simultaneously.

### How do I check for duplicates across programs?

Cross-program deduplication requires checking the registry level, not program level. Look for individuals appearing in multiple household groups, or use ID/phone deduplication at registry import time.

### Can I customize matching rules?

Yes. Developers can create custom deduplication managers with specific matching logic. The default managers check exact matches; custom managers can implement fuzzy matching, phonetic matching, etc.

## Next Steps

**Learn more about concepts:**
- {doc}`programs` - Where deduplication managers are configured
- {doc}`registry` - Source data for deduplication
- {doc}`eligibility` - Related checks during enrollment

**For configuration:**
- See the Configuration Guide for setting up deduplication managers

**For developers:**
- See the Developer Guide for creating custom deduplication managers

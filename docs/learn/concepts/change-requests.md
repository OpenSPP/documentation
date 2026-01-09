---
openspp:
  doc_status: draft
  products: [core]
---

# Change Requests

Change requests provide a controlled workflow for updating data in OpenSPP. Instead of direct edits, changes go through an approval process that ensures data quality, maintains audit trails, and enforces organizational controls.

**For:** All audiences

## What is a Change Request?

A change request is a formal request to modify data that requires review and approval before taking effect. It captures what change is requested, who requested it, supporting documents, and the approval decision.

**Examples:**

| Request Type | What Changes |
|-------------|--------------|
| Update address | Registrant's location |
| Correct name | Name spelling or legal name change |
| Add ID document | New identification document |
| Add household member | New person in a group |
| Remove household member | Person leaving a group |
| Transfer household | Move member between households |

## Why Use Change Requests?

| Benefit | Description |
|---------|-------------|
| **Data quality** | Changes reviewed before applied |
| **Accountability** | Clear record of who approved what |
| **Audit trail** | Complete history of all changes |
| **Fraud prevention** | Prevents unauthorized modifications |
| **Documentation** | Supporting evidence attached |
| **Workflow control** | Multi-level approvals when needed |

## Change Request Lifecycle

```{mermaid}
graph LR
    Draft -->|Submit| Pending[Under Review]
    Pending -->|Request changes| Revision[Needs Changes]
    Revision -->|Resubmit| Pending
    Pending -->|Approve| Approved
    Pending -->|Decline| Rejected
    Approved -->|Apply| Applied[Completed]

    style Draft fill:#fff3e0
    style Pending fill:#e3f2fd
    style Approved fill:#e8f5e9
    style Applied fill:#c8e6c9
    style Rejected fill:#ffebee
    style Revision fill:#fff3e0
```

### States

| State | Description | Who Acts |
|-------|-------------|----------|
| **Draft** | Being prepared | Requester |
| **Under Review** | Submitted for approval | Reviewer/Approver |
| **Needs Changes** | Sent back for revision | Requester |
| **Approved** | Approved, ready to apply | System or Approver |
| **Completed** | Changes applied | — |
| **Declined** | Rejected | — |

## Change Request Structure

### Core Information

| Field | Description |
|-------|-------------|
| **Reference** | Unique ID (auto-generated) |
| **Request Type** | What kind of change |
| **Registrant** | Who the change affects |
| **Applicant** | Who submitted (may differ from registrant) |
| **Description** | Explanation of the change |

### Detail Record

Each request type has specific fields:

**Example: Address Update**

| Field | Description |
|-------|-------------|
| New Street | Updated street address |
| New City | Updated city |
| New Area | Updated administrative area |
| Reason for Move | Why the address changed |

**Example: Add Household Member**

| Field | Description |
|-------|-------------|
| New Member | Person being added |
| Relationship | Relationship to head |
| Role | Role in household |

### Supporting Documents

Attach evidence to support the request:

| Document Type | Example |
|--------------|---------|
| ID document | Scanned national ID |
| Proof of address | Utility bill |
| Legal document | Marriage certificate |
| Photo | Verification photo |

## Request Types

Request types define what changes are possible and how they're processed:

| Configuration | Purpose |
|--------------|---------|
| **Target type** | Individual, group, or both |
| **Detail model** | What data fields to capture |
| **Apply strategy** | How to apply the change |
| **Approval workflow** | Who reviews and approves |
| **Required documents** | What evidence is needed |
| **Required fields** | Mandatory data before submission |

### Common Request Types

| Type | Target | Changes |
|------|--------|---------|
| **Update Personal Info** | Individual | Name, birthdate, gender |
| **Update Contact** | Both | Phone, email, address |
| **Add ID Document** | Individual | New ID record |
| **Add Member** | Group | New household member |
| **Remove Member** | Group | Remove from household |
| **Transfer Member** | Group | Move between households |
| **Update Household** | Group | Household-level data |

## Approval Workflow

### Single-Level Approval

Simple requests reviewed by one approver:

```{mermaid}
graph LR
    S[Submit] --> R[Reviewer]
    R --> |Approve| A[Applied]
    R --> |Decline| D[Declined]

    style A fill:#e8f5e9
    style D fill:#ffebee
```

### Multi-Level Approval

Sensitive changes require multiple approvals:

```{mermaid}
graph LR
    S[Submit] --> L1[Level 1: Field Officer]
    L1 --> L2[Level 2: Supervisor]
    L2 --> L3[Level 3: Manager]
    L3 --> A[Applied]

    style A fill:#e8f5e9
```

### Revision Workflow

When changes are needed:

```{mermaid}
graph LR
    P[Under Review] --> |Request revision| R[Needs Changes]
    R --> |Update & resubmit| P

    style R fill:#fff3e0
```

## Conflict Detection

Change requests can detect conflicts with other pending requests:

| Conflict Type | Example |
|--------------|---------|
| **Same field** | Two requests updating the same address |
| **Related data** | Adding member who's being transferred elsewhere |
| **Logical conflict** | Removing head while other changes pending |

Conflicts can be configured to:
- **Block** - Prevent submission
- **Warn** - Allow but notify reviewer

## Sources of Change Requests

| Source | Description |
|--------|-------------|
| **Manual entry** | Staff creates in OpenSPP |
| **Event data** | Triggered by survey/assessment |
| **API** | External system submits |
| **Bulk import** | Batch processing |

## Applying Changes

### Automatic Apply

For simple changes, apply immediately on approval:

| Setting | Behavior |
|---------|----------|
| **Auto-apply enabled** | Changes applied when approved |
| **Auto-apply disabled** | Separate "Apply" step needed |

### Preview Changes

Before applying, preview what will change:

| Current | New |
|---------|-----|
| Address: 123 Main St | Address: 456 Oak Ave |
| City: Springfield | City: Shelbyville |

### Apply Strategies

Different request types use different apply logic:

| Strategy | What It Does |
|----------|--------------|
| **Update fields** | Modify existing record |
| **Create record** | Add new related record |
| **Delete record** | Remove related record |
| **Add member** | Create group membership |
| **Remove member** | End group membership |
| **Transfer** | Move between groups |

## Audit Trail

All actions are recorded:

| Event | What's Logged |
|-------|--------------|
| Created | Who, when, initial data |
| Submitted | Submission timestamp |
| Approved/Rejected | Decision, reviewer, reason |
| Applied | Applied timestamp, by whom |
| Revised | What was changed |

## Best Practices

### For Requesters

| Practice | Reason |
|----------|--------|
| **Complete all fields** | Faster approval |
| **Attach documents** | Evidence speeds review |
| **Clear description** | Reviewer understands context |
| **Verify data** | Reduce revision cycles |

### For Reviewers

| Practice | Reason |
|----------|--------|
| **Check documents** | Verify supporting evidence |
| **Preview changes** | Understand impact |
| **Add notes** | Document decision rationale |
| **Timely review** | Don't create backlogs |

### For Administrators

| Practice | Reason |
|----------|--------|
| **Define clear types** | Users know what to request |
| **Appropriate workflows** | Balance control vs. speed |
| **Required fields** | Ensure complete data |
| **Train users** | Proper request submission |

## Are You Stuck?

### Why can't I submit my change request?

**Check:**
- Are all required fields completed?
- Are required documents attached?
- Is there a blocking conflict with another request?

### Why was my request declined?

Check the rejection notes from the reviewer. Common reasons:
- Insufficient documentation
- Data doesn't match supporting documents
- Duplicate of another request
- Outside of policy

### How do I see the changes before they're applied?

Click "Preview Changes" to see a side-by-side comparison of current vs. new values.

### Can I cancel a submitted request?

If the request is still "Under Review", ask an administrator to reset it to Draft or reject it. Once approved or applied, it cannot be cancelled.

### How do I handle urgent changes?

Some programs have expedited approval workflows. Contact your supervisor about priority processing. The audit trail will record any expedited approvals.

## Next Steps

**Learn more about concepts:**
- {doc}`registry` - Where change requests update data
- {doc}`programs` - Change requests can affect enrollments

**For configuration:**
- See the Configuration Guide for setting up change request types

**For developers:**
- See the Developer Guide for custom apply strategies

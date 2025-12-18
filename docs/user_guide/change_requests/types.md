---
openspp:
  doc_status: draft
---

# Change Request Types

This guide is for **users** who want to understand the different types of change requests available in OpenSPP.

## What Are Request Types?

Request types define what kind of changes you can make to registrant data. Each type has its own form with specific fields and validation rules.

Your organization's implementer configures which request types are available and what approval workflow each type follows.

## Common Request Types

### Add Group Member

**Purpose:** Add a new person to an existing household or group.

**When to use:**
- A baby was born
- Someone moved into the household
- A family member was previously missed during registration

**Information required:**
- New member's full name
- Date of birth
- Gender
- Relationship to household head (e.g., child, spouse, parent)
- ID number (if available)
- Phone number (optional)

**What happens when approved:**
- A new individual record is created in the registry
- The person is added as a member of the household
- The household size is automatically updated

**Approval required:** Usually requires supervisor approval

**Example:**
> Maria's household is registered, but her newborn baby needs to be added. She submits an "Add Group Member" request with the baby's name, birth date, and relationship (child).

![](types/add_member_example.png)

---

### Edit Individual Information

**Purpose:** Update personal information for an existing individual.

**When to use:**
- Contact information changed (phone, email, address)
- Name spelling correction
- Correcting birth date
- Updating gender
- Any other personal detail that needs fixing

**Information you can update:**
- Given name and family name
- Date of birth
- Gender
- Phone number
- Email address
- Physical address (street, city, postal code)

**What happens when approved:**
- The individual's record is updated with the new information
- The old values are preserved in the audit trail

**Approval required:** Depends on what's being changed (phone updates may be auto-approved, but birth date changes require supervisor approval)

**Example:**
> John moved to a new address and got a new phone number. A registry officer submits an "Edit Individual Information" request to update both fields.

![](types/edit_individual_example.png)

---

### Edit Group Information

**Purpose:** Update details about a household or group.

**When to use:**
- Household moved to a new address
- Contact person changed
- Group name needs correction
- Updating household location or area

**Information you can update:**
- Group name
- Contact phone number
- Physical address
- Location/area code
- Representative or contact person

**What happens when approved:**
- The group record is updated
- All members remain linked to the group

**Approval required:** Usually requires supervisor approval

**Example:**
> The Patel household moved from Region A to Region B. A registry officer submits an "Edit Group Information" request to update their location and address.

![](types/edit_group_example.png)

---

### Add Child (Custom Type Example)

**Purpose:** Specialized form for adding a child to a household, with child-specific fields.

**When to use:**
- Specifically for adding children under 18
- When child protection data needs to be collected
- Program-specific child enrollment

**Information required:**
- Child's full name
- Date of birth
- Gender
- Relationship to household head
- Birth certificate number
- Mother's name and ID
- Father's name and ID (optional)
- Vaccination records (optional)

**What happens when approved:**
- Child record is created
- Child is linked to the household
- Eligibility for child-focused programs is automatically checked

**Approval required:** May require additional verification for child protection

**Example:**
> A household wants to enroll their newborn in a child nutrition program. A health worker submits an "Add Child" request with birth certificate details and parent information.

![](types/add_child_example.png)

```{note}
Not all organizations use this request type. Check with your implementer about which custom types are configured.
```

---

## Request Type Variations

Your organization may have configured additional request types or variations:

### By Target

| Request Type | Works On |
|--------------|----------|
| Individual Changes | Single person (e.g., Edit Individual Information) |
| Group Changes | Household or group (e.g., Edit Group Information, Add Member) |

### By Complexity

| Request Type | Approval Levels |
|--------------|-----------------|
| Simple Changes | Auto-approved or single approver (e.g., phone update) |
| Standard Changes | Single supervisor approval (e.g., add member) |
| Sensitive Changes | Multi-level approval (e.g., birth date correction) |

### By Source

| Request Type | Initiated By |
|--------------|--------------|
| Manual Entry | Registry officer in the office |
| Field Collection | Mobile app or event data collection |
| API Submission | External system integration |
| Self-Service | Registrant portal (future feature) |

## Choosing the Right Request Type

Follow this decision tree:

```
Are you changing an existing person's information?
├─ Yes → Edit Individual Information
└─ No → Are you adding someone to a household?
    ├─ Yes → Is it a child under 18?
    │   ├─ Yes → Add Child (if available)
    │   └─ No → Add Group Member
    └─ No → Are you changing household details?
        ├─ Yes → Edit Group Information
        └─ No → Contact your supervisor for guidance
```

## Request Type Details

### Required Documents

Some request types require supporting documents:

| Request Type | Usually Required Documents |
|--------------|---------------------------|
| Add Group Member | ID card or birth certificate for new member |
| Edit Individual Information | Depends on field being changed (ID for name/birth date changes) |
| Add Child | Birth certificate, parent IDs |
| Edit Group Information | Rarely requires documents |

### Processing Time

Typical approval times (varies by organization):

| Request Type | Approval Time |
|--------------|---------------|
| Simple phone/address updates | Same day (may be auto-approved) |
| Add member | 1-3 days |
| Name or birth date changes | 3-5 days (requires verification) |
| Sensitive changes | 5-10 days (multi-level approval) |

### Auto-Apply vs. Manual Apply

| Request Type | When Changes Are Applied |
|--------------|--------------------------|
| Most types | Automatically when approved |
| Complex types | May require manual application by administrator |
| Imports | Usually manual to allow final review |

## Request Status Flow

All request types follow the same status workflow:

1. **Draft** - Being created, not yet submitted
2. **Pending Approval** - Waiting for approver action
3. **Revision Requested** - Sent back to submitter for corrections
4. **Approved** - Approved and ready to apply
5. **Applied** - Changes have been made to the registrant record
6. **Rejected** - Request was denied

![](types/status_flow.png)

```{note}
Some request types may skip states. For example, auto-approved types go directly from Draft → Approved → Applied.
```

## Custom Request Types

Your organization may have custom request types configured for specific programs or operations:

- **Enrollment Changes** - Update program enrollment status
- **Payment Information** - Update bank account or mobile money details
- **Grievance Corrections** - Apply changes based on grievance resolution
- **Farm Updates** - Update farm size, crops, or livestock (for farmer registries)
- **Business Updates** - Update business details (for MSME registries)

Check with your implementer or administrator to learn about custom types in your system.

## Are You Stuck?

**Don't see the request type you need?**
It may not be configured yet. Contact your implementer to request a new change request type.

**Not sure which request type to use?**
Start with the decision tree above. If still unsure, ask your supervisor or create a draft of the most likely type and ask for feedback before submitting.

**Request type is grayed out?**
Check:
- Is the registrant an individual or group? Some types only work on one or the other.
- Do you have permission to use this request type?
- Has the request type been deactivated? Contact your administrator.

**Need to change multiple things at once?**
Submit multiple change requests. You can create several requests for the same registrant - they'll be processed in the order submitted.

**Request type form is missing fields I need?**
The form only shows fields configured for that request type. If you need additional fields, contact your implementer to modify the request type configuration.

**Want to create your own request type?**
Only implementers can create new request types. If you're an implementer, see the [Configure Change Request Types](../../config_guide/change_request_types/configure.md) guide.

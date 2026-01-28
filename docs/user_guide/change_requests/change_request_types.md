---
openspp:
  doc_status: draft
  products: [core]
  applies_to:
    - social_registry
    - sp_mis
---

# Change Request Types

**Applies to:** Social Registry, SP-MIS

This guide describes the different types of change requests available in OpenSPP. Each type has its own form and purpose.

## Overview

Request types define what changes you can make to registrant data. Your organization's administrator configures which types are available and what approval workflow each follows.

The types and fields described in this guide match the standard OpenSPP change request types (from `spp_cr_types_base` and `spp_cr_types_advanced`). Your deployment may enable a subset of these or add custom types.

Request types are divided into two categories:

- **Basic Types** - Simple field updates. These use field mapping and can be customized via **Studio** (e.g., add or hide fields, change labels). Types: Edit Individual Information, Edit Group Information, Update ID Document.
- **Advanced Types** - Complex operations that use custom logic (e.g., creating individuals, transferring memberships). These cannot be edited via Studio. Types: Add Group Member, Remove Group Member, Change Head of Household, Transfer Member, Exit Registrant, Create New Group, Split Household, Merge Registrants.

## Basic Request Types

These types update fields directly on the registrant record.

### Edit Individual Information

**Purpose:** Update personal information for an individual registrant.

**Target:** Individuals only

**When to Use:**

- Contact information changed (phone, email, address)
- Name spelling correction
- Correcting birth date or gender
- Updating address after a move

**Fields You Can Update:**

| Field | Description |
|-------|-------------|
| Given Name | Person's first name |
| Family Name | Person's surname |
| Date of Birth | Birth date |
| Gender | Gender identity |
| Phone | Contact phone number |
| Email | Email address |
| Address Line 1 | Street address |
| Address Line 2 | Apartment, unit, etc. |
| City | City name |
| Postal Code | ZIP or postal code |

**Example Use Case:**
> Maria moved to a new apartment and got a new phone number. The registry officer submits an "Edit Individual Information" request to update her address and phone.

---

### Edit Group Information

**Purpose:** Update information for a household or group.

**Target:** Groups/Households only

**When to Use:**

- Household moved to a new address
- Contact phone number changed
- Group name needs correction

**Fields You Can Update:**

| Field | Description |
|-------|-------------|
| Group Name | Household or group name |
| Phone | Contact phone number |
| Email | Contact email |
| Address Line 1 | Street address |
| Address Line 2 | Additional address info |
| City | City name |
| Postal Code | ZIP or postal code |

**Example Use Case:**
> The Patel household moved from one district to another. The registry officer submits an "Edit Group Information" request to update their address.

---

### Update ID Document

**Purpose:** Add, update, or remove identification documents.

**Target:** Both individuals and groups

**When to Use:**

- Adding a new ID number (national ID, passport, etc.)
- Correcting an ID number that was entered incorrectly
- Recording a renewed ID with a new expiration date
- Removing an invalid or expired ID

**Information Required:**

| Field | Description |
|-------|-------------|
| Operation | Add New ID, Update Existing ID, or Remove ID |
| ID Type | Type of identification (National ID, Passport, etc.) |
| ID Number/Value | The identification number |
| Expiry Date | When the ID expires (if applicable) |
| Description / Remarks | Optional notes |

**Example Use Case:**
> John received his new national ID card. The registry officer submits an "Update ID Document" request to add the ID number to his record.

---

## Advanced Request Types

These types involve more complex operations that create, modify, or link records.

### Add Group Member

**Purpose:** Add a new person to an existing household or group.

**Target:** Groups/Households only

**When to Use:**

- A baby was born
- Someone moved into the household
- A family member was missed during initial registration

**Information Required:**

| Field | Description |
|-------|-------------|
| Given Name | New member's first name |
| Family Name | New member's surname |
| Date of Birth | Birth date |
| Gender | Gender identity |
| Relationship | Role in household (Child, Spouse, Parent, etc.) |
| Phone | Contact phone (optional) |
| ID Number | National ID or other identification (optional) |

**What Happens When Approved:**

1. A new individual record is created in the registry
2. The person is added as a member of the household
3. The household size is automatically updated

**Example Use Case:**
> The Garcia household had a new baby. The health worker submits an "Add Group Member" request with the baby's name, birth date, and relationship (Child).

---

### Remove Group Member

**Purpose:** Remove a person from a household or group.

**Target:** Groups/Households only

**When to Use:**

- A family member moved out to their own household
- Correcting a person who was added to the wrong household
- Recording a death (the individual record is kept but membership ends)

**Information Required:**

| Field | Description |
|-------|-------------|
| Member to Remove | Select from current household members |
| Reason for Removal | Why the member is being removed (e.g., Left Household, Deceased, Married Out, Migrated, Data Correction, Other) |
| End Date | When the membership ended |

**What Happens When Approved:**

1. The membership is ended (not deleted, for audit purposes)
2. The household size is updated
3. The individual record remains in the system

**Example Use Case:**
> The eldest son in the Nguyen household got married and moved out. The registry officer submits a "Remove Group Member" request.

---

### Change Head of Household

**Purpose:** Designate a different person as the household head.

**Target:** Groups/Households only

**When to Use:**

- The current head passed away
- The current head moved out
- Correcting an incorrect head assignment

**Information Required:**

| Field | Description |
|-------|-------------|
| New Head of Household | Select from current household members |
| Previous Head's New Role | The role for the previous head after the change (e.g., Spouse, Other Adult) |
| Reason | Why the head is being changed (e.g., Head Deceased, Head Moved Out) |

**What Happens When Approved:**

1. The previous head's role changes from "Head" to another role (e.g., "Member")
2. The new head's role changes to "Head"

**Example Use Case:**
> The original household head passed away. The registry officer submits a "Change Head of Household" request to designate the spouse as the new head.

---

### Transfer Member

**Purpose:** Move a person from one household to another.

**Target:** Groups/Households only

**When to Use:**

- A person moves between registered households
- Correcting a person assigned to the wrong household

**Information Required:**

| Field | Description |
|-------|-------------|
| Member to Transfer | Select from source household members |
| Destination Household | The household they are moving to |
| New Relationship | Their role in the new household |
| Transfer Date | When the transfer takes effect |

**What Happens When Approved:**

1. Membership in the source household is ended
2. New membership in the destination household is created
3. Both household sizes are updated

**Example Use Case:**
> A child moves from their parents' household to live with grandparents (also registered). The registry officer submits a "Transfer Member" request.

---

### Exit Registrant

**Purpose:** Deactivate or exit a registrant from the system.

**Target:** Both individuals and groups

**When to Use:**

- A registrant has passed away
- A registrant has permanently left the program area
- A registrant requests to be removed from the registry
- A household has dissolved

**Information Required:**

| Field | Description |
|-------|-------------|
| Exit Reason | Why they are exiting (e.g., Deceased, Emigrated, Duplicate Record, No Longer Eligible, Voluntary Exit, Fraudulent Registration, Other) |
| Exit Date | When the exit takes effect |
| Remarks | Additional context. Date of Death and Destination Country may be required depending on exit reason. |

**What Happens When Approved:**

1. The registrant is marked as inactive
2. They no longer appear in active registrant lists
3. Their data is preserved for historical records
4. If exiting a group, all memberships are ended

**Example Use Case:**
> A household permanently relocated outside the country. The registry officer submits an "Exit Registrant" request for the household.

---

### Create New Group

**Purpose:** Create a new household or group from scratch.

**Target:** Groups/Households only

**When to Use:**

- Registering a new household through the change request workflow
- Creating a household for someone who was previously an individual

**Information Required:**

| Field | Description |
|-------|-------------|
| Group Name | Name for the new household |
| Group Type | Type of group (e.g., household), if configured |
| Head of Household | Select an existing individual as head, or create a new head with name, date of birth, gender, and phone |
| Address | Address Line 1, Address Line 2, City, State/Province, Postal Code |
| Phone | Contact phone number (for head or group) |

**What Happens When Approved:**

1. A new group record is created
2. If a head is specified, they are added as a member with "Head" role

**Example Use Case:**
> An individual is getting married and setting up their own household. The registry officer submits a "Create New Group" request.

---

### Split Household

**Purpose:** Divide one household into two separate households.

**Target:** Groups/Households only

**When to Use:**

- Part of a household is moving out to form a new household
- Correcting households that were incorrectly combined

**Information Required:**

| Field | Description |
|-------|-------------|
| Members to Transfer | Which members move to the new household |
| New Household Name | Name for the new household |
| New Head | Who will head the new household |

**What Happens When Approved:**

1. A new household is created
2. Selected members are transferred to the new household
3. Both household sizes are updated

**Example Use Case:**
> A large household is splitting because adult children are forming their own household. The registry officer submits a "Split Household" request.

---

### Merge Registrants

**Purpose:** Combine duplicate registrant records into one.

**Target:** Both individuals and groups

**When to Use:**

- The same person was registered twice
- Duplicate household records exist

**Information Required:**

| Field | Description |
|-------|-------------|
| Primary Record | The record to keep |
| Records to Merge | The duplicate records to merge in |
| Field Resolution | Which values to keep when conflicts exist |

**What Happens When Approved:**

1. Data from duplicate records is merged into the primary record
2. Duplicate records are deactivated (not deleted)
3. References to duplicates are updated to point to the primary

**Example Use Case:**
> A person was registered in two different locations. The registry officer submits a "Merge Registrants" request to combine the records.

---

## Quick Reference

| Request Type | Target | Complexity |
|--------------|--------|------------|
| Edit Individual Information | Individual | Basic |
| Edit Group Information | Group | Basic |
| Update ID Document | Both | Basic |
| Add Group Member | Group | Advanced |
| Remove Group Member | Group | Advanced |
| Change Head of Household | Group | Advanced |
| Transfer Member | Group | Advanced |
| Exit Registrant | Both | Advanced |
| Create New Group | Group | Advanced |
| Split Household | Group | Advanced |
| Merge Registrants | Both | Advanced |

## Choosing the Right Type

```
What do you need to do?
│
├─ Update information for ONE PERSON?
│  └─ Edit Individual Information
│
├─ Update information for a HOUSEHOLD?
│  └─ Edit Group Information
│
├─ Add or change ID DOCUMENTS?
│  └─ Update ID Document
│
├─ Add someone to a household?
│  └─ Add Group Member
│
├─ Remove someone from a household?
│  └─ Remove Group Member
│
├─ Change who is the household head?
│  └─ Change Head of Household
│
├─ Move someone between households?
│  └─ Transfer Member
│
├─ Deactivate a registrant?
│  └─ Exit Registrant
│
├─ Create a new household?
│  └─ Create New Group
│
├─ Split a household in two?
│  └─ Split Household
│
└─ Combine duplicate records?
   └─ Merge Registrants
```

## Are You Stuck?

**Request type you need is not listed?**
Your organization may not have all types enabled. Contact your administrator.

**Not sure which type to use?**
Follow the decision tree above. If still unsure, ask your supervisor.

**Need to do something not covered by any type?**
Contact your administrator. They may need to configure a new request type or use a different process.

**Request type is grayed out when selecting a registrant?**
Some types only work with individuals or only with groups. Make sure your registrant matches the request type's target.

## Next Steps

- {doc}`submit_change_request` - Learn how to submit a request
- {doc}`review_change_request` - Learn how validators review requests

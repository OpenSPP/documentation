---
openspp:
  doc_status: draft
  products: [core]
---

# Recording Consent

This guide is for **implementers** and **users** recording consent from beneficiaries. You'll learn how to create consent records and manage consent status.

## Navigate to Consent Records

Go to **Registry → Configuration → Consent Management → Consent Records**.

## Recording Individual Consent

### Step 1: Create New Consent Record

Click **New** to create a consent record.

### Step 2: Configure Basic Information

**BASIC INFO section:**

| Field | Value | Notes |
|-------|-------|-------|
| Consent Name | Maria Santos - Program Enrollment | Descriptive name |
| Data Subject | Maria Santos | The beneficiary |
| Privacy Notice | Social Protection Enrollment | Notice shown to beneficiary |
| Status | Given | Current consent status |
| Legal Basis | Consent | Why processing is allowed |

### Step 3: Configure Dates

| Field | Value | Notes |
|-------|-------|-------|
| Effective From | 2024-03-15 | When consent starts |
| Expiry Date | 2025-03-15 | When consent expires (required) |

```{note}
Consent must have an expiry date. Choose a reasonable period based on your program (typically 1-2 years). You can renew consent before it expires.
```

### Step 4: Record Collection Details

**COLLECTION section:**

| Field | Value | Notes |
|-------|-------|-------|
| Collection Method | Written/Signed Form | How consent was obtained |
| Indicated By | (leave empty or select) | Who gave consent if not the data subject |
| Delegation Type | Self | Relationship to data subject |

**Collection Methods:**

| Method | When to Use |
|--------|-------------|
| **Written/Signed Form** | Paper consent form signed |
| **Verbal (Witnessed)** | Verbal consent with witness |
| **Electronic/Digital** | Digital form, tablet, mobile app |
| **Biometric Confirmation** | Fingerprint or biometric |

**Delegation Types:**

| Type | When to Use |
|------|-------------|
| **Self** | Beneficiary signed for themselves |
| **Legal Guardian** | Court-appointed guardian signed |
| **Parent/Caretaker** | Parent signed for child |
| **Power of Attorney** | Legal representative signed |
| **Authorized Representative** | Other authorized person |

### Step 5: Configure Purposes

In the **Purposes** tab, select what the beneficiary consented to:

- Beneficiary Registration
- Eligibility Assessment
- Program Enrollment
- Benefit Delivery

### Step 6: Configure Data Recipients

**RECIPIENTS section:**

| Field | Value |
|-------|-------|
| Recipient Mode | Specific Organizations OR Organization Categories |

**If Specific Organizations:**
Select the exact partners who can receive data.

**If Organization Categories:**
Select types of organizations (e.g., "All UN Agencies", "Government Health Departments").

### Step 7: Attach Evidence

**EVIDENCE section:**

| Field | Value |
|-------|-------|
| Evidence Document | Upload signed form |
| Delegation Evidence | Upload authorization (if applicable) |

### Step 8: Save

Click **Save** to create the consent record.

## Consent Status Options

| Status | Meaning | When to Use |
|--------|---------|-------------|
| **Requested** | Awaiting beneficiary response | Consent form sent but not returned |
| **Given** | Beneficiary consented | Form signed, consent recorded |
| **Renewed** | Re-confirmed after expiry | Consent extended |
| **Refused** | Beneficiary declined | Consent explicitly refused |
| **Withdrawn** | Previously given, now revoked | Beneficiary revoked consent |
| **Expired** | Past expiry date | Auto-set when date passes |
| **Invalidated** | Voided | Consent invalid due to error/breach |

## Recording Consent in Bulk

For mass registration, use the **Bulk Consent Recording Wizard**.

### Step 1: Open Bulk Wizard

From the Consent Records list, click **Action → Bulk Record Consent**.

### Step 2: Configure Common Settings

| Field | Value |
|-------|-------|
| Privacy Notice | Select notice |
| Legal Basis | Consent |
| Collection Method | Electronic/Digital |
| Effective From | Today |
| Expiry Date | 1 year from today |
| Purposes | Select applicable purposes |

### Step 3: Select Beneficiaries

Choose beneficiaries from the list or filter by:
- Program membership
- Area
- Registration date

### Step 4: Execute

Click **Record Consent** to create records for all selected beneficiaries.

## Withdrawing Consent

When a beneficiary wants to withdraw consent:

### Step 1: Find the Consent Record

Search for the beneficiary's consent record.

### Step 2: Update Status

Change **Status** to "Withdrawn".

### Step 3: Record Withdrawal Details

| Field | Value |
|-------|-------|
| Withdrawn Date | Today |
| Withdrawn By | Person who requested withdrawal |
| Withdrawal Reason | Beneficiary's stated reason |
| Withdrawal Channel | How request was received |

**Withdrawal Channels:**
- Web Portal
- Mobile App
- API
- Paper Form
- Verbal Request

### Step 4: Stop Data Processing

After withdrawal, data processing must stop. The system will:
- Block API access for this beneficiary
- Flag records as consent withdrawn
- Log the withdrawal in consent history

## Renewing Consent

Before consent expires:

### Step 1: Find Expiring Consents

Go to **Registry → Configuration → Expired Consents** to see consents expiring soon.

### Step 2: Contact Beneficiaries

Reach out to collect renewed consent.

### Step 3: Update Record

Change **Status** to "Renewed" and update:
- New Expiry Date
- Collection Method
- Evidence (if new form signed)

## Consent for Children

For beneficiaries under 16:

1. Select the **child** as Data Subject
2. Select the **parent/guardian** as Indicated By
3. Set Delegation Type to "Parent/Caretaker" or "Legal Guardian"
4. Attach evidence of guardianship if required

## Viewing Consent History

Each consent record tracks version history:

1. Open a consent record
2. Click the **History** smart button
3. View all status changes with timestamps

## Are You Stuck?

**Can I change a consent record after saving?**

Yes, but changes are tracked in history. For significant changes, consider creating a new consent record.

**What happens when consent expires?**

Status automatically changes to "Expired". Data processing should stop until consent is renewed.

**How do I handle consent refusal?**

Set status to "Refused" and record the refusal reason. The beneficiary can still be registered but data sharing will be restricted.

**Can one beneficiary have multiple consent records?**

Yes, for different purposes or notices. For example, separate consent for program enrollment and research participation.

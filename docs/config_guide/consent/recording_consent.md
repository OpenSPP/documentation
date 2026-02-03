---
openspp:
  doc_status: draft
  products: [core]
---

# Recording consent

This guide is for **implementers** and **users** recording consent from beneficiaries. You'll learn how to create consent records and manage consent status.

## Navigate to consent records

Go to **Registry → Configuration → Consent Management → Consent Records**.

## Recording individual consent

### Step 1: Create new consent record

Click **New** to create a consent record.

### Step 2: Configure basic information

**Data Subject section:**

| Field | Value | Notes |
|-------|-------|-------|
| Consent Name | Maria Santos - Program Enrollment | Descriptive name |
| Data Subject | Maria Santos | The beneficiary |
| Privacy Notice | Social Protection Enrollment | Notice shown to beneficiary |
| Status | Given | Current consent status |
| Legal Basis | Consent | Why processing is allowed |

### Step 3: Configure dates

In the **Consent Details** tab → **Validity** section:

| Field | Value | Notes |
|-------|-------|-------|
| Effective From | 2024-03-15 | When consent starts |
| Expiry Date | 2025-03-15 | When consent expires (required) |

```{note}
Consent must have an expiry date. Choose a reasonable period based on your program (typically 1-2 years). You can renew consent before it expires.
```

### Step 4: Record collection details

In the **Consent Details** tab → **Collection** section:

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

### Step 5: Configure purposes

In the **Processing** tab → **Purposes** section, select what the beneficiary consented to:

- Beneficiary Registration
- Eligibility Assessment
- Program Enrollment
- Benefit Delivery

### Step 6: Configure data recipients

On the main form → **Data Recipients** section:

| Field | Value |
|-------|-------|
| Recipient Mode | Specific Organizations OR Organization Categories |

**If Specific Organizations:**
Select the exact partners who can receive data.

**If Organization Categories:**
Select types of organizations (e.g., "All UN Agencies", "Government Health Departments").

### Step 7: Attach evidence

In the **Consent Details** tab → **Evidence** section:

| Field | Value |
|-------|-------|
| Evidence Document | Upload signed form |
| Delegation Evidence | Upload authorization (if applicable) |

### Step 8: Save and give consent

Click **Save** to create the consent record. Then click **Record Consent Given** to change status from "Requested" to "Given".

```{important}
Once status is "Given", consent terms become **immutable**. The parties, purposes, recipients, dates, and collection method cannot be changed. To correct errors, invalidate the consent and create a new one.
```

## Consent status options

| Status | Meaning | When to Use |
|--------|---------|-------------|
| **Requested** | Awaiting beneficiary response | Consent form sent but not returned |
| **Given** | Beneficiary consented | Form signed, consent recorded |
| **Renewed** | Re-confirmed after expiry | Consent extended |
| **Refused** | Beneficiary declined | Consent explicitly refused |
| **Withdrawn** | Previously given, now revoked | Beneficiary revoked consent |
| **Expired** | Past expiry date | Auto-set when date passes |
| **Invalidated** | Voided | Consent invalid due to error/breach |

## Recording consent in bulk

For mass registration, use the **Bulk Consent Recording Wizard**.

### Step 1: Open bulk wizard

From the Consent Records list, click **Action → Bulk Record Consent**.

### Step 2: Configure common settings

| Field | Value |
|-------|-------|
| Privacy Notice | Select notice |
| Legal Basis | Consent |
| Collection Method | Electronic/Digital |
| Effective From | Today |
| Expiry Date | 1 year from today |
| Purposes | Select applicable purposes |

### Step 3: Select beneficiaries

Choose beneficiaries from the list or filter by:
- Program membership
- Area
- Registration date

### Step 4: Execute

Click **Record Consent** to create records for all selected beneficiaries.

## Withdrawing consent

When a beneficiary wants to withdraw consent:

### Step 1: Find the consent record

Search for the beneficiary's consent record.

### Step 2: Click withdraw button

Click the **Withdraw Consent** button in the header (only visible when status is "Given" or "Renewed").

### Step 3: Record withdrawal details

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

### Step 4: System actions

After withdrawal, the system automatically:
- Updates `consent_summary` cache
- Blocks API access for this beneficiary
- Logs the withdrawal in consent history with timestamp and user

## Renewing consent

Before consent expires:

### Step 1: Find expiring consents

Go to **Registry → Configuration → Expired Consents** to see consents expiring soon.

### Step 2: Contact beneficiaries

Reach out to collect renewed consent.

### Step 3: Click renew button

Open the consent record and click **Renew Consent** button. The system will:
- Change status to "Renewed"
- Record the renewal in history
- Update consent summary cache

You can optionally update the expiry date when renewing.

## Consent for children

For beneficiaries under 16:

1. Select the **child** as Data Subject
2. Select the **parent/guardian** as Indicated By
3. Set Delegation Type to "Parent/Caretaker" or "Legal Guardian"
4. Attach evidence of guardianship if required

## Viewing consent history

Each consent record tracks version history:

1. Open a consent record
2. Click the **History** smart button (shows count of history entries)
3. View all status changes with timestamps, users, and reasons

The history includes:
- Status changes (requested → given → withdrawn, etc.)
- Who made each change
- When changes occurred
- IP address and channel (for electronic consent)

## Are you stuck?

**Can I change a consent record after saving?**

You can only modify consent terms while status is "Requested". Once status changes to "Given", consent terms are **locked** to preserve the legal agreement. To correct errors, invalidate the consent and create a new one.

**What happens when consent expires?**

Status automatically changes to "Expired". Data processing should stop until consent is renewed.

**How do I handle consent refusal?**

Set status to "Refused" and record the refusal reason. The beneficiary can still be registered but data sharing will be restricted.

**Can one beneficiary have multiple consent records?**

Yes, for different purposes or notices. For example, separate consent for program enrollment and research participation.

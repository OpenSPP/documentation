---
openspp:
  doc_status: draft
  products: [core]
---

# Configuring Privacy Notices

This guide is for **implementers** creating privacy notice templates in OpenSPP. Privacy notices explain to beneficiaries how their data will be used.

## What is a Privacy Notice?

A privacy notice is a document that tells beneficiaries:
- What personal data you collect
- Why you collect it (purposes)
- Who you may share it with
- How long you keep it
- Their rights regarding their data
- How to withdraw consent

## Navigate to Privacy Notices

Go to **Registry → Configuration → Consent Management → Configuration → Privacy Notices**.

## Creating a Privacy Notice

### Step 1: Create New Notice

Click **New** and configure the basic information.

**BASIC INFO section:**

| Field | Value | Notes |
|-------|-------|-------|
| Name | Social Protection Enrollment | User-facing name |
| Code | `SP_ENROLLMENT` | Unique identifier (uppercase, underscores) |
| Version | 1.0 | Version number |
| Effective Date | 2024-01-01 | When notice becomes active |
| Language | English | Notice language |
| State | Draft | Draft / Active / Archived |

### Step 2: Write Notice Content

**CONTENT section:**

| Field | Description |
|-------|-------------|
| **Summary** | Brief overview (shown first to beneficiaries) |
| **Full Notice Text** | Complete privacy notice (HTML supported) |
| **Purpose Description** | Explanation of why data is collected |
| **Data Categories** | What types of data are collected |
| **Recipients** | Who data may be shared with |
| **Retention Period** | How long data is kept |
| **Data Subject Rights** | Beneficiary's rights under applicable law |
| **How to Withdraw** | Instructions for withdrawing consent |

**Example Summary:**
```
We collect your personal information to register you for social protection
programs, assess your eligibility, and deliver benefits. Your data may be
shared with partner organizations providing services. You can withdraw
consent at any time by contacting our office.
```

### Step 3: Configure Purposes

In the **Purposes** tab, select which processing purposes this notice covers:

| Purpose | Select If... |
|---------|--------------|
| Beneficiary Registration | Collecting registration data |
| Eligibility Assessment | Determining program eligibility |
| Program Enrollment | Enrolling in programs |
| Benefit Delivery | Delivering cash/in-kind benefits |
| Grievance Handling | Managing complaints |
| Data Sharing | Sharing with partners |
| Research and Evaluation | Using data for studies |

### Step 4: Configure Data Categories

In the **Data Categories** tab, select what personal data is covered:

- Identifying Information (name, ID numbers)
- Contact Information (phone, address)
- Demographic Information (age, gender)
- Financial Information (income, assets)
- Health Information (if applicable)
- Location Data (GPS coordinates)

### Step 5: Configure Allowed Recipients

In the **Allowed Recipient Types** tab, select organization categories that may receive data:

- Government Agencies
- UN Agencies
- NGOs
- Financial Service Providers
- Healthcare Providers

### Step 6: Add Contact Information

**CONTACT INFO section:**

| Field | Value |
|-------|-------|
| Data Protection Officer Contact | dpo@agency.gov |
| Contact Email | privacy@agency.gov |
| Contact URL | https://agency.gov/privacy |
| Full Privacy Policy URL | https://agency.gov/privacy-policy |

### Step 7: Specify Legal Context

**LEGAL section:**

| Field | Value |
|-------|-------|
| Jurisdiction | KE (Kenya) |
| Applicable Law | Kenya Data Protection Act 2019 |

### Step 8: Activate the Notice

Once complete, change **State** from "Draft" to "Active".

```{note}
You cannot edit an active notice. To make changes, create a new version using the **Supersedes** field to link to the previous version.
```

## Privacy Notice States

| State | Description | Can Edit? |
|-------|-------------|-----------|
| **Draft** | Being prepared | Yes |
| **Active** | In use for new consents | No |
| **Archived** | No longer used | No |

## Versioning Notices

When you need to update a privacy notice:

1. Create a new notice
2. Set **Supersedes** to the previous version
3. Increment the **Version** number
4. Activate the new notice
5. Archive the old notice

Existing consent records retain their original notice version for audit purposes.

## Multi-Language Support

OpenSPP supports privacy notices in multiple languages:

| Language | Code |
|----------|------|
| English | en |
| French | fr |
| Spanish | es |
| Arabic | ar |
| Swahili | sw |

Create separate notices for each language with the same **Code** but different **Language** setting.

## Sample Privacy Notices

OpenSPP includes sample notices you can customize:

| Sample | Purpose |
|--------|---------|
| **Program Enrollment** | General program registration |
| **Beneficiary Verification** | Identity verification |
| **Data Sharing** | Partner data sharing |
| **Research Evaluation** | Impact studies |

## Are You Stuck?

**Can't edit an active notice?**

Active notices are locked to preserve the version beneficiaries agreed to. Create a new version instead.

**How do I translate a notice?**

Create a new notice with the same Code but different Language. The system matches notices by code and language.

**What if I need to update the notice for all beneficiaries?**

Create a new version and re-collect consent. You cannot retroactively change what someone agreed to.

**How detailed should the notice be?**

Enough for beneficiaries to understand data use, but not so long they won't read it. Use the Summary for key points and Full Notice for details.

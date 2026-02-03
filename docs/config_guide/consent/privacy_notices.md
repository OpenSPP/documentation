---
openspp:
  doc_status: draft
  products: [core]
---

# Configuring privacy notices

This guide is for **implementers** creating privacy notice templates in OpenSPP. Privacy notices explain to beneficiaries how their data will be used.

## What is a privacy notice?

A privacy notice is a document that tells beneficiaries:
- What personal data you collect
- Why you collect it (purposes)
- Who you may share it with
- How long you keep it
- Their rights regarding their data
- How to withdraw consent

Privacy notices implement ISO/IEC 29184:2020 and serve as the **boundary** for consent - beneficiaries can only consent to terms described in the notice.

## Navigate to privacy notices

Go to **Registry → Configuration → Consent Management → Configuration → Privacy Notices**.

## Creating a privacy notice

### Step 1: Create new notice

Click **New** and configure the basic information.

| Field | Value | Notes |
|-------|-------|-------|
| Name | Social Protection Enrollment | User-facing name |
| Code | `SP_ENROLLMENT` | Unique identifier (uppercase, underscores) |
| Version | 1.0 | Version number |
| Effective Date | 2024-01-01 | When notice becomes active |
| Language | English | Notice language |
| Jurisdiction | KE | Legal jurisdiction |
| Applicable Law | Kenya Data Protection Act 2019 | Governing law |

### Step 2: Write notice content

In the **Summary** and **Full Notice** tabs:

| Field | Description |
|-------|-------------|
| **Summary** | Brief overview (shown first to beneficiaries) |
| **Full Notice Text** | Complete privacy notice (HTML supported) |

**Example summary:**
```text
We collect your personal information to register you for social protection
programs, assess your eligibility, and deliver benefits. Your data may be
shared with partner organizations providing services. You can withdraw
consent at any time by contacting our office.
```

### Step 3: Configure purposes

In the **DPV Taxonomy** tab → **Purposes** section, select which processing purposes this notice covers:

**Social protection purposes:**

| Purpose | Select if... |
|---------|--------------|
| Beneficiary Registration | Collecting registration data |
| Eligibility Assessment | Determining program eligibility |
| Program Enrollment | Enrolling in programs |
| Benefit Delivery | Delivering cash/in-kind benefits |
| Grievance Handling | Managing complaints |
| Case Management | Referrals and case tracking |
| Monitoring & Evaluation | Program impact measurement |
| Deduplication | Detecting duplicate registrations |
| Inter-Agency Data Sharing | Sharing with partner agencies |

**General DPV purposes:**

| Purpose | Select if... |
|---------|--------------|
| Service Provision | General service delivery |
| Identity Verification | Verifying beneficiary identity |
| Research and Development | Research and studies |
| Legal Compliance | Required by law |

### Step 4: Configure data categories

In the **DPV Taxonomy** tab → **Data Categories** section, select what personal data is covered:

**Basic categories:**
- Identifying Data (name, ID numbers, photo)
- Demographic Data (age, gender, marital status)
- Contact Data (phone, address, email)
- Location Data (GPS coordinates, region)
- Financial Data (income, bank account)
- Family Data (household members, dependents)

**Sensitive categories (GDPR Article 9):**
- Health Data (medical conditions, disabilities)
- Biometric Data (fingerprints, facial features)
- Genetic Data
- Racial/Ethnic Origin
- Religious Beliefs

**Social protection-specific:**
- Vulnerability Assessment Data
- Program Enrollment Data
- Benefit History Data
- Livelihood Data

### Step 5: Configure allowed recipients

In the **Consent Boundaries** tab → **Allowed Recipient Types** section, select organization categories that may receive data:

| Type | Description |
|------|-------------|
| Government Agency | National/local government bodies |
| NGO / Non-Profit | National non-governmental organizations |
| International NGO | INGOs like Red Cross, Save the Children |
| UN Agency | WFP, UNHCR, UNICEF, etc. |
| Private Sector | Commercial entities (often excluded) |
| Research Institution | Universities and research institutes |

### Step 6: Configure ISO 29184 elements

In the **ISO 29184 Elements** tab, provide detailed descriptions for compliance:

| Field | Description |
|-------|-------------|
| **Controller Info** | Data controller identity and contact |
| **Purpose Description** | Detailed explanation of processing purposes |
| **Data Categories Description** | What personal data is collected |
| **Recipients Description** | Who data may be shared with |
| **Retention Description** | How long data is kept |
| **Rights Description** | Data subject rights under applicable law |
| **Withdrawal Description** | How to withdraw consent |

### Step 7: Add contact information

In the **Contact** tab:

| Field | Value |
|-------|-------|
| Contact Email | privacy@agency.gov |
| Contact URL | https://agency.gov/privacy |
| Full Privacy Policy URL | https://agency.gov/privacy-policy |
| DPO Contact | dpo@agency.gov |

### Step 8: Specify legal context

On the main form:

| Field | Value |
|-------|-------|
| Jurisdiction | KE (Kenya) |
| Applicable Law | Kenya Data Protection Act 2019 |

### Step 9: Activate the notice

Once complete, click the **Activate** button in the header.

```{important}
You cannot edit an active notice. To make changes, create a new version using the **Supersedes** field to link to the previous version.
```

## Privacy notice states

| State | Description | Can edit? |
|-------|-------------|-----------|
| **Draft** | Being prepared | Yes |
| **Active** | In use for new consents | No |
| **Archived** | No longer used | No |

## Versioning notices

When you need to update a privacy notice:

1. Create a new notice
2. Set **Supersedes** to the previous version
3. Increment the **Version** number
4. Activate the new notice
5. Archive the old notice

Existing consent records retain their original notice version for audit purposes.

## Multi-language support

OpenSPP supports privacy notices in multiple languages:

| Language | Code |
|----------|------|
| English | en |
| French | fr |
| Spanish | es |
| Arabic | ar |
| Swahili | sw |

Create separate notices for each language with the same **Code** but different **Language** setting.

## Are you stuck?

**Can't edit an active notice?**

Active notices are locked to preserve the version beneficiaries agreed to. Create a new version instead.

**How do I translate a notice?**

Create a new notice with the same Code but different Language. The system matches notices by code and language.

**What if I need to update the notice for all beneficiaries?**

Create a new version and re-collect consent. You cannot retroactively change what someone agreed to.

**How detailed should the notice be?**

Enough for beneficiaries to understand data use, but not so long they won't read it. Use the Summary for key points and Full Notice for details.

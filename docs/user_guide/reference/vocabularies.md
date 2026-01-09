---
openspp:
  doc_status: draft
  products: [core]
  applies_to:
    - social_registry
    - sp_mis
    - drims
---

# Vocabularies (Code Lists)

**Applies to:** Social Registry, SP-MIS, DRIMS

## What You'll Find Here

This reference guide explains vocabularies (controlled code lists) used in OpenSPP. You'll learn:

- What vocabularies are and why they matter
- Standard codes for gender, marital status, relationships, and more
- How to interpret codes in dropdown fields

## What Are Vocabularies?

Vocabularies are standardized lists of codes used throughout OpenSPP. They ensure:

- **Consistency** - Everyone uses the same codes for the same concepts
- **Interoperability** - Data can be shared with other systems
- **Accuracy** - Reduces data entry errors

When you see a dropdown field (like Gender or Marital Status), the options come from a vocabulary.

## Standard Vocabularies

OpenSPP includes vocabularies based on international standards. These "system vocabularies" cannot be changed to ensure data consistency.

### Gender (ISO 5218)

Used when recording a person's gender.

| Code | Display | Description |
|------|---------|-------------|
| 0 | Not Known | Gender is unknown |
| 1 | Male | Male |
| 2 | Female | Female |
| 9 | Not Applicable | Not applicable |

Based on ISO 5218 international standard.

### Marital Status (UN Census)

Used when recording a person's marital status.

| Code | Display | Description |
|------|---------|-------------|
| S | Never Married | Never entered into a marriage |
| M | Married | Currently married |
| W | Widowed | Spouse has died, not remarried |
| D | Divorced | Marriage legally dissolved |
| L | Separated | Married but living apart |
| C | Consensual Union | Living together without formal marriage |

Based on UN Principles and Recommendations for Population and Housing Censuses.

### Relationship Type

Used when recording how household members are related.

| Code | Display | Who Uses This |
|------|---------|---------------|
| head | Head of Household | The primary person in a household |
| spouse | Spouse/Partner | Married or domestic partner of the head |
| child | Child | Son or daughter (biological, adopted, or step) |
| child_in_law | Son/Daughter-in-law | Spouse of a child |
| grandchild | Grandchild | Child of a child |
| parent | Parent | Mother or father of the head |
| parent_in_law | Parent-in-law | Parent of spouse |
| grandparent | Grandparent | Parent of a parent |
| sibling | Sibling | Brother or sister |
| other_relative | Other Relative | Other family relationship |
| non_relative | Non-Relative | Not related by blood or marriage |

### ID Type

Used when recording identification documents.

| Code | Display | Description |
|------|---------|-------------|
| national_id | National ID | Government-issued national ID |
| passport | Passport | International travel document |
| tax_id | Tax ID | Tax identification number |
| birth_certificate | Birth Certificate | Official birth certificate |

### Group Type

Used when classifying the type of group being registered.

| Code | Display | Description |
|------|---------|-------------|
| household | Household | People living together and sharing resources |
| family | Family | People related by blood, marriage, or adoption |

### Education Level (UNESCO ISCED 2011)

Used when recording a person's education level.

| Code | Display | Description |
|------|---------|-------------|
| N | No Formal Education | Never attended formal education |
| 0 | Early Childhood Education | Pre-primary education |
| 1 | Primary Education | Elementary school |
| 2 | Lower Secondary Education | Middle school / Junior high |
| 3 | Upper Secondary Education | High school |
| 4 | Post-Secondary Non-Tertiary | Technical/vocational after high school |
| 5 | Short-Cycle Tertiary | Associate degree / 2-year college |
| 6 | Bachelor's or Equivalent | 4-year university degree |
| 7 | Master's or Equivalent | Graduate degree |
| 8 | Doctoral or Equivalent | PhD or equivalent |
| 9 | Not Stated / Unknown | Unknown or not collected |

Based on UNESCO ISCED 2011 international standard.

### Economic Activity Status (ILO)

Used when recording a person's employment status.

| Code | Display | Description |
|------|---------|-------------|
| employed | Employed | Currently working for pay |
| employer | Employer | Owns business with employees |
| own_account | Own-Account Worker | Self-employed without employees |
| employee | Permanent Employee | Regular employee with contract |
| casual | Casual / Day Labourer | Temporary or irregular work |
| contributing_family | Contributing Family Worker | Works in family business unpaid |
| unemployed | Unemployed | Seeking work but not employed |
| student | Student | Full-time student |
| homemaker | Homemaker / Care Provider | Unpaid household duties |
| retired | Retired / Pensioner | Retired from work |
| unable_to_work | Unable to Work | Cannot work due to disability/illness |
| below_working_age | Below Working Age | Under minimum working age |

Based on ILO international labor standards.

## Vocabulary Domains

Vocabularies are organized by domain:

| Domain | Description | Examples |
|--------|-------------|----------|
| Core | Basic registrant information | Gender, Marital Status, ID Type |
| Education | Educational attainment | Education Level |
| Labor | Employment and economic activity | Economic Activity Status |
| Health | Health-related codes | (varies by deployment) |
| Agriculture | Farming and agriculture | (varies by deployment) |

## How Vocabularies Appear in Forms

When filling out forms, vocabulary values appear in dropdown fields:

1. Click the dropdown field
2. Select the appropriate value from the list
3. The display name is shown, but the code is stored

The system stores the code (like "M" for Married) but shows the display name (like "Married") for readability.

## System vs Custom Vocabularies

| Type | Can Edit? | Examples |
|------|-----------|----------|
| System | No | Gender, Marital Status, Education Level |
| Custom | Yes (admin only) | Country-specific codes, local extensions |

System vocabularies are based on international standards and cannot be modified to ensure data consistency.

Custom vocabularies can be created by administrators for country-specific needs.

## Are You Stuck?

**Can't find the right code in a dropdown?**

- The code may not apply to your situation. Select the closest option or "Other/Unknown."
- Contact your administrator if a needed code is missing.

**Not sure which code to select?**

- Read the descriptions in the tables above.
- Ask the beneficiary to clarify their situation.
- When in doubt, document the situation in notes and select the closest match.

**Dropdown shows codes instead of names?**

- This may be a display issue. Contact your administrator.
- The system may be showing the code format. The data is still correct.

**Need a code that doesn't exist?**

- System vocabularies cannot be changed. Select "Other" if available.
- Custom vocabularies can be extended by your administrator.
- Document the specific situation in the notes field.

## Related Topics

- Registering individuals (see User Guides)
- Understanding registrant information (see User Guides)

---
openspp:
  doc_status: draft
  products: [core]
---

# Standard Vocabularies

This guide is for **implementers** who need to understand which standard vocabularies are available in OpenSPP and what codes they contain.

## Overview

OpenSPP V2 includes standard vocabularies based on international standards. These are **system vocabularies** (read-only) that ensure data consistency and interoperability.

**Why standards?** Using internationally recognized vocabularies means:
- Your data can be shared with other systems (WHO, ILO, government agencies)
- Reports are comparable across countries
- No need to reinvent classification systems
- Automatic compliance with international requirements

## Core Vocabularies

### ISO 5218: Gender

Internationally standardized codes for representing biological sex.

| Code | Display | URI |
|------|---------|-----|
| 0 | Not Known | `urn:iso:std:iso:5218#0` |
| 1 | Male | `urn:iso:std:iso:5218#1` |
| 2 | Female | `urn:iso:std:iso:5218#2` |
| 9 | Not Applicable | `urn:iso:std:iso:5218#9` |

**Namespace:** `urn:iso:std:iso:5218`
**Reference:** [ISO 5218 Standard](https://www.iso.org/standard/36266.html)
**Use in:** Individual registration, household members, beneficiary data

**Note:** Some deployments extend this with additional gender identity codes (non-binary, other, prefer not to say) using local vocabularies.

### Relationship Types

Household and family relationship classifications.

**Individual-to-Individual Relationships:**

| Code | Display | URI |
|------|---------|-----|
| head | Head of Household | `urn:openspp:vocab:relationship#head` |
| spouse | Spouse/Partner | `urn:openspp:vocab:relationship#spouse` |
| child | Child | `urn:openspp:vocab:relationship#child` |
| child_in_law | Son/Daughter-in-law | `urn:openspp:vocab:relationship#child_in_law` |
| grandchild | Grandchild | `urn:openspp:vocab:relationship#grandchild` |
| parent | Parent | `urn:openspp:vocab:relationship#parent` |
| parent_in_law | Parent-in-law | `urn:openspp:vocab:relationship#parent_in_law` |
| grandparent | Grandparent | `urn:openspp:vocab:relationship#grandparent` |
| sibling | Sibling | `urn:openspp:vocab:relationship#sibling` |
| other_relative | Other Relative | `urn:openspp:vocab:relationship#other_relative` |
| non_relative | Non-Relative | `urn:openspp:vocab:relationship#non_relative` |

**Group-to-Group Relationships:**

| Code | Display | URI |
|------|---------|-----|
| parent_organization | Parent Organization | `urn:openspp:vocab:relationship#parent_organization` |
| subsidiary | Subsidiary | `urn:openspp:vocab:relationship#subsidiary` |
| partner_organization | Partner Organization | `urn:openspp:vocab:relationship#partner_organization` |
| affiliated_with | Affiliated With | `urn:openspp:vocab:relationship#affiliated_with` |

**Namespace:** `urn:openspp:vocab:relationship`
**Reference:** OpenSPP-specific (no international standard)
**Use in:** Household member relationships, beneficiary household composition, organizational relationships

### Marital Status

Based on UN Population Census Principles.

| Code | Display | URI |
|------|---------|-----|
| S | Never Married | `urn:un:unsd:pop-census:marital-status#S` |
| M | Married | `urn:un:unsd:pop-census:marital-status#M` |
| W | Widowed | `urn:un:unsd:pop-census:marital-status#W` |
| D | Divorced | `urn:un:unsd:pop-census:marital-status#D` |
| L | Separated | `urn:un:unsd:pop-census:marital-status#L` |
| C | Consensual Union | `urn:un:unsd:pop-census:marital-status#C` |

**Namespace:** `urn:un:unsd:pop-census:marital-status`
**Reference:** [UN Census Recommendations](https://unstats.un.org/unsd/demographic/sources/census/)
**Use in:** Individual demographics, eligibility criteria (widows programs, etc.)

### ID Types

Standard identification document classifications.

| Code | Display | URI |
|------|---------|-----|
| national_id | National ID | `urn:openspp:vocab:id-type#national_id` |
| passport | Passport | `urn:openspp:vocab:id-type#passport` |
| tax_id | Tax ID | `urn:openspp:vocab:id-type#tax_id` |
| birth_certificate | Birth Certificate | `urn:openspp:vocab:id-type#birth_certificate` |

**Namespace:** `urn:openspp:vocab:id-type`
**Reference:** OpenSPP-specific
**Use in:** ID document tracking, identity verification, deduplication

```{note}
Deployments can extend this vocabulary with additional ID types (e.g., driver's license, voter ID, social security card) using custom vocabularies or local extensions. See {doc}`custom` for details.
```

## Geographic Vocabularies

### ISO 3166: Countries

ISO standard country codes.

**Sample codes:**

| Alpha-2 | Alpha-3 | Numeric | Country Name | URI |
|---------|---------|---------|--------------|-----|
| PH | PHL | 608 | Philippines | `urn:iso:std:iso:3166-1#PH` |
| KE | KEN | 404 | Kenya | `urn:iso:std:iso:3166-1#KE` |
| US | USA | 840 | United States | `urn:iso:std:iso:3166-1#US` |
| GB | GBR | 826 | United Kingdom | `urn:iso:std:iso:3166-1#GB` |

**Namespace:** `urn:iso:std:iso:3166-1`
**Reference:** [ISO 3166](https://www.iso.org/iso-3166-country-codes.html)
**Use in:** Address data, nationality, country of origin
**Total codes:** 249 countries and territories

### ISO 639: Languages

ISO standard language codes.

**Sample codes:**

| Code | Language | URI |
|------|----------|-----|
| en | English | `urn:iso:std:iso:639#en` |
| es | Spanish | `urn:iso:std:iso:639#es` |
| fr | French | `urn:iso:std:iso:639#fr` |
| ar | Arabic | `urn:iso:std:iso:639#ar` |
| zh | Chinese | `urn:iso:std:iso:639#zh` |
| tl | Tagalog | `urn:iso:std:iso:639#tl` |
| sw | Swahili | `urn:iso:std:iso:639#sw` |

**Namespace:** `urn:iso:std:iso:639`
**Reference:** [ISO 639](https://www.iso.org/iso-639-language-codes.html)
**Use in:** Preferred language, multilingual forms, translation requirements
**Total codes:** 180+ major languages

### ISO 4217: Currencies

ISO standard currency codes.

**Sample codes:**

| Code | Currency | Country/Region | URI |
|------|----------|----------------|-----|
| USD | US Dollar | United States | `urn:iso:std:iso:4217#USD` |
| EUR | Euro | European Union | `urn:iso:std:iso:4217#EUR` |
| PHP | Philippine Peso | Philippines | `urn:iso:std:iso:4217#PHP` |
| KES | Kenyan Shilling | Kenya | `urn:iso:std:iso:4217#KES` |
| GBP | Pound Sterling | United Kingdom | `urn:iso:std:iso:4217#GBP` |

**Namespace:** `urn:iso:std:iso:4217`
**Reference:** [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html)
**Use in:** Entitlement amounts, payment programs, financial tracking
**Total codes:** 170+ currencies

## Disability & Health

### Washington Group: Disability Domain

Washington Group Short Set disability functional domains.

| Code | Display | URI |
|------|---------|-----|
| seeing | Seeing | `urn:wg:disability:domain#seeing` |
| hearing | Hearing | `urn:wg:disability:domain#hearing` |
| walking | Walking | `urn:wg:disability:domain#walking` |
| remembering | Remembering | `urn:wg:disability:domain#remembering` |
| selfcare | Self-care | `urn:wg:disability:domain#selfcare` |
| communicating | Communicating | `urn:wg:disability:domain#communicating` |

**Namespace:** `urn:wg:disability:domain`
**Reference:** [Washington Group](https://www.washingtongroup-disability.com/)
**Use in:** Disability screening, functional assessment

### Washington Group: Disability Severity

Severity levels for Washington Group assessments.

| Code | Display | URI |
|------|---------|-----|
| no_difficulty | No difficulty | `urn:wg:disability:severity#no_difficulty` |
| some_difficulty | Some difficulty | `urn:wg:disability:severity#some_difficulty` |
| a_lot_of_difficulty | A lot of difficulty | `urn:wg:disability:severity#a_lot_of_difficulty` |
| cannot_do_at_all | Cannot do at all | `urn:wg:disability:severity#cannot_do_at_all` |

**Namespace:** `urn:wg:disability:severity`
**Use in:** Disability severity assessment, targeting criteria

### Disability Status

General disability status classification.

**Namespace:** `urn:openspp:vocab:disability-status`
**Use in:** Quick disability identification

## Labor & Education

### ILO ISCO-08: Occupations

International Labour Organization - International Standard Classification of Occupations.

**Sample codes (hierarchical):**

| Code | Display | Level | URI |
|------|---------|-------|-----|
| 1 | Managers | Major group | `urn:ilo:isco-08#1` |
| 11 | Chief executives, senior officials | Sub-major | `urn:ilo:isco-08#11` |
| 111 | Legislators and senior officials | Minor | `urn:ilo:isco-08#111` |
| 1111 | Legislators | Unit | `urn:ilo:isco-08#1111` |
| 5 | Service and sales workers | Major | `urn:ilo:isco-08#5` |
| 51 | Personal service workers | Sub-major | `urn:ilo:isco-08#51` |
| 511 | Travel attendants, conductors | Minor | `urn:ilo:isco-08#511` |
| 5111 | Travel attendants | Unit | `urn:ilo:isco-08#5111` |

**Namespace:** `urn:ilo:isco-08`
**Reference:** [ILO ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/)
**Use in:** Employment tracking, labor market programs, skills assessment
**Total codes:** 400+ occupation codes (4-level hierarchy)

### UNESCO ISCED 2011: Education Levels

UNESCO International Standard Classification of Education.

| Code | Display | URI |
|------|---------|-----|
| 0 | Early childhood education | `urn:unesco:isced:2011#0` |
| 1 | Primary education | `urn:unesco:isced:2011#1` |
| 2 | Lower secondary education | `urn:unesco:isced:2011#2` |
| 3 | Upper secondary education | `urn:unesco:isced:2011#3` |
| 4 | Post-secondary non-tertiary | `urn:unesco:isced:2011#4` |
| 5 | Short-cycle tertiary | `urn:unesco:isced:2011#5` |
| 6 | Bachelor's or equivalent | `urn:unesco:isced:2011#6` |
| 7 | Master's or equivalent | `urn:unesco:isced:2011#7` |
| 8 | Doctoral or equivalent | `urn:unesco:isced:2011#8` |

**Namespace:** `urn:unesco:isced:2011`
**Reference:** [UNESCO ISCED](http://uis.unesco.org/en/topic/international-standard-classification-education-isced)
**Use in:** Education level tracking, scholarship programs, education targeting
**Total codes:** 9 main levels + sub-levels

## Agriculture (Optional Module)

### FAO AGROVOC: Crops

FAO Agricultural Thesaurus (subset for common crops).

**Sample codes:**

| Code | Display | URI |
|------|---------|-----|
| c_6599 | Rice | `urn:fao:agrovoc#c_6599` |
| c_12332 | Maize (Corn) | `urn:fao:agrovoc#c_12332` |
| c_8373 | Wheat | `urn:fao:agrovoc#c_8373` |
| c_4849 | Millet | `urn:fao:agrovoc#c_4849` |
| c_10999 | Cassava | `urn:fao:agrovoc#c_10999` |
| c_6214 | Potato | `urn:fao:agrovoc#c_6214` |

**Namespace:** `urn:fao:agrovoc`
**Reference:** [FAO AGROVOC](https://agrovoc.fao.org/)
**Use in:** Farmer registries, agricultural programs, crop tracking
**Total codes:** 1,000+ crop and livestock terms
**Note:** Available only when `spp_registry_farmer` module is installed

## Additional System Vocabularies

OpenSPP includes additional system vocabularies for specialized use cases:

| Vocabulary | Namespace | Domain | Description |
|------------|-----------|--------|-------------|
| Group Type | `urn:openspp:vocab:group-type` | Core | Types of groups (household, family) |
| Group Membership Type | `urn:openspp:vocab:group-membership-type` | Core | Types of group memberships |
| Housing Type (UN Rev.3) | `urn:un:unsd:pop-census:housing-type` | Core | UN standard housing classification (hierarchical) |
| Economic Activity Status | `urn:ilo:icse-93` | Labor | ILO employment status codes |
| Religion | `urn:un:unsd:pop-census:religion` | Core | UN census religious affiliation framework |
| Ethnocultural Status | `urn:openspp:vocab:ethnocultural` | Core | Ethnicity and cultural identity |

These vocabularies are available in the system and can be browsed via **Settings → Vocabularies → Manage Vocabularies**.

## Using Standard Vocabularies

### In Registration Forms

Standard vocabularies populate dropdown fields automatically:

**Example: Gender field on Individual form**
```
Gender: [Select...]
  ↓ (shows codes from active deployment profile)
  Male
  Female
```

### In CEL Expressions

Use vocabulary codes in eligibility rules:

**Example: Check if female**
```
# Robust approach using concept groups
in_group(me.gender, "feminine_gender")

# OR explicit URI
me.gender == code("urn:iso:std:iso:5218#2")
```

See {doc}`/config_guide/cel/index` for more CEL vocabulary functions.

### In API Data

API V2 uses vocabulary URIs for interoperability:

**Request:**
```json
{
  "gender": "urn:iso:std:iso:5218#2",
  "marital_status": "urn:un:unsd:pop-census:marital-status#M"
}
```

**Response:**
```json
{
  "gender": {
    "uri": "urn:iso:std:iso:5218#2",
    "code": "2",
    "display": "Female"
  }
}
```

## Vocabulary Metadata

### Viewing Vocabulary Details

**Navigation:** Settings → Vocabularies → Manage Vocabularies

Each vocabulary shows:

| Field | Description |
|-------|-------------|
| Name | Human-readable name (e.g., "Gender") |
| Namespace URI | Unique identifier (e.g., `urn:iso:std:iso:5218`) |
| Version | Standard version (e.g., "2004") |
| Domain | Category: core, disability, labor, agriculture, etc. |
| Is System | Read-only (true for standards) |
| Is Hierarchical | Has parent-child codes (true for ICF, ISCO) |
| Reference URL | Link to official documentation |
| Code Count | Number of codes in vocabulary |

### Checking Which Codes Are Active

**Navigation:** Settings → Vocabularies → Vocabulary Selections

Shows which codes from each vocabulary are active in your deployment profile.

## Are You Stuck?

**Need a code that's not in the standard vocabulary?**
Check if you can add it as a custom extension. See {doc}`custom` → Local Extensions.

**Too many codes showing in dropdown?**
Configure your deployment profile to activate only needed codes. See {doc}`profiles`.

**Can't find a vocabulary for your data?**
Some domains don't have international standards. Create a custom vocabulary (see {doc}`custom`).

**Vocabulary is in English but need other languages?**
OpenSPP vocabularies support translation. Go to Settings → Translations to add your language.

**Codes are showing but values aren't being saved?**
Check field permissions - you may need Registry Officer role. Contact your administrator.

## Next Steps

| To... | See... |
|-------|--------|
| Configure which codes appear in your deployment | {doc}`profiles` |
| Add custom codes or vocabularies | {doc}`custom` |
| Use vocabularies in eligibility expressions | {doc}`/config_guide/cel/index` |
| View complete vocabulary reference | {doc}`/reference/vocabularies/index` |

---

**Related:**
- {doc}`overview` - Vocabulary system concepts
- {doc}`profiles` - Configure active codes
- {doc}`custom` - Create custom vocabularies
- {doc}`/reference/vocabularies/index` - Complete vocabulary reference

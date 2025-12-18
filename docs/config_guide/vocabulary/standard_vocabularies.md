---
openspp:
  doc_status: draft
---

# Standard Vocabularies

This guide is for **implementers** who need to understand which standard vocabularies are available in OpenSPP and what codes they contain.

## Overview

OpenSPP V2 includes 13 standard vocabularies based on international standards. These are **system vocabularies** (read-only) that ensure data consistency and interoperability.

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

| Code | Display | URI |
|------|---------|-----|
| head | Head of Household | `urn:openspp:vocab:relationship#head` |
| spouse | Spouse/Partner | `urn:openspp:vocab:relationship#spouse` |
| child | Child | `urn:openspp:vocab:relationship#child` |
| parent | Parent | `urn:openspp:vocab:relationship#parent` |
| sibling | Sibling | `urn:openspp:vocab:relationship#sibling` |
| grandparent | Grandparent | `urn:openspp:vocab:relationship#grandparent` |
| grandchild | Grandchild | `urn:openspp:vocab:relationship#grandchild` |
| other_relative | Other Relative | `urn:openspp:vocab:relationship#other_relative` |
| non_relative | Non-Relative | `urn:openspp:vocab:relationship#non_relative` |

**Namespace:** `urn:openspp:vocab:relationship`
**Reference:** OpenSPP-specific (no international standard)
**Use in:** Household member relationships, beneficiary household composition

### Marital Status

Based on UN Population Census Principles.

| Code | Display | URI |
|------|---------|-----|
| S | Single | `urn:un:unsd:pop-census:marital-status#S` |
| M | Married | `urn:un:unsd:pop-census:marital-status#M` |
| W | Widowed | `urn:un:unsd:pop-census:marital-status#W` |
| D | Divorced | `urn:un:unsd:pop-census:marital-status#D` |
| L | Separated | `urn:un:unsd:pop-census:marital-status#L` |
| C | Civil Union | `urn:un:unsd:pop-census:marital-status#C` |

**Namespace:** `urn:un:unsd:pop-census:marital-status`
**Reference:** [UN Census Recommendations](https://unstats.un.org/unsd/demographic/sources/census/)
**Use in:** Individual demographics, eligibility criteria (widows programs, etc.)

### ID Document Types

Standard identification document classifications.

| Code | Display | URI |
|------|---------|-----|
| national_id | National ID Card | `urn:openspp:vocab:id-document#national_id` |
| passport | Passport | `urn:openspp:vocab:id-document#passport` |
| birth_cert | Birth Certificate | `urn:openspp:vocab:id-document#birth_cert` |
| drivers_license | Driver's License | `urn:openspp:vocab:id-document#drivers_license` |
| voter_id | Voter Registration Card | `urn:openspp:vocab:id-document#voter_id` |
| tax_id | Tax Identification Number | `urn:openspp:vocab:id-document#tax_id` |
| social_security | Social Security Card | `urn:openspp:vocab:id-document#social_security` |
| refugee_id | Refugee ID | `urn:openspp:vocab:id-document#refugee_id` |
| other | Other Document | `urn:openspp:vocab:id-document#other` |

**Namespace:** `urn:openspp:vocab:id-document`
**Reference:** OpenSPP-specific
**Use in:** ID document tracking, identity verification, deduplication

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

### WHO ICF: Body Functions (b codes)

WHO International Classification of Functioning - Body Functions component.

**Sample codes (hierarchical):**

| Code | Display | Parent | URI |
|------|---------|--------|-----|
| b2 | Sensory functions and pain | - | `urn:who:icf:b#b2` |
| b210 | Seeing functions | b2 | `urn:who:icf:b#b210` |
| b230 | Hearing functions | b2 | `urn:who:icf:b#b230` |
| b280 | Sensation of pain | b2 | `urn:who:icf:b#b280` |
| b7 | Neuromusculoskeletal functions | - | `urn:who:icf:b#b7` |
| b710 | Mobility of joint functions | b7 | `urn:who:icf:b#b710` |
| b730 | Muscle power functions | b7 | `urn:who:icf:b#b730` |

**Namespace:** `urn:who:icf:b`
**Reference:** [WHO ICF Browser](https://icd.who.int/dev11/l-icf/en)
**Use in:** Disability classification, functional assessment, targeting
**Total codes:** 400+ hierarchical codes
**Note:** Hierarchical - users can select at any level of detail

### WHO ICF: Activities & Participation (d codes)

WHO ICF - Activities and Participation component.

**Sample codes:**

| Code | Display | Parent | URI |
|------|---------|--------|-----|
| d4 | Mobility | - | `urn:who:icf:d#d4` |
| d450 | Walking | d4 | `urn:who:icf:d#d450` |
| d5 | Self-care | - | `urn:who:icf:d#d5` |
| d540 | Dressing | d5 | `urn:who:icf:d#d540` |
| d6 | Domestic life | - | `urn:who:icf:d#d6` |
| d640 | Doing housework | d6 | `urn:who:icf:d#d640` |

**Namespace:** `urn:who:icf:d`
**Reference:** [WHO ICF](https://www.who.int/standards/classifications/icf)
**Use in:** Activity limitations, participation restrictions, needs assessment

### WHO ICD-11: Health Conditions

WHO International Classification of Diseases, 11th Revision.

**Sample codes:**

| Code | Display | URI |
|------|---------|-----|
| 9B71.0 | Type 1 diabetes mellitus | `urn:who:icd-11#9B71.0` |
| BA00 | Essential hypertension | `urn:who:icd-11#BA00` |
| 6A70 | HIV disease | `urn:who:icd-11#6A70` |
| 8B20 | Tuberculosis | `urn:who:icd-11#8B20` |

**Namespace:** `urn:who:icd-11`
**Reference:** [ICD-11 Browser](https://icd.who.int/browse11)
**Use in:** Health condition tracking, medical eligibility criteria
**Total codes:** 17,000+ diagnostic codes

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

**Navigation:** Studio → Vocabularies

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

**Navigation:** Settings → Social Protection → Vocabulary Management

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

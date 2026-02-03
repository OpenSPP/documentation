---
openspp:
  doc_status: draft
  products: [core]
---

# Vocabulary Reference

Complete reference for all standard vocabularies in OpenSPP V2.

## Quick Reference

| Vocabulary | Namespace | Codes | Hierarchical | Domain |
|------------|-----------|-------|--------------|--------|
| [Gender (ISO 5218)](#iso-5218-gender) | `urn:iso:std:iso:5218` | 4 | No | Core |
| [Relationship Types](#relationship-types) | `urn:openspp:vocab:relationship` | 9 | No | Core |
| [Marital Status](#marital-status) | `urn:un:unsd:pop-census:marital-status` | 6 | No | Core |
| [ID Document Types](#id-document-types) | `urn:openspp:vocab:id-document` | 9 | No | Core |
| [Countries (ISO 3166)](#iso-3166-countries) | `urn:iso:std:iso:3166-1` | 249 | No | Geographic |
| [Languages (ISO 639)](#iso-639-languages) | `urn:iso:std:iso:639` | 180+ | No | Geographic |
| [Currencies (ISO 4217)](#iso-4217-currencies) | `urn:iso:std:iso:4217` | 170+ | No | Geographic |
| [WHO ICF Body Functions](#who-icf-body-functions) | `urn:who:icf:b` | 400+ | Yes | Disability |
| [WHO ICF Activities](#who-icf-activities--participation) | `urn:who:icf:d` | 300+ | Yes | Disability |
| [WHO ICD-11 Health](#who-icd-11-health-conditions) | `urn:who:icd-11` | 17,000+ | Yes | Health |
| [ILO ISCO-08 Occupations](#ilo-isco-08-occupations) | `urn:ilo:isco-08` | 400+ | Yes | Labor |
| [UNESCO ISCED Education](#unesco-isced-2011-education) | `urn:unesco:isced:2011` | 9 | Yes | Education |
| [FAO AGROVOC Crops](#fao-agrovoc-crops) | `urn:fao:agrovoc` | 1,000+ | Yes | Agriculture |

## Core Vocabularies

### ISO 5218: Gender

Standardized codes for representing biological sex.

**Namespace:** `urn:iso:std:iso:5218`
**Reference:** [ISO 5218:2004](https://www.iso.org/standard/36266.html)
**System:** Yes (read-only)
**Hierarchical:** No

**Codes:**

| Code | URI | Display | Definition |
|------|-----|---------|------------|
| 0 | `urn:iso:std:iso:5218#0` | Not Known | Sex is not known |
| 1 | `urn:iso:std:iso:5218#1` | Male | Male sex |
| 2 | `urn:iso:std:iso:5218#2` | Female | Female sex |
| 9 | `urn:iso:std:iso:5218#9` | Not Applicable | Not applicable or not stated |

**Use cases:**
- Individual registration
- Demographic data collection
- Beneficiary targeting (gender-specific programs)
- Eligibility criteria

**CEL expressions:**
```cel
# Check if female
in_group(me.gender, "feminine_gender")

# Explicit code check
me.gender == code("urn:iso:std:iso:5218#2")
```

---

### Relationship Types

Household and family relationship classifications.

**Namespace:** `urn:openspp:vocab:relationship`
**Reference:** OpenSPP-specific (no international standard)
**System:** Yes
**Hierarchical:** No

**Codes:**

| Code | URI | Display | Definition |
|------|-----|---------|------------|
| head | `urn:openspp:vocab:relationship#head` | Head of Household | Primary household decision-maker |
| spouse | `urn:openspp:vocab:relationship#spouse` | Spouse/Partner | Married or domestic partner |
| child | `urn:openspp:vocab:relationship#child` | Child | Son or daughter (biological/adopted) |
| parent | `urn:openspp:vocab:relationship#parent` | Parent | Father or mother |
| sibling | `urn:openspp:vocab:relationship#sibling` | Sibling | Brother or sister |
| grandparent | `urn:openspp:vocab:relationship#grandparent` | Grandparent | Grandparent |
| grandchild | `urn:openspp:vocab:relationship#grandchild` | Grandchild | Grandchild |
| other_relative | `urn:openspp:vocab:relationship#other_relative` | Other Relative | Related but not in above categories |
| non_relative | `urn:openspp:vocab:relationship#non_relative` | Non-Relative | Unrelated household member |

**Use cases:**
- Household member relationships
- Household composition analysis
- Dependency ratio calculations
- Head of household identification

**CEL expressions:**
```cel
# Check if head of household
in_group(m.relationship, "head_of_household")

# Count children
members.filter(m, m.relationship.code == "child").size()
```

---

### Marital Status

UN Population Census standard marital status codes.

**Namespace:** `urn:un:unsd:pop-census:marital-status`
**Reference:** [UN Census Recommendations](https://unstats.un.org/unsd/demographic/sources/census/)
**System:** Yes
**Hierarchical:** No

**Codes:**

| Code | URI | Display | Definition |
|------|-----|---------|------------|
| S | `urn:un:unsd:pop-census:marital-status#S` | Single | Never married |
| M | `urn:un:unsd:pop-census:marital-status#M` | Married | Currently married |
| W | `urn:un:unsd:pop-census:marital-status#W` | Widowed | Spouse deceased, not remarried |
| D | `urn:un:unsd:pop-census:marital-status#D` | Divorced | Legally divorced |
| L | `urn:un:unsd:pop-census:marital-status#L` | Separated | Married but living apart |
| C | `urn:un:unsd:pop-census:marital-status#C` | Civil Union | Registered partnership |

**Use cases:**
- Demographic data
- Widows/widowers programs
- Family targeting criteria
- Household composition

**CEL expressions:**
```cel
# Widowed individuals
me.marital_status.code == "W"

# Married or civil union
me.marital_status.code in ["M", "C"]
```

---

### ID Document Types

Standard identification document classifications.

**Namespace:** `urn:openspp:vocab:id-document`
**Reference:** OpenSPP-specific
**System:** Yes
**Hierarchical:** No

**Codes:**

| Code | URI | Display |
|------|-----|---------|
| national_id | `urn:openspp:vocab:id-document#national_id` | National ID Card |
| passport | `urn:openspp:vocab:id-document#passport` | Passport |
| birth_cert | `urn:openspp:vocab:id-document#birth_cert` | Birth Certificate |
| drivers_license | `urn:openspp:vocab:id-document#drivers_license` | Driver's License |
| voter_id | `urn:openspp:vocab:id-document#voter_id` | Voter Registration Card |
| tax_id | `urn:openspp:vocab:id-document#tax_id` | Tax Identification Number |
| social_security | `urn:openspp:vocab:id-document#social_security` | Social Security Card |
| refugee_id | `urn:openspp:vocab:id-document#refugee_id` | Refugee ID |
| other | `urn:openspp:vocab:id-document#other` | Other Document |

**Use cases:**
- Identity verification
- Document tracking
- Deduplication
- KYC compliance

---

## Geographic Vocabularies

### ISO 3166: Countries

ISO standard country codes.

**Namespace:** `urn:iso:std:iso:3166-1`
**Reference:** [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html)
**System:** Yes
**Hierarchical:** No
**Total Codes:** 249

**Sample Codes:**

| Alpha-2 | Alpha-3 | Numeric | URI | Country Name |
|---------|---------|---------|-----|--------------|
| PH | PHL | 608 | `urn:iso:std:iso:3166-1#PH` | Philippines |
| KE | KEN | 404 | `urn:iso:std:iso:3166-1#KE` | Kenya |
| US | USA | 840 | `urn:iso:std:iso:3166-1#US` | United States |
| GB | GBR | 826 | `urn:iso:std:iso:3166-1#GB` | United Kingdom |
| IN | IND | 356 | `urn:iso:std:iso:3166-1#IN` | India |
| BR | BRA | 076 | `urn:iso:std:iso:3166-1#BR` | Brazil |
| ZA | ZAF | 710 | `urn:iso:std:iso:3166-1#ZA` | South Africa |
| AU | AUS | 036 | `urn:iso:std:iso:3166-1#AU` | Australia |

**Use cases:**
- Address data
- Nationality tracking
- Country of origin
- Geographic reporting

---

### ISO 639: Languages

ISO standard language codes.

**Namespace:** `urn:iso:std:iso:639`
**Reference:** [ISO 639](https://www.iso.org/iso-639-language-codes.html)
**System:** Yes
**Hierarchical:** No
**Total Codes:** 180+

**Sample Codes:**

| Code | URI | Language |
|------|-----|----------|
| en | `urn:iso:std:iso:639#en` | English |
| es | `urn:iso:std:iso:639#es` | Spanish |
| fr | `urn:iso:std:iso:639#fr` | French |
| ar | `urn:iso:std:iso:639#ar` | Arabic |
| zh | `urn:iso:std:iso:639#zh` | Chinese |
| hi | `urn:iso:std:iso:639#hi` | Hindi |
| pt | `urn:iso:std:iso:639#pt` | Portuguese |
| ru | `urn:iso:std:iso:639#ru` | Russian |
| ja | `urn:iso:std:iso:639#ja` | Japanese |
| tl | `urn:iso:std:iso:639#tl` | Tagalog |
| sw | `urn:iso:std:iso:639#sw` | Swahili |

**Use cases:**
- Preferred language
- Multilingual forms
- Translation requirements
- Communication preferences

---

### ISO 4217: Currencies

ISO standard currency codes.

**Namespace:** `urn:iso:std:iso:4217`
**Reference:** [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html)
**System:** Yes
**Hierarchical:** No
**Total Codes:** 170+

**Sample Codes:**

| Code | URI | Currency | Country/Region |
|------|-----|----------|----------------|
| USD | `urn:iso:std:iso:4217#USD` | US Dollar | United States |
| EUR | `urn:iso:std:iso:4217#EUR` | Euro | European Union |
| PHP | `urn:iso:std:iso:4217#PHP` | Philippine Peso | Philippines |
| KES | `urn:iso:std:iso:4217#KES` | Kenyan Shilling | Kenya |
| GBP | `urn:iso:std:iso:4217#GBP` | Pound Sterling | United Kingdom |
| INR | `urn:iso:std:iso:4217#INR` | Indian Rupee | India |
| BRL | `urn:iso:std:iso:4217#BRL` | Brazilian Real | Brazil |
| ZAR | `urn:iso:std:iso:4217#ZAR` | South African Rand | South Africa |

**Use cases:**
- Entitlement amounts
- Payment programs
- Financial tracking
- Multi-currency deployments

---

## Disability & Health

### WHO ICF: Body Functions

WHO International Classification of Functioning - Body Functions.

**Namespace:** `urn:who:icf:b`
**Reference:** [WHO ICF Browser](https://icd.who.int/dev11/l-icf/en)
**System:** Yes
**Hierarchical:** Yes (4 levels)
**Total Codes:** 400+

**Sample Hierarchy:**

```
b1 - Mental functions
├── b110 - Consciousness functions
├── b114 - Orientation functions
├── b117 - Intellectual functions
└── b122 - Global psychosocial functions

b2 - Sensory functions and pain
├── b210 - Seeing functions
│   ├── b2100 - Visual acuity
│   ├── b2101 - Visual field
│   └── b2102 - Quality of vision
├── b230 - Hearing functions
│   ├── b2300 - Sound detection
│   └── b2301 - Sound discrimination
└── b280 - Sensation of pain

b7 - Neuromusculoskeletal and movement-related functions
├── b710 - Mobility of joint functions
├── b730 - Muscle power functions
└── b740 - Muscle endurance functions
```

**Use cases:**
- Disability classification
- Functional assessment
- Targeting persons with disabilities
- Service needs identification

**CEL expressions:**
```cel
# Check for sensory disability
me.disability_codes.exists(d, d.code.startsWith("b2"))

# Specific function impairment
in_group(me.disability_primary, "seeing_functions")
```

---

### WHO ICF: Activities & Participation

WHO ICF - Activities and Participation component.

**Namespace:** `urn:who:icf:d`
**Reference:** [WHO ICF](https://www.who.int/standards/classifications/icf)
**System:** Yes
**Hierarchical:** Yes
**Total Codes:** 300+

**Sample Codes:**

```
d4 - Mobility
├── d450 - Walking
├── d455 - Moving around
└── d465 - Moving around using equipment

d5 - Self-care
├── d510 - Washing oneself
├── d520 - Caring for body parts
├── d530 - Toileting
├── d540 - Dressing
└── d550 - Eating

d6 - Domestic life
├── d620 - Acquisition of goods and services
├── d630 - Preparing meals
└── d640 - Doing housework
```

**Use cases:**
- Activity limitations assessment
- Participation restrictions
- Needs-based targeting
- Support service planning

---

### WHO ICD-11: Health Conditions

WHO International Classification of Diseases, 11th Revision.

**Namespace:** `urn:who:icd-11`
**Reference:** [ICD-11 Browser](https://icd.who.int/browse11)
**System:** Yes
**Hierarchical:** Yes
**Total Codes:** 17,000+

**Sample Codes:**

| Code | URI | Display | Category |
|------|-----|---------|----------|
| 9B71.0 | `urn:who:icd-11#9B71.0` | Type 1 diabetes mellitus | Endocrine |
| BA00 | `urn:who:icd-11#BA00` | Essential hypertension | Cardiovascular |
| 6A70 | `urn:who:icd-11#6A70` | HIV disease | Infectious |
| 8B20 | `urn:who:icd-11#8B20` | Tuberculosis | Infectious |
| 2A00 | `urn:who:icd-11#2A00` | Malaria | Infectious |

**Use cases:**
- Health condition tracking
- Medical eligibility criteria
- Disease surveillance
- Health program targeting

---

## Labor & Education

### ILO ISCO-08: Occupations

International Labour Organization - International Standard Classification of Occupations.

**Namespace:** `urn:ilo:isco-08`
**Reference:** [ILO ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/)
**System:** Yes
**Hierarchical:** Yes (4 levels)
**Total Codes:** 400+

**Hierarchy Structure:**

```
1-digit: Major group (10 groups)
2-digit: Sub-major group (~40 groups)
3-digit: Minor group (~130 groups)
4-digit: Unit group (~400 groups)
```

**Sample Codes:**

| Code | Level | URI | Display |
|------|-------|-----|---------|
| 1 | Major | `urn:ilo:isco-08#1` | Managers |
| 11 | Sub-major | `urn:ilo:isco-08#11` | Chief executives, senior officials and legislators |
| 111 | Minor | `urn:ilo:isco-08#111` | Legislators and senior officials |
| 1111 | Unit | `urn:ilo:isco-08#1111` | Legislators |
| 5 | Major | `urn:ilo:isco-08#5` | Service and sales workers |
| 51 | Sub-major | `urn:ilo:isco-08#51` | Personal service workers |
| 511 | Minor | `urn:ilo:isco-08#511` | Travel attendants, conductors and guides |
| 5111 | Unit | `urn:ilo:isco-08#5111` | Travel attendants and travel stewards |

**Use cases:**
- Employment tracking
- Labor market programs
- Skills assessment
- Occupational hazard identification

---

### UNESCO ISCED 2011: Education

UNESCO International Standard Classification of Education.

**Namespace:** `urn:unesco:isced:2011`
**Reference:** [UNESCO ISCED](http://uis.unesco.org/en/topic/international-standard-classification-education-isced)
**System:** Yes
**Hierarchical:** Yes (levels with sub-categories)
**Total Codes:** 9 main levels

**Codes:**

| Code | URI | Display | Description |
|------|-----|---------|-------------|
| 0 | `urn:unesco:isced:2011#0` | Early childhood education | Less than primary |
| 1 | `urn:unesco:isced:2011#1` | Primary education | Basic literacy/numeracy |
| 2 | `urn:unesco:isced:2011#2` | Lower secondary | Foundation for lifelong learning |
| 3 | `urn:unesco:isced:2011#3` | Upper secondary | More specialized education |
| 4 | `urn:unesco:isced:2011#4` | Post-secondary non-tertiary | Bridge to tertiary |
| 5 | `urn:unesco:isced:2011#5` | Short-cycle tertiary | Practical/technical orientation |
| 6 | `urn:unesco:isced:2011#6` | Bachelor's or equivalent | First tertiary degree |
| 7 | `urn:unesco:isced:2011#7` | Master's or equivalent | Advanced specialization |
| 8 | `urn:unesco:isced:2011#8` | Doctoral or equivalent | Research qualification |

**Use cases:**
- Education level tracking
- Scholarship programs
- Education targeting
- Skills assessment

---

## Agriculture (Optional)

### FAO AGROVOC: Crops

FAO Agricultural Thesaurus - crop and livestock terms.

**Namespace:** `urn:fao:agrovoc`
**Reference:** [FAO AGROVOC](https://agrovoc.fao.org/)
**System:** Yes
**Hierarchical:** Yes
**Total Codes:** 1,000+
**Availability:** Requires `spp_registry_farmer` module

**Sample Codes:**

| Code | URI | Display | Category |
|------|-----|---------|----------|
| c_6599 | `urn:fao:agrovoc#c_6599` | Rice | Cereal |
| c_12332 | `urn:fao:agrovoc#c_12332` | Maize (Corn) | Cereal |
| c_8373 | `urn:fao:agrovoc#c_8373` | Wheat | Cereal |
| c_4849 | `urn:fao:agrovoc#c_4849` | Millet | Cereal |
| c_10999 | `urn:fao:agrovoc#c_10999` | Cassava | Root/tuber |
| c_6214 | `urn:fao:agrovoc#c_6214` | Potato | Root/tuber |
| c_1439 | `urn:fao:agrovoc#c_1439` | Coffee | Cash crop |
| c_1872 | `urn:fao:agrovoc#c_1872` | Cotton | Cash crop |

**Use cases:**
- Farmer registries
- Agricultural programs
- Crop tracking
- Food security monitoring

---

## Concept Groups

Semantic groupings for business logic abstraction.

### Built-in Groups

| Group Name | Description | Codes Included |
|------------|-------------|----------------|
| `feminine_gender` | Codes representing feminine gender | ISO 5218: Female (2) |
| `masculine_gender` | Codes representing masculine gender | ISO 5218: Male (1) |
| `head_of_household` | Head of household relationships | Relationship: head |
| `pregnant_eligible` | Pregnancy statuses for maternal benefits | (custom per deployment) |

### Usage in CEL

```cel
# Check semantic group membership
in_group(me.gender, "feminine_gender")

# Semantic helper functions
is_female(me.gender)
is_male(me.gender)
is_head(member.relationship)
is_pregnant(me.pregnancy_status)
```

---

## API Usage

### Requesting with URIs

**POST /api/v2/individuals:**
```json
{
  "gender": "urn:iso:std:iso:5218#2",
  "marital_status": "urn:un:unsd:pop-census:marital-status#M",
  "country": "urn:iso:std:iso:3166-1#PH"
}
```

### Response Format

**GET /api/v2/individuals/{id}:**
```json
{
  "gender": {
    "uri": "urn:iso:std:iso:5218#2",
    "code": "2",
    "display": "Female",
    "namespace": "urn:iso:std:iso:5218"
  },
  "marital_status": {
    "uri": "urn:un:unsd:pop-census:marital-status#M",
    "code": "M",
    "display": "Married"
  }
}
```

### Filtering by Code

**GET /api/v2/individuals?gender=urn:iso:std:iso:5218#2**

Returns all individuals with female gender code.

---

## Extending Vocabularies

For information on creating custom vocabularies or local extensions, see:

- {doc}`/config_guide/vocabulary/custom` - Creating custom vocabularies
- {doc}`/config_guide/vocabulary/profiles` - Configuring deployment profiles

---

## Related Documentation

- {doc}`/config_guide/vocabulary/index` - Vocabulary configuration guide
- {doc}`/config_guide/vocabulary/overview` - Vocabulary system overview
- {doc}`/config_guide/vocabulary/standard_vocabularies` - Standard vocabulary details
- {doc}`/config_guide/vocabulary/profiles` - Deployment profiles
- {doc}`/config_guide/vocabulary/custom` - Custom vocabularies
- {doc}`/config_guide/cel/index` - Using vocabularies in CEL expressions

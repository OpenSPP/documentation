---
openspp:
  doc_status: draft
  products: [core]
---

# Vocabulary Overview

This guide is for **implementers** configuring OpenSPP's vocabulary system. You should be comfortable with configuration tools like Kobo or CommCare, but you don't need to write code.

## What Are Vocabularies?

Vocabularies are standardized lists of codes used throughout OpenSPP for consistent data collection.

**Example:** Gender field

| Old Approach (Hardcoded) | New Approach (Vocabulary) |
|--------------------------|---------------------------|
| Dropdown: Male, Female | Dropdown: Codes from ISO 5218 Gender vocabulary |
| Fixed in code | Configurable per deployment |
| No interoperability | Maps to international standards |
| Requires code changes to extend | Add codes via UI |

## Mental Model

Think of vocabularies in three layers:

```
┌───────────────────────────────────────────────────────┐
│  1. VOCABULARY                                        │
│     Name: "Gender"                                    │
│     Namespace: urn:iso:std:iso:5218                   │
│     (The container)                                   │
└───────────────────────────────────────────────────────┘
                         │
                         │ contains
                         ▼
┌───────────────────────────────────────────────────────┐
│  2. CODES                                             │
│     • Code: "1"  Display: "Male"                      │
│     • Code: "2"  Display: "Female"                    │
│     • Code: "0"  Display: "Not Known"                 │
│     • Code: "9"  Display: "Not Applicable"            │
│     (The individual values)                           │
└───────────────────────────────────────────────────────┘
                         │
                         │ filtered by
                         ▼
┌───────────────────────────────────────────────────────┐
│  3. DEPLOYMENT PROFILE                                │
│     Active codes for "Philippines 4Ps":               │
│     • Male                                            │
│     • Female                                          │
│     (What users see in this deployment)               │
└───────────────────────────────────────────────────────┘
```

**Key insight:** One vocabulary can be used differently in each country/program by selecting which codes are active.

## Why Use Vocabularies?

### 1. Consistency Across Deployments

**Without vocabularies:**
- Kenya uses: "M", "F"
- Philippines uses: "Male", "Female", "Other"
- Can't compare data between countries

**With vocabularies:**
- Both use ISO 5218 codes
- Different active subsets, but same standard
- Reporting works across deployments

### 2. International Standard Compliance

OpenSPP uses globally recognized standards where available:

| Domain | Standard | Authority |
|--------|----------|-----------|
| Gender | ISO 5218 | International Organization for Standardization |
| Countries | ISO 3166 | ISO |
| Disability | WHO ICF | World Health Organization |
| Occupations | ILO ISCO-08 | International Labour Organization |
| Education | UNESCO ISCED | UNESCO |
| Languages | ISO 639 | ISO |

### 3. No Code Changes for Extensions

**Scenario:** Your program needs to track a new disability type.

| Old Approach | New Approach |
|--------------|--------------|
| 1. Request developer to modify code | 1. Go to **Settings → Vocabularies** |
| 2. Wait for module update | 2. Add new code |
| 3. Deploy to production | 3. Done - immediately available |
| 4. Risk breaking existing data | 4. No deployment needed |

### 4. Local Terminology with Global Mapping

**Example:** Philippines uses local hazard terms

```
Local Term          Maps To                 Result
─────────────────── ─────────────────────── ───────────────────
"Bagyong"       →   Typhoon (standard)  →   Interoperable data
"Pagbaha"       →   Flood (standard)    →   Reports work globally
"Lindol"        →   Earthquake          →   Can exchange with WHO
```

Users see "Bagyong", but data exports use the standard code for interoperability.

## Core Concepts

### Namespace URIs

Every vocabulary has a globally unique identifier (URI).

**Format:**
```
urn:{authority}:{standard}:{component}
```

**Examples:**
```
urn:iso:std:iso:5218              → ISO 5218 Gender
urn:who:icf:b                      → WHO ICF Body Functions
urn:ilo:isco-08                    → ILO Occupations
urn:openspp:vocab:relationship     → OpenSPP-specific (no standard exists)
```

**Why URIs?** Ensures no naming conflicts. "Gender" is ambiguous, but `urn:iso:std:iso:5218` is precise.

### Code URIs

Each code within a vocabulary also gets a unique URI.

**Format:**
```
{vocabulary_namespace}#{code}
```

**Examples:**
```
urn:iso:std:iso:5218#1                    → Male
urn:iso:std:iso:5218#2                    → Female
urn:openspp:vocab:relationship#head       → Head of Household
urn:openspp:vocab:relationship#spouse     → Spouse
```

These URIs are used in:
- Data exports (API V2)
- CEL expressions
- Code mappings

### System vs. Custom Vocabularies

| Aspect | System Vocabulary | Custom Vocabulary |
|--------|-------------------|-------------------|
| Example | ISO 5218 Gender | Your org's "Program Types" |
| Editable | No (read-only) | Yes |
| Namespace | International standard | `urn:openspp:*` or local |
| Use Case | Compliance, interoperability | Organization-specific needs |

**Rule:** Use international standards when available. Only create custom vocabularies when no standard exists.

### Hierarchical Codes

Some vocabularies organize codes in parent-child relationships.

**Example:** WHO ICF Disability Classification

```
b2 - Sensory functions and pain
├── b210 - Seeing functions
├── b230 - Hearing functions
└── b280 - Sensation of pain

b7 - Neuromusculoskeletal functions
├── b710 - Mobility of joint functions
└── b730 - Muscle power functions
```

**Benefit:** Users can select at any level of detail (e.g., "Sensory" or specific "Hearing").

## How Vocabularies Work in OpenSPP

### 1. Model Fields Use Vocabulary Codes

**Old approach (hardcoded):**
```python
gender = fields.Selection([
    ('male', 'Male'),
    ('female', 'Female'),
])
```

**New approach (vocabulary-based):**
```python
gender_id = fields.Many2one(
    'spp.vocabulary.code',
    domain="[('namespace_uri', '=', 'urn:iso:std:iso:5218')]"
)
```

**Result:** Field shows codes from the Gender vocabulary, filtered by active deployment profile.

### 2. Deployment Profiles Filter Active Codes

**Setup:**
1. Vocabulary has 10 codes
2. Deployment profile selects 3 as active
3. UI dropdowns show only the 3 active codes
4. API can still accept any valid code (for interoperability)

**Why?** Different countries need different options without maintaining separate codebases.

### 3. CEL Expressions Use Concept Groups

Instead of checking specific codes, expressions check semantic groups:

**Fragile (breaks if code changes):**
```
me.gender == "female"
```

**Robust (works across deployments):**
```
in_group(me.gender, "feminine_gender")
```

The concept group includes all codes that represent "feminine" across different vocabularies and local extensions.

## Common Vocabulary Patterns

### Pattern 1: Subset Selection

**Use case:** Use ISO standard but limit options for cultural context

| Full Vocabulary | Your Deployment |
|-----------------|-----------------|
| ISO 5218 has 8 gender codes | Activate only: Male, Female |

**Setup:** Configure deployment profile to include only needed codes.

### Pattern 2: Local Extension

**Use case:** Add local terms that map to standards

```
Standard Vocabulary: urn:openspp:vocab:hazard
└── typhoon, flood, earthquake, drought

Local Extension: urn:openspp:ph:vocab:hazard
├── bagyong      (maps to → typhoon)
├── pagbaha      (maps to → flood)
└── lindol       (maps to → earthquake)
```

**Setup:**
1. Create custom vocabulary with local namespace
2. Add codes with `reference_uri` pointing to standard codes
3. Users see local terms, exports use standard URIs

### Pattern 3: Organization-Specific

**Use case:** No international standard exists

**Example:** "Program Delivery Method"
- Cash transfer
- In-kind (food)
- Voucher
- Direct service

**Setup:**
1. Create vocabulary with OpenSPP namespace: `urn:openspp:vocab:delivery-method`
2. Add codes
3. Mark as non-system (editable)

### Pattern 4: Hierarchical Classification

**Use case:** Allow selection at different detail levels

**Example:** Disability classification (WHO ICF)

```
User can select:
- "Sensory functions" (broad)
  OR
- "Seeing functions" (specific)
  OR
- "b2101 - Light perception" (very specific)
```

**Setup:** Use vocabulary with `is_hierarchical=True` and parent-child codes.

## Vocabulary Lifecycle

```
1. INSTALLATION
   ↓
   Standard vocabularies loaded automatically

2. CONFIGURATION
   ↓
   Create deployment profile → Select active codes

3. EXTENSION (optional)
   ↓
   Add custom codes or local vocabularies

4. USAGE
   ↓
   Forms show active codes → Data uses URIs

5. MAINTENANCE
   ↓
   Add/deprecate codes → Update profiles
```

## Data Storage

**In the database:**
- Vocabulary: `spp.vocabulary` (name, namespace_uri, domain)
- Codes: `spp.vocabulary.code` (code, display, uri, parent_id)
- Profiles: `spp.deployment.profile`
- Selections: `spp.vocabulary.selection` (which codes are active)
- Mappings: `spp.vocabulary.mapping` (code A → code B equivalence)

**In your data:**
- Fields store a reference to `spp.vocabulary.code.id`
- API exports use code URIs (e.g., `urn:iso:std:iso:5218#2`)
- Import can accept code, display, or URI

## Are You Stuck?

**Don't understand namespace URIs?**
Think of them like email addresses - they're globally unique identifiers. `urn:iso:std:iso:5218` is like `gender@iso.org` - it tells you exactly which gender vocabulary you mean.

**Can't find the vocabulary you need?**
Check {doc}`standard_vocabularies` for the 13 built-in ones. If it's not there, you can create a custom one (see {doc}`custom`).

**Confused about profiles?**
Think of profiles like presets on a camera. The camera has many features (codes), but each preset (profile) uses only some of them.

**Codes not showing up in dropdowns?**
Check your deployment profile - only active codes appear in UI. See {doc}`profiles`.

## Next Steps

| If you want to... | Go to... |
|-------------------|----------|
| Browse available vocabularies | {doc}`standard_vocabularies` |
| Configure which codes appear in your deployment | {doc}`profiles` |
| Add custom codes or vocabularies | {doc}`custom` |
| Use vocabularies in CEL expressions | {doc}`/config_guide/cel/index` |

---

**Related:**
- {doc}`standard_vocabularies` - Explore built-in vocabularies
- {doc}`profiles` - Configure active codes
- {doc}`custom` - Create custom vocabularies

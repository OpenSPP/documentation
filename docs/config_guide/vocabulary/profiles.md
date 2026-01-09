---
openspp:
  doc_status: draft
  products: [core]
---

# Vocabulary Profiles

This guide is for **implementers** configuring which vocabulary codes are active in their OpenSPP deployment.

## What Are Vocabulary Profiles?

Vocabulary profiles let you select which codes from a vocabulary appear in your deployment's user interface.

### Example: Gender Codes

```
┌────────────────────────────────────────────────┐
│ ISO 5218 Gender Vocabulary (Full)              │
│ ├─ 0: Not Known                                │
│ ├─ 1: Male                                     │
│ ├─ 2: Female                                   │
│ ├─ 9: Not Applicable                           │
│ └─ (+ extended codes: non-binary, other...)    │
└────────────────────────────────────────────────┘
              │
              │ filtered by profile
              ▼
┌────────────────────────────────────────────────┐
│ "Philippines 4Ps" Profile                      │
│ Active gender codes:                           │
│ ├─ 1: Male         ✓                          │
│ └─ 2: Female       ✓                          │
│                                                 │
│ Result: Users only see Male/Female dropdown    │
└────────────────────────────────────────────────┘
```

**Key insight:** One vocabulary, multiple deployment configurations, no code changes.

## Why Use Profiles?

### 1. Cultural Context

Different countries/programs need different options:

| Deployment | Active Gender Codes | Reason |
|------------|---------------------|---------|
| Country A | Male, Female | Cultural/legal context requires binary |
| Country B | Male, Female, Other | More inclusive, but simplified |
| Country C | Full ISO 5218 + extensions | Progressive legal framework |

All use the **same vocabulary**, just different subsets.

### 2. Simplified User Interface

**Without profiles:** Users see all 50+ disability codes
**With profiles:** Users see only the 5 codes relevant to your program

**Result:** Fewer errors, faster data entry, better data quality.

### 3. Compliance Requirements

**Scenario:** Your government requires specific demographic categories.

**Solution:** Configure profile to show only compliant codes while maintaining internal standard mappings.

### 4. Staged Rollout

**Example:** Start with basic codes, add more as users become comfortable

| Phase | Active Codes |
|-------|--------------|
| Phase 1 (Launch) | Male, Female |
| Phase 2 (3 months) | + Not Known |
| Phase 3 (6 months) | + Other, Prefer not to say |

## Mental Model: Profiles vs. Vocabularies

```
DEPLOYMENT PROFILE                    (Your configuration package)
├── Name: "Philippines 4Ps"
├── Description: "4Ps Cash Transfer Program"
└── Vocabulary Selections:
    ├── Gender (ISO 5218)             (Which codes from this vocab)
    │   └── Active: Male, Female
    ├── Marital Status
    │   └── Active: Single, Married, Widowed, Separated
    ├── Relationship Types
    │   └── Active: Head, Spouse, Child, Parent, Sibling
    └── Disability (WHO ICF)
        └── Active: Seeing, Hearing, Mobility, Cognitive
```

**One deployment profile** contains **many vocabulary selections** (one per vocabulary).

## Configuring Profiles

### Step 1: Navigate to Profile Settings

Go to **Settings → Social Protection → Vocabulary Management**

You'll see:
```
┌──────────────────────────────────────────────┐
│ 🌍 Deployment Profile                        │
│                                               │
│ Active Profile: [Philippines 4Ps ▼]         │
│                                               │
│ [Configure Profiles...]  [Preview Changes]   │
└──────────────────────────────────────────────┘
```

### Step 2: Create or Select Profile

**To create new profile:**

| Field | Value |
|-------|-------|
| Name | "Kenya CT-OVC" |
| Description | "Cash Transfer for Orphans and Vulnerable Children" |
| Parent Profile | (optional) "Base Profile" |
| Active | ✓ |

**To modify existing:**

Click **Configure Profiles** → Select profile from list → **Edit**

### Step 3: Configure Vocabulary Selections

For each vocabulary, select active codes:

**Example: Configuring Gender codes**

| Field | Value |
|-------|-------|
| Vocabulary | Gender (ISO 5218) |
| Active Codes | ☑ Male<br>☑ Female<br>☐ Not Known<br>☐ Not Applicable |
| Inheritance | From parent profile (if applicable) |

**Example: Configuring Relationship Types**

| Field | Value |
|-------|-------|
| Vocabulary | Relationship Type |
| Active Codes | ☑ Head of Household<br>☑ Spouse<br>☑ Child<br>☑ Parent<br>☑ Sibling<br>☐ Grandparent<br>☐ Grandchild<br>☐ Other Relative<br>☐ Non-Relative |

### Step 4: Preview Impact

Before activating, click **Preview Changes** to see:

```
📊 Impact Analysis

✓ Gender: 2/4 codes active
  • 45,231 records will continue to display correctly
  • 0 orphaned records (using non-profile codes)

⚠️ Relationship Type: 5/9 codes active
  • 12 records use "Grandparent" (not in profile)
  • These records remain valid but cannot be created new

✓ No CEL expressions affected
```

### Step 5: Activate Profile

Click **Save & Activate**

**Result:** Forms immediately show only selected codes. Existing data remains intact.

## Profile Inheritance

Profiles can extend other profiles, reducing duplication.

### Example: Base + Country-Specific

```
Profile: "Base African Context"
├── Gender: Male, Female
├── Marital Status: Single, Married, Divorced, Widowed
└── Relationship: Head, Spouse, Child, Parent, Sibling

       │
       │ extends (inherits all codes)
       ▼

Profile: "Kenya CT-OVC" (parent: Base)
├── INHERITS: All codes from Base
├── ADDS:
│   └── Disability: Seeing, Hearing, Mobility, Cognitive
└── EXCLUDES:
    └── Marital Status: Divorced (remove from inherited)

       ▼ Result

Kenya CT-OVC Active Codes:
├── Gender: Male, Female (inherited)
├── Marital Status: Single, Married, Widowed (inherited - Divorced)
├── Relationship: Head, Spouse, Child... (inherited)
└── Disability: Seeing, Hearing... (added)
```

### Configuring Inheritance

| Field | Value |
|-------|-------|
| Parent Profile | "Base African Context" |
| Inherit Mode | ☑ Inherit all parent codes |
| Excluded Codes | ☑ Marital Status → Divorced |
| Additional Codes | ☑ Disability: Seeing, Hearing, Mobility, Cognitive |

**Benefits:**
- DRY principle (don't repeat yourself)
- Update parent → all children inherit changes
- Country-specific tweaks without full duplication

**Warning:** Keep inheritance shallow (1-2 levels). Deep chains are hard to debug.

## Advanced Configuration

### UI vs. API Behavior

| Context | Behavior |
|---------|----------|
| **UI Dropdowns** | Show only active profile codes |
| **Existing Records** | Display all codes (including non-profile) |
| **API Accepts** | Any valid code by default |
| **API Strict Mode** | Only profile codes (if enabled) |

**Why?** Data integrity + interoperability. External systems may send valid codes not in your profile.

### Enabling API Strict Mode

**When to use:** You want to reject API requests with codes outside your profile.

| Field | Value |
|-------|-------|
| API Vocabulary Validation | Strict |

**Result:**
```json
POST /api/v2/individuals
{
  "gender": "urn:iso:std:iso:5218#9"  // Not Applicable - not in profile
}

→ 400 Bad Request
{
  "error": "Code not in active deployment profile",
  "code": "urn:iso:std:iso:5218#9",
  "allowed_codes": [
    "urn:iso:std:iso:5218#1",
    "urn:iso:std:iso:5218#2"
  ]
}
```

**Default mode (Permissive):** Same request would succeed (for interoperability).

### Handling Orphaned Records

**Scenario:** You change profile, some records use codes no longer active.

**Example:**
1. Old profile included "Other" gender
2. 50 records marked as "Other"
3. New profile removes "Other"

**Result:**
```
Gender: Other ⓘ
        ↑
        Tooltip: "This value is not in your active profile but
                  remains valid for existing records."
```

**Options:**

| Action | How To |
|--------|--------|
| Keep as-is | No action needed - displays with info icon |
| Map to active code | Tools → Vocabulary Mapping → Map "Other" → "Not Known" |
| Reactivate code | Edit profile → Add "Other" back to active codes |
| View affected records | Dashboard shows count → [View Records] button |

### Profile Health Dashboard

**Navigation:** Settings → Vocabulary Management → Dashboard

Shows:

```
📊 Profile: Philippines 4Ps (Active)

Gender (2/4 codes active)              ✓ In use: 45,231 records
├─ Male                                ✓ 23,145 records
├─ Female                              ✓ 22,086 records
└─ Other                               ⓘ 0 records (inactive)

Relationship (5/9 codes active)        ⚠️ Has orphaned codes
├─ Head                                ✓ 12,543 records
├─ Spouse                              ✓ 8,234 records
├─ Child                               ✓ 15,678 records
├─ Parent                              ✓ 3,456 records
├─ Sibling                             ✓ 2,345 records
└─ Grandparent                         ⚠️ 12 records (not in profile)

⚠️ Orphaned Codes Summary:
• Grandparent: 12 records
  [Map These Records...] [View Records] [Reactivate Code]
```

## Common Profile Patterns

### Pattern 1: Conservative Subset

**Use case:** Simplified options for easier data entry

| Vocabulary | Full Set | Your Profile |
|------------|----------|--------------|
| Gender | 8 codes | Male, Female |
| Marital Status | 6 codes | Married, Single |
| Disability | 50+ codes | Physical, Visual, Hearing, Mental |

**Result:** Clean, simple forms for field staff.

### Pattern 2: Regional Standard

**Use case:** Government compliance

**Example:** ASEAN demographic standards
- Gender: ISO 5218 core (0, 1, 2, 9)
- Marital Status: UN census categories
- Education: UNESCO ISCED

**Setup:** Create "ASEAN Standard" profile → Activate compliant codes

### Pattern 3: Progressive Expansion

**Use case:** Add codes as program matures

| Timeline | Gender Codes | Reason |
|----------|--------------|--------|
| Month 1-3 | Male, Female | Initial rollout, keep simple |
| Month 4-6 | + Not Known | Users requested "unknown" option |
| Month 7+ | + Other, Prefer not to say | Legal requirement update |

**Setup:** Clone profile → Add codes → Test → Activate

### Pattern 4: Multi-Tenant

**Use case:** Different organizations in same system

| Organization | Profile | Gender Codes |
|--------------|---------|--------------|
| Ministry of Health | Health Profile | Male, Female, Other |
| Faith-based NGO | NGO Profile | Male, Female |
| Research Institute | Research Profile | Full ISO 5218 set |

**Setup:** Create profile per company → Set company_id field

## Testing Profile Changes

**Before activating a new profile:**

### 1. Preview Mode

Enable preview without affecting production:

| Field | Value |
|-------|-------|
| Profile Status | Preview |
| Preview Users | admin@example.com, test@example.com |

**Result:** Only specified users see new profile. Others see old one.

### 2. Run Impact Report

**Navigation:** Configure Profiles → [Your Profile] → Impact Analysis

Shows:
- How many records use non-profile codes
- Which CEL expressions reference affected codes
- Forms that will change

### 3. Test in Sandbox

**Best practice:** Clone production database to test environment

```bash
# Steps
1. Clone database to test environment
2. Activate new profile in test
3. Test all forms and expressions
4. If OK → activate in production
```

### 4. Gradual Rollout

**Use field groups:**

| Field | Value |
|-------|-------|
| Profile | Kenya CT-OVC v2 |
| Active For Groups | Pilot District Admins |
| Fallback Profile | Kenya CT-OVC v1 |

**Result:** Pilot users see v2, others see v1. Gradual migration.

## Migration Checklist

Before changing active profile:

- [ ] Backup database
- [ ] Run impact analysis
- [ ] Identify orphaned codes (if any)
- [ ] Plan mapping for orphaned codes
- [ ] Review affected CEL expressions
- [ ] Test in sandbox environment
- [ ] Document changes for users
- [ ] Schedule change during low-usage period
- [ ] Prepare rollback plan
- [ ] Notify users of upcoming changes

## Are You Stuck?

**Profile changes not appearing in UI?**
Clear your browser cache and refresh. Profile changes are cached for performance.

**Orphaned codes causing confusion?**
Use the mapping tool to bulk-update records: Tools → Vocabulary Mapping → Bulk Map.

**Want to A/B test two profiles?**
Use Preview Mode with different user groups.

**Inheritance not working as expected?**
Check parent profile is active. Inactive parents don't propagate changes.

**Need to switch profiles frequently?**
Avoid this - it confuses users and creates data inconsistency. Profiles should be stable.

**Can't see "Configure Profiles" button?**
You need Administrator role. Contact your system admin.

## Next Steps

| To... | See... |
|-------|--------|
| Add custom codes to a vocabulary | {doc}`custom` |
| Use profile codes in CEL expressions | {doc}`/config_guide/cel/index` |
| Understand vocabulary architecture | {doc}`overview` |
| Browse available vocabularies | {doc}`standard_vocabularies` |

---

**Related:**
- {doc}`overview` - Vocabulary system concepts
- {doc}`standard_vocabularies` - Built-in vocabularies
- {doc}`custom` - Create custom vocabularies

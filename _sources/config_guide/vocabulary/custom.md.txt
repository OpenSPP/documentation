---
openspp:
  doc_status: draft
  products: [core]
---

# Custom Vocabularies

This guide is for **implementers** who need to create organization-specific vocabularies or extend existing ones with local terminology.

## When to Create Custom Vocabularies

**Use international standards first.** Only create custom vocabularies when:
- No international standard exists for your domain
- You need local terminology that maps to standards
- Program-specific classifications are required

### Decision Tree

```
Do you need codes for...

  Gender, Country, Language, Currency,
  Disability, Occupation, Education?
    ├─ YES → Use standard vocabulary (see Standard Vocabularies doc)
    └─ NO ↓

  Is there an international standard for your domain?
    ├─ YES → Use that standard, extend if needed
    └─ NO ↓

  Is it specific to your program/organization?
    ├─ YES → Create custom vocabulary
    └─ NO → Check with OpenSPP community (may become standard)
```

## Custom Vocabulary Patterns

### Pattern 1: Program-Specific Vocabulary

**Use case:** No standard exists, internal classification only

**Example:** "Cash Transfer Delivery Methods"
- Bank transfer
- Mobile money
- Cash at agent
- Postal order
- Direct deposit

**Setup:**

| Field | Value |
|-------|-------|
| Name | Delivery Method |
| Namespace URI | `urn:openspp:vocab:delivery-method` |
| Domain | Social Assistance |
| Is System | No (editable) |
| Is Hierarchical | No |

### Pattern 2: Local Extension

**Use case:** Local terminology that maps to international standards

**Example:** Philippine hazard terms → Standard codes
- "Bagyong" → Typhoon
- "Pagbaha" → Flood
- "Lindol" → Earthquake

**Setup:** Create local vocabulary with reference URIs

### Pattern 3: Extended Standard

**Use case:** International standard + additional codes

**Example:** ISO 5218 Gender + inclusive options
- Standard: Male (1), Female (2)
- Extended: Non-binary, Other, Prefer not to say

**Setup:** Add codes to existing vocabulary (if not system-locked)

### Pattern 4: Hierarchical Classification

**Use case:** Nested categories

**Example:** Service types
- Health Services
  - Primary care
  - Specialist care
  - Emergency care
- Education Services
  - Tuition support
  - Supplies
  - Transportation

**Setup:** Enable hierarchical, use parent-child relationships

## Creating a Custom Vocabulary

### Step 1: Navigate to Vocabularies

Go to **Settings → Vocabularies → Manage Vocabularies → Create**

### Step 2: Define Vocabulary Metadata

| Field | Example Value | Notes |
|-------|---------------|-------|
| Name | "Program Delivery Method" | User-facing name |
| Namespace URI | `urn:openspp:org:4ps:delivery-method` | Must be globally unique |
| Version | "2024" | Your versioning scheme |
| Domain | Social Assistance | Category for organization |
| Is System | ☐ (No) | Allow editing |
| Is Hierarchical | ☐ (No) | Check if nested codes |
| Description | "Methods for delivering cash transfers" | Help text |
| Reference URL | (optional) | Link to policy doc |

#### Namespace URI Guidelines

**Format:** `urn:{authority}:{org}:vocab:{name}`

**Examples:**
```
urn:openspp:vocab:{name}                    → OpenSPP community standard
urn:openspp:ph:vocab:{name}                 → Philippines-specific
urn:openspp:org:{your-org}:vocab:{name}     → Your organization
urn:openspp:4ps:vocab:{name}                → Specific program
```

**Rules:**
- Use lowercase, hyphens (not underscores)
- Must be unique globally
- Cannot change after creation
- No spaces or special characters

### Step 3: Add Codes

Click **Codes** tab → **Add Code**

**Example: Delivery methods**

| Code | Display | Definition | Sequence |
|------|---------|------------|----------|
| bank_transfer | Bank Transfer | Direct transfer to beneficiary bank account | 1 |
| mobile_money | Mobile Money | Transfer to mobile wallet (e.g., GCash, M-Pesa) | 2 |
| cash_agent | Cash at Agent | Pick up cash at designated agent location | 3 |
| postal_order | Postal Order | Delivered via postal service | 4 |
| direct_deposit | Direct Deposit | Government direct deposit system | 5 |

#### Code Field Guidelines

| Field | Description | Example |
|-------|-------------|---------|
| **Code** | Machine-readable identifier | `mobile_money` |
| **Display** | User-facing label (translatable) | "Mobile Money" |
| **Definition** | Formal definition (optional) | "Transfer to mobile wallet service" |
| **Sequence** | Display order | 10, 20, 30... |
| **Active** | Enabled for use | ✓ |

**Naming conventions:**
- Code: lowercase, underscores, short (e.g., `mobile_money`)
- Display: Title Case, user-friendly (e.g., "Mobile Money")
- Use consistent patterns across codes

### Step 4: Test the Vocabulary

Before deployment, test:

1. **Create test record** using the new vocabulary codes
2. **Check dropdown** shows codes in correct order
3. **Test CEL expression** if using in eligibility rules
4. **Verify translations** if multilingual

## Creating Local Extensions

Local extensions map local terminology to international standards for interoperability.

### Example: Philippine Hazard Terms

**Goal:** Users see local terms, but data maps to standard codes for reporting.

### Step 1: Create Local Vocabulary

| Field | Value |
|-------|-------|
| Name | Hazards (Philippines) |
| Namespace URI | `urn:openspp:ph:vocab:hazard` |
| Domain | Social Assistance |
| Is System | No |
| Description | Local Philippine terminology for natural hazards |

### Step 2: Add Codes with Reference URIs

| Code | Display | Reference URI | Equivalence |
|------|---------|---------------|-------------|
| bagyong | Bagyong (Typhoon) | `urn:openspp:vocab:hazard#typhoon` | equivalent |
| pagbaha | Pagbaha (Flood) | `urn:openspp:vocab:hazard#flood` | equivalent |
| lindol | Lindol (Earthquake) | `urn:openspp:vocab:hazard#earthquake` | equivalent |
| bulkan | Bulkan (Volcanic Eruption) | `urn:openspp:vocab:hazard#volcanic_eruption` | equivalent |

**Key fields:**

| Field | Value | Purpose |
|-------|-------|---------|
| Code | `bagyong` | Local identifier |
| Display | "Bagyong (Typhoon)" | Shows both terms |
| Is Local | ✓ | Marks as local extension |
| Reference URI | `urn:openspp:vocab:hazard#typhoon` | Points to standard code |
| Equivalence | equivalent | How closely it maps |

#### Equivalence Levels

| Level | Meaning | Example |
|-------|---------|---------|
| **Equivalent** | Exact match | "Bagyong" = Typhoon |
| **Wider** | Target more general | "Skin condition" → Disability |
| **Narrower** | Target more specific | "Disability" → Visual impairment |
| **Inexact** | Approximate match | "Traditional healer" → Health worker |

### Step 3: Configure Profile to Use Local Codes

**Navigation:** Settings → Vocabularies → Vocabulary Selections

| Field | Value |
|-------|-------|
| Vocabulary | Hazards (Philippines) |
| Active Codes | ☑ Bagyong<br>☑ Pagbaha<br>☑ Lindol<br>☑ Bulkan |

**Result:** Users see local terms in forms.

### Step 4: Verify Data Exchange

**API Export:**
```json
{
  "hazard_type": {
    "uri": "urn:openspp:ph:vocab:hazard#bagyong",
    "code": "bagyong",
    "display": "Bagyong (Typhoon)",
    "reference_uri": "urn:openspp:vocab:hazard#typhoon"
  }
}
```

**Interoperability:** Other systems can use `reference_uri` to understand "Bagyong" = "Typhoon".

## Hierarchical Vocabularies

For nested classifications.

### Example: Service Types

**Goal:** Two-level hierarchy of services

```
Health Services
├── Primary Care
├── Specialist Care
└── Emergency Care

Education Services
├── Tuition Support
├── School Supplies
└── Transportation
```

### Step 1: Create Vocabulary

| Field | Value |
|-------|-------|
| Name | Service Types |
| Namespace URI | `urn:openspp:org:myorg:service-types` |
| Is Hierarchical | ✓ |

### Step 2: Add Parent Codes

| Code | Display | Parent | Level |
|------|---------|--------|-------|
| health | Health Services | (none) | 0 |
| education | Education Services | (none) | 0 |

### Step 3: Add Child Codes

| Code | Display | Parent | Level |
|------|---------|--------|-------|
| health_primary | Primary Care | health | 1 |
| health_specialist | Specialist Care | health | 1 |
| health_emergency | Emergency Care | health | 1 |
| edu_tuition | Tuition Support | education | 1 |
| edu_supplies | School Supplies | education | 1 |
| edu_transport | Transportation | education | 1 |

**Parent field:** Select parent code from same vocabulary

**Result in UI:**
```
Service Type: [Select...]
  ↓
  Health Services
    ├─ Primary Care
    ├─ Specialist Care
    └─ Emergency Care
  Education Services
    ├─ Tuition Support
    ├─ School Supplies
    └─ Transportation
```

### Advanced: Multi-Level Hierarchies

**Example:** WHO ICF has 4 levels

```
Level 0: Chapter (e.g., "b2 - Sensory functions")
Level 1: Block (e.g., "b210 - Seeing functions")
Level 2: Category (e.g., "b2101 - Light perception")
Level 3: Subcategory
```

**Setup:** Same process, just keep adding children to children.

## Code Mappings

Map codes between different vocabularies.

### Use Case: Cross-Vocabulary Translation

**Scenario:** Your old system used custom disability codes, new system uses WHO ICF.

**Goal:** Map old codes to WHO ICF for data migration.

### Step 1: Create Mapping

**Navigation:** Settings → Vocabularies → Code Mappings → Create

| Field | Value |
|-------|-------|
| Source Code | Old System: "blind" |
| Target Code | WHO ICF: b210 (Seeing functions) |
| Equivalence | Narrower (WHO ICF is more specific) |
| Comment | "Legacy 'blind' maps to ICF seeing functions category" |

### Step 2: Bulk Mappings

For many mappings, use import:

**CSV format:**
```text
source_uri,target_uri,equivalence,comment
urn:myorg:disability#blind,urn:who:icf:b#b210,narrower,Seeing functions
urn:myorg:disability#deaf,urn:who:icf:b#b230,narrower,Hearing functions
urn:myorg:disability#mobility,urn:who:icf:b#b7,wider,Neuromusculoskeletal
```

**Import:** Settings → Vocabularies → Code Mappings → Import

### Step 3: Use in Data Migration

**Migration script (pseudo-code):**
```python
for record in old_records:
    old_code = record.disability_code
    mapping = find_mapping(old_code, target_vocab="WHO ICF")
    if mapping:
        record.disability_icf_id = mapping.target_id
    else:
        log_unmapped(old_code)
```

## Managing Vocabulary Lifecycle

### Deprecating Codes

**When to deprecate:** Code no longer used but exists in historical data.

**Steps:**

| Field | Value |
|-------|-------|
| Code | old_code |
| Deprecated | ✓ |
| Deprecated Date | 2024-06-30 |
| Replaced By | new_code |
| Active | ☐ (No) |

**Result:**
- Historical records still display the code
- New records cannot select it
- UI shows warning if trying to use

### Versioning Vocabularies

**Approach 1: Version in namespace**
```
urn:openspp:vocab:delivery-method:v1
urn:openspp:vocab:delivery-method:v2
```

**Approach 2: Version field**
```
Namespace: urn:openspp:vocab:delivery-method
Version: 2024
```

**Recommendation:** Use version field, update when major changes.

### Archiving Unused Vocabularies

**Steps:**
1. Check usage: Dashboard → Vocabulary → View Records
2. If 0 records: Safe to archive
3. Set Active = ☐ (No)
4. Vocabulary hidden from UI but preserved for historical reference

## Import/Export Vocabularies

### Export Vocabulary

**Use case:** Share with another deployment or backup

**Navigation:** Settings → Vocabularies → Manage Vocabularies → [Your Vocabulary] → Export

**Formats:**
- **XML** - For loading in another OpenSPP instance
- **CSV** - For editing in spreadsheet
- **JSON** - For API integration

**Example XML:**
```xml
<record id="vocab_delivery_method" model="spp.vocabulary">
    <field name="name">Delivery Method</field>
    <field name="namespace_uri">urn:openspp:vocab:delivery-method</field>
</record>

<record id="code_bank_transfer" model="spp.vocabulary.code">
    <field name="vocabulary_id" ref="vocab_delivery_method"/>
    <field name="code">bank_transfer</field>
    <field name="display">Bank Transfer</field>
</record>
```

### Import Vocabulary

**Use case:** Load vocabulary from another deployment

**Navigation:** Settings → Vocabularies → Manage Vocabularies → Import

**Steps:**
1. Select file (XML/CSV/JSON)
2. Map fields if CSV
3. Review preview
4. Import
5. Verify codes loaded

**CSV Template:**
```text
code,display,definition,sequence,parent_code
bank_transfer,Bank Transfer,Direct transfer to bank account,10,
mobile_money,Mobile Money,Transfer to mobile wallet,20,
cash_agent,Cash at Agent,Pick up cash,30,
```

## Best Practices

### Naming Conventions

| Item | Convention | Example |
|------|------------|---------|
| Vocabulary Name | Title Case, descriptive | "Program Delivery Method" |
| Namespace URI | lowercase, hyphens | `urn:openspp:vocab:delivery-method` |
| Code | lowercase, underscores | `mobile_money` |
| Display | Title Case | "Mobile Money" |

### Code Design

**DO:**
- Keep codes short but meaningful
- Use consistent patterns (all verbs, all nouns, etc.)
- Plan for future additions (leave sequence gaps: 10, 20, 30...)
- Document in definition field

**DON'T:**
- Use codes like "code1", "code2" (not meaningful)
- Mix languages in codes (UI can be multilingual, codes should be one language)
- Change codes after deployment (break references)
- Delete codes (deprecate instead)

### Documentation

**For each custom vocabulary, document:**

| What | Where |
|------|-------|
| Purpose | Description field |
| Source/Authority | Reference URL field |
| Mapping rationale | Code definition field |
| Version history | External change log |
| Who can edit | Vocabulary metadata |

**Example Documentation:**
```
Vocabulary: urn:openspp:4ps:vocab:grievance-category
Purpose: Classification of beneficiary complaints and feedback
Authority: 4Ps Program Operations Manual Section 8.3
Version: 2024.1 (Updated Jan 2024)
Maintainer: M&E Unit
Review Cycle: Annually
```

### Translation Strategy

**Multilingual deployments:**

1. **Create codes in English** (international standard)
2. **Translate display field** via Settings → Translations
3. **Keep code itself untranslated** (machine-readable)

**Example:**
```
Code: mobile_money (unchanged in all languages)

Translations:
├─ en: "Mobile Money"
├─ fr: "Argent mobile"
├─ es: "Dinero móvil"
└─ tl: "Mobile Money" (same, widely used)
```

### Quality Control

**Before deploying custom vocabulary:**

- [ ] Namespace URI is globally unique
- [ ] Codes are meaningful and consistent
- [ ] No duplicate codes within vocabulary
- [ ] Sequence numbers have gaps for future additions
- [ ] All codes have display names
- [ ] Critical codes have definitions
- [ ] Tested in sandbox environment
- [ ] Translations complete (if multilingual)
- [ ] Deployment profile configured
- [ ] Documentation written
- [ ] Reviewed by subject matter expert

## Common Scenarios

### Scenario 1: Cash Transfer Program Types

**Need:** Classify different cash transfer programs

**Solution:**

| Code | Display |
|------|---------|
| conditional | Conditional Cash Transfer |
| unconditional | Unconditional Cash Transfer |
| emergency | Emergency Cash Assistance |
| graduation | Graduation/Livelihoods Support |

**Namespace:** `urn:openspp:vocab:ct-program-type`

### Scenario 2: Vulnerability Criteria

**Need:** Track vulnerabilities for targeting

**Solution (hierarchical):**

```
Economic Vulnerability
├── Unemployed
├── Underemployed
└── No income source

Health Vulnerability
├── Chronic illness
├── Disability
└── Elderly care needs

Social Vulnerability
├── Single parent
├── Orphan
└── Abandoned
```

**Namespace:** `urn:openspp:vocab:vulnerability-criteria`

### Scenario 3: Intervention Types

**Need:** Track services provided

**Solution:**

| Code | Display | Parent |
|------|---------|--------|
| cash | Cash Assistance | - |
| inkind | In-Kind Support | - |
| service | Social Services | - |
| cash_monthly | Monthly Transfer | cash |
| cash_lumpsum | Lump Sum Payment | cash |
| inkind_food | Food Package | inkind |
| service_counsel | Counseling | service |

**Namespace:** `urn:openspp:vocab:intervention-type`

## Are You Stuck?

**Can't decide if you need a custom vocabulary?**
Ask: "Is there an international standard for this?" If yes, use it. If no, create custom.

**Namespace URI already exists?**
Each vocabulary needs a unique URI. Add your organization: `urn:openspp:{org}:vocab:{name}`

**Codes not appearing in forms?**
Check deployment profile has activated your custom vocabulary codes.

**Need to change a code value?**
Don't change the code itself (breaks references). Deprecate old → Create new → Map old to new.

**Import fails with "duplicate code" error?**
Check if vocabulary already exists. Either delete old or use different namespace URI.

**Hierarchical codes not showing correctly?**
Verify `Is Hierarchical = True` on vocabulary and parent relationships are set.

## Next Steps

| To... | See... |
|-------|--------|
| Configure which codes appear in forms | {doc}`profiles` |
| Use custom codes in eligibility rules | {doc}`/config_guide/cel/index` |
| Understand vocabulary architecture | {doc}`overview` |
| Browse standard vocabularies | {doc}`standard_vocabularies` |

---

**Related:**
- {doc}`overview` - Vocabulary system concepts
- {doc}`standard_vocabularies` - Built-in vocabularies
- {doc}`profiles` - Configure active codes
- {doc}`/config_guide/studio/index` - Studio configuration tools

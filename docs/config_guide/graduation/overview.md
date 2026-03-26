---
openspp:
  doc_status: draft
  products: [core]
---

# Graduation overview

This guide is for **implementers** configuring program exit pathways in OpenSPP. You should understand your program's graduation policy but don't need programming knowledge.

## Mental model

Graduation in OpenSPP has three layers:

| Layer | What it does | Example |
|-------|--------------|---------|
| **Pathway** | Defines the type of exit | "Standard Graduation" (positive), "Administrative Exit" (neutral) |
| **Criteria** | Conditions that must be met | "Monthly income > $200", "Has savings account" |
| **Assessment** | Individual evaluation against criteria | "Maria meets 4/5 criteria - ready for graduation" |

Think of it like a school graduation: **pathways** are the degree programs (with honors, standard, early exit), **criteria** are the course requirements, and **assessments** are the final exams.

## Key concepts

### Graduation pathways

| Field | What it means |
|-------|---------------|
| **Name** | Pathway label (e.g., "Standard Graduation") |
| **Exit Type** | Positive or Negative |
| **Assessment Required** | Whether formal assessment is needed before exit |
| **Approval Required** | Whether graduation needs supervisor approval |
| **Monitoring Duration** | Months of post-graduation monitoring |

#### Exit types

| Type | Meaning | Example |
|------|---------|---------|
| **Positive** | Beneficiary achieved program goals | Completed training, above poverty line |
| **Negative** | Exit without achieving goals | Relocated, deceased, administrative removal |

### Pre-configured pathways

```{figure} /_images/en-us/config_guide/graduation/02-graduation-pathway-form.png
:alt: Graduation pathway form showing criteria, assessment methods, and weights
Graduation pathway form showing criteria, assessment methods, and weights.
```

OpenSPP includes three default pathways:

| Pathway | Exit Type | Assessment | Approval |
|---------|-----------|-----------|----------|
| Standard Graduation | Positive | Yes | Yes |
| Early Graduation | Positive | Yes | Yes |
| Administrative Exit | Negative | No | No |

## Navigation

| Menu | Purpose |
|------|---------|
| **Graduation > Graduation Pathways** | Define exit pathways |
| **Graduation > Graduation Criteria** | Configure assessment criteria |
| **Graduation > Assessments** | View individual assessments |

```{figure} /_images/en-us/config_guide/graduation/01-graduation-pathways-list.png
:alt: Graduation pathways list showing exit type and assessment requirements
Graduation pathways list showing exit type and assessment requirements.
```

## Common use cases

### Use case 1: Poverty graduation program

**Goal:** Graduate beneficiaries who achieve economic self-sufficiency.

**Setup:**
1. Use the "Standard Graduation" pathway
2. Set criteria: income threshold, savings, livelihood activity
3. Require assessment and supervisor approval
4. Set 6-month post-graduation monitoring

### Use case 2: Emergency program exit

**Goal:** Administrative exit when emergency response concludes.

**Setup:**
1. Use the "Administrative Exit" pathway
2. No assessment or approval required
3. Set 0 months monitoring
4. Bulk-process exits for all remaining beneficiaries

## Are You Stuck?

**Where do I configure graduation?**

Navigate to **Graduation** in the main menu. If you don't see it, ask your administrator to install the **Graduation** module.

**What happens during post-graduation monitoring?**

The system tracks graduated beneficiaries for the configured duration. This allows re-enrollment if they fall back below thresholds.

**Can I customize the default pathways?**

Yes. Edit or create new pathways to match your program's exit policies.

## Next steps

- {doc}`criteria` - Configure assessment criteria
- {doc}`/config_guide/eligibility/index` - Connect graduation to eligibility rules

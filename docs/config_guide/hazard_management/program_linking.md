---
openspp:
  doc_status: draft
  products: [core]
---

# Linking programs to hazard incidents

This guide is for **implementers** connecting emergency programs to hazard incidents for targeted disaster response. This feature requires the **Hazard Programs** module — ask your administrator if you don't see program-incident linking fields.

## Mental model

Program-incident linking bridges disaster assessment with benefit delivery:

| Component | What it does | Example |
|-----------|--------------|---------|
| **Target Incident** | Links a program to a specific disaster | "Emergency Cash → Typhoon Rai" |
| **Damage Threshold** | Sets minimum damage level for eligibility | "Only moderate damage or worse" |
| **Emergency Mode** | Relaxes compliance rules for speed | Skip attendance requirements |

## Configuration

When `spp_hazard_programs` is installed, programs gain these fields:

| Field | What it means |
|-------|---------------|
| **Target Incident** | The hazard incident this program responds to |
| **Damage Level Threshold** | Minimum damage for eligibility: Any, Moderate+, Severe+, Critical |
| **Emergency Mode** | Enable relaxed compliance (e.g., skip training attendance) |

### Damage thresholds

| Threshold | Who qualifies |
|-----------|--------------|
| **Any** | All registrants with any recorded impact |
| **Moderate+** | Registrants with moderate, severe, or critical damage |
| **Severe+** | Only registrants with severe or critical damage |
| **Critical** | Only registrants with critical-level damage |

## Setting up emergency program targeting

### Step 1: Create the hazard incident

1. Record the disaster event with severity and affected areas
2. Begin impact assessments for affected registrants

### Step 2: Link the program

1. Open the emergency program
2. Set the **Target Incident**
3. Set the **Damage Level Threshold** based on available resources and policy
4. Enable **Emergency Mode** if compliance rules should be relaxed

### Step 3: Run eligibility

When the program runs eligibility checks, it automatically:
1. Filters to registrants in the incident's affected areas
2. Checks impact records against the damage threshold
3. Qualifies registrants meeting the threshold

## Common use cases

### Use case 1: Emergency cash transfer

**Goal:** Provide immediate cash to severely affected households.

**Setup:**
1. Link program to the incident
2. Set threshold to "Severe+"
3. Enable emergency mode
4. Run eligibility to identify qualifying households

### Use case 2: Tiered response

**Goal:** Different programs for different damage levels.

**Setup:**
1. Program A (food packs): threshold = "Any"
2. Program B (shelter kits): threshold = "Moderate+"
3. Program C (rebuilding grant): threshold = "Severe+"
4. Each program targets the same incident but different damage levels

## Are You Stuck?

**Program not finding affected registrants?**

Check that impact records exist for the registrants and that the damage levels match the threshold. Also verify the registrants are in the incident's affected areas.

**Emergency mode - what exactly does it relax?**

Emergency mode disables non-essential compliance checks like training attendance and review schedules. The exact behavior depends on your program configuration.

**Can I link a program to multiple incidents?**

Currently, one program links to one incident. For multi-incident response, create separate programs or use a broader eligibility criteria.

## Next steps

- {doc}`overview` - Hazard management fundamentals
- {doc}`/config_guide/eligibility/index` - Configure eligibility rules
- {doc}`/config_guide/entitlement_formulas/index` - Calculate emergency benefit amounts

---
openspp:
  doc_status: draft
  products: [core]
---

# Graduation criteria

This guide is for **implementers** defining the conditions beneficiaries must meet for program graduation.

## Criteria configuration

Each criterion within a pathway has:

| Field | What it means |
|-------|---------------|
| **Name** | Criterion label (e.g., "Income Threshold") |
| **Pathway** | Which graduation pathway this belongs to |
| **Weight** | Importance (default 1.0, higher = more important) |
| **Assessment Method** | How the criterion is verified |
| **Required** | Must be met for graduation (vs. optional) |

### Assessment methods

| Method | How it works | Best for |
|--------|-------------|----------|
| **Self-report** | Beneficiary provides information | Income, savings, livelihood status |
| **Verification Required** | Third-party or document verification | Employment, bank account, asset ownership |
| **Computed** | System calculates from data | Program attendance, payment history |
| **Field Observation** | Case worker observes during visit | Housing quality, livelihood activity |

### Pre-configured criteria examples

| Criterion | Method | Weight | Description |
|-----------|--------|--------|-------------|
| Income threshold | Verification Required | 1.0 | Monthly income above poverty line |
| Livelihood activity | Field Observation | 1.0 | Has active income-generating activity |
| Savings account | Verification Required | 0.8 | Has functional savings account |
| Training completion | Computed | 0.6 | Completed required training sessions |
| Debt level | Self-report | 0.5 | Manageable debt-to-income ratio |

## Setting up criteria

### Step 1: Plan your graduation conditions

Determine what beneficiaries must achieve:
- Which criteria are mandatory vs. optional?
- How will each criterion be verified?
- What weights reflect your program's priorities?

### Step 2: Create criteria

1. Navigate to **Graduation > Graduation Criteria**
2. Click **Create**
3. Select the **Pathway**
4. Set the **Name**, **Weight**, and **Assessment Method**
5. Mark as **Required** if mandatory
6. Save

### Step 3: Run assessments

1. Open a beneficiary's graduation assessment
2. For each criterion, record whether it is met
3. The system calculates an overall readiness score based on weights
4. If all required criteria are met, the beneficiary is eligible for graduation

## Monitoring duration

After graduation, beneficiaries enter a monitoring period:

| Setting | What it means |
|---------|-------------|
| **Monitoring Duration (months)** | How long to track post-graduation |

During monitoring:
- The system continues tracking the graduated beneficiary
- If key indicators fall below thresholds, they can be flagged for re-enrollment
- At the end of monitoring, the graduation is confirmed as final

## Are You Stuck?

**Criteria weights - how are they used?**

Weights contribute to an overall graduation readiness score. A criterion with weight 1.0 has twice the impact of one with weight 0.5. The exact threshold for "ready to graduate" depends on your program policy.

**Can I have different criteria for different pathways?**

Yes. Each criterion is linked to a specific pathway. Standard Graduation might require 5 criteria while Early Graduation requires 3.

**How do I handle computed criteria?**

Computed criteria pull data from the system automatically (e.g., attendance records, payment history). The computation is based on existing program data.

**Beneficiary meets criteria but supervisor disagrees?**

If the pathway has **Approval Required** enabled, the supervisor can reject the graduation even if criteria are met, with a documented reason.

## Next steps

- {doc}`overview` - Graduation pathway fundamentals
- {doc}`/config_guide/scoring/overview` - Use scoring models for graduation assessment
- {doc}`/config_guide/session_tracking/overview` - Track training completion for criteria

---
openspp:
  doc_status: draft
---

# Programs

**Module:** `spp_programs`

## Overview

OpenSPP Programs is the comprehensive program management module for social protection and agricultural support. It manages the complete program lifecycle from beneficiary enrollment through entitlement generation to payment disbursement, supporting both cash transfers and in-kind distributions.

## Purpose

This module is designed to:

- **Manage social protection programs:** Create and configure programs with eligibility rules, entitlement calculations, and payment workflows.
- **Handle program cycles:** Define time-bound periods for enrollment, entitlement generation, and disbursement.
- **Generate entitlements:** Calculate cash and in-kind benefits based on configurable rules and CEL expressions.
- **Process payments:** Manage payment batches, track disbursement status, and integrate with payment providers.
- **Support compliance workflows:** Implement approval processes and conditionality tracking.

## Module Dependencies

| Dependency           | Purpose                                       |
| -------------------- | --------------------------------------------- |
| `account`            | Accounting and fund management                |
| `web`                | Web interface components                      |
| `base`               | Odoo core framework                           |
| `mail`               | Communication and notifications               |
| `spp_registry`       | Beneficiary registry for enrollment           |
| `spp_banking`        | Bank account management for payments          |
| `calendar`           | Scheduling capabilities                       |
| `product`            | Product catalog for in-kind items             |
| `stock`              | Inventory management for in-kind distribution |
| `spp_security`       | Security groups and access control            |
| `spp_area`           | Geographic targeting                          |
| `spp_service_points` | Distribution point management                 |
| `spp_user_roles`     | Role-based access control                     |
| `spp_base_common`    | OpenSPP main menu integration                 |
| `spp_approval`       | Approval workflow management                  |
| `spp_cel_domain`     | CEL expression for eligibility rules          |
| `spp_cel_widget`     | CEL expression editor UI                      |

### External Dependencies

| Package           | Purpose                       |
| ----------------- | ----------------------------- |
| `python-dateutil` | Date calculations and parsing |

## Key Features

### Program Structure

Programs follow a hierarchical structure:

```
Program
├── Configuration
│   ├── Eligibility Manager (who qualifies)
│   ├── Entitlement Manager (what they receive)
│   └── Payment Manager (how they receive it)
├── Cycles
│   ├── Cycle 1 (Jan-Mar 2025)
│   ├── Cycle 2 (Apr-Jun 2025)
│   └── ...
└── Membership
    └── Enrolled beneficiaries
```

### Program Types

| Type          | Description              | Entitlement             |
| ------------- | ------------------------ | ----------------------- |
| Cash Transfer | Direct monetary benefits | Cash amounts            |
| In-Kind       | Goods distribution       | Products from inventory |
| Voucher       | Redeemable vouchers      | Voucher cards           |
| Mixed         | Combination programs     | Cash + in-kind          |

### Managers

Programs use configurable managers for each stage:

| Manager Type              | Purpose                 | Configuration               |
| ------------------------- | ----------------------- | --------------------------- |
| **Eligibility Manager**   | Determine who qualifies | CEL expressions, criteria   |
| **Cycle Manager**         | Define program periods  | Date ranges, sequencing     |
| **Entitlement Manager**   | Calculate benefits      | Amounts, formulas, products |
| **Deduplication Manager** | Prevent duplicates      | Matching rules              |
| **Notification Manager**  | Send communications     | Templates, channels         |
| **Payment Manager**       | Process disbursements   | Payment methods, batching   |

### Eligibility with CEL

Define eligibility rules using CEL expressions:

| Example Rule      | CEL Expression                 |
| ----------------- | ------------------------------ |
| Adults only       | `age_years(r.birthdate) >= 18` |
| Income threshold  | `r.monthly_income < 5000`      |
| Geographic target | `r.area_id.code == "REGION_1"` |
| Household size    | `household_size >= 3`          |

### Entitlement Types

#### Cash Entitlements

| Field       | Description            |
| ----------- | ---------------------- |
| Amount      | Cash value to disburse |
| Currency    | Payment currency       |
| Calculation | Fixed or formula-based |

#### In-Kind Entitlements

| Field     | Description               |
| --------- | ------------------------- |
| Product   | Item from product catalog |
| Quantity  | Units to distribute       |
| Warehouse | Source inventory location |

### Payment Processing

Payment workflow:

```
Entitlements Approved
    ↓
Create Payment Batch
    ↓
Assign to Service Points
    ↓
Process Payments
    ↓
Reconcile Results
```

### Compliance and Conditionalities

Track beneficiary compliance with program requirements:

| Feature            | Description                         |
| ------------------ | ----------------------------------- |
| Compliance checks  | Define required conditions          |
| Status tracking    | Monitor compliance per beneficiary  |
| Entitlement impact | Adjust benefits based on compliance |

### Approval Workflows

Multi-tier approval support:

| Stage       | Approval Type                |
| ----------- | ---------------------------- |
| Enrollment  | Program membership approval  |
| Entitlement | Benefit calculation approval |
| Payment     | Disbursement authorization   |

## Integration

### With Registry

Enrollment sources from the registry:

| Source      | Process                    |
| ----------- | -------------------------- |
| Individuals | Direct enrollment          |
| Groups      | Enroll household/group     |
| Bulk import | Mass enrollment from files |

### With Service Points

Distribution through service points:

| Integration    | Function                                |
| -------------- | --------------------------------------- |
| Assignment     | Link beneficiaries to collection points |
| Disbursement   | Track payments at service points        |
| Reconciliation | Report actual distributions             |

### With Accounting

Fund management:

| Feature         | Purpose                      |
| --------------- | ---------------------------- |
| Program budgets | Allocate funds to programs   |
| Journal entries | Track financial transactions |
| Fund reports    | Monitor utilization          |

### With CEL

Expression-based configuration:

| Use Case            | CEL Application      |
| ------------------- | -------------------- |
| Eligibility         | Filter rules         |
| Entitlement amounts | Calculation formulas |
| Conditionality      | Compliance checks    |

## Program Workflow

### 1. Create Program

| Step        | Configuration                  |
| ----------- | ------------------------------ |
| Basic info  | Name, description, target type |
| Eligibility | Criteria and expressions       |
| Entitlement | Benefit calculation rules      |
| Payment     | Disbursement method            |

### 2. Enroll Beneficiaries

| Method    | Description                   |
| --------- | ----------------------------- |
| Manual    | Add individual registrants    |
| Bulk      | Import from CSV/Excel         |
| Automatic | Based on eligibility criteria |

### 3. Create Cycle

| Configuration      | Purpose                             |
| ------------------ | ----------------------------------- |
| Date range         | Cycle period                        |
| Inherit membership | Copy from program or previous cycle |
| Compliance rules   | Cycle-specific requirements         |

### 4. Generate Entitlements

| Stage   | Action                             |
| ------- | ---------------------------------- |
| Prepare | Calculate entitlements for members |
| Review  | Verify amounts and eligibility     |
| Approve | Authorize for payment              |

### 5. Process Payments

| Stage        | Action                               |
| ------------ | ------------------------------------ |
| Create batch | Group entitlements for processing    |
| Assign       | Link to payment method/service point |
| Disburse     | Execute payments                     |
| Reconcile    | Record actual disbursements          |

## Technical Details

| Property       | Value          |
| -------------- | -------------- |
| Technical Name | `spp_programs` |
| Category       | OpenSPP/Core   |
| Version        | 19.0.2.0.0     |
| License        | LGPL-3         |
| Application    | Yes            |

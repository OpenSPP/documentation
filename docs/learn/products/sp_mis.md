---
openspp:
  doc_status: draft
---

# SP-MIS - Social Protection Management Information System

SP-MIS extends the Social Registry with full program management capabilities. It handles the complete beneficiary lifecycle from enrollment through payment disbursement, enabling efficient delivery of cash transfers, social assistance, and other social protection interventions.

**Who is this for:** Social protection agencies managing benefit programs, program managers overseeing cash transfers, M&E teams tracking program performance.

## What SP-MIS Does

Social protection programs need more than a registry—they need to manage eligibility, enrollment, payments, and outcomes. SP-MIS provides:

- **Program management** for multiple concurrent social protection interventions
- **Eligibility engine** using CEL expressions for flexible, transparent targeting
- **Enrollment workflows** with configurable approval chains
- **Payment cycle management** for recurring benefit disbursement
- **Service point tracking** for distribution locations and in-kind transfers
- **Monitoring dashboards** for program performance and coverage

## Core Workflows

| Workflow | Purpose | Key Users |
|----------|---------|-----------|
| **Program Setup** | Define programs with eligibility criteria and benefit structures | Program Managers |
| **Beneficiary Enrollment** | Enroll eligible registrants into programs | Enrollment Officers |
| **Payment Cycles** | Create and execute recurring payment disbursements | Finance Officers |
| **Monitoring** | Track coverage, payments, and program outcomes | M&E Teams |

## Program Types

SP-MIS supports various social protection program types:

| Type | Description | Example |
|------|-------------|---------|
| **Unconditional Cash Transfer (UCT)** | Regular cash payments without conditions | Social pension, child grants |
| **Conditional Cash Transfer (CCT)** | Payments linked to compliance (school attendance, health visits) | Education grants |
| **Emergency Assistance** | Rapid response to shocks and crises | Disaster relief payments |
| **Agricultural Support** | Targeted support for farming households | Input subsidies, crop insurance |
| **In-Kind Transfers** | Non-cash benefits distributed at service points | Food baskets, school supplies |

## Key Capabilities

### Program Management

- **Multiple programs** - Run several programs simultaneously with shared or separate beneficiary pools
- **Program targeting** - Target individuals, households, or groups based on eligibility
- **Benefit configuration** - Define payment amounts, frequency, and duration
- **Program lifecycle** - Track enrollment, active, suspended, and graduated beneficiaries

### Eligibility Engine

SP-MIS uses CEL (Common Expression Language) for powerful, transparent eligibility rules:

```cel
# Universal Child Grant - households with children under 5
group.members.filter(m, m.age < 5).size() >= 1

# Elderly Pension - individuals above retirement age
individual.age >= variables.retirement_age

# Emergency Relief - vulnerability-based targeting
group.dependency_ratio > 0.5 && group.vulnerability_score > 3
```

- **No-code builder** - Logic Studio provides visual expression construction
- **Logic Packs** - Reusable expression libraries for common eligibility patterns
- **Transparency** - Rules are visible and auditable, not hidden in code

### Payment Processing

- **Cycle management** - Create payment cycles with defined periods
- **Entitlement calculation** - Automatically compute amounts based on rules
- **Payment reconciliation** - Track successful, failed, and pending payments
- **Multiple channels** - Support for bank transfers, mobile money, and manual distribution

### Approval Workflows

- **Multi-level approval** - Configure approval chains by program and action type
- **Role-based routing** - Automatic routing to appropriate approvers
- **Audit trail** - Complete history of all approvals and rejections
- **Delegation** - Temporary approval delegation during absences

### Service Points

For in-kind programs and decentralized distribution:

- **Location management** - Track distribution points and their capacity
- **Schedule coordination** - Plan distribution events
- **Attendance tracking** - Record beneficiary collection
- **Stock integration** - Link with inventory for supply planning

## How It Works

```{mermaid}
graph LR
    A[Create<br/>Program] --> B[Define<br/>Eligibility]
    B --> C[Enroll<br/>Beneficiaries]
    C --> D[Create<br/>Cycle]
    D --> E[Calculate<br/>Entitlements]
    E --> F[Disburse<br/>Payments]
    F --> G[Monitor<br/>Outcomes]
```

1. **Create program** - Define program objectives, target population, and benefit structure
2. **Define eligibility** - Build CEL expressions for transparent, rule-based targeting
3. **Enroll beneficiaries** - Automatically or manually enroll eligible registrants
4. **Create cycle** - Initiate a payment period with defined dates and budget
5. **Calculate entitlements** - System computes individual payment amounts
6. **Disburse payments** - Execute payments through configured channels
7. **Monitor outcomes** - Track coverage, payment success rates, and program impact

## Security & Access Control

| Role | Access Level | Typical Users |
|------|--------------|---------------|
| Program Viewer | Read-only access to program data | Auditors, observers |
| Enrollment Officer | Enroll and manage beneficiaries | Field officers |
| Finance Officer | Manage payment cycles and disbursements | Accountants |
| Program Manager | Full program configuration and oversight | Program directors |
| SP-MIS Administrator | System-wide administration | IT administrators |

## Dependencies

SP-MIS builds on Social Registry and adds program-specific modules:

**Includes Social Registry plus:**
- **spp_programs** - Program and enrollment management
- **spp_approval** - Multi-tier approval workflow engine
- **spp_event_data** - Audit trail for program activities
- **spp_service_points** - Distribution location management
- **spp_entitlement** - Entitlement calculation and tracking

## Demo Data

The `spp_mis_demo_v2` module provides sample data for evaluation:

- **6 programs** with CEL eligibility expressions
- **12 personas** (8 eligible scenarios + 4 ineligible edge cases)
- **Logic Pack** with reusable expression variables
- **11 change request types** with approval workflows

Install with:
```shell
ODOO_INIT_MODULES=spp_mis_demo_v2 docker compose --profile ui up -d
```

## Next Steps

**New to SP-MIS?**
- {doc}`/get_started/installation/docker` - Install with demo data
- {doc}`/get_started/first_program/index` - Create your first program

**Setting up for your organization?**
- {doc}`/config_guide/index` - Configuration overview

**Understanding the concepts?**
- {doc}`/learn/concepts/programs` - Program concepts explained
- {doc}`/learn/concepts/eligibility` - Eligibility and targeting

## Learn More

- [World Bank SP Delivery Systems Sourcebook](https://openknowledge.worldbank.org/entities/publication/c44dc506-72dd-5428-a088-6fb7aea53095) - Comprehensive SP-MIS guidance
- [Digital Convergence Initiative](https://spdci.org/) - SP-MIS interoperability standards
- [socialprotection.org](https://socialprotection.org/) - Global social protection resources

## Alternative Names

SP-MIS systems are known by various names globally:

| Acronym | Name | Context |
|---------|------|---------|
| SSNS | Social Safety Net Systems | Safety net programs |
| BMS | Beneficiary Management Systems | Beneficiary-focused systems |
| SAIS | Social Assistance Information Systems | Poverty alleviation |
| ISSS | Integrated Social Services Systems | Multi-sector integration |

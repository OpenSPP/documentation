---
openspp:
  doc_status: draft
---

# Demo module

The SPMIS demo module (`spp_mis_demo_v2`) provides ready-to-use demonstration data for exploring SP-MIS capabilities. It is designed for training, product demonstrations, and system testing without requiring manual data setup.

## What's included

| Item | Count |
|------|-------|
| Social protection programs | 6 |
| Demo personas (registrants) | 7 |
| Pre-configured enrollments | ~500 |
| Program cycles with entitlements | Yes |
| Pre-configured eligibility rules (Logic Packs) | Yes |
| Change requests at various workflow stages | Yes |

## Demo programs

Six programs are pre-configured to demonstrate different program types and configurations:

| Program | Description |
|---------|-------------|
| Cash Transfer | Direct cash payments to eligible households based on income and household size |
| Food Assistance | In-kind food distribution for food-insecure households |
| Child Support | Benefits for families with children below a defined age |
| Emergency Relief | Rapid-response assistance for households affected by shocks |
| Conditional Child Grant | Monthly grant for households with children under 2 |
| Pension | Regular payments for elderly household members |

## Demo personas

Seven pre-created registrant stories illustrate realistic household situations and program journeys:

| Name | Story |
|------|-------|
| Maria Santos | Single mother with 3 children; demonstrates enrollment, compliance passing, and payment processing |
| Ahmed Hassan | Elderly pensioner; demonstrates pension eligibility and regular disbursement |
| Lakshmi Devi | Rural farmer household head; demonstrates agricultural program interactions |
| John Kamau | Urban informal worker; demonstrates cash transfer enrollment and graduation |
| Dela Cruz / Mensah / Bandara household | Remains compliant each cycle; contrasts with non-compliant household |
| Santos / Koffi / Perera household | Fails compliance and graduates; demonstrates program exit workflow |
| Additional households | Cover payment failure and recovery, split/merge change requests, and multi-program enrollment |

*Read the full stories: {doc}`SP-MIS stories </get_started/try_our_products/try_spmis/stories>`*

## Demo users

Four users are pre-configured with distinct roles for testing role-based access:

| Role | Username | Purpose |
|------|----------|---------|
| Administrator | admin | Full system access |
| Program Manager | pm_demo | Program configuration and cycle management |
| Field Officer | officer_demo | Data entry and beneficiary enrollment |
| Approver | approver_demo | Reviewing and approving workflow requests |

## Pre-configured workflows

### Approval definitions

| Workflow | Description |
|----------|-------------|
| Program enrollment | Two-level approval for new beneficiary enrollments |
| High-value payments | Additional approval tier for large disbursements |
| Change requests | Review chain for data modification requests |

### Event types

| Event type | Description |
|------------|-------------|
| Enrollment | Beneficiary enrolled in a program |
| Disbursement | Payment or in-kind distribution made |
| Verification | Identity or eligibility verified |
| Graduation | Beneficiary exits program successfully |

### Change request types

| CR type | Description |
|---------|-------------|
| Add member | Add an individual to an existing household |
| Remove member | Remove an individual from a household |
| Split household | Divide one household into two separate households |
| Merge household | Combine two households into one |
| Exit program | Formal program exit for a beneficiary |

## GIS reports

| Report | Description |
|--------|-------------|
| Beneficiary map | Geographic distribution of registrants by area |
| Service point map | Location of distribution and payment centers |
| Coverage report | Program coverage by administrative region |

## Installing the demo

To load the demo data into a running SP-MIS instance, follow the installation guide: {doc}`Install demo data </get_started/try_our_products/try_spmis/install_data>`.

## Exploring demo scenarios

Once the demo is installed, work through pre-built scenarios that demonstrate key workflows: {doc}`Demo scenarios </get_started/try_our_products/try_spmis/demo_scenarios>`.

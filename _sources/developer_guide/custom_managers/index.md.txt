---
openspp:
  doc_status: draft
  products: [core]
---

# Custom program managers

**For: developers**

Build custom program managers to implement eligibility, entitlement, cycle, and payment logic for OpenSPP programs.

## How to use this section

1. Read {doc}`manager_pattern` to understand the wrapper/implementation architecture
2. Read {doc}`building_managers` for the step-by-step process and method reference
3. Follow the {doc}`tutorial` to build a complete CCT program with all three manager types

```{tip}
The tutorial includes a downloadable module: {download}`spp_cct_managers.zip </_static/samples/spp_cct_managers.zip>`
```

## When do you need this?

Programs in OpenSPP use managers for eligibility, entitlements, cycles, and payments. The built-in managers cover common patterns, but you need a custom manager when the program requires logic they do not support.

| Requirement | Built-in managers | Custom manager |
|-------------|:-:|:-:|
| Standard recurrence-based cycles | Yes | |
| Per-beneficiary fixed-amount entitlements | Yes | |
| Basic eligibility filters | Yes | |
| Custom eligibility formula (e.g., income + children) | | Yes |
| Per-child or per-member entitlement calculations | | Yes |
| Non-standard cycle timing (e.g., calendar quarters) | | Yes |
| Integration with external payment gateways | | Yes |
| Multi-criteria scoring for eligibility ranking | | Yes |

## Topics covered

- {doc}`manager_pattern` — how the strategy pattern works: wrapper models, implementation models, base classes, and extension points
- {doc}`building_managers` — step-by-step guide with registration pattern and method reference for all manager types
- {doc}`tutorial` — complete module with eligibility, entitlement, and cycle managers for a conditional cash transfer program

## See also

- {doc}`/developer_guide/change_request_types/index` — building custom change request types (similar tutorial pattern)

```{toctree}
:maxdepth: 2
:hidden:

manager_pattern
building_managers
tutorial
```

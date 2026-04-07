---
openspp:
  doc_status: draft
  products: [core]
---

# Custom change request types

**For: developers**

Build change request (CR) types that go beyond what Studio and UI configuration support.

## How to use this section

1. Read {doc}`tutorial` first — build a complete CR type end-to-end
2. Use the reference pages when building your own types:
   - {doc}`detail_models` for field patterns and validation
   - {doc}`apply_strategies` for custom apply logic
   - {doc}`approval_hooks` for lifecycle customization
   - {doc}`testing` for test patterns

## Prerequisites

- Python and Odoo model inheritance
- Development environment set up ({doc}`/developer_guide/setup/index`)
- Familiarity with the CR system concepts ({doc}`/config_guide/change_request_types/overview`)

## When do you need code?

Most CR types can be created through Studio or UI configuration. You only need a custom module when the CR type requires logic that configuration cannot express.

| Requirement | Studio / Config | Custom module |
|-------------|:-:|:-:|
| Capture new fields on a form | Yes | |
| Map detail fields to registrant fields | Yes | |
| Require document uploads | Yes | |
| Configure approval workflows | Yes | |
| Set up conflict detection rules | Yes | |
| Validate fields with custom Python logic | | Yes |
| Create or delete related records on apply | | Yes |
| Update multiple models in a single apply | | Yes |
| Compute fields dynamically (e.g., filter a dropdown based on another field) | | Yes |
| Add custom conflict detection beyond built-in scopes | | Yes |
| Extend approval hooks with side effects (e.g., send notifications) | | Yes |

**Rule of thumb:** If the apply action does anything other than copy fields from the detail record to the registrant, you need a custom module.

For Studio-based CR type creation, see {doc}`/config_guide/change_request_types/custom_detail_models`.

## Architecture

Every CR type has three layers:

1. **CR type** (`spp.change.request.type`) — configuration record that defines the type's name, target, detail model, and apply strategy
2. **Detail model** (`spp.cr.detail.*`) — an Odoo model with real fields that captures the requested changes
3. **Apply strategy** (`spp.cr.strategy.*` or `spp.cr.apply.*`) — the logic that applies the approved changes to the registry

For a full explanation of this architecture, see {doc}`/config_guide/change_request_types/overview`.

## What you will build

The {doc}`tutorial` walks you through building a **Transfer Member** CR type — a request to move an individual from one household to another. This type requires a custom apply strategy because it must end the source membership and create a new one in the target group, which field mapping alone cannot do.

By the end of the tutorial, you will have a working Odoo module with:

- A detail model with computed fields and validation
- A form view with dynamic field filtering
- A custom apply strategy that modifies group memberships
- Security rules and access control
- A test suite covering happy paths and error cases

## Reference guides

After the tutorial, use these references when building your own CR types:

- {doc}`detail_models` — base class API, field patterns, validation, and the 12 built-in detail models
- {doc}`apply_strategies` — when to use field mapping vs. custom strategies, and how to build each
- {doc}`approval_hooks` — lifecycle hooks, dynamic approval, conflict detection, and audit events
- {doc}`testing` — test setup patterns, what to test, and common pitfalls

```{toctree}
:maxdepth: 2
:hidden:

tutorial
detail_models
apply_strategies
approval_hooks
testing
```

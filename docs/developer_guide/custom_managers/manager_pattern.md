---
openspp:
  doc_status: draft
  products: [core]
---

# Manager pattern

**For: developers**

OpenSPP uses the **strategy pattern** for program management logic. Instead of hardcoding business rules into the program model, each program delegates decisions to pluggable "managers." This lets different programs use different eligibility criteria, entitlement calculations, payment methods, and cycle behaviors without changing core code.

## How it works

Each program has manager slots connected via Many2many fields. Each slot accepts one or more managers of a specific type. Managers are Odoo models that inherit from a base class and implement the required interface methods.

```
spp.program
    |
    +-- eligibility_manager_ids  → spp.eligibility.manager (wrapper)
    |                                → spp.program.membership.manager.default
    |
    +-- entitlement_manager_ids  → spp.program.entitlement.manager (wrapper)
    |                                → spp.program.entitlement.manager.cash
    |                                → spp.program.entitlement.manager.inkind
    |
    +-- cycle_manager_ids        → spp.cycle.manager (wrapper)
    |                                → spp.cycle.manager.default
    |
    +-- payment_manager_ids      → spp.program.payment.manager (wrapper)
                                     → spp.program.payment.manager.default
```

### Wrapper and implementation models

Each manager type uses a **wrapper/implementation** pattern:

1. **Wrapper model** (e.g., `spp.program.entitlement.manager`) — Holds a `manager_ref_id` Reference field that points to the actual implementation. This is what the program links to via Many2many.

2. **Implementation model** (e.g., `spp.program.entitlement.manager.cash`) — Contains the actual business logic and configuration fields. Inherits from a base abstract model.

This two-level indirection lets the program hold references to managers of different implementation types through a single Many2many field.

## Manager types

### Eligibility managers

Determine which registrants qualify for a program.

| Model | Description |
|-------|-------------|
| `spp.eligibility.manager` | Wrapper |
| `spp.program.membership.manager` | Base abstract model |
| `spp.program.membership.manager.default` | Default CEL-based eligibility |

**Key methods:**

- `enroll_eligible_registrants(program_memberships)` — filters program memberships to those meeting the criteria
- `verify_cycle_eligibility(cycle, membership)` — re-checks eligibility for cycle members
- `import_eligible_registrants(state=None)` — imports qualifying registrants into the program

### Entitlement managers

Calculate what each beneficiary receives in a cycle.

| Model | Description |
|-------|-------------|
| `spp.program.entitlement.manager` | Wrapper |
| `spp.base.program.entitlement.manager` | Base abstract model |
| `spp.program.entitlement.manager.default` | Fixed amount per cycle |
| `spp.program.entitlement.manager.cash` | CEL-based cash with line items |
| `spp.program.entitlement.manager.inkind` | In-kind (product-based) entitlements |

**Cash entitlement items** (`spp.program.entitlement.manager.cash.item`):

| Field | Description |
|-------|-------------|
| `amount` | Base amount |
| `condition` | CEL expression for conditional inclusion |
| `multiplier_field` | Field to multiply amount by (e.g., household size) |
| `max_multiplier` | Maximum multiplier cap |

### Cycle managers

Control how program cycles are created and processed.

| Model | Description |
|-------|-------------|
| `spp.cycle.manager` | Wrapper |
| `spp.base.cycle.manager` | Base abstract model |
| `spp.cycle.manager.default` | Default with recurrence support |

**Key method:** `new_cycle(name, new_start_date, sequence)` — Creates the next cycle. The manager already knows its own `program_id`, so it is not passed as an argument.

### Payment managers

Handle payment processing for approved entitlements.

| Model | Description |
|-------|-------------|
| `spp.program.payment.manager` | Wrapper |
| `spp.base.program.payment.manager` | Base abstract model |
| `spp.program.payment.manager.default` | Default payment processing |

### Other managers

| Type | Wrapper model | Purpose |
|------|---------------|---------|
| Program | `spp.program.manager` | Program lifecycle management |
| Deduplication | `spp.deduplication.manager` | Duplicate detection strategies |
| Notification | `spp.program.notification.manager` | Beneficiary communications |
| Compliance | `spp.compliance.manager` | Compliance checking |

## Base classes

Each manager type has its own base class:

| Manager type | Base class |
|-------------|------------|
| Eligibility | `spp.program.membership.manager` |
| Entitlement | `spp.base.program.entitlement.manager` |
| Cycle | `spp.base.cycle.manager` |
| Payment | `spp.base.program.payment.manager` |

Eligibility and entitlement base classes also inherit from `spp.base.programs.manager`, which provides common utility methods like `_safe_eval()` for CEL expression evaluation. Cycle managers define their own standalone base.

Each base class provides `name` and `program_id` fields. The mixin `spp.manager.mixin` provides the `manager_ref_id` Reference field and display name computation for wrapper models.

When you select a manager implementation from the dropdown (e.g., "CCT Eligibility"), the wrapper's `manager_ref_id` stores a reference string like `spp.program.membership.manager.cct,42`. The wrapper then delegates method calls to this implementation record.

## Linking managers to programs

Managers are linked to programs via Many2many fields using the Odoo Command API:

```python
# Set a program's entitlement manager (replaces existing)
program.write({
    "entitlement_manager_ids": [(6, 0, [wrapper_id])]
})
```

```{important}
Most manager slots are constrained to a single manager per program. Use Command `(6, 0, [id])` to replace, not `(4, id)` to append. See the individual manager type guides for complete examples.
```

## Source code

All manager models are in `spp_programs/models/managers/`:

| File | Contents |
|------|----------|
| `base_manager.py` | `spp.base.programs.manager` abstract base |
| `manager_mixin.py` | `spp.manager.mixin` (wrapper reference field) |
| `eligibility_manager.py` | Eligibility wrapper and default implementation |
| `entitlement_manager_base.py` | Entitlement wrapper and base implementation |
| `entitlement_manager_cash.py` | Cash entitlement with CEL items |
| `entitlement_manager_inkind.py` | In-kind entitlement with products |
| `entitlement_manager_default.py` | Fixed-amount entitlement |
| `cycle_manager_base.py` | Cycle wrapper and default implementation |
| `payment_manager.py` | Payment wrapper and default implementation |
| `program_manager.py` | Program lifecycle manager |
| `deduplication_manager.py` | Deduplication strategies |
| `notification_manager.py` | Notification manager |
| `compliance_manager.py` | Compliance checking |
| `recurrence_mixin.py` | Recurrence scheduling mixin |
| `source_mixin.py` | Source tracking mixin for managers |

## What's next

- {doc}`building_managers` — step-by-step guide to creating a custom manager, with method references for all manager types
- {doc}`tutorial` — build a complete CCT program module with eligibility, entitlement, and cycle managers

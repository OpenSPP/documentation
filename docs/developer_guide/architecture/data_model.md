---
openspp:
  doc_status: draft
  products: [core]
---

# Data model

**For: developers**

This page describes the core data entities in OpenSPP and how they relate to each other. Understanding these models is essential for building modules that interact with the registry, programs, or entitlements.

## Registrants

OpenSPP does not define its own registrant model from scratch. Instead, it extends Odoo's built-in `res.partner` model using `_inherit`. This means all registrant data lives in the `res_partner` table alongside regular Odoo contacts.

### Individuals and groups

Both individuals and groups are `res.partner` records, distinguished by flags:

| Field           | Individual | Group  |
| --------------- | ---------- | ------ |
| `is_registrant` | `True`     | `True` |
| `is_group`      | `False`    | `True` |

**Individual fields** (defined in `spp_registry/models/individual.py`):

| Field         | Type      | Description            |
| ------------- | --------- | ---------------------- |
| `family_name` | Char      | Last name              |
| `given_name`  | Char      | First name             |
| `addl_name`   | Char      | Additional/middle name |
| `birthdate`   | Date      | Date of birth          |
| `gender`      | Selection | Gender                 |
| `birth_place` | Char      | Place of birth         |

**Group fields** (defined in `spp_registry/models/group.py`):

| Field           | Type     | Description                                |
| --------------- | -------- | ------------------------------------------ |
| `group_type_id` | Many2one | Reference to group type vocabulary         |
| `kind`          | Many2one | Group kind (deprecated, use group_type_id) |

### Group membership

The link between individuals and groups is managed by `spp.group.membership`:

| Field        | Type                     | Description                                        |
| ------------ | ------------------------ | -------------------------------------------------- |
| `group`      | Many2one (`res.partner`) | The group                                          |
| `individual` | Many2one (`res.partner`) | The individual member                              |
| `kind`       | Many2many                | Membership roles (head of household, spouse, etc.) |
| `start_date` | Date                     | When membership began                              |
| `ended_date` | Date                     | When membership ended (if applicable)              |

### Identifiers

Registrants can have multiple IDs (national ID, passport, etc.) stored in `spp.registry.id`:

| Field         | Type                     | Description                              |
| ------------- | ------------------------ | ---------------------------------------- |
| `partner_id`  | Many2one (`res.partner`) | The registrant                           |
| `id_type`     | Many2one (`spp.id.type`) | Type of ID (e.g., national ID, passport) |
| `value`       | Char                     | The ID number                            |
| `expiry_date` | Date                     | Expiration date                          |

ID types (`spp.id.type`) support namespace URIs for interoperability (e.g., `urn:gov:ph:psa:philsys` for Philippines PhilSys IDs), enabling cross-system identifier matching.

### Relationships

Registrants can have relationships with each other via `spp.registry.relationship`:

| Field         | Type                          | Description        |
| ------------- | ----------------------------- | ------------------ |
| `source`      | Many2one (`res.partner`)      | Source registrant  |
| `destination` | Many2one (`res.partner`)      | Related registrant |
| `relation`    | Many2one (`spp.relationship`) | Relationship type  |

## Programs

Programs are the central entity for social protection delivery. A program manages the full lifecycle from enrollment to payment.

### Program model (`spp.program`)

Key fields:

| Field                    | Type      | Description             |
| ------------------------ | --------- | ----------------------- |
| `name`                   | Char      | Program name            |
| `target_type`            | Selection | `group` or `individual` |
| `state`                  | Selection | `active`, `ended`       |
| `program_membership_ids` | One2many  | Enrolled beneficiaries  |
| `cycle_ids`              | One2many  | Program cycles          |

### Managers (configuration)

Each program has managers that encapsulate domain logic. Instead of hardcoding business rules, programs delegate decisions to pluggable managers using the strategy pattern. Each manager type handles a specific concern:

| Field                       | Manager type  | Purpose                            |
| --------------------------- | ------------- | ---------------------------------- |
| `eligibility_manager_ids`   | Eligibility   | Who qualifies for the program      |
| `cycle_manager_ids`         | Cycle         | How cycles are created and managed |
| `entitlement_manager_ids`   | Entitlement   | What beneficiaries receive         |
| `payment_manager_ids`       | Payment       | How payments are processed         |
| `program_manager_ids`       | Program       | Program lifecycle management       |
| `deduplication_manager_ids` | Deduplication | Duplicate detection                |
| `notification_manager_ids`  | Notification  | Beneficiary communications         |

Managers are linked to programs via Many2many fields. Each slot uses a wrapper/implementation model pattern that allows different implementation types (e.g., cash vs. in-kind entitlements) through a single reference field. See {doc}`../custom_managers/index` for a full explanation of the manager pattern and how to build custom managers.

### Program membership (`spp.program.membership`)

Links registrants to programs:

| Field             | Type                     | Description                                                           |
| ----------------- | ------------------------ | --------------------------------------------------------------------- |
| `partner_id`      | Many2one (`res.partner`) | The beneficiary                                                       |
| `program_id`      | Many2one (`spp.program`) | The program                                                           |
| `state`           | Selection                | `draft`, `enrolled`, `paused`, `exited`, `not_eligible`, `duplicated` |
| `enrollment_date` | Date                     | When enrolled                                                         |
| `exit_date`       | Date                     | When exited (if applicable)                                           |

## Cycles

Cycles represent distribution periods within a program (e.g., monthly, quarterly).

### Cycle model (`spp.cycle`)

| Field                  | Type                     | Description                                                           |
| ---------------------- | ------------------------ | --------------------------------------------------------------------- |
| `name`                 | Char                     | Cycle name                                                            |
| `program_id`           | Many2one (`spp.program`) | Parent program                                                        |
| `state`                | Selection                | `draft`, `to_approve`, `approved`, `distributed`, `canceled`, `ended` |
| `start_date`           | Date                     | Cycle start                                                           |
| `end_date`             | Date                     | Cycle end                                                             |
| `cycle_membership_ids` | One2many                 | Beneficiaries in this cycle                                           |

## Entitlements

Entitlements represent what a beneficiary receives in a given cycle.

### Entitlement model (`spp.entitlement`)

| Field            | Type                     | Description                                                                                  |
| ---------------- | ------------------------ | -------------------------------------------------------------------------------------------- |
| `partner_id`     | Many2one (`res.partner`) | The beneficiary                                                                              |
| `cycle_id`       | Many2one (`spp.cycle`)   | The cycle                                                                                    |
| `state`          | Selection                | `draft`, `pending_validation`, `approved`, `trans2FSP`, `rdpd2ben`, `rejected*`, `cancelled` |
| `initial_amount` | Float                    | Calculated entitlement amount                                                                |

## Program lifecycle

Understanding how programs, cycles, and entitlements move through their states is essential for developers extending the system. Here is the end-to-end flow:

### 1. Program setup

```
spp.program: active
```

A program is created and configured with managers (eligibility, entitlement, cycle, payment). Programs start in `active` state.

### 2. Beneficiary enrollment

```
Program.import_eligible_registrants()    → creates memberships in "draft"
Program.enroll_eligible_registrants()    → moves memberships to "enrolled"
Program.verify_eligibility()             → re-checks enrolled members, removes ineligible
```

| Membership state | Meaning                       |
| ---------------- | ----------------------------- |
| `draft`          | Imported but not yet enrolled |
| `enrolled`       | Actively participating        |
| `paused`         | Temporarily suspended         |
| `exited`         | Left the program              |
| `not_eligible`   | Failed eligibility check      |
| `duplicated`     | Identified as duplicate       |

### 3. Cycle creation and processing

```
Program.create_new_cycle()                        → new cycle in "draft"
Cycle.copy_beneficiaries_from_program()            → copies enrolled members into cycle
Cycle.prepare_entitlement()                        → creates entitlements via entitlement manager
Cycle (button: "To Approve")                       → cycle moves to "to_approve"
Cycle.approve() / CycleManager.approve_cycle()     → cycle moves to "approved"
Cycle.validate_entitlement()                       → entitlements move to "pending_validation"
```

| Cycle state   | Meaning                                 |
| ------------- | --------------------------------------- |
| `draft`       | Newly created, being prepared           |
| `to_approve`  | Submitted for approval                  |
| `approved`    | Approved, entitlements can be validated |
| `distributed` | Payments completed                      |
| `canceled`    | Cancelled                               |
| `ended`       | Cycle period ended                      |

### 4. Entitlement approval and payment

```
Entitlement.approve_entitlement()     → moves to "approved"
(Payment manager processes payment)    → moves to "trans2FSP" then "rdpd2ben"
```

| Entitlement state    | Meaning                                   |
| -------------------- | ----------------------------------------- |
| `draft`              | Created by entitlement manager            |
| `pending_validation` | Awaiting approval                         |
| `approved`           | Approved for payment                      |
| `trans2FSP`          | Transferred to financial service provider |
| `rdpd2ben`           | Redeemed/paid to beneficiary              |
| `rejected*`          | Rejected (multiple reasons)               |
| `cancelled`          | Cancelled                                 |

### Flow summary

```
Program (active)
    |
    +-- import_eligible_registrants() → Memberships (draft)
    +-- enroll_eligible_registrants() → Memberships (enrolled)
    |
    +-- create_new_cycle() → Cycle (draft)
            |
            +-- copy_beneficiaries_from_program()
            +-- prepare_entitlement() → Entitlements (draft)
            +-- "To Approve" → Cycle (to_approve)
            +-- approve() → Cycle (approved)
            +-- validate_entitlement() → Entitlements (pending_validation)
                    |
                    +-- approve_entitlement() → Entitlements (approved)
                    +-- (payment) → Entitlements (trans2FSP → rdpd2ben)
```

Each step in this flow is delegated to the appropriate manager. The eligibility manager handles `import_eligible_registrants`, the entitlement manager handles `prepare_entitlement`, the cycle manager handles cycle state transitions, and the payment manager handles the payment steps.

## Supporting entities

These entities support the core pipeline. They are described briefly here — refer to the source code for full field definitions.

### Vocabularies

Controlled code lists used throughout OpenSPP for standardized values (ID types, relationship types, group types, etc.).

| Model                      | Purpose                                                      | Module           |
| -------------------------- | ------------------------------------------------------------ | ---------------- |
| `spp.vocabulary`           | A vocabulary (e.g., "ID Types", "Relationship Types")        | `spp_vocabulary` |
| `spp.vocabulary.code`      | A code within a vocabulary (e.g., "National ID", "Passport") | `spp_vocabulary` |
| `spp.vocabulary.selection` | Deployment-specific subset of codes to expose                | `spp_vocabulary` |
| `spp.deployment.profile`   | Deployment profile (Agriculture, Social Protection, etc.)    | `spp_vocabulary` |

Vocabularies are referenced by many models. For example, `spp.id.type` uses vocabulary codes for ID type definitions, and group types reference vocabulary codes for classification.

### Areas

Hierarchical geographic areas for targeting and reporting (country → region → district → sub-district).

| Model             | Purpose                                     | Module     |
| ----------------- | ------------------------------------------- | ---------- |
| `spp.area`        | Geographic area with parent/child hierarchy | `spp_area` |
| `spp.area.tag`    | Tags for area classification                | `spp_area` |
| `spp.area.import` | Bulk area import from shapefiles or CSV     | `spp_area` |

Areas are linked to registrants, programs, and service points for geographic targeting and reporting.

### Service points

Physical locations where beneficiaries receive services or collect entitlements.

| Model               | Purpose                                                         | Module               |
| ------------------- | --------------------------------------------------------------- | -------------------- |
| `spp.service.point` | A service delivery location (office, distribution center, etc.) | `spp_service_points` |

Service points are linked to areas and can be assigned to programs for distribution planning.

### Change requests

Data modification requests that go through an approval workflow before being applied to the registry.

| Model                             | Purpose                                                      | Module                  |
| --------------------------------- | ------------------------------------------------------------ | ----------------------- |
| `spp.change.request`              | A change request (create, update, or delete registrant data) | `spp_change_request_v2` |
| `spp.change.request.type`         | Defines a type of change request and its configuration       | `spp_change_request_v2` |
| `spp.cr.detail.base`              | Abstract base for CR detail models (custom data per CR type) | `spp_change_request_v2` |
| `spp.change.request.type.mapping` | Maps CR type fields to target model fields                   | `spp_change_request_v2` |
| `spp.cr.conflict.rule`            | Rules for detecting conflicting concurrent changes           | `spp_change_request_v2` |

See {doc}`../change_request_types/index` for building custom CR types.

### Event data

Records of field visits, surveys, or other data collection events linked to registrants.

| Model             | Purpose                                              | Module           |
| ----------------- | ---------------------------------------------------- | ---------------- |
| `spp.event.data`  | An event record (survey response, field visit, etc.) | `spp_event_data` |
| `spp.event.type`  | Defines an event type and its fields                 | `spp_event_data` |
| `spp.event.field` | A field definition within an event type              | `spp_event_data` |

Events are linked to registrants via `res.partner` and can trigger program membership changes or entitlement recalculations.

### Approval workflows

Multi-tier approval system used by programs, change requests, and other workflows.

| Model                     | Purpose                                                  | Module         |
| ------------------------- | -------------------------------------------------------- | -------------- |
| `spp.approval.definition` | Defines an approval workflow (tiers, groups, conditions) | `spp_approval` |
| `spp.approval.tier`       | A tier within an approval workflow                       | `spp_approval` |
| `spp.approval.review`     | A review instance tracking approval progress             | `spp_approval` |
| `spp.approval.mixin`      | Abstract mixin — add to any model to make it approvable  | `spp_approval` |
| `spp.approval.config`     | Global approval configuration                            | `spp_approval` |

Models that need approval workflows inherit from `spp.approval.mixin`, which adds approval state fields and workflow methods.

## Entity relationship summary

```
res.partner (registrants)
    |
    +-- spp.group.membership      (individual ↔ group links)
    +-- spp.registry.id           (identity documents)
    +-- spp.registry.relationship (inter-registrant relationships)
    +-- spp.phone.number          (phone numbers)
    +-- spp.event.data            (field data collection)
    +-- spp.change.request        (data modification requests)
    |
    +-- spp.program.membership    (enrollment in programs)
            |
            +-- spp.program       (program definition)
            |       +-- managers  (eligibility, entitlements, cycles, payments)
            |       +-- spp.approval.definition (approval workflows)
            |
            +-- spp.cycle         (distribution periods)
            |       +-- spp.area  (geographic targeting)
            |
            +-- spp.entitlement   (what beneficiaries receive)
                    +-- spp.service.point (delivery locations)

spp.vocabulary                    (code systems — referenced by many models)
    +-- spp.vocabulary.code       (individual codes within a vocabulary)
```

## Source code locations

### Core entities

| Model              | Module         | File                           |
| ------------------ | -------------- | ------------------------------ |
| Registrant (base)  | `spp_registry` | `models/registrant.py`         |
| Individual         | `spp_registry` | `models/individual.py`         |
| Group              | `spp_registry` | `models/group.py`              |
| Group membership   | `spp_registry` | `models/group_membership.py`   |
| Registry ID        | `spp_registry` | `models/reg_id.py`             |
| Relationships      | `spp_registry` | `models/reg_relationship.py`   |
| Program            | `spp_programs` | `models/programs.py`           |
| Program membership | `spp_programs` | `models/program_membership.py` |
| Cycle              | `spp_programs` | `models/cycle.py`              |
| Entitlement        | `spp_programs` | `models/entitlement.py`        |
| Managers           | `spp_programs` | `models/managers/*.py`         |

### Supporting entities

| Model               | Module                  | File                            |
| ------------------- | ----------------------- | ------------------------------- |
| Vocabulary          | `spp_vocabulary`        | `models/vocabulary.py`          |
| Vocabulary code     | `spp_vocabulary`        | `models/vocabulary_code.py`     |
| Area                | `spp_area`              | `models/area_core.py`           |
| Service point       | `spp_service_points`    | `models/registrant.py`          |
| Change request      | `spp_change_request_v2` | `models/change_request.py`      |
| CR type             | `spp_change_request_v2` | `models/change_request_type.py` |
| Event data          | `spp_event_data`        | `models/event_data.py`          |
| Event type          | `spp_event_data`        | `models/event_type.py`          |
| Approval definition | `spp_approval`          | `models/approval_definition.py` |
| Approval mixin      | `spp_approval`          | `models/approval_mixin.py`      |

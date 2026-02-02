---
openspp:
  doc_status: draft
  products: [core]
---

# Learn

These pages explain the core concepts behind OpenSPP. Understanding these concepts will help you use and configure the platform effectively.

## Registry

The {doc}`registry` is the central database storing information about people and groups. It's the foundation for all programs and services.

## Programs

{doc}`programs` define social protection interventions—who receives benefits, what they receive, and how benefits are delivered.

## Cycles

{doc}`cycles` are distribution rounds within programs. Each cycle represents a period when benefits are calculated and paid out.

## Eligibility

{doc}`eligibility` determines who qualifies for programs based on defined criteria like age, income, location, or household composition.

## Compliance

{doc}`compliance` tracks whether beneficiaries meet ongoing conditions like school attendance, health checkups, or training participation—essential for conditional cash transfer programs.

## Entitlements

{doc}`entitlements` specify what each beneficiary receives in a cycle—whether cash, vouchers, or physical goods.

## Payments

{doc}`payments` are the actual disbursements that deliver entitlements to beneficiaries through various channels.

## Deduplication

{doc}`deduplication` identifies and handles duplicate registrations to prevent fraud and ensure each beneficiary receives benefits only once.

## Change requests

{doc}`change-requests` provide a controlled workflow for updating registry data with approval processes, audit trails, and supporting documentation.

```{toctree}
:maxdepth: 2
:hidden:

registry
programs
cycles
eligibility
compliance
entitlements
payments
deduplication
change-requests
```
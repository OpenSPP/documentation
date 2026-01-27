---
openspp:
  doc_status: draft
  products: [programs]
  applies_to:
    - sp_mis
---

# Understand Programs

**Applies to:** SP-MIS

## What You Will Learn

This guide explains the core concepts of OpenSPP programs. By the end, you will understand:

- What a program is and what information it contains
- How programs, cycles, and entitlements connect
- The different states a program can be in
- How to navigate the program interface

## What is a Program?

A **program** is a social protection intervention that delivers benefits to eligible registrants. Examples include:

- Monthly cash transfers to low-income households
- Food assistance for families with children under 5
- Emergency relief payments during disasters

Each program defines:

| Component | Purpose |
|-----------|---------|
| **Target type** | Who can enroll (individuals or groups/households) |
| **Eligibility rules** | Criteria that determine who qualifies |
| **Entitlement rules** | How benefit amounts are calculated |
| **Cycles** | Time periods for benefit distribution |

## How Programs, Cycles, and Entitlements Connect

```
Program
   |
   +-- Beneficiaries (enrolled registrants)
   |
   +-- Cycle 1 (January 2025)
   |      |
   |      +-- Entitlement for Beneficiary A
   |      +-- Entitlement for Beneficiary B
   |      +-- Entitlement for Beneficiary C
   |
   +-- Cycle 2 (February 2025)
   |      |
   |      +-- Entitlement for Beneficiary A
   |      +-- Entitlement for Beneficiary B
   |      +-- Entitlement for Beneficiary C
   |
   +-- Cycle 3 (March 2025)
          |
          +-- (entitlements generated when cycle is prepared)
```

**The relationship works like this:**

1. **Registrants** are imported into a program
2. **Eligibility is verified** to confirm they qualify
3. Verified registrants become **beneficiaries**
4. For each **cycle**, entitlements are generated for all beneficiaries
5. Entitlements are approved and benefits are distributed

## Program States

A program can be in one of two states:

| State | Meaning | What You Can Do |
|-------|---------|-----------------|
| **Active** | Program is operational | Import registrants, enroll beneficiaries, create cycles |
| **Ended** | Program is closed | View only - no changes allowed |

![Program with Active status](/_images/en-us/programs/understanding/01-program-form-showing-active-status-badge.png)

## Navigate the Program Interface

### Finding Programs

1. Click **Programs** in the main menu.

   ![Programs menu](/_images/en-us/programs/understanding/02-main-menu-with-programs-option-highlighted.png)

2. Click **Programs** in the submenu.

   ![Programs submenu](/_images/en-us/programs/understanding/03-programs-submenu-showing-programs-link.png)

3. The program list shows all programs you have access to.

### Program List Columns

| Column | Description |
|--------|-------------|
| **Name** | Program name |
| **Target Type** | Group (households) or Individual |
| **Beneficiaries** | Number of enrolled beneficiaries |
| **Cycles** | Number of cycles created |
| **State** | Active or Ended |

### Opening a Program

Click on a program row to open the program form.

![Program form](/_images/en-us/programs/understanding/hover-program.png)

## Program Form Overview

The program form has four main tabs:

### Overview Tab

Shows basic program information and recent cycles:

| Field | Description |
|-------|-------------|
| **Name** | Program name |
| **Target Type** | Group or Individual |
| **Company** | Organization running the program (if multi-company) |
| **Beneficiaries** | Total number of registered beneficiaries |
| **Eligible Beneficiaries** | Number currently enrolled |

The **Recent Cycles** section shows the most recent cycles with their status.

![Program overview tab](/_images/en-us/programs/understanding/06-program-overview-tab-showing-basic-information.png)

### Beneficiaries Tab

Lists all registrants associated with this program:

| Column | Description |
|--------|-------------|
| **Registrant** | Name of the beneficiary |
| **Enrollment Date** | When they were enrolled |
| **State** | Draft, Enrolled, Paused, Exited, Not Eligible, or Duplicated |

![Beneficiaries tab](/_images/en-us/programs/understanding/07-program-beneficiaries-tab.png)

### Configuration Tab

Program Managers can view and edit program settings here. This tab is not visible to all users.

![configuration tab](/_images/en-us/programs/understanding/configuration-tab.png)

### History Tab

Shows audit information: who created and last modified the program.

![history tab](/_images/en-us/programs/understanding/history-tab.png)

## Smart Buttons

At the top of the program form, smart buttons provide quick access to related information:

| Button | Shows |
|--------|-------|
| **Beneficiaries** | Opens the full beneficiary list |
| **Cycles** | Opens the list of all cycles |
| **Duplicates** | Opens the list of duplicate records (if any exist) |

![Program smart buttons](/_images/en-us/programs/understanding/smart-buttons.png)

## Program Actions

The header bar shows actions you can perform (based on your role):

| Button | What It Does | When Available |
|--------|--------------|----------------|
| **Import Eligible** | Import registrants matching eligibility criteria | Active programs |
| **Enroll Eligible** | Enroll all eligible registrants | Active programs with beneficiaries |
| **Verify Eligibility** | Re-check eligibility for all beneficiaries | Active programs |
| **New Cycle** | Create a new distribution cycle | Active programs with enrollees |
| **Deduplicate** | Find and mark duplicate beneficiaries | Active programs |
| **Notify** | Send notifications to beneficiaries | Active programs |

![Program action buttons](/_images/en-us/programs/understanding/09-program-action-buttons.png)

## Are You Stuck?

**Cannot see the Configuration tab?**
This tab is only visible to Program Managers and Administrators.

**Beneficiaries count shows zero but you added people?**
Registrants must be enrolled (not just imported). Run **Enroll Eligible** to move them from draft to enrolled status.

**Cannot see any action buttons?**
Your role may not have permission to perform program actions. Contact your administrator.

**Program shows a warning about missing journal?**
This is an accounting configuration issue. Contact your Program Manager or Administrator.

## Next Steps

- {doc}`program_cycles` - Learn how to work with program cycles
- {doc}`enroll_beneficiaries` - Add registrants to a program

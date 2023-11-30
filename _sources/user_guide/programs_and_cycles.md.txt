# Programs and cycles


# Introduction

OpenSPP centers around Social Protection {term}`Program` and {term}`Cycle` Management, using the World Bank Sourcebook Model, a widely accepted framework for designing and implementing programs.

OpenSPP enables program administrators to define eligibility criteria, configure payment schemes, manage grievance redress mechanisms, track inventory and distribution of goods, and generate reports and dashboards for monitoring and evaluation 
purposes.

# Program components

In OpenSPP, a program is composed of multiple components that can be installed and configured independently. OpenSPP provide a default program creation wizard, but this one can be replaced to fit the needs of the program administrator and the seperation of duty between different parties.

## Eligibility manager

The eligibility manager verifies if a beneficiary is eligible for a given program. The eligibility determination can be based on data stored in OpenSPP or on an external system using API calls.

The eligibility manager allows to select one or multiple areas and different categorical or threshold based criteria based on the data stored in OpenSPP.


## Cycle manager

The cycle manager defines how a cycle is managed. It can be used to define how a cycle is created, how beneficiaries are selected, how payments are made, how payments are reconciled, etc.

## Entitlement manager

The entitlement manager determines what a beneficiary is entitled to for a given cycle.

### Basic cash

### Cash

### In kinds

### Basket entitlement

# Creating a new program

- Open the **Programs** menu.
- Click **Create Program**. You will be taken through a wizard to create a new program.

```{figure} programs_and_cycles/program-wizard-1.png
:align: center
:height: 300
:alt: View of a program creation wizard emphasizing the first step in OpenSPP
```

- Give a name to your program.
- Select the target type. This is the type of entity that will be targeted by the program, group or individual. For example, if you are running a program to provide food assistance to households, you will select **Household**.
- If you wish to restrict the program to a specific area, select the target area. This is the area that will be targeted by the program. For example, if you are running a program to provide food assistance to households in a specific district, you will select the district name(s).

---
openspp:
  doc_status: draft
---

# Registry

The Registry is the central database that stores information about people and groups in OpenSPP. It's the foundation that all programs, eligibility rules, and benefits are built upon.

**For:** All audiences

## What is a Registry?

A registry is a structured database of individuals, households, and other groups that may be eligible for social protection programs. Think of it as a comprehensive address book that contains not just names and contact information, but also demographic data, household composition, identification documents, and other information needed to determine program eligibility and deliver benefits.

In social protection systems, registries serve several purposes:

| Purpose | Description |
|---------|-------------|
| **Identification** | Uniquely identify individuals and households across programs |
| **Assessment** | Store demographic and socio-economic data used to assess needs |
| **Eligibility** | Provide data for determining who qualifies for which programs |
| **Delivery** | Maintain payment details and contact information for benefit delivery |
| **Coordination** | Share verified data across multiple programs and agencies |

## Registry vs. Program Enrollment

It's important to understand the difference:

| Registry | Program Enrollment |
|----------|-------------------|
| **Who might be eligible** for programs | **Who is enrolled** in a specific program |
| **Broader population** (potential beneficiaries) | **Subset** of registry (actual beneficiaries) |
| **Longer-term** data storage | **Time-bound** by program cycles |
| **Cross-program** information | **Program-specific** status |

Being in the registry doesn't mean you're receiving benefits - it means your information is available for program staff to assess eligibility and enroll you when appropriate.

## Types of Registries

### Social Registry

A **social registry** (sometimes called a unified registry) serves multiple social protection programs:

- Contains a broad population that might be eligible for various programs
- Data is collected once and shared across programs
- Reduces duplication of data collection efforts
- Enables coordination between different ministries and programs
- Examples: National social registry, poverty database

### Program-Specific Registry

A **program-specific registry** serves a single program:

- Contains only people relevant to that specific program
- May include specialized data fields unique to the program
- Often used when programs have very different target populations
- Examples: School feeding program registry, farmer support registry

OpenSPP supports both approaches and can operate as either type.

## The Two Main Registrant Types

Every record in the registry is called a **registrant**. There are two types:

### Individuals

An individual represents a single person with:

**Basic Information:**
- Full name (given name, family name, other names)
- Date of birth and age
- Gender
- Place of birth

**Identification:**
- ID document types (national ID, voter card, birth certificate, passport, etc.)
- ID numbers
- Photos and biometric data (if collected)

**Contact Information:**
- Phone numbers (mobile, landline)
- Email addresses
- Physical addresses

**Demographics:**
- Marital status
- Education level
- Occupation
- Disability status
- Language preferences

**Location:**
- Administrative area (province, district, village)
- Geographic coordinates (if collected)
- Address details

::::{important}

Only collect the data you actually need for your programs. More data means more privacy risk and more maintenance burden.

::::

### Groups (Households)

A group represents a collection of people - most commonly a **household** - with:

**Group Information:**
- Group name or identifier
- Group type (household, family, cooperative, etc.)
- Number of members (can be stored without listing individual members)
- Registration date

**Membership Details:**
- Individual members (if tracked)
- Member roles (head, principal recipient, alternative recipient, etc.)
- Household composition counts (adults, children, elderly)

**Group-Level Data:**
- Location and address (typically shared by all members)
- Household assets
- Income sources
- Living conditions
- Contact information

Groups can exist in two forms:

1. **With individual members** - Each household member is registered as an individual with a membership link
2. **Without individual members** - Only aggregate counts (e.g., "3 adults, 2 children") are stored

The choice depends on program requirements and privacy considerations.

## Data Model Overview

Here's how the registry data is structured:

```
┌─────────────────────────────────────────────────────────────┐
│                         REGISTRANTS                          │
│  (Base information common to individuals and groups)         │
│                                                              │
│  • Name                                                      │
│  • Registration date                                         │
│  • Location/Administrative area                              │
│  • Contact information                                       │
│  • ID documents                                              │
│  • Tags and categories                                       │
│  • Status (active, inactive, archived)                       │
└───────────────────┬─────────────────────────┬───────────────┘
                    │                         │
        ┌───────────▼─────────┐   ┌──────────▼──────────┐
        │    INDIVIDUALS      │   │       GROUPS        │
        │                     │   │                     │
        │  • Birthdate        │   │  • Group type       │
        │  • Gender           │   │  • Member count     │
        │  • Marital status   │   │  • Household data   │
        │  • Education        │   │                     │
        │  • Disability       │   └──────────┬──────────┘
        └──────────┬──────────┘              │
                   │                         │
                   └────────┬────────────────┘
                            │
                ┌───────────▼────────────┐
                │  GROUP MEMBERSHIP      │
                │                        │
                │  • Individual          │
                │  • Group               │
                │  • Role (head, etc.)   │
                │  • Start/end dates     │
                └────────────────────────┘
```

## Relationships in the Registry

### Group Membership

Individuals can belong to one or more groups with defined roles:

| Role | Description | Constraint |
|------|-------------|------------|
| **Head** | Head of household or group leader | Only one per group |
| **Principal Recipient** | Primary person who receives benefits | Only one per group |
| **Alternative Recipient** | Backup recipient if principal unavailable | Can have multiple |
| **Member** | General member without special role | No limit |

Additional roles can be configured by administrators based on program needs.

**Key concepts:**

- An individual can be head of one household and a regular member of another group
- Membership can have start and end dates to track changes over time
- Roles determine who can receive payments and make decisions for the group

### Registrant Relations

Beyond group membership, you can define specific relationships between registrants:

**Individual to Individual:**
- Parent/Child
- Siblings
- Spouse
- Guardian/Ward
- Caretaker

**Group to Group:**
- Neighboring households
- Extended family groups
- Cooperative members

**Individual to Group:**
- Social worker assigned to household
- Teacher assigned to student group
- Community health worker coverage area

These relationships help with:
- Eligibility rules (e.g., "single parent households")
- Targeting (e.g., "households with elderly members living alone")
- Service coordination (e.g., "assign case worker to vulnerable families")

## Key Registry Fields

While every deployment can customize fields, these are commonly used:

### Individual Fields

| Category | Common Fields |
|----------|---------------|
| **Identity** | National ID, Voter ID, Birth Certificate, Passport, Social Security Number |
| **Demographics** | Age, Gender, Marital Status, Education Level, Literacy |
| **Family** | Relationship to household head, Number of children, Number of dependents |
| **Economic** | Occupation, Employment status, Income level, Assets owned |
| **Health** | Disability status, Chronic illness, Vaccination status, Health card number |
| **Location** | Address, Village/Ward, GPS coordinates, Years at residence |

### Group/Household Fields

| Category | Common Fields |
|----------|---------------|
| **Composition** | Number of members, Adults, Children, Elderly, People with disabilities |
| **Housing** | House ownership, Type of structure, Sanitation, Water source, Electricity |
| **Assets** | Land ownership, Livestock, Vehicles, Appliances |
| **Economic** | Total household income, Income sources, Employment count |
| **Vulnerability** | Female-headed household, Child-headed household, Chronic illness in family |

## How Registry Data is Used

### For Eligibility Determination

Programs use registry data to determine who qualifies:

**Example: Cash Transfer for Poor Households**

```
Registry data used:
- Household monthly income
- Number of children under 5
- Area of residence
- Housing conditions

Eligibility rule:
"Household income below poverty line AND
 has at least one child under 5 AND
 lives in target districts"
```

### For Benefit Calculation

Registry data can determine how much beneficiaries receive:

**Example: School Feeding Program**

```
Registry data used:
- Number of school-age children (6-14 years)
- School enrollment status

Entitlement rule:
"Amount = Number of enrolled children × Daily rate × School days"
```

### For Targeting and Outreach

Programs can identify and reach specific populations:

- "Find all households with pregnant women in District X"
- "List all farmers with less than 2 hectares in drought-affected areas"
- "Identify elderly people living alone without family support"

### For Deduplication

Registry data helps ensure people aren't registered multiple times:

- Compare names and birthdates
- Check ID document numbers
- Use biometric matching (fingerprints, facial recognition)
- Verify household composition

## Registry Data Quality

High-quality registry data is essential for effective programs:

| Quality Aspect | What It Means |
|----------------|---------------|
| **Accuracy** | Data correctly represents reality |
| **Completeness** | Required fields are filled in |
| **Consistency** | Data doesn't contradict itself (e.g., birthdate vs. age) |
| **Timeliness** | Data is updated when changes occur |
| **Uniqueness** | No duplicate registrations |

Common data quality issues:

- Missing birthdates or identification documents
- Outdated addresses after people move
- Duplicate registrations under different names
- Inconsistent spelling of names
- Group membership not updated when people join or leave

## Registry Operations

### Data Collection

Registry data comes from various sources:

| Source | Method | When Used |
|--------|--------|-----------|
| **Registration campaigns** | Field teams visit communities | Initial population registration |
| **On-demand registration** | People come to registration centers | Ongoing enrollment |
| **Mobile data collection** | Tablets/smartphones with forms | Field assessments and updates |
| **Import from other systems** | Data files (CSV, Excel, API) | Integration with existing databases |
| **Program intake** | Application forms | Program-specific registration |

### Data Updates

Registry data needs to stay current:

- **Profile updates** - Name changes, new phone numbers, address changes
- **Life events** - Births, deaths, marriages, migrations
- **Household changes** - Members joining/leaving, change of household head
- **Economic changes** - New employment, change in income, asset acquisition
- **Periodic re-verification** - Scheduled updates to confirm data accuracy

### Data Security and Privacy

Registry data is sensitive and must be protected:

**Security measures:**
- Access controls (who can view/edit which data)
- Encryption of sensitive fields (ID numbers, bank accounts)
- Audit logs (track who accessed or changed data)
- Data classification (mark sensitive vs. public data)

**Privacy principles:**
- Collect only necessary data
- Obtain consent for data use
- Limit data sharing to authorized programs
- Allow people to view and correct their data
- Set data retention periods and delete old data

## Registry vs. Other OpenSPP Features

Understanding what the registry does and doesn't do:

| Feature | Purpose | Relationship to Registry |
|---------|---------|-------------------------|
| **Registry** | Store individual/household profile data | Foundation for everything |
| **Event Data** | Record time-based observations (surveys, visits) | Supplements registry with temporal data |
| **Programs** | Define benefits and eligibility rules | Use registry data to select beneficiaries |
| **Cycles** | Time-bound benefit distribution periods | Operate on subsets of registry (enrolled beneficiaries) |
| **Variables** | Computed values from registry data | Calculate from registry fields (e.g., household size) |
| **Change Requests** | Workflow for updating registry data | Controlled way to modify registry |

**When to use registry fields vs. event data:**

| Use Registry Fields | Use Event Data |
|-------------------|----------------|
| Stable personal information (name, birthdate) | Periodic assessments (income verification) |
| Current status (marital status, address) | Historical records (past visits, surveys) |
| Identification documents | External system data syncs |
| One value per person/household | Multiple observations over time |

## Working with the Registry

### As a User (Gov Employee)

You'll use the registry to:

- Register new individuals and households
- Search for existing registrants
- View and update registrant information
- Verify identity documents
- Print registration cards

See the User Guide for step-by-step instructions on registering individuals, registering groups, and searching registrants.

### As an Implementer (M&E/Technical Staff)

You'll configure:

- Custom fields for program-specific data
- ID document types accepted
- Group types and membership roles
- Relationship types
- Data validation rules
- Import templates

See the Configuration Guide for setting up custom fields, ID types, and group configuration.

### As a Developer

You'll extend the registry with:

- Custom registrant subtypes
- Complex computed fields
- External system integrations
- Custom deduplication logic
- Specialized import/export formats

See the Developer Guide for extending models, custom imports, and external registry integrations.

### As a System Administrator

You'll manage:

- Database performance and indexes
- Data backup and recovery
- Access permissions and security
- Encryption and data protection
- Audit logging and compliance

See the Operations Guide for data encryption, access control, and backup/restore procedures.

## Best Practices

### Data Collection

- **Minimize data collection** - Only collect what you'll actually use for programs
- **Standardize early** - Define consistent field names and formats before collection starts
- **Plan for updates** - Design processes to keep data current
- **Train collectors** - Ensure field teams understand why data accuracy matters

### Data Management

- **Regular deduplication** - Check for duplicate registrations frequently
- **Data quality monitoring** - Track completeness and accuracy metrics
- **Scheduled updates** - Plan periodic re-verification campaigns
- **Version control** - Track changes to registry data over time

### Privacy and Security

- **Need-to-know access** - Limit data visibility based on roles
- **Encrypt sensitive fields** - Protect ID numbers, bank accounts, biometrics
- **Audit access** - Log who views or changes data
- **Data agreements** - Document how data can be shared between agencies

### Integration

- **Use external IDs** - Assign unique IDs for linking to other systems
- **API-first integration** - Prefer API connections over file exports
- **Consent management** - Track which programs people have consented to share data with
- **Change detection** - Sync only changed records to external systems

## Are You Stuck?

**Should I register individuals or households?**

It depends on your programs. If benefits are household-level (e.g., cash transfers to families), register households. If benefits are individual-level (e.g., scholarships, pensions), register individuals. You can register both and link them via membership.

**How do I handle people who belong to multiple households?**

OpenSPP supports multiple group memberships. A person can be head of their immediate household and a member of their extended family group. Each membership can have different roles and dates.

**What's the difference between a registrant and a beneficiary?**

A **registrant** is anyone in the registry database - they might be eligible for programs. A **beneficiary** is someone enrolled in a specific program and receiving benefits. Registrants become beneficiaries through enrollment.

**Can I add custom fields to the registry?**

Yes. Use OpenSPP Studio to add custom fields without writing code. See the Configuration Guide for details.

**How do I import existing data into the registry?**

OpenSPP supports CSV/Excel imports and API integration. See the User Guide for import procedures.

**How often should registry data be updated?**

It depends on your programs. For poverty-targeted programs, annual updates are common. For emergency response, real-time updates may be needed. Balance accuracy needs with data collection costs.

## Next Steps

**Learn more about concepts:**
- {doc}`programs` - How programs use registry data
- {doc}`/config_guide/event_data/overview` - Supplementing registry with event data
- {doc}`/config_guide/eligibility/index` - Using registry data in eligibility rules

**Start using the registry:**
- See the User Guide for step-by-step instructions on registering individuals, registering groups, and searching for registrants.

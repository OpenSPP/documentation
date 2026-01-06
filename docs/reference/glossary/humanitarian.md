---
openspp:
  doc_status: draft
---

# Humanitarian Terms Glossary

This glossary defines humanitarian logistics and disaster response terminology used throughout DRIMS. These terms follow international standards established by the UN Office for the Coordination of Humanitarian Affairs (OCHA) and the Inter-Agency Standing Committee (IASC).

**Audience**: All users - government staff, implementing partners, and system administrators.

## Organizations & Coordination

### OCHA
**UN Office for the Coordination of Humanitarian Affairs**

The UN agency responsible for coordinating international humanitarian response during major disasters. OCHA establishes the cluster system and provides overall coordination frameworks.

**Example**: When a major flood occurs, OCHA activates the cluster system to coordinate all humanitarian partners.

### IASC
**Inter-Agency Standing Committee**

The primary mechanism for inter-agency coordination of humanitarian assistance. IASC brings together UN agencies, NGOs, and other humanitarian partners to set policy and coordinate response.

**Example**: The IASC defines the standard cluster structure that DRIMS implements.

### Cluster
**Sector-Based Coordination Group**

A humanitarian coordination mechanism that organizes response into specific sectors (health, food, shelter, etc.). Each cluster is led by a designated UN agency with expertise in that sector.

**Standard Clusters**:
- Food Security (WFP/FAO)
- Health (WHO)
- Nutrition (UNICEF)
- WASH - Water, Sanitation, Hygiene (UNICEF)
- Shelter (UNHCR/IFRC)
- Protection (UNHCR)
- Education (UNICEF/Save the Children)
- Early Recovery (UNDP)
- Logistics (WFP)
- Emergency Telecommunications (WFP)
- Camp Coordination & Management (UNHCR/IOM)

**Example**: A request for water purification tablets would be tagged with the WASH cluster.

**See also**: {doc}`../../modules/drims/coordination`

### Lead Agency
**Primary Coordinating Organization**

The organization (typically a UN agency or government ministry) that has primary responsibility for coordinating a specific humanitarian cluster or the overall response.

**Example**: UNICEF serves as the lead agency for the Nutrition cluster.

### Co-Lead
**Shared Coordination Organization**

An organization that shares coordination responsibility with the lead agency, particularly when technical expertise or geographic coverage requires multiple coordinators.

**Example**: UNHCR and IFRC serve as co-leads for the Shelter cluster.

### Implementing Partner
**Service Delivery Organization**

An organization (typically NGO or local agency) that delivers services directly to affected populations on the ground.

**Example**: A local NGO distributing food parcels is an implementing partner in the Food Security cluster.

### Funding Partner
**Financial Resource Provider**

An organization (donor government, foundation, or multilateral fund) that provides financial resources to support humanitarian operations.

**Example**: USAID acts as a funding partner providing resources for multiple clusters.

### Technical Partner
**Expertise Provider**

An organization that provides specialized technical expertise, guidance, or standards without directly implementing programs.

**Example**: WHO provides technical guidance on disease surveillance as a technical partner to the Health cluster.

### Coordination Mode

The organizational structure used to manage multi-agency disaster response:

| Mode | Description |
|------|-------------|
| **Lead Agency** | Single agency (usually government) coordinates all partners |
| **Cluster System** | UN-led sector coordination with designated cluster leads |
| **Consortium** | NGO-led coordination among partner organizations |
| **Bilateral** | Direct government-to-government or agency-to-agency cooperation |

**Example**: A small-scale local disaster might use lead agency mode, while a major earthquake activates the full cluster system.

## Reporting & Tracking

### 4W Report
**Who does What, Where, When**

A standard humanitarian coordination tool that provides a comprehensive overview of all relief operations by answering four key questions:
- **Who**: Which organizations are responding
- **What**: What type of assistance (clusters/items)
- **Where**: Geographic areas of operation
- **When**: Time period of activities

**Purpose**: Identify gaps, prevent duplication, and coordinate multi-agency response.

**Example**: The weekly 4W report shows that three NGOs are distributing food in District A, but no one is providing shelter assistance in District B.

**See also**: {doc}`../../modules/drims/4w-reporting`

### Waybill
**Shipment Document**

A printed document that accompanies goods during transport from warehouse to distribution point. Contains dispatch details, item list, quantities, and signature blocks.

**Required Information**:
- Dispatch reference number
- Source warehouse
- Destination location and contact
- Complete item manifest
- Departure and expected arrival dates
- Signature blocks for sender and receiver

**Example**: The truck driver carries the waybill showing 500 blankets and 200 hygiene kits being transported from the central warehouse to the field distribution point.

### POD
**Proof of Delivery**

Documentation confirming that goods were successfully delivered to the intended recipient. Includes recipient signature, delivery date, and any notes about condition or quantity discrepancies.

**Required Fields**:
- Name of receiving person
- Title/position
- Contact phone number
- Digital signature or photo
- Date and time of receipt
- Delivery notes (condition, discrepancies)

**Example**: The field coordinator signs the POD confirming receipt of all items listed on the waybill, noting that 2 boxes arrived slightly damaged.

**See also**: {doc}`../../modules/drims/workflows`

### Beneficiary
**Person Receiving Assistance**

An individual or household receiving humanitarian assistance during a disaster response. DRIMS tracks beneficiary counts to measure reach and impact.

**Example**: A distribution serving 500 families represents approximately 2,500 individual beneficiaries (using average household size).

### Affected Population
**People Impacted by Disaster**

The total number of people directly or indirectly impacted by a disaster event within a specific geographic area. Used to justify request quantities and measure coverage.

**Example**: A request for emergency shelter kits cites an affected population of 10,000 people in the flood-impacted district.

## Inventory & Distribution

### Donation
**Contributed Goods or Services**

Items or services provided to support disaster response, typically from donors (UN agencies, NGOs, private sector, governments, or individuals).

**Donation Types by Source**:
- UN Agency
- International NGO
- Local NGO
- Private Sector/Corporate
- Individual Donor
- Government (bilateral)

**Example**: A pharmaceutical company donates 10,000 medical kits to support the health cluster response.

### Usage Restriction
**Limitations on Donated Items**

Conditions placed by donors on how, where, or when donated items can be used.

**Common Restrictions**:
- Geographic (specific district/province only)
- Demographic (women/children only, specific age groups)
- Sectoral (health use only, education only)
- Temporal (must be distributed within 30 days)

**Example**: A donor specifies that distributed blankets must be used only in the mountain districts affected by winter storms.

### Prepositioned Stock
**Strategically Located Emergency Supplies**

Relief items stored in warehouses before a disaster occurs, positioned for rapid deployment when needed.

**Example**: The national disaster management agency maintains prepositioned stocks of tarpaulins and water containers in regional warehouses.

### Pipeline
**Goods in Transit or Procurement**

Items that have been committed (ordered, shipped, or in procurement) but have not yet arrived at the destination warehouse.

**Example**: The pipeline report shows 5,000 hygiene kits currently being shipped from the regional hub, expected to arrive in 3 days.

### Stock Health
**Inventory Condition Status**

Assessment of inventory quality and usability, tracking condition codes assigned during inspection.

**Condition Categories**:
- Good/Serviceable
- Damaged/Impaired
- Expired
- Quarantined (pending inspection)
- Rejected/Disposed

**Example**: After inspection, 95% of the donated rice was marked as good stock health, but 5% showed water damage.

## Response Categories & Prioritization

### Priority Level

Classification system for requests indicating urgency and required response time:

| Priority | Response Time | Description |
|----------|---------------|-------------|
| **Critical** | Immediate (hours) | Life-threatening situations requiring emergency response |
| **High** | 24 hours | Urgent needs impacting health and safety |
| **Medium** | 48-72 hours | Standard requests for essential supplies |
| **Low** | As resources allow | Non-urgent needs that can be scheduled |

**Example**: A request for emergency medical supplies for a cholera outbreak is marked as Critical priority.

### Life-Threatening
**Emergency Flag**

A special designation for requests involving immediate risk to human life. Life-threatening requests bypass normal approval thresholds and trigger emergency escalation procedures.

**Criteria**:
- Imminent risk of death or serious injury
- Critical medical needs
- Lack of safe water or shelter in extreme conditions
- Protection emergencies

**Example**: A request for emergency water supplies when wells are contaminated and disease outbreak is imminent is flagged as life-threatening.

### Approval State
**Authorization Status**

Current position in the request approval workflow:

| State | Description |
|-------|-------------|
| **Draft** | Being prepared, not yet submitted |
| **Pending** | Submitted and awaiting approval decision |
| **Approved** | Authorized for fulfillment |
| **Rejected** | Denied with documented reason |
| **Revision** | Returned to requester for changes |

**Example**: After the logistics coordinator submits the request, it moves from Draft to Pending approval state.

### Fulfillment State
**Delivery Progress Status**

Tracks progress of approved requests through the distribution process:

| State | Description |
|-------|-------------|
| **Pending** | Approved but not yet allocated to warehouse |
| **Allocated** | Source warehouse assigned |
| **Dispatched** | Items shipped from warehouse |
| **In Transit** | En route to destination |
| **Delivered** | Proof of delivery confirmed |
| **Partial** | Some items delivered, others pending |

**Example**: The request moves to Dispatched state when the truck leaves the warehouse with the goods.

## Related Documentation

- {doc}`../../modules/drims/index` - DRIMS module overview
- {doc}`../../modules/drims/coordination` - Multi-agency coordination features
- {doc}`../../modules/drims/4w-reporting` - Generating 4W reports
- {doc}`../../modules/drims/workflows` - Donation, request, and dispatch workflows
- {doc}`./technical` - Technical terms glossary

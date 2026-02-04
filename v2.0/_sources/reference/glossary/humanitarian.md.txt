---
openspp:
  doc_status: draft
  products: [core]
---

# Humanitarian Terms Glossary

This glossary defines humanitarian logistics and disaster response terminology used throughout DRIMS. These terms follow international standards established by the UN Office for the Coordination of Humanitarian Affairs (OCHA) and the Inter-Agency Standing Committee (IASC).

**Audience**: All users - government staff, implementing partners, and system administrators.

## Organizations & Coordination

```{glossary}
OCHA
    **UN Office for the Coordination of Humanitarian Affairs** - The UN agency responsible for coordinating international humanitarian response during major disasters. OCHA establishes the cluster system and provides overall coordination frameworks.

IASC
    **Inter-Agency Standing Committee** - The primary mechanism for inter-agency coordination of humanitarian assistance. IASC brings together UN agencies, NGOs, and other humanitarian partners to set policy and coordinate response.

Cluster
    A humanitarian coordination mechanism that organizes response into specific sectors (health, food, shelter, etc.). Each cluster is led by a designated UN agency with expertise in that sector. Standard clusters include: Food Security (WFP/FAO), Health (WHO), Nutrition (UNICEF), WASH (UNICEF), Shelter (UNHCR/IFRC), Protection (UNHCR), Education (UNICEF/Save the Children), Early Recovery (UNDP), Logistics (WFP), Emergency Telecommunications (WFP), and Camp Coordination & Management (UNHCR/IOM).

Lead Agency
    The organization (typically a UN agency or government ministry) that has primary responsibility for coordinating a specific humanitarian cluster or the overall response.

Co-Lead
    An organization that shares coordination responsibility with the {term}`Lead Agency`, particularly when technical expertise or geographic coverage requires multiple coordinators.

Implementing Partner
    An organization (typically NGO or local agency) that delivers services directly to affected populations on the ground.

Funding Partner
    An organization (donor government, foundation, or multilateral fund) that provides financial resources to support humanitarian operations.

Technical Partner
    An organization that provides specialized technical expertise, guidance, or standards without directly implementing programs.

Coordination Mode
    The organizational structure used to manage multi-agency disaster response. Options include: **Lead Agency** (single agency coordinates all partners), **Cluster System** (UN-led sector coordination), **Consortium** (NGO-led coordination), or **Bilateral** (direct government-to-government cooperation).
```

## Reporting & Tracking

```{glossary}
4W Report
    **Who does What, Where, When** - A standard humanitarian coordination tool that provides a comprehensive overview of all relief operations by answering four key questions: Who (which organizations), What (type of assistance), Where (geographic areas), and When (time period). Used to identify gaps, prevent duplication, and coordinate multi-agency response.

Waybill
    A printed document that accompanies goods during transport from warehouse to distribution point. Contains dispatch reference, source warehouse, destination, item manifest, dates, and signature blocks for sender and receiver.

POD
Proof of Delivery
    Documentation confirming that goods were successfully delivered to the intended recipient. Includes recipient name, title, contact, signature or photo, date/time, and delivery notes about condition or discrepancies.

Beneficiary
    An individual or household receiving humanitarian assistance during a disaster response. DRIMS tracks beneficiary counts to measure reach and impact.

Affected Population
    The total number of people directly or indirectly impacted by a disaster event within a specific geographic area. Used to justify request quantities and measure coverage.
```

## Inventory & Distribution

```{glossary}
Donation
    Items or services provided to support disaster response, typically from donors (UN agencies, NGOs, private sector, governments, or individuals). Donation types include: UN Agency, International NGO, Local NGO, Private Sector/Corporate, Individual Donor, and Government (bilateral).

Usage Restriction
    Conditions placed by donors on how, where, or when donated items can be used. Common restrictions include geographic (specific district only), demographic (women/children only), sectoral (health use only), or temporal (must be distributed within 30 days).

Prepositioned Stock
    Relief items stored in warehouses before a disaster occurs, positioned for rapid deployment when needed.

Pipeline
    Items that have been committed (ordered, shipped, or in procurement) but have not yet arrived at the destination warehouse.

Stock Health
    Assessment of inventory quality and usability. Categories include: Good/Serviceable, Damaged/Impaired, Expired, Quarantined (pending inspection), and Rejected/Disposed.
```

## Response Categories & Prioritization

```{glossary}
Priority Level
    Classification system for requests indicating urgency and required response time. Levels are: **Critical** (immediate/hours, life-threatening), **High** (24 hours, urgent health/safety), **Medium** (48-72 hours, standard essential supplies), **Low** (as resources allow, non-urgent).

Life-Threatening
    A special designation for requests involving immediate risk to human life. Life-threatening requests bypass normal approval thresholds and trigger emergency escalation procedures. Criteria include imminent risk of death, critical medical needs, lack of safe water/shelter in extreme conditions, or protection emergencies.

Approval State
    Current position in the request approval workflow: **Draft** (being prepared), **Pending** (awaiting approval), **Approved** (authorized for fulfillment), **Rejected** (denied with reason), or **Revision** (returned for changes).

Fulfillment State
    Tracks progress of approved requests through distribution: **Pending** (not yet allocated), **Allocated** (warehouse assigned), **Dispatched** (shipped), **In Transit** (en route), **Delivered** ({term}`POD` confirmed), or **Partial** (some items delivered).
```

## Using These Terms

You can reference glossary terms from anywhere in the documentation using the `:term:` role:

- `:term:`Cluster`` renders as: {term}`Cluster`
- `:term:`4W Report`` renders as: {term}`4W Report`
- `:term:`POD`` renders as: {term}`POD`

## Related Documentation

- {doc}`/user_guide/drims/index` - DRIMS user guide
- {doc}`/config_guide/drims/index` - DRIMS configuration guide

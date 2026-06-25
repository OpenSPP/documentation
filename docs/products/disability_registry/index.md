---
openspp:
  doc_status: draft
myst:
  html_meta:
    "title": "OpenSPP Disability Registry"
    "description": "OpenSPP Disability Registry product for standardized disability assessment and assistive device management in social protection programs"
    "keywords": "OpenSPP, disability registry, Washington Group, CFM, assessment, assistive devices, social protection"
---

# OpenSPP Disability Registry

*A digital system for standardized disability assessment and inclusive program targeting*

The **OpenSPP Disability Registry** provides structured disability assessment and tracking for social protection programs. It implements internationally recognized standards — the Washington Group Short Set (WG-SS) for adults and the UNICEF Child Functioning Module (CFM) for children — enabling programs to identify persons with disabilities, manage assistive device needs, and apply disability criteria in eligibility targeting.

## Key features

**Standardized disability assessment –** Conduct structured assessments using the Washington Group Short Set (WG-SS) for adults and the UNICEF Child Functioning Module (CFM) for children aged 2–17. Assessment type is automatically selected based on the registrant's age at the time of assessment.

---

**Six-domain functioning measurement –** Capture difficulty levels across six core domains: seeing, hearing, walking, remembering, self-care, and communicating. Disability status is automatically computed when any domain reaches "a lot of difficulty" or "cannot do at all," in line with the WG standard.

---

**Age-appropriate child assessments –** Apply the CFM 5–17 instrument for school-age children and CFM 2–4 for young children, with proxy response tracking for cases where a parent or caregiver answers on the child's behalf.

---

**Impairment classification –** Record impairment type, cause, and severity using DCI-aligned vocabulary codes (ICF-based). Multiple impairment types per assessment are supported.

---

**Assistive device management –** Track assistive device needs, requests, and provisions for each registrant. A built-in status workflow (needed → requested → provided) and an unmet-need flag make it easy to identify gaps and prioritize support.

---

**Review scheduling –** Assign a review category to each assessment — improvement expected (12 months), improvement possible (3 years), or improvement not expected (6 years) — and automatically compute the next review date.

---

**Approval workflows –** Route assessments through configurable multi-tier approval before the result becomes the registrant's active disability status, ensuring data quality and accountability.

---

**Eligibility targeting with CEL –** Use built-in CEL functions to apply disability criteria in program eligibility rules, including household-level checks such as whether any member has a disability or how many members need reassessment.

## Who is it for?

**Government agencies** implementing inclusive social protection policies

**Social protection programs** targeting persons with disabilities or households with disabled members

**Health and welfare ministries** conducting population-level disability assessments

**Program implementers** needing disability-aware eligibility and entitlement rules

## Next steps

The OpenSPP Disability Registry is an open-source product, built and supported by the OpenSPP community.

- {doc}`Try the demo </get_started/try_our_products/try_disability_registry/index>` — Explore pre-loaded assessments, impairment records, and device management without any setup
- Read more about {doc}`installing OpenSPP Disability Registry </get_started/modules/disability_installation>`

```{toctree}
:maxdepth: 1
:caption: Contents
:hidden:

modules_included
user_guides
config_guides
demo_module
```

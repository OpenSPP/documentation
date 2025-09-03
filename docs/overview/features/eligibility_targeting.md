---
myst:
  html_meta:
    "title": "Configurable Eligibility and Targeting"
    "description": "OpenSPP flexible rules engine for precise beneficiary identification and enrollment using multiple targeting methodologies"
    "keywords": "OpenSPP, eligibility, targeting, beneficiary selection, proxy means test, social protection"
---

# Configurable eligibility and targeting

OpenSPP's {term}`eligibility` and targeting system provides a powerful rules engine that enables programs to precisely identify and enroll their intended {term}`beneficiaries` through flexible criteria ranging from simple categorical filters to sophisticated poverty {term}`assessment of needs and conditions` algorithms.

## The targeting challenge

Accurate beneficiary targeting forms the foundation of effective {term}`social protection` delivery. Programs must balance multiple objectives: reaching the most vulnerable populations, ensuring fair and transparent selection processes, operating within budget constraints, and adapting to local contexts and needs. Poor targeting leads to inclusion errors where {term}`benefits` go to those who don't need them, or exclusion errors where eligible {term}`households <household>` are left out. Both types of errors undermine program effectiveness and public trust.

OpenSPP's configurable approach recognizes that different programs require different targeting methodologies. A disaster response program might need geographic targeting to quickly reach all households in affected areas. A poverty alleviation program might employ {term}`proxy means test` to identify the poorest households based on observable characteristics. A categorical program might target specific demographic groups like elderly persons or households with disabled members. The platform supports all these approaches and allows them to be combined, giving program designers the tools to implement evidence-based targeting strategies that align with program objectives and local implementation capacity. The system's transparency in how eligibility decisions are made also supports accountability and helps build trust with communities and beneficiaries.

## Targeting methods

* **Manual selection and approval**: Enable program staff to directly select beneficiaries with multi-level approval workflows for oversight and accountability
* **Tag-based targeting**: Automatically enroll {term}`registrants <registrant>` marked with specific tags such as "vulnerable household," "displaced family", or custom program-specific categories
* **Geographic targeting**: Define eligible areas at any administrative level from national to village, with support for complex boundary definitions
* **Demographic and categorical filters**: Target based on age groups, gender, disability status, household composition, or any combination of demographic criteria
* **SQL-based custom rules**: Create sophisticated eligibility rules using SQL queries for maximum flexibility in defining complex targeting logic
* **Proxy Means Testing (PMT)**: Calculate poverty scores using weighted indicators with configurable formulas adapted to local contexts and data availability
* **Exclusion filters**: Define criteria to explicitly exclude certain populations, such as government employees or high-income earners, from program enrollment
* **Dynamic re-assessment**: Continuously evaluate eligibility as registrant data changes, with automatic enrollment and graduation based on updated criteria

## Technical implementation

The eligibility and targeting system is implemented through specialized modules:

* **[spp_manual_eligibility](/reference/modules/spp_manual_eligibility.md)**: Manual beneficiary selection with approval workflows and audit trails
* **[spp_eligibility_tags](/reference/modules/spp_eligibility_tags.md)**: Tag-based automatic enrollment using registrant classifications
* **[spp_eligibility_sql](/reference/modules/spp_eligibility_sql.md)**: SQL-based eligibility rules for complex, custom targeting logic
* **[g2p_proxy_means_test](/reference/modules/g2p_proxy_means_test.md)**: Core PMT framework for poverty assessment calculations
* **[spp_pmt](/reference/modules/spp_pmt.md)**: OpenSPP-specific PMT extensions with additional indicators and formulas
* **[spp_exclusion_filter](/reference/modules/spp_exclusion_filter.md)**: Exclusion list management to prevent ineligible enrollment
* **[spp_area](/reference/modules/spp_area.md)**: Geographic area management for location-based targeting
* **[spp_registrant_tag](/reference/modules/spp_registrant_tag.md)**: Tag management system for categorizing and filtering registrants
---
openspp:
  doc_status: draft
myst:
  html_meta:
    "title": "OpenSPP Disability Registry Installation Guide"
    "description": "Step-by-step guide for installing the OpenSPP Disability Registry module"
    "keywords": "OpenSPP, disability registry, installation, Odoo, WG-SS, CFM, Washington Group"
---

# Disability Registry installation

**OpenSPP Disability Registry / spp_disability_registry**

The {doc}`OpenSPP Disability Registry <../../products/disability_registry/index>` provides structured disability assessment and tracking for social protection programs. It implements internationally recognized standards — the Washington Group Short Set (WG-SS) for adults and the UNICEF Child Functioning Module (CFM) for children — enabling programs to identify persons with disabilities, manage assistive device needs, and apply disability criteria in eligibility targeting.

**What's included:**
- Standardized disability assessment using WG-SS (adults) and CFM (children aged 2–17)
- Six-domain functioning measurement with automatic disability status computation
- Impairment classification using DCI-aligned ICF-based vocabulary codes
- Assistive device management with status workflow (needed → requested → provided)
- Approval workflows for multi-tier assessment review
- CEL functions for disability-aware eligibility targeting

**Installation steps:**

1. Navigate to the **Apps** menu.
2. Search for `spp_disability_registry` or "OpenSPP Disability Registry". If the module does not appear, clear the default "Apps" filter from the search bar.

![Searching for the Disability Registry module in Apps](/_images/en-us/get_started/module_installation/disability_installation/01-disability-apps-search.png)

3. Click the **Activate** button to install the module. This will also install all required dependencies.

![Disability Registry module activation screen](/_images/en-us/get_started/module_installation/disability_installation/02-disability-activate.png)

Once installed, disability assessment forms will be available on individual registrant records.

![Disability Registry module successfully installed](/_images/en-us/get_started/module_installation/disability_installation/03-disability-installed.png)

## Next steps

Now that you have installed the OpenSPP Disability Registry:

- {doc}`../../products/disability_registry/user_guides` - Start conducting disability assessments
- {doc}`../../products/disability_registry/config_guides` - Configure assessment workflows and approval tiers

---
openspp:
  doc_status: draft
  products: [disability_registry]
---

# Install Disability Registry demo data

Install the module that generates the sample data needed to explore OpenSPP Disability Registry features.

**For:** Evaluators, learners, and trainers

Before trying out the Disability Registry use cases, you'll need sample data to work with. This guide walks you through installing and running the demo data generator that creates registrants, assessments, assistive devices, and programs.

## Before you start

- OpenSPP should be installed and running (see {doc}`../../installation/index`)
- You need administrator access to OpenSPP

## Install the Disability Registry Demo module

Installing an Odoo module follows a standard procedure:

1. Navigate to the **Apps** menu.

2. Clear the default "Apps" filter from the search bar and search for **OpenSPP Disability Registry Demo**.

3. Click **Activate** on the module card to begin installation.

## Load demo data

### 1. Log in as administrator

Log in using administrator credentials (default: admin/admin).

### 2. Open Settings and navigate to demo data

1. Click **Settings** in the left sidebar.

2. In the Settings top menu, click **Demo Data** > **Load Disability Registry Demo**.

   ![Screenshot: Settings with Demo Data menu](/_images/en-us/get_started/try_disability_registry/install_disability_registry_demo_data/01-settings-disability-demo-data-menu.png)

3. The **Load Disability Registry Demo** wizard opens. Click **Load Demo Data**.

   ![Screenshot: Load Disability Registry Demo wizard](/_images/en-us/get_started/try_disability_registry/install_disability_registry_demo_data/02-load-disability-registry-demo-wizard.png)

```{note}
Demo data generation takes 2–5 minutes. The wizard redirects to the Registry page when complete.
```

## What's included

### Story registrants

The demo seeds ten registrant stories designed to showcase specific features. See {doc}`stories` for full details on each person's assessment, impairments, and device records.

| # | Registrant | Age group | Location | Instrument | State | Has disability |
|---|-----------|-----------|----------|-----------|-------|---------------|
| 1 | Maria Santos | Adult (39) | Quezon City, NCR | WG-SS | Approved | Yes |
| 2 | Juan Cruz Jr | Child (9) | Cebu City, Cebu | CFM 5–17 | Pending | Yes |
| 3 | Ana Reyes | Adult (34) | Davao City, Davao del Sur | WG-SS | Draft | No |
| 4 | Roberto Dela Cruz | Adult (55) | Batangas City, Batangas | WG-SS | Approved | Yes |
| 5 | Liza Villanueva | Toddler (2) | Cagayan de Oro City, Misamis Oriental | CFM 2–4 | Pending | Yes |
| 6 | Danilo Mangudadatu | Adult (42) | Cotabato City, Maguindanao del Norte | WG-SS | Approved | Yes |
| 7 | Elena Garcia | Elderly (72) | Iloilo City, Iloilo | WG-SS | Approved | Yes |
| 8 | Grace Bautista | Adolescent (14) | Angeles City, Pampanga | CFM 5–17 | Approved | Yes |
| 9 | Michael Torres | Young adult (19) | Pasig City, Metro Manila | WG-SS | Pending | Yes |
| 10 | Sofia Pangandaman | Adult (27) | Marawi City, Lanao del Sur | WG-SS | Approved | Yes |

### Assessments

| Registrant | Instrument | Domains above threshold | Review category | State |
|-----------|-----------|------------------------|----------------|-------|
| Maria Santos | WG-SS | 3 (seeing, walking, self-care) | MINE (72 mo) | Approved |
| Juan Cruz Jr | CFM 5–17 | 3 (hearing, comm. inside, comm. outside) | MIP (36 mo) | Pending |
| Ana Reyes | WG-SS | 0 | — | Draft |
| Roberto Dela Cruz | WG-SS | 2 (remembering, communicating) | MIE (12 mo) | Approved |
| Liza Villanueva | CFM 2–4 | 1 (vision) | MIP (36 mo) | Pending |
| Danilo Mangudadatu | WG-SS | 2 (walking, remembering) | MINE (72 mo) | Approved |
| Elena Garcia | WG-SS | 3 (seeing, hearing, walking) | MINE (72 mo) | Approved |
| Grace Bautista | CFM 5–17 | 4 (learning, concentrating, accepting change, anxiety) | MIP (36 mo) | Approved |
| Michael Torres | WG-SS | 2 (self-care, communicating) | MIE (12 mo) | Pending |
| Sofia Pangandaman | WG-SS | 1 (remembering) | MIP (36 mo) | Approved |

### Assistive devices

| Registrant | Device | Status |
|-----------|--------|--------|
| Maria Santos | Wheelchair | Provided |
| Maria Santos | Magnifier | Needed |
| Juan Cruz Jr | Hearing Aid | Needed |
| Roberto Dela Cruz | Cognitive Aid | Needed |
| Liza Villanueva | Corrective Glasses | Provided |
| Danilo Mangudadatu | Walker/Rollator | Provided |
| Danilo Mangudadatu | AAC Device | Requested |
| Elena Garcia | Walking Cane | Provided |
| Elena Garcia | Corrective Glasses | Provided |
| Elena Garcia | Hearing Aid | Needed |
| Michael Torres | Orthotic Device | Needed |

### Programs

The demo creates five disability-aware programs. Each uses CEL eligibility rules based on the built-in disability registry functions.

| Program | CEL eligibility condition | Target stories |
|---------|--------------------------|----------------|
| PWD Cash Assistance Program | `has_disability(registrant) == True` | 1, 2, 4, 5, 6, 7, 8, 9, 10 |
| Severe Disability Supplement | `is_severe_disability(registrant) == True` | 1, 6 |
| Assistive Device Support Grant | `has_disability(registrant) and registrant.has_unmet_device_need` | 1, 2, 4, 7, 9 |
| Child Disability Benefit | `has_disability(registrant) and registrant.age < 18` | 2, 5, 8 |
| Annual Reassessment Service | `needs_reassessment(registrant) == True` | 4, 9 (review due dates already past) |

### Demo users

| Login | Password | Role(s) |
|-------|----------|---------|
| `admin` | `admin` | System Administrator |
| `assessor` | `demo` | Disability Assessor |
| `validator` | `demo` | Disability Validator |
| `viewer` | `demo` | Disability Viewer |

### Volume registrants

In addition to the ten story registrants, the generator creates approximately 200 volume registrants from deterministic blueprints. These populate list views, search filters, and reports with realistic data covering all regions, instruments, and assessment states.

## Are you stuck?

**Can't find Settings menu?**
Make sure you are logged in as an administrator. Regular users do not have access to system settings.

**Demo Data menu not visible?**
The Disability Registry Demo module may not be installed. Check with your system administrator that `spp_disability_registry_demo` is installed.

**Loading takes too long?**
Demo data generation may take 2–5 minutes. The page will update when complete.

**No Disability menu visible after loading?**
Your user account may not have disability registry roles assigned. Log in as `admin` to access all menus.

## Next steps

Now that you have sample data, you are ready to explore:

- {doc}`stories` — Read the registrant stories to understand each demo record's situation
- {doc}`demo_scenarios` — Walk through guided scenarios covering key workflows

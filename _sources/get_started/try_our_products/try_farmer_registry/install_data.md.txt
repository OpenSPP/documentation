---
openspp:
  doc_status: draft
  products: [farmer_registry]
---

# Install Farmer Registry demo data

Install the module that contains the sample data needed to explore OpenSPP Farmer Registry features.

**For:** Evaluators, learners, and trainers

Before trying out the Farmer Registry use cases, you'll need sample data to work with. This guide walks you through installing and loading demo data that includes sample farms, farmers, cooperatives, and agricultural programs.

## Before you start

- OpenSPP should be installed and running (see {doc}`../../installation/index`)
- You need administrator access to OpenSPP

## Install Farmer Registry demo module

Installing an Odoo module follows a standard procedure:

1. Navigate to the **Apps** menu.

2. Clear the default "Apps" filter from the search bar and search for the module **OpenSPP Farmer Registry Demo**.

3. Click the **Activate** button on the module's card to begin the installation.

## Load demo data

### 1: Log in as administrator

Log in to OpenSPP using administrator credentials (default: admin/admin).

### 2: Open Settings and navigate to demo data

1. Click **Settings** in the left sidebar.

2. In the Settings top menu, click **Demo Data** > **Load Farmer Registry Demo**.

  ![Screenshot: Settings with Demo Data menu](/_images/en-us/get_started/try_farmer_registry/install_farmer_registry_demo_data/01-settings-mis-demo-data-menu.png)

3. The Load Farmer Registry Demo wizard opens in a dialog. Click the button **Load Demo Data** to add the demo data to the system.

  ![Screenshot: Wizard opening](/_images/en-us/get_started/try_farmer_registry/install_farmer_registry_demo_data/02-load-farmer-registry-demo-wizard.png)

```{note}
Demo data generation takes 2–5 minutes depending on your system. The wizard will redirect you to the Registry page when complete.
```

## What's included

### Sample programs

| Program             | Description                                                     |
| ------------------- | --------------------------------------------------------------- |
| Input Subsidy       | Agricultural input support for smallholder farmers              |
| Livestock Support   | Per-head benefit for farmers with livestock                     |
| Aquaculture Support | Support for fishpond and aquaculture operators                  |
| Equipment Grant     | Capital grant for experienced smallholders                      |
| Climate Resilience  | Vulnerability-based support for farms with idle/fallow land     |

### Demo farms

The demo includes 8 complete farm stories:

- Farm households with full registration data (land size, crop activities, livestock)
- Program enrollments with eligibility determinations and payment histories
- Change requests at various workflow stages
- Land parcel records with GIS coordinates
- Irrigation infrastructure linked to farms (Mangudadatu Farm)

Two cooperatives demonstrate the group-of-groups data model.

### Demo users

| Login                | Password | Role(s)                         |
| -------------------- | -------- | ------------------------------- |
| `admin`              | `admin`  | System Administrator            |
| `manager`            | `demo`   | Farm Manager + CR Requestor     |
| `officer`            | `demo`   | Farm User + CR Requestor        |
| `supervisor`         | `demo`   | Farm Manager                    |
| `viewer`             | `demo`   | Farm User (read-only)           |
| `program_manager`    | `demo`   | Program Manager + Farm User     |
| `cycle_approver`     | `demo`   | Cycle Approver                  |
| `cr_local_validator` | `demo`   | CR Local Validator (Tier-1)     |
| `cr_hq_validator`    | `demo`   | CR HQ Validator (Tier-2)        |

## Are you stuck?

**Can't find Settings menu?**
Make sure you're logged in as an administrator. Regular users don't have access to system settings.

**Demo Data menu not visible?**
The Farmer Registry Demo module may not be installed. Check with your system administrator that `spp_farmer_registry_demo` is installed.

**Loading takes too long?**
Large demo data sets may take 2–5 minutes to generate. The page will update when complete.

**Error during loading?**
Check the browser console for errors. Try refreshing the page and running the wizard again.

## Next steps

Now that you have sample data, you're ready to start exploring:

- {doc}`stories` — Read the farm stories to understand each demo farm's situation
- {doc}`demo_scenarios` — Walk through guided scenarios covering key workflows

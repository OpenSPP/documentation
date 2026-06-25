---
openspp:
  doc_status: draft
  products: [disability_registry]
---

# Install Disability Registry demo data

Install the module that contains the sample data needed to explore OpenSPP Disability Registry features.

**For:** Evaluators, learners, and trainers

Before trying out the Disability Registry use cases, you'll need sample data to work with. This guide walks you through installing and loading demo data that includes sample registrants, disability assessments, and assistive device records.

## Before you start

- OpenSPP should be installed and running (see {doc}`../../installation/index`)
- You need administrator access to OpenSPP

## Install Disability Registry demo module

Installing an Odoo module follows a standard procedure:

1. Navigate to the **Apps** menu.

2. Clear the default "Apps" filter from the search bar and search for the module **OpenSPP Disability Registry Demo**.

3. Click the **Activate** button on the module's card to begin the installation.

## Load demo data

### 1: Log in as administrator

Log in to OpenSPP using administrator credentials (default: admin/admin).

### 2: Open Settings and navigate to demo data

1. Click **Settings** in the left sidebar.

2. In the Settings top menu, click **Demo Data** > **Load Disability Registry Demo**.

  ![Screenshot: Settings with Demo Data menu](/_images/en-us/get_started/try_disability_registry/install_disability_registry_demo_data/01-settings-disability-demo-data-menu.png)

3. The Load Disability Registry Demo wizard opens in a dialog. Click the button **Load Demo Data** to add the demo data to the system.

  ![Screenshot: Wizard opening](/_images/en-us/get_started/try_disability_registry/install_disability_registry_demo_data/02-load-disability-registry-demo-wizard.png)

```{note}
Demo data generation takes 2–5 minutes depending on your system. The wizard will redirect you to the Registry page when complete.
```

## What's included

### Sample registrants

The demo includes 3 registrant stories covering key assessment outcomes:

| Registrant | Age group | Assessment state | Has disability |
|------------|-----------|-----------------|----------------|
| Maria Santos | Adult | Approved | Yes |
| Juan Cruz Jr | Child | Pending | Yes |
| Ana Reyes | Adult | Draft | No |

### Demo assessments

| Registrant | Instrument | Domains above threshold | State |
|------------|-----------|------------------------|-------|
| Maria Santos | WG-SS | 3 (seeing, walking, self-care) | Approved |
| Juan Cruz Jr | WG-SS | 2 (hearing, communicating) | Pending |
| Ana Reyes | WG-SS | 0 | Draft |

### Assistive devices

| Registrant | Device | Status |
|------------|--------|--------|
| Maria Santos | Wheelchair | Provided |
| Maria Santos | Magnifier | Requested |
| Juan Cruz Jr | Hearing Aid | Needed |

### Demo users

| Login      | Password | Role(s)                  |
|------------|----------|--------------------------|
| `admin`    | `admin`  | System Administrator     |
| `assessor` | `demo`   | Disability Assessor      |
| `validator`| `demo`   | Disability Validator     |
| `viewer`   | `demo`   | Disability Viewer        |

## Are you stuck?

**Can't find Settings menu?**
Make sure you're logged in as an administrator. Regular users don't have access to system settings.

**Demo Data menu not visible?**
The Disability Registry Demo module may not be installed. Check with your system administrator that `spp_disability_registry_demo` is installed.

**Loading takes too long?**
Demo data generation may take 2–5 minutes. The page will update when complete.

**Error during loading?**
Check the browser console for errors. Try refreshing the page and running the wizard again.

**No Disability menu visible?**
Your user account may not have disability registry roles assigned. Log in as `admin` to access all menus.

## Next steps

Now that you have sample data, you're ready to start exploring:

- {doc}`stories` — Read the registrant stories to understand each demo record's situation
- {doc}`demo_scenarios` — Walk through guided scenarios covering key workflows

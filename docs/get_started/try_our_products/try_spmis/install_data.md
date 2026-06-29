---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Install SP-MIS demo data

Install the module that contains the sample data needed to explore OpenSPP SP-MIS features.

**For:** Evaluators, learners, and trainers

Before trying out the SP-MIS use cases, you'll need sample data to work with. This guide walks you through installing and loading demo data that includes sample households, individuals, and programs.

## Before you start

- OpenSPP should be installed and running (see {doc}`../../installation/index`)
- You need administrator access to OpenSPP

## Install SP-MIS demo module

Installing an Odoo module follows a standard procedure:

1.  Navigate to the **Apps** menu.

2. Clear the default "Apps" filter from the search bar and Search for the module **OpenSPP MIS Demo V2**

3. Click the **Activate** button on the module's card to begin the installation.

## Load demo data

### 1: Log in as administrator

Log in to OpenSPP using administrator credentials (default: admin/admin).

### 2: Open Settings and navigate to demo data

1. Click **Settings** in the left sidebar.

2. In the Settings top menu, click **Demo Data** > **Load MIS Demo**.

  ![Screenshot: Settings with Demo Data menu](/_images/en-us/get_started/try_openspp_sp_mis/install_sp_mis_demo_data/01-settings-farmer-demo-data-menu.png)

3. The Load MIS Demo wizard opens in a dialog. Click the button **Load Demo Data** to add the demo data to the system.

  ![Screenshot: Wizard opening](/_images/en-us/get_started/try_openspp_sp_mis/install_sp_mis_demo_data/02-load-mis-demo-wizard.png)

```{note}
Demo data generation takes 2-5 minutes depending on your system. The wizard will redirect you to the Programs page when complete.
```

## What's included

### Sample programs

| Program                  | Description                                      |
| ------------------------ | ------------------------------------------------ |
| Food Assistance          | Food voucher program                             |
| Cash Transfer Program    | General cash transfer program                    |
| Emergency Relief Fund    | One-time emergency assistance                    |
| Elderly Social Pension   | Social pension for elderly citizens              |
| Conditional Child Grant  | Monthly grant for households with children under 2 |
| Universal Child Grant    | Monthly cash transfer for families with children |

### Demo personas

The demo includes 8 complete registrant stories:

- Individuals and households with full registration data
- Program enrollments with eligibility determinations
- Payment history and entitlement records
- Change requests at various workflow stages

### Demo users

| User                     | Role                    | Password |
| ------------------------ | ----------------------- | -------- |
| sppadmin                 | OpenSPP Admin           | demo     |
| demo_manager             | Demo Manager             | demo     |
| demo_officer             | Demo Officer             | demo     |
| demo_supervisor          | Demo Supervisor          | demo     |
| demo_viewer              | Demo Viewer              | demo     |
| demo_global_registrar    | Demo Global Registrar   | demo     |
| demo_local_registrar     | Demo Local Registrar    | demo     |
| demo_cr_hq_validator     | Demo CR HQ Validator    | demo     |
| demo_cr_local_validator | Demo CR Local Validator | demo     |
| demo_program_manager     | Demo Program Manager    | demo     |
| demo_program_validator   | Demo Program Validator  | demo     |
| demo_cycle_approver      | Demo Cycle Approver     | demo     |

## Are you stuck?

**Can't find Settings menu?**
Make sure you're logged in as an administrator. Regular users don't have access to system settings.

**Demo Data menu not visible?**
The MIS Demo module may not be installed. Check with your system administrator that `spp_mis_demo_v2` is installed.

**Loading takes too long?**
Large demo data sets may take 1-2 minutes to generate. The page will update when complete.

**Error during loading?**
Check the browser console for errors. Try refreshing the page and running the wizard again.

## Next Steps

Now that you have sample data, you're ready to start exploring:

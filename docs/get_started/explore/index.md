---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Explore OpenSPP

Load sample data to explore OpenSPP features before starting tutorials.

**For:** Evaluators, learners, and trainers

Before diving into the tutorials, you'll need sample data to work with. This guide walks you through loading demo data that includes sample households, individuals, and programs.

## What You'll Get

After loading the MIS demo data, you'll have:

- **6 social protection programs** - Child Grant, Pension, Emergency Relief, Cash Transfer, Disability Support, Food Assistance
- **8 demo personas** - Sample registrants with complete stories and payment history
- **~500 enrollments** - Beneficiaries enrolled across programs
- **Program cycles** - With generated entitlements
- **Logic Packs** - Pre-configured eligibility rules
- **Change requests** - At various workflow stages

## Before You Start

- OpenSPP should be installed and running (see {doc}`../installation/index`)
- You need administrator access to OpenSPP

## Load Demo Data

### Step 1: Log in as Administrator

Log in to OpenSPP using administrator credentials (default: admin/admin).

![Screenshot: Dashboard after login](/_images/en-us/get_started/explore/1.png)

### Step 2: Open Settings

Click **Settings** in the left sidebar.

![Screenshot: Settings page](/_images/en-us/get_started/explore/2.png)

### Step 3: Navigate to Demo Data

In the Settings top menu, click **Demo Data** > **Load MIS Demo**.

![Screenshot: Settings with Demo Data menu](/_images/en-us/get_started/explore/3.png)

### Step 4: Open the Wizard

The Load MIS Demo wizard opens in a dialog.

![Screenshot: Wizard opening](/_images/en-us/get_started/explore/4.png)

### Step 5: Generate Demo Data

Review the configuration options and click **Generate Demo Data** to start.

![Screenshot: Generate MIS Demo Data wizard](/_images/en-us/get_started/explore/5.png)

```{note}
Demo data generation takes 2-5 minutes depending on your system. The wizard will redirect you to the Programs page when complete.
```

## What's Included

### Sample Programs

| Program            | Description                                      |
| ------------------ | ------------------------------------------------ |
| Child Grant        | Monthly cash transfer for families with children |
| Pension            | Social pension for elderly citizens              |
| Emergency Relief   | One-time emergency assistance                    |
| Cash Transfer      | General cash transfer program                    |
| Disability Support | Assistance for persons with disabilities         |
| Food Assistance    | Food voucher program                             |

### Demo Personas

The demo includes 8 complete registrant stories:

- Individuals and households with full registration data
- Program enrollments with eligibility determinations
- Payment history and entitlement records
- Change requests at various workflow stages

### Demo Users

| User         | Role             | Password |
| ------------ | ---------------- | -------- |
| demo_admin   | Administrator    | demo     |
| demo_manager | Program Manager  | demo     |
| demo_officer | Registry Officer | demo     |

## Are You Stuck?

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

- {doc}`../first_household/index` - Register your first household
- {doc}`../first_program/index` - Create your first social protection program

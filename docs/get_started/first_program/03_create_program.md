---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Step 3: Create Your First Social Protection Program

This tutorial is for **users** who want to learn how to set up a social protection program in OpenSPP.

## What You'll Do

Create a "Cash Transfer for Vulnerable Families" program that will provide monthly cash assistance to eligible families. You'll configure the basic program settings including the program name, target beneficiaries, and currency.

## Before You Start

- You completed [Step 2: Import Beneficiaries](02_import_beneficiaries.md)
- Your registry has family and individual data
- You need **System Administrator** or **Program Manager** access
- Allow 5-10 minutes to complete this step

## The Scenario

You're creating a **Cash Transfer for Vulnerable Families** program with these goals:
- **Target**: Low-income families with young children
- **Benefit**: Monthly cash transfer
- **Currency**: Philippine Peso (PHP)
- **Distribution**: Monthly recurring payments

## Steps

### 1. Access the Programs Module

Click the **four-square icon** in the top-left corner to open the main menu. Then click **Programs**.

![Screenshot: Main menu with four-square icon and Programs option highlighted](/_images/en-us/get_started/first_program/03_create_program/01-main-menu-with-programs-option-highlighted.png)

### 2. Create a New Program

Click the **Create** button in the top-left corner of the Programs list.

![Screenshot: Programs list view with Create button highlighted in top-left](/_images/en-us/get_started/first_program/03_create_program/02-programs-list-with-create-button-highlighted.png)

### 3. Enter Basic Program Information

You'll see the program creation form. Fill in the following basic information:

**Program Name**: Cash Transfer for Vulnerable Families

**Target Type**: Select **Group** from the dropdown. This means the program will evaluate families (groups) for eligibility, not individual people.

![Screenshot: Program creation form showing Program Name field filled with "Cash Transfer for Vulnerable Families" and Target Type set to "Group"](/_images/en-us/get_started/first_program/03_create_program/03-program-form-with-name-and-target-type-filled.png)

### 4. Set the Currency

Scroll down to the **Currency** field and select **PHP - Philippine Peso** from the dropdown.

![Screenshot: Currency field showing PHP - Philippine Peso selected](/_images/en-us/get_started/first_program/03_create_program/04-currency-field-with-php-selected.png)

### 5. Review the Configuration Tabs

Notice there are several tabs at the top of the form:
- **Configuration**: Basic program settings (where you are now)
- **Eligibility**: Where you'll set rules for who qualifies
- **Cycle Manager**: Controls how often benefits are distributed
- **Entitlement Manager**: Defines what benefits are given

For now, we'll just create the basic program. You'll configure these in the next steps.

![Screenshot: Program form showing the four tabs: Configuration, Eligibility, Cycle Manager, Entitlement Manager](/_images/en-us/get_started/first_program/03_create_program/05-form-showing-all-configuration-tabs.png)

### 6. Leave Other Settings as Default

Keep the default settings for now:
- **Auto-import Eligible Beneficiaries**: Unchecked (you'll manually control enrollment)
- **Notification Settings**: Empty (no notifications yet)
- **Journal**: Empty (accounting setup comes later)

These can be configured later as you become more familiar with OpenSPP.

![Screenshot: Lower portion of Configuration tab showing default settings](/_images/en-us/get_started/first_program/03_create_program/06-default-settings-section.png)

### 7. Save the Program

Click the **Save** button in the top-left corner to create your program.

![Screenshot: Save button in top-left corner of program form](/_images/en-us/get_started/first_program/03_create_program/07-save-button-highlighted.png)

You should see a success notification: "Program created successfully."

![Screenshot: Green success notification banner showing "Program created successfully"](/_images/en-us/get_started/first_program/03_create_program/08-success-notification.png)

### 8. Verify the Program Was Created

After saving, you'll stay on the program page. Notice:
- The program name appears at the top
- The status shows **Draft** (not active yet)
- The record has an ID number

![Screenshot: Program page showing "Cash Transfer for Vulnerable Families" at top with Draft status badge](/_images/en-us/get_started/first_program/03_create_program/09-saved-program-with-draft-status.png)

### 9. Check the Programs List

Click **Programs** in the breadcrumb navigation or return to the Programs menu. You should see your new program in the list.

![Screenshot: Programs list showing "Cash Transfer for Vulnerable Families" as a new program with Draft status](/_images/en-us/get_started/first_program/03_create_program/10-programs-list-showing-new-program.png)

## What You Accomplished

You've successfully created your first social protection program with:

- **Program Name**: Cash Transfer for Vulnerable Families
- **Target Type**: Group (evaluating families, not individuals)
- **Currency**: PHP (Philippine Peso)
- **Status**: Draft (not active yet)

The program is created but not yet configured. In the next steps, you'll set up:
- Who is eligible (eligibility criteria)
- How often benefits are distributed (cycle manager)
- What benefits people receive (entitlement manager)

## Are You Stuck?

**Can't find the Programs menu?**
Make sure you're logged in with **System Administrator** or **Program Manager** role. Only users with these roles can create programs.

**Create button is grayed out?**
You may not have the right permissions. Contact your system administrator.

**Not sure whether to select Group or Individual as Target Type?**
Use **Group** when you want to evaluate entire families/households for eligibility (like this cash transfer program). Use **Individual** when benefits are for specific people regardless of their family (like an elderly pension program).

**Don't see PHP in the currency list?**
Your OpenSPP installation may not have Philippine Peso enabled. You can use any currency available in the list - the process is the same. Common alternatives: USD (US Dollar), EUR (Euro), or your local currency.

**The Save button doesn't work?**
Make sure you've filled in the required fields (marked with red text if missing):
- Program Name
- Target Type

## Next Step

Now that your program exists, you need to define who is eligible to receive benefits. Continue to [Step 4: Configure Eligibility Rules](04_configure_eligibility.md).

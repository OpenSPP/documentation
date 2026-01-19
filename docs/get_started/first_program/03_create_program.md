---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Step 3: Create your first social protection program

This tutorial is for **users** who want to learn how to set up a social protection program in OpenSPP.

## What you'll do

Create a "Cash transfer for vulnerable families" program that will provide monthly cash assistance to eligible families. You'll configure the basic program settings including the program name, target beneficiaries, currency, eligibility, amount and distribution schedule.

## Before you start

- You completed [Step 2: Import beneficiaries](02_import_beneficiaries.md)
- Your registry has family and individual data
- Sample data loaded for exploration (see {doc}`../explore/index`)
- Allow 10-15 minutes to complete this step

## The scenario

You're creating a **Cash transfer for vulnerable families** program with these goals:
- **Target**: Low-income families with young children
- **Benefit**: Monthly cash transfer of XXXXADD AMOUNTXXXX
- **Currency**: Philippine Peso (PHP)
- **Distribution**: Monthly recurring payments

Your program targets vulnerable families. To identify them, you'll use two criteria:
1. **Income Test**: Family earns less than 10,000 PHP per month
2. **Child Test**: Family has at least one child under 5 years old

## Steps

### 1. Sign in as a Program Manager

In the installed sample data, use the following information:

**User name:** demo_manager

**Password:** demo

### 2. Access the programs module

Click the **four-square icon** in the top-left corner to open the main menu. Then click **Programs**.

![Screenshot: Main menu with four-square icon and Programs option highlighted](/_images/en-us/get_started/first_program/03_create_program/01-programs-list.png)

### 3. Create a new program

Click the **Create** button in the top-left corner of the Programs list.

![Screenshot: Programs list view with Create button highlighted in top-left](/_images/en-us/get_started/first_program/03_create_program/02-create-program-button.png)

### 4. Enter basic program information

You'll see the program creation form. Fill in the following basic information:

**Program Name**: Cash transfer for vulnerable families

**Target Type**: Select **Group** from the dropdown. This means the program will evaluate families (groups) for eligibility, not individual people.

**Benefit Type**: Make sure that **Cash** is selected.

![Screenshot: Program creation form showing Program Name field filled with "Cash Transfer for Vulnerable Families" and Target Type set to "Group"](/_images/en-us/get_started/first_program/03_create_program/cle5_3.png)

### 5. Set the currency

Scroll down to the **Currency** field and select **PHP - Philippine Peso** from the dropdown.

![Screenshot: Currency field showing PHP - Philippine Peso selected](/_images/en-us/get_started/first_program/03_create_program/cle5_7.png)

### 6. Configure the program

Click "Next: Configure Program" to proceed with the configurations. Notice that there are several tabs at the top of the form:
- **Who Qualifies?** (where you are now): Define the criteria that determine who can participate in this program
- **Entitlements**: Configure what beneficiaries will receive from this program
- **Schedule**: Set up how often benefits will be distributed

![Screenshot: Program form showing the four tabs: Who Qualifies?, hat Do They Receive?, Distribution Schedule, Ongoing Compliance (Optional)](/_images/en-us/get_started/first_program/03_create_program/cle5_1.png)

### 7. Configure eligibility

Your program targets vulnerable families. To identify them, you'll use two criteria:
- **Income Test**: Family earns less than 10,000 PHP per month
- **Child Test**: Family has at least one child under 5 years old

TODO: **ADD DESCRIPTION XXXXX**

TODO: **CREATE NEW SCREENSHOT**

![Screenshot: Create program button at the bottom of of program form](/_images/en-us/get_started/first_program/03_create_program/cle5_2.png)

### 8. Configure amount to be distributed

Click on tab **Entitlements**

You want to distribute the fixed amount **300 PHP** to each family that fulfills the eligibility.

Click **Add a line**.

![Screenshot: Add a line button at the bottom of of program form](/_images/en-us/get_started/first_program/03_create_program/cle5_8.png)

In the popup window displayed, select **Fixed Amount** in the dropdown for **Amount Formula**. Enter **300** in the field **Base Amount**. Click **Save & Close**.

![Screenshot: Pop up window to configure distributed amount](/_images/en-us/get_started/first_program/03_create_program/cle5_9.png)

### 9. Configure distribution schedule

Click on tab **Schedule**.

In this scenario we want the distribution to be performed once every month, therefore select the option **Monthly**.

![Entitlement configuration dialog showing Distribution Schedule](/_images/en-us/get_started/first_program/03_create_program/cle5_5.png)

### 10. Complete creation of program

Click the **Create Program** button at the bottom to create your program.

After saving, you'll be taken to the program page. Notice:
- The program name appears at the top
- The status shows **Active**

![Screenshot: Program page showing "Cash Transfer for Vulnerable Families" at top](/_images/en-us/get_started/first_program/03_create_program/cle5_6.png)

### 11. Verify the created program

Click the tab **Configuration**. Notice:
- The section **Who Qualifies** displays the eligibility criteria previously entered.
- The section **What Do They Receive?** displays Cash. To verify the amount, click the cogwheel on the line where it says **Cash**.
- The section **Program Schedule** displays **Every 1 monthly**.
- The section **Payment Method** displays XXX.

TODO: **ADD INFO ABOVE**

![Screenshot: Program page showing "Cash Transfer for Vulnerable Families" and the tab "Configuration"](/_images/en-us/get_started/first_program/03_create_program/cle5_10.png)


### 12. Check the programs list

Click **Programs** in the breadcrumb navigation or return to the Programs menu. You should see your new program in the list.

![Screenshot: Programs list showing "Cash Transfer for Vulnerable Families" as a new program with Active status](/_images/en-us/get_started/first_program/03_create_program/cle5_6.png)

## What you accomplished

You've successfully created your first social protection program with:

- **Program Name**: Cash Transfer for Vulnerable Families
- **Target Type**: Group (evaluating families, not individuals)
- **Currency**: PHP (Philippine Peso)
- **Status**: Active

You've successfully configured eligibility criteria for your program:

- **Income Rule**: Families earning less than 10,000 PHP per month qualify
- **Children Rule**: Families with at least one child under 5 qualify
- **Combined Logic**: Families must meet BOTH rules to be eligible

Based on the sample data you imported:
- **Garcia Family**: Not eligible (income 15,000 - too high ❌)
- **Santos Family**: Eligible (income 8,000 ✓, has child born 2021 ✓)
- **Cruz Family**: Not eligible (income 12,000 - too high ❌)
- **Reyes Family**: Eligible (income 6,000 ✓, has child born 2023 ✓)
- **Ramos Family**: Not eligible (income 18,000 - too high ❌)

**Expected eligible families**: Santos Family and Reyes Family (2 out of 5)

## Are you stuck?

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

## Next step

Now that your program exists, you need to define who is eligible to receive benefits. Continue to [Step 4: Configure Eligibility Rules](04_configure_eligibility.md).

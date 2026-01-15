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
- You need **System Administrator** or **Program Manager** access
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

### 1. Access the programs module

Click the **four-square icon** in the top-left corner to open the main menu. Then click **Programs**.

![Screenshot: Main menu with four-square icon and Programs option highlighted](/_images/en-us/get_started/first_program/03_create_program/01-programs-list.png)

### 2. Create a new program

Click the **Create** button in the top-left corner of the Programs list.

![Screenshot: Programs list view with Create button highlighted in top-left](/_images/en-us/get_started/first_program/03_create_program/02-create-program-button.png)

### 3. Enter basic program information

You'll see the program creation form. Fill in the following basic information:

**Program Name**: Cash transfer for vulnerable families

**Target Type**: Select **Group** from the dropdown. This means the program will evaluate families (groups) for eligibility, not individual people.

![Screenshot: Program creation form showing Program Name field filled with "Cash Transfer for Vulnerable Families" and Target Type set to "Group"](/_images/en-us/get_started/first_program/03_create_program/cle5_3.png)

### 4. Set the currency

Scroll down to the **Currency** field and select **PHP - Philippine Peso** from the dropdown.

TODO: **NEW SCREENSHOT NEEDED**

![Screenshot: Currency field showing PHP - Philippine Peso selected](/_images/en-us/get_started/first_program/03_create_program/04-currency.png)

### 5. Configure the program

Click "Next: Configure Program" to proceed with the configurations. Notice that there are several tabs at the top of the form:
- **Who Qualifies?** (where you are now): Define the criteria that determine who can participate in this program
- **What Do They Receive?**: Configure what beneficiaries will receive from this program
- **Distribution Schedule**: Set up how often benefits will be distributed
- **Ongoing Compliance (Optional)**: Define criteria that beneficiaries must continue to meet to remain eligible. This setting is optional and can be left unselected if it should not be used.

TODO: **CREATE NEW SCREENSHOT**

![Screenshot: Program form showing the four tabs: Who Qualifies?, hat Do They Receive?, Distribution Schedule, Ongoing Compliance (Optional)](/_images/en-us/get_started/first_program/03_create_program/cle5_1.png)

### 6. Configure eligibility

Your program targets vulnerable families. To identify them, you'll use two criteria:
- **Income Test**: Family earns less than 10,000 PHP per month
- **Child Test**: Family has at least one child under 5 years old

TODO: **ADD DESCRIPTION XXXXX**

TODO: **CREATE NEW SCREENSHOT**

![Screenshot: Create program button at the bottom of of program form](/_images/en-us/get_started/first_program/03_create_program/cle5_2.png)

### 7. Configure amount to be distributed

Click on tab **What Do They Receive?**

Note that the option **Basic Cash** is selected. This option is used for distributions where a fixed amount should be distributed and no complex calculations are needed.

In the right section, under **BENEFIT AMOUNTS**, the field **Amount per Cycle** shows how much each beneficiary receives. Enter the value **$150.00**.

TODO: **NEW SCREENSHOT NEEDED WITH CORRECT CURRENCY AND AMOUNT**

![Entitlement configuration dialog showing Amount per Cycle](/_images/en-us/get_started/first_program/03_create_program/cle5_4.png)

You can also configure:
- **Amount per Person (in group)** - Additional amount per family member
- **Transfer fees** - Percentage or fixed fees
- **Approval settings** - Validation groups

### 8. Configure distribution schedule

Click on tab **Distribution Schedule**.

In this scenario we want the distribution to be performed once every month, therefore select the option **Monthly**.

![Entitlement configuration dialog showing Distribution Schedule](/_images/en-us/get_started/first_program/03_create_program/cle5_5.png)

You can also configure:
- **Cycle Duration** - How many days, weeks or months each cycle lasts
- **Monthly Options** - Configure what day of the month the distribution should occur
- **Distribution Type** - Select if the distribution should only occur once
- **Cycle Approval** - Select the validation group for the cycle

### 9. Complete creation of program

Click the **Create Program** button at the bottom to create your program.

After saving, you'll be taken to the program page. Notice:
- The program name appears at the top
- The status shows **Active**

![Screenshot: Program page showing "Cash Transfer for Vulnerable Families" at top](/_images/en-us/get_started/first_program/03_create_program/cle5_6.png)

### 10. Verify the created program

Click the tab **Configuration**. Notice:
- The section **Who Qualifies** displays the eligibility criteria previously entered.
- The section **What Do They Receive?** displays XXX.
- The section **Program Schedule** displays **Every 1 monthly**.
- The section **Payment Method** displays XXX.

TODO: **ADD INFO ABOVE AND SCREENSHOT**

![Screenshot: Program page showing "Cash Transfer for Vulnerable Families" and the tab "Configuration"](/_images/en-us/get_started/first_program/03_create_program/X.png)


### 11. Check the programs list

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

---
openspp:
  doc_status: draft
  products: [registry, programs]
---

# Step 3: Create your first social protection program

This tutorial is for **users** who want to learn how to set up a social protection program in OpenSPP.

## What you'll do

Create a "Cash transfer for vulnerable families" program that will provide monthly cash assistance to eligible families. You'll configure the basic program settings including the program name, target beneficiaries, and currency.

## Before you start

- You completed [Step 2: Import beneficiaries](02_import_beneficiaries.md)
- Your registry has family and individual data
- You need **System Administrator** or **Program Manager** access
- Allow 5-10 minutes to complete this step

## The scenario

You're creating a **Cash transfer for vulnerable families** program with these goals:
- **Target**: Low-income families with young children
- **Benefit**: Monthly cash transfer
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

![Screenshot: Program creation form showing Program Name field filled with "Cash Transfer for Vulnerable Families" and Target Type set to "Group"](/_images/en-us/get_started/first_program/03_create_program/03-program-name.png)

### 4. Set the currency

Scroll down to the **Currency** field and select **PHP - Philippine Peso** from the dropdown.

![Screenshot: Currency field showing PHP - Philippine Peso selected](/_images/en-us/get_started/first_program/03_create_program/04-currency.png)

### 5. Configure the program

Click "Next: Configure Program" to proceed with the configurations. Notice that there are several tabs at the top of the form:
- **Who Qualifies?** (where you are now): Define the criteria that determine who can participate in this program
- **What Do They Receive?**: Configure what beneficiaries will receive from this program
- **Distribution Schedule**: Set up how often benefits will be distributed
- **Ongoing Compliance (Optional)**: Define criteria that beneficiaries must continue to meet to remain eligible. This setting is optional and can be left unselected if it should not be used.

![Screenshot: Program form showing the four tabs: Who Qualifies?, hat Do They Receive?, Distribution Schedule, Ongoing Compliance (Optional)](/_images/en-us/get_started/first_program/03_create_program/cle5_1.png)

### 6. Configure eligibility

Your program targets vulnerable families. To identify them, you'll use two criteria:
- **Income Test**: Family earns less than 10,000 PHP per month
- **Child Test**: Family has at least one child under 5 years old

Click the **Create Program** button at the bottom to create your program.

![Screenshot: Create program button at the bottom of of program form](/_images/en-us/get_started/first_program/03_create_program/cle5_2.png)

You should see a success notification: "Program created successfully."

![Screenshot: Green success notification banner showing "Program created successfully"](/_images/en-us/get_started/first_program/03_create_program/08-program-create-button.png)

### 8. Verify the Program Was Created

After saving, you'll stay on the program page. Notice:
- The program name appears at the top
- The status shows **Draft** (not active yet)
- The record has an ID number

![Screenshot: Program page showing "Cash Transfer for Vulnerable Families" at top with Draft status badge](/_images/en-us/get_started/first_program/03_create_program/09-program-saved.png)

### 9. Check the Programs List

Click **Programs** in the breadcrumb navigation or return to the Programs menu. You should see your new program in the list.

![Screenshot: Programs list showing "Cash Transfer for Vulnerable Families" as a new program with Draft status](/_images/en-us/get_started/first_program/03_create_program/10-programs-list-result.png)

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

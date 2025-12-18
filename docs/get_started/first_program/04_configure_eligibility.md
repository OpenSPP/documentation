---
openspp:
  doc_status: draft
---

# Step 4: Configure Basic Eligibility Rules

This tutorial is for **users** who want to learn how to set up rules that determine which families qualify for program benefits.

## What You'll Do

Set up simple eligibility rules for your Cash Transfer for Vulnerable Families program. You'll create rules that select families with:
- Household income below 10,000 PHP per month
- At least one child under 5 years old

## Before You Start

- You completed [Step 3: Create Program](03_create_program.md)
- Your program "Cash Transfer for Vulnerable Families" exists
- You need **Program Manager** or **Administrator** access
- Allow 5-10 minutes to complete this step

## The Scenario

Your program targets vulnerable families. To identify them, you'll use two criteria:
1. **Income Test**: Family earns less than 10,000 PHP per month
2. **Child Test**: Family has at least one child under 5 years old

Families must meet **both** conditions to be eligible.

## Steps

### 1. Open Your Program

Go to **Programs** from the main menu and click on **Cash Transfer for Vulnerable Families** to open it.

![Screenshot: Programs list with "Cash Transfer for Vulnerable Families" highlighted](/_images/en-us/get_started/first_program/04_configure_eligibility/1.png)

### 2. Go to the Eligibility Tab

Click the **Eligibility** tab at the top of the program form.

![Screenshot: Program form with Eligibility tab highlighted](/_images/en-us/get_started/first_program/04_configure_eligibility/2.png)

### 3. Choose Default Eligibility Manager

In the **Eligibility Manager** field, select **Default** from the dropdown. This is the standard way to set up eligibility rules.

![Screenshot: Eligibility Manager dropdown with "Default" selected](/_images/en-us/get_started/first_program/04_configure_eligibility/3.png)

### 4. Set Filter Mode to "All"

Below the Eligibility Manager field, you'll see **Filter Mode**. Select **All** from the dropdown.

This means families must meet **all** the rules you create (income AND children). If you selected "Any," families would only need to meet one rule.

![Screenshot: Filter Mode dropdown showing "All" selected](/_images/en-us/get_started/first_program/04_configure_eligibility/4.png)

### 5. Add the First Rule (Income Test)

Click **Add a line** in the eligibility rules section.

![Screenshot: Eligibility rules section with "Add a line" button highlighted](/_images/en-us/get_started/first_program/04_configure_eligibility/5.png)

A new rule line appears. Configure it as follows:

| Field | Value |
|-------|-------|
| Field | Household Income |
| Operator | is less than |
| Value | 10000 |

This rule selects families with household income less than 10,000 PHP.

![Screenshot: First rule showing "Household Income is less than 10000"](/_images/en-us/get_started/first_program/04_configure_eligibility/6.png)

### 6. Add the Second Rule (Children Under 5)

Click **Add a line** again to add a second rule.

![Screenshot: Add a line button with first rule already visible above](/_images/en-us/get_started/first_program/04_configure_eligibility/7.png)

Configure the second rule:

| Field | Value |
|-------|-------|
| Field | Number of Children Under 5 |
| Operator | is greater than or equal to |
| Value | 1 |

This rule selects families with at least one child under 5 years old.

![Screenshot: Second rule showing "Number of Children Under 5 is greater than or equal to 1"](/_images/en-us/get_started/first_program/04_configure_eligibility/8.png)

### 7. Review Your Eligibility Rules

You should now see both rules:

**Rule 1**: Household Income is less than 10000
**Rule 2**: Number of Children Under 5 is greater than or equal to 1
**Filter Mode**: All (must meet both rules)

![Screenshot: Complete eligibility configuration showing both rules with "All" filter mode](/_images/en-us/get_started/first_program/04_configure_eligibility/9.png)

### 8. Save the Program

Click **Save** in the top-left corner to save your eligibility configuration.

![Screenshot: Save button in top-left corner](/_images/en-us/get_started/first_program/04_configure_eligibility/10.png)

You should see a success notification: "Program updated successfully."

![Screenshot: Success notification showing "Program updated successfully"](/_images/en-us/get_started/first_program/04_configure_eligibility/11.png)

### 9. Verify Eligibility is Configured

After saving, review the Eligibility tab to confirm your rules are saved correctly. You should see:
- Eligibility Manager: Default
- Filter Mode: All
- Two rules configured

![Screenshot: Saved eligibility configuration showing all settings](/_images/en-us/get_started/first_program/04_configure_eligibility/12.png)

## What You Accomplished

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

## Are You Stuck?

**Can't find "Household Income" in the field list?**
The available fields depend on what data you collected during registration. If you don't see Household Income, you may need to use a different field or add custom fields in the registry configuration.

**Don't see "Number of Children Under 5" field?**
This is a computed field that counts children based on their birthdates. If it's not available, you may need to enable it in the registry settings or your OpenSPP version may use a different field name like "Children Count" with an age filter.

**Not sure whether to use "All" or "Any"?**
- **All**: Stricter - families must meet every single rule (AND logic)
- **Any**: More inclusive - families need to meet at least one rule (OR logic)

For this program, we want families that are BOTH low-income AND have young children, so we use "All."

**Rules not saving?**
Make sure each rule has:
- A field selected
- An operator selected
- A value entered

Empty rules will prevent saving.

**Want to test if a specific family is eligible?**
You'll be able to test this in the next step when you run a program cycle. The system will evaluate all families against these rules.

## Next Step

Now that your eligibility rules are set, you're ready to run your first program cycle to identify eligible families. Continue to [Step 5: Run a Program Cycle](05_run_cycle.md).

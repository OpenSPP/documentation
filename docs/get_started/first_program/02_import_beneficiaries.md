---
openspp:
  doc_status: draft
---

# Step 2: Import Sample Beneficiary Data

This tutorial is for **users** who want to learn how to add beneficiary records to their OpenSPP registry.

## What You'll Do

Import sample data for families and individuals into your registry. This data will be used to demonstrate the Cash Transfer for Vulnerable Families program in the following steps.

## Before You Start

- You completed [Step 1: Set Up Registry](01_setup_registry.md)
- You need **Registry Officer** or **Administrator** access
- Download the sample data files (links provided below)
- Allow 5-10 minutes to complete this step

## The Scenario

Your Cash Transfer for Vulnerable Families program needs beneficiary data. You'll import:
- **5 families** (groups/households)
- **15 individuals** (family members)

The data includes families with various income levels and children of different ages, so you can test eligibility criteria later.

## Sample Data Files

For this tutorial, we'll use sample CSV files. Create two files on your computer:

**families.csv** - Contains family/household records:
```csv
name,area,address,phone,household_income
Garcia Family,Metro Manila,123 Rizal St Manila,+63-2-1234-5678,15000
Santos Family,Metro Manila,456 Quezon Ave Manila,+63-2-2345-6789,8000
Cruz Family,Cebu,789 Osmena Blvd Cebu,+63-32-3456-7890,12000
Reyes Family,Metro Manila,321 Taft Ave Manila,+63-2-4567-8901,6000
Ramos Family,Davao,654 Bonifacio St Davao,+63-82-5678-9012,18000
```

**individuals.csv** - Contains individual/person records:
```csv
family_name,given_name,birthdate,gender,is_group_head
Garcia,Juan,1985-03-15,Male,Yes
Garcia,Maria,1987-06-20,Female,No
Garcia,Sofia,2020-08-10,Female,No
Garcia,Miguel,2022-11-05,Male,No
Santos,Pedro,1990-01-25,Male,Yes
Santos,Ana,1992-04-18,Female,No
Santos,Carlos,2021-02-14,Male,No
Cruz,Roberto,1988-07-30,Male,Yes
Cruz,Elena,1989-12-08,Female,No
Reyes,Luis,1995-05-12,Male,Yes
Reyes,Carmen,1996-09-22,Female,No
Reyes,Isabella,2023-01-30,Female,No
Ramos,Diego,1982-11-17,Male,Yes
Ramos,Rosa,1984-02-28,Female,No
Ramos,Mateo,2015-06-19,Male,No
```

Save these files to your computer as `families.csv` and `individuals.csv`.

## Steps

### 1. Open the Registry Search Portal

Click **Registry → Search** from the main menu to open the Registry Search Portal.

![Screenshot: Main menu with Registry > Search option highlighted](/_images/en-us/get_started/first_program/02_import_beneficiaries/1.png)

### 2. Access the Import Tool

From the Registry Search Portal, click the **three-dot menu** in the top right, then select **Import Records**.

![Screenshot: Registry Search Portal with three-dot menu expanded showing Import Records option](/_images/en-us/get_started/first_program/02_import_beneficiaries/2.png)

### 3. Import Families First

In the Import dialog, select:
- **Record Type**: Group
- **Import File**: Click **Choose File** and select your `families.csv` file

![Screenshot: Import dialog showing Record Type dropdown set to "Group" and Choose File button](/_images/en-us/get_started/first_program/02_import_beneficiaries/3.png)

### 4. Map the Family Fields

The system will show you a preview of your CSV data. Map the columns to OpenSPP fields:

| CSV Column | Maps To OpenSPP Field |
|------------|----------------------|
| name | Group Name |
| area | Administrative Area |
| address | Address |
| phone | Phone Number |
| household_income | Household Income |

Click **Next** after mapping the fields.

![Screenshot: Field mapping screen showing CSV columns on the left matched to OpenSPP fields on the right](/_images/en-us/get_started/first_program/02_import_beneficiaries/4.png)

### 5. Validate and Import Families

The system will validate your data. Review any warnings or errors. If everything looks correct, click **Import** to add the families to the registry.

![Screenshot: Validation screen showing "5 records ready to import" with Import button](/_images/en-us/get_started/first_program/02_import_beneficiaries/5.png)

You should see a success message: "5 groups imported successfully."

![Screenshot: Success notification showing "5 groups imported successfully"](/_images/en-us/get_started/first_program/02_import_beneficiaries/6.png)

### 6. Verify the Families Were Imported

In the Registry Search Portal, search for "Garcia" to verify the families were imported. You should see the Garcia Family in the results.

![Screenshot: Registry Search Portal with "Garcia" in search box and Garcia Family in results](/_images/en-us/get_started/first_program/02_import_beneficiaries/7.png)

### 7. Import Individuals

Now repeat the import process for individuals. Click the **three-dot menu → Import Records** again.

This time, select:
- **Record Type**: Individual
- **Import File**: Select your `individuals.csv` file

![Screenshot: Import dialog showing Record Type set to "Individual" and individuals.csv selected](/_images/en-us/get_started/first_program/02_import_beneficiaries/8.png)

### 8. Map the Individual Fields

Map the CSV columns to OpenSPP fields:

| CSV Column | Maps To OpenSPP Field |
|------------|----------------------|
| family_name | Family Name (Surname) |
| given_name | Given Name (First Name) |
| birthdate | Date of Birth |
| gender | Gender |
| is_group_head | Is Group Head |

Click **Next** after mapping.

![Screenshot: Field mapping screen for individuals showing all columns mapped](/_images/en-us/get_started/first_program/02_import_beneficiaries/9.png)

### 9. Link Individuals to Families

On the next screen, you'll need to specify how individuals should be linked to their family groups:

- **Link Method**: Match by Group Name
- **Group Name Field**: Use the family name from the individual record

This tells OpenSPP to add each individual to the group with a matching name.

![Screenshot: Linking configuration showing "Match by Group Name" selected](/_images/en-us/get_started/first_program/02_import_beneficiaries/10.png)

### 10. Import the Individuals

Review the validation results. You should see "15 records ready to import, 15 will be linked to existing groups."

Click **Import** to add the individuals and link them to their families.

![Screenshot: Validation showing "15 records ready to import" with family linking information](/_images/en-us/get_started/first_program/02_import_beneficiaries/11.png)

You should see: "15 individuals imported successfully."

![Screenshot: Success notification showing "15 individuals imported successfully"](/_images/en-us/get_started/first_program/02_import_beneficiaries/12.png)

### 11. Verify the Complete Data

Search for "Garcia Family" and open the record. You should see all four family members listed in the **Group Members** section.

![Screenshot: Garcia Family record showing Juan, Maria, Sofia, and Miguel as members with their ages](/_images/en-us/get_started/first_program/02_import_beneficiaries/13.png)

## What You Accomplished

You've successfully imported beneficiary data into your registry:

- **5 family groups** with contact information and household income
- **15 individuals** with names, birthdates, and gender
- **Family relationships** linking individuals to their households

Your registry now has realistic sample data to use for creating and testing your first program.

## Are You Stuck?

**Import button is grayed out?**
Check that all required fields are mapped. Fields marked with an asterisk (*) must be mapped to proceed.

**Getting "No matching group found" errors?**
Make sure you imported the families first before importing individuals. The individuals import looks for existing groups to link to.

**CSV file not uploading?**
Check that your file is saved as UTF-8 encoding and uses commas as separators. Excel sometimes saves with different encodings.

**Birthdates showing as numbers or errors?**
Make sure birthdates in your CSV are in YYYY-MM-DD format (e.g., 2020-08-10).

**Can't find the Import Records option?**
You may not have the right permissions. You need **Registry Officer** or **Administrator** role to import data.

## Next Step

Now that you have beneficiary data in your registry, you're ready to create your first program. Continue to [Step 3: Create Your First Program](03_create_program.md).

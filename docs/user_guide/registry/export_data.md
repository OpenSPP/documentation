---
openspp:
  doc_status: draft
  products: [registry]
  applies_to:
    - social_registry
    - sp_mis
---

# Export Registrant Data

**Applies to:** Social Registry, SP-MIS

## What You Will Do

Export registrant data from OpenSPP to CSV or Excel files for analysis, backup, or preparing data updates.

## Before You Start

- You need **Administrator** access (export requires admin permissions)
- Know which fields you need to export

## Understanding Export

Export serves several purposes:

| Purpose | Description |
|---------|-------------|
| **Record keeping** | Archive or backup registrant data |
| **Analysis** | Analyze data in Excel, Google Sheets, or other tools |
| **Import templates** | Get correct headers for importing new data |
| **Update preparation** | Get IDs needed to update existing records |

## Export Data

### Step 1: Navigate to Records

Go to **Registry** > **Browse All (Audit)** > **All Individuals** or **All Groups**.

![Navigate to Browse All](/_images/en-us/registry/export-data/01-navigate-to-browse-all-for-export.png)

### Step 2: Select Records to Export

Select the records you want to export:

| Goal | How to Select |
|------|---------------|
| Export specific records | Click the checkbox next to each record |
| Export current page | Click the checkbox in the header row |
| Export all records | Click the checkbox, then click **Select all** link |

![Select records](/_images/en-us/registry/export-data/02-select-records-with-checkboxes-for-export.png)

### Step 3: Open Export Dialog

1. Click the **Action** button
2. Select **Export**

![Action menu with Export option](/_images/en-us/registry/export-data/03-action-menu-with-export-option.png)

### Step 4: Choose Export Format

Select your preferred format:

![Export format selection](/_images/en-us/registry/export-data/04-export-format-selection-csv-or-xlsx.png)

| Format | Best For |
|--------|----------|
| **CSV** | Data analysis tools, programming, universal compatibility |
| **XLSX** | Excel users, preserves formatting |

### Step 5: Select Fields to Export

The export dialog shows available fields and fields to export:

![Export dialog with field selection](/_images/en-us/registry/export-data/05-export-dialog-with-field-selection.png)

| Section | Description |
|---------|-------------|
| **Available fields** | All fields you can add to export |
| **Fields to export** | Currently selected fields |

**To add a field:**
- Click the **+** icon next to a field

**To remove a field:**
- Click the trash icon in the "Fields to export" list

**To see nested fields:**
- Click the arrow **>** next to a field to expand it

### Step 6: Export

Click **Export** to download the file.

![Export button](/_images/en-us/registry/export-data/06-export-button-to-download-file.png)

The file downloads to your computer.

## Export for Specific Purposes

### For Analysis or Reporting

Export all the fields you need for your analysis:

1. Select all relevant records
2. Add all fields you want to analyze
3. Choose CSV (for data tools) or XLSX (for Excel)
4. Click **Export**

![Export for analysis](/_images/en-us/registry/export-data/07-export-for-analysis-with-all-relevant-fields.png)

### For Creating Import Templates

Get a template with correct headers for importing new data:

1. Select just **one record** (to get the headers)
2. Add the fields you will need for import
3. Export the file
4. Open the file and delete the data row, keeping only the header row
5. Fill in your new data

### For Updating Existing Records

When you need to update records and import them back:

1. Select the records you want to update
2. Check **"I want to update data (import-compatible export)"**
3. Click **Export**

![Export for update option](/_images/en-us/registry/export-data/08-export-for-update-option-including-id-column.png)

This option:
- Includes the **ID** column (required for updates)
- Shows only fields that can be imported
- Hides calculated fields (like Age)

After export:
1. Open the file
2. Modify the values you want to change
3. Keep the ID column unchanged
4. Import the file back to update records

## Create Export Templates

Save time by creating templates for exports you run frequently.

### Create a New Template

1. Configure your export (select all the fields you need)
2. Click the dropdown arrow next to template selection
3. Click **New template**
4. Enter a name for your template
5. Click the save icon

![Create export template](/_images/en-us/registry/export-data/09-create-export-template-for-frequent-exports.png)

### Use an Existing Template

1. Open the Export dialog
2. Click the template dropdown
3. Select your saved template
4. Fields are automatically selected

![Select export template](/_images/en-us/registry/export-data/10-select-existing-export-template-from-dropdown.png)

## Common Export Fields

### Individual Fields

| Field | Description |
|-------|-------------|
| **name** | Full name (auto-generated from family/given name) |
| **family_name** | Last name / surname |
| **given_name** | First name |
| **addl_name** | Middle name |
| **birthdate** | Date of birth |
| **gender_id** | Gender |
| **address** | Physical address |
| **email** | Email address |
| **phone** | Primary phone number |
| **registration_date** | Date of registration |

### Group Fields

| Field | Description |
|-------|-------------|
| **name** | Group name |
| **group_type_id** | Type of group (Household, etc.) |
| **address** | Physical address |
| **email** | Email address |
| **phone** | Primary phone number |
| **registration_date** | Date of registration |

### Nested Fields

Some fields have nested data. Click the arrow to expand:

- **reg_ids** > Shows all ID documents
- **phone_number_ids** > Shows all phone numbers
- **tags_ids** > Shows all tags

## Are You Stuck?

**Export option not visible?**

- You need Administrator access
- Contact your administrator to request export permissions

**Cannot find a field?**

- Some fields may be nested (click arrows to expand)
- Some calculated fields are not exportable
- Check if the field is available for the record type (Individual vs Group)

**Exported dates look wrong?**

- Dates export in YYYY-MM-DD format
- Excel may reformat them based on your regional settings
- Format the column as Text to preserve the original format

**Phone numbers missing leading zeros?**

- Format the column as Text in Excel after opening
- Or open the CSV in a text editor to see raw values

**Export takes too long?**

- Export fewer records at a time
- Select fewer fields
- Try CSV format (faster than XLSX)

**Need to export more than shown on page?**

- Click the header checkbox, then click **Select all** link
- This selects all records matching your current search/filter

**Template not saving?**

- Make sure you clicked the save icon after naming the template
- Refresh the page and check if the template appears

## Next Steps

- {doc}`import_data` - Import data back into OpenSPP
- {doc}`search_filter` - Filter records before exporting
- {doc}`register_individual` - Register individuals manually

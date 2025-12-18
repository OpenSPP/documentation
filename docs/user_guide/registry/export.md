---
openspp:
  doc_status: draft
---

# Export Registrant Data

This guide is for **users** who need to export registrant data from OpenSPP.

## What You'll Learn

By the end of this guide, you will be able to:
- Export individual or group data
- Choose which fields to export
- Create reusable export templates
- Prepare exports for data updates

## Prerequisites

- **System Admin** role in OpenSPP (export requires admin access)
- Knowledge of which fields you need to export

## Understanding Export

Export serves multiple purposes:

| Purpose | Description |
|---------|-------------|
| **Record keeping** | Archive or backup registrant data |
| **Analysis** | Analyze data in external tools |
| **Import preparation** | Get correct headers for importing new data |
| **Update preparation** | Get IDs needed to update existing records |

## Export Data

### Step 1: Navigate to Registry

1. Click the four-square menu icon
2. Select **Registry**

![Navigate to Registry](howto/user_guides/export_registrant_data/1.png)

### Step 2: Select Record Type

Click **Individuals** or **Groups** depending on what you want to export.

![Select type](howto/user_guides/export_registrant_data/2.png)

### Step 3: Select Records

Select records to export:

| Goal | Selection Method |
|------|------------------|
| Export specific records | Click checkboxes next to each record |
| Export current page | Click checkbox next to "Name" header |
| Export all records | Click "Select all" link |

![Select records](howto/user_guides/export_registrant_data/3.png)

### Step 4: Open Export Dialog

1. Click **Action** button
2. Select **Export**

### Step 5: Configure Export

![Export dialog](howto/user_guides/export_registrant_data/4.png)

| Option | Description |
|--------|-------------|
| **Format** | CSV or XLSX |
| **Available fields** | Fields you can add to export |
| **Fields to export** | Currently selected fields |
| **I want to update data** | Includes ID column and limits to importable fields |

**To add fields**: Click the **+** icon next to a field.

**To remove fields**: Click the trash icon in "Fields to export".

**To see subfields**: Click the arrow **>** next to a field.

### Step 6: Export

Click **Export** to download the file.

## Export for Specific Purposes

### For Record Keeping / Analysis

1. Select all records you need
2. Choose all relevant fields
3. Select CSV (for data tools) or XLSX (for Excel)
4. Click Export

### For Importing New Records

1. Select just one record (to get headers)
2. Choose fields you'll need for import
3. Export the file
4. Delete the data row, keep only headers
5. Fill in your new data

### For Updating Existing Records

1. Select records you want to update
2. Check **"I want to update data (import-compatible export)"**
3. This automatically:
   - Includes the ID column (required for updates)
   - Hides non-importable fields (like calculated Age)
4. Export and modify the values you want to change
5. Import the modified file back

## Create Export Templates

Save time by creating templates for frequently used exports.

### Create a Template

1. Configure your export (select fields)
2. Click the dropdown arrow next to template selection
3. Click **New template**
4. Enter a template name
5. Click the save icon

![Create template](tutorial/user_guides/export_registrant_data/4.png)

### Use a Template

1. Open the Export dialog
2. Click the template dropdown
3. Select your saved template
4. Fields are automatically selected

## Export Format Comparison

| Format | Best For | Notes |
|--------|----------|-------|
| **CSV** | Data analysis tools, programming | Universal compatibility |
| **XLSX** | Excel users | Preserves formatting, multiple sheets |

## Are You Stuck?

**Export option not visible?**
- You need System Admin role
- Contact your administrator

**Can't find a field?**
- Some fields may be nested (click arrows to expand)
- Some fields aren't exportable

**Exported data looks wrong?**
- Check date formats
- Numbers with leading zeros may need Text format in Excel

**Need to export more than shown on page?**
- Click "Select all" to include records beyond current page

## Next Steps

- {doc}`import` - Import data back into OpenSPP
- {doc}`register_individual` - Register individuals manually

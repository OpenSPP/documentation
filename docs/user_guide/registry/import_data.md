---
openspp:
  doc_status: draft
  products: [registry]
  applies_to:
    - social_registry
    - sp_mis
---

# Import registrant data

**Applies to:** Social Registry, SP-MIS

## What you will do

Bulk import registrant data from CSV or Excel files to add new records or update existing ones.

## Before you start

- You need **Administrator** access (import requires admin permissions)
- Data file in CSV or XLSX (Excel) format
- Spreadsheet software (Excel, Google Sheets, or LibreOffice) to prepare the file

## Understanding import

Import in OpenSPP works by uploading a file (CSV or Excel) whose **structure matches the data model used by OpenSPP**. Column names in your file must correspond to the field names in the implementation so that each column maps to the correct field when records are created or updated. If the structure or field names do not match, data may be ignored, misapplied, or the import may fail.

You can use import to:

| Purpose | Description |
|---------|-------------|
| **Add new records** | Create multiple individuals or groups at once |
| **Update existing records** | Modify data for registrants already in the system |

The recommended way to get the correct structure is to **export a template** from OpenSPP (see [Prepare your import file](#prepare-your-import-file)) and use that file’s headers and format as the basis for your import file. This ensures your columns align with OpenSPP’s fields and map correctly during import.

## Prepare your import file

### Step 1. Get a template

The best way to prepare your file is to export existing records first:

1. Go to **Registry** > **Browse All (Audit)** > **All Individuals** (or **All Groups**)
2. Select one record
3. Use **Action** > **Export** to download a template
4. Select the checkbox **I want to update data (import-compatible export)** to export only fields that OpenSPP recognizes for import
4. On the downloaded xlsx file template, keep only the header row, delete the data rows

![Export template](/_images/en-us/registry/import-data/01-export-headers.png)

### Step 2. Format your data

Prepare your data following these rules:

| Data type | Format | Example |
|-----------|--------|---------|
| **Dates** | YYYY-MM-DD | 1990-05-15 |
| **Phone numbers** | Text (not number) | 09171234567 |
| **IDs** | Text (not number) | 000123456 |
| **Yes/No fields** | TRUE or FALSE | TRUE |

```{important}
Format phone numbers and ID columns as **Text** in Excel. Otherwise, Excel may remove leading zeros (000123 becomes 123).
```

**In Excel:** Right-click column > Format Cells > Text

### Step 3. Required fields

For new individual records, these fields are required:

| Field | Description |
|-------|-------------|
| **family_name** | Last name / surname |
| **given_name** | First name |
| **name** | given name + family name |


For new group records, this field is required:

| Field | Description |
|-------|-------------|
| **name** | Group name |

### Step 4. Optional fields

Common optional fields you can include:

| Field | Description |
|-------|-------------|
| **birthdate** | Date of birth (YYYY-MM-DD) |
| **address** | Physical address |
| **email** | Email address |
| **phone** | Primary phone number |
| **registration_date** | Registration date (defaults to today) |

## Import new records

### Step 1: Navigate to import

1. Go to **Registry** > **Browse All (Audit)** > **All Individuals** (or **All Groups**)
2. Click the **Gear** icon.
3. Select **Import records**

![Import menu location](/_images/en-us/registry/import-data/02-import-menu.png)

### Step 2: Upload your file

1. Click **Upload File**
2. Select your prepared CSV or XLSX file

Sample document for reference:
![sample file document](/_images/en-us/registry/import-data/03-sample-file-document.png)

<!-- ![Upload file dialog](/_images/en-us/registry/import-data/03-upload-file-dialog-for-csv-or-xlsx.png) -->

### Step 3: Map columns

OpenSPP automatically maps columns based on header names. Review the mapping:

![Column mapping screen](/_images/en-us/registry/import-data/04-column-mapping-screen-showing-fields-matched.png)

- Green checkmarks indicate successfully mapped columns
- Yellow warnings indicate columns that need manual mapping
- Use the dropdown to manually map any unrecognized columns

### Step 4: Test the import

Click **Test** to validate your file without importing.

![Test button](/_images/en-us/registry/import-data/05-test-button-for-validating-import-file.png)

If successful, you will see: **"Everything seems valid"**

If there are errors, see the [Error Handling](#error-handling) section below.

### Step 5: Import

When validation passes, click **Import** to create the records.

![Import button](/_images/en-us/registry/import-data/07-import-button-to-create-records.png)

A notification confirms how many records were imported.

![Import success notification](/_images/en-us/registry/import-data/08-import-success-notification-with-record-count.png)

```{tip}
For large files (1,000+ records), check **Import in the background** to prevent browser timeouts.
```

### Step 6: Verify

Search for imported records to confirm they were created correctly:

1. Use the Registry Search Portal to find records by name
2. Or filter by "Created on" date to find today's imports

![Verify imported records](/_images/en-us/registry/import-data/09-verify-imported-records-in-search-results.png)

## Update existing records

To update records that already exist in the system:

### Step 1: Export records to update

1. Select the records you want to update by clicking the checkbox beside the individual or group
2. **Action** button should appear, use **Action** > **Export**
3. Check **"I want to update data (import-compatible export)"**
4. Click **Export**

![Export for update option](/_images/en-us/registry/import-data/10-export-for-update-option.png)

This includes the **ID** column, which is required for referencing the corresponding record.

![Export for update option](/_images/en-us/registry/import-data/12-reference-id.png)

### Step 2: Modify the file

1. Open the exported file in your spreadsheet software
2. Modify the values you want to change
3. **Keep the ID column unchanged**
4. Save the file

```{warning}
Empty cells will overwrite existing values with blank. If you do not want to change a field, keep its original value.
```

### Step 3: Import the modified file

Follow the same import steps as above. OpenSPP will match records by ID and update them.

## Add individuals to existing groups

To add individuals to existing groups during import:

### Step 1: Get the group external ID

1. Go to **Registry** > **Browse All (Audit)** > **All Groups**
2. Select the group(s) you want to add individuals to
3. Use **Action** > **Export**
4. Check **"I want to update data (import-compatible export)"**
5. Click **Export**
6. Note the **External ID** value from the exported file for the group(s)

![Group external ID](/_images/en-us/registry/import-data/14-group-external-id.png)

### Step 2: Get the membership header

1. Go to **Registry** > **Browse All (Audit)** > **All Individuals**
2. Select at least one individual record
3. Use **Action** > **Export**
4. Check **"I want to update data (import-compatible export)"**
5. In the export dialog, search for **membership to groups**
6. Expand the section and add **Membership to Groups/Group/External ID** to the fields to export
7. Click **Export**

![Membership header selection](/_images/en-us/registry/import-data/15-membership-header.png)

The exported file will contain the header **individual_membership_ids/group/id**. This is the column where you will assign the group's External ID.

### Step 3: Prepare your import file

1. Open the exported individual file in your spreadsheet software
2. Add or modify the **individual_membership_ids/group/id** column
3. Enter the External ID of the group(s) you want to assign individuals to
4. Save the file

### Step 4: Import the file

Follow the same import steps as described in [Import New Records](#import-new-records). Once imported, the individuals will belong to the group(s) you specified.

## Error handling

### "No matching records found"

**Cause:** A field value does not match predefined options.

![No matching error](/_images/en-us/registry/import-data/11-no-matching-records-found-error.png)

**Solution:**
- Find valid values in the system
- Go to **Settings** > **Vocabulary** > **Manage Vocabularies**
- Search for the field (for example, gender), then click it and open the **Codes** tab to see valid values
- Use the exact values as shown in the system

### "To import, select a field"

**Cause:** OpenSPP does not recognize a column header.

![Unrecognized column error](/_images/en-us/registry/import-data/16-unrecognized-column.png)

**Solution:**
- Click the dropdown to manually map the field
- Or remove the column if not needed

### "Column contains incorrect values"

**Cause:** Date format is incorrect.

![Date format error](/_images/en-us/registry/import-data/13-date-format-error.png)

**Solution:** Change dates to YYYY-MM-DD format (for example, 2024-12-18)

## Best practices

| Practice | Why |
|----------|-----|
| **Always test first** | Catches errors before they affect data |
| **Format numbers as text** | Prevents Excel from removing leading zeros |
| **Keep backups** | Export data before bulk updates |
| **Use background import** | Prevents timeouts for large files |
| **Verify after import** | Confirms data imported correctly |
| **Import in batches** | For very large datasets, split into smaller files |

## Are you stuck?

**Import menu not visible?**

- You need Administrator access
- Contact your administrator to request access

**File not uploading?**

- Only CSV and XLSX formats are accepted
- Check the file is not corrupted or too large
- Try saving as a new file

**Some fields not importing?**

- Calculated fields (like Age) cannot be imported
- Use "import-compatible export" to see which fields can be imported

**Dates showing incorrectly?**

- Make sure dates are in YYYY-MM-DD format
- Check that the column is not formatted as a number in Excel

**Phone numbers missing leading zeros?**

- Format the phone number column as Text before entering data
- Re-type the numbers with leading zeros if needed

**Import takes too long?**

- Use **Import in the background** option
- Split large files into smaller batches (500-1000 records each)

## Next steps

- {doc}`export_data` - Learn how to export data
- {doc}`search_filter` - Find imported records
- {doc}`register_individual` - Register individuals manually instead

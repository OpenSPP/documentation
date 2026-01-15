---
openspp:
  doc_status: draft
  products: [registry]
  applies_to:
    - social_registry
    - sp_mis
---

# Import Registrant Data

**Applies to:** Social Registry, SP-MIS

## What You Will Do

Bulk import registrant data from CSV or Excel files to add new records or update existing ones.

## Before You Start

- You need **Administrator** access (import requires admin permissions)
- Data file in CSV or XLSX (Excel) format
- Spreadsheet software (Excel, Google Sheets, or LibreOffice) to prepare the file

## Understanding Import

Import allows you to:

| Purpose | Description |
|---------|-------------|
| **Add new records** | Create multiple individuals or groups at once |
| **Update existing records** | Modify data for registrants already in the system |

## Prepare Your Import File

### Step 1: Get a Template

The best way to prepare your file is to export existing records first:

1. Go to **Registry** > **Browse All (Audit)** > **All Individuals** (or **All Groups**)
2. Select one record
3. Use **Action** > **Export** to download a template
4. Keep only the header row, delete the data rows

![Export template](/_images/en-us/registry/import-data/01-export-template-from-browse-all-for-import-prepara.png)

### Step 2: Format Your Data

Prepare your data following these rules:

| Data Type | Format | Example |
|-----------|--------|---------|
| **Dates** | YYYY-MM-DD | 1990-05-15 |
| **Phone numbers** | Text (not number) | 09171234567 |
| **IDs** | Text (not number) | 000123456 |
| **Yes/No fields** | TRUE or FALSE | TRUE |

```{important}
Format phone numbers and ID columns as **Text** in Excel. Otherwise, Excel may remove leading zeros (000123 becomes 123).
```

**In Excel:** Right-click column > Format Cells > Text

### Step 3: Required Fields

For new individual records, these fields are required:

| Field | Description |
|-------|-------------|
| **family_name** | Last name / surname |
| **given_name** | First name |

For new group records, this field is required:

| Field | Description |
|-------|-------------|
| **name** | Group name |

### Step 4: Optional Fields

Common optional fields you can include:

| Field | Description |
|-------|-------------|
| **birthdate** | Date of birth (YYYY-MM-DD) |
| **address** | Physical address |
| **email** | Email address |
| **phone** | Primary phone number |
| **registration_date** | Registration date (defaults to today) |

## Import New Records

### Step 1: Navigate to Import

1. Go to **Registry** > **Browse All (Audit)** > **All Individuals** (or **All Groups**)
2. Click the **Favorites** icon (star) in the top right
3. Select **Import records**

![Import menu location](/_images/en-us/registry/import-data/02-import-menu-location-showing-import-records-option.png)

### Step 2: Upload Your File

1. Click **Upload File** (or **Load File**)
2. Select your prepared CSV or XLSX file

![Upload file dialog](/_images/en-us/registry/import-data/03-upload-file-dialog-for-csv-or-xlsx.png)

### Step 3: Map Columns

OpenSPP automatically maps columns based on header names. Review the mapping:

![Column mapping screen](/_images/en-us/registry/import-data/04-column-mapping-screen-showing-fields-matched.png)

- Green checkmarks indicate successfully mapped columns
- Yellow warnings indicate columns that need manual mapping
- Use the dropdown to manually map any unrecognized columns

### Step 4: Test the Import

Click **Test** to validate your file without importing.

![Test button](/_images/en-us/registry/import-data/05-test-button-for-validating-import-file.png)

If successful, you will see: **"Everything seems valid"**

![Validation success](/_images/en-us/registry/import-data/06-validation-success-showing-everything-seems-valid.png)

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

## Update Existing Records

To update records that already exist in the system:

### Step 1: Export Records to Update

1. Select the records you want to update
2. Use **Action** > **Export**
3. Check **"I want to update data (import-compatible export)"**
4. Click **Export**

![Export for update option](/_images/en-us/registry/import-data/10-export-for-update-option-with-import-compatible-ex.png)

This includes the **ID** column, which is required for updates.

### Step 2: Modify the File

1. Open the exported file in your spreadsheet software
2. Modify the values you want to change
3. **Keep the ID column unchanged**
4. Save the file

```{warning}
Empty cells will overwrite existing values with blank. If you do not want to change a field, keep its original value.
```

### Step 3: Import the Modified File

Follow the same import steps as above. OpenSPP will match records by ID and update them.

## Error Handling

### "No matching records found"

**Cause:** A field value does not match predefined options.

![No matching error](/_images/en-us/registry/import-data/11-no-matching-records-found-error.png)

**Solution:**
- Check valid values in the system
- For tags: Go to **Registry** > **Configuration** > **Registrant Tags**
- For gender: Go to **Configuration** > **Vocabularies**
- Use exact values as shown in the system

### "To import, select a field"

**Cause:** OpenSPP does not recognize a column header.

![Unrecognized column error](/_images/en-us/registry/import-data/12-unrecognized-column-error-requiring-field-selectio.png)

**Solution:**
- Click the dropdown to manually map the field
- Or remove the column if not needed

### "Column contains incorrect values"

**Cause:** Date format is incorrect.

![Date format error](/_images/en-us/registry/import-data/13-date-format-error-showing-incorrect-values.png)

**Solution:** Change dates to YYYY-MM-DD format (for example, 2024-12-18)

### "You are not allowed to access 'Import Matching'"

**Cause:** Your account lacks Administrator permissions.

![Access denied error](/_images/en-us/registry/import-data/14-access-denied-error-for-non-administrators.png)

**Solution:** Contact your administrator to request import access.

## Best Practices

| Practice | Why |
|----------|-----|
| **Always Test first** | Catches errors before they affect data |
| **Format numbers as Text** | Prevents Excel from removing leading zeros |
| **Keep backups** | Export data before bulk updates |
| **Use background import** | Prevents timeouts for large files |
| **Verify after import** | Confirms data imported correctly |
| **Import in batches** | For very large datasets, split into smaller files |

## Are You Stuck?

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

## Next Steps

- {doc}`export_data` - Learn how to export data
- {doc}`search_filter` - Find imported records
- {doc}`register_individual` - Register individuals manually instead

---
openspp:
  doc_status: draft
---

# Import Registrant Data

This guide is for **users** who need to bulk import registrant data from CSV or Excel files.

## What You'll Learn

By the end of this guide, you will be able to:
- Prepare data files for import
- Import new individuals or groups
- Update existing registrant data
- Handle common import errors

## Prerequisites

- **System Admin** role in OpenSPP (import requires admin access)
- Data in CSV or XLSX (Excel) format
- Spreadsheet software (Excel, Google Sheets, LibreOffice)

## Understanding Import

Import serves two purposes:

| Purpose | Description |
|---------|-------------|
| **Add new records** | Create new individuals or groups from file data |
| **Update existing records** | Modify data for registrants already in the system |

## Prepare Your File

### For New Records

1. **Export a template** first to get correct headers:
   - Go to Registry > Individuals (or Groups)
   - Select one record and export it
   - Keep only the header row, delete data rows

2. **Format numeric columns as Text**:
   - Phone numbers, dates, IDs
   - In Excel: Right-click column > Format Cells > Text

3. **Fill in your data**:
   - Use YYYY-MM-DD format for dates
   - Empty cells will create blank values

### For Updating Existing Records

1. **Export records to update**:
   - Select the records you want to update
   - Check "I want to update data (import-compatible export)"
   - This includes the **ID** column needed for updates

2. **Modify the exported file**:
   - Keep the ID column unchanged
   - Update values in other columns
   - Empty cells will overwrite with blank values

## Perform the Import

### Step 1: Navigate to Import

1. Go to **Registry** > **Individuals** (or **Groups**)
2. Click the **Favorites** icon (star)
3. Select **Import records**

![Import menu](howto/user_guides/import_registrant_data/2.png)

### Step 2: Upload File

1. Click **Load File** (or **Upload File**)
2. Select your prepared CSV or XLSX file

![Upload screen](howto/user_guides/import_registrant_data/3.png)

```{tip}
For large files (1,000+ records), check **Import in the background** to prevent timeouts.
```

### Step 3: Test the Import

1. Click **Test** to validate your file

![Test validation](howto/user_guides/import_registrant_data/4.png)

2. If successful, you'll see "Everything seems valid"
3. If errors appear, see [Error Handling](#error-handling) below

### Step 4: Import

1. Click **Import** when validation passes
2. A notification confirms the number of imported records

![Import success](tutorial/user_guides/import_registrant_data/9.png)

### Step 5: Verify

1. Use filters to find imported records:
   - For new records: Filter by "Created on"
   - For updates: Filter by "Last updated on"

![Verify import](howto/user_guides/import_registrant_data/5.png)

## Error Handling

### "No matching records found"

**Cause**: A field value doesn't match predefined options in OpenSPP.

**Example**: Invalid category_id value.

![No matching error](tutorial/user_guides/import_registrant_data/10.png)

**Solution**: Check valid values in Registry > Configuration > Registrant Tags.

![Valid tags](tutorial/user_guides/import_registrant_data/11.png)

### "To import, select a field"

**Cause**: OpenSPP doesn't recognize a column header.

![Unrecognized header](tutorial/user_guides/import_registrant_data/12.png)

**Solution**:
- Click the dropdown to manually map the field, OR
- Remove the column if the field isn't needed

### "Column contains incorrect values"

**Cause**: Date format is incorrect.

![Date error](tutorial/user_guides/import_registrant_data/13.png)

**Solution**: Change dates to YYYY-MM-DD format (e.g., 2024-12-18).

### "You are not allowed to access 'Import Matching'"

**Cause**: Your account lacks System Admin role.

![Access error](tutorial/user_guides/import_registrant_data/14.png)

**Solution**: Contact your administrator to assign System Admin role.

## Best Practices

| Practice | Reason |
|----------|--------|
| Always **Test** before importing | Catches errors before they affect data |
| Format numbers as Text | Prevents Excel from reformatting phone numbers, IDs |
| Keep backups | Export data before bulk updates |
| Use background import for large files | Prevents browser timeouts |
| Verify after import | Confirms data imported correctly |

## Are You Stuck?

**Import button not visible?**
- You need System Admin role
- Contact your administrator

**File not uploading?**
- Only CSV and XLSX formats are accepted
- Check file isn't corrupted

**Some fields not importing?**
- Not all fields can be imported (e.g., calculated fields like Age)
- Use "import-compatible export" to see importable fields

## Next Steps

- {doc}`export` - Export registrant data
- {doc}`register_individual` - Register individuals manually

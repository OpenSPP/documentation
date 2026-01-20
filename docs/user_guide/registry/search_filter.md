---
openspp:
  doc_status: draft
  products: [registry]
  applies_to:
    - social_registry
    - sp_mis
---

# Search and Filter Registrants

**Applies to:** Social Registry, SP-MIS

## What You Will Do

Find specific individuals or groups in the registry using search and filter features.

## Before You Start

- You need **Registry Viewer**, **Officer**, or **Administrator** access
- Know what you are looking for (name, ID, phone number, etc.)

## Using the Registry Search Portal

The Registry Search Portal is the main way to find registrants.

### 1. Open the Registry

Click **Registry** in the main menu to open the Registry Search Portal.

![Registry Search Portal](/_images/en-us/registry/search-filter/01-registry-search-portal-with-search-bar-and-type-filter.png)

### 2. Enter Search Terms

Type in the search box to search by:

- Name (first name, last name, or full name)
- Phone number
- Email address

![Search box with text entered](/_images/en-us/registry/search-filter/02-search-box-with-text-entered-for-search.png)

Press **Enter** or click **Search** to see results.

### 3. View Results

Results show matching registrants with key information:

![Search results list](/_images/en-us/registry/search-filter/03-search-results-list-showing-matching-registrants.png)

| Column | Description |
|--------|-------------|
| **Name** | Individual or group name |
| **Phone** | Contact phone number |
| **Registration Date** | When they were registered |

## Filtering by Type

### Search Individuals Only

To search only for individuals:

1. Open the Registry Search Portal
2. Select **Individuals** from the type filter (if available)
3. Enter your search terms
4. The results would only display individuals.

![Filtering for groups](/_images/en-us/registry/search-filter/04-type-filter-highlight-individuals.png)

### 5. Search Groups Only

To search only for groups:

1. Open the Registry Search Portal
2. Select **Groups** from the type filter
3. Enter your search terms

![Filtering for groups](/_images/en-us/registry/search-filter/05-type-filter-set-to-groups-only.png)

## Using Advanced Filters (Browse All)

For more advanced filtering, use the Browse All view (requires Auditor or Administrator access).

### 1. Navigate to Browse All

Go to **Registry** > **Browse All (Audit)** > **All Individuals** or **All Groups**.



### 2. Use the Search Bar

The search bar supports searching by:
- Name
- Phone
- Email

![Search bar in Browse All](/_images/en-us/registry/search-filter/07-search-bar-in-browse-all-view.png)

### 3. Apply Filters

Click the dropdown icon beside the searchbar to access preset filters:

![Filter dropdown](/_images/en-us/registry/search-filter/08-filter-dropdown-with-preset-filters.png)

#### Available Filters for Individuals

| Filter | What It Shows |
|--------|---------------|
| **Archived** | Records that have been archived |
| **Disabled** | Records that have been disabled |
| **Male** | Individuals with Male gender |
| **Female** | Individuals with Female gender |

#### Available Filters for Groups

| Filter | What It Shows |
|--------|---------------|
| **Archived** | Records that have been archived |
| **Disabled** | Records that have been disabled |
| **Recently Registered** | Groups registered in the last 30 days |
| **Has Email** | Groups with an email address |
| **Has Phone** | Groups with at least one phone number |

### 9. Group Results

Use **Group By** to organize results by category. Click the Group By button and select **Group Type**:

![Group By options](/_images/en-us/registry/search-filter/09-group-by-group-type.png)

| Group By Option | What It Does |
|-----------------|--------------|
| **Gender** | Groups results by gender |
| **Registration Date** | Groups by exact registration date |
| **Registration Month** | Groups by month of registration |
| **Registration Year** | Groups by year of registration |
| **Group Type** | Groups by type (for group records) |

### 10. Combine Multiple Filters

Click multiple filters to combine them. For example:
- **Female** + **Recently Registered** = Female individuals registered in the last 30 days

![Combined filters](/_images/en-us/registry/search-filter/10-combined-filters-applied-showing-results.png)

### 11. Custom Filter Domains

For advanced users, click the dropdown beside the search, then click **Custom Filter** to create custom search criteria:

1. Click the dropdown beside the search
2. Click **Custom Filter**
3. Select a field, operator, and value
4. Click **Apply**

![Custom filter dialog](/_images/en-us/registry/search-filter/11-custom-filter-dialog-for-advanced-criteria.png)

Example custom filters:

| Field | Operator | Value | Result |
|-------|----------|-------|--------|
| Registration Date | >= | 2024-01-01 | Registered this year |
| Income | < | 5000 | Low income registrants |

### 12. Sorting Results

Click on any column header to sort by that column:

- Click once for ascending order (A-Z, oldest first)
- Click again for descending order (Z-A, newest first)

![Sorting by column](/_images/en-us/registry/search-filter/12-sorting-by-column-header.png)

### Default Sort Order

By default, results are sorted by ID in descending order (newest records first).

### 13. Viewing Record History

Each record shows when it was created and last modified in the **History** tab:

![History tab](/_images/en-us/registry/search-filter/13-history-tab-showing-record-creation-and-modification.png)

| Field | Description |
|-------|-------------|
| **Created on** | Date and time the record was created |
| **Created by** | User who created the record |
| **Last Updated on** | Date and time of last modification |
| **Last Updated by** | User who last modified the record |

## Are You Stuck?

**Search returns no results?**

- Check your spelling
- Try searching by a different field (name, phone, email)
- Make sure you are searching the right type (Individuals vs Groups)
- The person may not be registered yet

**Cannot see Browse All menu?**

- Browse All requires Auditor or Administrator access
- Use the Registry Search Portal instead
- Contact your administrator if you need auditor access

**Filters not working as expected?**

- Make sure you have selected the correct filter
- Check if multiple filters are applied (they combine with AND logic)
- Clear all filters and start again

**Cannot find a recently registered person?**

- Try sorting by Registration Date (newest first)
- Check if they were registered under a different name
- Verify the registration was saved successfully

**Custom filter shows error?**

- Make sure the field, operator, and value are compatible
- Date fields need values in YYYY-MM-DD format
- Numeric fields need numeric values

## Next Steps

- {doc}`export_data` - Export search results to CSV or Excel
- {doc}`register_individual` - Register a new individual if not found
- {doc}`register_group` - Register a new group if not found

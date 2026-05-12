---
openspp:
  doc_status: draft
  products: [core]
---

# HDX COD integration

This guide is for **implementers** importing standardized administrative boundaries from the Humanitarian Data Exchange (HDX) Common Operational Datasets (COD).

## Mental model

HDX COD integration has two layers:

| Layer | What it does | Example |
|-------|--------------|---------|
| **COD Source** | Links to a country's boundary dataset on HDX | "Philippines Administrative Boundaries" |
| **COD Resource** | Individual boundary files within the dataset | "Admin Level 3 - Municipalities (GeoJSON)" |

Think of it like this: the **source** is the book (one per country) and **resources** are the chapters (one per admin level).

## Key concepts

### COD source

| Field | What it means |
|-------|---------------|
| **Country** | Target country |
| **Country ISO3** | ISO 3166-1 alpha-3 code (e.g., PHL, KEN) |
| **HDX Dataset ID** | Unique identifier from HDX |
| **HDX Dataset URL** | Link to the dataset on HDX |
| **Last Sync** | When resources were last fetched from HDX |
| **Last Import** | When boundaries were last imported into OpenSPP |
| **Areas Updated** | Number of area records created or updated |

### COD resource

Each resource represents one admin level's boundary data:

| Field | What it means |
|-------|---------------|
| **Admin Level** | Administrative level (0 = country, 1 = region, etc.) |
| **Format** | File format (GeoJSON, Shapefile, etc.) |
| **P-code Field** | Field containing the standardized location code |
| **Name Field** | Field containing the area name |
| **Feature Count** | Number of boundary features in the file |

### P-codes

P-codes (place codes) are standardized location identifiers used across the humanitarian community. They map directly to OpenSPP area codes, enabling interoperability with other systems.

## Step-by-step setup

### Step 1: Create a COD source

1. Navigate to the HDX COD configuration (requires admin access)
2. Click **Create**
3. Select the **Country**
4. Enter the **HDX Dataset ID** (find this on [data.humdata.org](https://data.humdata.org))
5. Save

### Step 2: Sync resources

1. Open the COD source record
2. Click **Sync from HDX**
3. The system fetches available resources (boundary files) from HDX
4. Review the detected resources and their admin levels

### Step 3: Map fields

1. For each resource, the system auto-detects the P-code and Name fields
2. Review the **P-code Field** and **Name Field** mappings
3. Adjust if the auto-detection chose incorrectly

### Step 4: Import boundaries

1. Click **Import** on the COD source
2. Select which admin levels to import
3. The system creates area records with:
   - P-code as the area code
   - Name from the name field
   - Parent-child relationships based on admin level hierarchy
4. Review the import results

## Navigation

| Menu | Purpose |
|------|---------|
| **HDX COD Sources** | Manage country-level HDX connections |
| **HDX COD Resources** | View individual boundary files |

```{note}
HDX COD configuration is restricted to administrators.
```

## Common use cases

### Use case 1: Initial country setup

**Goal:** Populate the entire area hierarchy for a new country deployment.

**Setup:**
1. Find the country's COD dataset on [data.humdata.org](https://data.humdata.org)
2. Create a COD source with the dataset ID
3. Sync and import all admin levels (0 through 3 or 4)
4. Verify the hierarchy in **Area > Areas > Area**

### Use case 2: Boundary update

**Goal:** Update area boundaries after an administrative redistricting.

**Setup:**
1. Open the existing COD source
2. Re-sync from HDX to fetch updated resources
3. Re-import - existing areas are updated by P-code, new areas are created
4. Review areas where names changed

## Are You Stuck?

**Where do I find the HDX Dataset ID?**

Go to [data.humdata.org](https://data.humdata.org), search for your country + "administrative boundaries", and look for datasets tagged "cod-ab". The dataset ID is in the URL.

**Sync fails with a connection error?**

Check that the OpenSPP server has internet access and can reach `data.humdata.org`. If behind a proxy, configure the proxy settings.

**P-code field not auto-detected?**

Manually select the correct field. Common field names are `ADM1_PCODE`, `ADM2_PCODE`, `admin2Pcode`, etc.

**Imported areas don't have parents?**

Import admin levels in order from 0 (country) down to the lowest level. Parent relationships depend on higher levels existing first.

**Can I import just one admin level?**

Yes. Select only the admin level you need during import. Make sure parent levels already exist in the system.

## Next steps

- {doc}`overview` - Area management fundamentals
- {doc}`/config_guide/gis/overview` - Visualize areas on maps

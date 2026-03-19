---
openspp:
  doc_status: draft
---

# View maps and generate reports

This guide is for **users** — field officers, program managers, and decision-makers who need to view registry data on a map or generate geographic reports.

## What you will do

Configure map layers, view registrant locations on an interactive map, add GPS coordinates to registrant records, and generate geographic coverage reports.

## Before you start

You need:

- **GIS Viewer** access or higher to view maps and reports
- **Administrator** access to configure map layers and data layers
- The `spp_gis` module installed (ask your administrator to install it from the Apps menu)
- `spp_registrant_gis` installed if you need GPS coordinates on registrant records
- `spp_gis_report` installed if you need geographic reports
- A MapTiler API key (obtain one from the [MapTiler Cloud documentation](https://docs.maptiler.com/cloud/api/))

## Steps

### Step 1. Configure the MapTiler API key

This is done once by an administrator before maps can display tiles.

1. Log in as an administrator.
2. Go to **Settings** and activate **Developer Mode** (scroll to the bottom of the Settings page and click **Activate the developer mode**).
3. Refresh the page, then go back to **Settings > Technical > Parameters > System Parameters**.
4. In the search bar, enter `spp_gis.map_tiler_api_key` and open the record.
5. Enter your MapTiler API key in the **Value** field.
6. Click **Save**, then refresh your browser for the changes to take effect.

```{warning}
Keep your API key secure. Do not share it publicly or store it in version control systems.
```

![System parameters form showing the MapTiler API key field](/_images/en-us/gis/01-maptiler-api-key-system-parameter.png)

### Step 2. Configure the raster layer

Set up which map tiles appear as the background. You need an existing group with at least one land parcel defined before starting.

1. Go to **Registry > Groups** and open an existing group.
2. Click the **Land Parcels** smart button, then click the **Pin** icon to open the map.
3. A **Default** layer is already provided. You can use it as-is or add a custom raster layer.
4. To add a new raster layer, click **+**, fill in the required information, and click **Save**.

![Raster layer configuration form showing layer name, type, and URL fields](/_images/en-us/gis/02-raster-layer-form.png)

### Step 3. Configure and view data layers in the registry

Data layers control which records and fields appear on the map. Requires the `spp_registrant_gis` module.

1. From the map view (Pin icon), click the **Data Layer** tab.
2. Click the **Edit** icon to configure how data is displayed on the map.
3. Click **Save** to apply the changes.
4. Check the boxes beside **Land Coordinates** or **Land Parcels** to display the associated land or farm data for the registrant on the map.

![Data layer configuration showing Land Coordinates and Land Parcels checkboxes](/_images/en-us/gis/03-data-layer-form.png)

### Step 4. Add GPS coordinates to a registrant

*Requires the `spp_registrant_gis` module.*

1. Go to **Registry > Groups** (or **Individuals**) and open a registrant record.
2. Click the **Land Parcels** smart button to open the map.

   ```{note}
   For an individual registrant, click the **Profile** tab and scroll to the **Location** section instead.
   ```

3. Click the tool icon just above the zoom **+** button to activate the drawing tool.
   - **Coordinates:** click anywhere on the map to pin the location.
   - **Polygon:** click to draw a shape point by point; double-click the final point to close the shape.
4. Click **Save**.

![Registrant map view showing the tool icon and a pinned location](/_images/en-us/gis/04-registrant-location-section.png)

### Step 5. Configure and view data layers in an area

Make sure you have existing area data before starting.

1. Go to **Area** and click the **Pin** icon to open the map view.
2. In the **Raster Layer** tab, click **+** to add a new raster layer if needed. Default layers are already provided.
3. In the **Data Layer** tab, click the **Edit** button to configure how data is displayed on the map.
4. Use the map controls to zoom in and out and switch between layers.
5. To define the area's location in the map, from Area list view, click on an area record and scroll down and click the **Coordinates** or **Polygon** tab.
6. Click the tool icon just above the zoom **+** button to activate the drawing tool.
   - **Coordinates:** click anywhere on the map to pin the location.
   - **Polygon:** click to draw a shape point by point; double-click the final point to close the shape.
7. Click **Save**.

![Area map view showing the Polygon tab with raster and data layer controls](/_images/en-us/gis/05-area-polygon-tab.png)

## Are you stuck?

**The map is blank or shows no tiles.**
- API key may have not been defined properly from step 1.
- The Raster layer may not be configured or the tile server URL is unreachable.

**Registrant coordinates are not showing on the map.**

- Make sure `spp_registrant_gis` is installed and that coordinates have been entered on the registrant's Profile tab.
- Records without coordinates do not appear as map pins.

**I cannot access GIS Configuration.**

- Access to configuration menus is restricted to administrators and GIS managers.
- Ask your system administrator to assign you the appropriate role.

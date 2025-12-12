# Integrate geolocation

This guide provides step-by-step instructions for integrating geolocation platforms such as MapTiler with the OpenSPP Farmer Registry module to enhance area-based functionality.

## Prerequisites
To enable geolocation integration in OpenSPP, ensure the following:
- Your user account has the System Admin role. Learn more in this guide: {doc}`user_access`.
- Your OpenSPP instance has the Farmer Registry base module installed. Learn more in this guide: {doc}`../../getting_started/farmer_installation`.
- You have an API key for MapTiler to enable GIS functionality. You can retrieve this by checking their documentation [here](https://docs.maptiler.com/cloud/api/).
- Developer mode in OpenSPP is enabled to allow configuration of the MapTiler key. For details, refer to the {doc}`../../developer_guide/developer_mode`.

## Objective
By the end of this guide, you will have configured MapTiler integration to enable area-based features in the Farmer Registry and will learn how to add, edit, and remove farm geolocation data using the map tools.

## Process

### Setting Up the API Key for MapTiler
As a System Admin, log in to your OpenSPP Farmer Registry instance. Go to **Settings**, then select **Technical**, and click **System Parameters**.

![Settings menu with Technical and System Parameters options](farmer_geolocation/farmer_geolocation_system_parameters.png)

Click the **New** button. Set the Key field to **spp_base_gis.map_tiler_api_key** and enter your MapTiler API key in the **value** field.

![Setup farmer registry maptiler key](farmer_geolocation/farmer_geolocation_maptiler_key.png)

```{note}
Keep your API key secure. Avoid sharing it publicly or storing it in version control systems.
```

Click the **Save** button to apply the configuration. Refresh your browser to see the changes.

### Add Geolocation Data

After setting up the API key for the geolocation platform, navigate to the Registry and click an existing farm group, then open the **Farm Details** tab.

![Farm details tab](farmer_geolocation/farmer_geolocation_farm_details.png)

#### Add Address Coordinates

Under the **Farm Details** tab, click **Address Coordinates**.

Click the Marker tool once, then select a location on the map to add a pin for the farm.

![Marker button](farmer_geolocation/farmer_geolocation_marker_button.png)

You can also click the **Find My Location** button to center the map on your current location.

![Find my location button](farmer_geolocation/farmer_geolocation_find_my_location.png)

#### Add Farm Land

Under the **Farm Details** tab, click **Farm Land**.

Click the polygon tool once, then click the map to add vertices until the area is outlined; double-click the final point to close the polygon.

![polygon tool](farmer_geolocation/farmer_geolocation_polygon_tool.png)

You can also click the **Find My Location** button to center the map on your current location.

![Find my location button](farmer_geolocation/farmer_geolocation_find_my_location.png)

### Remove Geolocation Data

To remove geolocation data, navigate to the **Farm Details** tab, then open the tab for either **Address Coordinates** or **Farm Land**.

Click the trash icon to remove the geolocation data.

![Delete button](farmer_geolocation/farmer_geolocation_delete_button.png)

```{note}
- The trash icon appears only when there is existing map data.
- Deletion cannot be undone.
```
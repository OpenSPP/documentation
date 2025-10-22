# Integrate Geolocation

This guide provides step-by-step instructions for integrating geolocation platforms such as MapTiler with the OpenSPP Farmer Registry module to enhance area-based functionality.

## Prerequisites
To enable geolocation integration in OpenSPP, ensure the following:
- Your user account has the System Admin role. Learn more in this guide: {doc}`user_access`
- Your OpenSPP instance installed Farmer registry base module. Learn more in this gu
- You have an API Key for MapTiler to enable GIS functionality. You can retrieve this by checking their documentation [here](https://docs.maptiler.com/cloud/api/).
- Developer mode in OpenSPP is enabled to allow configuration of the MapTiler key. For details, refer to the {doc}`../../developer_guide/developer_mode`

## Objective
By the end of this guide, you will be able to configure MapTiler integration to support area-based features in the Farmer Registry.

## Process

### Setting Up the API Key for MapTiler
As a System Admin, log in to your OpenSPP Farmer Registry instance. Go to **Settings**, then select **Technical**, and click **System Parameters**.

![Settings menu with Technical and System Parameters options](farmer_geolocation/farmer_geolocation_system_parameters.png)

Click the **New** button. Set the Key field to **spp_base_gis.map_tiler_api_key** and enter your MapTiler API Key in the **value** field.

![Setup farmer registry maptiler key](farmer_geolocation/farmer_geolocation_maptiler_key.png)

Click the **Save** button to apply the configuration. Refresh your browser to see the changes.


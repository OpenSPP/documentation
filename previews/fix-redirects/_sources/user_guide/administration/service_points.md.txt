---
myst:
  html_meta:
    "title": "Setting up service points"
    "description": "Learn how to create, configure, and manage service points in OpenSPP for effective entitlement delivery and benefit distribution"
    "keywords": "OpenSPP, service points, entitlement delivery, benefit distribution, administration"
---

# Setting up service points

A service point is a virtual or physical location where individuals can receive or access their social protection services and benefits.
Setting up service points is crucial for entitlement delivery to ensure that services and benefits are delivered to the recipients correctly.
In this tutorial, you will learn how to set up service points.

## Prerequisites

To configure Service Points, you need to:

- Have an access role as an **System Admin**. Learn more in this guide: {doc}`user_access`.
- Make sure that the modules {doc}`spp_programs_sp </reference/modules/spp_programs_sp>` (**OpenSPP Programs: Service Points Integration**) and {doc}`spp_service_points </reference/modules/spp_service_points>` (**OpenSPP Service Points Management**) are installed. Learn more on installing additional modules in the {doc}`../../getting_started/module_installation`

## Objective

After completing this tutorial, you will understand how to create, update, disable, enable, and export service points in OpenSPP.

## Process

Service points-related tasks such as creating, updating, listing, disabling, enabling, and exporting CSV are performed on the **Service Point** page.

You can access the service point page by clicking on the menu icon on the left side of the header and clicking **Service Point** on the dashboard.

![Screenshot showing the OpenSPP dashboard with the left navigation menu expanded, highlighting the Service Point menu item](setting_up_service_points/1.png)

### Filtering service points

You can filter the list of service points by using the **Search** bar.
Type the text you want to search for, for example, if you search for a service point with the agent name of John.
Type the word John and click the **Search Agent for John**.

![Service Points page showing the search bar with 'John' entered and the Search Agent for John button highlighted](setting_up_service_points/2.png)

The list will be filtered with agents named John.

![Service Points list filtered to show only service points with agents named John](setting_up_service_points/3.png)

You can also group service points by **field**.
For example, you want to group by **Area**.
Click **Group By**, and a dropdown will show.
Click **Area**, the result list will be a group of service types by **Area** list.

![Service Points page showing the Group By dropdown menu with Area option highlighted](setting_up_service_points/4.png)

![Service Points list grouped by Area, showing service points organized under different geographical areas](setting_up_service_points/5.png)

To filter service points using service type fields like **Active Contract**, click the **Arrow down icon** in the **Search** bar and click the **Add Custom Filter**.

![Search bar dropdown menu showing the Add Custom Filter option highlighted](setting_up_service_points/6.png)

If you want to filter service points with **Active Contract**, click **Active Contract is set**.

![Custom filter dialog showing the Active Contract is set filter option ready to be applied](setting_up_service_points/7.png)

The list of service points with **Active Contract** will be displayed.

![Service Points list filtered to show only service points that have an active contract](setting_up_service_points/8.png)

### Creating service point

To create a service point, click the **New** button, you will be redirected to a form.

![Service Points page showing the New button highlighted to create a new service point](setting_up_service_points/9.png)

Fill in the **Agent Name, Address, Phone Number**, and other fields.
Select the **Area** from the list, add **Service Types**, tick **Active Contract**, and hit the **Save** button.

![Service Point creation form with fields for Agent Name, Address, Phone Number, Area selection, Service Types, and Active Contract checkbox](setting_up_service_points/10.png)

### Updating service point

Choose the service point you want to update from the list of service points.
You will be redirected to the view page.
Update fields and click the **Save** button.

![Service Point details page showing editable fields and the Save button, with Disable and Enable options available](setting_up_service_points/11.png)

You can disable a service point by clicking the **Disable** button.
The beneficiaries won't be able to redeem their entitlements from this service point.

To enable a disabled service point, click the service from the list, then click **Enable**.

### Exporting service points

On the **Service Point** page, you can use the export feature to download service points.
You can use filters to narrow down the fields you want your list to have.
Use the **Group By** feature to group service points.
For example, group service points by **Area**, click **Group By**, and select **Area**.

![Service Points page with data grouped by Area, showing the organized list ready for export](setting_up_service_points/14.png)

Click the **Gear icon**, and click **Export All** as a CSV file.
The result CSV will contain a grouped by **Area** service points.

![Service Points page showing the gear menu dropdown with Export All option highlighted for CSV export](setting_up_service_points/16.png)

The specific steps and interface may vary depending on the OpenSPP version.
Always seek assistance from the support team if you need further guidance.

---
review-status: reviewed
review-date: 2025-08-12
reviewer: Mark Penalosa
migration-notes: "Added during 2025 documentation reorganization"
---

# Event Data

## Introduction

In OpenSPP, Event Data provides a flexible mechanism to record and track specific, significant occurrences related to registrants over time. This functionality enhances the system's capacity to capture a chronological history of changes and actions without directly modifying the main registrant profile.

### Overview of Event Data Functionality

The `spp_event_data` module is designed to:
- Provide a structured way to log and store data about events impacting registrants.
- Link these events to the specific data entries they affect, creating a clear audit trail.
- Offer tools to view and navigate the event history of a registrant.
- Store multiple versions of the data, manage separate data lifecycles and sharing agreements, better manage the source of different data, and store data that should not be visible to all users or that loses relevance over time.

### Integration with Program Membership Events

The `spp_event_data_program_membership` module enhances OpenSPP by integrating the Event Data module (`spp_event_data`) with the G2P Programs module (`g2p_programs`). This allows users to record and track program membership-related events, such as enrollment, suspension, exit, and changes in eligibility status, and link them to specific program membership records.

<!-- ### Key Features

1.  **Event Data Model (`spp.event.data`):** This new data model stores event-specific information. It includes fields to record event type, related document/record, registrar, collection date, optional expiry date, and event status (active/inactive).
2.  **Automatic Event Type Calculation:** The event type is dynamically determined and displayed based on the linked data model, providing a clear and user-friendly representation of the event.
3.  **Event History on Registrant Forms:** A dedicated tab is added to both individual and group registrant forms to display their associated event history, enabling users to directly access and review past events related to a specific registrant.
4.  **Event Creation Wizard:** A streamlined process for creating new event data entries through a dedicated wizard, simplifying data entry and ensuring consistency in event logging.
5.  **Active Event Management:** Logic is implemented to manage the active status of events. When a new active event of the same type is created for the same registrant, the previous one is automatically ended, providing a clear view of the current status. -->

## Prerequisites

To utilize and manage Event Data, ensure the following prerequisites are met:

- Individual or group records already exist in your registry. For more information, refer to {doc}`register_individual` or {doc}`import_data`.
- The `spp_event_data` module (OpenSPP Event Data) is installed and activated.
- If specific event types are required (such as program membership events), ensure that any related modules (e.g., `spp_event_data_program_membership`) are also installed and activated.
- To access demonstration features, the `spp_event_demo` module should be activated.
- Appropriate user access roles are assigned to allow creation or viewing of event records. By default, the **System admin** user account has access to event data functionality.

## Objective

By understanding Event Data, you will be able to:
- Log and store structured data about events impacting registrants.
- Link these events to specific data entries, creating a clear audit trail.
- View and navigate the event history of a registrant from their profile.
- Manage different types of event data, allowing for flexible data collection and historical tracking.

## Process

Event data functionality fulfills several important roles, including the systematic tracking of changes to a registrant’s information. A system administrator or authorized user may create an event data entry to record the registrant’s current details at a specific point in time. Subsequent data collection cycles can generate additional event data entries to document any updates or modifications. This approach enables comprehensive monitoring of changes over time and supports the use of event data as conditions or eligibility criteria for particular programs, when appropriately configured.

<!-- ### Demonstration and Examples
The `spp_event_demo` module provides demonstration data and functionalities for the `spp_event_data` module. It showcases how to extend and utilize the event tracking capabilities of OpenSPP for specific use cases through:
* **Predefined Event Types:** Including House Visit (`spp.event.house.visit`), Phone Survey (`spp.event.phone.survey`), and School Enrollment Record (`spp.event.schoolenrollment.record`).
* **Data Models and Views:** Specific data models and user-friendly views for each event type.
* **Event Creation Wizards:** Dedicated wizards for creating new events like "Create Event: House Visit," "Create Event: Phone Survey," and "Create Event: School Enrollment".
* **Integration with Registrant Profiles:** Displays active events on registrant profiles for a quick overview. -->

### Create Event Data

To demonstrate the **event data** functionality, ensure that `spp_event_demo` is activated. To verify, navigate to **Apps** and search for `spp_event_demo`. If it is not yet enabled, click **Activate**. Once successfully activated, the **Activate** button will no longer be visible.

![](using_event_data/using_event_data_verify_event_data_module.png)

Navigate to the registry and select a record either from groups or individuals, then click on the **event data** button from the top menu bar.

![](using_event_data/using_event_data_click_event_button.png)

A modal window will appear. In the **Event Type** field, select an event data template; **House Visit** is suggested for this demonstration. Set an **Expiry Date** to determine when the record will become inactive. Click **Next** to continue.

> The field names displayed in the event data modal are customizable depending on your preference or configuration. 

Fill in the fields you wish to define, then click **Save** to create the event data entry.

### View Event Data

From **Registry**, select a group or an individual and click on the event data tab.

![](using_event_data/Using_event_data_event_data_tab.png)

Click on the green button to view the registrant’s event data details.

![](using_event_data/Using_event_data_view_data.png)

A modal should display the values of the fields for that event data.

![](using_event_data/Using_event_data_event_data_values.png)

From the **Event Data** tab, you can click on the record’s name to view the event data’s information.

![](using_event_data/using_event_data_event_data_name.png)

The displayed fields are all **read-only** and cannot be modified. For the Related Data field, the number shown indicates how many event data entries of the same type currently exist in the registrant's records.

![](using_event_data/using_event_data_click_event_data_name.png)

### Active/Inactive Event Data

When a new event data entry is saved, it is automatically marked as active. Any existing entries with the same event type are automatically updated to **inactive**, ensuring only the latest entry remains active.

> Please note that only one event data entry of each type can be active at a time.

Once an event data entry reaches its expiration date, it will automatically be set to inactive.

![](using_event_data/using_event_data_automatically_inactive.png)

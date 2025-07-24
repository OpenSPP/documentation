---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Event data

## Introduction

In OpenSPP, Event Data provides a flexible mechanism to record and track specific, significant occurrences related to registrants over time. This functionality enhances the system's capacity to capture a chronological history of changes and actions without directly modifying the main registrant profile.

## Prerequisites

To utilize and manage Event Data, you would typically need:
- Existing individual or group records in your registry.
- The `spp_event_data` module (OpenSPP Event Data) installed and activated.
- Depending on the specific event types (e.g., program membership events), related modules like `spp_event_data_program_membership` or `spp_event_demo` might be required.
- Appropriate user access roles to create, view, or manage event records.

## Objective
By understanding Event Data, you will be able to:
- Log and store structured data about events impacting registrants.
- Link these events to specific data entries, creating a clear audit trail.
- View and navigate the event history of a registrant from their profile.
- Manage different types of event data, allowing for flexible data collection and historical tracking.

## Process

### Overview of Event Data Functionality
The `spp_event_data` module is designed to:
- Provide a structured way to log and store data about events impacting registrants.
- Link these events to the specific data entries they affect, creating a clear audit trail.
- Offer tools to view and navigate the event history of a registrant.
- Store multiple versions of the data, manage separate data lifecycles and sharing agreements, better manage the source of different data, and store data that should not be visible to all users or that loses relevance over time.

### Key Features

1.  **Event Data Model (`spp.event.data`):** This new data model stores event-specific information. It includes fields to record event type, related document/record, registrar, collection date, optional expiry date, and event status (active/inactive).
2.  **Automatic Event Type Calculation:** The event type is dynamically determined and displayed based on the linked data model, providing a clear and user-friendly representation of the event.
3.  **Event History on Registrant Forms:** A dedicated tab is added to both individual and group registrant forms to display their associated event history, enabling users to directly access and review past events related to a specific registrant.
4.  **Event Creation Wizard:** A streamlined process for creating new event data entries through a dedicated wizard, simplifying data entry and ensuring consistency in event logging.
5.  **Active Event Management:** Logic is implemented to manage the active status of events. When a new active event of the same type is created for the same registrant, the previous one is automatically ended, providing a clear view of the current status.

### Integration with Program Membership Events:
The `spp_event_data_program_membership` module enhances OpenSPP by integrating the Event Data module (`spp_event_data`) with the G2P Programs module (`g2p_programs`). This allows users to record and track program membership-related events, such as enrollment, suspension, exit, and changes in eligibility status, and link them to specific program membership records.

### Demonstration and Examples (`spp_event_demo`)
The `spp_event_demo` module provides demonstration data and functionalities for the `spp_event_data` module. It showcases how to extend and utilize the event tracking capabilities of OpenSPP for specific use cases through:
* **Predefined Event Types:** Including House Visit (`spp.event.house.visit`), Phone Survey (`spp.event.phone.survey`), and School Enrollment Record (`spp.event.schoolenrollment.record`).
* **Data Models and Views:** Specific data models and user-friendly views for each event type.
* **Event Creation Wizards:** Dedicated wizards for creating new events like "Create Event: House Visit," "Create Event: Phone Survey," and "Create Event: School Enrollment".
* **Integration with Registrant Profiles:** Displays active events on registrant profiles for a quick overview.


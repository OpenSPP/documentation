---
orphan: true
---

# Event Data

The OpenSPP Event Data module is a core component for maintaining a comprehensive and chronological history of all significant actions and changes related to individual and group registrants within the OpenSPP system. It serves as an auditable log, tracking when and how key registrant information evolves.

## Purpose

The OpenSPP Event Data module provides essential capabilities for managing registrant data history:

*   **Centralized History**: Establishes a single, organized source for tracking all events associated with individual and group registrants. This ensures a complete timeline of their engagement with social protection programs.
*   **Data Versioning**: Manages the active status of registrant-related records, ensuring that OpenSPP always refers to the most current version of specific data (e.g., an ID, a phone number, or an enrollment status) at any given time.
*   **Auditability and Accountability**: Provides a clear, time-stamped record of changes, crucial for program transparency, compliance with regulations, and resolving data-related inquiries.
*   **Contextual Detail**: Links each event directly to the specific data record that was created or modified, offering immediate access to the full context of the change. This allows users to quickly understand the "what" and "why" behind an event.
*   **Operational Oversight**: Supports program managers and field agents in understanding the historical journey of each registrant, from initial registration to various program interventions or data updates, enabling informed decision-making.

## Dependencies and Integration

The OpenSPP Event Data module integrates deeply with the core registry modules to track changes to registrant profiles:

*   **[G2P Registry: Base](g2p_registry_base)**: This foundational module provides the `res.partner` model, which represents all registrants (individuals and groups). The Event Data module records events directly linked to these registrant records and other base components like identification documents, phone numbers, and relationships.
*   **[G2P Registry: Individual](g2p_registry_individual)**: When data specific to individual registrants (e.g., birthdate changes, gender updates, or new personal identifiers) is created or modified, the Event Data module tracks these events, linking them to the individual's profile.
*   **[G2P Registry: Group](g2p_registry_group)**: Similarly, for group registrants, the module logs events related to group types, membership changes, or other group-specific data, ensuring a complete history for collective entities.

This module acts as a historical ledger, receiving event notifications from these registry modules to build a comprehensive timeline of registrant data evolution.

## Additional Functionality

### Comprehensive Event Logging
The module automatically records a wide array of events, capturing significant actions taken on a registrant's profile. For instance, when a new identification document is added, a phone number is updated, or a relationship is established, the system logs a corresponding event. Each event includes the date of collection, the registrar who made the change, and its current state (active or inactive).

### Active Record Management
A key feature is its ability to manage the "active" state of various registrant-related data. When a new record of a certain type (e.g., a new primary ID) is created for a registrant, the system automatically sets any previously active record of that same type to "inactive." This ensures that OpenSPP always refers to the most current and relevant data for a registrant without losing the historical context. For example, if a registrant receives a new National ID, the old ID record can be automatically marked as inactive while still being part of the historical record.

### Direct Access to Event Details
Users can directly view the specific data record associated with any recorded event. From an event log entry, a user can click to open the full details of the linked record, such as the specific ID card, phone number, or relationship record that the event pertains to. This provides immediate context and allows for thorough investigation of historical data.

### Streamlined Event Creation
The module provides a user-friendly wizard directly accessible from a registrant's profile to create new events. This streamlines the process of adding new data points or marking significant changes, ensuring that all actions are properly logged and associated with the correct registrant.

## Conclusion

The OpenSPP Event Data module is indispensable for maintaining a transparent, auditable, and comprehensive historical record of all registrant-related data, ensuring data integrity and supporting robust program management within OpenSPP.
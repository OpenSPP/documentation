# G2P Notifications Rest Api

The G2P Notifications Rest Api module provides a secure and standardized API for managing beneficiary notification preferences within OpenSPP. It extends existing registrant and group management APIs to allow external systems to set and retrieve how individuals and group members prefer to receive program communications.

## Purpose

This module enables seamless integration for managing notification preferences, ensuring OpenSPP programs can respect beneficiary choices and communicate effectively. It accomplishes this by:

*   **Exposing Notification Preferences**: Allows external applications, such as beneficiary self-service portals or mobile apps, to read and update an individual's preferred notification channels (e.g., SMS, email, or none).
*   **Integrating with Registrant Data**: Extends the core registrant and group membership APIs to include notification preference as a standard field, ensuring consistency across data management.
*   **Supporting Beneficiary Opt-Outs**: Provides the capability to explicitly record when a beneficiary or group member prefers not to receive any notifications, enhancing privacy and user control.
*   **Enabling External Preference Management**: Empowers program administrators or integrated systems to centrally manage and update notification settings for large groups of beneficiaries.

## Dependencies and Integration

This module acts as an API extension, building upon foundational modules to expose notification preference management:

*   **[G2P Registry: Rest API Module](g2p_registry_rest_api)**: This module is a direct dependency, providing the base RESTful API endpoints for managing registrants and group memberships. The `g2p_notifications_rest_api` module extends the data models exposed by `g2p_registry_rest_api`, adding the `notification_preference` field to existing API endpoints for individual registrants and group members.
*   **[G2P Notifications Base](g2p_notifications_base)**: This foundational module handles the core logic for sending notifications and respecting preferences. While `g2p_notifications_rest_api` does not send notifications itself, it provides the API layer for external systems to *set* the preferences that `g2p_notifications_base` then uses when determining how and if to send communications.

## Additional Functionality

### Managing Individual Beneficiary Notification Preferences

External systems can use the extended API to retrieve or update the notification preferences for individual beneficiaries. This allows for dynamic management of how a registrant wishes to receive communications, such as "email," "sms," "both," or "none," directly through API calls. For example, a mobile app could allow a beneficiary to change their preference from SMS to email.

### Managing Group Member Notification Preferences

Similar to individual registrants, this module extends the API to manage notification preferences for members within a defined group. This ensures that group-level communications can also adhere to specific preferences set for each member, providing granular control over how information reaches all participants.

### Supporting Opt-Out Functionality

A key capability is the explicit support for a "none" preference. This allows beneficiaries, or systems on their behalf, to specify that no notifications should be sent to them. This is vital for respecting individual choices and complying with communication policies.

## Conclusion

The `g2p_notifications_rest_api` module is critical for enabling external systems to seamlessly manage and respect beneficiary notification preferences, enhancing communication transparency and control across OpenSPP programs.
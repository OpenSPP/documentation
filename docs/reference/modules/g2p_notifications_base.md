# G2P Notifications Base

The G2P Notifications Base module provides the foundational capabilities for sending automated communications to beneficiaries and other stakeholders within OpenSPP programs. It establishes the framework for managing and delivering timely, event-driven notifications via various channels, primarily email and SMS.

## Purpose

This module empowers OpenSPP to maintain transparent and efficient communication with beneficiaries by:

*   **Automating Critical Communications**: Automatically sends notifications for key program events, such as enrollment, payment disbursements, and One-Time Passcodes (OTPs).
*   **Supporting Multiple Channels**: Allows administrators to configure notification delivery via email, SMS, or both, catering to diverse beneficiary access needs.
*   **Enabling Customizable Messaging**: Provides flexible templates for each notification type, allowing program managers to tailor messages to specific program requirements and languages.
*   **Respecting Beneficiary Preferences**: Manages individual beneficiary preferences for how they wish to receive notifications, ensuring relevant and desired communication.
*   **Tracking Notification Status**: Records whether enrollment or payment notifications have been sent, preventing duplicate communications and aiding in audit trails.

## Dependencies and Integration

This module is a core extension for program operations, deeply integrating with other key OpenSPP modules:

*   **[G2P Programs](g2p_programs)**: This module extends the core program management functionality by adding the ability to define and trigger notifications for specific program events. It introduces notification managers directly into programs and enables the `G2P Program` to initiate mass notifications to eligible beneficiaries.
*   **Registrant Management**: It leverages `res.partner` (the base registrant model) to store and respect each beneficiary's preferred notification method (email, SMS, none, or both), and uses their contact information (email address, phone number) for delivery.
*   **Payment Processing**: Integrates with the payment management system to automatically trigger notifications when payments are successfully disbursed, informing beneficiaries of their received benefits.

## Additional Functionality

### Configurable Notification Managers

Administrators can set up distinct notification managers for email and SMS. These managers act as central points for defining how and when specific types of notifications are sent. Each manager can be configured with its own set of templates and sending rules.

### Event-Driven Notifications

The system automatically triggers notifications based on significant program events, ensuring beneficiaries are always informed:

*   **Program Enrollment**: Notifies beneficiaries upon their successful enrollment into a social protection program.
*   **Payment Disbursement**: Informs beneficiaries when a payment has been successfully sent to them.
*   **One-Time Passcode (OTP) Delivery**: Facilitates secure access by sending OTPs for verification purposes.
*   **Program Cycle Events**: Provides the framework to notify beneficiaries when a program cycle starts or ends (though specific implementation for these events may be completed in subsequent updates or related modules).

### Beneficiary Communication Preferences

Each registrant can specify their preferred method for receiving communications:

*   **None**: Opt-out of all automated notifications.
*   **Email**: Receive notifications via their registered email address.
*   **SMS**: Receive notifications via their registered mobile phone number.
*   **Both**: Receive notifications via both email and SMS, providing maximum reach.

These preferences are respected by the system when sending out any automated communication.

### Customizable Notification Templates

For each notification event (e.g., enrollment, payment, OTP), administrators can link specific email or SMS templates. This allows for highly flexible and localized messaging, ensuring that communications are clear, culturally appropriate, and contain all necessary information for the beneficiaries.

## Conclusion

The G2P Notifications Base module is crucial for fostering transparency and efficient communication within OpenSPP, ensuring beneficiaries receive timely and relevant information about their social protection programs. It establishes the essential infrastructure for automated, event-driven messaging, enhancing program reach and beneficiary engagement.
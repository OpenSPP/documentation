---
orphan: true
---

# G2P Notifications Fast2Sms

The G2P Notifications Fast2Sms module integrates OpenSPP programs with the Fast2SMS service, enabling the reliable and efficient delivery of SMS notifications to beneficiaries and other stakeholders. It extends the core notification framework to provide a dedicated gateway for sending text messages through a widely used third-party provider.

## Purpose

This module empowers OpenSPP programs to leverage the Fast2SMS platform for their communication needs by:

*   **Integrating with Fast2SMS**: Establishes a direct connection, allowing OpenSPP to send SMS messages via the Fast2SMS service provider. This expands the available channels for reaching beneficiaries.
*   **Ensuring Reliable SMS Delivery**: Provides a robust mechanism for dispatching critical program updates, payment alerts, and One-Time Passcodes (OTPs) directly to beneficiary mobile phones.
*   **Customizing SMS Sending Parameters**: Enables administrators to configure specific Fast2SMS parameters, such as the API endpoint, preferred SMS language, and message route. This tailors message delivery to service offerings.
*   **Securing API Access**: Manages the necessary authentication credentials (access tokens) required to securely connect and interact with the Fast2SMS API. This ensures only authorized communications are sent.
*   **Extending Base Notification Capabilities**: Provides a concrete and ready-to-use SMS implementation that plugs directly into the OpenSPP's foundational notification system.

## Dependencies and Integration

This module is a specialized extension that builds upon OpenSPP's core communication infrastructure.

*   **[G2P Notifications Base](g2p_notifications_base)**: This module serves as a concrete implementation for SMS delivery within the foundational `G2P Notifications Base` module. It registers itself as a specific SMS notification manager option, allowing program administrators to select Fast2SMS as their preferred SMS gateway for all program-related text communications.
*   **G2P Program Management**: By providing an active SMS channel, it enhances `G2P Programs` by ensuring that event-driven notifications, such as enrollment confirmations or payment disbursements, can be reliably sent to beneficiaries' mobile phones.

## Additional Functionality

### Fast2SMS Service Configuration

Administrators can easily configure the specific parameters for connecting to the Fast2SMS service. This includes defining the `Send API Endpoint`, which dictates the exact URL OpenSPP uses to send messages. This ensures flexibility in connecting to different Fast2SMS service regions or configurations.

### SMS Language and Route Customization

The module allows for detailed control over how messages are sent through Fast2SMS. Program managers can specify the `SMS Language` (e.g., "english", "hindi") for messages and select the appropriate `SMS Route` (e.g., "q" for quick transactional messages, "t" for promotional). This enables targeted and context-appropriate message delivery.

### Secure Access Token Management

To ensure secure communication with Fast2SMS, the module provides a dedicated field for storing the `Access Token`. This token is essential for authenticating OpenSPP's requests to the Fast2SMS API, safeguarding against unauthorized message sending and maintaining the integrity of program communications.

### Seamless SMS Dispatch

Once configured, the module transparently handles the technical process of sending SMS messages. It integrates with the `g2p_notifications_base` to take message content and beneficiary phone numbers, then formats and dispatches them through the Fast2SMS API, ensuring beneficiaries receive timely information.

## Conclusion

The G2P Notifications Fast2Sms module provides OpenSPP programs with a configurable and secure gateway to send essential SMS notifications via the Fast2SMS service, significantly enhancing direct and reliable beneficiary communication.
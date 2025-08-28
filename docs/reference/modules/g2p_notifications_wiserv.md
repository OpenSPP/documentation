# G2P Notifications Wiserv

The G2P Notifications Wiserv module integrates OpenSPP with the Wiserv SMS gateway, enabling the system to send automated SMS notifications to beneficiaries and other stakeholders through this specific service provider. It extends the core notification framework to offer Wiserv as a reliable channel for delivering critical program communications.

## Purpose

This module provides OpenSPP with a dedicated mechanism for sending SMS notifications via the Wiserv platform, ensuring timely and effective communication with beneficiaries. It specifically accomplishes the following:

*   **Enables Wiserv as an SMS Channel**: Configures OpenSPP to use the Wiserv SMS gateway for sending text messages, expanding the available communication options.
*   **Facilitates Automated Program Alerts**: Delivers automated SMS messages for crucial program events, such as enrollment confirmations, payment disbursement alerts, or One-Time Passcodes (OTPs).
*   **Manages Wiserv API Credentials**: Provides a secure interface for administrators to configure and manage the necessary API URL, username, and password for authenticating with the Wiserv service.
*   **Ensures Reliable SMS Delivery**: Handles the technical integration with the Wiserv API to transmit SMS messages, leveraging a specialized service for bulk messaging.
*   **Logs Communication Outcomes**: Records the responses from the Wiserv API, helping administrators monitor message delivery status and troubleshoot any transmission failures.

## Dependencies and Integration

This module is an essential extension of OpenSPP's communication capabilities, building upon the foundational notification framework.

It primarily depends on the `g2p_notifications_base` module, which establishes the core logic for managing notification types, templates, and preferences. The `g2p_notifications_wiserv` module extends this base by adding Wiserv as a concrete SMS sending method. When a program or system event triggers an SMS notification, `g2p_notifications_base` can then utilize the Wiserv integration provided here to send the actual message.

Additionally, this module leverages the `mail` module for its robust logging and activity tracking features. This allows OpenSPP to record details of SMS transmissions, including any errors or failures reported by the Wiserv API, directly within the system for audit and troubleshooting purposes. This integration ensures that notification attempts and outcomes are visible to program administrators.

## Additional Functionality

### Wiserv SMS Gateway Configuration

Administrators can easily configure the Wiserv SMS service within OpenSPP. This involves entering the specific API URL, username, and password provided by Wiserv. Proper configuration is essential for the module to successfully connect and send messages through the Wiserv platform, ensuring secure and authorized communication.

### Automated SMS Delivery

Once configured, the module enables OpenSPP to automatically send SMS notifications for various program events. These include informing beneficiaries about successful enrollment in a program, confirming payment disbursements, or providing critical security information like One-Time Passcodes. Messages are sent to the phone numbers registered for beneficiaries, respecting their communication preferences.

### Error Handling and Logging

The module includes robust error handling to manage potential issues during SMS transmission. If the Wiserv API reports an error (e.g., invalid credentials, service unavailability), the system logs these failures. This provides administrators with crucial insights into why a message might not have been delivered, allowing for prompt investigation and resolution.

### Beneficiary Communication Preferences

This module works in conjunction with the base notification system to respect beneficiary communication preferences. SMS messages are only sent to beneficiaries who have opted to receive notifications via phone, ensuring that communications are relevant and desired.

## Conclusion

The G2P Notifications Wiserv module is vital for OpenSPP, providing a dedicated and reliable channel for sending automated SMS communications to beneficiaries through the Wiserv service. It enhances program transparency and ensures that critical information reaches beneficiaries efficiently.
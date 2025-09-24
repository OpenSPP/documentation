# Incoming email configuration

Configuring an incoming email server allows OpenSPP to fetch emails from a dedicated mailbox and process them automatically. This is a powerful feature that can create or update records based on the content of the emails. For example, an email sent to `support@youremailserver.com` could automatically create a new Grievance ticket.

## Prerequisites

To configure an incoming email server, you will need:
- A user account with **System Admin** role. For details on user roles and access levels, refer to the {doc}`user_access` documentation.
- The connection details for your IMAP or POP email server:
    - Server type (IMAP or POP)
    - Server address (e.g., `imap.youremailserver.com`)
    - Server port (e.g., 993 for IMAP with SSL/TLS)
    - Whether SSL/TLS is required
    - Username and password for the dedicated email account.

## Objective

After completing this section, you will be able to configure OpenSPP to fetch emails from a mailbox and create new records automatically.

## Process

The process is similar to configuring an outgoing server, involving developer mode and navigating to the technical settings.

### Activate developer mode

If you have not already, activate developer mode to access the technical settings.

### Navigate to incoming email servers

1.  Go back to the main **Settings** page.
2.  Click on the **Technical** menu in the header.
3.  Under the **Email** section, click on **Incoming Email Servers**.

![Technical menu dropdown showing the Email section with 'Incoming Email Servers' option highlighted](incoming_email_configuration/B-step02-open-incoming-email-servers.jpg)

### Create a new server configuration

1.  On the **Incoming Email Servers** page, click the **New** button.

![Incoming Email Servers list page with the 'New' button highlighted to create a new server configuration](incoming_email_configuration/B-step03-create-new-incoming-email-server.jpg)

This will open a form to enter your incoming server details.

### Fill in server details

Fill in the form with the details for the mailbox you want OpenSPP to monitor.

- **Name**: A descriptive name, e.g., `Grievance Mailbox`.
- **Server Type**: Choose `IMAP Server` or `POP Server`. IMAP is generally recommended.
- **Server Name**: Enter your server's address, e.g., `imap.youremailserver.com`.
- **Port**: Enter the correct port number (e.g., `993` for IMAP).
- **SSL/TLS**: Check this box if your server uses SSL/TLS encryption.
- **Username**: The full email address of the mailbox.
- **Password**: The password for the email account.
- **Action to Perform on Incoming Mails**: Select `Create a new Record`.
- **Create a New Record**: This is a critical field. Select the type of record you want to create from incoming emails. For example, you could select `Grievance` if you have a grievance module installed. The available options depend on the modules installed in your system.

![IMAP/POP server configuration form showing fields for Name, Server Type, Server Name, Port, SSL/TLS, Username, Password, and Action settings](incoming_email_configuration/B-step04-fill-in-server-details.jpg)

### Test and save

1.  Click the **Test & Confirm** button.
2.  OpenSPP will attempt to connect to the mailbox. If successful, you will see a confirmation.
3.  If there is an error, re-check all your server settings.
4.  Once the test is successful, click **Save**.

![Completed incoming email server configuration form with 'Test & Confirm' and 'Save' buttons highlighted](incoming_email_configuration/B-step05-test-and-save-config.jpg)

OpenSPP will now periodically check this mailbox for new emails and create records based on your configuration.

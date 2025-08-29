---
review-status: reviewed
review-date: 2025-07-08
reviewer: Mark Penalosa
migration-notes: "Added during 2025 documentation reorganization"
---

# Change Requests

## Introduction

This guide explains how to update registrant information in OpenSPP using the Change Request module. The process follows a defined workflow, requiring users with specific roles to initiate and validate requests. Permission-based access and thorough documentation help ensure data accuracy and reliable operations.

## Prerequisites

Before submitting or approving change requests, ensure the following:
- Have existing individual records in your registry, either by creating records manually {doc}`register_individual` or importing records into OpenSPP {doc}`import_export_registrant_data`.
- Assign appropriate roles to Change Request validators. You can learn how to perform these tasks in the {doc}`../administration/user_access` document under the **Configuring Roles** section:
  - **Local Validator**: Add the group name under the Groups tab: `Change Request Module Access / Change Request Validator Local`.
  - **HQ Validator**: Add the group name under the Groups tab: `Change Request Module Access / Change Request Validator HQ`.
- Install the Change Request Module.
  1. Log in as Administrator. Then navigate to Apps.

    ![](using_change_request/change_request_app_menu.png)

  2. Search OpenSPP Change Request and click install. Once installed, the page should refresh, then Activate button should disappear.

    ![](using_change_request/change_request_install_module.png)

  3. This indicates that the module has been installed successfully.

## Objective

After completing this tutorial, you will be able to:
- Submit and validate change requests for registrant data.
- Navigate role-specific approval workflows.
- Attach supporting documentation and track updates efficiently.

## Process

To update a registry record, a change request is initiated by a System Administrator or Registrar. The request is drafted, applicant information is updated for validation, and supporting documents are attached to have a reference for the updating of information. Once submitted, the request undergoes validation by a Local Validator. If approved, it proceeds to an HQ Validator for final review. Upon HQ validation, the change request is applied to the applicant’s record and can be verified through the registry.

### Creating a Change Request draft

Login as System Administrator or Registrar, then from the menu, click on **Change Request**.

   ![](using_change_request/change_request_change_request_page.png)

From the Change request page, click the **New** button. Then fill in the request details:
- Request Type: Select Change Information.
- Registrant: Choose the registrant initiating the request.
- Applicant: Select the registrant whose data will be changed.
- Phone Number: Enter the registrant's contact number.

Click **Create** to proceed. Clicking Create will generate a draft file for your change request.

 ![](using_change_request/change_request_create_button.png)

#### Updating Applicant Information

From the Change request page, select a **Change request** file currently in Draft state.

![](using_change_request/change_request_list_of_requests.png)

Click **Next**, then fill in the necessary fields.

* **Family Name** and **Given Name** are required.  
  * Input directly into the field data you wish to update.  
  * If you do not wish to update the field, leave it blank.

Please note that more fields may be displayed here depending on the specific configuration for your OpenSPP instance.

Navigate to the **Attachments** tab:

* Click **Request Form** *(required) then upload your file related with your information request.*  
* Optionally, attach **Birth Certificate** or **Other Documents** as reference for your change request update.

 ![](using_change_request/change_request_attachment_tabs.png)

Click **Request Validation** to submit for approval.

### Validation Workflow

#### Review request by Local Validator Role

Log in using a **Local Validator** user account then go to **Change Request**.

Select the request and click **Assign to me**.

![](using_change_request/change_request_assign_to_local_validator.png)

Review **Request details** and **Attachment** for uploaded files as reference for the change request. Alternatively, you can review uploaded files in DMS (Directory Management System) feature. Learn more in this guide: {doc}`dms`

![](using_change_request/change_request_review_change_information.png)

Click **Validate** to partially approve the change request. A success notification will appear upon approval. Otherwise, click reject to negate and cancel change request.

![](using_change_request/change_request_success_partial.png)

Partially approved change requests are then reviewed by users with HQ validator roles.

#### Review request by HQ Validator Role

Log in using a **HQ Validator** user account then go to **Change Request**.

Select a change request, review **Request details** and **Attachment** for uploaded files as reference for the change request. Alternatively, you can review uploaded files in DMS (Directory Management System) feature. Learn more in this guide: {doc}`dms`

![](using_change_request/change_request_review_change_information_as_hq.png)

Click **Validate** to completely approve the change request. A success notification will appear upon approval. Otherwise, click reject to negate and cancel change request.

![](using_change_request/change_request_success_complete.png)

Change requests approved by **HQ validator** users are applied directly to the applicant’s records.

- Please note that change requests may be rejected by the **HQ validator** user even if they haven't been approved by a local validator user.  
- Please note that change requests cannot be validated by the **HQ validator** user unless they have been pre-validated by a **local validator** user.

###  Reviewing Changes

Log back in as Administrator or Registrar and go to Registry→Individual.

Click **search filter** dropdown.

![](using_change_request/change_request_search_filter.png)

Click on **Add Custom Filter**.

- Filter by **Last Updated By \-**  to search by validator name. Define the relational operators. Then click on Add.  
 
 ![](using_change_request/change_request_last_updated_by.png)

- Filter by **Last Updated On \-**  to search by updated date. Define the relational operators. Then click on Add.  

![](using_change_request/change_request_last_updated_on.png)

Verify that registrant changes are reflected in their profile.

![](using_change_request/change_request_review_updated_information.png)
---
review-status: reviewed
review-date: 2025-07-29
reviewer: mark penalosa
migration-notes: "Added during 2025 documentation reorganization"
---

# Enrol beneficiaries

In this tutorial, you will learn the process of enrolling beneficiaries in OpenSPP. Accurate beneficiary enrolment ensures that the right individuals or groups receive the intended benefits.

## Prerequisites

To enrol beneficiaries in OpenSPP, you need an existing program. Learn more about how to configure a program in the documentation {doc}`create_program`.

## Objective

This tutorial instructs users on how to enrol beneficiaries into a program in OpenSPP. By following these procedures, users will be able to import and enrol both individual and group beneficiaries, ensuring they are registered for the necessary support and benefits. Upon completion, users will have successfully added eligible beneficiaries to their respective social protection programs.

## Process

Efficient enrolment is important for the success of social protection programs in OpenSPP. Depending on the target type, the enrolment is done for groups or individuals. Both enrolments can be done either as part of the program setup or after configuring the program. The process of creating a social protection program is described in the documentation Create a social protection program.

### Beneficiary Import and Enrolment

Upon finalizing the creation of the program, the process progresses through two sequential stages, regardless of whether the program supports individual or group beneficiaries:

- Import beneficiaries. This step involves the integration of beneficiaries who are eligible to receive support from a social protection program. Which beneficiaries to import into the program are defined by the filter in the eligibility criteria.
- Enrol beneficiaries. After the beneficiaries have been imported into the system, the next step is to enrol them in the program. Enrolment involves verifying the eligibility of each beneficiary based on the program's criteria, such as income level, age, or other factors. Once a beneficiary is enrolled in the program, they are entitled to receive the benefits or services provided by the program

Depending on the choices made in the program setup, there are two different ways to perform these steps, both of them are described below.

### Import and Enrolment as part of Program Setup

If **Yes** is selected during the final step of program setup, both the beneficiary **import** and **enrolment** processes are automatically executed as part of program creation.

![](enrol_beneficiaries/enrol_beneficiaries_auto_enrol.png)

Once completed, the number of beneficiaries imported and enrolled is displayed on the toolbar.

![](enrol_beneficiaries/enrol_beneficiaries_enrolled.png)

Click the **Beneficiaries** button to view the imported and enrolled beneficiaries in the table view.

![](enrol_beneficiaries/2.png)

This confirms that the beneficiaries are imported and enrolled.

### Import and Enrolment after Program Creation

If the option **No** has been selected as the final step of the program setup, both Import and Enrol steps needs to be done as a separate action prior to proceeding.

This action consists of two steps, first the import of registrants into the program, and then the enrolment of the previously imported registrants into the program.

To import registrants into a program manually, Select the program you wish to import registrants into, then click on **Import new Eligible Registrants button**

![](enrol_beneficiaries/enrol_beneficiaries_manual_import.png)

A success notification should prompt

![](enrol_beneficiaries/enrol_beneficiaries_import_notification.png)

**Note:** The number displayed on the **Beneficiaries** button reflects the total count of beneficiaries who have been successfully enrolled in the program. This does not represent the number of registrants imported.

![](enrol_beneficiaries/enrol_beneficiaries_count.png)

Please note that when potentially large volume of beneficiaries are being imported, it is essential to ensure that the import process has fully completed prior to initiating enrolment. This precaution helps prevent any issues during the enrolment phase.

In the case of less than 1000 beneficiaries, a green pop-up will appear on the right side of the screen, indicating that the import process is complete and beneficiaries have already imported. The time it takes to import the beneficiaries will depend on the number of beneficiaries eligible for the program, and it is vital to allow the import to complete before proceeding.

![](enrol_beneficiaries/enrol_beneficiaries_success_import.png)

In the case of more than 1000 beneficiaries, a yellow notification will display informing that the page needs to be refreshed to see the status of the import.

![](enrol_beneficiaries/4.png)

To manually enrol registrants into a program, first confirm that the import process has been completed. This can be verified by observing the green notification popup for fewer than 1000 beneficiaries, or, for more than 1000 beneficiaries, by refreshing the page until the yellow notification popup is no longer displayed. Once confirmation is received, proceed and click **Enrol Eligible Registrants**.

![](enrol_beneficiaries/enrol_beneficiaries_enrol_beneficiaries_button.png)

If there are a large number of records to process, a yellow notification will appear on the right side of the screen to indicate that enrolment is in progress. After enrolment for all participants is complete, refresh the page. If the warning message disappears or a success notification is displayed, this confirms that the enrolment process has finished.

![](enrol_beneficiaries/5.png)

The number of beneficiaries imported and enrolled is displayed on the **Beneficiaries** icon.

![](enrol_beneficiaries/enrol_beneficiaries_count.png)

You should also check the beneficiary page to verify that the beneficiaries are there. Click the **Beneficiaries** button to view the imported and enrolled beneficiaries in the table view.

![](enrol_beneficiaries/enrol_beneficiaries_list.png)

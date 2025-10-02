---
myst:
  html_meta:
    "title": "Point of Sales (POS) system usage"
    "description": "Learn how to configure and use the OpenSPP Point of Sales system for beneficiary transactions, including web and mobile interfaces, refunds, and area grouping."
    "keywords": "OpenSPP, Point of Sales, POS, beneficiary transactions, cash disbursement, refunds, mobile POS"
---

# Point of Sales

In this tutorial, you will learn about the POS feature, covering configuration, creating point of sales, and setting it by area.

## Prerequisites

To utilise this feature, you need the following:

- Make sure that both modules **OpenSPP POS: ID Redemption** and **OpenSPP POS** are installed and activated.
  For details on installing additional modules, refer to the {doc}`../../getting_started/module_installation` documentation.
- Have existing individual records in your registry, either by creating records manually or importing records into OpenSPP.
- Have an access role either as **System Admin** or **POS operator** to perform tasks in the POS application.
- Have an access role as **System Admin** to perform tasks in OpenSPP.
  Learn more about assigning user role in the guide {doc}`administration/user_access`.
- Have an existing cycle with beneficiaries and entitlements generated on a program.
  Learn more about this in the guide {doc}`program_management/create_program`.

## Objective

By the end of this tutorial, you will be able to configure point of sales, manage, classify by area, and generate transactions within the POS feature.

## Process

### Verify POS module

To be able to create point of sales, you have to make sure that the necessary modules are installed and activated on your OpenSPP instance.
This can be verified by logging in to your OpenSPP instance as Administrator, go to **Apps**, search for **OpenSPP POS** and **OpenSPP POS: ID Redemption** respectively and if not already done, activate them by clicking **Activate** button.

![OpenSPP POS module activation screen showing both POS modules with Activate buttons](point_of_sales/POS_module.png)

Upon successful activation, the button label should change to **Learn more**.

### Configure POS Settings

Navigate to the menu screen.
On the sidebar menu, click **Point of Sale** to open the POS dashboard.

![Point of Sale dashboard showing configured POS stations in a table format](point_of_sales/point_of_sales_table.png)

Click on **Configuration** and select **Payment methods** to see the payment methods available.
By default, the options **Cash**, **Bank** and **Customer Account** are available.

![Payment methods configuration screen showing Cash, Bank, and Customer Account options](point_of_sales/point_of_sales_payment_methods.png)

#### Create point of sales

To create a point of sale, click on **Point of Sales** from the sidebar, click **Configuration** and select **Point of Sales**, then click on **New**.

![Point of Sales configuration screen with New button highlighted](point_of_sales/point_of_sales_create_pos.png)

Assign a name to the point of sale you want to create.
It is also possible to assign the shop to a specific area by selecting the desired area from the dropdown.
Click on **Save** button to keep the changes.

![Point of Sale creation form with name field and area dropdown selection](point_of_sales/point_of_sales_save.png)

#### Select payment methods

To select a payment method for your point of sale, click on **Point of Sales** from the sidebar, navigate to **Configuration** and click on **Settings**.
From the **Point of Sale** dropdown, click and select the point of sale you want to manage.

![Point of Sale settings screen with dropdown to select specific POS station](point_of_sales/point_of_sales_select_pos.png)

Once you have selected a point of sale, click on the dropdown from **Payment methods** and select the desired payment methods for this point of sale.
Click the **Save** button to keep the changes.

Please Note: For **Cash** payment method a unique payment method needs to be created for each point of sale.
In order to create a new **Cash** payment method, navigate to **Point of Sale**, click on **Configuration** and select **Payment methods**, then click **New**.

![New payment method creation screen with form fields](point_of_sales/point_of_sales_new_payment_method.png)

Define the name of the payment method and click on the Journal Input field.

![Payment method form with name field and Journal dropdown](point_of_sales/point_of_sales_define_payment_method.png)

Click on **Search More** from the dropdown.

![Journal selection dropdown with Search More option highlighted](point_of_sales/point_of_sales_search_more.png)

Click on **New** button.

![Journal creation dialog with New button](point_of_sales/point_of_sales_new_journal.png)

Define the **Journal name**, then select **Cash** under **Type** dropdown.
To complete the journal creation, click **Save & Close**.

![Journal creation form with name field, Cash type selection, and Save & Close button](point_of_sales/point_of_sales_save_journal.png)

You may now select the new Cash payment method for a point of sale.
Navigate to **Configuration** and click on **Settings**.
Select a **Point of sale**.
Then under payment methods dropdown, select your new Cash payment method and click **Save**.

![POS settings screen showing new Cash payment method selected in dropdown](point_of_sales/point_of_sales_new_cash_payment_method.png)

#### Group point of sales by area

In order to group point of sales by area, make sure you have areas already existing in your OpenSPP instance.
Learn more about importing areas in the guide {doc}`administration/import_areas`.
From the sidebar, navigate to **Point of Sale**, select **Configuration** and click **Point of Sales**.
Select the point of sale you wish to manage and assign by clicking an area from the dropdown **Area**.

![POS configuration screen with Area dropdown showing available areas for assignment](point_of_sales/point_of_sales_select_area.png)

Navigate to **Point of Sale** and select **Dashboard**.
The point of sales will now be grouped by area.

![POS dashboard showing point of sales organized by geographical areas](point_of_sales/point_of_sales_grouped_by_area.png)

Point of sales that do not belong to any area will display as minimized.
Click the **<>** arrows from the dashboard to expand the view.
Click on **Gear** icon to collapse view.

![POS dashboard with expand/collapse arrows and gear icon for view options](point_of_sales/point_of_sales_view_options.png)

### Starting point of sale in web view

The POS application is viewable in either web view or mobile view.
This section will be covering the web view, for mobile view, proceed to **Starting point of sale in mobile view** of this document.

The POS application can be operated by either an **Administrator** or a **POS Operator** role.

To start the point of sale, click on **Point of Sale** in the sidebar.
You should be redirected to the **Dashboard**, where you can select the point of sale you wish to start.

![POS dashboard displaying available point of sales with New Session buttons](point_of_sales/16.png)

Click on **New Session** to be redirected to the POS application, then click on **Beneficiary** to display the list of beneficiaries.

![POS application interface with Beneficiary button highlighted on the main screen](point_of_sales/17.png)

Click on the beneficiary you wish to transact with.

![Beneficiary selection dialog showing list of registered beneficiaries](point_of_sales/18.png)

Once selected, the beneficiary's name will be displayed in the POS application.

![POS interface displaying selected beneficiary name in the transaction area](point_of_sales/19.png)

Click on the **Entitlement** button to display all the entitlements available for this beneficiary.

![Entitlement selection dialog showing available entitlements for the selected beneficiary](point_of_sales/20.png)

Select the entitlement you wish to disburse by clicking on it.
Then click **Close** button.

![POS interface showing selected entitlement with Close button visible](point_of_sales/21.png)

Click on **Payment** button to proceed.

![POS payment screen with payment method options and transaction details](point_of_sales/22.png)

Click on **Validate** button to complete.

![POS validation screen with Validate button to complete the transaction](point_of_sales/23.png)

The transaction is now complete.
If you wish to start a new transaction, click on **New Order**.

![POS completion screen showing transaction success with New Order button](point_of_sales/24.png)

### Starting point of sale in mobile view

The POS application is viewable in either web view or mobile view.
This section will cover the mobile view, for web view, proceed to **Starting point of sale in web view** of this document.

Click on the upper left box icon to bring up the menu, then click **Point of Sale**.

![Mobile menu interface with hamburger icon and Point of Sale option](point_of_sales/25.png)

You will be taken to the **Dashboard**.
Select a point of sale you wish to start by swiping horizontally and click on **New Session**.

![Mobile POS dashboard with swipeable point of sale cards and New Session button](point_of_sales/26.png)

Click on **Review**.

![Mobile POS Review screen with transaction overview and navigation options](point_of_sales/27.png)

Then click on **Beneficiary** to display a list of beneficiaries.

![Mobile beneficiary selection screen with Beneficiary button highlighted](point_of_sales/28.png)

Click on the relevant beneficiary in the displayed list.

![Mobile beneficiary list showing registered beneficiaries for selection](point_of_sales/29.png)

Once selected, the beneficiary's name is displayed in the POS application.

![Mobile POS interface showing selected beneficiary name in the transaction area](point_of_sales/30.png)

Click on **More** and then **Entitlement** to display available entitlements for this beneficiary.

![Mobile POS More menu with Entitlement option visible](point_of_sales/31.png)

Click on the entitlement you wish to disburse and click the **Close** button.

![Mobile entitlement selection screen showing available entitlements with Close button](point_of_sales/32.png)

Optionally, you may add a note by clicking on **More** followed by **Beneficiary note**.
Fill in the note and click on **Add** button.
This note will be displayed on the receipt.

![Mobile beneficiary note interface with text field and Add button](point_of_sales/33.png)

Click on the **Payment** button to proceed.

![Mobile POS payment screen showing transaction details and payment options](point_of_sales/34.png)

Click on the **Validate** button to complete.

![Mobile POS validation screen with Validate button to complete transaction](point_of_sales/35.png)

The order or transaction is now complete.
Click on **New Order** to start a new transaction.

![Mobile POS completion screen showing successful transaction with New Order button](point_of_sales/36.png)

### Refunds

When necessary, it is possible to do refunds for cash entitlements.
To start a refund, click on a point of sale and select a beneficiary.
Click on **Refund**.

![Mobile POS refund interface with beneficiary selected and Refund button](point_of_sales/37.png)

The orders/transactions associated with the beneficiary will be displayed.
Click on any transaction to view the details on the right side.

![Mobile transaction history screen showing beneficiary's past transactions](point_of_sales/38.png)

Click on an item.
You may only refund items that are disbursed, indicated by the negative (-) sign beside its amount.

![Mobile transaction details showing refundable items with negative amounts](point_of_sales/39.png)

Note that if an item has been already refunded, it will display **Refunded** and you will be unable to click it anymore.

![Mobile transaction details showing previously refunded item marked as Refunded](point_of_sales/40.png)

Upon clicking the item, click **1** from the number pad key and then click on the **Refund** button.

![Mobile refund screen with number pad and Refund button for amount selection](point_of_sales/41.png)

The item to be refunded will be displayed on the menu.
Click on **Payment**.

![Mobile refund payment screen showing item to be refunded with Payment button](point_of_sales/42.png)

Select a payment method and click **Validate**.
This completes the refund process.

![Mobile refund validation screen with payment method selection and Validate button](point_of_sales/43.png)

To verify that the item was successfully refunded you can click on the burger menu on the top right corner of the screen.

![Mobile POS interface with hamburger menu in top right corner](point_of_sales/44.png)

Click on **Orders**.
You will be redirected to the screen below.
Click on **All active orders** and select **Paid**.

![Mobile orders screen with filter options showing All active orders and Paid status](point_of_sales/45.png)

Click on the transaction that involves the refund and notice that the amount is now a positive value indicating that the cash entitlement has been successfully refunded.

![Mobile transaction details showing completed refund with positive amount value](point_of_sales/46.png)

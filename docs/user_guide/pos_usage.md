---
review-status: Reviewed
review-date: 2025-07-10
reviewer: Mark Penalosa
migration-notes: "Added during 2025 documentation reorganization"
---

# Point of Sales

In this Tutorial, you will learn about the POS feature; covering configuration, creating Point of sales and setting it by area.

## Prerequisites

To utilise this feature, you need the following:

- Make sure that both modules **OpenSPP POS: ID Redemption** and **OpenSPP POS** are installed and activated. For details on installing additional modules, refer to the {doc}`../../getting_started/module_installation` documentation.
- Have existing individual records in your registry, either by creating records manually or importing records into OpenSPP.
- Have an access role either as **System Admin** or **POS operator** to perform tasks in the POS Application.
- Have an access role as  **System Admin** to perform tasks in OpenSPP. Learn more about assigning user role in the guide {doc}`administration/user_access`
- Have an existing cycle with beneficiaries and entitlements generated on a program. Learn more about this in the guide {doc}`program_management/create_program`

## Objective

By the end of this Tutorial, you will be able to configure Point of sales, manage, classify by area, and generate transactions within the POS feature.

## Process

### Verify POS module

To be able to create Point of sales, you have to make sure that the necessary modules are installed and activated on your OpenSPP instance, this can be verified by logging in to your OpenSPP instance as Administrator, go to **Apps**, search for **OpenSPP POS** and **OpenSPP POS: ID Redemption** respectively and if not already done, activate them by clicking **Activate** button.

![](point_of_sales/POS_module.png)

Upon successful activation, the button label should change to **Learn more**.

### Configure POS Settings

Navigate to the menu screen. On the sidebar menu, click **Point of Sale** to open the POS dashboard.

![](point_of_sales/point_of_sales_table.png)

Click on **Configuration** and select **Payment methods** to see the payment methods available. By default, the options **Cash**, **Bank** and **Customer Account** are available.

![](point_of_sales/point_of_sales_payment_methods.png)

#### Create Point of sales

To create a Point of sale, click on **Point of Sales** from the sidebar, click **Configuration** and select **Point of Sales,** then click on **New**.

![](point_of_sales/point_of_sales_create_pos.png)

Assign a name to the Point of Sale you want to create. It is also possible to assign the shop to a specific area by selecting the desired area from the dropdown. Click on **Save** button to keep the changes.

![](point_of_sales/point_of_sales_save.png)

#### Select Payment methods

To select a payment method for your Point of sale, click on **Point of Sales** from the sidebar, navigate to **Configuration** and click on **Settings.** From the **Point of Sale** dropdown, click and select the Point of sale you want to manage.

![](point_of_sales/point_of_sales_select_pos.png)

Once you have selected a Point of sale, click on the dropdown from **Payment methods** and select the desired payment methods for this Point of sale. Click the **Save** button to keep the changes.

Please Note: For **Cash** payment method a unique payment method needs to be created for each Point of sale. In order to create a new **Cash** Payment method, navigate to **Point of Sale**, click on **Configuration** and select **Payment methods**, then click **New**.

![](point_of_sales/point_of_sales_new_payment_method.png)

Define the name of the Payment method and click on the Journal Input field.

![](point_of_sales/point_of_sales_define_payment_method.png)

Click on **Search More** from the dropdown.

![](point_of_sales/point_of_sales_search_more.png)

Click on **New** button.

![](point_of_sales/point_of_sales_new_journal.png)

Define the **Journal name**, then select **Cash** under **Type** dropdown. To complete the journal creation, click **Save & Close.**

![](point_of_sales/point_of_sales_save_journal.png)

You may now select the new Cash payment method for a Point of sale. Navigate to **Configuration** and click on **Settings**. Select a **Point of sale**. Then under payment methods dropdown, select your new Cash payment method and click **Save**.

![](point_of_sales/point_of_sales_new_cash_payment_method.png)

#### Group Point of sales by area

In order to group Point of sales by area, make sure you have areas already existing in your OpenSPP instance. Learn more about importing areas in the guide {doc}`administration/import_areas`. From the sidebar, navigate to **Point of Sale**, select **Configuration** and click **Point of Sales**. Select the Point of sale you wish to manage and assign by clicking an area from the dropdown **Area**.

![](point_of_sales/point_of_sales_select_area.png)

Navigate to **Point of Sale** and select **Dashboard**. The Point of sales will now be grouped by Area.

![](point_of_sales/point_of_sales_grouped_by_area.png)

Point of sales that do not belong to any area will display as minimized. Click the **<>** arrows from the dashboard to expand the view. Click on **Gear** icon to Collapse view.

![](point_of_sales/point_of_sales_view_options.png)

### Starting Point of sale in Web view

The POS application is viewable in either web view or mobile view, this section will be covering the web view, for mobile view, proceed to **Starting Point of sale in Mobile view** of this document.

The POS application can be operated by either an **Administrator** or a **POS Operator** role.

To start the Point of sale, click on **Point of Sale** in the sidebar. You should be redirected to the **Dashboard**, where you can select the Point of sale you wish to start.

![](point_of_sales/16.png)

Click on **New Session** to be redirected to the POS Application, then click on **Beneficiary** to display the list of Beneficiaries.

![](point_of_sales/17.png)

Click on the Beneficiary you wish to transact with.

![](point_of_sales/18.png)

Once selected, the beneficiary's name will be displayed in the POS application.

![](point_of_sales/19.png)

Click on the **Entitlement** button to display all the entitlements available for this Beneficiary.

![](point_of_sales/20.png)

Select the entitlement you wish to disburse by clicking on it. Then click **Close** button.

![](point_of_sales/21.png)

Click on **Payment** button to proceed.

![](point_of_sales/22.png)

Click on **Validate** button to complete.

![](point_of_sales/23.png)

The transaction is now complete. If you wish to start a new transaction, click on **New Order**.

![](point_of_sales/24.png)

### Starting Point of sale in Mobile view

The POS application is viewable in either web view or mobile view. This section will cover the Mobile view, for Web view, proceed to **Starting Point of sale in Web view** of this document

Click on the upper left box icon to bring up the menu, then click **Point of Sale.**

![](point_of_sales/25.png)

You will be taken to the **Dashboard**. Select a Point of sale you wish to start by swiping horizontally and click on **New Session.**

![](point_of_sales/26.png)

Click on **Review**

![](point_of_sales/27.png)

Then click on **Beneficiary** to display a list of beneficiaries.

![](point_of_sales/28.png)

Click on the relevant beneficiary in the displayed list.

![](point_of_sales/29.png)

Once selected, the beneficiary's name is displayed in the POS application.

![](point_of_sales/30.png)

Click on **More** and then **Entitlement** to display available entitlements for this beneficiary.

![](point_of_sales/31.png)

Click on the entitlement you wish to disburse and click the **Close** button.

![](point_of_sales/32.png)

Optionally, you may add a note by clicking on **More** followed by **Beneficiary note**. Fill in the note and click on **Add** button. This note will be displayed on the receipt.

![](point_of_sales/33.png)

Click on the **Payment** button to proceed.

![](point_of_sales/34.png)

Click on the **Validate** button to complete.

![](point_of_sales/35.png)

The order or transaction is now complete. Click on **New Order** to start a new transaction.

![](point_of_sales/36.png)

### Refunds

When necessary, it is possible to do refunds for cash entitlements. To start a refund, click on a Point of sale and select a beneficiary. Click on **Refund**.

![](point_of_sales/37.png)

The orders/transactions associated with the beneficiary will be displayed. Click on any transaction to view the details on the right side.

![](point_of_sales/38.png)

Click on an item. You may only refund items that are disbursed, indicated by the negative (-) sign beside its amount.

![](point_of_sales/39.png)

Note that If an item has been already refunded, it will display **Refunded** and you will be unable to click it anymore.

![](point_of_sales/40.png)

Upon clicking the item, click **1** from the number pad key and then click on the **Refund** button.

![](point_of_sales/41.png)

The item to be refunded will be displayed on the menu. Click on **Payment.**

![](point_of_sales/42.png)

Select a payment method and click **Validate.** This completes the refund process.

![](point_of_sales/43.png)

To verify that the item was successfully refunded you can click on the burger menu on the top right corner of the screen.

![](point_of_sales/44.png)

Click on **Orders**. You will be redirected to the screen below. Click on **All active orders** and select **Paid**

![](point_of_sales/45.png)

Click on the Transaction that involves the Refund and notice that the amount is now a positive value indicating that the cash entitlement has been successful.

![](point_of_sales/46.png)

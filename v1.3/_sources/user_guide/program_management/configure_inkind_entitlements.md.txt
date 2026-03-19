---
myst:
  html_meta:
    "title": "Configure in-kind entitlements"
    "description": "Complete guide for setting up in-kind entitlements in OpenSPP, including product management and program configuration."
    "keywords": "OpenSPP, in-kind entitlements, products, inventory, program configuration"
---

# Configure in-kind entitlements

This guide includes steps for approving in-kind entitlements and preparing cycles with in-kind entitlements.

## Prerequisites
- Ensure you have the appropriate user permissions, such as **Global Registry** or **System Admin** roles. For details on user roles and access levels, refer to the {doc}`../administration/user_access` documentation.
- Create a Program or have an already existing program. Learn more about this in the guide {doc}`create_program`.
- Install the module: **OpenSPP In-Kind Entitlement** on your OpenSPP instance as **System Admin**. Learn more on installing modules in the guide: {doc}`../../getting_started/module_installation`.


## Objective

This guide will enable you to effectively set up and manage in-kind entitlements in OpenSPP. By the end of this tutorial, you will be able to define the products for distribution, configure their quantities, and link them to your programs to ensure accurate and efficient benefit delivery.

## Process

### Create in-kind entitlements

Login as **System Admin**, and navigate to Inventory from the sidebar.
If it is not visible, you must enable the checkbox **Show Non-OpenSPP Menu** from the **Access Rights** tab of this User.

![Access rights tab](configure_inkind_entitlements/access_rights_tab.png)

 To edit this Access right tab, you must enable developer mode as show in the guide: {doc}`../../developer_guide/developer_mode`.

 In the Inventory Page click on Products-->Products

![Create product](configure_inkind_entitlements/create_product.png)

Click on **New**, then Define the name of your product

![Product name](configure_inkind_entitlements/product_name.png)

Click on **Save** to complete the changes.


### Categorize Products

You can also further categorize these products using **Product Categories** Feature

![Product category](configure_inkind_entitlements/product_category.png)

Click on **New** to define a new product category.

![Product category name](configure_inkind_entitlements/product_category_name.png)

You can go back to Products page and search for a product.

![Search product](configure_inkind_entitlements/search_product.png)

Select the product and define the Product Category field.

![Select product category](configure_inkind_entitlements/select_product_category.png)

Click on **save** to complete the changes.

![Save product](configure_inkind_entitlements/save_product.png)

### In-kind entitlements in a program

You can modify in-kind entitlements during program creation or on an existing one.
Both methods are explained below.

#### Selecting in-kind during creation of a program

Define the in-kind entitlements during program creation under **Configure the Entitlement Manager**

![During create program inkind](configure_inkind_entitlements/during_create_program_inkind.png)

Scroll down from the program modal and click on **Add a line**

![Create program add products](configure_inkind_entitlements/create_program_add_products.png)

Select the product you wish to use.

![Select product](configure_inkind_entitlements/select_product.png)

>Note that the Multiplier defines how many quantity is generated in relation to the selected value under multiplier.
>Maximum number sets the limit how much multiplier value can reach. change to zero to to set it with no limit.

In the example below, if a group has 5 individuals, it would supposedly get 5 eggs , however with Maximum number defined as `2`, the group would only get `2` eggs.

![Example calculation inkind](configure_inkind_entitlements/example_calculation_inkind.png)

##### Configure Entitlement Validator

Select which user role is able to approve these in-kind entitlements for this program, this needs to be defined if auto-approved entitlements is not enabled.

![Entitlement approver](configure_inkind_entitlements/entitlement_approver.png)

then continue with program creation. Learn more in the guide {doc}`create_program`.

##### Verify entitlement count

Go to your program and select the cycle you want to verify.

![Open cycle](configure_inkind_entitlements/open_cycle.png)

Once prepare entitlement is clicked. Navigate to entitlements page.

![View entitlement page](configure_inkind_entitlements/view_entitlement_page.png)

Click on a group and verify the quantity of in-kind entitlements generated if it is correct.

In this example, Group A consists of 3 individuals, but since the maximum is set to 2, only 2 eggs will be generated instead of 3.
![Entitlement count](configure_inkind_entitlements/entitlement_count.png)

#### Selecting in-kind on existing program

You can modify the in-kind entitlements generated for an existing progam by navigating to program page and going to configuration tab.

![Configuration tab](configure_inkind_entitlements/configuration_tab.png)

Scroll down to see **Entitlement Manager**, then click on the green icon.

![Entitlement manager green icon](configure_inkind_entitlements/entitlement_manager_green_icon.png)

In the modal below, you can add, edit or remove products for this program, click **Save** to complete.
Note that any changes in the in-kind entitlements would only take effect to those cycles that are still yet to prepare entitlements. 

![Edit existing program inkind](configure_inkind_entitlements/edit_existing_program_inkind.png)



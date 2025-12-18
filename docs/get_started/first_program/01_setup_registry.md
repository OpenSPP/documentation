---
openspp:
  doc_status: draft
---

# Step 1: Set Up a Basic Beneficiary Registry

This tutorial is for **users** who are new to OpenSPP and want to learn how to set up their first beneficiary registry.

## What You'll Do

Set up a basic registry to store information about individuals and families. You'll configure the registry settings that will be used for your Cash Transfer for Vulnerable Families program.

## Before You Start

- You need **Administrator** or **System Manager** access
- OpenSPP should be installed and running
- Allow 5-10 minutes to complete this step

## The Scenario

You're setting up a **Cash Transfer for Vulnerable Families** program. This program will provide monthly cash assistance to low-income families with children under 5 years old. First, you need to set up a registry to store family and individual information.

## Steps

### 1. Access OpenSPP

Open your web browser and navigate to your OpenSPP installation. Log in with your administrator credentials.

![Screenshot: OpenSPP login screen showing username and password fields](/_images/get_started/first_program/01_setup_registry/1.png)

### 2. Open the Registry Configuration

Click the **four-square icon** in the top-left corner to open the main menu. Then click **Registry** to access the registry module.

![Screenshot: Main menu with four-square icon highlighted and Registry option visible](/_images/get_started/first_program/01_setup_registry/2.png)

### 3. Verify Registry Settings

Navigate to **Configuration → Settings** in the Registry menu. This is where you configure how the registry behaves.

![Screenshot: Registry menu expanded showing Configuration > Settings option](/_images/get_started/first_program/01_setup_registry/3.png)

### 4. Enable Required Features

In the Registry Settings page, ensure the following features are enabled:

- **Groups/Households**: This allows you to register families as groups
- **Individual Members**: This allows you to add family members to groups
- **Privacy-First Search**: This protects beneficiary privacy by requiring search before viewing

Check the boxes next to each feature if they're not already enabled.

![Screenshot: Registry Settings page showing checkboxes for Groups/Households, Individual Members, and Privacy-First Search](/_images/get_started/first_program/01_setup_registry/4.png)

### 5. Save the Configuration

Scroll to the bottom of the page and click **Save** to apply your registry settings.

![Screenshot: Save button at the bottom of the Registry Settings page](/_images/get_started/first_program/01_setup_registry/5.png)

### 6. Verify the Registry is Ready

Click **Registry → Search** from the menu. You should see the Registry Search Portal, which is the privacy-first interface for accessing beneficiary records.

![Screenshot: Registry Search Portal with search bar and "New Individual" and "New Group" buttons](/_images/get_started/first_program/01_setup_registry/6.png)

## What You Accomplished

You've successfully configured your beneficiary registry with the following settings:

- **Groups/Households enabled**: You can now register families as groups
- **Individual Members enabled**: You can add people to family groups
- **Privacy-First Search enabled**: All searches are logged and beneficiary data is protected

## Are You Stuck?

**Can't find the Registry menu?**
Make sure you're logged in with administrator privileges. Only users with the **System Manager** or **Administrator** role can access registry configuration.

**The Settings option is grayed out?**
You may not have the right permissions. Ask your system administrator to grant you access.

**Don't see the Groups/Households option?**
Your OpenSPP installation may not have the Groups module installed. Check with your system administrator about installing the required modules.

## Next Step

Now that your registry is set up, you're ready to add beneficiary data. Continue to [Step 2: Import Beneficiaries](02_import_beneficiaries.md).

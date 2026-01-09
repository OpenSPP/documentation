---
openspp:
  doc_status: draft
  products: [registry]
  applies_to:
    - social_registry
    - sp_mis
---

# Register an Individual

**Applies to:** Social Registry, SP-MIS

## What You Will Do

Add a new person to the registry with their basic information, identity documents, and contact details.

## Before You Start

- You need **Registry Officer** or **Administrator** access
- Have the person's information ready (name, date of birth, ID documents)

## Steps

### 1. Open the Registry

Click **Registry** in the main menu to open the Registry Search Portal.

![Registry menu in sidebar](/_images/en-us/registry/register-individual/01-registry-search-portal-showing-search-bar-and-new.png)

### 2. Click New Individual

Click the **New Individual** button to open the registration form.

![New Individual button](/_images/en-us/registry/register-individual/02-click-new-individual-button.png)

### 3. Enter Basic Information

Fill in the **Profile** tab with the person's basic information.

![Profile tab with name fields](/_images/en-us/registry/register-individual/03-individual-registration-form-with-data-filled.png)

| Field | Required | What to Enter |
|-------|----------|---------------|
| **Family Name** | Yes | Last name or surname |
| **Given Name** | Yes | First name |
| **Middle Name** | No | Additional name(s) |
| **Registration Date** | Auto | Date of registration (defaults to today) |

### 4. Add Demographics

In the **Demographics** section, enter additional information.

![Demographics section](/_images/en-us/registry/register-individual/04-search-results-showing-created-individual.png)

| Field | Required | What to Enter |
|-------|----------|---------------|
| **Date of Birth** | No | Birth date (use calendar picker or type YYYY-MM-DD) |
| **Gender** | No | Select from dropdown |
| **Age** | Auto | Calculated from date of birth |
| **Birth Place** | No | Place of birth |
| **Approximate Birthdate** | No | Check if birth date is estimated |
| **Civil Status** | No | Marital status (single, married, etc.) |
| **Occupation** | No | Select from list |
| **Income** | No | Monthly income amount |

### 5. Add Contact Information

In the **Contact Information** section, enter address and phone details.

![Contact information section](/_images/en-us/registry/register-individual/05-new-group-button-highlighted.png)

| Field | Required | What to Enter |
|-------|----------|---------------|
| **Address** | No | Physical address |
| **Email** | No | Email address |

#### Add Phone Numbers

To add a phone number:

1. In the **Phone Numbers** section, click **Add a line**
2. Enter the phone number
3. Select the country (optional)

![Phone number entry](/_images/en-us/registry/register-individual/06-group-registration-form.png)

You can add multiple phone numbers.

### 6. Add Tags (Optional)

In the **Tags** section, add labels to categorize this individual.

![Tags section](/_images/en-us/registry/register-individual/07-saved-group-form.png)

Click in the tags field and select from available tags, or type to search.

### 7. Save the Record

Click **Save** in the top left corner to create the individual record.

![Save button](/_images/en-us/registry/register-individual/08-group-search-results.png)

### 8. Add Identity Documents (Optional)

After saving, you can add identity documents in the **Identity** tab.

1. Click the **Identity** tab
2. In the **Identity Documents** section, click **Add a line**
3. Select the ID type and enter the ID number

![Identity tab with documents](/_images/en-us/registry/register-individual/09-adding-member-to-group.png)

| Field | Required | What to Enter |
|-------|----------|---------------|
| **ID Type** | Yes | Type of document (National ID, Passport, etc.) |
| **ID Number** | Yes | The document number |
| **Expiry Date** | No | When the document expires |

Click **Save** to save the identity document.

### 9. Verify Registration

Search for the individual in the Registry Search Portal to confirm they were registered.

![Search results showing new individual](/_images/en-us/registry/register-individual/10-group-saved-with-member.png)

## Form Tabs Overview

The individual form has four tabs:

| Tab | Contents |
|-----|----------|
| **Profile** | Name, demographics, contact info, tags |
| **Identity** | ID documents, relationships to other registrants |
| **Participation** | Group memberships, program enrollments |
| **History** | Audit information, status changes |

## Are You Stuck?

**Cannot find the New Individual button?**

- Verify you have Registry Officer or Administrator access
- Contact your administrator if you need access

**Date picker not working?**

- Try typing the date as YYYY-MM-DD (for example, 1990-05-15)
- Make sure the date is not in the future (for birth dates)

**Cannot select a Gender or Civil Status option?**

- These options come from configured vocabularies
- Contact your administrator if options are missing

**Required field error when saving?**

- Family Name and Given Name are always required
- Other required fields depend on your program's configuration
- Look for fields marked with a red asterisk

**Phone number not saving?**

- Enter the phone number without country code prefix if selecting a country
- Check the format matches what is expected in your country

## Next Steps

- {doc}`register_group` - Create a group and add this individual as a member
- {doc}`search_filter` - Learn how to search for registrants

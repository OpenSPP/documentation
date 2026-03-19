---
openspp:
  doc_status: draft
  products: [registry]
  applies_to:
    - social_registry
    - sp_mis
---

# Register an individual

**Applies to:** Social Registry, SP-MIS

## What you will do

Add a new person to the registry with their basic information, identity documents, and contact details.

## Before you start

- You need **Registry Officer** or **Administrator** access
- Have the person's information ready (name, date of birth, ID documents)

## Steps

### Step 1. Open the registry

Click **Registry** in the main menu to open the Registry Search Portal.

![Registry menu in sidebar](/_images/en-us/registry/register-individual/01-registry-search-portal-showing-search-bar-and-new.png)

### Step 2. Click New Individual

Click the **New Individual** button to open the registration form.

![New Individual button](/_images/en-us/registry/register-individual/02-click-new-individual-button.png)

### Step 3. Enter basic information

Fill in the **Profile** tab with the person's basic information.

![Profile tab with name fields](/_images/en-us/registry/register-individual/03-individual-registration-form-with-data-filled.png)

| Field | Required | What to enter |
|-------|----------|---------------|
| **Family Name** | Yes | Last name or surname |
| **Given Name** | Yes | First name |
| **Middle Name** | No | Additional name(s) |
| **Registration Date** | Auto | Date of registration (defaults to today) |

### Step 4. Add demographics

In the **Demographics** section, enter additional information.

![Demographics section](/_images/en-us/registry/register-individual/04-demographics-section-with-date-of-birth-and-gender.png)

| Field | Required | What to enter |
|-------|----------|---------------|
| **Date of Birth** | No | Birth date (use calendar picker or type YYYY-MM-DD) |
| **Gender** | No | Select from dropdown |
| **Age** | Auto | Calculated from date of birth |
| **Birth Place** | No | Place of birth |
| **Approximate Birthdate** | No | Check if birth date is estimated |
| **Civil Status** | No | Marital status (single, married, etc.) |
| **Occupation** | No | Select from list |
| **Income** | No | Monthly income amount |

### Step 5. Add contact information

In the **Contact Information** section, enter address and phone details.

![Contact information section](/_images/en-us/registry/register-individual/05-contact-information-section-with-address-and-email.png)

| Field | Required | What to enter |
|-------|----------|---------------|
| **Address** | No | Physical address |
| **Email** | No | Email address |

#### Add phone numbers

To add a phone number:

1. In the **Phone Numbers** section, click **Add a line**
2. Enter the phone number
3. Select the country (optional)

You can add multiple phone numbers.

### Step 6. Add tags (optional)

In the **Tags** section, add labels to categorize this individual.

![Tags section](/_images/en-us/registry/register-individual/07-tags-section-for-categorizing-the-individual.png)

Click in the tags field and select from available tags, or type to search.

### Step 7. Save the record

Click **Save** in the top left corner to create the individual record.

![Save button](/_images/en-us/registry/register-individual/08-save-button-highlighted-in-top-left-corner.png)

### Step 8. Add identity documents (optional)

After saving, you can add identity documents in the **Identity** tab.

1. Click the **Identity** tab
2. In the **Identity Documents** section, click **Add a line**
3. Select the ID type and enter the ID number

![Identity tab with documents](/_images/en-us/registry/register-individual/09-identity-tab-with-documents-section.png)

| Field | Required | What to enter |
|-------|----------|---------------|
| **ID Type** | Yes | Type of document (National ID, Passport, etc.) |
| **ID Number** | Yes | The document number |
| **Expiry Date** | No | When the document expires |

Click **Save** to save the identity document.

### Step 9. Verify registration

Search for the individual in the Registry Search Portal to confirm they were registered.

![Search results showing new individual](/_images/en-us/registry/register-individual/10-search-results-showing-created-individual.png)

## Form tabs overview

The individual form has four tabs:

| Tab | Contents |
|-----|----------|
| **Profile** | Name, demographics, contact info, tags |
| **Identity** | ID documents, relationships to other registrants |
| **Participation** | Group memberships, program enrollments |
| **History** | Audit information, status changes |

## Are you stuck?

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

## Next steps

- {doc}`register_group` - Create a group and add this individual as a member
- {doc}`search_filter` - Learn how to search for registrants

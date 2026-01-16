---
openspp:
  doc_status: draft
  products: [registry]
  applies_to:
    - social_registry
    - sp_mis
---

# Register a Group

**Applies to:** Social Registry, SP-MIS

## What You Will Do

Create a new group (such as a household) and add individual members to it.

## Before You Start

- You need **Registry Officer** or **Administrator** access
- Individuals should already be registered before adding them to a group
- Have the group information ready (name, type, address)

## Understanding Groups

A **group** represents a collection of related individuals, typically a household. Groups are important because:

- Many programs target households rather than individuals
- Benefits may be calculated based on household composition
- One member is usually designated as the household **head**

## Steps

### 1. Open the Registry

Click **Registry** in the main menu to open the Registry Search Portal.

![Registry menu in sidebar](/_images/en-us/registry/register-group/01-registry-menu-in-sidebar-showing-registry-search.png)

### 2. Click New Group

Click the **New Group** button to open the group registration form.

![New Group button](/_images/en-us/registry/register-group/02-new-group-button-highlighted-in-registry-search.png)

### 3. Enter Group Information

Fill in the **Profile** tab with the group's basic information.

![Group profile tab](/_images/en-us/registry/register-group/03-group-profile-tab-showing-empty-registration-form.png)

| Field | Required | What to Enter |
|-------|----------|---------------|
| **Group Name** | Yes | Name to identify this group (for example, "Santos Household") |
| **Group Type** | No | Type of group (Household, Family, etc.) |
| **Registration Date** | Auto | Date of registration (defaults to today) |

### 4. Add Contact Information

In the **Contact Information** section, enter the group's address and contact details.

![Contact information section](/_images/en-us/registry/register-group/04-contact-information-section-with-address-and-email.png)

| Field | Required | What to Enter |
|-------|----------|---------------|
| **Address** | No | Physical address of the group |
| **Email** | No | Contact email address |

#### Add Phone Numbers

To add a phone number for the group:

1. In the **Phone Numbers** section, click **Add a line**
2. Enter the phone number
3. Select the country (optional)

![Phone number entry](/_images/en-us/registry/register-group/05-phone-number-entry-section-with-add-a-line-button.png)

### 5. Add Tags (Optional)

In the **Tags** section, add labels to categorize this group.

![Tags section](/_images/en-us/registry/register-group/06-tags-section-for-categorizing-the-group.png)

```{note}
If no tags appear in the dropdown, they may need to be configured by your administrator first. Contact your administrator to set up tags for your organization.
```

### 6. Save the Group

Click **Save** in the top left corner to create the group record.

![Save button](/_images/en-us/registry/register-group/07-save-button-highlighted-in-top-left-corner.png)

### 7. Add Members to the Group

After saving, add individuals as members of this group.

1. Click the **Participation** tab
2. In the **Group Members** section, click **Add a line**

![Group Members section with Add a line](/_images/en-us/registry/register-group/08-group-members-section-with-add-a-line-button-in-pa.png)

3. Select an individual from the **Member name** column dropdown.

![Select individual from dropdown](/_images/en-us/registry/register-group/09-individual-selection-dropdown-in-group-membership.png)

4. Fill in the membership details:

| Field | Required | What to Enter |
|-------|----------|---------------|
| **Member Name** | Yes | Select the individual to add |
| **Membership Types** | No | Role in the group (Head, Spouse, Child, etc.) |
| **Start Date** | Auto | When membership began (defaults to now) |
| **End Date** | No | Leave empty for active members |

![Membership details filled in](/_images/en-us/registry/register-group/10-membership-details-filled-in-with-member-name-and.png)

5. Repeat to add more members
6. Click **Save** to save all members

### 8. Designate a Household Head

One member should be designated as the household head:

1. Click the membership row for the head of household
2. In **Membership Types**, select **Head**
3. Click **Save**

![Designating household head](/_images/en-us/registry/register-group/11-designating-household-head-with-head-membership-ty.png)

```{note}
Only one member can be the Head per group. If you try to set a second Head, you will see an error message.
```

### 9. Verify the Group

Search for the group in the Registry Search Portal to confirm it was created with all members.

![Search results showing new group](/_images/en-us/registry/register-group/12-search-results-showing-newly-created-group.png)

## Viewing Group Membership

### From the Group Record

Open the group and click the **Participation** tab to see all members.

![Group with members listed](/_images/en-us/registry/register-group/13-group-record-with-members-listed-in-participation.png)

Each row shows:
- Member name
- Date of birth
- Gender
- Membership type
- Start and end dates
- Status (active or inactive)

### From an Individual Record

Open an individual and click the **Participation** tab to see which groups they belong to.

![Individual participation tab showing groups](/_images/en-us/registry/register-group/14-individual-participation-tab-showing-groups.png)


## Ending a Membership

To remove someone from a group without deleting their individual record:

1. Open the group
2. Click the **Participation** tab
3. Find the member and click their row
4. Set an **End Date** for the membership
5. Click **Save**

The membership status will change to **Inactive**.

## Are You Stuck?

**Cannot find the New Group button?**

- Verify you have Registry Officer or Administrator access
- Contact your administrator if you need access

**Cannot find an individual to add as a member?**

- The individual must be registered first
- Use {doc}`register_individual` to register them, then return to add them to the group
- Check your search term if using Search More

**Error: "Only one Head is allowed per group"**

- Each group can only have one member with the Head membership type
- Remove the Head type from the current head before assigning it to someone else

**Error: "Duplication of Member is not allowed"**

- Each individual can only be added to a group once
- Check if the person is already listed in the Group Members section

**Members not showing after save?**

- Make sure you clicked **Save** after adding members
- Refresh the page if members still do not appear

**Group Type options are missing?**

- Group types come from configured vocabularies
- Contact your administrator to add more group types

## Next Steps

- {doc}`search_filter` - Learn how to search for groups and individuals
- {doc}`register_individual` - Register more individuals to add to groups

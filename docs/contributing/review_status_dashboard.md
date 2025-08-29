---
review-status: approved
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Status dashboard for documentation review tracking"
---

# Documentation Review Status Dashboard

This page tracks the review status of all documentation pages after the 2025 reorganization.

## Status Definitions

- 🟢 **Approved**: Content is up-to-date and accurate
- 🟡 **Reviewed**: Content has been checked and is likely accurate  
- 🔴 **Needs Review**: Content needs to be reviewed for accuracy after reorganization
- 🟠 **In Review**: Currently being reviewed by someone
- ⚪ **Outdated**: Content is known to be outdated

## How the Review Status System Works

The review status system has been implemented to help track the documentation quality after the major reorganization. You should see:

- A **status ribbon** in the top-right corner of each page
- A **status banner** at the top of pages that need attention

## Review Progress Summary

Based on the 2025 documentation reorganization:

### ✅ **Approved** (11 pages)
Pages that are newly created or completely up-to-date:
- `getting_started/installation_pypi.md` - Newly created PyPI installation guide
- `overview/case_studies/index.md` - New section index
- `overview/features/index.md` - New features overview index
- `developer_guide/customization/index.md` - New customization index
- `developer_guide/integrations/index.md` - New integrations index
- `developer_guide/api_usage/index.md` - New API usage index
- `reference/api/index.md` - New API reference index
- `reference/technical/index.md` - New technical reference index
- `user_guide/registry_management/index.md` - New registry management index
- `user_guide/program_management/index.md` - New program management index
- `user_guide/administration/index.md` - New administration index

### 🟡 **Reviewed** (98 pages)
Content that was moved but likely still accurate:
- All files in `community/` (9 pages) - Simple moves from community_and_support
- All files in `reference/modules/` (87 pages) - Direct moves, content unchanged
- `getting_started/installation_docker.md` - Updated Docker guide
- `getting_started/poc_and_pilot.md` - Direct move
- `reference/glossary.rst` - Direct move

### 🔴 **Needs Review** (118+ pages)
Content that requires review due to reorganization:
- Most files in `user_guide/` - Merged from tutorial/howto sections
- Most files in `overview/concepts/` - Moved from explanation/
- Most files in `developer_guide/customization/` - Complex restructuring
- Most files in `developer_guide/integrations/` - Complex restructuring
- Most files in `reference/technical/` - Moved from technical_reference/

## Testing the System

To see the review status system in action:

1. **Visit any documentation page** - You should see a colored ribbon in the top-right corner
2. **Check pages that need review** - Look for the orange/red warning banner
3. **Compare different status types** - Visit pages in different sections to see various statuses

### Test Pages

- **Approved**: {doc}`../getting_started/installation_deb`
- **Reviewed**: {doc}`../community/code_of_conduct`  
- **Needs Review**: {doc}`../overview/concepts/user_management`

## Review Guidelines

### For Reviewers

When reviewing a page:

1. **Update the frontmatter** in the markdown file:
   ```yaml
   ---
   review-status: reviewed  # or approved
   review-date: 2025-06-04
   reviewer: your-name
   migration-notes: "Reviewed content after reorganization - updated links"
   ---
   ```

2. **Check for**:
   - Accuracy of content in new location
   - Broken or outdated links
   - Consistency with new structure
   - Proper cross-references using `{doc}` syntax

3. **Status Guidelines**:
   - **Approved**: Content is completely accurate and up-to-date
   - **Reviewed**: Content has been checked and minor issues fixed
   - **Needs Review**: Content needs significant updates or verification

### For Contributors

To help with the review process:

1. **File Issues**: Report pages with outdated or incorrect information
2. **Submit PRs**: Fix obvious issues like broken links or outdated instructions
3. **Update Status**: When you fix a page, update its review status appropriately

## Technical Implementation

The review status system includes:

- **Path-based detection**: JavaScript determines status based on URL patterns
- **Visual indicators**: CSS-based ribbons and banners
- **Frontmatter tracking**: Each page has YAML frontmatter with status info
- **Build integration**: Status information is preserved in git

### Files Added

- `docs/_static/review_status.css` - Status styling
- `docs/_static/review_status_simple.js` - Status detection and display
- `docs/_templates/layout.html` - Template modifications
- `add_review_status.py` - Script to add frontmatter to all pages

---

*Last updated: 2025-06-04*  
*Total pages tracked: 227*  
*Review status system: ✅ Active*

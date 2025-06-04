# Migrating OpenSPP Documentation to New Structure

## 1\. Introduction

This guide provides instructions for migrating the existing OpenSPP documentation content into the new, standardized structure outlined in the Proposed OpenSPP Documentation Structure. The goal is to improve organization, discoverability, and maintainability.

This process requires careful planning and execution, especially regarding updating links.

## 2\. Reference Documents

*   **New Structure:** Proposed OpenSPP Documentation Structure
    
*   **Contributor Guidelines:** OpenSPP Documentation Contributor Guidelines
    

## 3\. Migration Process Overview

The migration involves the following key phases:

1.  **Audit Existing Content:** Analyze each current documentation file.
    
2.  **Map to New Structure:** Determine the new location for each file.
    
3.  **Move & Rename Files:** Physically relocate files according to the map.
    
4.  **Refactor Content:** Adjust content to fit the new structure and guidelines.
    
5.  **Update Links & Cross-References:** Fix all internal links and navigation elements.
    
6.  **Build & Review:** Verify the migrated documentation builds correctly and is navigable.
    

## 4\. Step-by-Step Guide

**Step 1: Content Audit**

*   Create a list (e.g., in a spreadsheet) of all current `.md` and `.rst` files in the `docs/` directory (excluding `_static`, `_templates`, `conf.py`, `Makefile`, etc.).
    
*   For each file, determine:
    
    *   **Primary Purpose:** Is it mainly for Learning (Tutorial), Doing (How-to), Explaining (Concept), or Looking Up (Reference)?
        
    *   **Primary Audience:** Decision Maker, Admin/User, Developer?
        
    *   **Current Location:** Note the existing path.
        
    *   **Keep/Discard/Merge:** Decide if the content is still relevant, needs merging, or should be discarded.
        

**Step 2: Map to New Structure**

*   Based on the audit (Purpose & Audience), assign a **New Location** within the proposed structure (Proposed OpenSPP Documentation Structure) to each file you intend to keep or merge.
    
*   Identify content gaps (topics listed in the proposed structure but not covered by existing files). These will need new pages created later.
    
*   Plan any necessary merges (e.g., combining separate import/export guides).
    

**Step 3: Move & Rename Files**

*   Create the new directory structure locally (e.g., `overview/`, `user_guide/`, etc.).
    
*   Using your map from Step 2, physically move the files (`git mv old/path/file.md new/path/file.md`) to their new locations.
    
*   Rename files if necessary for clarity or consistency (use dashes `-`, lowercase).
    
*   Update the `.gitignore` file if any new patterns are needed for generated files in the new structure.
    

**Step 4: Refactor Content**

This is a significant step. For each moved file:

*   **Review Purpose:** Ensure the content aligns with the purpose of its new section (e.g., a file moved to `user_guide/` should be task-oriented).
    
*   **Rewrite Introductions/Conclusions:** Adjust the opening and closing paragraphs to fit the context of the new section.
    
*   **Apply "Principles First" (where applicable):** For files moved to `overview/concepts/` or `overview/use_cases/`, restructure to present general principles before OpenSPP specifics.
    
*   **Formatting:** Ensure adherence to the Contributor Guidelines (MyST, code blocks, images, :term: usage).
    
*   **Metadata:** **Critically important:** Add or update the `html_meta` block at the top of _every single page_ with an accurate `title`, `description`, and relevant `keywords`.
    
*   **Split/Merge:** Perform any content splitting or merging identified in Step 2.
    

**Step 5: Update Links & Cross-References**

This is the most error-prone step and requires diligence.

*   **Internal Links (`{doc}`):** Search across _all_ documentation files for `{doc}` references. Update the paths to reflect the new file locations. Relative paths (`../`) will likely need adjustment.
    
*   **Heading Links (`{ref}`):** Ensure the labels used in `{ref}` still exist in the target documents. If files were split or headings changed, these links might break.
    
*   **`toctree` Directives:** Update all `toctree` directives in `index.md` files (and potentially other pages) to list the correct paths of the files within that section. Ensure `:maxdepth:` and `:hidden:`/:`caption:` options are appropriate.
    
*   **Image Paths:** Verify that image paths (e.g., `/_static/...`) are still correct relative to the documentation root. Using root-relative paths (`/...`) is generally safer during restructuring.
    
*   **External Links:** While not directly affected by the structure change, this is a good time to re-run `make linkcheck` and fix any broken external links found.
    

**Tools:**

*   Use your IDE's "Find in Files" or command-line tools like `grep -r "{doc}" .` to locate links.
    
*   Be systematic. Go through the documentation section by section or file by file.
    

**Step 6: Build & Review**

*   Run `make clean` to remove old build artifacts.
    
*   Run `make html`. Address _all_ errors and warnings reported by Sphinx. Pay close attention to "document not in toctree" warnings or broken link errors.
    
*   Run `make linkcheck` again.
    
*   Run `make vale` again.
    
*   Open the locally built HTML (`_build/html/index.html`) in your browser.
    
    *   Click through the navigation extensively.
        
    *   Check internal links on various pages.
        
    *   Verify `toctree` structures are correct.
        
    *   Ensure pages render correctly.
        

### 5\. Tracking Progress

*   Use the spreadsheet created in Step 1 & 2 to track the migration status of each file (Audited -> Mapped -> Moved -> Refactored -> Links Updated -> Reviewed).
    
*   Consider using GitHub Issues or a project board for larger efforts to track tasks and assign work if multiple people are involved.
    

### 6\. Committing Changes

*   Make frequent, logical commits (e.g., commit after moving files for one section, commit after updating links for that section). This makes it easier to revert changes if something goes wrong.
    
*   Use clear commit messages describing the migration step performed.
    

This migration requires careful attention to detail, especially when updating links. Proceed methodically and test thoroughly at each stage.

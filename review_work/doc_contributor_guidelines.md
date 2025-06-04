
# OpenSPP Documentation Contributor Guidelines

## 1\. Introduction

Welcome to the OpenSPP documentation project! These guidelines are intended for anyone writing or reviewing documentation to ensure consistency, quality, and usability. Our goal is to create documentation that is not only accurate and helpful for OpenSPP users but also serves as a valuable resource for the broader social protection community.

Familiarity with the proposed documentation structure is essential. Please refer to the Proposed OpenSPP Documentation Structure.

## 2\. Target Audience

Always keep the primary audience for the section you are writing for in mind:

*   **Decision Makers:** Need high-level overviews, benefits, features, and concepts. Avoid deep technical jargon.
    
*   **Administrators / End-Users:** Need clear, task-oriented steps (How-to Guides) and foundational learning (Tutorials). Focus on the UI and practical workflows.
    
*   **Developers:** Need technical depth, code examples, API details, architecture, and customization guides.
    

## 3\. Writing Style & Tone

*   **Style Guide:** Follow the [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/ "null").
    
*   **Tone:** Informative, clear, concise, and friendly.
    
*   **Voice:** Use "you" to address the reader directly.
    
*   **Headings:** Use Sentence case (e.g., "Configure cash entitlements," not "Configure Cash Entitlements").
    
*   **Sentences:** Aim for one main idea per sentence. Keep sentences relatively short and easy to understand. Use one sentence per line in the source file for easier diffs and collaboration.
    
*   **Terminology:** Use consistent terminology. Refer to the Glossary and use the `:term:` role for defined terms (e.g., `` :term:`Social Registry` ``).
    

## 4\. Content Structure & Purpose

Adhere to the purpose of each main section as defined in the Proposed Structure:

*   **overview:** High-level introductions, features, benefits, concepts, use cases. _Target: Decision Makers, New Users._
    
*   **getting\_started:** Installation, initial setup. _Target: Admins, Developers._
    
*   **user\_guide:** Task-based "How-to Guides" for using the platform. Foundational workflows can be structured as "Tutorials". _Target: Admins, End-Users._
    
*   **developer\_guide:** Technical "How-to Guides" and explanations for development tasks. _Target: Developers._
    
*   **reference:** Detailed, factual lookup information (Modules, APIs, Technical Specs, Glossary). _Target: Developers, Admins._
    
*   **community:** Contribution, support, legal information. _Target: All._
    

**Tutorials vs. How-to Guides:**

*   **Tutorials (Learning):** Guide a beginner step-by-step to achieve basic competence. Explain the _why_. Primarily belong in `getting_started` or for foundational workflows in `user_guide`.
    
*   **How-to Guides (Doing):** Provide steps to solve a specific problem for someone with some existing knowledge. Focus on the _how_. Make up the bulk of `user_guide` and `developer_guide`.
    

**Platform-Agnostic Content (Important for Reference Goal):**

*   In `overview/concepts/` and `overview/use_cases/`, first explain the general principles, best practices, and challenges related to the topic (e.g., Social Registries) in a platform-agnostic way.
    
*   _Then_, explain how OpenSPP implements or addresses these points, linking to specific features and guides. Clearly separate general vs. OpenSPP-specific content.
    

## 5\. Formatting

*   **Markup:** Use MyST Markdown (`.md` files). Use reStructuredText (`.rst`) only where necessary (e.g., complex directives not supported by MyST).
    
*   **Code Blocks:**
    
    *   Use correct language identifiers for syntax highlighting (e.g., `python,` json, `xml,` bash). Verify lexers work using `make html`.
        
    *   Do _not_ use `...` to indicate omitted code; comment it out properly or use separate blocks.
        
    *   Use `console` for shell sessions showing commands and output. Use `shell` for commands only (no prompts).
        
*   **Images:**
    
    *   Provide descriptive `alt` text for accessibility.
        
    *   Keep width under 740px if possible.
        
    *   Use cards for captions and links to larger versions (see `myst-reference.md` example).
        
    *   Store images in `_static/` within relevant subdirectories. Use root-relative paths (e.g., `/_static/user-guide/my-image.png`).
        
*   **Links:**
    
    *   Use `{doc}` role for linking to other pages (e.g., `` {doc}`../user_guide/registry_management/register_individual` ``).
        
    *   Use `{ref}` role for linking to specific labels/headings (e.g., `` {ref}`my-heading-label` ``).
        
    *   Ensure all external links are valid (`make linkcheck`). Avoid linking to unstable sources like blogs if possible; summarize and cite instead.
        
*   **Metadata:** **Every page MUST have a `myst:` frontmatter block with `html_meta` containing accurate `title`, `description`, and `keywords`.**
    

## 6\. Quality Checks

Before submitting a Pull Request (PR):

*   Run `make html` locally to check for build errors or warnings (especially lexer issues).
    
*   Run `make vale` to check spelling, grammar, and style. Add necessary terms to `styles/Vocab/OpenSPP/accept.txt`.
    
*   Run `make linkcheck` to verify all external and internal links. Fix or justify any broken links.
    
*   Ensure `html_meta` is present and accurate on all modified/added pages.
    

## 7\. Review Process

**For Authors:**

*   Submit focused PRs addressing a single issue or documentation section.
    
*   Clearly describe the changes in the PR description.
    
*   Ensure all quality checks pass locally before submitting.
    
*   Respond to reviewer feedback promptly.
    

**For Reviewers:**

*   Verify the content is accurate and clear.
    
*   Check adherence to style and tone guidelines.
    
*   Ensure the content fits the purpose of its new section in the new structure.
    
*   Validate formatting (code blocks, images, links).
    
*   Confirm `html_meta` is present and makes sense.
    
*   Check for broken links (`make linkcheck` if possible).
    
*   Ensure adequate cross-linking to related topics.
    
*   Verify platform-agnostic content is handled correctly where applicable.
    

## 8\. Updating Documentation

Documentation is a living entity. If you notice outdated information, missing steps, or areas for improvement, please file an issue or submit a PR. Keep guides aligned with the current software version.

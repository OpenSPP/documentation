---
review-status: needs-review
review-date: 2025-08-28
reviewer: Edwin Gonzales
migration-notes: "Added during 2025 documentation reorganization"
---

# Best Practices

OpenSPP follows the coding standards of the [Odoo Community Association (OCA)](https://github.com/OCA/odoo-community.org/blob/master/website/Contribution/CONTRIBUTING.rst), which are designed to ensure high-quality, maintainable, and consistent code. While the full guidelines are extensive, here are some of the most important best practices to follow:

## Enforce Coding Standards with Pre-Commit
- OpenSPP uses `pre-commit` to automatically enforce **PEP8** and other coding standards. This is the recommended way to ensure your code is compliant before committing.
- The configuration runs tools like `black` (formatting), `isort` (import sorting), and `flake8` (linting).
- To set it up, run these commands once in your repository:
  ```bash
  pip install pre-commit
  pre-commit install
  ```
- After setup, these checks will run automatically on every `git commit`. If an issue is found, the commit will be stopped, and some tools may automatically fix the files for you.

## Write Clean and Readable XML
- Use a consistent naming convention for record IDs. For example: `view_model_name_form`, `action_model_name_window`.
- Logically order fields in views to create an intuitive user experience.

## Prioritize Security and Extensibility
- Always define access rights in `security/ir.model.access.csv`. Never grant universal access (`group_id:id,"",...`) without a strong reason.
- Avoid using raw SQL queries. Use the Odoo ORM to ensure security rules are respected.
- Always use `_inherit` and `xpath` to extend existing functionality. Never modify core OpenSPP or Odoo files directly.

## Adhere to Licensing Requirements
- All custom modules for OpenSPP must be licensed under **LGPL-3**.
- Ensure that any third-party Python libraries or other dependencies you add are compatible with the LGPL-3 license.
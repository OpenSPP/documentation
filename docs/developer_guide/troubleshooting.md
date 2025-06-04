---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Troubleshooting

This guide offers insights and solutions for common errors encountered in Odoo application development. Understanding these errors and knowing how to address them efficiently is crucial for maintaining a smooth development process.

1. Error: Field “x” does not exist in model “y”

   - Confirm the field's presence in the model.
   - Ensure the Python file is listed in `models/__init__.py`.
   - Verify the existence of from . import models in the `__init__.py` file.
   - Consider upgrading the module.
   - Double-check the field name for any spelling errors.

2. Error: Unable to install module “x” due to an unmet external dependency: Missing Python library “y”, “z”

   - Execute pip install -r requirements.txt to install the module's required Python libraries.
   - If specific libraries are mentioned in the error, install them individually using pip.

3. Error: Invalid field “x” on model “y”

   - Ensure the field exists within the model.
   - Restart the Odoo server and then upgrade the module.

4. Error: Some modules are not loaded, potentially due to missing dependencies or manifests: [“x”]

   - Check if the module is located in the custom/ or custom/src/ folder. If absent, add the module, restart the Odoo server, and attempt reinstallation.
   - Confirm the existence of the dependency module of the missing module in either the custom/ or custom/src/ folder.

5. Error: Inconsistent module states, possibly due to missing dependencies: [“x”]

   - This issue often arises when a dependency of the “x” module encounters an error.
   - Explore and rectify errors in other related modules.

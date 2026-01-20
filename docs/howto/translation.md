# Translation

## Introduction
OpenSPP uses the GNU gettext system for internationalization and localization, leveraging PO (Portable Object) and POT (Portable Object Template) files. This guide explains the workflow for managing translations, adding new languages, updating existing translations, and maintaining high-quality localized content.

For additional reference, see:
- [Odoo 17 Translation Guide](https://www.odoo.com/documentation/17.0/developer/howtos/translations.html)
- [Odoo 16 Translation Guide](https://www.odoo.com/documentation/16.0/developer/howtos/translations.html)
- [polib Python Library](https://pypi.org/project/polib/)

## Understanding PO and POT Files

- **POT Files (Portable Object Templates):** These files act as templates that contain all the translatable strings extracted from the source code.
- **PO Files (Portable Objects):** Language-specific files that contain translations for strings found in the POT files. Each PO file corresponds to a specific language.
- **MO Files (Machine Object):** Binary files generated from PO files, used for faster runtime translation processing.

## Adding Translations for a New Language

1. **Generate the POT file:**
   ```sh
   xgettext -o locale/messages.pot $(find . -name "*.py" -o -name "*.html")
   ```
2. **Create a new PO file for the target language:**
   ```sh
   msginit --locale=es --input=locale/messages.pot --output=locale/es/LC_MESSAGES/messages.po
   ```
   Replace `es` with the appropriate language code.
3. **Edit the PO file:** Open `locale/es/LC_MESSAGES/messages.po` and provide translations for each string.
4. **Compile the PO file into an MO file:**
   ```sh
   msgfmt -o locale/es/LC_MESSAGES/messages.mo locale/es/LC_MESSAGES/messages.po
   ```
5. **Test the translations in OpenSPP** to ensure they display correctly.

## Updating Existing Translations

1. **Extract updated translatable strings:**
   ```sh
   xgettext -o locale/messages.pot $(find . -name "*.py" -o -name "*.html")
   ```
2. **Merge updates into existing PO files:**
   ```sh
   msgmerge --update locale/es/LC_MESSAGES/messages.po locale/messages.pot
   ```
3. **Review and update translations** where necessary.
4. **Recompile the PO files:**
   ```sh
   msgfmt -o locale/es/LC_MESSAGES/messages.mo locale/es/LC_MESSAGES/messages.po
   ```
5. **Test the updated translations** to verify changes are applied correctly.

## Best Practices for Translation Maintenance

- **Consistency:** Use a standardized glossary for key terms.
- **Context:** Always provide translator comments (`#:`) in source files where necessary.
- **Review Process:** Have a second translator review translations to ensure quality.
- **Automation:** Use tools like `gettext` and `polib` to streamline extraction, merging, and management.
- **Regular Updates:** Update translations periodically, especially after major code changes.

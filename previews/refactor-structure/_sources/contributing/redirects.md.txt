---
orphan: true
---

# Managing Documentation Redirects

This guide explains how to handle redirects when refactoring or moving documentation pages in the OpenSPP documentation.

## Configuration

The OpenSPP documentation uses the `sphinx-reredirects` extension to handle redirects. The configuration is located in `docs/conf.py`.

## Adding Redirects

To add a redirect when moving or renaming a page:

1. Open `docs/conf.py`
2. Find the `redirects` dictionary (around line 177)
3. Add your redirect mapping:

```python
redirects = {
    # Redirect from old path to new path
    "old-page": "new-page.html",
    "old-folder/page": "new-folder/page.html",
    
    # Examples:
    "getting-started": "getting_started/index.html",
    "api/v1/reference": "technical_reference/apis.html",
}
```

## Important Notes

- Paths in the `redirects` dictionary are relative to the documentation root
- The old path should NOT include the `.html` extension
- The new path MUST include the `.html` extension
- Redirects work for both files and directories
- You can redirect to external URLs as well

## Testing Redirects

After adding redirects:

1. Build the documentation locally:
   ```bash
   make clean
   make html
   ```

2. Navigate to the old URL in your browser
3. Verify that you are automatically redirected to the new location

## Best Practices

1. **Always add redirects** when moving or renaming documentation pages
2. **Keep redirects for at least 6-12 months** for public documentation
3. **Document major moves** in the changelog or release notes
4. **Update internal links** to point directly to new locations
5. **Test redirects** after deployment to ensure they work correctly

## Example Use Cases

### Renaming a Page
```python
redirects = {
    "installation": "getting_started/installation_guide.html",
}
```

### Moving to a Different Section
```python
redirects = {
    "tutorials/basic-setup": "getting_started/installation_guide.html",
}
```

### Consolidating Multiple Pages
```python
redirects = {
    "setup/requirements": "getting_started/installation_guide.html",
    "setup/installation": "getting_started/installation_guide.html",
    "setup/configuration": "getting_started/installation_guide.html",
}
```

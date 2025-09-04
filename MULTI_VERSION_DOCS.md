# Multi-Version Documentation System

This repository implements a multi-version documentation system that publishes different versions of the documentation to GitHub Pages.

## Overview

The system supports three types of documentation deployments:

1. **Stable Documentation** (`main` branch) → Published at https://docs.openspp.org/
2. **Preview Documentation** (feature branches) → Published at https://docs.openspp.org/previews/{branch-name}/
3. **Version Releases** (future) → Published at https://docs.openspp.org/{version}/

## How It Works

### Environment Variables

The build system uses environment variables to configure each build:

- `DOCS_VERSION`: Version identifier (e.g., "stable", "refactor-structure")
- `DOCS_BASEURL`: Base URL for the documentation (e.g., "https://docs.openspp.org/")
- `IS_PREVIEW`: Set to "1" for preview builds, "0" for stable/release builds

### SEO Protection

Preview builds are protected from search engine indexing:

1. **Meta Tags**: Preview builds include `<meta name="robots" content="noindex,nofollow,noarchive">`
2. **robots.txt**: Only deployed with stable builds, blocks `/previews/` directory
3. **Visual Indicator**: Preview builds show a warning banner to users

### GitHub Actions Workflow

The `.github/workflows/build_deploy.yml` workflow handles automatic deployment:

- Triggers on push to any branch
- Main branch deploys to root as stable documentation
- Other branches deploy to `/previews/{sanitized-branch-name}/`
- Branch names are sanitized (special characters replaced with hyphens, limited to 50 chars)

### Version Switcher

The documentation includes a version switcher dropdown configured via `docs/_static/switcher.json`.

**Important Note:** sphinx-book-theme version 0.3.3 doesn't have built-in version switcher support. The current implementation uses a custom JavaScript solution (`_static/version_switcher.js`). For full native support, consider upgrading to sphinx-book-theme >= 1.0.0.

#### Managing Versions

Use the helper script to manage versions:

```bash
# List current versions
python Scripts/update_version_switcher.py list

# Add a new version
python Scripts/update_version_switcher.py add \
  --version "1.2" \
  --name "Version 1.2" \
  --url "https://docs.openspp.org/1.2/"

# Remove a version
python Scripts/update_version_switcher.py remove --version "old-preview"
```

### Cleanup of Old Previews

The `.github/workflows/cleanup_previews.yml` workflow automatically removes old preview deployments:

- Runs weekly (Sunday at 00:00 UTC)
- Can be manually triggered
- Keeps previews newer than 30 days (configurable)
- Always keeps at least 10 newest previews (configurable)
- Updates version switcher when removing previews

To manually trigger cleanup:
1. Go to Actions → Cleanup old preview deployments
2. Click "Run workflow"
3. Optionally adjust keep_days and keep_count parameters

## Local Testing

To test multi-version builds locally:

```bash
# Test stable build
export DOCS_VERSION=stable
export DOCS_BASEURL=https://docs.openspp.org/
export IS_PREVIEW=0
make html

# Test preview build
export DOCS_VERSION=my-feature
export DOCS_BASEURL=https://docs.openspp.org/previews/my-feature/
export IS_PREVIEW=1
make html
```

## Security Features

The implementation includes several security measures:

1. **Branch Name Sanitization**: Only alphanumeric, dots, underscores, and hyphens allowed
2. **Path Traversal Protection**: Version switcher script validates file paths
3. **Input Validation**: URLs and version names are validated to prevent injection
4. **Atomic File Operations**: Prevents corruption during concurrent updates
5. **Error Handling**: Build failures are properly caught and reported

## Maintenance

### Adding a New Release Version

When creating a new release (e.g., v1.2):

1. Tag the release in git
2. Update the version switcher:
   ```bash
   python Scripts/update_version_switcher.py add \
     --version "1.2" \
     --name "v1.2 (latest)" \
     --url "https://docs.openspp.org/1.2/"
   ```
3. The GitHub Actions workflow will build and deploy to `/1.2/`

### Monitoring

- Check GitHub Actions for build status
- Review cleanup workflow runs for removed previews
- Monitor disk usage on GitHub Pages

## Troubleshooting

### Preview Not Appearing

1. Check GitHub Actions for build failures
2. Verify branch name doesn't contain invalid characters
3. Check that `keep_files: true` is set in the workflow

### Version Switcher Not Updated

1. Ensure switcher.json is valid JSON
2. Check file permissions on gh-pages branch
3. Verify the update script ran successfully

### SEO Issues

1. Verify preview builds have noindex meta tag
2. Check robots.txt is only present in stable build
3. Test with Google Search Console or similar tools

## Future Enhancements

- Automatic version detection from git tags
- PR comment with preview URL
- Build caching for faster deployments
- Version-specific search functionality
# CLAUDE.md

This file provides guidance to Claude Code when working with the OpenSPP documentation repository.

## Overview

This is the documentation repository for OpenSPP - an open-source social protection platform. The documentation is built using Sphinx with MyST parser for Markdown support.

## Project Structure

```
docs/
├── overview/           # High-level information for decision makers
│   ├── features/      # Feature overviews by functional area
│   ├── concepts/      # Conceptual explanations
│   ├── products/      # Product configurations (SP-MIS, Social Registry, Farmer Registry)
│   └── case_studies/  # Implementation examples
├── getting_started/    # Installation and quickstart guides
├── user_guide/        # Task-oriented guides for administrators
│   ├── registry_management/
│   ├── program_management/
│   └── administration/
├── developer_guide/   # Technical documentation
│   ├── customization/
│   ├── integrations/
│   └── api_usage/
├── reference/         # Detailed reference material
│   ├── modules/       # OpenSPP module documentation
│   └── technical/     # Technical specifications
└── community/         # Contribution and support information
```

## Build Commands

### Development Setup
```bash
# Create Python virtual environment and install dependencies
make deps

# This installs requirements and initializes git submodules
```

### Building Documentation
```bash
# Build HTML documentation
make html

# Live reload server for development (port 8050)
make livehtml

# Clean build artifacts
make clean

# Clean everything including virtual environment
make distclean
```

### Quality Checks
```bash
# Run Vale for style, grammar, and spell checks
make vale

# Check for broken links
make linkcheck

# Run all quality checks and build
make all  # Runs: clean, vale, linkcheck, html

# Run tests
make test
```

## Documentation Standards

When working with documentation:

1. **File Format**: All documentation uses MyST Markdown (.md files)
2. **Metadata**: Every page MUST have MyST frontmatter with html_meta for SEO
3. **Headings**: Use sentence case (e.g., "Getting started" not "Getting Started")
4. **Links**: 
   - Use `{doc}` for internal documentation links
   - Link to module reference pages when mentioning modules
   - Link to product pages when mentioning SP-MIS, Social Registry, or Farmer Registry
   - Never put links or `:term:` in headings
5. **Terminology**: Use `:term:` only on first occurrence of glossary terms

Example frontmatter:
```yaml
---
myst:
  html_meta:
    "title": "Page Title"
    "description": "Brief description for SEO"
    "keywords": "OpenSPP, relevant, keywords"
---
```

## Common Tasks

### Adding a New Documentation Page
1. Create the .md file in the appropriate directory
2. Add required MyST frontmatter with html_meta
3. Add the page to the appropriate index.md toctree
4. Use sentence case for all headings
5. Run `make html` to verify it builds

### Updating Module Documentation
- Module docs are in `docs/reference/modules/`
- Each module has its own .md file named after the module
- Include sections: Overview, Features, Configuration, Usage

### Linking to Modules
When mentioning a module like `spp_base`:
```markdown
The {doc}`spp_base </reference/modules/spp_base>` module provides...
```

### Linking to Products
When mentioning product configurations:
```markdown
The {doc}`SP-MIS <../overview/products/sp_mis>` configuration...
```

## Key Configuration Files

- `conf.py` - Sphinx configuration
- `.vale.ini` - Vale linter configuration
- `requirements.txt` - Python dependencies
- `.github/workflows/` - CI/CD pipelines

## Important Notes

- Documentation uses Sphinx 4.5.0 with MyST parser
- Vale is configured with Microsoft and alex style guides
- Live reload server runs on port 8050
- GitHub Actions handle automated builds on push to main
- The build warns about missing files but usually succeeds


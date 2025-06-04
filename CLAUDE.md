# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the documentation repository for OpenSPP - an open-source social protection platform. The documentation is built using Sphinx with MyST parser for Markdown support.

## Build Commands

### Setup Development Environment
```bash
# Create Python virtual environment and install dependencies
make deps

# This will:
# - Create a Python virtual environment
# - Install requirements from requirements_frozen.txt
# - Initialize git submodules (openg2p-program, openg2p-registry)
```

### Build Documentation
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
```

### Testing
```bash
# Run tests (cleans then runs linkcheck)
make test
```

## Architecture

The documentation is organized into several key sections:

1. **docs/** - Main documentation source files
   - `getting_started/` - Installation guides and quickstart tutorials
   - `explanation/` - Conceptual documentation about registries, security, and core concepts
   - `howto/` - Step-by-step guides for developers and users
   - `tutorial/` - User-focused tutorials for common tasks
   - `technical_reference/` - API documentation, architecture details
   - `modules/` - Documentation for OpenSPP modules
   - `community_and_support/` - Contributing guidelines, support resources

2. **submodules/** - Git submodules containing related OpenG2P projects
   - `odoo/` - Odoo framework (OpenSPP is built on Odoo)
   - `openg2p-program/` - OpenG2P program management modules
   - `openg2p-registry/` - OpenG2P registry modules
   - `queue/` - Queue job management

3. **Configuration**
   - `conf.py` - Sphinx configuration with custom OpenSPP/Odoo integration
   - `.vale.ini` - Vale linter configuration using Microsoft and alex style guides
   - `requirements_frozen.txt` - Pinned Python dependencies

## Key Development Notes

- The documentation uses Sphinx 4.5.0 with MyST parser for Markdown support
- Vale is configured for style checking with OpenSPP-specific vocabulary
- The build system automatically handles Odoo module documentation integration
- Live reload development server runs on port 8050
- GitHub Actions handle automated builds and deployment on push to main branch
- Redirects are managed using sphinx-reredirects extension (see `redirects` dict in conf.py)

## Module Documentation

When documenting OpenSPP modules, follow the existing pattern in `docs/modules/`. Each module should have its own Markdown file with standardized sections for overview, features, configuration, and usage.

## Managing Redirects

When moving or renaming documentation pages, add redirects in `docs/conf.py`:
```python
redirects = {
    "old-path": "new-path.html",
}
```
See `docs/contributing/redirects.md` for detailed instructions.
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

The documentation is organized into several key sections following a modernized structure implemented in January 2025:

1. **docs/** - Main documentation source files (restructured)
   - `overview/` - High-level information for decision makers and new users
     - `features/` - Feature overviews organized by functional area
     - `concepts/` - Conceptual explanations (moved from `explanation/`)
     - `use_cases/` - Use-case specific entry points (social registry, farmer registry, SP-MIS)
     - `case_studies/` - Implementation examples
   - `getting_started/` - Installation guides and quickstart tutorials
   - `user_guide/` - Task-oriented guides for administrators and end-users
     - `registry_management/` - Registry operations and data management
     - `program_management/` - Program creation, cycles, and management
     - `administration/` - System administration tasks
   - `developer_guide/` - Technical information for developers
     - `customization/` - Guides for customizing OpenSPP functionality
     - `integrations/` - Integration guides for external systems
     - `api_usage/` - API guides and references
   - `reference/` - Detailed reference material
     - `modules/` - Documentation for OpenSPP modules (moved from `docs/modules/`)
     - `technical/` - Technical specifications and deep-dives
     - `api/` - API references and specifications
   - `community/` - Community interaction, contribution processes, and legal information

2. **submodules/** - Git submodules containing related OpenG2P projects
   - `odoo/` - Odoo framework (OpenSPP is built on Odoo)
   - `openg2p-program/` - OpenG2P program management modules
   - `openg2p-registry/` - OpenG2P registry modules
   - `queue/` - Queue job management

3. **Configuration**
   - `conf.py` - Sphinx configuration with custom OpenSPP/Odoo integration
   - `.vale.ini` - Vale linter configuration using Microsoft and alex style guides
   - `requirements_frozen.txt` - Pinned Python dependencies

4. **Migration Tools** (available for reference)
   - `refactor_docs.py` - Automated documentation restructuring script
   - `update_navigation.py` - Navigation menu management
   - `update_links.py` - Cross-reference link updating

## Key Development Notes

- The documentation uses Sphinx 4.5.0 with MyST parser for Markdown support
- Vale is configured for style checking with OpenSPP-specific vocabulary
- The build system automatically handles Odoo module documentation integration
- Live reload development server runs on port 8050
- GitHub Actions handle automated builds and deployment on push to main branch
- Redirects are managed using sphinx-reredirects extension (currently disabled due to version conflicts)

## Module Documentation

When documenting OpenSPP modules, follow the existing pattern in `docs/reference/modules/`. Each module should have its own Markdown file with standardized sections for overview, features, configuration, and usage.

## Managing Redirects

When moving or renaming documentation pages, add redirects in `docs/conf.py`:
```python
redirects = {
    "old-path": "new-path.html",
}
```
Note: The sphinx-reredirects extension is currently disabled due to version conflicts with Sphinx 4.5.0. The redirect mappings are prepared in conf.py but commented out until a compatible version is available.

## Documentation Refactoring Lessons Learned

### Automated Migration Approach

The 2025 documentation restructuring used Python scripts for automation:
- **refactor_docs.py**: Main script for moving files and handling merges/splits
- **update_navigation.py**: Updates toctree entries in index files
- **update_links.py**: Updates internal cross-references

This approach proved essential for:
- Consistency across 117+ file movements
- Handling complex directory structures and image relocations
- Maintaining content integrity during merges

### Critical Success Factors

1. **Comprehensive Mapping**: Create detailed mapping of old → new structure before starting
2. **Phased Execution**: Break migration into discrete phases (audit, move, navigate, validate)
3. **Navigation Updates**: Moving files is only half the work - updating toctree entries requires systematic attention
4. **Build Validation**: Test builds frequently to catch dependency issues early
5. **Content Consolidation**: Migration reveals duplication opportunities (tutorial/howto sections)

### Technical Challenges

- **Dependency Management**: PIL/Pillow library conflicts can break builds
- **Extension Compatibility**: sphinx-reredirects requires newer Sphinx versions
- **Cross-Reference Complexity**: Internal links need careful updating across all files
- **Image Path Management**: Images need to move with their content while maintaining relative paths

When performing future refactoring, use the existing scripts as templates and follow the phased approach documented in `review_work/doc_migration_guide.md`.
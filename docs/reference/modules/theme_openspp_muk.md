---
openspp:
  doc_status: draft
---

# Theme

**Module:** `theme_openspp_muk`

## Overview

The OpenSPP Theme module provides custom styling for the OpenSPP platform. Built on the MuK Web Theme, it applies OpenSPP's brand colors and visual identity to the Odoo backend interface, supporting both light and dark modes.

## Purpose

This module is designed to:

- **Apply OpenSPP branding:** Use OpenSPP's color palette across the interface
- **Maintain visual consistency:** Ensure a unified look throughout the platform
- **Support accessibility:** Provide both light and dark mode options
- **Customize navigation:** Style the navbar with OpenSPP identity

## Module Dependencies

| Dependency        | Description                                    |
| ----------------- | ---------------------------------------------- |
| **base**          | Odoo core functionality                        |
| **web**           | Odoo web client assets                         |
| **muk_web_theme** | MuK Hacker theme as the base styling framework |

## Key Features

### Color Customization

The theme defines OpenSPP's brand colors:

| Asset Bundle      | Description                  |
| ----------------- | ---------------------------- |
| Primary Variables | Core color definitions       |
| Light Mode Colors | Color scheme for light theme |
| Dark Mode Colors  | Color scheme for dark theme  |

### Light Mode

Default color scheme with:

- OpenSPP primary brand colors
- Readable contrast ratios
- Professional appearance

### Dark Mode

Alternative color scheme for:

- Reduced eye strain in low-light environments
- Energy savings on OLED displays
- User preference support

### Navigation Bar Styling

Custom navbar appearance:

- OpenSPP branding in header
- Consistent button styling
- Improved menu visibility

## Theme Assets

| Asset               | Purpose                 |
| ------------------- | ----------------------- |
| `colors.scss`       | Primary color variables |
| `colors_light.scss` | Light theme overrides   |
| `colors_dark.scss`  | Dark theme overrides    |
| `navbar.scss`       | Navigation bar styling  |

## Integration

The OpenSPP Theme integrates with:

- **muk_web_theme:** Extends MuK's theme infrastructure
- **web.assets_backend:** Loads into Odoo's backend interface
- **All OpenSPP modules:** Provides consistent styling across the platform

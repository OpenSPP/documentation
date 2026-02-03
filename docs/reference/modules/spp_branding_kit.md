---
openspp:
  doc_status: draft
---

# Branding Kit

This module is for **sys admins** and **developers** who need to customize OpenSPP's branding, URL routing, and telemetry settings.

## Overview

Branding Kit provides comprehensive branding customization for OpenSPP deployments. It replaces Odoo branding with OpenSPP branding across the platform, adds URL routing aliases, and manages telemetry configuration.

Use this module when you need to:

- Replace Odoo branding with OpenSPP or custom branding
- Provide `/openspp` URL routes as aliases for `/odoo` routes
- Control telemetry data collection
- Customize email signatures, report footers, and system messages

## Module Dependencies

| Dependency | Purpose |
|------------|---------|
| `base` | Odoo core framework |
| `web` | Web interface components |
| `base_setup` | Configuration settings framework |
| `spp_security` | Security groups and access control |
| `theme_openspp_muk` | OpenSPP visual theme styling |

## Key Features

### URL Routing

The module provides branded URL paths as aliases:

| Branded URL | Original URL |
|-------------|--------------|
| `/openspp/programs/123` | `/odoo/programs/123` |
| `/openspp/action/456` | `/odoo/action/456` |
| `/openspp/*` | `/odoo/*` |

### Telemetry Management

Control how telemetry data is handled:

| Option | Behavior |
|--------|----------|
| Enabled | Redirects telemetry to OpenSPP endpoint |
| Disabled | Completely disables telemetry data collection |

### Branding Customization

| Element | Customization |
|---------|---------------|
| System name | Configurable (default: "OpenSPP Platform") |
| Email signatures | Replaces Odoo signature with OpenSPP |
| Report headers | Updates company branding |
| Help links | Custom documentation and support URLs |
| Module filtering | "OpenSPP Apps" menu for OpenSPP modules |

### Post-Install Changes

The module automatically applies these changes on installation:

- Disables Odoo brand promotion messages
- Removes module update notification crons
- Hides theme store menu
- Injects OpenSPP branding into web client session

## Configuration

After installing:

1. Open **Settings**
2. Scroll to the **OpenSPP Branding** section
3. Configure the following options:

| Setting | Description | Default |
|---------|-------------|---------|
| System Name | Name shown in UI | OpenSPP Platform |
| Documentation URL | Link for help/docs | https://docs.openspp.org |
| Support URL | Link for support requests | - |
| Display Branding | Show "Powered by OpenSPP" | Enabled |
| Enable Telemetry | Send anonymized usage data | Disabled |
| Telemetry Endpoint | Target URL for telemetry | https://telemetry.openspp.org |

## Extended Models

This module does not introduce new models. It extends existing Odoo models:

| Model | Extension Purpose |
|-------|-------------------|
| `res.users` | Custom email signature, removes Odoo URLs |
| `res.config.settings` | Branding and telemetry configuration fields |
| `ir.http` | Injects OpenSPP branding into session info |
| `ir.module.module` | Utility to count paid/proprietary apps |

## Technical Details

| Property | Value |
|----------|-------|
| Technical Name | `spp_branding_kit` |
| Category | Theme/Backend |
| Version | 19.0.1.4.0 |
| License | LGPL-3 |
| Application | No |
| Auto Install | Yes (with base, web) |

## Are you stuck?

### Branding not appearing after install

**Symptom:** OpenSPP branding elements not visible after installation.

**Cause:** Browser cache may contain old assets.

**Solution:** Clear browser cache and reload, or hard refresh with Ctrl+Shift+R (Cmd+Shift+R on macOS).

### URL routing not working

**Symptom:** `/openspp/*` URLs return 404 errors.

**Cause:** Router patch may not have loaded properly.

**Solution:**

1. Restart the Odoo server
2. Clear browser cache
3. Verify module is installed without errors in the module list

### Custom branding not showing in reports

**Symptom:** Reports still show default branding after configuration.

**Cause:** Report templates may be cached or company settings not applied.

**Solution:**

1. Clear the report cache: **Settings > Technical > Actions > Report Layout**
2. Verify company logo is uploaded in **Settings > Companies**
3. Regenerate reports after changes

## See Also

- {doc}`theme_openspp_muk` - Visual theme styling for OpenSPP
- {doc}`spp_security` - Security groups and access control

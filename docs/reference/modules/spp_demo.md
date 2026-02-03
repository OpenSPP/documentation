---
openspp:
  doc_status: draft
---

# Demo


## Overview

The Demo module provides core demonstration functionality for OpenSPP, including a data generator with locale-specific providers, sample user data, and demo stories for realistic test scenarios. It serves as the foundation for domain-specific demo modules.

## Purpose

This module is designed to:

- **Generate realistic test data:** Create sample registrants with locale-appropriate names and attributes
- **Provide demo users:** Pre-configure users with appropriate roles for testing
- **Support multiple locales:** Generate culturally appropriate data for different countries
- **Enable rapid prototyping:** Quickly populate a system for demonstrations and training

## Module Dependencies

| Dependency          | Description                                         |
| ------------------- | --------------------------------------------------- |
| **base**            | Odoo core functionality                             |
| **spp_base_common** | OpenSPP common utilities                            |
| **spp_registry**    | Registry for individuals and groups                 |
| **spp_vocabulary**  | Standardized code lists                             |
| **queue_job**       | Background job processing for large data generation |
| **spp_security**    | Security groups for demo users                      |

### External Python Dependencies

| Package   | Description                       |
| --------- | --------------------------------- |
| **faker** | Generates fake but realistic data |

## Key Features

### Data Generator

Generate sample registrant data with configurable options:

| Setting           | Description                          |
| ----------------- | ------------------------------------ |
| Number of Records | How many registrants to create       |
| Locale            | Language/country for name generation |
| Include Groups    | Generate households with members     |
| Group Size Range  | Min/max members per household        |

### Locale Providers

Generate culturally appropriate names for:

| Locale Code | Region              |
| ----------- | ------------------- |
| en_KE       | Kenya (English)     |
| sw_KE       | Kenya (Swahili)     |
| lo_LA       | Laos                |
| si_LK       | Sri Lanka (Sinhala) |
| ta_LK       | Sri Lanka (Tamil)   |

### Demo Users

Pre-configured users for testing different roles:

| User Type     | Description                     |
| ------------- | ------------------------------- |
| Administrator | Full system access              |
| Manager       | Program and registry management |
| Officer       | Data entry and processing       |
| Viewer        | Read-only access                |

### Demo Stories

Realistic scenarios for testing:

- Typical household compositions
- Common registrant attributes
- Representative geographic distributions

### Configuration Settings

Access demo generation settings through Odoo's configuration:

| Setting                 | Description                     |
| ----------------------- | ------------------------------- |
| Demo Generation Enabled | Allow demo data creation        |
| Default Locale          | Default language for generation |
| Batch Size              | Records per background job      |

## Integration

The Demo module provides the foundation for:

- **spp_mis_demo_v2:** SP-MIS specific demo with programs and indicators
- **spp_base_farmer_registry_demo:** Farmer registry demo data
- **spp_case_demo:** Case management demo data
- **spp_grm_demo:** Grievance management demo data
- **spp_event_demo:** Event tracking demo data

## Are you stuck?

### Demo data generation fails

**Symptom:** Error when running the data generator

**Cause:** The faker package may not be installed or there are memory issues with large batches

**Solution:** Verify faker is installed with `pip install faker`. For large datasets, reduce the batch size or use queue jobs for background processing.

### Names appear in wrong language

**Symptom:** Generated names do not match the expected locale

**Cause:** The locale provider may not be correctly configured

**Solution:** Check that the desired locale is selected in the demo generator settings. Verify the locale code matches the supported options.

### Demo users not created

**Symptom:** Pre-configured demo users are not available after installation

**Cause:** Demo data may not have been loaded during installation

**Solution:** Check that the module was installed with demo data enabled. You can manually trigger demo user creation from the configuration.

### Background generation stuck

**Symptom:** Data generation started but records are not appearing

**Cause:** Queue jobs may not be processing

**Solution:** Verify that the queue_job module is properly configured and workers are running. Check the job queue for errors.

### Cannot find demo generator

**Symptom:** The demo data generator wizard is not visible

**Cause:** User lacks administrator privileges

**Solution:** Only administrators can access the demo data generator. Log in with an admin account to access this feature.

---
openspp:
  doc_status: draft
---

# Registry Search Portal


## Overview

The Registry Search Portal provides a privacy-first interface for accessing beneficiary records. Instead of displaying all registrants by default, users must search to find specific records. This design protects beneficiary privacy by preventing bulk browsing while maintaining full audit trails of who viewed which records.

## Purpose

This module is designed to:

- **Protect beneficiary privacy:** Prevent unauthorized bulk browsing of registrant data by requiring explicit searches
- **Track access patterns:** Maintain audit trails of which users viewed which registrants
- **Support quick lookups:** Enable efficient searches with minimum 3-character queries and advanced filters
- **Personalize the interface:** Show recently viewed registrants per user for quick re-access

## Module Dependencies

| Dependency       | Description                                            |
| ---------------- | ------------------------------------------------------ |
| **spp_registry** | Core registry functionality for individuals and groups |

## Key Features

### Search-First Interface

The portal displays a search landing page instead of loading all records. Users must enter at least 3 characters to search, which:

- Reduces database load from large result sets
- Prevents accidental exposure of beneficiary data
- Encourages targeted lookups rather than browsing

### Advanced Search Filters

Beyond basic name search, users can filter by:

| Filter            | Description                           |
| ----------------- | ------------------------------------- |
| Phone             | Search by phone number                |
| Email             | Search by email address               |
| Registration Date | Filter by when registrants were added |

### Recently Viewed Registrants

Each user sees their own personal history of recently viewed records:

- Stores up to 50 records per user
- Updates automatically when viewing a registrant
- Displays avatar, name, and last view date
- Can be cleared by the user

### Role-Based Access

| Security Group   | Capabilities                              |
| ---------------- | ----------------------------------------- |
| Registry User    | Must search to find registrants           |
| Registry Auditor | Can browse all registrants without search |
| Registry Officer | Can edit registrants via UI               |
| Registry Manager | Full management access                    |

### View History Tracking

The module tracks:

- Which user viewed which registrant
- When the view occurred
- How many times each registrant was viewed

This data supports compliance auditing and security monitoring.

### Area-Based Filtering

When integrated with `spp_area`, the recently viewed list automatically filters to show only registrants within the user's assigned geographic areas.

## Integration

The Registry Search Portal integrates with:

- **spp_registry:** Extends the core registry with search-first behavior
- **spp_area:** Filters results by user's assigned geographic areas
- **spp_security:** Respects role-based access controls

## Are you stuck?

### Search returns no results

**Symptom:** Searching for a known registrant returns empty results

**Cause:** Search requires at least 3 characters, or the registrant may be outside your assigned areas

**Solution:** Ensure you enter at least 3 characters. If area restrictions apply, check with your administrator that you have access to the registrant's geographic area.

### Cannot see recently viewed registrants

**Symptom:** The "Recently Viewed" section is empty even after viewing records

**Cause:** History may have been cleared, or an error occurred during recording

**Solution:** View a registrant's profile to add them to your history. If the issue persists, contact your administrator.

### Cannot browse all registrants

**Symptom:** No option to view all records without searching

**Cause:** This is intentional privacy protection. Only auditors can browse all records.

**Solution:** If you need browse-all access for legitimate audit purposes, request the "Registry Auditor" role from your administrator.

### Archive button not visible

**Symptom:** Cannot archive or unarchive registrants

**Cause:** Only officers, managers, and administrators can archive registrants

**Solution:** If you need to archive a registrant, contact a user with the Registry Officer or Registry Manager role.

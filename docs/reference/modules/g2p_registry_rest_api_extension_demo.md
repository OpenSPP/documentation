---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# G2P Registry: Rest API Extension Demo

```{warning}

**Work in Progress**: This document is actively being developed and updated. Content may be incomplete or subject to change.
```

## Overview

This module serves as a demonstration of how to extend the OpenG2P Registry Rest API. It provides a practical example of adding new fields to existing API responses without directly modifying the core API module ([g2p_registry_rest_api](g2p_registry_rest_api)).

## Purpose

The main goal of this module is to illustrate the extensibility of the OpenG2P Registry Rest API. By providing a concrete example, it guides developers on how to tailor the API output to their specific needs without compromising the integrity of the core API functionality.

## Functionality

The module focuses on extending the `GroupInfoOut` model from the [g2p_registry_rest_api](g2p_registry_rest_api) module. It adds a new field `active` to the `GroupInfoOut` response, which indicates whether the group is currently active. 

This is achieved using the `extends` feature provided by the `extendable-pydantic` library. This approach ensures that the extended model inherits all the existing fields and functionalities of the original `GroupInfoOut` model while adding the new `active` field.

## Integration

The [g2p_registry_rest_api_extension_demo](g2p_registry_rest_api_extension_demo) module depends on the [g2p_registry_rest_api](g2p_registry_rest_api) module. It leverages the API endpoints and data models provided by the core API module and extends them to include additional information.

## Conclusion

This demonstration module provides a blueprint for developers looking to customize the OpenG2P Registry Rest API. By following the principles illustrated in this module, developers can seamlessly extend the API to accommodate specific data requirements and functionalities. 

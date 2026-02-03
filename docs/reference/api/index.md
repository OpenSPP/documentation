---
orphan: true
openspp:
  doc_status: draft
  products: [core]
---

# API Reference

This section provides comprehensive API documentation for OpenSPP, including REST APIs, GraphQL endpoints, and integration interfaces.

## API Documentation

OpenSPP provides APIs for:
- **Registry Operations**: Managing registrants, individuals, and groups
- **Program Management**: Creating and managing programs, enrollment, eligibility
- **Payment Processing**: Initiating and tracking payments
- **Data Import/Export**: Bulk data operations
- **Authentication**: OAuth2 and API key authentication
- **Webhooks**: Event notifications and callbacks

## Documentation Format

API documentation is auto-generated from the OpenSPP codebase using OpenAPI/Swagger specifications. The interactive API documentation allows you to:
- Browse all available endpoints
- View request/response schemas
- Test API calls directly from the documentation
- Download OpenAPI specifications

## Accessing API Documentation

When OpenSPP is running, you can access the interactive API documentation at:

```
https://your-openspp-instance/api/docs
```

Alternative formats:
- **Swagger UI**: `/api/docs` (interactive interface)
- **ReDoc**: `/api/redoc` (alternative documentation view)
- **OpenAPI JSON**: `/api/openapi.json` (machine-readable specification)

<!--
```{toctree}
:maxdepth: 2

authentication
registry-api
program-api
payment-api
import-export-api
webhooks
rate-limits
errors
```
-->

**Note:** Content coming soon. Links to live API documentation will be provided when available. This section will include additional guides for common API use cases and integration patterns.

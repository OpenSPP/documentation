---
openspp:
  doc_status: unverified
  products: [core]
---

# Technical Reference

The Technical Reference is a detailed document outlining the system's architecture and technical specifications. It serves as a resource for architects and developers to understand the system's functionalities and operations.

**Configuration and Architecture**

- {doc}`architecture`
- {doc}`extensibility`

**Security and Compliance**

- {doc}`security`
- {doc}`Access Rights </ops_guide/security/access_control>` (moved to Operations Guide)
- {doc}`audit_logs`

**Code and Release Management**

- {doc}`code`
- {doc}`release_management`

**Monitoring and Analytics**

- {doc}`monitoring`
- {doc}`programs/dashboards`

**Integrations**

- {doc}`integrations`
- {doc}`apis`
- {doc}`API v2 (REST) </developer_guide/api_v2/index>` (moved to Developer Guide)
- {doc}`external_api`

**Other**

- {doc}`backup`
- {doc}`performance_optimization`
- {doc}`CEL </config_guide/cel/index>` (moved to Configuration Guide)

**Managers and Modules**

- {doc}`programs/concepts`
- {doc}`programs/program_manager`
- {doc}`programs/cycle_manager`
- {doc}`programs/eligibility_manager`
- {doc}`programs/entitlement_manager`
- {doc}`programs/deduplication_manager`
- {doc}`programs/notification_manager`

```{toctree}
:maxdepth: 3
:hidden: true
:caption: Configuration and Architecture

architecture
extensibility
```

```{toctree}
:maxdepth: 3
:hidden: true
:caption: Security and Compliance

security
/ops_guide/security/access_control
oidc
audit_logs
```

```{toctree}
:maxdepth: 3
:hidden: true
:caption: Code and Release Management

code
release_management
```

```{toctree}
:maxdepth: 3
:hidden: true
:caption: Monitoring and Analytics

monitoring
programs/dashboards
```

```{toctree}
:maxdepth: 3
:hidden: true
:caption: Integrations

integrations
apis
/developer_guide/api_v2/index
dci
external_api
```

```{toctree}
:maxdepth: 3
:hidden: true
:caption: Other

backup
performance_optimization
```

```{toctree}
:maxdepth: 3
:hidden: true
:caption: Managers and Modules

module
programs/index
programs/concepts
programs/program_manager
programs/cycle_manager
programs/eligibility_manager
programs/entitlement_manager
programs/deduplication_manager
programs/notification_manager
```

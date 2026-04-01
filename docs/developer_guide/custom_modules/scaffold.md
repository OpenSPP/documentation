---
openspp:
  doc_status: draft
  products: [core]
---

# Module scaffold

**For: developers**

This page shows you how to create the directory structure and initial files for a new OpenSPP module.

## Directory structure

A typical OpenSPP module follows this layout:

```
spp_my_module/
├── __init__.py
├── __manifest__.py
├── pyproject.toml
├── models/
│   ├── __init__.py
│   └── my_model.py
├── views/
│   ├── my_model_views.xml
│   └── menus.xml
├── security/
│   ├── groups.xml
│   ├── ir.model.access.csv
│   └── rules.xml
├── data/
│   └── (sequences, vocabularies, cron jobs, etc.)
├── tests/
│   ├── __init__.py
│   ├── common.py
│   └── test_my_model.py
└── readme/
    └── DESCRIPTION.md
```

## The manifest

Every module needs an `__manifest__.py` file. OpenSPP enforces specific fields via pre-commit hooks:

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenSPP My Module",
    "summary": "Brief description of what this module does.",
    "category": "OpenSPP/Core",
    "version": "19.0.2.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/OpenSPP2",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": ["your-github-handle"],
    "depends": [
        "base",
        "spp_security",
    ],
    "data": [
        # Security files MUST be loaded first
        "security/groups.xml",
        "security/ir.model.access.csv",
        "security/rules.xml",
        # Data files
        # Views and menus last
        "views/my_model_views.xml",
        "views/menus.xml",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
```

### Required fields

These are enforced by the `.pylintrc-mandatory` checks and will fail CI if missing:

| Field     | Requirement                                                |
| --------- | ---------------------------------------------------------- |
| `license` | Must be `LGPL-3` (other GPL variants also accepted)        |
| `author`  | Must include `OpenSPP.org`                                 |
| `version` | Format: `19.0.{major}.{minor}.{patch}`                     |
| `depends` | Must include `spp_security` for access control integration |

### Data file load order

The order of files in the `data` list matters. Security files must come first because views and menus reference security groups:

1. `security/groups.xml` — Group definitions
2. `security/ir.model.access.csv` — Model access rules
3. `security/rules.xml` — Record rules
4. `data/*.xml` — Sequences, vocabularies, cron jobs
5. `views/*.xml` — Form, list, search views
6. `views/menus.xml` — Menu items (last, since they reference actions)

### Module categories

Choose the category that best fits your module:

| Category                 | When to use                                   |
| ------------------------ | --------------------------------------------- |
| `OpenSPP/Core`           | Foundation modules needed by most deployments |
| `OpenSPP/Configuration`  | Admin tools, no-code configuration            |
| `OpenSPP/Integration`    | APIs, external system connectors              |
| `OpenSPP/GIS`            | Geographic/spatial functionality              |
| `OpenSPP/Infrastructure` | System-level utilities                        |
| `OpenSPP`                | General-purpose modules                       |

### Development status

| Status              | Meaning                               |
| ------------------- | ------------------------------------- |
| `Alpha`             | Early development, API may change     |
| `Beta`              | Feature-complete but not fully tested |
| `Production/Stable` | Ready for production use              |

## Init files

The root `__init__.py` imports the `models` package:

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from . import models
```

The `models/__init__.py` imports each model file:

```python
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from . import my_model
```

If you have tests:

```python
# tests/__init__.py
# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from . import common
from . import test_my_model
```

## Build configuration

Every module needs a `pyproject.toml` for the whool build system:

```toml
[build-system]
requires = ["whool"]
build-backend = "whool.buildapi"
```

## Module naming

Module directory names must start with `spp_`:

```
spp_my_feature/        # Correct
my_feature/            # Will fail pre-commit checks
openspp_my_feature/    # Will fail pre-commit checks
```

The pre-commit hooks enforce this naming rule. A small set of third-party modules are whitelisted (e.g., `fastapi`, `job_worker`, `base_user_role`).

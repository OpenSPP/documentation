---
openspp:
  doc_status: draft
---

# Installation

This guide is for **sys admins** and **evaluators** deploying OpenSPP.

## Installation Methods

| Method | Status | Best For |
|--------|--------|----------|
| {doc}`docker` | ✅ Available | Evaluation, development, production |
| Debian/Ubuntu package | 🚧 Coming soon | Native Linux deployments |
| Windows installer | 🚧 Coming soon | Windows Server environments |

```{note}
**Recommended:** Start with Docker. It's the officially supported method and works on all platforms.
```

## System Requirements

### Minimum (Evaluation)

| Component | Requirement |
|-----------|-------------|
| CPU | 2 cores |
| RAM | 4 GB |
| Disk | 20 GB SSD |
| OS | Ubuntu 20.04+, Debian 11+, macOS 12+, Windows with WSL2 |

### Recommended (Production)

| Component | Requirement |
|-----------|-------------|
| CPU | 4+ cores |
| RAM | 8+ GB (16 GB for large registries) |
| Disk | 100+ GB SSD |
| OS | Ubuntu 22.04 LTS, Debian 12 |

## Prerequisites

Before installing, you'll need:

- **Docker 24.0+** and **Docker Compose v2.20+**
- **Git 2.30+**

See {doc}`docker` for platform-specific installation commands.

```{toctree}
:maxdepth: 1
:hidden:

docker
```

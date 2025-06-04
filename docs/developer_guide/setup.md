---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Development Setup

Setting up a local OpenSPP environment can be accomplished through two distinct methodologies.

## 1. OpenSPP Docker Setup Using Doodba

This technique utilizes Docker, simplifying the installation of Odoo and its dependencies, with the added benefits offered by Doodba.

### Prerequisites

- Basic understanding of Git, Docker, Docker Compose, Git-aggregator, Invoke, Odoo, and Python
- Terminal access
- Visual Studio Code (VSCode)

### Setup

1. Begin by cloning the OpenSPP Docker repository from [here](https://github.com/OpenSPP/openspp-docker.git)

2. Switch to the openspp-docker directory.

3. Execute the following commands:

- `invoke develop` - Sets up a VSCode development environment.
- `invoke img-pull` - Retrieves Docker images as per .yaml file specifications.
- `invoke img-build` - Constructs Docker images locally.
- `invoke img-build` --pull - Builds or pulls images from a remote repository as needed.
- `invoke resetdb` - Generates a new, demo-data-free database.
- `invoke resetdb` --demo - Creates a new database inclusive of demo data.
- `invoke start` - Activates Odoo.

4. Combine these commands for a single execution if desired.

- e.g. `invoke develop img-pull img-build git-aggregate resetdb start`

5. Browse the following in a preferred browser:

- Odoo: http://localhost:17069/
- Mailhog: http://localhost:17025/
- Wdb: http://localhost:17984/
- Pgweb: http://localhost:17081/

Refer to the Readme in the repository for more detailed instructions on Docker Odoo and Invoke commands.

## 2. OpenSPP Setup from PyPI

For installing OpenSPP modules via PyPI, see the {doc}`../getting_started/installation_pypi` guide.

---
myst:
  html_meta:
    "title": "Development setup"
    "description": "Complete guide to setting up OpenSPP development environment using Docker and Doodba with step-by-step instructions"
    "keywords": "OpenSPP, development setup, Docker, Doodba, development environment, installation"
---

# Development setup

## OpenSPP Docker Setup Using Doodba

Docker simplifies the installation of Odoo and its dependencies, with the added benefits offered by Doodba.

### Prerequisites

- Basic understanding of Git, Docker, Docker Compose, Git-aggregator, Invoke, Odoo, and Python
- Terminal access
- Visual Studio Code (VSCode)

### Setup

1. Begin by cloning the OpenSPP Docker repository from [here](https://github.com/OpenSPP/openspp-docker.git)

2. Switch to the openspp-docker directory.

3. Execute the following commands:

```bash
invoke develop        # Sets up a VSCode development environment
invoke img-pull       # Retrieves Docker images as per .yaml file specifications
invoke img-build      # Constructs Docker images locally
invoke git-aggregate  # Pull the dependencies with git
invoke resetdb        # Generates a new, demo-data-free database
invoke start          # Activates Odoo
```

4. Combine these commands for a single execution if desired:

```bash
invoke develop img-pull img-build git-aggregate resetdb start
```

5. Browse the following in a preferred browser:

- Odoo: <http://localhost:17069/>
- Mailhog: <http://localhost:17025/>
- Wdb: <http://localhost:17984/>
- Pgweb: <http://localhost:17081/>

Refer to the Readme in the repository for more detailed instructions on Docker Odoo and Invoke commands.

# Development Setup

Setting up a local Odoo environment can be accomplished through two distinct methodologies.

## 1. Docker Odoo Setup Using Doodba

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

- Odoo: http://localhost:15069/
- Mailhog: http://localhost:15025/
- Wdb: http://localhost:15984/
- Pgweb: http://localhost:15081/

Refer to the Readme.md in the repository for more detailed instructions on Docker Odoo and Invoke commands

## 2. Odoo Setup from source

This method is the traditional way of installing Odoo, involving manual installation and configuration.

### Prerequisites

- Knowledge of your current Operating System
- Terminal access

### Setup

1. Follow the official Odoo installation guide suitable for your Operating System.[Link](https://www.odoo.com/documentation/17.0/administration/on_premise.html)

2. Inside the Odoo folder, create a new directory named custom.

3. Other Odoo repositories or Odoo modules should be added to the “custom” folder.

4. Navigate to “custom” and git clone all of the following repositories and their corresponding branches:

- `git clone –branch 17.0 https://github.com/OCA/connector.git`
- `git clone –branch 17.0 https://github.com/OCA/dms.git`
- `git clone –branch 17.0 https://github.com/OpenSPP/openspp-modules`
- `git clone –branch 17.0 https://github.com/OCA/queue.git`
- `git clone –branch 17.0 https://github.com/OCA/rest-framework.git`
- `git clone –branch 17.0 https://github.com/OCA/server-auth.git`
- `git clone –branch 17.0 https://github.com/OCA/server-backend.git`
- `git clone –branch 17.0 https://github.com/Smile-SA/odoo_addons.git`
- `git clone –branch 17.0 https://github.com/OCA/social.git`
- `git clone –branch 17.0 https://github.com/OCA/web.git`

5. `pip install the requirements in requirements.txt in each of the repositories if there is a requirements.txt.

6. Open `odoo.conf` in a preferred IDE and add in the `addons_path` the absolute path of the “custom” folder

- e.g. `addons_path = /Users/username/odoo/addons,/Users/username/odoo/custom`

7. Execute `python3 odoo-bin -c odoo.conf` to run Odoo.

8. Open http://localhost:8069/ in a browser to use OpenSPP.

To learn more about Odoo command, visit [this documentation](https://www.odoo.com/documentation/17.0/developer/reference/cli.html)

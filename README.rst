OpenSPP - Social Protection Platform
====================================

`OpenSPP` is an open-source project that aims to streamline the management of social protection programs.
It can be used on its own or in conjunction with other services.

.. image:: docs/programs/images/openspp_overview.png
  :alt: OpenSPP overview

`OpenSPP` is based on an open-source `ERP <https://en.wikipedia.org/wiki/Enterprise_resource_planning>`_ called `Odoo 15.0 <https://odoo.com/documentation/15.0/>`_. It allows
the project to take advantage of a vast ecosystem of existing integrations and modules.

`OpenSPP` is currently in development, and everything is evolving rapidly as a result of our users' comments.
If you have any questions or needs, please do not hesitate to contact the team through Github
issues or the `OpenSPP website <https://openspp.org/>`_.


Building the documentation
==========================

It is recommended that you use a virtual environment to build the documentation. This will allow you to install
the required dependencies without affecting your system.

Python 3.10 should be used to build the documentation. You can install it using your package manager or by
following the instructions on the `pyenv GitHub page <https://github.com/pyenv/pyenv>`_.

::

  cd docs
  pip install -r requirements.txt
  make html

::

Contributing to the documentation
=================================

If you want to contribute to the documentation, you can do so by following the steps below:

- Fork the repository
- Create a virtual environment and install the dependencies as described in the previous section.
- Set up pre-commit hooks to ensure that your code is compliant with the project's standards.
  ::

    pre-commit install

- Create a new branch
- Make your changes and commit them to your branch
- Submit a pull request

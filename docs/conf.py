# Configuration file for the Sphinx documentation builder.
# OpenSPP Documentation build configuration file


# -- Path setup --------------------------------------------------------------
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

from datetime import datetime
import os
import re
import sys
import logging
import json

from pathlib import Path
_logger = logging.getLogger(__name__)


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath("."))



#=== Odoo configuration ===#


odoo_current_branch = '17.0'
# `current_version` is the Odoo version linked to the current branch.
# E.g., saas-15.4 -> 15.4; 12.0 -> 12; master -> master (*).
odoo_current_version = odoo_current_branch.replace('saas-', '').replace('.0', '')
# `current_major_branch` is the technical name of the major branch before the current branch.
# E.g., saas-15.4 -> 15.0; 12.0 -> 12.0; master -> master (*).
odoo_current_major_branch = re.sub(r'\.\d', '.0', odoo_current_branch.replace('saas-', ''))
# `current_major_version` is the Odoo version linked to the current major branch.
# E.g., saas-15.4 -> 15; 12.0 -> 12; master -> master (*).
odoo_current_major_version = odoo_current_major_branch.replace('.0', '')
# (*): We don't care for master.


odoo_source_read_replace_vals = {
    'BRANCH': odoo_current_branch,
    'CURRENT_BRANCH': odoo_current_branch,
    'CURRENT_VERSION': odoo_current_version,
    'CURRENT_MAJOR_BRANCH': odoo_current_major_branch,
    'CURRENT_MAJOR_VERSION': odoo_current_major_version,
    'GITHUB_PATH': f'https://github.com/odoo/odoo/blob/{odoo_current_branch}',
    'GITHUB_ENT_PATH': f'https://github.com/odoo/enterprise/blob/{odoo_current_branch}',
}


# Search for the directory of odoo sources to know whether autodoc should be used on the dev doc
# odoo_sources_candidate_dirs = (Path('odoo'), Path('../odoo'), Path('../../dockerdoo/src/odoo'))
odoo_sources_candidate_dirs = (Path('../submodules/odoo'), )
odoo_sources_dirs = [
    d for d in odoo_sources_candidate_dirs if d.is_dir() and (d / 'odoo-bin').exists()
]
odoo_dir_in_path = False
print (odoo_sources_dirs)


if not odoo_sources_dirs:
    _logger.warning(
        "Could not find Odoo sources directory in neither of the following folders:\n"
        "%(dir_list)s\n"
        "The 'Developer' documentation will be built but autodoc directives will be skipped.\n"
        "In order to fully build the 'Developer' documentation, clone the repository with "
        "`git clone https://github.com/odoo/odoo` or create a symbolic link.",
        {'dir_list': '\n'.join([f'\t- {d.resolve()}' for d in odoo_sources_candidate_dirs])},
    )
else:
    if (3, 6) < sys.version_info < (3, 7):
        # Running odoo needs python 3.7 min but monkey patch version_info to be compatible with 3.6.
        sys.version_info = (3, 7, 0)
    odoo_dir = odoo_sources_dirs[0].resolve()
    odoo_source_read_replace_vals['ODOO_RELPATH'] = '/../' + str(odoo_sources_dirs[0])
    sys.path.insert(0, str(odoo_dir))
    print(f"Found Odoo sources in {odoo_dir}.")
    import odoo.addons

    # # import my addons
    # if "dockerdoo" in str(odoo_dir):
    #     print("Found Odoo sources in dockerdoo dev environment.")
    #     my_addons_dir = os.path.abspath(os.path.join(odoo_dir, '..', '..', 'custom'))
    #     my_addons_dir = Path(my_addons_dir)
    #     for folder in my_addons_dir.iterdir():
    #         if folder.is_dir():
    #             sys.path.insert(0, str(folder))
    #             odoo.addons.__path__.append(str(folder))
    #             print(f"Found custom addon in {folder}.")


    # First add Odoo's standard addons
    odoo.addons.__path__.append(str(odoo_dir) + '/addons')
    
    if "submodules" in str(odoo_dir):
        print("Found Odoo sources in submodules dev environment.")
        my_addons_dir = os.path.abspath(os.path.join(odoo_dir, '..'))
        my_addons_dir = Path(my_addons_dir)
        for folder in my_addons_dir.iterdir():
            if folder.is_dir() and not folder.name == 'odoo':
                sys.path.insert(0, str(folder))
                odoo.addons.__path__.append(str(folder))
                print(f"Found custom addon in {folder}.")
    from odoo import release as odoo_release  # Don't collide with Sphinx's 'release' config option
    odoo_version = odoo_release.version.replace('~', '-') \
        if 'alpha' not in odoo_release.version else 'master'
    
    _logger.info(
        "Found Odoo sources in %(directory)s matching documentation version '%(version)s'.",
        {'directory': odoo_dir, 'version': odoo_release},
    )
    odoo_dir_in_path = True

#### End of Odoo


# -- Project information -----------------------------------------------------

project = "OpenSPP Documentation"
copyright = "OpenSPP"
author = "The OpenSPP community"
trademark_name = "OpenSPP"
now = datetime.now()
year = str(now.year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1.3"
# The full version, including alpha/beta/rc tags.
release = "1.3"

# -- Multi-version configuration ----------------------------------------------
# Support environment-driven configuration for multi-version builds
DOCS_VERSION = os.getenv("DOCS_VERSION", "stable")
DOCS_BASEURL = os.getenv("DOCS_BASEURL", "https://docs.openspp.org/")
IS_PREVIEW = os.getenv("IS_PREVIEW", "0") == "1"

# Update version display based on environment
if DOCS_VERSION != "stable":
    version = DOCS_VERSION
    release = DOCS_VERSION

# -- General configuration ----------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named "sphinx.ext.*")
# or your custom ones.
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "sphinx_design",
    # "sphinx_sitemap",
    "sphinxcontrib.httpdomain", 
    "sphinxcontrib.httpexample",
    'sphinxcontrib.googleanalytics',
    "sphinxcontrib.video",
    "sphinxext.opengraph",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.graphviz",
    "sphinx_tabs.tabs",
    'sphinxcontrib.mermaid',
    "notfound.extension",
]

# Must come after extensions are defined
myst_fence_as_directive = ["mermaid"]

# Additional MyST configuration for fence directives
myst_dmath_double_inline = True
myst_all_links_external = False

sphinx_tabs_disable_tab_closing = True
sphinx_tabs_disable_css_loading = True

# -- Mermaid configuration ----------------------------------
mermaid_version = "10.6.1"
mermaid_init_js = """
mermaid.initialize({
    startOnLoad: true,
    theme: 'default',
    themeVariables: {
        primaryColor: '#0066cc',
        primaryTextColor: '#000000',
        primaryBorderColor: '#0066cc'
    }
});
"""

# -- sphinx-reredirects configuration ----------------------------------
# Redirect configuration for moved or renamed pages
# Format: "old-path": "new-path.html"
# Paths are relative to the documentation root
# NOTE: sphinx-reredirects is temporarily disabled due to version conflicts
# redirects = {
#     "best_practices/index.md": "developer_guide/best_practices.html",
#     "community_and_support/code_of_conduct.md": "community/code_of_conduct.html",
#     "community_and_support/how_to_contribute_to_the_project.md": "community/contributing.html",
#     "community_and_support/index.md": "community/index.html",
#     "community_and_support/l3_support.md": "community/support.html",
#     "community_and_support/license.md": "community/license.html",
#     "community_and_support/security_report.md": "community/security_reporting.html",
#     "contributing/admins.md": "community/contributing.html",
#     "contributing/authors.md": "community/contributing.html",
#     "contributing/index.md": "community/contributing.html",
#     "contributing/myst-reference.md": "community/contributing.html",
#     "contributing/setup-build.md": "community/contributing.html",
#     "contributing/sphinx-extensions.md": "community/contributing.html",
#     "explanation/Registering_individuals_and_groups.md": "overview/concepts/registrant_concepts.html",
#     "explanation/data_collection_validation.md": "overview/concepts/data_collection_validation.html",
#     "explanation/data_protection.md": "overview/concepts/data_protection.html",
#     "explanation/digital_public_infrastructure.md": "overview/concepts/digital_public_infrastructure.html",
#     "explanation/farmer_registry.md": "overview/concepts/farmer_registry.html",
#     "explanation/index.md": "overview/concepts/index.html",
#     "explanation/integrated_beneficiary_registry.md": "overview/concepts/integrated_beneficiary_registry.html",
#     "explanation/registry_key_concepts.md": "overview/concepts/registry_key_concepts.html",
#     "explanation/security_archi.md": "reference/technical/security.html",
#     "explanation/social_protection_management_information_systems.md": "overview/concepts/sp_mis.html",
#     "explanation/social_registry.md": "overview/concepts/social_registry.html",
#     "explanation/user_mgt.md": "overview/concepts/user_management.html",
#     "getting_started/creating_a_program.md": "user_guide/program_management/create_program.html",
#     "getting_started/installation_guide.md": "getting_started/installation_docker.html",
#     "glossary.rst": "reference/glossary.html",
#     "howto/developer_guides/beneficiary_keycloak.md": "developer_guide/integrations/keycloak_beneficiary_portal.html",
#     "howto/developer_guides/custom_areas.md": "developer_guide/customization/customizing_areas.html",
#     "howto/developer_guides/custom_audit.md": "developer_guide/customization/customizing_audit.html",
#     "howto/developer_guides/custom_cr.md": "developer_guide/customization/customizing_change_requests.html",
#     "howto/developer_guides/custom_cycle.md": "developer_guide/customization/customizing_cycles.html",
#     "howto/developer_guides/custom_entitlement.md": "developer_guide/customization/customizing_entitlements.html",
#     "howto/developer_guides/custom_fields_indicators.md": "developer_guide/customization/customizing_fields.html",
#     "howto/developer_guides/custom_program.md": "developer_guide/customization/customizing_programs.html",
#     "howto/developer_guides/custom_registry.md": "developer_guide/customization/customizing_registry.html",
#     "howto/developer_guides/custom_registry_tab_fields.md": "developer_guide/customization/customizing_registry.html",
#     "howto/developer_guides/custom_service_points.md": "developer_guide/customization/customizing_service_points.html",
#     "howto/developer_guides/dci.md": "developer_guide/integrations/dci.html",
#     "howto/developer_guides/development_setup.md": "developer_guide/setup.html",
#     "howto/developer_guides/esignet.md": "developer_guide/integrations/esignet.html",
#     "howto/developer_guides/implmenting_pmt.md": "developer_guide/customization/implementing_pmt.html",
#     "howto/developer_guides/indicators.md": "developer_guide/customization/customizing_indicators.html",
#     "howto/developer_guides/module.md": "developer_guide/module_development.html",
#     "howto/developer_guides/oidc.md": "developer_guide/integrations/oidc.html",
#     "howto/developer_guides/rest_api.md": "developer_guide/api_usage/rest_api.html",
#     "howto/developer_guides/setting_up_using_pypi.md": "getting_started/installation_pypi.html",
#     "howto/developer_guides/troubleshooting.md": "developer_guide/troubleshooting.html",
#     "howto/developer_mode.md": "developer_guide/developer_mode.html",
#     "howto/index.md": "user_guide/index.html",
#     "howto/translation.md": "community/contributing.html",
#     "howto/user_guides/administrating_role_based_access.md": "user_guide/administration/user_access.html",
#     "howto/user_guides/enroll_beneficiaries.md": "user_guide/program_management/enroll_beneficiaries.html",
#     "howto/user_guides/export_registrant_data.md": "user_guide/registry_management/import_export_data.html",
#     "howto/user_guides/implementing_pmt.md": "user_guide/program_management/implementing_pmt.html",
#     "howto/user_guides/import_registrant_data.md": "user_guide/registry_management/import_export_data.html",
#     "howto/user_guides/register_new_individual.md": "user_guide/registry_management/register_individual.html",
#     "howto/user_guides/setting_up_farmer_registry.md": "user_guide/registry_management/setting_up_farmer_registry.html",
#     "howto/user_guides/setting_up_service_points.md": "user_guide/administration/service_points.html",
#     "technical_reference/apis.md": "developer_guide/api_usage/index.html",
#     "technical_reference/architecture.md": "developer_guide/architecture.html",
#     "technical_reference/audit_logs.md": "reference/technical/audit_logs.html",
#     "technical_reference/backup.md": "reference/technical/backup.html",
#     "technical_reference/code.md": "developer_guide/best_practices.html",
#     "technical_reference/extensibility.md": "overview/concepts/extensibility.html",
#     "technical_reference/external_api.rst": "developer_guide/api_usage/external_api_xmlrpc.html",
#     "technical_reference/g2p-connect.md": "developer_guide/integrations/g2p-connect.html",
#     "technical_reference/index.md": "reference/index.html",
#     "technical_reference/integrations.md": "overview/features/integrations_apis.html",
#     "technical_reference/monitoring.md": "reference/technical/monitoring.html",
#     "technical_reference/openg2p.md": "overview/concepts/openg2p.html",
#     "technical_reference/performance_optimization.md": "reference/technical/performance.html",
#     "technical_reference/programs/concepts.md": "developer_guide/architecture.html",
#     "technical_reference/programs/cycle_manager.rst": "reference/technical/cycle_manager.html",
#     "technical_reference/programs/dashboards.md": "user_guide/reporting_dashboards.html",
#     "technical_reference/programs/deduplication_manager.md": "reference/technical/deduplication_manager.html",
#     "technical_reference/programs/eligibility_manager.rst": "reference/technical/eligibility_manager.html",
#     "technical_reference/programs/entitlement_manager.rst": "reference/technical/entitlement_manager.html",
#     "technical_reference/programs/index.md": "reference/technical/index.html",
#     "technical_reference/programs/notification_manager.rst": "reference/technical/notification_manager.html",
#     "technical_reference/programs/program_manager.rst": "reference/technical/program_manager.html",
#     "technical_reference/release_management.md": "community/release_management.html",
#     "technical_reference/security.md": "reference/technical/security.html",
#     "tutorial/access_management.md": "user_guide/administration/user_access.html",
#     "tutorial/audit_log.md": "user_guide/administration/using_audit_logs.html",
#     "tutorial/change_requests.md": "user_guide/registry_management/using_change_requests.html",
#     "tutorial/consent_management.md": "user_guide/consent_management.html",
#     "tutorial/custom_fields.md": "user_guide/administration/managing_custom_fields.html",
#     "tutorial/dashboards_and_reports.md": "user_guide/reporting_dashboards.html",
#     "tutorial/event_data.md": "user_guide/registry_management/using_event_data.html",
#     "tutorial/geotargeting.md": "user_guide/program_management/using_geotargeting.html",
#     "tutorial/grievance_redressal_management.md": "user_guide/grievance_management.html",
#     "tutorial/hardware_integration.md": "user_guide/administration/hardware_integration.html",
#     "tutorial/index.md": "user_guide/index.html",
#     "tutorial/indicators.md": "user_guide/program_management/using_indicators.html",
#     "tutorial/managing_social_protection_programs.md": "user_guide/program_management/index.html",
#     "tutorial/programs/export_beneficiaries.md": "user_guide/program_management/export_beneficiaries.html",
#     "tutorial/programs_and_cycles.md": "user_guide/program_management/programs_overview.html",
#     "tutorial/proxy_means_test.md": "user_guide/program_management/using_pmt.html",
#     "tutorial/user_guides/administrating_role_based_access.md": "user_guide/administration/user_access.html",
#     "tutorial/user_guides/allocate_funds.md": "user_guide/program_management/allocate_funds.html",
#     "tutorial/user_guides/configure_ID_generate_qr.md": "user_guide/registry_management/identity_management.html",
#     "tutorial/user_guides/configure_cash_entitlements.md": "user_guide/program_management/configure_entitlements.html",
#     "tutorial/user_guides/create_program_cycle_prepare_entitlements.md": "user_guide/program_management/create_cycle.html",
#     "tutorial/user_guides/create_social_protection_program.md": "user_guide/program_management/create_program.html",
#     "tutorial/user_guides/enroll_beneficiaries.md": "user_guide/program_management/enroll_beneficiaries.html",
#     "tutorial/user_guides/export_registrant_data.md": "user_guide/registry_management/import_export_data.html",
#     "tutorial/user_guides/import_areas.md": "user_guide/administration/import_areas.html",
#     "tutorial/user_guides/import_registrant_data.md": "user_guide/registry_management/import_export_data.html",
#     "tutorial/user_guides/point_of_sales.md": "user_guide/pos_usage.html",
#     "tutorial/user_guides/register_new_individual.md": "user_guide/registry_management/register_individual.html",
#     "tutorial/user_guides/setting_up_service_points.md": "user_guide/administration/service_points.html",
#     "tutorial/vouchers.md": "user_guide/program_management/using_vouchers.html",
# }

# If true, the Docutils Smart Quotes transform, originally based on SmartyPants
# (limited to English) and currently applying to many languages, will be used
# to convert quotes and dashes to typographically correct entities.
# Note to maintainers: setting this to `True` will cause contractions and
# hyphenated words to be marked as misspelled by spellchecker.
smartquotes = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = "sphinx.pygments_styles.PyramidStyle"
pygments_style = "sphinx"

# Only register CSV lexer on non-Windows platforms
import platform
if platform.system() != 'Windows':
    from pygments import token 
    from sphinx.highlighting import lexers
    from csvlexer.csv import CsvLexer

    lexers['csv'] = CsvLexer(startinline=True)

# Options for the linkcheck builder
# Ignore localhost
linkcheck_ignore = [
    r"http://localhost",
    r"http://0.0.0.0",
    r"http://127.0.0.1",
    r"^/_static/",
    r"https://www.researchgate.net/",
    
]
linkcheck_anchors = True
linkcheck_timeout = 10
linkcheck_retries = 2
# linkcheck_timeout = 5
# linkcheck_retries = 1

# The suffix of source filenames.
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

default_role = 'literal'

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "spelling_wordlist.txt",
    "**/CHANGES.rst",
    "**/CONTRIBUTORS.rst",
    "**/LICENSE.rst",
    "**/README.rst",
]

html_js_files = ["patch_scrollToActive.js", "search_shortcut.js", "version_switcher.js"]

# Only include robots.txt for stable builds
if not IS_PREVIEW:
    html_extra_path = [
        "_static/robots.txt",
        "_static/_redirects",
    ]
else:
    # Include redirects in previews too for validation
    html_extra_path = [
        "_static/_redirects",
    ]

html_static_path = [
    "_static",  # Last path wins. So this one will override the default theme's static files.
]

# -- Options for myST markdown conversion to html -----------------------------

# For more information see:
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    "deflist",  # You will be able to utilise definition lists
    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#definition-lists
    "linkify",  # Identify “bare” web URLs and add hyperlinks.
    "colon_fence",  # You can also use ::: delimiters to denote code fences,\
    #  instead of ```.
    "substitution", # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2
    "html_image",  # For inline images. See https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
]

# MyST html_meta configuration - disabled due to incorrect behavior
# myst_html_meta = {
#     "review-status": "review-status",
#     "review-date": "review-date", 
#     "reviewer": "reviewer",
#     "migration-notes": "migration-notes"
# }

myst_substitutions = {
    "postman_basic_auth": "![](../_static/img/postman_basic_auth.png)",
    "postman_headers": "![](../_static/img/postman_headers.png)",
    "postman_request": "![](../_static/img/postman_request.png)",
    "postman_response": "![](../_static/img/postman_response.png)",
    "postman_retain_headers": "![](../_static/img/postman_retain_headers.png)",
    "fawrench": '<span class="fa fa-wrench" style="font-size: 1.6em;"></span>',
}

# -- Intersphinx configuration ----------------------------------

# This extension can generate automatic links to the documentation of objects
# in other projects. Usage is simple: whenever Sphinx encounters a
# cross-reference that has no matching target in the current documentation set,
# it looks for targets in the documentation sets configured in
# intersphinx_mapping. A reference like :py:class:`zipfile.ZipFile` can then
# linkto the Python documentation for the ZipFile class, without you having to
# specify where it is located exactly.
#
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
#
# Note that OpenSPP Documentation imports documentation from several remote repositories.
# These projects need to build their docs as part of their CI/CD and testing.
# We use Intersphinx to resolve targets when either the individual project's or
# the entire OpenSPP Documentation is built.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "odoo": ("https://www.odoo.com/documentation/17.0/", None),
}


# -- GraphViz configuration ----------------------------------

graphviz_output_format = "svg"


# -- OpenGraph configuration ----------------------------------

ogp_site_url = "https://docs.openspp.org/"
ogp_description_length = 200
ogp_image = "https://docs.openspp.org/_static/openspp_logo.png"
ogp_site_name = "OpenSPP Documentation"
ogp_type = "website"
ogp_custom_meta_tags = [
    '<meta property="og:locale" content="en_US" />',
]


# -- sphinx_copybutton -----------------------
copybutton_prompt_text = r"^ {0,2}\d{1,3}"
copybutton_prompt_is_regexp = True


# -- sphinx-notfound-page configuration ----------------------------------

notfound_urls_prefix = ""
notfound_template = "404.html"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# html_logo = "_static/logo.svg"
html_favicon = "_static/icon_192.png"

html_css_files = ["custom.css", ("print.css", {"media": "print"})]

# See http://sphinx-doc.org/ext/todo.html#confval-todo_include_todos
todo_include_todos = True

# Announce that we have an opensearch plugin
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_use_opensearch
html_use_opensearch = "https://docs.openspp.org"

html_sidebars = {
    "**": [
        "sidebar-logo.html",
        "search-field.html",
        "sbt-sidebar-nav.html",
    ]
}

html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/openspp/documentation",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "search_bar_text": "Search",
    "extra_navbar": """
    <p class="openspporglink">
        <a href="https://openspp.org">
            <img src="/_static/openspp_logo.png" alt="openspp.org" /> openspp.org</a>
    </p>""",
    "extra_footer": """<p>The text and illustrations in this website are licensed by the OpenSPP Project under a Creative Commons Attribution 4.0 International license. All other trademarks are owned by their respective owners.</p>
    """,
}

# Version switcher configuration (for future theme versions)
# Note: sphinx-book-theme 0.3.3 doesn't have built-in version switcher support
# Using custom JavaScript implementation in version_switcher.js instead
html_theme_options["switcher"] = {
    "json_url": "https://docs.openspp.org/_static/switcher.json", 
    "version_match": DOCS_VERSION,
}

# Add announcement banner for preview builds
if IS_PREVIEW:
    html_theme_options["announcement"] = f"""
    <p><strong>⚠️ Preview Documentation</strong>: You are viewing a preview build from branch <code>{DOCS_VERSION}</code>. 
    For the stable documentation, visit <a href="https://docs.openspp.org/">docs.openspp.org</a></p>
    """

googleanalytics_id = 'G-RS4T4ZPG52'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "%(project)s v%(release)s" % {"project": project, "release": release}

# If false, no index is generated.
html_use_index = True

# Used by sphinx_sitemap to generate a sitemap
html_baseurl = DOCS_BASEURL
sitemap_url_scheme = "{link}"

# -- Options for HTML help output -------------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "OpenSPPDocumentation"


# -- Options for LaTeX output -------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual])
latex_documents = [
    (
        "index",
        "OpenSPPDocumentation.tex",
        "OpenSPP Documentation",
        "The OpenSPP community",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/logo_2x.png"


# suggest edit link
# remark: {{ file_name }} is mandatory in "edit_page_url_template"
html_context = {
    "edit_page_url_template": "https://docs.openspp.org/contributing/?{{ file_name }}#making-contributions-on-github",
    "display_github": True,
    "github_user": "openspp",  # Username
    "github_repo": "documentation",  # Repo name
    "github_version": "main",  # Version
    "conf_py_path": "/docs/",  # Path in the checkout to the docs root
    "is_preview": IS_PREVIEW,  # Flag for preview builds to add noindex meta tag
}

# An extension that allows replacements for code blocks that
# are not supported in `rst_epilog` or other substitutions.
# https://stackoverflow.com/a/56328457/2214933
def source_replace(app, docname, source):
    result = source[0]
    for key in app.config.source_replacements:
        result = result.replace(key, app.config.source_replacements[key])
    source[0] = result


def modify_sitemap(app, exception):
    if exception is None:  # Only run if the build was successful
        sitemap_path = os.path.join(app.outdir, 'sitemap.xml')
        if os.path.exists(sitemap_path):
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

            for url in root.findall('ns:url', namespace):
                loc = url.find('ns:loc', namespace)
                if loc.text and loc.text.endswith('/index.html'):
                    loc.text = loc.text[:-10]  # Remove 'index.html'

            tree.write(sitemap_path, xml_declaration=True, encoding='utf-8')


def update_html_files(app, exception):
    if exception is None:  # Only run if the build was successful
        for root, dirs, files in os.walk(app.outdir):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        soup = BeautifulSoup(file, 'html.parser')

                    # Update the canonical link
                    canonical_link = soup.find('link', {'rel': 'canonical'})
                    if canonical_link and canonical_link['href'].endswith('/index.html'):
                        canonical_link['href'] = canonical_link['href'][:-10]

                    # Update internal reference links
                    for a_tag in soup.find_all('a', {'class': 'reference internal'}):
                        href = a_tag.get('href', '')
                        if href.endswith('index.html'):
                            a_tag['href'] = href[:-10]

                    # update home logo link
                    home_link = soup.find('a', {'class': 'navbar-brand text-wrap'})
                    if home_link and home_link['href'].endswith('/index.html'):
                        home_link['href'] = home_link['href'][:-10]

                    # Write the changes back to the file
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(str(soup))

# def setup(app):
    # app.connect('build-finished', modify_sitemap)
    # app.connect('build-finished', update_html_files)

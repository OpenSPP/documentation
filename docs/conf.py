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

from pathlib import Path
_logger = logging.getLogger(__name__)


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath("."))

# Add local extensions directory for custom Pygments lexers
sys.path.insert(0, os.path.abspath("_ext"))



#=== Odoo configuration ===#


odoo_current_branch = "19.0"
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
    try:
        import odoo.addons
    except Exception as exc:  # pragma: no cover - build-environment dependent
        _logger.warning(
            "Found Odoo sources, but failed to import Odoo. Autodoc directives depending on Odoo will be skipped.\n"
            "Error: %(error)s",
            {"error": exc},
        )
    else:

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


        if "submodules" in str(odoo_dir):
            print("Found Odoo sources in submodules dev environment.")
            my_addons_dir = os.path.abspath(os.path.join(odoo_dir, ".."))
            my_addons_dir = Path(my_addons_dir)
            for folder in my_addons_dir.iterdir():
                if folder.is_dir() and not folder.name == "odoo":
                    sys.path.insert(0, str(folder))
                    odoo.addons.__path__.append(str(folder))
                    print(f"Found custom addon in {folder}.")

        odoo.addons.__path__.append(str(odoo_dir) + "/addons")
        from odoo import release as odoo_release  # Don't collide with Sphinx's 'release' config option

        odoo_version = odoo_release.version.replace("~", "-") if "alpha" not in odoo_release.version else "master"

        _logger.info(
            "Found Odoo sources in %(directory)s matching documentation version '%(version)s'.",
            {"directory": odoo_dir, "version": odoo_release},
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
version = "1.1"
# The full version, including alpha/beta/rc tags.
release = "1.1"

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
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.httpexample",
    "sphinxcontrib.video",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.autosummary",
    "sphinx.ext.graphviz",
    "sphinx_tabs.tabs",
    "cel_lexer",  # Custom CEL expression syntax highlighting
    "sphinxcontrib.mermaid",  # Mermaid diagrams (flowcharts, sequence, state)
]

# Extensions that slow down builds - only load for production
if not os.environ.get("SPHINX_DEV_BUILD"):
    extensions += [
        "sphinx_sitemap",
        "sphinxcontrib.googleanalytics",
        "notfound.extension",
        "sphinx_reredirects",  # URL redirects for documentation restructure
    ]

# Mermaid configuration
# For offline/air-gapped builds, set MERMAID_OFFLINE=svg and install mermaid-cli:
#   npm install -g @mermaid-js/mermaid-cli
# This will pre-render diagrams to SVG at build time (no JavaScript needed at runtime)
_mermaid_offline = os.environ.get("MERMAID_OFFLINE", "") == "svg"
mermaid_output_format = "svg" if _mermaid_offline else "raw"
mermaid_version = "11.4.0"  # Pin mermaid version for stability
# Use puppeteer config for no-sandbox mode (required on Ubuntu 23.10+)
mermaid_cmd = ["mmdc", "--puppeteerConfigFile", os.path.join(os.path.dirname(__file__), "_static/puppeteer-config.json")]
mermaid_include_elk = False  # Disable ELK layout to reduce dependencies
mermaid_init_js = "" if _mermaid_offline else "mermaid.initialize({startOnLoad:true});"

# Monkeypatch sphinxcontrib.mermaid to skip JS loading in offline/SVG mode
if _mermaid_offline:
    import sphinxcontrib.mermaid
    _original_install_js = sphinxcontrib.mermaid.install_js
    def _patched_install_js(app, pagename, templatename, context, doctree):
        # Skip JS installation entirely when rendering to SVG
        if app.config.mermaid_output_format == "svg":
            return
        return _original_install_js(app, pagename, templatename, context, doctree)
    sphinxcontrib.mermaid.install_js = _patched_install_js

# -- External links configuration ----------------------------------
# Shortcuts for linking to GitHub source files
# Usage in MyST: {gh-spp}`spp_drims/models/donation.py`
# Usage in RST: :gh-spp:`spp_drims/models/donation.py`

extlinks = {
    # OpenSPP modules v2 repository
    'gh-spp': (
        f'https://github.com/openspp/openspp-modules-v2/blob/{odoo_current_branch}/%s',
        '%s',
    ),
    # DRIMS module shortcut
    'gh-drims': (
        f'https://github.com/openspp/openspp-modules-v2/blob/{odoo_current_branch}/spp_drims/%s',
        'spp_drims/%s',
    ),
    # Odoo core (for reference)
    'gh-odoo': (
        f'https://github.com/odoo/odoo/blob/{odoo_current_branch}/%s',
        'odoo/%s',
    ),
}

# Some optional extensions depend on Pillow. In environments where Pillow cannot
# be imported (for example, Python versions without compatible wheels), build
# the documentation without those extensions.
_pillow_available = True
try:
    from PIL import Image  # noqa: F401
except Exception as exc:  # pragma: no cover - build-environment dependent
    _pillow_available = False
    _logger.warning("Pillow is not available (%s). Disabling sphinxext.opengraph.", exc)

if _pillow_available and not os.environ.get("SPHINX_DEV_BUILD"):
    extensions.append("sphinxext.opengraph")

sphinx_tabs_disable_tab_closing = True
sphinx_tabs_disable_css_loading = True

# If true, the Docutils Smart Quotes transform, originally based on SmartyPants
# (limited to English) and currently applying to many languages, will be used
# to convert quotes and dashes to typographically correct entities.
# Note to maintainers: setting this to `True` will cause contractions and
# hyphenated words to be marked as misspelled by spellchecker.
smartquotes = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = "sphinx.pygments_styles.PyramidStyle"
pygments_style = "friendly"

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

html_js_files = [
    ("https://code.jquery.com/jquery-3.7.1.min.js", {"integrity": "sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=", "crossorigin": "anonymous"}),
    ("https://cdn.jsdelivr.net/npm/mermaid@11.4.0/dist/mermaid.min.js", {}),
    "mermaid_init.js",
    "patch_scrollToActive.js",
    "search_shortcut.js",
]

html_extra_path = [
    "robots.txt",
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
    "odoo": ("https://www.odoo.com/documentation/15.0/", None),
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


# -- sphinx-reredirects configuration ----------------------------------
# URL redirects for documentation restructure (Phase 1 setup, populated in Phase 3)
# Format: "old/path.html": "new/path.html"
# These redirects will be populated as content is migrated to the new structure.
# See DOCUMENTATION_IMPLEMENTATION_PLAN.md for the full migration plan.

redirects = {
    # Phase 3: CEL Consolidation redirects (11 files → 6 files) - ACTIVE
    "tutorial/cel_quickstart.html": "config_guide/cel/quick_start.html",
    "tutorial/cel_cookbook.html": "config_guide/cel/cookbook.html",
    "tutorial/cel_troubleshooting.html": "config_guide/cel/troubleshooting.html",
    "tutorial/variables_and_expressions.html": "config_guide/cel/variables.html",
    "technical_reference/cel/index.html": "config_guide/cel/index.html",
    "technical_reference/cel/usage_by_feature.html": "config_guide/cel/variables.html",
    "technical_reference/cel/profiles_and_symbols.html": "config_guide/cel/variables.html",
    "technical_reference/cel/variables.html": "config_guide/cel/variables.html",
    "technical_reference/cel/expressions.html": "config_guide/cel/syntax.html",
    "technical_reference/cel/events.html": "config_guide/cel/variables.html",
    "technical_reference/cel/widget_and_validation.html": "config_guide/cel/syntax.html",
    "technical_reference/cel/caching_and_metric.html": "developer_guide/architecture/cel_internals.html",

    # Phase 3: User Guide Deduplication redirects - ACTIVE
    "tutorial/user_guides/register_new_individual.html": "user_guide/registry/register_individual.html",
    "tutorial/user_guides/register_new_individual/index.html": "user_guide/registry/register_individual.html",
    "howto/user_guides/register_new_individual.html": "user_guide/registry/register_individual.html",
    "howto/user_guides/register_new_individual/index.html": "user_guide/registry/register_individual.html",
    "tutorial/user_guides/enroll_beneficiaries.html": "user_guide/programs/enroll.html",
    "tutorial/user_guides/enroll_beneficiaries/index.html": "user_guide/programs/enroll.html",
    "howto/user_guides/enroll_beneficiaries.html": "user_guide/programs/enroll.html",
    "howto/user_guides/enroll_beneficiaries/index.html": "user_guide/programs/enroll.html",
    "tutorial/user_guides/import_registrant_data.html": "user_guide/registry/import.html",
    "tutorial/user_guides/import_registrant_data/index.html": "user_guide/registry/import.html",
    "howto/user_guides/import_registrant_data.html": "user_guide/registry/import.html",
    "howto/user_guides/import_registrant_data/index.html": "user_guide/registry/import.html",
    "tutorial/user_guides/export_registrant_data.html": "user_guide/registry/export.html",
    "tutorial/user_guides/export_registrant_data/index.html": "user_guide/registry/export.html",
    "howto/user_guides/export_registrant_data.html": "user_guide/registry/export.html",
    "howto/user_guides/export_registrant_data/index.html": "user_guide/registry/export.html",

    # Phase 3: Orphan Resolution redirects - ACTIVE
    "tutorial/managing_social_protection_programs.html": "learn/concepts/programs.html",
    "tutorial/managing_social_protection_programs/index.html": "learn/concepts/programs.html",
    "howto/developer_guides/custom_cycle.html": "developer_guide/extending/cycle_manager.html",
    "howto/developer_guides/custom_cycle/index.html": "developer_guide/extending/cycle_manager.html",
    "howto/developer_guides/custom_program.html": "developer_guide/extending/custom_modules.html",
    "howto/developer_guides/custom_program/index.html": "developer_guide/extending/custom_modules.html",
    "howto/developer_guides/implmenting_pmt.html": "config_guide/scoring/pmt.html",
    "howto/developer_guides/implmenting_pmt/index.html": "config_guide/scoring/pmt.html",
    "howto/translation.html": "index.html",
    "getting_started/creating_a_program.html": "get_started/first_program/index.html",
    "tutorial/programs/export_beneficiaries.html": "user_guide/registry/export.html",

    # Phase 3: Partial Content Migration redirects - ACTIVE
    # API V2 Migration
    "technical_reference/api_v2/index.html": "developer_guide/api_v2/index.html",
    "technical_reference/api_v2/authentication.html": "developer_guide/api_v2/authentication.html",
    "technical_reference/api_v2/clients_and_scopes.html": "developer_guide/api_v2/authentication.html",
    "technical_reference/api_v2/resources.html": "developer_guide/api_v2/resources.html",
    "technical_reference/api_v2/search.html": "developer_guide/api_v2/search.html",
    "technical_reference/api_v2/batch.html": "developer_guide/api_v2/batch.html",
    "technical_reference/api_v2/extensions.html": "developer_guide/api_v2/external_identifiers.html",
    "technical_reference/api_v2/errors.html": "developer_guide/api_v2/errors.html",
    "technical_reference/api_v2/consent_model.html": "developer_guide/api_v2/consent.html",
    # Security Migration
    "technical_reference/access_rights.html": "ops_guide/security/access_control.html",
    "technical_reference/access_rights/index.html": "ops_guide/security/access_control.html",
    # Scoring Migration
    "tutorial/proxy_means_test.html": "config_guide/scoring/pmt.html",
    "tutorial/proxy_means_test/index.html": "config_guide/scoring/pmt.html",
    # Event Data Migration
    "tutorial/event_data.html": "config_guide/event_data/index.html",
    "tutorial/event_data/index.html": "config_guide/event_data/index.html",

    # Add more redirects as content is migrated
}


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

googleanalytics_id = 'G-RS4T4ZPG52'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "%(project)s v%(release)s" % {"project": project, "release": release}

# If false, no index is generated.
html_use_index = True

# Used by sphinx_sitemap to generate a sitemap
html_baseurl = "https://docs.openspp.org/"
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
    # Skip during livehtml/dev builds for speed
    if os.environ.get("SPHINX_DEV_BUILD"):
        return
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
    # Skip during livehtml/dev builds for speed
    if os.environ.get("SPHINX_DEV_BUILD"):
        return
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

def setup(app):
    app.connect('build-finished', modify_sitemap)
    app.connect('build-finished', update_html_files)

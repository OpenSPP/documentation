# Configuration file for the Sphinx documentation builder.
# OpenSPP Documentation build configuration file


# -- Path setup --------------------------------------------------------------

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



#=== Odoo configuration ===#


odoo_current_branch = '15.0'
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


    if "submodules" in str(odoo_dir):
        print("Found Odoo sources in submodules dev environment.")
        my_addons_dir = os.path.abspath(os.path.join(odoo_dir, '..'))
        my_addons_dir = Path(my_addons_dir)
        for folder in my_addons_dir.iterdir():
            if folder.is_dir() and not folder.name == 'odoo':
                sys.path.insert(0, str(folder))
                odoo.addons.__path__.append(str(folder))
                print(f"Found custom addon in {folder}.")

    odoo.addons.__path__.append(str(odoo_dir) + '/addons')
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
version = "1.0"
# The full version, including alpha/beta/rc tags.
release = "1.0"

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
    "sphinx_sitemap",
    "sphinxcontrib.httpdomain", 
    "sphinxcontrib.httpexample",
    'sphinxcontrib.googleanalytics',
    "sphinxcontrib.video",
    "sphinxext.opengraph",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.graphviz",
    "sphinx_tabs.tabs",
    "notfound.extension",
]

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
pygments_style = "sphinx"

# Options for the linkcheck builder
# Ignore localhost
linkcheck_ignore = [
    r"http://localhost",
    r"http://0.0.0.0",
    r"http://127.0.0.1",
    r"^/_static/",
]
linkcheck_anchors = True
# linkcheck_timeout = 10
# linkcheck_retries = 2
linkcheck_timeout = 5
linkcheck_retries = 1

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

html_js_files = ["patch_scrollToActive.js", "search_shortcut.js"]

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
html_baseurl = "https://docs.openspp.org"

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
    "edit_page_url_template": "https://docs.openspp.org/contributing/index.html?{{ file_name }}#making-contributions-on-github",
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

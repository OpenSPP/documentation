import os
import re
import sys
import logging

from pathlib import Path
_logger = logging.getLogger(__name__)


from sphinx.locale import _

# Prefer to use the version of the theme in this repo
# and not the installed version of the theme.
sys.path.insert(0, os.path.abspath("../../../openg2p-program/"))
sys.path.insert(0, os.path.abspath(".."))
# sys.path.append(os.path.abspath("./demo/"))
# sys.path.append(os.path.abspath("./using/"))


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
odoo_sources_candidate_dirs = (Path('odoo'), Path('../odoo'), Path('../../dockerdoo/src/odoo'))
odoo_sources_dirs = [
    d for d in odoo_sources_candidate_dirs if d.is_dir() and (d / 'odoo-bin').exists()
]
odoo_dir_in_path = False


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

    # import my addons
    if "dockerdoo" in str(odoo_dir):
        print("Found Odoo sources in dockerdoo dev environment.")
        my_addons_dir = os.path.abspath(os.path.join(odoo_dir, '..', '..', 'custom'))
        my_addons_dir = Path(my_addons_dir)
        # my_addons_dir = odoo_dir.__parent__.__parent__ / "custom"
        for folder in my_addons_dir.iterdir():
            if folder.is_dir():
                sys.path.insert(0, str(folder))
                odoo.addons.__path__.append(str(folder))
                print(f"Found custom addon in {folder}.")


    odoo.addons.__path__.append(str(odoo_dir) + '/addons')
    from odoo import release as odoo_release  # Don't collide with Sphinx's 'release' config option
    odoo_version = odoo_release.version.replace('~', '-') \
        if 'alpha' not in odoo_release.version else 'master'
    if odoo_release != odoo_version:
        _logger.warning(
            "Found Odoo sources in %(directory)s but with version '%(odoo_version)s' incompatible "
            "with documentation version '%(doc_version)s'.\n"
            "The 'Developer' documentation will be built but autodoc directives will be skipped.\n"
            "In order to fully build the 'Developer' documentation, checkout the matching branch"
            " with `cd odoo && git checkout %(doc_version)s`.",
            {'directory': odoo_dir, 'odoo_version': odoo_version, 'doc_version': odoo_version},
        )
    else:
        _logger.info(
            "Found Odoo sources in %(directory)s matching documentation version '%(version)s'.",
            {'directory': odoo_dir, 'version': odoo_release},
        )
        odoo_dir_in_path = True

#### End of Odoo


project = "OpenSPP"
slug = re.sub(r"\W+", "-", project.lower())
version = "2.0-dev"
# release = theme_version_full
author = "OpenSPP.org"
# copyright = author
copyright = (  # pylint: disable=redefined-builtin
    "2023 OpenSPP.org Licensed under CC BY 4.0"
)
language = "en"
sd_fontawesome_latex = True


extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinxcontrib.youtube",
    # "sphinxcontrib.bibtex",
    "sphinxcontrib.httpdomain",
    "sphinx_design",
    # "sphinx_rtd_theme",
    "myst_parser",
    "autodocsumm",
    "sphinx_reredirects",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "sphinx_togglebutton",
    "sphinxext.opengraph",
]

templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
locale_dirs = ["locale/"]
gettext_compact = False

# add the config to make sure the file ".well-known/security.txt" is not converted to html by sphinx
html_extra_path = [".well-known/"]


myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
    "colon_fence",
]

master_doc = "index"
suppress_warnings = ["myst.domains", "ref.ref", "image.nonlocal_uri"]
pygments_style = "default"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
    # "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    # "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

html_theme = "sphinx_book_theme"
html_title = "OpenSPP - Social Protection Platform Documentation"
html_copy_source = True

html_sourcelink_suffix = ""
# html_favicon = "_static/logo-square.svg"
html_last_updated_fmt = ""

html_theme_options = {
    # "logo_only": False,
    # "navigation_depth": 5,
    # "style_external_links": True,
    "home_page_in_toc": True,
    "path_to_docs": "docs",
    "repository_url": "https://github.com/OpenSPP/documentation",
    "repository_branch": "main",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/OpenSPP",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Linkedin",
            "url": "https://www.linkedin.com/company/87212895/",
            "icon": "fab fa-linkedin-square",
        },
    ],
    "navbar_start": ["navbar-logo", "version-switcher"],
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "use_sidenotes": True,
    # "logo_only": True,
    "search_bar_text": "Search OpenSPP...",
    "show_toc_level": 2,
    # "switcher": {
    #     "json_url": "https://sphinx-primer.readthedocs.io/en/latest/_static/switcher.json",
    #     "version_match": os.environ.get("READTHEDOCS_LANGUAGE", "en")
    # },
}
html_context = {
    "display_github": True,
    "github_user": "openspp",  # Username
    "github_repo": "documentation",  # Repo name
    "github_version": "main",  # Version
    "conf_py_path": "/docs/",  # Path in the checkout to the docs root
    "doc_path": ".",
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]


# Used by sphinx.ext.githubpages to generate docs/CNAME
html_baseurl = "https://docs.openspp.org"

if "READTHEDOCS" not in os.environ:
    html_static_path = ["_static/"]
    html_js_files = ["debug.js"]

    # Add fake versions for local QA of the menu
    # html_context["test_versions"] = list(map(lambda x: str(x / 10), range(1, 100)))

# html_logo = "https://openspp.org/wp-content/uploads/2022/08/logo_lite-1.svg"
html_show_sourcelink = True

htmlhelp_basename = slug


latex_documents = [
    ("index", "{}.tex".format(slug), project, author, "manual"),
]

man_pages = [("index", slug, project, [author], 1)]

texinfo_documents = [
    ("index", slug, project, author, slug, project, "Miscellaneous"),
]

redirects = {
    "code_of_conduct": "community_and_support/code_of_conduct",
    "security-report": "community_and_support/security_report",
    "installation": "getting_started/installation_guide",
}


# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
        doc_field_types=[
            PyField(
                "type",
                label=_("Type"),
                has_arg=False,
                names=("type",),
                bodyrolename="class",
            ),
            Field(
                "default",
                label=_("Default"),
                has_arg=False,
                names=("default",),
            ),
        ],
    )
    # if not os.environ.get("READTHEDOCS") and not os.environ.get("GITHUB_ACTIONS"):
    #     app.add_css_file(
    #         "https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css"
    #     )
    #     app.add_css_file("https://assets.readthedocs.org/static/css/badge_only.css")
    #
    #     # Create the dummy data file so we can link it
    #     # ref: https://github.com/readthedocs/readthedocs.org/blob/bc3e147770e5740314a8e8c33fec5d111c850498/readthed
    #     ocs/core/static-src/core/js/doc-embed/footer.js  # noqa: E501
    #     app.add_js_file("rtd-data.js")
    #     app.add_js_file(
    #         "https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js",
    #         priority=501,
    #     )


# import odoo
autodoc_mock_imports = ["odoo.addons.phone_validation"]
# autodoc_default_options = {
#     'autosummary': True,
# }

todo_include_todos = True

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

import os
import re
import sys

from sphinx.locale import _

# Prefer to use the version of the theme in this repo
# and not the installed version of the theme.
sys.path.insert(0, os.path.abspath("../../../openg2p-program/"))
sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("./demo/"))
sys.path.append(os.path.abspath("./using/"))


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

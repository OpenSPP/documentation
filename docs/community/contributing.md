---
review-status: needs-review
review-date: 2025-06-04
reviewer: migration-script
migration-notes: "Added during 2025 documentation reorganization"
---

# Contributing

Thank you for considering contributing to the OpenSPP project! We welcome and appreciate contributions from
the community, and are grateful for the time and effort that people put into improving the project.

## Code of Conduct

We expect all contributors to the OpenSPP project to adhere to our [Code of Conduct](code_of_conduct.md).
This document outlines the standards of behavior that we expect from all members of the community, and
provides guidance on how to report any incidents of misconduct.

## **Did you find a bug?**

- **Do not open up a GitHub issue if the bug is a security vulnerability in OpenSPP**, and instead follow the
  [security disclosure policy](security_report).

- **Ensure the bug was not already reported** by searching on GitHub under
  [Issues](https://github.com/openspp/documentation/issues).

- If you're unable to find an open issue addressing the problem,
  [open a new one](https://github.com/openspp/documentation/issues/new). Be sure to include a **title and
  clear description**, as much relevant information as possible demonstrating the expected behavior that is
  not occurring.

## Contributing to the code

### Getting Started

Before you start working on a new feature or bug fix, it's a good idea to check the project's issue tracker to
see if someone else is already working on it. If you find an open issue that you'd like to work on, you can
comment on the issue to let people know that you're planning to take it on.

If you don't see any open issues that match your area of expertise, feel free to open a new issue to propose a
new feature or report a bug. Make sure to include as much detail as possible, and to clearly describe the
problem or feature that you're proposing.

### Submitting a Pull Request

Once you have made your changes, you can submit a pull request (PR) to propose your changes for review and
inclusion in the project. Here are some tips for making a successful PR:

- Make sure that your PR is focused on a single issue or feature. Avoid bundling multiple unrelated changes in
  a single PR.
- Write clear and concise commit messages that explain the purpose of each change.
- Follow the project's coding style and conventions.
- Test your code thoroughly before submitting your PR. Make sure that all unit tests pass, and consider adding
  additional tests if necessary.
- Ensure that your code is well-documented using reStructuredText markup, with clear and concise comments
  explaining any non-obvious code.
- Make sure that your PR is reviewed by at least one other contributor before submitting.
- Address any feedback or issues raised during the review process in a timely manner.
- If your PR involves any significant changes or new features, consider writing documentation or updating the
  project's README to reflect these changes.
- Make sure that your PR is up to date with the latest version of the codebase before submitting.
- If your PR is large or complex, consider breaking it down into smaller, more manageable chunks that can be
  reviewed and merged more easily.

### Documentation Update

If your PR involves any significant changes or new features, it is important to update the project's
documentation to reflect these changes. This will help users and developers understand how to use and work
with the updated code.

To update the documentation, you should edit the relevant documentation and submit a separate PR with your
documentation changes to the [documentation](https://github.com/openspp/documentation) project.

When updating the documentation, make sure to:

- Clearly and concisely describe the changes that have been made.
- Provide examples or code snippets to illustrate how to use the new or updated features.
- Update any relevant reference documentation or API documentation.
- Test the documentation to ensure that it is accurate and up-to-date.

Updating the documentation is an important part of the PR process, and will help to ensure that the project is
easy to use and understand for all users and developers.

### Review Process

Once you have submitted your PR, it will be reviewed by one or more contributors to the project. The review
process is an opportunity for the project maintainers to provide feedback on your code, and for you to address
any issues or concerns that are raised.

During the review process, you may be asked to make changes to your code, or to provide additional information
or clarification. It's important to be responsive to these requests, as it will help to ensure that your PR is
accepted and merged in a timely manner.

Some things to keep in mind during the review process:

- Be open to feedback and suggestions. The review process is meant to help improve the quality and reliability
  of the project, and to ensure that all code meets the standards of the project.
- Address all issues and concerns raised during the review process. If you disagree with a suggestion or
  comment, feel free to engage in a constructive dialogue to reach a resolution.
- If you are asked to make changes to your code, try to make these changes as soon as possible. This will help
  to keep the review process moving forward and ensure that your PR is reviewed and merged in a timely manner.

Once all issues have been addressed and the code has been approved by the reviewers, your PR will be ready to
be merged into the project.

### Merging a Pull Request

Once your PR has been reviewed and all issues have been addressed, it can be merged into the project. In most
cases, PRs will be merged by the project maintainers, but in some cases, contributors may be granted the
ability to merge their own PRs.

Before merging a PR, it is important to double-check that all of the following conditions have been met:

- The PR has been reviewed and approved by at least one other contributor.
- All issues and concerns raised during the review process have been addressed.
- The code has been tested and is known to be in good working order.
- The PR is up to date with the latest version of the codebase.
- Once these conditions have been met, the PR can be safely merged into the project. This can usually be done
  with a single click using the "Merge" button in the GitHub interface.

After your PR has been merged, it will become part of the official project codebase, and will be included in
the next release of OpenSPP. Congratulations on your contribution!

## Contributing to the documentation

If you want to contribute to the [documentation](https://docs.openspp.org/), you can do so by following the
steps below:

- Fork the [documentation repository](https://github.com/OpenSPP/documentation).

- Fork the project's [documentation repository](https://github.com/OpenSPP/documentation)
- Make your changes in a new branch. It is recommended to name your branch something descriptive, such as
  "feature/new-section" or "bugfix/typo-correction".
- Before making any changes, ensure that you have the necessary dependencies installed and that you have a
  local version of the documentation set up. This can typically be done by installing Sphinx, and then running
  the command `make html` to build the documentation.
- Install pre-commit by running `pip install pre-commit` or `brew install pre-commit` depending on your
  system.
- Once you have made your changes, use the command `make html` again to rebuild the documentation and check
  that your changes display correctly.
- Configure pre-commit by running `pre-commit install`.
- Before committing any changes, make sure to run the project's pre-commit checks:
  `pre-commit run --all-files`. These checks will ensure that the code adheres to the project's style
  guidelines and that there are no obvious errors or issues.
- Commit your changes with a clear and descriptive commit message.
- Push your branch to your fork of the repository.
- Submit a pull request to the main repository for review.
- Make sure that you have explained in the pull request what changes you've made and why. And if there's any
  specific instructions or dependencies need to be followed.
- The project lead or maintainers will review the pull request and provide feedback. If any revisions are
  requested, make the necessary changes and push them to the same branch on your fork.
- Once your pull request is approved, it will be merged into the main repository.

### Building the documentation

It is recommended that you use a virtual environment to build the documentation. This will allow you to
install the required dependencies without affecting your system.

Python 3.10 should be used to build the documentation. You can install it using your package manager or by
following the instructions on the [pyenv GitHub page](https://github.com/pyenv/pyenv).

```bash
cd docs
pip install -r requirements.txt
make html
```


---

## Merged Content



### Content from docs/contributing/admins.md

(administrators-guide-label)=

# Administrators Guide

This guide is for administrators of OpenSPP Documentation.
It covers automated deployments, hosting, automated testing, previewing, and importing external package documentation into OpenSPP Documentation.


(administrators-import-docs-submodule-label)=

## Importing external docs with submodules

To add an external package to OpenSPP Documentation, we use git submodules.
Your package must be available under the OpenSPP GitHub organization.

Inside the repository `openspp/documentation`, add a git submodule that points to your project.

```shell
git submodule add git@github.com:openspp/my_package.git submodules/my_package
```

Add a target `docs/my_package` in `Makefile`, then add `docs/my_package` to the `deps` target, following `openspp_registry` as a pattern.
You might need to adjust the paths to your package's documentation after it is cloned.

To complete setup, generate a symlink to your project's docs, and build the docs, use a single command.

```shell
make html
```

To make it easier for other contributors to work with your project, update the following files, using `openspp_registry` as a model.
 
-   Add it to the documentation section {ref}`contributing-editing-external-package-documentation-label`.
-   Add the symlink `docs/my_package` to `.gitignore`.
-   Optionally set a branch to work on in `.gitmodules`.

Commit and push your changes to a remote, and submit a pull request against [`openspp/documentation`](https://github.com/openspp/documentation/compare).


### Content from docs/contributing/authors.md

(authors-guide-label)=

# Authors guide

This guide is for authors of OpenSPP Documentation.
It covers how to run a live preview of documentation while editing, build documentation, and perform quality checks.
For general markup syntax, see {doc}`myst-reference`.


## Synchronize the browser while editing

Use `sphinx-autobuild` to view changes in the browser while you edit documentation.

```shell
make livehtml
```

You can open a browser at http://127.0.0.1:8000/ to preview the documentation.


(authors-quality-checks-label)=

## Quality checks

We strive for high quality documentation, setting the following minimum standards.


(authors-markup-syntax-label)=

### Markup syntax must be valid

See both the specific markup syntax above and general markup in {doc}`myst-reference`.

To validate markup, run the following command.

```shell
make html
```

Open `/_build/html/index.html` in a web browser.


(authors-english-label)=

### American English spelling, grammar, and syntax, and style guide

Spellings are enforced through [`Vale`](https://vale.sh/).
OpenSPP uses American English.

Spelling is configured in {file}`Makefile`, {file}`.vale.ini`, and in files in `styles/Vocab/OpenSPP/`.

Authors should add new words and proper names using correct casing to {file}`styles/Vocab/OpenSPP/accept.txt`, sorted alphabetically and case-insensitive.

Vale also provides English grammar and syntax checking, as well as a Style Guide.
We follow the [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/).

To perform all these checks, run the following command.

```shell
make vale
```

Because it is difficult to automate good American English grammar and syntax, we do not strictly enforce it.
We also understand that contributors might not be fluent in English.
We encourage contributors to make a reasonable effort, and to request a review of their pull request from community members who are fluent in English to fix grammar and syntax.
Please ask!


(authors-linkcheck-label)=

### All links must be valid

```{important}
Before you add a link, consider whether you really need it for the documentation.
Avoid linking to blog posts because they rapidly succumb to bitrot.
It is preferred to copy the content from the source and add a link to the source as a reference through a `seealso` admonition or footnote, than to merely link to the source.
```

Valid links are enforced automatically through Sphinx's `linkcheck` builder.

[Configuration of the `linkcheck` builder](https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder) is in {file}`Makefile` and {file}`docs/conf.py`.

`linkcheck_ignore` supports regular expression syntax.

When authors add a link to the documentation, it must be a valid public URL without requiring authentication.

If it is not a valid link, or is private or local, then you must exclude it from `linkcheck` by wrapping it in single backticks.

```md
Visit the URL `http://www.example.com` for an example.
```

This will render as follows.

> Visit the URL `http://www.example.com` for an example.

If a link has succumbed to bit rot, then try finding the most recently scraped version on the [Internet Archive Wayback Machine](https://web.archive.org/), and update the link.

To validate links, run the following command.

```shell
make linkcheck
```

Open `/_build/linkcheck/output.txt` for a list of broken links.

```{danger}
Please do not abuse `linkcheck_ignore`.

There is a special place in hell reserved for contributors who do not bother to update bad links, either dead ones or redirects, causing `linkcheck` to fail.
And there is a doubly punishing place for those who disable `linkcheck` because there are too many bad links.

Please do not be "that person".
```


(authors-syntax-highlighting-label)=

### Syntax highlighting

Pygments provides syntax highlighting in Sphinx.

When including code snippets, you should specify the language.
Authors must use a proper [Pygments lexer](https://pygments.org/docs/lexers/) and not generate warnings.

The snippet must be valid syntax for the language you specify, else it will not be highlighted properly.
Avoid adding comments to code snippets, unless you use valid comment syntax for that language.
For example, JSON does not allow comments.

Do not indicate elided or omitted code with ellipses (`...` or `…`).
These are almost never valid syntax and will cause syntax highlighting to fail for the code block.


#### Choosing a Lexer

Some lexers are less than perfect.
If your code block does not highlight well, then consider specifying a less ambitious lexer, such as `text`.

Use `shell` for commands to be issued in a terminal session.
Do not include shell prompts.
This will make commands easy to copy and paste for readers.

Use `console` for output of a shell session.
If you have a mix of a shell command and its output, then use `console`.

If `xml` does not work well, then try `html`.

`jsx` has a complex syntax that is difficult to parse.
We have high hopes for the project [`jsx-lexer`](https://github.com/fcurella/jsx-lexer).
We include it in our `requirements.txt` file.
Please contribute to its further development.

The lexers `html+ng2`, `scss`, `http`, `less` are also suboptimal and particular.

If no other lexer works well, then fall back to `text`.
At least then the build will succeed without warnings, although syntax highlighting for such snippets will not appear.


#### Validate the lexer

Always build the page to validate syntax.
The change should not be merged if there are any Sphinx warnings.
The Sphinx console will display any warnings, such as the following.

```console
/OpenSPP/documentation/classic-ui/bodyclasses.md:10: WARNING: Could not lex literal_block as "python". Highlighting skipped.
```

The above warning indicates that the syntax is not valid.
Common mistakes include:

- Using `...` or `…` to indicate omitted code.
  It is preferable to never use ellipses.
  If you must do that, comment it out using the language's comment syntax.
- Using comments in JSON.
- A previous code block bleeds through to the next due to invalid MyST syntax.

To validate code block syntax, run the following command.

```shell
make html
```

An [online demo of all lexers that Pygments supports](https://pygments.org/demo/) may be helpful to test out your code blocks and snippets for syntax highlighting.
You can also use the [`pygmentize`](https://pygments.org/docs/cmdline/) binary.

When using the online lexer, if any red-bordered rectangles appear, then the lexer for Pygments interprets your snippet as not valid.
You can search the [Pygments issue tracker](https://github.com/pygments/pygments/search) for possible solutions, or submit a pull request to enhance the lexer.


(authors-html-meta-data-label)=

### HTML and Open Graph metadata

All documents must have a `myst` topmatter key with an `html_meta` directive at the top of every page.
When rendered to HTML, it inserts `<meta>` tags for improved search engine results and nicer social media posts.
Authors should include at least `description`, `property=og:description`, `property=og:title`, and `keywords` meta tags.

The following is an example of `html_meta`.
Note that the content of the two tags `description` and `property=og:description` should be identical.

```md
---
myst:
  html_meta:
    "description": "Authors' guide to writing OpenSPP Documentation. It covers configuring quality checks and syntax for writing markup that is of particular interest to authors."
    "property=og:description": "Authors' guide to writing OpenSPP Documentation. It covers configuring quality checks and syntax for writing markup that is of particular interest to authors."
    "property=og:title": "Authors Guide"
    "keywords": "OpenSPP, Documentation, SEO, meta, Vale, spell, grammar, style, check, linkcheck, lexer"
---
```

This renders in the HTML `<head>` section as follows.

```html
<meta content="Authors' guide to writing OpenSPP Documentation. It covers configuring quality checks and syntax for writing markup that is of particular interest to authors." name="description" />
<meta content="Authors' guide to writing OpenSPP Documentation. It covers configuring quality checks and syntax for writing markup that is of particular interest to authors." property="og:description" />
<meta content="Authors Guide" property="og:title" />
<meta content="OpenSPP, Documentation, SEO, meta, Vale, spell, grammar, style, check, linkcheck, lexer" name="keywords" />
```

Additional Open Graph metadata is implemented through the Sphinx extension [`sphinxext-opengraph`](https://github.com/wpilibsuite/sphinxext-opengraph) and the [MyST `html_meta` directive](https://myst-parser.readthedocs.io/en/latest/configuration.html#setting-html-metadata), which resolves to the [Docutils `meta` directive](https://docutils.sourceforge.io/docs/ref/rst/directives.html#metadata).
See the site-wide configuration in {file}`conf.py`.


## OpenSPP documentation styleguide

We follow [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/).

Key concepts from that guide include the following.

-   Documentation should be informational, but friendly.
-   Address the reader by using "you" instead of "the user".
-   Headings should be Sentence cased, not Title Cased.

The OpenSPP Documentation Team adopted additional guidelines.

-   Use one sentence per line.
    Keep sentences short and understandable.
    This will greatly improve the editing and maintenance of your documentation.

-   Do not follow PEP8 maximum line length standard.
    Documentation is narrative text and images, not Python code.

-   Use dashes `-` in filenames and avoid underscores.

-   Images should be no wider than 740 pixels to fit within the documentation's main view port.
    This avoids scaling and reducing legibility of images.
    To make that work in Volto, set your browser width to 1180 pixels.
    You will notice that the drag and trash icons for each block move inside the block from outside.

-   In user documentation, provide screenshots of each step where the interface changes.
    It is painstaking, but worth the effort.
    Provide sufficient detail of what each option is and does.


## General documentation writing references

-   [Write the Docs - Documentation Guide](https://www.writethedocs.org/guide/)
-   [A Guide to Em Dashes, En Dashes, and Hyphens](https://www.merriam-webster.com/words-at-play/em-dash-en-dash-how-to-use)


### Content from docs/contributing/index.md

(contributing-index-label)=

# Contributing to documentation

This document describes how to contribute to OpenSPP Documentation.

Contributions to the OpenSPP Documentation are welcome.

(contributing-quality-requirements-label)=

## Documentation quality requirements

We use GitHub Actions with every pull request to enforce OpenSPP Documentation quality.
We recommend that you build the documentation locally to catch errors and warnings early on.


### Content from docs/contributing/myst-reference.md

(contributing-myst-reference)=

# MyST reference

This chapter provides information and examples for how to write proper MyST syntax—with references to Sphinx extensions for their specific directives—in OpenSPP Documentation.

## MyST, reStructuredText, and Markdown

We use [MyST, or Markedly Structured Text](https://myst-parser.readthedocs.io/en/latest/), a rich and extensible flavor of Markdown, for authoring training documentation.

MyST extends Markdown by incorporating all the features of reStructuredText and Sphinx and its extensions.
Contributors are welcome to use either Markdown or MyST syntax.

MyST may be more familiar to reStructuredText authors.
MyST allows the use of a fence and `{rst-eval}` to evaluate native reStructuredText.
This may be useful when Markdown does not provide sufficient flexibility, such as for `figure`.

## MyST syntax reference

The following are frequently used snippets and examples.

```{seealso}

Official MyST documentation

- [The MyST Syntax Guide](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html)
- [MyST Syntax Reference](https://myst-parser.readthedocs.io/en/latest/syntax/reference.html)
```

### Cross-references

```{seealso}
[The MyST Syntax Guide > Cross-references](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html)
```

#### Link to a chapter or page

```md
Here is how to set up and build the documentation locally {doc}`/contributing/setup-build`.
```

Here is how to set up and build the documentation locally {doc}`/contributing/setup-build`.

(myst-reference-link-heading-label)=

#### Link to a heading

```md
(myst-reference-hello-heading-label)=

##### Hello heading

Read the section {ref}`myst-reference-link-heading-label`.
```

(myst-reference-hello-heading-label)=

##### Hello heading

Read the section {ref}`myst-reference-hello-heading-label`.

#### Link to an arbitrary location

```md
(example-target-label)=

I have an HTML anchor above me.

Click the link to visit {ref}`my text <example-target-label>`.
```

(example-target-label)=

I have an HTML anchor above me.

Click the link to visit {ref}`my text <example-target-label>`.

#### Link to external page

```md
Use [Shimmer](http://example.com) for cleaner whiter teeth.
```

Use [Shimmer](http://example.com) for cleaner whiter teeth.

### Images and figures

[Figures](https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure) allow a caption and legend, whereas [images](https://docutils.sourceforge.io/docs/ref/rst/directives.html#images) do not.
However we can {ref}`enhance images with cards <enhance-images-label>` to add a caption and more features.

Use `image` for anything but diagrams.

Use `figure` for diagrams.

(static-assets-label)=

#### Static assets

When the documentation is in a submodule, paths to static assets—including, images, figures, and videos—must resolve in both the main documentation and the submodule's documentation.

Inside the `docs` directory, place static assets in the `/_static/` directory, and preferably inside a subdirectory named after the part or page of the documentation.
For example, in the `volto` submodule, inside its `src/docs` directory, place an image at `/_static/user-manual/block-left-add-icon.png`.
In your markup, use that same `docs`-root-relative path for the target, such as `/_static/user-manual/block-left-add-icon.png`.
Don't use file-relative paths.

Configuration in the `conf.py` files for the main documentation and its submodules handle the resolution of `docs`-root-relative paths for you.

#### Width of media

The main content area of a page in the documentation is 743 pixels wide.
When taking screenshots or videos, resize your browser window, or try to limit the width of your media to 740 pixels.
This will preserve legibility of images.

(enhance-images-label)=

#### Enhance images

We use cards from the Sphinx extension [`sphinx-design`](https://sphinx-design.readthedocs.io/en/latest/cards.html) to enhance the display and functionality of images.

Cards allow the display of a caption, create a link to the source image to display when it is too large to fit within the documentation page without scaling, and add a border to demarcate the image from the page's white background.

The following MyST example will display as shown below.

`````md
````{card}
```{image} /_static/caching/caching-disabled.png
:alt: Caching Control Panel
:target: /_static/caching/caching-disabled.png
```
+++
_Caching Control Panel_
````
`````

````{card}
```{image} /_static/caching/caching-disabled.png
:alt: Caching Control Panel
:target: /_static/caching/caching-disabled.png
```
+++
_Caching Control Panel_
````

#### Accessibility with `alt` text

From [Web Accessibility In Mind (WebAIM)](https://webaim.org/techniques/alttext/):

> Alternative text serves several functions:
>
> - It is read by screen readers in place of images allowing the content and function of the image to be accessible to those with visual or certain cognitive disabilities.
> - It is displayed in place of the image in browsers if the image file is not loaded or when the user has chosen not to view images.
> - It provides a semantic meaning and description to images which can be read by search engines or be used to later determine the content of the image from page context alone.

The following MyST example will display as shown below.

````md
```{image} /_static/standards.png
:alt: XKCD "Standards" comic strip
```
````

```{image} /_static/standards.png
:alt: XKCD "Standards" comic strip
```

#### Inline images

For inline images, we use the MyST extension [`html_image`](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#html-images).
Example syntax is shown below.

```html
You can copy
<img alt="Copy icon" src="../../_images/copy.svg" class="inline" /> blocks.
```

Note that the HTML attribute `class` must be set to `inline` to render the image inline at `1rem`.

The above syntax renders as shown below.

> You can copy <img alt="Copy icon" src="/_static/copy.svg" class="inline"> blocks.

Images and figures should always include `alt` text.

The following MyST example will display as shown below.

````md
```{eval-rst}
.. figure:: /_static/voting_flowchart.png
    :alt: Voting flowchart

    This is a caption in a single paragraph.

    This is a legend, which consists of all elements after the caption.
    It can include a table.

    ======  =======
    Symbol  Meaning
    ======  =======
    ⃞       Object
    ⬭       View
    ➞       Flow
    ======  =======
```
````

```{eval-rst}
.. figure:: /_static/voting_flowchart.png
    :alt: Voting flowchart

    This is a caption in a single paragraph.

    This is a legend, which consists of all elements after the caption.
    It can include a table.

    ======  =======
    Symbol  Meaning
    ======  =======
    ⃞       Object
    ⬭       View
    ➞       Flow
    ======  =======
```

### Video

To embed local videos, such as recordings of demonstrating the user interface, we require that the videos be saved as `.mp4` for greatest compatibility, usability, accessibility, and reduced file size.

Avoid animated GIFs because they do not allow control of playback.

Audio is not required, but may be helpful.
If you include audio, it is helpful to include closed captions or a transcript.

It is helpful to include overlays of key strokes, and mouse and other input gestures, to describe how to interact with the user interface.

Paths to videos must resolve in both the main documentation and the submodule's documentation, if present.
See {ref}`static-assets-label` for details.

Example MyST syntax is shown below.

````md
```{video} /_static/user-manual/blocks/block-copy-cut.mp4
    :width: 100%
```
````

Note that the path must be absolute to support both submodules and the main documentation.
Don't use file-relative paths.
The above MyST markup renders as shown below.

```{video} /_static/user-manual/blocks/block-copy-cut.mp4
    :width: 100%
```

### Diagrams and graphs with Graphviz

We use [Graphviz](https://graphviz.org/download/) and its Sphinx extension [`sphinx.ext.graphviz`](https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html) to render diagrams and graph visualizations.

The following MyST example will display as shown below.

````markdown
```{eval-rst}
.. graphviz::
    :align: center

    digraph viewstructure {
      {
        node [margin=5,shape=box]
      }
      ZCML -> {Python, Template};
    }
```
````

```{eval-rst}
.. graphviz::
    :align: center

    digraph viewstructure {
      {
        node [margin=5,shape=box]
      }
      ZCML -> {Python, Template};
    }
```

### Code block

A Python code snippet without reStructuredText options, using a simple fence.

````md
```python
a = 2
print("my 1st line")
print(f"my {a}nd line")
```
````

```python
a = 2
print("my 1st line")
print(f"my {a}nd line")
```

A Python code snippet with reStructuredText options, using a fence with the parsed reStructuredText directive `code-block`.

````md
```{code-block} python
:linenos:
:emphasize-lines: 1, 3

a = 2
print("my 1st line")
print(f"my {a}nd line")
```
````

```{code-block} python
:linenos:
:emphasize-lines: 1, 3

a = 2
print("my 1st line")
print(f"my {a}nd line")
```

### Escape literal backticks inline

```md
This is MyST syntax for term `React `
```

This is MyST syntax for term `React `

### Glossary terms

Add a term to the {ref}`glossary-label`, located at {file}`/glossary.md`.

```md
React
[React](https://reactjs.org/) is a JavaScript library for building user interfaces.
```

Reference a term in the {ref}`glossary-label`.

```md
Using React makes frontends fun again!
```

Using React makes frontends fun again!

### Nesting directives

You can [nest directives](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html#nesting-directives), such as [admonitions](https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html) and code blocks, by ensuring that the backtick-lines corresponding to the outermost directive are longer than the backtick-lines for the inner directives.

`````
````{tip}
To use formatted string literals ("f-strings"), begin a string with `f` or `F` before the opening quotation mark or triple quotation mark.
Inside this string, you can write a Python expression between `{` and `}` characters that can refer to variables or literal values.

```{code-block} python
:linenos:
:emphasize-lines: 1, 3

a = 2
print("my 1st line")
print(f"my {a}nd line")
```
````
`````

This would be rendered as:

````{tip}
To use formatted string literals ("f-strings"), begin a string with `f` or `F` before the opening quotation mark or triple quotation mark.
Inside this string, you can write a Python expression between `{` and `}` characters that can refer to variables or literal values.

```{code-block} python
:linenos:
:emphasize-lines: 1, 3

a = 2
print("my 1st line")
print(f"my {a}nd line")
```
````


### Content from docs/contributing/setup-build.md

(setup-build-label)=

# Building and checking the quality of documentation

This document covers how to build the OpenSPP Documentation and check it for quality.


(setup-build-installation-label)=

## Installation

Installation of OpenSPP Documentation includes pre-requisites and the repository itself.


(setup-build-installation-python-label)=

### Python

Python 3.8 or later is required.
A more recent Python is preferred.
Use your system's package manager or [pyenv](https://github.com/pyenv/pyenv) to install an appropriate version of Python.


(setup-build-installation-vale-label)=

### Vale

Vale is a linter for narrative text.
It checks spelling, English grammar, and style guides.
OpenSPP documentation uses a custom spelling dictionary, with accepted and rejected spellings in `styles/Vocab/OpenSPP`.

Use your operating system's package manager to [install Vale](https://vale.sh/docs/vale-cli/installation/).

Vale also has [integrations](https://vale.sh/docs/integrations/guide/) with various IDEs.

-   [JetBrains](https://vale.sh/docs/integrations/jetbrains/)
-   [Vim](https://github.com/dense-analysis/ale)
-   [VS Code](https://github.com/errata-ai/vale-vscode)

OpenSPP documentation uses a file located at the root of the repository, `.vale.ini`, to configure Vale.
This file allows overriding rules or changing their severity.

The OpenSPP Documentation Team selected the [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) for its ease of use—especially for non-native English readers and writers—and attention to non-technical audiences. 

```{note}
More corrections to spellings and Vale's configuration are welcome by submitting a pull request.
This is an easy way to become a contributor to OpenSPP.
```


(setup-build-installation-graphviz-label)=

### Graphviz

Install [Graphviz](https://graphviz.org/download/) for graph visualization.

`````{tab-set}
````{tab-item} macOS
```shell
brew install graphviz
```
````

````{tab-item} Ubuntu
```shell
sudo apt-get install graphviz
```
````
`````


(setup-build-installation-clone-OpenSPP-documentation-label)=

### Clone `OpenSPP/documentation`

Clone the OpenSPP Documentation repository, and change your working directory into the cloned project.
Then with a single command using `Makefile`, create a Python virtual environment, install project dependencies, pull in Volto documentation as a git submodule, build the docs, and view the results in a web browser by opening `/_build/html/index.html`.

```shell
git clone https://github.com/OpenSPP/documentation.git
cd documentation
make html
```

(setup-build-available-documentation-builds-label)=

## Available documentation builds

All build and check documentation commands use the file `Makefile`.

To see the most frequently used builds, use the following command.

```shell
make help
```

Else you can open `Makefile` to see other build formats, including PDF.


### `html`

`html` is the HTML version of the documentation.

```shell
make html
```

Open `/_build/html/index.html` in a web browser.


### `livehtml`

`livehtml` rebuilds Sphinx documentation on changes, with live-reload in the browser.

```shell
make livehtml
```

Open http://0.0.0.0:8000/ in a web browser.


### `linkcheck`

`linkcheck` checks all links.
See {ref}`authors-linkcheck-label` for configuration.

```shell
make linkcheck
```

Open `/_build/linkcheck/output.txt` for a list of broken links.


### `vale`

`vale` checks for American English spelling, grammar, syntax, and the Microsoft Developer Style Guide.
See {ref}`authors-english-label` for configuration.

```shell
make vale
```

See the output on the console for suggestions.


### `html_meta`

`html_meta` adds a meta data section to each chapter if missing.
See {ref}`authors-html-meta-data-label` for more info.

```shell
make html_meta
```


### Content from docs/contributing/sphinx-extensions.md

(contributing-sphinx-extensions)=

# Sphinx extensions

We use several Sphinx extensions to enhance the presentation of OpenSPP documentation.

-   [`sphinx.ext.graphviz`](https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html) allows you to embed [Graphviz](https://graphviz.org/download/) graphs in your documents.
-   [`sphinx.ext.intersphinx`](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html) provides linking between separate projects that use Sphinx for documentation.
-   [`sphinx.ext.todo`](https://www.sphinx-doc.org/en/master/usage/extensions/todo.html) adds support for todo items.
-   [`sphinx_copybutton`](https://sphinx-copybutton.readthedocs.io/en/latest/index.html)  adds a little "copy" button to the right of code blocks.
-   [`sphinx-design`](https://sphinx-design.readthedocs.io/en/latest/) adds grids, cards, icons, badges, buttons, tabs, and dropdowns.
-   [`sphinx_sitemap`](https://pypi.org/project/sphinx-sitemap/) generates multiversion and multilanguage [sitemaps.org](https://www.sitemaps.org/protocol.html) compliant sitemaps.
-   [`sphinxcontrib.httpdomain`](https://sphinxcontrib-httpdomain.readthedocs.io/en/stable/) provides a Sphinx domain for describing HTTP APIs.
-   [`sphinxcontrib.httpexample`](https://sphinxcontrib-httpexample.readthedocs.io/en/latest/) enhances `sphinxcontrib-httpdomain` by generating RESTful HTTP API call examples for different tools from a single HTTP request example.
    Supported tools include [curl](https://curl.se/), [wget](https://www.gnu.org/software/wget/), [httpie](https://httpie.io/), and [python-requests](https://requests.readthedocs.io/en/latest/).
-   [`sphinxcontrib.video`](https://pypi.org/project/sphinxcontrib-video/) allows you to embed local videos as defined by the HTML5 standard.
-   [`sphinxext.opengraph`](https://pypi.org/project/sphinxext-opengraph/) generates [OpenGraph metadata](https://ogp.me/).
-   [`sphinx.ext.viewcode`](https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html) generates pages of source code modules and links between the source and the description.
-   [`sphinx.ext.autosummary`](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html) generates function/method/attribute summary lists.


### Content from docs/howto/translation.md

### Translation
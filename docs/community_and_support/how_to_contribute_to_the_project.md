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

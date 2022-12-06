# Contributing

The project follows the OpenSPP [Code of Conduct](code_of_conduct). If you are not familiar with our code of
conduct policy, take a minute to read the policy before starting with your first contribution.

Bug reports and code and documentation patches are welcome. You can help this project also by using the
development version and by reporting any bugs you might encounter.

## **Did you find a bug?**

- **Do not open up a GitHub issue if the bug is a security vulnerability in OpenSPP**, and instead follow the
  [security disclosure policy](security-report).

- **Ensure the bug was not already reported** by searching on GitHub under
  [Issues](https://github.com/openspp/documentation/issues).

- If you're unable to find an open issue addressing the problem,
  [open a new one](https://github.com/openspp/documentation/issues/new). Be sure to include a **title and
  clear description**, as much relevant information as possible demonstrating the expected behavior that is
  not occurring.

## **Did you write a patch that fixes a bug?**

- Open a new GitHub pull request with the patch.

- Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if
  applicable.

<!-- ## **Do you have questions about the source code?**

- Ask any question about how to use OpenSPP in the
  [Discussions](https://github.com/openspp/documentation/discussions). -->

## Contributing to the documentation

If you want to contribute to the documentation, you can do so by following the steps below:

- Fork the repository.
- Create a virtual environment and install the dependencies as described in the next section.
- Set up pre-commit hooks to ensure that your code is compliant with the project's standards.

  ```
  pre-commit install
  ```

- Create a new branch.
- Make your changes and commit them to your branch.
- Submit a pull request.

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

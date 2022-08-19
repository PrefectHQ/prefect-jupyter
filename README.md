# prefect-jupyter

<a href="https://pypi.python.org/pypi/prefect-jupyter/" alt="PyPI Version">
    <img src="https://badge.fury.io/py/prefect-jupyter.svg" /></a>
<a href="https://github.com/PrefectHQ/prefect-jupyter/" alt="Stars">
    <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-jupyter" /></a>
<a href="https://pepy.tech/badge/prefect-jupyter/" alt="Downloads">
    <img src="https://pepy.tech/badge/prefect-jupyter" /></a>
<a href="https://github.com/PrefectHQ/prefect-jupyter/pulse" alt="Activity">
    <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-jupyter" /></a>
<a href="https://github.com/PrefectHQ/prefect-jupyter/graphs/contributors" alt="Contributors">
    <img src="https://img.shields.io/github/contributors/PrefectHQ/prefect-jupyter" /></a>
<br>
<a href="https://prefect-community.slack.com" alt="Slack">
    <img src="https://img.shields.io/badge/slack-join_community-red.svg?logo=slack" /></a>
<a href="https://discourse.prefect.io/" alt="Discourse">
    <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?logo=discourse" /></a>

## Welcome!

Prefect integrations interacting with Jupyter.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-jupyter` with `pip`:

```bash
pip install prefect-jupyter
```

### Run a parameterized notebook

```python
from prefect import flow
from prefect_jupyter import notebook

@flow
def example_execute_notebook():
    body = notebook.execute_notebook(
        "test_notebook.ipynb",
        parameters={"num": 5}
    )
    output_path = "executed_notebook.ipynb"
    with open(output_path, "w") as f:
        f.write(body)
    return output_path

example_execute_notebook()
```

## Resources

If you encounter any bugs while using `prefect-jupyter`, feel free to open an issue in the [prefect-jupyter](https://github.com/PrefectHQ/prefect-jupyter) repository.

If you have any questions or issues while using `prefect-jupyter`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-jupyter` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-jupyter.git

cd prefect-jupyter/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```

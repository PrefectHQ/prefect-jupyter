# prefect-jupyter

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-jupyter/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-jupyter?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-jupyter/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-jupyter?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-jupyter/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-jupyter?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-jupyter/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-jupyter?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

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
`prefect-jupyter` uses papermill under the hood. Check out [papermill's documentation](https://papermill.readthedocs.io/en/latest/usage-parameterize.html) to learn how to parametrize the notebook.

The following code shows how to run a parameterized notebook:

```python
from prefect import flow
from prefect_jupyter import notebook

@flow
def example_execute_notebook():
    nb = notebook.execute_notebook(
        "test_notebook.ipynb",
        parameters={"num": 5}
    )
    body = notebook.export_notebook(nb)
    output_path = "executed_notebook.ipynb"
    with open(output_path, "w") as f:
        f.write(body)
    return output_path

example_execute_notebook()
```

## Resources

If you encounter any bugs while using `prefect-jupyter`, feel free to open an issue in the [prefect-jupyter](https://github.com/PrefectHQ/prefect-jupyter) repository.

If you have any questions or issues while using `prefect-jupyter`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`prefect-jupyter`](https://github.com/PrefectHQ/prefect-jupyter) for updates too!

## Development

If you'd like to install a version of `prefect-jupyter` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-jupyter.git

cd prefect-jupyter/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```

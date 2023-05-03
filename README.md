# prefect-jupyter

<p align="center">
    <!--- Insert a cover image here -->
    <!--- <br> -->
    <a href="https://pypi.python.org/pypi/prefect-jupyter/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-jupyter?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-jupyter/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-jupyter?color=0052FF&labelColor=090422" /></a>
    <a href="https://pypistats.org/packages/prefect-jupyter/" alt="Downloads">
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

### Feedback

If you encounter any bugs while using `prefect-jupyter`, feel free to open an issue in the [prefect-jupyter](https://github.com/PrefectHQ/prefect-jupyter) repository.

If you have any questions or issues while using `prefect-jupyter`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to star or watch [`prefect-jupyter`](https://github.com/PrefectHQ/prefect-jupyter) for updates too!

## Contributing

If you'd like to help contribute to fix an issue or add a feature to `prefect-jupyter`, please [propose changes through a pull request from a fork of the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

Here are the steps:
 
1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
2. [Clone the forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository)
3. Install the repository and its dependencies:
```bash
 pip install -e ".[dev]"
```
4. Make desired changes
5. Add tests
6. Insert an entry to [CHANGELOG.md](https://github.com/PrefectHQ/prefect-jupyter/blob/main/CHANGELOG.md)
7. Install `pre-commit` to perform quality checks prior to commit:
```bash
 pre-commit install
 ```
8. `git commit`, `git push`, and create a pull request

"""Module containing tasks for interacting with Jupyter."""

from enum import Enum
from typing import Any, Dict, Optional

import nbconvert
import nbformat
import papermill as pm
from prefect import task


class OutputFormat(Enum):
    """
    Valid output formats of a notebook.
    """

    ASCIIDOC = "asciidoc"
    CUSTOM = "custom"
    HTML = "html"
    LATEX = "latext"
    MARKDOWN = "markdown"
    NOTEBOOK = "notebook"
    JSON = "notebook"
    PDF = "pdf"
    PYTHON = "python"
    RST = "rst"
    SCRIPT = "script"
    WEBPDF = "webpdf"


@task
def execute_notebook(
    path: str,
    parameters: Optional[Dict[str, Any]] = None,
    log_output: bool = False,
    kernel_name: Optional[str] = None,
    **execute_kwargs: Dict[str, Any],
) -> str:
    """
    Task for running Jupyter Notebooks.

    In order to parametrize the notebook, you need to mark the parameters
    cell as described in the [papermill documentation](
    https://papermill.readthedocs.io/en/latest/usage-parameterize.html).

    Args:
        path: Where to fetch the notebook from; can be a cloud storage path.
        parameters: Parameters to use for the notebook.
        log_output: Whether or not to log notebook cell output to the papermill logger.
        kernel_name: Name of kernel to execute the notebook against.
        **execute_kwargs: Additional keyword arguments to pass to `execute_notebook`.

    Returns:
        The NotebookNode object of the executed notebook.
    """
    return pm.execute_notebook(
        path,
        "-",
        parameters=parameters,
        kernel_name=kernel_name,
        log_output=log_output,
        **execute_kwargs,
    )


@task
def export_notebook(
    nb: nbformat.NotebookNode,
    output_format: OutputFormat = OutputFormat.NOTEBOOK,
    **export_kwargs: Dict[str, Any],
) -> str:
    """
    Task for exporting a NotebookNode.

    Args:
        nb: The notebook to export.
        output_format: The notebook output format.
        **export_kwargs: Additional keyword arguments to pass to `nbconvert.export`.

    Returns:
        The body of the output.
    """
    exporter = nbconvert.get_exporter(output_format.value)
    body, _ = nbconvert.export(exporter, nb, **export_kwargs)
    return body

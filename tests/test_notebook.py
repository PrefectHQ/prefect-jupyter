import json
from pathlib import Path

import pytest

from prefect_jupyter import notebook


def test_execute_notebook():
    file_path = Path(__file__).parent.resolve()
    body = notebook.execute_notebook.fn(
        file_path / "test_notebook.ipynb", parameters={"num": 5}
    )
    contents = json.loads(body)
    assert len(contents["cells"]) == 3  # generates a parameter cell

    last_cell = contents["cells"][-1]
    actual_text = last_cell["outputs"][0]["text"][0]
    expected_text = "one is 1, 2 is two, num is 5!\n"
    assert actual_text == expected_text


def test_execute_notebook_not_found():
    with pytest.raises(FileNotFoundError, match="No such file"):
        notebook.execute_notebook.fn("test_non_existent_notebook.ipynb")

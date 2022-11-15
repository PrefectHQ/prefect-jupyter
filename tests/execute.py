import json
from pathlib import Path

import cloudpickle
from prefect import flow
from prefect.context import FlowRunContext
from pydantic import BaseModel

from prefect_jupyter import notebook


class MyObject(BaseModel):
    test: str = "abc"


def is_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


print(is_notebook())


@flow
def execute_notebook():
    # client", "flow", "task_runner", "background_tasks
    filename = "flow_context.pkl"
    with open(filename, "wb") as f:
        cloudpickle.dump(
            FlowRunContext.get().dict(
                include={
                    "flow",
                    "flow_run",
                    "result_factory",
                    "task_runner",
                    "sync_portal",
                }
            ),
            f,
        )
    body = notebook.execute_notebook(
        "test_notebook.ipynb",
        parameters={"num": 5, "flow_run_context_filename": filename},
    )
    return body


with open("output.ipynb", "w") as f:
    f.write(execute_notebook())

# pyright: strict, reportUnnecessaryIsInstance=false

import os

from great_project.__about__ import __version__


def compute(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        msg = "int only"
        raise TypeError(msg)
    return a + b


def get_env_value(env_variable: str) -> str | None:
    return os.environ.get(env_variable)


def entrypoint():
    print(f"Hello from {__version__}")  # noqa: T201

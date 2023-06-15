from great_project.__about__ import __version__


def compute(a: int, b: int) -> int:
    return a + b


def entrypoint():
    print(f"Hello from {__version__}")  # noqa: T201

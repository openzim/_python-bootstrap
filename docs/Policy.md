This openZIM Python Bootstrap setup (`main` branch) represents the **current** recommendations for setting-up a Python project.

- It should be used as base for any new Python project
- It should serve as a reference to migrate older Python projects
- Requirements for older projects are relaxed:
  - Static Type Checking:
    - `pyright` mode might be set to `basic` (with the `typeCheckingMode` parameter)
    - few `# pyright: ignore` comments are allowed in the code
  - Ruff rules:
    - `# noqa: xxx` comments can be placed when necessary
    - as a last resort (because it means that the situation might continue to get worse), some rule or groups might be completely commented in `pyproject.toml`
  - Cython-using projects should continue with setuptools/setup.py

## Contributing

Discussions on significant improvements should happen via [Opening an Issue](https://github.com/openzim/_python-bootstrap/issues/new).

Simpler suggestions are expected as [Pull Request](https://github.com/openzim/_python-bootstrap/compare)


## Versioning

We will most likely tag have _versions_ as tags at some point in time but we are yet to achieve an initial one.
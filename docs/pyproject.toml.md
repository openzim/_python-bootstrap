Python setup uses `hatchling` as build backend and leans on [`hatch`](https://hatch.pypa.io) for various features.

### Target Python Version 

Target  depends on the audience of the project:
- Specific version if audience has specific requirement (eg. raspberry-pi)
- Latest stable version for internal tools (eg. docker deployed)
- [Latest still maintained version](https://en.wikipedia.org/wiki/History_of_Python#Table_of_versions) for larger audience (eg. library)

### Version

Version must be dynamic and set once in code. `module.__about__` usually.

### Dependencies

- Solely specified in this file.
- Projects that are not meant to interact with others (tools vs library) use strict matching versions.
- Libraries and alike uses ranges when possible (semantic versioning).
- Only direct dependencies (unless required to bypass a sub-dependency issue)

### Linting

- Black (latest available version)
- Ruff for import sorting (isort-like) and many other checks
- Dedicated hatch environment
- Black and ruff configuration so those works without hatch as well
- Scripts for just black and just ruff checking
- Scripts for black fixing and ruf fixing (accepts params)
- Scripts for global checking and fixing
- Sample ruff configuration

### Checking

- [pyright](https://microsoft.github.io/pyright) for static type checking
- Dedicated hatch environment
- Sample pyright configuration
- Scripts for running pyright

### QA

- Tests and coverage reporting with [`pytest`](https://docs.pytest.org)
- Dedicated hatch environment
- Hatch environment matrix to easily tests on multiple python versions
- pytest and coverage configuration so those works without hatch as well
- Scripts for running tests (accepts params), running with coverage and reporting
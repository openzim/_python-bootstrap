Please check our [[Policy]] first.

## Using Hatch

```sh
❯ pip install hatch

# local install (in default env) / re-sync packages
❯ hatch run pip list
❯ pre-commit install

# scripts discovery
❯ hatch env show

# linting, testing, coverage, checking
❯ hatch run lint:all
❯ hatch run lint:fixall
# run tests on all matrixed' envs
❯ hatch run test:run
# run tests in a single matrixed' env
❯ hatch env run -e test -i py=3.11 coverage
# run static type checks
❯ hatch env run check:all

# building packages
❯ hatch build
```

## _Bare_ Python

```sh
❯ python3 -m venv .env && source .env/bin/activate

# local install / install newly added packages
❯ pip install -e .[dev]
❯ pre-commit install

# scripts discovery
❯ inv -l

# linting, testing, coverage, static type checks
❯ inv lintall
❯ inv fixall
❯ inv test
❯ inv coverage
❯ inv checkall

# building packages
❯ pip install build
❯ python3 -m build
```
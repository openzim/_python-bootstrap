If you've not already read it, please check our [Policy](./Policy.md) first.

## Using Hatch

```sh
❯ pip install hatch

# local install (in default env) / re-sync packages
❯ hatch run pip list
❯ pre-commit install

# scripts discovery
❯ hatch env show

# linting, testing, coverage, checking
❯ hatch run qa:check-all
❯ hatch run qa:fix-all
# run tests on all matrixed' envs
❯ hatch run test:run
# run tests in a single matrixed' env
❯ hatch env run -e test -i py=3.11 coverage

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

# check linting, formatting and static type checks
❯ inv check-all
# fix everything automatically
❯ inv fix-all
# run tests
❯ inv test
❯ inv coverage

# building packages
❯ pip install build
❯ python3 -m build
```

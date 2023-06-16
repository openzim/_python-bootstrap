from invoke import task


@task(optional=["args"], help={"args": "pytest additional arguments"})
def test(c, args: str | None = ""):
    """run tests (without coverage)"""
    c.run(f"pytest {args}")


@task(optional=["args"], help={"args": "pytest additional arguments"})
def test_cov(c, args: str | None = ""):
    """run test vith coverage"""
    c.run(f"coverage run -m pytest {args}")


@task()
def cov_report(c):
    """report coverage"""
    c.run("coverage combine", warn=True)
    c.run("coverage report --show-missing")


@task(optional=["args"], help={"args": "pytest additional arguments"})
def cov(c, args: str | None = ""):
    """run tests and report coverage"""
    test_cov(c, args)
    cov_report(c)


@task(
    optional=["args"], help={"args": "linting tools (black, ruff) additional arguments"}
)
def lint_black(c, args: str | None = ""):
    args = args or "."
    c.run("black --version")
    c.run(f"black --check --diff {args}")


@task(
    optional=["args"], help={"args": "linting tools (black, ruff) additional arguments"}
)
def lint_ruff(c, args: str | None = ""):
    args = args or "."
    c.run("ruff --version")
    c.run(f"ruff check {args}")


@task(
    optional=["args"], help={"args": "linting tools (black, ruff) additional arguments"}
)
def lintall(c, args: str | None = ""):
    """check linting"""
    args = args or "."
    lint_black(c, args)
    lint_ruff(c, args)


@task(optional=["args"], help={"args": "black additional arguments"})
def fix_black(c, args: str | None = ""):
    """fix black formatting"""
    args = args or "."
    c.run(f"black {args}")


@task(optional=["args"], help={"args": "ruff additional arguments"})
def fix_ruff(c, args: str | None = ""):
    """fix all ruff rules"""
    args = args or "."
    c.run(f"ruff --fix {args}")


@task(
    optional=["args"],
    help={"args": "linting (fix mode) tools (black, ruff) additional arguments"},
)
def fixall(c, args: str | None = ""):
    """fix everything automatically"""
    args = args or "."
    fix_black(c, args)
    fix_ruff(c, args)
    lintall(c, args)

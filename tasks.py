# pyright: strict, reportUntypedFunctionDecorator=false
import os

from invoke.context import Context
from invoke.tasks import task  # pyright: ignore [reportUnknownVariableType]

use_pty = not os.getenv("CI", "")


@task(optional=["args"], help={"args": "pytest additional arguments"})
def test(ctx: Context, args: str = ""):
    """run tests (without coverage)"""
    ctx.run(f"pytest {args}", pty=use_pty)


@task(optional=["args"], help={"args": "pytest additional arguments"})
def test_cov(ctx: Context, args: str = ""):
    """run test vith coverage"""
    ctx.run(f"pytest --cov=src {args}", pty=use_pty)


@task(optional=["no-html"], help={"no-html": "flag to not export html report"})
def report_cov(ctx: Context, *, no_html: bool = False):
    """report coverage"""
    ctx.run("coverage combine", warn=True, pty=use_pty)
    ctx.run("coverage report --show-missing", pty=use_pty)
    if not no_html:
        ctx.run("coverage html", pty=use_pty)


@task(
    optional=["args", "no-html"],
    help={
        "args": "pytest additional arguments",
        "no-html": "flag to not export html report",
    },
)
def coverage(ctx: Context, args: str = "", *, no_html: bool = False):
    """run tests and report coverage"""
    test_cov(ctx, args=args + " --cov-report xml")
    report_cov(ctx, no_html=no_html)


@task(
    optional=["args"], help={"args": "linting tools (black, ruff) additional arguments"}
)
def lint_black(ctx: Context, args: str = "."):
    ctx.run("black --version", pty=use_pty)
    ctx.run(f"black --check --diff {args}", pty=use_pty)


@task(
    optional=["args"], help={"args": "linting tools (black, ruff) additional arguments"}
)
def lint_ruff(ctx: Context, args: str = "."):
    ctx.run("ruff --version", pty=use_pty)
    ctx.run(f"ruff check {args}", pty=use_pty)


@task(
    optional=["black_args", "ruff_args"],
    help={
        "black_args": "linting (fix mode) black arguments",
        "ruff_args": "linting (fix mode) ruff arguments",
    },
)
def lintall(ctx: Context, black_args: str = ".", ruff_args: str = "."):
    """Check linting"""
    lint_black(ctx, black_args)
    lint_ruff(ctx, ruff_args)


@task(optional=["args"], help={"args": "check tools (pyright) additional arguments"})
def check_pyright(ctx: Context, args: str = ""):
    """check static types with pyright"""
    ctx.run("pyright --version")
    ctx.run(f"pyright {args}", pty=use_pty)


@task(optional=["args"], help={"args": "check tools (pyright) additional arguments"})
def checkall(ctx: Context, args: str = ""):
    """check static types"""
    check_pyright(ctx, args)


@task(optional=["args"], help={"args": "black additional arguments"})
def fix_black(ctx: Context, args: str = "."):
    """fix black formatting"""
    ctx.run(f"black {args}", pty=use_pty)


@task(optional=["args"], help={"args": "ruff additional arguments"})
def fix_ruff(ctx: Context, args: str = "."):
    """fix all ruff rules"""
    ctx.run(f"ruff --fix {args}", pty=use_pty)


@task(
    optional=["black_args", "ruff_args"],
    help={
        "black_args": "linting (fix mode) black arguments",
        "ruff_args": "linting (fix mode) ruff arguments",
    },
)
def fixall(ctx: Context, black_args: str = ".", ruff_args: str = "."):
    """Fix everything automatically"""
    fix_black(ctx, black_args)
    fix_ruff(ctx, ruff_args)
    lintall(ctx, black_args=black_args, ruff_args=ruff_args)

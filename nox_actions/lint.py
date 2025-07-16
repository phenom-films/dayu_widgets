# Import third-party modules
import nox
from nox_actions.utils import PACKAGE_NAME


def lint(session: nox.Session) -> None:
    session.install("isort", "ruff")
    session.run("isort", "--check-only", PACKAGE_NAME)
    session.run("ruff", "check")


def lint_fix(session: nox.Session) -> None:
    session.install("isort", "ruff", "pre-commit", "autoflake")
    session.run("ruff", "check", "--fix")
    session.run("isort", ".")
    session.run("pre-commit", "run", "--all-files")
    session.run("autoflake", "--in-place", "--remove-all-unused-imports", "--remove-unused-variables", ".")

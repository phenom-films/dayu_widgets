# Import third-party modules
import nox
from nox_actions.utils import PACKAGE_NAME


@nox.session
def mypy(session: nox.Session) -> None:
    """Run mypy for type checking."""
    session.install("mypy", "types-six")  # types-six for six package
    session.install("-e", ".")
    session.run(
        "mypy",
        PACKAGE_NAME,
        "--ignore-missing-imports",  # Ignore missing stubs for third-party packages
        "--disallow-untyped-defs",  # Disallow functions without type annotations
        "--disallow-incomplete-defs",  # Disallow partially typed functions
        "--check-untyped-defs",  # Type check the interior of functions without annotations
        "--disallow-untyped-decorators",  # Disallow decorators without types
        "--no-implicit-optional",  # Don't assume arguments with default values are Optional
        "--warn-redundant-casts",  # Warn about redundant type casts
        "--warn-unused-ignores",  # Warn about unnecessary # type: ignore comments
        "--warn-return-any",  # Warn about returning Any from functions
        "--warn-unreachable",  # Warn about unreachable code
    )

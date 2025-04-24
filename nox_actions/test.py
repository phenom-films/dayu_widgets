# Import built-in modules
from pathlib import Path

# Import third-party modules
import nox
from nox_actions.utils import get_qt_dependencies


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11", "3.12"])
@nox.parametrize("qt_binding", ["pyside2", "pyside6"])
def test(session: nox.Session, qt_binding: str) -> None:
    """Run tests with specific Qt binding and Python version."""
    # Get the project root directory
    root_dir = Path(__file__).parent.parent.absolute()

    # 检查Python版本和Qt绑定的兼容性
    import sys
    if qt_binding == "pyside2" and sys.version_info >= (3, 11):
        session.skip("PySide2 is not supported on Python 3.11+")
        return

    # Install dependencies first
    deps = get_qt_dependencies(qt_binding)
    if not deps:  # 如果依赖列表为空，说明需要跳过测试
        session.skip("No dependencies available for this configuration")
        return

    # Check if uv is available
    try:
        session.run("uv", "--version", external=True, silent=True)
        has_uv = True
    except Exception:
        has_uv = False

    # Install dependencies
    if has_uv:
        # Install dependencies with uv
        session.run("uv", "pip", "install", *deps, external=True)

        # Then install the package itself
        if qt_binding == "pyside2":
            session.run("uv", "pip", "install", "-e", ".[pyside2]", external=True)
        else:
            session.run("uv", "pip", "install", "-e", ".[pyside6]", external=True)
    else:
        # Fall back to pip if uv is not available
        for dep in deps:
            session.install(dep)

        # Then install the package itself
        if qt_binding == "pyside2":
            session.install("-e", ".[pyside2]")
        else:
            session.install("-e", ".[pyside6]")

    # Set environment variables
    env = {
        "QT_API": qt_binding,
        "PYTHONPATH": str(root_dir)
    }

    # Run tests
    session.run(
        "pytest",
        "tests",
        "-v",
        "--cov=dayu_widgets",
        "--cov-report=xml",
        env=env
    )

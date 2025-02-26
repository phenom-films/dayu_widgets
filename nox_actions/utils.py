# Import built-in modules
import os
import sys
from pathlib import Path

PACKAGE_NAME = "dayu_widgets"
THIS_ROOT = Path(__file__).parent.parent
PROJECT_ROOT = THIS_ROOT.parent


def get_qt_dependencies(qt_binding):
    """Get Qt dependencies based on binding type.

    Args:
        qt_binding (str): Qt binding type ('pyside2' or 'pyside6')

    Returns:
        List of package requirements
    """
    # 基础测试依赖
    base_deps = [
        "pytest>=7.0.0",
        "pytest-qt>=4.2.0",
        "pytest-cov>=4.1.0",
    ]

    # Qt 依赖
    if qt_binding == "pyside2":
        # PySide2 在 Python 3.11+ 上不再支持
        if sys.version_info >= (3, 11):
            print("Skipping PySide2 tests on Python 3.11+")
            return []  # 返回空列表，让调用者处理跳过测试
        # 不再返回PySide2和qtpy，因为它们会通过extras安装
        return base_deps
    else:  # pyside6
        # 不再返回PySide6和qtpy，因为它们会通过extras安装
        return base_deps


def setup_qt_test_env():
    """Setup environment for Qt testing.
    
    This ensures:
    1. The package is importable
    2. Qt can find necessary plugins
    """
    if THIS_ROOT not in sys.path:
        sys.path.insert(0, str(THIS_ROOT))
    
    # Set QT_QPA_PLATFORM for headless testing if needed
    if os.environ.get("CI") or os.environ.get("HEADLESS"):
        os.environ["QT_QPA_PLATFORM"] = "offscreen"

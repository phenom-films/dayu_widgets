# Import built-in modules
import sys
from pathlib import Path

# Import third-party modules
import nox

# Ensure nox_actions is importable
ROOT = Path(__file__).parent.absolute()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Import local modules
from nox_actions.test import test
from nox_actions.lint import lint, lint_fix
from nox_actions.maya_test import maya_test
from nox_actions.blender_test import blender_test

# Register sessions
nox.session(test, name="test")
nox.session(lint, name="lint")
nox.session(lint_fix, name="lint-fix")
nox.session(maya_test, name="maya-test")
nox.session(blender_test, name="blender-test")

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

# Register sessions
nox.session(test, name="test")
nox.session(lint, name="lint")
nox.session(lint_fix, name="lint-fix")

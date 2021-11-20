"""
Test class MBadge.
"""
# Import third-party modules
from examples.badge_example import BadgeExample
import pytest

# Import local modules
from dayu_widgets.badge import MBadge
from dayu_widgets.qt import QLabel
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget


class TestAlertExample(object):
    @pytest.fixture(autouse=True)
    def set_up(self, qtbot):
        """Set up to test the view."""
        # We need to initialize this here because pytest won't let us use an
        # __init__ constructor. If we did, the tests won't run.
        self.view = (
            BadgeExample()
        )  # noqa: E501 pylint: disable=attribute-defined-outside-init, line-too-long
        qtbot.addWidget(self.view)

    def test_badge_dot(self, qtbot):
        """Test MBadge init."""
        assert self.view.badge_1.get_dayu_dot()
        assert self.view.badge_hot.get_dayu_text() == "hot"

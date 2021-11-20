# Import third-party modules
import pytest

# Import local modules
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.qt import QLabel
from dayu_widgets.qt import QPushButton


class TestProgressCircle:
    @pytest.fixture(autouse=True)
    def set_up(self, qtbot):
        """Set up to test the view."""
        # We need to initialize this here because pytest won't let us use an
        # __init__ constructor. If we did, the tests won't run.
        self.view = MProgressCircle()

        qtbot.addWidget(self.view)

    def test_progress_circle_init(self):
        self.view.setRange(0, 10)
        self.view.setValue(5)
        assert self.view.text() == "50%"

    @pytest.mark.parametrize("width, result", ((80, 80), (100, 100), (120, 120)))
    def test_progress_circle_width(self, qtbot, width, result):
        self.view.set_dayu_width(width)
        dashboard = MProgressCircle(dashboard=True)
        dashboard.set_dayu_width(width)
        qtbot.addWidget(dashboard)
        assert self.view.width() == result
        assert self.view.height() == result
        assert self.view.get_dayu_width() == result

        assert dashboard.width() == result
        assert dashboard.height() < result
        assert dashboard.get_dayu_width() == result

    @pytest.mark.parametrize(
        "color, result",
        (
                ("#f00", "#f00"),
                ("#fff", "#fff"),
        ),
    )
    def test_progress_circle_color(self, qtbot, color, result):
        self.view.set_dayu_color(color)
        assert self.view.get_dayu_color() == result
        self.view.set_dayu_color("#0f0")
        assert self.view.get_dayu_color() == "#0f0"
        self.view.setValue(20)
        assert self.view.text() == "20%"

    #
    def test_progress_circle_widget(self, qtbot):
        label = QLabel("text")
        self.view.set_widget(label)
        self.view.repaint()
        self.view.show()
        assert not self.view.isTextVisible()

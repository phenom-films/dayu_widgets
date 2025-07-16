# Import third-party modules
import pytest
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.progress_circle import MProgressCircle


def test_progress_circle_init(qtbot):
    circle = MProgressCircle()
    circle.setRange(0, 10)
    circle.setValue(5)
    qtbot.addWidget(circle)
    assert circle.text() == "50%"


@pytest.mark.parametrize("width, result", ((80, 80), (100, 100), (120, 120)))
def test_progress_circle_width(qtbot, width, result):
    circle = MProgressCircle()
    circle.set_dayu_width(width)
    dashboard = MProgressCircle(dashboard=True)
    dashboard.set_dayu_width(width)
    qtbot.addWidget(circle)
    qtbot.addWidget(dashboard)
    assert circle.width() == result
    assert circle.height() == result
    assert circle.get_dayu_width() == result

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
def test_progress_circle_color(qtbot, color, result):
    circle = MProgressCircle()
    circle.set_dayu_color(color)
    qtbot.addWidget(circle)
    circle.show()
    assert circle.get_dayu_color() == result
    circle.set_dayu_color("#0f0")
    assert circle.get_dayu_color() == "#0f0"
    circle.setValue(20)
    assert circle.text() == "20%"


def test_progress_circle_widget(qtbot):
    label = QtWidgets.QLabel("text")
    circle = MProgressCircle()
    circle.set_widget(label)
    qtbot.addWidget(circle)
    circle.show()
    circle.repaint()

    def check():
        assert not circle.isTextVisible()
        assert not circle._default_label.isVisible()
        assert label.isVisible()

    qtbot.waitUntil(check)


def test_progress_circle_class_method(qtbot):
    circle = MProgressCircle.dashboard()
    qtbot.addWidget(circle)
    assert circle.width() > circle.height()

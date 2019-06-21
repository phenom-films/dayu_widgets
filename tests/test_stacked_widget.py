"""Test MStackedWidget class"""
from dayu_widgets.stacked_widget import MStackedWidget
from dayu_widgets.qt import QLabel


def test_stacked_widget_init(qtbot):
    """Test MStackedWidget init"""
    stacked_widget = MStackedWidget()
    stacked_widget.addWidget(QLabel('test'))
    qtbot.addWidget(stacked_widget)
    stacked_widget.show()

    assert stacked_widget.currentIndex() == 0


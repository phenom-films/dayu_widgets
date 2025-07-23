"""Test MStackedWidget class"""

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.stacked_widget import MStackedWidget


def test_stacked_widget_init(qtbot):
    """Test MStackedWidget init"""
    stacked_widget = MStackedWidget()
    stacked_widget.addWidget(QtWidgets.QLabel("test"))
    qtbot.addWidget(stacked_widget)
    stacked_widget.show()

    assert stacked_widget.currentIndex() == 0

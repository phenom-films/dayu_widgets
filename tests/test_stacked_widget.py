"""Test MStackedWidget class"""
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from dayu_widgets.qt import QLabel
from dayu_widgets.stacked_widget import MStackedWidget


def test_stacked_widget_init(qtbot):
    """Test MStackedWidget init"""
    stacked_widget = MStackedWidget()
    stacked_widget.addWidget(QLabel("test"))
    qtbot.addWidget(stacked_widget)
    stacked_widget.show()

    assert stacked_widget.currentIndex() == 0

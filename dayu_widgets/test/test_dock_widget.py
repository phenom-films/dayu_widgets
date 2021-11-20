"""Test MDockWidget class"""
import pytest
from dayu_widgets.dock_widget import MDockWidget


@pytest.mark.parametrize("title", ("", "test"))
def test_dock_widget_init(qtbot, title):
    """Test MDockWidget init"""
    if title:
        dock_widget = MDockWidget(title)
    else:
        dock_widget = MDockWidget()

    qtbot.addWidget(dock_widget)
    dock_widget.show()
    assert dock_widget.widget() is None

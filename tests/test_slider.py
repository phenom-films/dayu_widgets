"""Test MSlider class"""
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from dayu_widgets.qt import Qt
from dayu_widgets.slider import MSlider
import pytest


@pytest.mark.parametrize("orient", (Qt.Horizontal, Qt.Vertical))
def test_slider_init(qtbot, orient):
    """Test MSlider init"""
    slider = MSlider(orientation=orient)
    slider.setValue(10)
    qtbot.addWidget(slider)
    slider.show()

    assert slider.value() == 10

    # test mouseMoveEvent, show the tooltip
    # qtbot.mouseMove(slider)  # mouse enter
    # qtbot.mousePress(slider, Qt.LeftButton)  # click
    # qtbot.mouseMove(slider)  # click

    # assert slider.toolTip() == '10'

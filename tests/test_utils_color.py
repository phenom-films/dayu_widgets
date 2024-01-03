"""
Test Color helper functions.
"""
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
import pytest

# Import local modules
from Qt import QtGui
from dayu_widgets import utils


@pytest.mark.parametrize(
    "color, alpha, result",
    (
        ("#ff0000", "20%", "rgba(255, 0, 0, 20%)"),
        ("#FF0000", "70%", "rgba(255, 0, 0, 70%)"),
        ("#00FF00", "40%", "rgba(0, 255, 0, 40%)"),
        ("#0a0a0a", "40%", "rgba(10, 10, 10, 40%)"),
        ("#aaa", "80%", "rgba(170, 170, 170, 80%)"),
        ("#009", "80%", "rgba(0, 0, 153, 80%)"),
        ("#ff", "80%", "rgba(0, 0, 0, 80%)"),  # wrong color format
        ("#0090", "80%", "rgba(0, 0, 0, 80%)"),  # wrong color format
    ),
)
def test_fade_color(color, alpha, result):
    """Test fade_color."""
    assert utils.fade_color(color, alpha) == result


@pytest.mark.parametrize(
    "color, index, result",
    (
        ("#f5222d", 1, "#fff1f0"),
        ("#f5222d", 2, "#ffccc7"),
        ("#f5222d", 3, "#ffa39e"),
        ("#f5222d", 4, "#ff7875"),
        ("#f5222d", 5, "#ff4d4f"),
        ("#f5222d", 6, "#f5222d"),
        ("#f5222d", 7, "#cf1322"),
        ("#f5222d", 8, "#a8071a"),
        ("#f5222d", 9, "#820014"),
        ("#f5222d", 10, "#5c0011"),
        ("#a0d911", 1, "#fcffe6"),
        ("#a0d911", 3, "#eaff8f"),
        ("#a0d911", 5, "#bae637"),
        ("#a0d911", 7, "#7cb305"),
        ("#a0d911", 9, "#3f6600"),
        ("#722ed1", 2, "#efdbff"),
        ("#722ed1", 4, "#b37feb"),
        ("#722ed1", 6, "#722ed1"),
        ("#722ed1", 8, "#391085"),
        ("#722ed1", 10, "#120338"),
        ("#ffb7b2", 8, "#b36b6c"),
    ),
)
def test_generate_color(color, index, result):
    """
    test data reference from https://ant.design/docs/spec/colors-cn
    """
    assert compile_color(utils.generate_color(color, index), result)


def compile_color(color1, color2):
    """
    There is some bias when calculate with float. Set margin of error to 0.01
    """
    delta = 0.01
    q_color_1 = QtGui.QColor(color1)
    q_color_2 = QtGui.QColor(color2)

    return (
        (abs(q_color_1.redF() - q_color_2.redF()) < delta)
        and (abs(q_color_1.greenF() - q_color_2.greenF()) < delta)
        and (abs(q_color_1.blueF() - q_color_2.blueF()) < delta)
    )

"""
Test MLoading and MLoadingWrapper class
"""
# Import third-party modules
import pytest
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3 import dayu_theme
from dayu_widgets3.loading import MLoading
from dayu_widgets3.loading import MLoadingWrapper


@pytest.mark.parametrize(
    "cls, size",
    (
        (MLoading.tiny, dayu_theme.tiny),
        (MLoading.small, dayu_theme.small),
        (MLoading.medium, dayu_theme.medium),
        (MLoading.large, dayu_theme.large),
        (MLoading.huge, dayu_theme.huge),
    ),
)
@pytest.mark.parametrize("color", (None, "#13c2c2"))
def test_loading_class_method(qtbot, cls, size, color):
    """Test for MLoading class methods"""
    if color:
        widget = cls(color=color)
    else:
        widget = cls()
    qtbot.addWidget(widget)

    assert widget.height() == size
    assert widget.width() == size
    pix = widget.pix
    assert pix is not None
    assert not pix.isNull()
    assert pix.width() == size
    assert pix.width() == size


def test_loading_wrapper(qtbot):
    """Test for MLoadingWrapper class methods"""
    label = QtWidgets.QLabel("test")
    label.setFixedSize(QtCore.QSize(100, 100))
    widget = MLoadingWrapper(label, loading=False)
    widget.show()
    qtbot.addWidget(widget)

    assert not widget._loading_widget.isVisible()
    assert not widget._mask_widget.isVisible()
    assert not widget.get_dayu_loading()

    widget.set_dayu_loading(True)

    def check_loading_visible():
        assert widget.get_dayu_loading()
        assert widget._loading_widget.isVisible()
        assert widget._mask_widget.isVisible()

    qtbot.waitUntil(check_loading_visible)

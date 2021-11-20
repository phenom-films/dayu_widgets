"""
Test class MDivider.
"""
# Import third-party modules
import pytest

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget
from dayu_widgets.qt import Qt


@pytest.mark.parametrize("text, visible_text", (("", False), ("test", True)))
@pytest.mark.parametrize(
    "orient, visible_orient",
    ((Qt.Horizontal, True), (Qt.Vertical, False)),
    ids=("h", "v"),
)
@pytest.mark.parametrize(
    "align", (Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter), ids=("l", "r", "c")
)
def test_divider_init(qtbot, text, visible_text, orient, visible_orient, align):
    """Test MDivider init."""
    divider = MDivider(text, orientation=orient, alignment=align)

    divider.show()

    assert divider._text_label.text() == text
    # when orient is vertical, hide the text_label and right_frame
    show = visible_orient and visible_text
    _asset_divider_perform(divider, show, align)
    qtbot.addWidget(divider)


@pytest.mark.parametrize("text, visible_text", (("", False), ("test", True)))
def test_divider_class_method(qtbot, text, visible_text):
    """Test MDivider class methods."""
    main_widget = QWidget()
    main_lay = QVBoxLayout()
    main_widget.setLayout(main_lay)

    divider_left = MDivider.left(text)
    divider_center = MDivider.center(text)
    divider_right = MDivider.right(text)
    divider_ver = MDivider.vertical()
    main_lay.addWidget(divider_left)
    main_lay.addWidget(divider_center)
    main_lay.addWidget(divider_right)
    main_lay.addWidget(divider_ver)
    qtbot.addWidget(main_widget)
    main_widget.show()

    _asset_divider_perform(divider_left, True and visible_text, Qt.AlignLeft)
    _asset_divider_perform(divider_right, True and visible_text, Qt.AlignRight)
    _asset_divider_perform(divider_center, True and visible_text, Qt.AlignCenter)
    _asset_divider_perform(divider_ver, False, Qt.AlignCenter)

    assert divider_left.get_dayu_text() == text
    assert divider_right.get_dayu_text() == text
    assert divider_center.get_dayu_text() == text
    assert divider_ver.get_dayu_text() == ""


def _asset_divider_perform(divider, show, align):
    assert divider._text_label.isVisible() == show
    assert divider._right_frame.isVisible() == show
    assert divider._main_lay.stretch(0) == MDivider._alignment_map.get(align)
    assert divider._main_lay.stretch(2) == (100 - MDivider._alignment_map.get(align))

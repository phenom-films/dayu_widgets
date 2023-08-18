"""Test MSwitch class"""
# Import third-party modules
import pytest

# Import local modules
from dayu_widgets3 import dayu_theme
from dayu_widgets3.switch import MSwitch


@pytest.mark.parametrize(
    "cls, size",
    (
        ("tiny", dayu_theme.tiny),
        ("small", dayu_theme.small),
        ("medium", dayu_theme.medium),
        ("large", dayu_theme.large),
        ("huge", dayu_theme.huge),
    ),
)
def test_switch_class_method(qtbot, cls, size):
    """test MSwitch class method"""
    switch = MSwitch()
    getattr(switch, cls)()
    switch.setChecked(True)
    qtbot.addWidget(switch)

    assert switch.get_dayu_size() == size
    assert switch.isChecked()
    switch.setChecked(False)
    assert not switch.isChecked()
    assert switch.minimumSizeHint().width() == int(size * 1.2)
    assert switch.minimumSizeHint().height() == int(size * 0.6)

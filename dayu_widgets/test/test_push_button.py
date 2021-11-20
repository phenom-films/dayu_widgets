"""Test MPushButton"""

import pytest
from dayu_widgets.push_button import MPushButton
from dayu_widgets import dayu_theme
from dayu_widgets.qt import MIcon

MPUSHBUTTON_TYPE_LIST = (
    MPushButton.DefaultType,
    MPushButton.PrimaryType,
    MPushButton.SuccessType,
    MPushButton.WarningType,
    MPushButton.DangerType,
)


@pytest.mark.parametrize("dayu_type", MPUSHBUTTON_TYPE_LIST)
@pytest.mark.parametrize(
    "dayu_size",
    (
        dayu_theme.huge,
        dayu_theme.large,
        dayu_theme.medium,
        dayu_theme.small,
        dayu_theme.tiny,
    ),
)
@pytest.mark.parametrize("icon", (None, "success_fill.svg"))
@pytest.mark.parametrize("text", ("test", ""))
def test_mpushbutton_init(qtbot, dayu_type, dayu_size, icon, text):
    """Test MPushButton set_dayu_size and set_dayu_type."""
    widget = MPushButton(icon=MIcon(icon) if icon else icon, text=text)
    widget.set_dayu_size(dayu_size)
    widget.set_dayu_type(dayu_type)
    qtbot.addWidget(widget)

    assert widget.property("dayu_type") == dayu_type
    assert widget.property("dayu_size") == dayu_size


@pytest.mark.parametrize(
    "attr, dayu_type",
    zip((None, "primary", "success", "warning", "danger"), MPUSHBUTTON_TYPE_LIST),
)
def test_chain_method(qtbot, attr, dayu_type):
    """Test MPushButton class methods."""
    widget = MPushButton()
    if attr:
        getattr(widget, attr)()
    # widget.set_dayu_type(dayu_type)
    qtbot.addWidget(widget)
    assert widget.property("dayu_type") == dayu_type
    assert widget.property("dayu_size") == dayu_theme.default_size


@pytest.mark.parametrize("input_type", ("infos", 3, None, {"name": "test"}))
def test_with_wrong_type(qtbot, input_type):
    """Test MPushButton set_dayu_type method with wrong arg. raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        widget = MPushButton()
        widget.set_dayu_type(input_type)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert (
        exception_msg == "Input argument 'value' should be one of "
        "default/primary/success/warning/danger string."
    )

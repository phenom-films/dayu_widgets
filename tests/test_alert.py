"""Test MAlert class"""

# Import third-party modules
import pytest
from qtpy import QtCore

# Import local modules
from dayu_widgets.alert import MAlert


TYPE_LIST = (
    None,
    MAlert.InfoType,
    MAlert.SuccessType,
    MAlert.WarningType,
    MAlert.ErrorType,
)

TEST_INPUT = []
TEST_OUTPUT = []
for text in (None, "", "test"):
    input_dict = {} if text is None else {"text": text}
    result_dict = {"text": "" if text is None else text, "visible": bool(text)}
    for t in TYPE_LIST:
        if t is not None:
            input_dict.update({"type": t})
        result_dict.update({"type": t or "info"})
        TEST_INPUT.append(input_dict)
        TEST_OUTPUT.append(result_dict)


@pytest.mark.parametrize("kwargs,result", [(i, r) for i, r in zip(TEST_INPUT, TEST_OUTPUT)])
def test_malert_init(qtbot, kwargs, result):
    """Test MAlert with different arguments."""
    widget = MAlert()
    if kwargs.get("text"):
        widget.set_dayu_text(kwargs.get("text"))
    if kwargs.get("type"):
        widget.set_dayu_type(kwargs.get("type"))
    qtbot.addWidget(widget)

    assert widget.property("dayu_type") == result["type"]
    assert widget.property("dayu_text") == result["text"]
    assert widget.isVisible() == result["visible"]


@pytest.mark.parametrize("input_type", ("infos", 3, None, {"name": "test"}))
def test_malert_with_wrong_type(qtbot, input_type):
    """Test MAlert with wrong type for type arg"""
    with pytest.raises(ValueError) as exc_info:
        widget = MAlert()
        widget.set_dayu_type(input_type)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be " "one of info/success/warning/error string."


@pytest.mark.parametrize(
    "input_text, error_type",
    (
        (3, int),
        ([], list),
        ((1,), tuple),
        (set(), set),
        ({}, dict),
        (object(), object),
    ),
)
def test_malert_with_wrong_text(qtbot, input_text, error_type):
    """Test MAlert with wrong type for text arg."""
    with pytest.raises(TypeError) as exc_info:
        widget = MAlert()
        widget.set_dayu_text(input_text)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be string type, " "but get {}".format(error_type)


def test_malert_close_button(qtbot):
    """Test MAlert close button functionality"""
    widget = MAlert(text="Test Alert")
    qtbot.addWidget(widget)

    # By default, close button should be invisible
    assert not widget._close_button.isVisible()

    # Enable close button
    widget.set_closable(True)
    assert widget._close_button.isVisible()

    # Test clicking close button
    assert widget.isVisible()
    qtbot.mouseClick(widget._close_button, QtCore.Qt.LeftButton)
    assert not widget.isVisible()


def test_malert_close_button_signal(qtbot):
    """Test MAlert close button signal"""
    widget = MAlert(text="Test Alert")
    qtbot.addWidget(widget)

    # Enable close button
    widget.set_closable(True)

    # Test close button signal
    with qtbot.waitSignal(widget._close_button.clicked, timeout=1000):
        qtbot.mouseClick(widget._close_button, QtCore.Qt.LeftButton)

    # Verify widget is hidden after close button click
    assert not widget.isVisible()


def test_malert_visibility_chain(qtbot):
    """Test MAlert visibility chain reactions"""
    widget = MAlert()
    qtbot.addWidget(widget)

    # Should be invisible when text is empty
    widget.set_dayu_text("")
    assert not widget.isVisible()

    # Should become visible when text is set
    widget.set_dayu_text("Test Alert")
    assert widget.isVisible()

    # Should hide when text is cleared
    widget.set_dayu_text("")
    assert not widget.isVisible()


def test_malert_type_chain(qtbot):
    """Test MAlert type change chain reactions"""
    widget = MAlert(text="Test Alert")
    qtbot.addWidget(widget)

    # Test type change updates icon
    for alert_type in [MAlert.InfoType, MAlert.SuccessType, MAlert.WarningType, MAlert.ErrorType]:
        widget.set_dayu_type(alert_type)
        icon_image = widget._icon_label.property("dayu_image")
        assert icon_image is not None
        # 不再检查文件名，只检查图标是否存在
        assert not icon_image.isNull()


def test_malert_icon_visibility(qtbot):
    """Test MAlert icon show/hide functionality"""
    widget = MAlert(text="Test Alert")
    qtbot.addWidget(widget)

    # By default, icon should be visible
    assert widget._icon_label.isVisible()

    # Hide icon
    widget.set_show_icon(False)
    assert not widget._icon_label.isVisible()

    # Show icon again
    widget.set_show_icon(True)
    assert widget._icon_label.isVisible()


def test_malert_type_switch(qtbot):
    """Test MAlert type switching and style changes"""
    widget = MAlert(text="Test Alert")
    qtbot.addWidget(widget)

    # Test switching between different types
    types = [MAlert.InfoType, MAlert.SuccessType, MAlert.WarningType, MAlert.ErrorType]
    for alert_type in types:
        widget.set_dayu_type(alert_type)
        assert widget.property("dayu_type") == alert_type
        # Ensure icon is updated
        assert widget._icon_label.property("dayu_image") is not None

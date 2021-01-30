"""Test MAlert class"""
import pytest

from dayu_widgets.alert import MAlert

TYPE_LIST = (None,
             MAlert.InfoType,
             MAlert.SuccessType,
             MAlert.WarningType,
             MAlert.ErrorType)

TEST_INPUT = []
TEST_OUTPUT = []
for text in (None, '', 'test'):
    input_dict = {} if text is None else {'text': text}
    result_dict = {'text': '' if text is None else text, 'visible': bool(text)}
    for t in TYPE_LIST:
        if t is not None:
            input_dict.update({'type': t})
        result_dict.update({'type': t or 'info'})
        TEST_INPUT.append(input_dict)
        TEST_OUTPUT.append(result_dict)


@pytest.mark.parametrize('kwargs,result', [
    (i, r) for i, r in zip(TEST_INPUT, TEST_OUTPUT)
])
def test_malert_init(qtbot, kwargs, result):
    """Test MAlert with different arguments."""
    widget = MAlert()
    if kwargs.get('text'):
        widget.set_dayu_text(kwargs.get('text'))
    if kwargs.get('type'):
        widget.set_dayu_type(kwargs.get('type'))
    qtbot.addWidget(widget)

    assert widget.property('dayu_type') == result['type']
    assert widget.property('dayu_text') == result['text']
    assert widget.isVisible() == result['visible']


@pytest.mark.parametrize('input_type', ('infos', 3, None, {'name': 'test'}))
def test_malert_with_wrong_type(qtbot, input_type):
    """Test MAlert with wrong type for type arg"""
    with pytest.raises(ValueError) as exc_info:
        widget = MAlert()
        widget.set_dayu_type(input_type)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be " \
                            "one of info/success/warning/error string."


@pytest.mark.parametrize('input_text, error_type', (
    (3, int),
    ([], list),
    ((1,), tuple),
    (set(), set),
    ({}, dict),
    (object(), object),
))
def test_malert_with_wrong_text(qtbot, input_text, error_type):
    """Test MAlert with wrong type for text arg."""
    with pytest.raises(TypeError) as exc_info:
        widget = MAlert()
        widget.set_dayu_text(input_text)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be string type, " \
                            "but get {}".format(error_type)

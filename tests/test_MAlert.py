from dayu_widgets.MAlert import MAlert
import pytest

type_list = (None,
             MAlert.InfoType,
             MAlert.SuccessType,
             MAlert.WarningType,
             MAlert.ErrorType)

test_input = []
test_result = []
for text in (None, '', 'test'):
    input_dict = {} if text is None else {'text': text}
    result_dict = {'text': '' if text is None else text, 'visible': bool(text)}
    for t in type_list:
        if t is not None:
            input_dict.update({'type': t})
        result_dict.update({'type': t or 'info'})
        test_input.append(input_dict)
        test_result.append(result_dict)


@pytest.mark.parametrize('kwargs,result', [
    (i, r) for i, r in zip(test_input, test_result)
])
def test_malert_init(qtbot, kwargs, result):
    widget = MAlert(**kwargs)
    qtbot.addWidget(widget)

    assert widget.property('type') == result['type']
    assert widget.property('text') == result['text']
    assert widget.isVisible() == result['visible']


@pytest.mark.parametrize('input_type', ('infos', 3, None, {'name': 'test'}))
def test_malert_with_wrong_type(qtbot, input_type):
    with pytest.raises(ValueError) as exc_info:
        widget = MAlert(type=input_type)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be one of info/success/warning/error string."


@pytest.mark.parametrize('input_text, error_type', (
        (3, 'int'),
        ([], 'list'),
        ((1,), 'tuple'),
        (set(), 'set'),
        ({}, 'dict'),
        (object(), 'object'),
))
def test_malert_with_wrong_text_type(qtbot, input_text, error_type):
    with pytest.raises(TypeError) as exc_info:
        widget = MAlert(text=input_text)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be string type, but get <type '{}'>".format(error_type)

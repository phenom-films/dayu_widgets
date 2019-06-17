"""
Test class MBadge.
"""
import pytest

from dayu_widgets.MBadge import MBadge
from dayu_widgets.qt import QLabel, QWidget, QVBoxLayout


@pytest.mark.parametrize('content,text,visible', (
    (1, '1', True),
    (100, '99+', True),
    (0, '0', False),
    (-1, '-1', True),  # when user set to -1, maybe is useful to show something special.
    ('hot', 'hot', True),
    ('', '', False),
    (True, '', True),
    (False, '', False),
))
def test_malert_init(qtbot, content, text, visible):
    """Test MAlert init."""
    label = QLabel('test')
    widget_1 = MBadge(widget=label, content=content)
    widget_2 = MBadge(content=content)
    main_widget = QWidget()
    main_lay = QVBoxLayout()
    main_widget.setLayout(main_lay)
    main_lay.addWidget(widget_1)
    main_lay.addWidget(widget_2)
    qtbot.addWidget(main_widget)
    main_widget.show()

    assert widget_1._badge_button.text() == text
    assert widget_1._badge_button.isVisible() == visible
    assert widget_2._badge_button.text() == text
    assert widget_2._badge_button.isVisible() == visible


@pytest.mark.parametrize('input_arg, error_type', (
    ([], 'list'),
    ((1,), 'tuple'),
    (set(), 'set'),
    ({}, 'dict'),
    (object(), 'object'),
))
def test_with_wrong_content_type(qtbot, input_arg, error_type):
    """Test MAlert.set_content method with wrong input type."""
    with pytest.raises(TypeError) as exc_info:
        widget = MBadge()
        widget.set_content(input_arg)
        widget.show()
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be int or bool or string type, " \
                            "but get <type '{}'>".format(error_type)

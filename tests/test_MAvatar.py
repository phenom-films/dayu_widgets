from dayu_widgets.MAvatar import MAvatar
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *
import pytest


@pytest.mark.parametrize('size,result', (
        (None, dayu_theme.default_size),
        (dayu_theme.default_size, dayu_theme.default_size),
        (dayu_theme.tiny, dayu_theme.tiny),
        (dayu_theme.small, dayu_theme.small),
        (dayu_theme.medium, dayu_theme.medium),
        (dayu_theme.large, dayu_theme.large),
        (dayu_theme.huge, dayu_theme.huge),
))
def test_mavatar_no_image(qtbot, size, result):
    widget = MAvatar(size=size)
    qtbot.addWidget(widget)

    assert widget.height() == result
    assert widget.width() == result
    pix = widget.pixmap()
    assert pix is not None
    assert not pix.isNull()
    assert pix.width() == result
    assert pix.width() == result

    orig = MPixmap('sphere.svg')
    widget.set_image(orig)
    pix = widget.pixmap()
    assert pix is not None
    assert not pix.isNull()
    assert pix.width() == result
    assert pix.width() == result


@pytest.mark.parametrize('size,result', (
        (None, dayu_theme.default_size),
        (dayu_theme.default_size, dayu_theme.default_size),
        (dayu_theme.tiny, dayu_theme.tiny),
        (dayu_theme.small, dayu_theme.small),
        (dayu_theme.medium, dayu_theme.medium),
        (dayu_theme.large, dayu_theme.large),
        (dayu_theme.huge, dayu_theme.huge),
))
def test_mavatar_with_image(qtbot, size, result):
    widget = MAvatar(size=size, image=MPixmap('check.svg'))
    qtbot.addWidget(widget)

    assert widget.height() == result
    assert widget.width() == result
    pix = widget.pixmap()
    assert pix is not None
    assert not pix.isNull()
    assert pix.width() == result
    assert pix.width() == result

    orig = MPixmap('sphere.svg')
    widget.set_image(orig)
    pix = widget.pixmap()
    assert pix is not None
    assert not pix.isNull()
    assert pix.width() == result
    assert pix.width() == result


@pytest.mark.parametrize('input_file, error_type', (
        ('3', 'str'),
        (3, 'int'),
        (set('google'), 'set'),
        ({'name': 'test'}, 'dict'),
        (['g'], 'list'),
        ((2,), 'tuple'),
        (object(), 'object'),
))
def test_mavatar_with_wrong_image(qtbot, input_file, error_type):
    """Make sure when user give a wrong type arg, raise TypeError"""
    with pytest.raises(TypeError) as exc_info:
        widget = MAvatar(image=input_file)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be QPixmap or None, but get <type '{}'>".format(error_type)

from dayu_widgets import MAbstractSpinBox
from dayu_widgets import dayu_theme
import pytest
import datetime


@pytest.mark.parametrize('size,result', (
        (None, dayu_theme.default_size),
        (dayu_theme.default_size, dayu_theme.default_size),
        (dayu_theme.tiny, dayu_theme.tiny),
        (dayu_theme.small, dayu_theme.small),
        (dayu_theme.medium, dayu_theme.medium),
        (dayu_theme.large, dayu_theme.large),
        (dayu_theme.huge, dayu_theme.huge),
))
def test_MSpinBox(qtbot, size, result):
    widget = MAbstractSpinBox.MSpinBox(size=size)
    qtbot.addWidget(widget)
    assert widget.property('dayu_size') == result


@pytest.mark.parametrize('size,result', (
        (None, dayu_theme.default_size),
        (dayu_theme.default_size, dayu_theme.default_size),
        (dayu_theme.tiny, dayu_theme.tiny),
        (dayu_theme.small, dayu_theme.small),
        (dayu_theme.medium, dayu_theme.medium),
        (dayu_theme.large, dayu_theme.large),
        (dayu_theme.huge, dayu_theme.huge),
))
def test_MDoubleSpinBox(qtbot, size, result):
    widget = MAbstractSpinBox.MDoubleSpinBox(size=size)
    qtbot.addWidget(widget)
    assert widget.property('dayu_size') == result


@pytest.mark.parametrize('size,result', (
        (None, dayu_theme.default_size),
        (dayu_theme.default_size, dayu_theme.default_size),
        (dayu_theme.tiny, dayu_theme.tiny),
        (dayu_theme.small, dayu_theme.small),
        (dayu_theme.medium, dayu_theme.medium),
        (dayu_theme.large, dayu_theme.large),
        (dayu_theme.huge, dayu_theme.huge),
))
def test_MDateTimeEdit(qtbot, size, result):
    widget = MAbstractSpinBox.MDateTimeEdit(size=size)
    qtbot.addWidget(widget)
    assert widget.property('dayu_size') == result

    now = datetime.datetime.now()
    widget_with_datetime = MAbstractSpinBox.MDateTimeEdit(now)
    qtbot.addWidget(widget_with_datetime)
    assert widget_with_datetime.property('dayu_size') == dayu_theme.default_size
    assert widget_with_datetime.dateTime() == now


@pytest.mark.parametrize('size,result', (
        (None, dayu_theme.default_size),
        (dayu_theme.default_size, dayu_theme.default_size),
        (dayu_theme.tiny, dayu_theme.tiny),
        (dayu_theme.small, dayu_theme.small),
        (dayu_theme.medium, dayu_theme.medium),
        (dayu_theme.large, dayu_theme.large),
        (dayu_theme.huge, dayu_theme.huge),
))
def test_MDateEdit(qtbot, size, result):
    widget = MAbstractSpinBox.MDateEdit(size=size)
    qtbot.addWidget(widget)
    assert widget.property('dayu_size') == result

    today = datetime.datetime.today()
    widget_with_date = MAbstractSpinBox.MDateEdit(today)
    qtbot.addWidget(widget_with_date)
    assert widget_with_date.property('dayu_size') == dayu_theme.default_size
    assert widget_with_date.date() == today


@pytest.mark.parametrize('size,result', (
        (None, dayu_theme.default_size),
        (dayu_theme.default_size, dayu_theme.default_size),
        (dayu_theme.tiny, dayu_theme.tiny),
        (dayu_theme.small, dayu_theme.small),
        (dayu_theme.medium, dayu_theme.medium),
        (dayu_theme.large, dayu_theme.large),
        (dayu_theme.huge, dayu_theme.huge),
))
def test_MTimeEdit(qtbot, size, result):
    widget = MAbstractSpinBox.MTimeEdit(size=size)
    qtbot.addWidget(widget)
    assert widget.property('dayu_size') == result

    today = datetime.datetime.today()
    widget_with_time = MAbstractSpinBox.MTimeEdit(today.time())
    qtbot.addWidget(widget_with_time)
    assert widget_with_time.property('dayu_size') == dayu_theme.default_size
    assert widget_with_time.time() == today.time()

"""Test class: MSpinBox MDoubleSpinBox MDateTimeEdit MDateEdit MTimeEdit"""
import datetime

import pytest

from dayu_widgets import MAbstractSpinBox
from dayu_widgets import dayu_theme


@pytest.mark.parametrize('size,result', (
    (None, dayu_theme.default_size),
    (dayu_theme.default_size, dayu_theme.default_size),
    (dayu_theme.tiny, dayu_theme.tiny),
    (dayu_theme.small, dayu_theme.small),
    (dayu_theme.medium, dayu_theme.medium),
    (dayu_theme.large, dayu_theme.large),
    (dayu_theme.huge, dayu_theme.huge),
))
class TestAbstractSpinBox(object):
    """
    Test subclasses of QAbstractSpinBox.
    Use same args for init
    """
    @staticmethod
    def test_mspinbox(qtbot, size, result):
        """Test MSpinBox"""
        widget = MAbstractSpinBox.MSpinBox(size=size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

    @staticmethod
    def test_mdoublespinbox(qtbot, size, result):
        """Test MDoubleSpinBox"""
        widget = MAbstractSpinBox.MDoubleSpinBox(size=size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

    @staticmethod
    def test_mdatetimeedit(qtbot, size, result):
        """Test MDateTimeEdit"""
        widget = MAbstractSpinBox.MDateTimeEdit(size=size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

        date_time_obj = datetime.datetime(2019, 1, 1)
        widget_with_datetime = MAbstractSpinBox.MDateTimeEdit(date_time_obj)
        qtbot.addWidget(widget_with_datetime)
        assert widget_with_datetime.property('dayu_size') == dayu_theme.default_size
        assert widget_with_datetime.dateTime() == date_time_obj

    @staticmethod
    def test_mdateedit(qtbot, size, result):
        """Test MDateEdit"""
        widget = MAbstractSpinBox.MDateEdit(size=size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

        date_time_obj = datetime.datetime(2019, 1, 1)
        widget_with_date = MAbstractSpinBox.MDateEdit(date_time_obj)
        qtbot.addWidget(widget_with_date)
        assert widget_with_date.property('dayu_size') == dayu_theme.default_size
        assert widget_with_date.date() == date_time_obj

    @staticmethod
    def test_mtimeedit(qtbot, size, result):
        """Test MTimeEdit"""
        widget = MAbstractSpinBox.MTimeEdit(size=size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

        date_time_obj = datetime.datetime(2019, 1, 1)
        widget_with_time = MAbstractSpinBox.MTimeEdit(date_time_obj.time())
        qtbot.addWidget(widget_with_time)
        assert widget_with_time.property('dayu_size') == dayu_theme.default_size
        assert widget_with_time.time() == date_time_obj.time()

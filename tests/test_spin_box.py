"""Test class: MSpinBox MDoubleSpinBox MDateTimeEdit MDateEdit MTimeEdit"""
import datetime

import pytest

from dayu_widgets import spin_box
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
        widget = spin_box.MSpinBox()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

    @staticmethod
    def test_mdoublespinbox(qtbot, size, result):
        """Test MDoubleSpinBox"""
        widget = spin_box.MDoubleSpinBox()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

    @staticmethod
    def test_mdatetimeedit(qtbot, size, result):
        """Test MDateTimeEdit"""
        widget = spin_box.MDateTimeEdit()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

        date_time_obj = datetime.datetime(2019, 1, 1)
        widget_with_datetime = spin_box.MDateTimeEdit(date_time_obj)
        qtbot.addWidget(widget_with_datetime)
        assert widget_with_datetime.property('dayu_size') == dayu_theme.default_size
        assert widget_with_datetime.dateTime() == date_time_obj

    @staticmethod
    def test_mdateedit(qtbot, size, result):
        """Test MDateEdit"""
        widget = spin_box.MDateEdit()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

        date_time_obj = datetime.datetime(2019, 1, 1)
        widget_with_date = spin_box.MDateEdit(date_time_obj)
        qtbot.addWidget(widget_with_date)
        assert widget_with_date.property('dayu_size') == dayu_theme.default_size
        assert widget_with_date.date() == date_time_obj

    @staticmethod
    def test_mtimeedit(qtbot, size, result):
        """Test MTimeEdit"""
        widget = spin_box.MTimeEdit()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property('dayu_size') == result

        date_time_obj = datetime.datetime(2019, 1, 1)
        widget_with_time = spin_box.MTimeEdit(date_time_obj.time())
        qtbot.addWidget(widget_with_time)
        assert widget_with_time.property('dayu_size') == dayu_theme.default_size
        assert widget_with_time.time() == date_time_obj.time()

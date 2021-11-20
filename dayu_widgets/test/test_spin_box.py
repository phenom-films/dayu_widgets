"""Test class: MSpinBox MDoubleSpinBox MDateTimeEdit MDateEdit MTimeEdit"""
import datetime

import pytest

from dayu_widgets import spin_box
from dayu_widgets import dayu_theme


@pytest.mark.parametrize(
    "size,attr, result",
    (
        (None, None, dayu_theme.default_size),
        (dayu_theme.default_size, None, dayu_theme.default_size),
        (dayu_theme.tiny, "tiny", dayu_theme.tiny),
        (dayu_theme.small, "small", dayu_theme.small),
        (dayu_theme.medium, "medium", dayu_theme.medium),
        (dayu_theme.large, "large", dayu_theme.large),
        (dayu_theme.huge, "huge", dayu_theme.huge),
    ),
)
class TestAbstractSpinBox(object):
    """
    Test subclasses of QAbstractSpinBox.
    Use same args for init
    """

    @staticmethod
    def test_mspinbox(qtbot, size, attr, result):
        """Test MSpinBox"""
        widget = spin_box.MSpinBox()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property("dayu_size") == result

        widget_2 = spin_box.MSpinBox()
        if attr:
            getattr(widget_2, attr)()
        qtbot.addWidget(widget_2)
        assert widget_2.property("dayu_size") == result

    @staticmethod
    def test_mdoublespinbox(qtbot, size, attr, result):
        """Test MDoubleSpinBox"""
        widget = spin_box.MDoubleSpinBox()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property("dayu_size") == result

        widget_2 = spin_box.MDoubleSpinBox()
        if attr:
            getattr(widget_2, attr)()
        qtbot.addWidget(widget_2)
        assert widget_2.property("dayu_size") == result

    @staticmethod
    def test_mdatetimeedit(qtbot, size, attr, result):
        """Test MDateTimeEdit"""
        widget = spin_box.MDateTimeEdit()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property("dayu_size") == result

        widget_2 = spin_box.MDateTimeEdit()
        if attr:
            getattr(widget_2, attr)()
        qtbot.addWidget(widget_2)
        assert widget_2.property("dayu_size") == result

        date_time_obj = datetime.datetime(2019, 1, 1)
        widget_with_datetime = spin_box.MDateTimeEdit(date_time_obj)
        qtbot.addWidget(widget_with_datetime)
        assert widget_with_datetime.property("dayu_size") == dayu_theme.default_size
        assert widget_with_datetime.dateTime() == date_time_obj

    @staticmethod
    def test_mdateedit(qtbot, size, attr, result):
        """Test MDateEdit"""
        widget = spin_box.MDateEdit()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property("dayu_size") == result

        widget_2 = spin_box.MDateEdit()
        if attr:
            getattr(widget_2, attr)()
        qtbot.addWidget(widget_2)
        assert widget_2.property("dayu_size") == result

        date_time_obj = datetime.datetime(2019, 1, 1)
        widget_with_date = spin_box.MDateEdit(date_time_obj)
        qtbot.addWidget(widget_with_date)
        assert widget_with_date.property("dayu_size") == dayu_theme.default_size
        assert widget_with_date.date() == date_time_obj

    @staticmethod
    def test_mtimeedit(qtbot, size, attr, result):
        """Test MTimeEdit"""
        widget = spin_box.MTimeEdit()
        if size:
            widget.set_dayu_size(size)
        qtbot.addWidget(widget)
        assert widget.property("dayu_size") == result

        widget_2 = spin_box.MTimeEdit()
        if attr:
            getattr(widget_2, attr)()
        qtbot.addWidget(widget_2)
        assert widget_2.property("dayu_size") == result

        time_obj = datetime.datetime(2019, 1, 1).time()
        widget_with_time = spin_box.MTimeEdit(time_obj)
        qtbot.addWidget(widget_with_time)
        assert widget_with_time.property("dayu_size") == dayu_theme.default_size
        assert widget_with_time.time() == time_obj

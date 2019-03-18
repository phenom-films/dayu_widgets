#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MLabel import MLabel
from dayu_widgets.qt import *
from dayu_widgets.MTheme import global_theme
from dayu_widgets.qt import *
from dayu_widgets import STATIC_FOLDERS

qss = '''
#qt_calendar_calendarview {{
    background: {background};
    {text_font}
}}

#qt_calendar_navigationbar {{
    background: {background_selected};
}}

QToolButton {{
    icon-size: 18px, 18px;
    width: 20px;
    height: 20px;
}}

QToolButton#qt_calendar_prevmonth {{
    qproperty-icon: url(left_fill.svg);
}}

QToolButton#qt_calendar_nextmonth {{
    qproperty-icon: url(right_fill.svg);
}}

QToolButton#qt_calendar_monthbutton {{
    {text_font}
    padding-right: 20px;
}}

QToolButton#qt_calendar_yearbutton {{
    {text_font}
    padding-right: 20px;
}}

QToolButton#qt_calendar_monthbutton::menu-indicator {{
    subcontrol-origin: padding;
    subcontrol-position: center right;
    right: 0;
    width: 10px;
}}

QAbstractItemView {{
    color: black;
    selection-color: white;
    selection-background-color: {primary};
}}
QAbstractSpinBox {{
    spacing: 4px;
    {text_font}
    {font_family}
}}
QAbstractSpinBox{{
    {text_font}
    border: 1px solid {border};
    border-radius: 3px;
}}

QAbstractSpinBox:focus{{
    border: 1px solid {primary};
}}

QAbstractSpinBox::up-button {{
    subcontrol-origin: border;
    subcontrol-position: top right;
    margin-top: 1px;
    margin-right: 1px;
    border-left: 1px solid {border};
}}

QAbstractSpinBox::up-button:hover {{
    border-left: 1px solid {primary};
}}

QAbstractSpinBox::up-arrow {{
    image: url(up_line.svg);
}}
QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {{
    background-color: {disabled};
}}

QAbstractSpinBox::down-button {{
    subcontrol-origin: border;
    subcontrol-position: bottom right; /* position at bottom right corner */
    margin-bottom: 1px;
    margin-right: 1px;
    border-left: 1px solid {border};
    border-top: 1px solid {border};
}}

QAbstractSpinBox::down-button:hover {{
    border-left: 1px solid {primary};
}}

QAbstractSpinBox::down-arrow {{
    image: url(down_line.svg);
}}

QAbstractSpinBox::down-arrow:disabled,
QAbstractSpinBox::down-arrow:off {{
    background-color: {disabled};
}}


QAbstractSpinBox[line_size=default]{{
    min-height: {default_size}px;
    max-height: {default_size}px;
}}
QAbstractSpinBox[line_size=large]{{
    font-size: 16px;
    border-radius: 4px;
    min-height: {large_size}px;
    max-height: {large_size}px;
}}
QAbstractSpinBox[line_size=small]{{
    border-radius: 2px;
    min-height: {small_size}px;
    max-height: {small_size}px;
}}

QAbstractSpinBox[line_size=large]::up-button {{
    width: 26px;
}}
QAbstractSpinBox[line_size=default]::up-button {{
    width: 24px;
}}
QAbstractSpinBox[line_size=small]::up-button {{
    width: 20px;
}}

QAbstractSpinBox[line_size=large]::up-arrow {{
    width: 12px;
    height: 12px;
}}
QAbstractSpinBox[line_size=default]::up-arrow {{
    width: 10px;
    height: 10px;
}}
QAbstractSpinBox[line_size=small]::up-arrow {{
    width: 8px;
    height: 8px;
}}

QAbstractSpinBox[line_size=large]::down-button {{
    width: 26px;
}}
QAbstractSpinBox[line_size=default]::down-button {{
    width: 24px;
}}
QAbstractSpinBox[line_size=small]::down-button {{
    width: 20px;
}}

QAbstractSpinBox[line_size=large]::down-arrow {{
    width: 12px;
    height: 12px;
}}
QAbstractSpinBox[line_size=default]::down-arrow {{
    width: 10px;
    height: 10px;
}}
QAbstractSpinBox[line_size=small]::down-arrow {{
    width: 8px;
    height: 8px;
}}

QAbstractSpinBox::drop-down {{
    subcontrol-origin: border;
    subcontrol-position: center right;
    image: url(down_line.svg);
}}
QAbstractSpinBox[line_size=large]::drop-down{{
    right: 6px;
    height: 20px;
    width: 20px;
}}
QAbstractSpinBox[line_size=default]::drop-down{{
    right: 5px;
    height: 20px;
    width: 20px;
}}
QAbstractSpinBox[line_size=small]::drop-down{{
    right: 4px;
    height: 18px;
    width: 18px;
}}

'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


class MCalendarWidgetTest(QWidget):
    def __init__(self, parent=None):
        super(MCalendarWidgetTest, self).__init__(parent)
        self.setStyleSheet(qss)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        date_edit_large = QDateEdit()
        date_edit_large.setProperty('line_size', MView.LargeSize)
        date_edit_large.setCalendarPopup(True)
        date_edit_default = QDateEdit()
        date_edit_default.setProperty('line_size', MView.DefaultSize)
        date_edit_default.setCalendarPopup(True)
        date_edit_small = QDateEdit()
        date_edit_small.setProperty('line_size', MView.SmallSize)
        date_edit_small.setCalendarPopup(True)

        time_edit_large = QTimeEdit()
        time_edit_large.setProperty('line_size', MView.LargeSize)
        time_edit_default = QTimeEdit()
        time_edit_default.setProperty('line_size', MView.DefaultSize)
        time_edit_small = QTimeEdit()
        time_edit_small.setProperty('line_size', MView.SmallSize)

        lay_date = QHBoxLayout()
        lay_date.addWidget(date_edit_large)
        lay_date.addWidget(date_edit_default)
        lay_date.addWidget(date_edit_small)

        lay_time = QHBoxLayout()
        lay_time.addWidget(time_edit_large)
        lay_time.addWidget(time_edit_default)
        lay_time.addWidget(time_edit_small)

        main_lay.addLayout(lay_date)
        main_lay.addLayout(lay_time)

        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_prefix_button_clicked(self):
        print 'prefix button clicked'


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MCalendarWidgetTest()
    test.show()
    sys.exit(app.exec_())

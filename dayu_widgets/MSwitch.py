#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import STATIC_FOLDERS
from dayu_widgets.MTheme import global_theme
from dayu_widgets.qt import *

qss = '''
QRadioButton{{
    spacing: -20px;

}}
QRadioButton::indicator{{
    subcontrol-origin: border;
    subcontrol-position: center left;
    image: url(sphere.svg);
}}
QRadioButton[line_size=large]::indicator{{
    width: 48px;
    height: 24px;
    border-radius: 12px;
}}
QRadioButton[line_size=default]::indicator{{
    width: 38px;
    height: 19px;
    border-radius: 9px;
}}
QRadioButton[line_size=small]::indicator{{
    width: 28px;
    height: 14px;
    border-radius: 7px;
}}
QRadioButton::indicator:checked{{
    image-position: center right;
    background-color: {primary};
}}
QRadioButton::indicator:unchecked{{
    image-position: center left;
    background-color: {background_dark};
}}
QRadioButton::indicator:disabled{{
    background-color: {disabled};
}}
'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


@property_mixin
class MSwitch(QWidget):
    '''
    自定义 props:
        checked
    '''
    sig_checked_changed = Signal(bool)

    def __init__(self, size=None, parent=None):
        super(MSwitch, self).__init__(parent)
        self.setProperty('line_size', size or MView.DefaultSize)
        self.radio = QRadioButton()
        self.radio.setProperty('line_size', size or MView.DefaultSize)
        self.radio.toggled.connect(self.set_checked)
        self.radio.toggled.connect(self.sig_checked_changed)
        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.addWidget(self.radio)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setLayout(main_lay)
        self.setStyleSheet(qss)

    def minimumSizeHint(self, *args, **kwargs):
        height = global_theme.get(self.property('line_size') + '_size') * 1.2
        return QSize(height, height / 2)

    def _set_checked(self, value):
        if value != self.radio.isChecked():
            # 更新来自代码
            self.radio.setChecked(value)
            self.sig_checked_changed.emit(value)
        self.style().polish(self)

    def set_checked(self, flag):
        self.setProperty('checked', flag)

    def enterEvent(self, *args, **kwargs):
        QApplication.setOverrideCursor(Qt.PointingHandCursor if self.isEnabled() else Qt.ForbiddenCursor)
        return super(MSwitch, self).enterEvent(*args, **kwargs)

    def leaveEvent(self, *args, **kwargs):
        QApplication.restoreOverrideCursor()
        return super(MSwitch, self).leaveEvent(*args, **kwargs)

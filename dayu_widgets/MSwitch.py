#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import STATIC_FOLDERS
from dayu_widgets.MTheme import global_theme
from dayu_widgets.mixin import property_mixin, cursor_mixin
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
@cursor_mixin
class MSwitch(QRadioButton):
    def __init__(self, size=None, parent=None):
        super(MSwitch, self).__init__(parent)
        self.setProperty('line_size', size or MView.DefaultSize)
        self.setAutoExclusive(False)
        self.setStyleSheet(qss)

    def minimumSizeHint(self, *args, **kwargs):
        height = global_theme.get(self.property('line_size') + '_size') * 1.2
        return QSize(height, height / 2)
